"""The ledger: which Lean declarations get an entry, in which volume and chapter, and how many are written.

The spine of the proof (records/spine/spine.jsonl.gz of tamnd/riemann) has one row for each declaration that
riemannHypothesis depends on, with its immediate dominator `idom` and the size of the subtree that it dominates.
Each declaration of the spine is in the dominated subtree of exactly one planned entry: its nearest planned
ancestor. So when every planned entry is written, every declaration of the spine is inside the proof of a written
entry.

Planned entries are the declarations with a dominated subtree of at least `--min` declarations (tier 1: 1000,
tier 2: 300, tier 3: 100). The eight trunk declarations are in Volume 2. A declaration in one of the eight named
branches of the spine goes to the volume of its branch; any other goes to the volume of its Lean folder. In a
volume the chapter is the Lean folder of the declaration, and the entries of a chapter come in the order of a walk
of the dominator tree from the top, larger subtrees first.

    python -m rhb ledger --records /tmp/rr/records --min 1000 [--write]

--write writes ledger/outline.yaml, ledger/coverage.md and the volume.yaml of each development volume.
"""

from __future__ import annotations

import collections
import gzip
import json
import os
import re

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GAL = "UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter"
VWIN = "UpperTheory.One.vwin_of_row"
COVOL = "SelfIntersectionVolumeEstimates.topCovolSlim2_use_alt_alt"
THETA = "UpperTheory.LiteratureTheorems.theta_integrals_agree_and_local_matching_of_literature"
GREEN = "UpperTheory.Top.every_character_of_green_v_win"
HYPS = "GlobalTheory.Fc.S0.StageU.hypotheses_nonempty_of_unramified_exponents_alt"
ONTO = "GlobalTheory.Fc.S0.ontoX_and_lamLow_of_unitaryGroupHypotheses'"
OPEN0 = "GlobalTheory.T.open0_of_unitary_group_hypotheses"

# number, id, title, summary, the branches (layers) or the Lean folders that make it
VOLUMES = [
    (3, "galois-row", "The Galois row",
     "The proof of the row hypothesis: Galois representations attached to theta lifts, their geometric "
     "realization in weight one, and the local-global compatibility that the trunk needs.", [GAL], []),
    (4, "window-bound", "The window bound",
     "The proof of VWin from the row hypothesis: automorphy, descent and vanishing, and the bound on "
     "Tate-Shafarevich groups over the fields that a character cuts out.", [VWIN], []),
    (5, "volume-estimates", "Volume estimates and positivity",
     "The covolume bound of the literature layer: towers of good reduction, self-intersection volumes and the "
     "positivity statement of Arakelov geometry.", [COVOL], []),
    (6, "theta-integrals", "Theta integrals and the green window",
     "The two branches of the theta chapter: the agreement of theta integrals with local matching, and the short "
     "branch that ends in the nonvanishing of L-functions.", [THETA, GREEN], []),
    (7, "unitary-hypotheses", "The unitary hypotheses",
     "The three large branches below the record HypsAlt: unramified exponents, the map onto X with the low "
     "lambda bound, and the open orbit.", [HYPS, ONTO, OPEN0], []),
    (8, "automorphic-arithmetic", "Automorphic arithmetic",
     "The shared results of the folder AutomorphicArithmetic: theta correspondence, automorphic varieties and "
     "their foundations.", [], ["Development.AutomorphicArithmetic"]),
    (9, "abelian-varieties", "Abelian varieties",
     "The shared results on abelian varieties: their definitions, block theory, the published theorems and "
     "their proofs.", [], ["Development.AbelianVarietyTheory"]),
    (10, "development", "The Weil bound, the spectrum and resolution",
     "The other shared folders of the development: the Weil bound, the automorphic spectrum, discrete groups "
     "and the resolution of singularities.", [], ["Development"]),
    (11, "formalism", "The formalism",
     "Local to global arguments, Hermitian curvature, sharp restriction, period integrals and the other folders "
     "of Formalism.", [], ["Formalism"]),
    (12, "ground-theory", "Ground theory",
     "Global and local fields, automorphic forms, heights and theta, profinite cohomology, reductive groups and "
     "the companion theories.", [], ["GroundTheory", "ReciprocityTheory", "CompanionTheory", "PositivityTheory",
                                     "Lemmata", "Supplements", "Statements", "Main", "BuildAid"]),
]


def load_spine(records: str) -> list[dict]:
    """The rows of the spine, one for each name. A name can have two rows (3,678 of them do); keep the larger."""
    best = {}
    with gzip.open(os.path.join(records, "spine", "spine.jsonl.gz"), "rt") as f:
        for line in f:
            r = json.loads(line)
            if r["name"] not in best or r["size"] > best[r["name"]]["size"]:
                best[r["name"]] = r
    return list(best.values())


def slug(name: str) -> str:
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", name.replace("'", "-prime"))
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower()
    return s


def folder_title(folder: str) -> str:
    """ThetaCorrespondence → Theta correspondence; GL3MeanSquares → GL3 mean squares."""
    last = folder.split(".")[-1]
    words = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1 \2", last)).split()
    words = [w if (w.isupper() or any(ch.isdigit() for ch in w)) and len(w) > 1 else w.lower() for w in words]
    t = " ".join(words)
    return t[:1].upper() + t[1:]


def plan(rows: list[dict], minsize: int) -> dict:
    by = {r["name"]: r for r in rows}
    kids = collections.defaultdict(list)
    for r in rows:
        if r["idom"]:
            kids[r["idom"]].append(r["name"])
    trunk = [r["name"] for r in rows if r.get("layer") == "trunk"]
    # the walk from the top, larger subtrees first: the reading order
    order, stack = {}, ["riemannHypothesis"]
    while stack:
        n = stack.pop()
        if n in order:
            continue
        order[n] = len(order)
        stack.extend(sorted(kids[n], key=lambda c: by[c]["size"]))
    layer_vol = {}
    for num, vid, title, summ, layers, folders in VOLUMES:
        for la in layers:
            layer_vol[la] = num
    folder_vols = sorted(((f, v[0]) for v in VOLUMES for f in v[5]), key=lambda x: -len(x[0]))

    def volume_of(r: dict) -> int:
        if r["name"] in trunk:
            return 2
        if r.get("layer") in layer_vol:
            return layer_vol[r["layer"]]
        m = r["module"]
        for f, v in folder_vols:
            if m == f or m.startswith(f + "."):
                return v
        return 12

    planned = [r for r in rows if r["size"] >= minsize]
    vols = collections.defaultdict(list)
    for r in planned:
        vols[volume_of(r)].append(r)
    out = {}
    for num, vid, title, summ, layers, folders in VOLUMES:
        entries = vols.get(num, [])
        # chapters: the Lean folder at depth 4, merged up while a chapter has fewer than 4 entries
        depth = {r["name"]: 4 for r in entries}

        def key(r):
            parts = r["module"].split(".")[:-1] or r["module"].split(".")
            return ".".join(parts[:depth[r["name"]]])
        for _ in range(3):
            cnt = collections.Counter(key(r) for r in entries)
            changed = False
            for r in entries:
                if cnt[key(r)] < 4 and depth[r["name"]] > 2:
                    depth[r["name"]] -= 1
                    changed = True
            if not changed:
                break
        chapters = collections.defaultdict(list)
        for r in entries:
            chapters[key(r)].append(r)
        chs = []
        far = len(order)
        for folder, es in sorted(chapters.items(), key=lambda kv: min(order.get(r["name"], far) for r in kv[1])):
            es.sort(key=lambda r: order.get(r["name"], far))
            chs.append({"id": slug(folder.split(".")[-1]) or "top", "folder": folder, "title": folder_title(folder),
                        "entries": [{"name": r["name"], "id": slug(r["name"]), "kind": r["kind"],
                                     "module": r["module"], "size": r["size"], "fanin": r.get("fanin", 0),
                                     "idom": r["idom"],
                                     "tier": 1 if r["size"] >= 1000 else 2 if r["size"] >= 300 else 3}
                                    for r in es]})
        # chapter ids unique in a volume
        seen = collections.Counter()
        for c in chs:
            seen[c["id"]] += 1
            if seen[c["id"]] > 1:
                c["id"] += f"-{seen[c['id']]}"
        out[num] = {"number": num, "id": vid, "title": title, "summary": summ,
                    "declarations": sum(by[la]["size"] for la in layers if la in by) if layers else None,
                    "chapters": chs}
    return {"min": minsize, "spine": len(rows), "trunk": trunk, "volumes": out, "_by": by, "_kids": kids}


def written_names(book) -> set[str]:
    names = set()
    for decl in book.labels.by_decl:
        names.add(decl)
    return names


def _is_written(name: str, written: set[str]) -> bool:
    if name in written:
        return True
    return any(name.endswith("." + w) or w.endswith("." + name) for w in written)


def coverage(p: dict, written: set[str]) -> dict:
    """The declarations of the spine whose nearest planned ancestor is written (the trunk counts as planned)."""
    by = p["_by"]
    planned = {e["name"] for v in p["volumes"].values() for c in v["chapters"] for e in c["entries"]}
    planned |= set(p["trunk"])
    done = {n for n in planned if _is_written(n, written)}
    covered = by_trunk = 0
    trunk = set(p["trunk"])
    memo = {}
    for n in by:
        chain, x = [], n
        while x and x not in memo and x not in planned:
            chain.append(x)
            x = by[x]["idom"] if x in by else ""
        owner = memo.get(x, x) if x else ""
        for c in chain:
            memo[c] = owner
        memo[n] = owner
        if owner in trunk and n not in trunk:
            by_trunk += 1          # a small shared subtree right under the trunk: lower tiers must explain it
        elif owner in done:
            covered += 1
    return {"planned": len(planned), "written": len(done), "covered": covered, "by_trunk": by_trunk,
            "spine": len(by)}


def run(book, args) -> int:
    rows = load_spine(args.records)
    p = plan(rows, args.min)
    written = written_names(book)
    cov = coverage(p, written)
    lines = [f"# Coverage of the spine (entries for subtrees of {args.min} or more declarations)", "",
             f"Planned entries {cov['planned']:,} (with the 8 trunk declarations of Volume 2), written "
             f"{cov['written']:,}.", "",
             f"Of the {cov['spine']:,} declarations of the spine, {cov['covered']:,} "
             f"({100 * cov['covered'] / cov['spine']:.1f}%) are in the subtree of a written entry below the trunk. "
             f"Another {cov['by_trunk']:,} ({100 * cov['by_trunk'] / cov['spine']:.1f}%) are in small shared subtrees "
             f"that hang right under the trunk: no entry of this tier explains them, and the lower tiers must.", "",
             "| Volume | Title | Chapters | Planned | Written |", "|---|---|---|---|---|"]
    for num, v in sorted(p["volumes"].items()):
        n = sum(len(c["entries"]) for c in v["chapters"])
        w = sum(1 for c in v["chapters"] for e in c["entries"] if _is_written(e["name"], written))
        lines.append(f"| {num} | {v['title']} | {len(v['chapters'])} | {n} | {w} |")
    report = "\n".join(lines) + "\n"
    print(report)
    if args.write:
        os.makedirs(os.path.join(ROOT, "ledger"), exist_ok=True)
        clean = {k: v for k, v in p.items() if not k.startswith("_")}
        for v in clean["volumes"].values():
            for c in v["chapters"]:
                for e in c["entries"]:
                    e["written"] = _is_written(e["name"], written)
        with open(os.path.join(ROOT, "ledger", "outline.yaml"), "w") as f:
            yaml.safe_dump(clean, f, sort_keys=False, allow_unicode=True, width=200)
        open(os.path.join(ROOT, "ledger", "coverage.md"), "w").write(report)
        for num, v in sorted(p["volumes"].items()):
            d = os.path.join(ROOT, "content", "dev", f"{num:02d}-{v['id']}")
            os.makedirs(d, exist_ok=True)
            old = {}   # keep the chapter titles that a person edited
            if os.path.exists(os.path.join(d, "volume.yaml")):
                old = {c["id"]: c.get("title") for c in
                       (yaml.safe_load(open(os.path.join(d, "volume.yaml"))) or {}).get("chapters") or []}
            vy = {"title": v["title"], "summary": v["summary"],
                  "chapters": [{"id": c["id"], "title": old.get(c["id"]) or c["title"], "folder": c["folder"],
                                "entries": [e["id"] for e in c["entries"]]} for c in v["chapters"]]}
            with open(os.path.join(d, "volume.yaml"), "w") as f:
                f.write("# Written by `rhb ledger --write` from the spine. Edit titles here; the entry list follows "
                        "the spine.\n")
                yaml.safe_dump(vy, f, sort_keys=False, allow_unicode=True, width=200)
    return 0
