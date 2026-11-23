"""The ledger: which Lean declarations get an entry, in which volume and chapter, and how many are written.

The spine of the proof (records/spine/spine.jsonl.gz of tamnd/riemann) has one row for each declaration that
riemannHypothesis depends on, with its immediate dominator `idom` and the size of the subtree that it dominates.
Each declaration of the spine is in the dominated subtree of exactly one planned entry: its nearest planned
ancestor. So when every planned entry is written, every declaration of the spine is inside the proof of a written
entry.

Planned entries are the declarations with a dominated subtree of at least `--min` declarations (tier 1: 1000,
tier 2: 300, tier 3: 100). The eight trunk declarations are in Volume 2. The others first get an old chapter, as
the first plan had them: a declaration in one of the eight named branches of the spine goes to the old volume of
its branch, any other to the old volume of its Lean folder, and in an old volume the chapter is the Lean folder of
the declaration. Then ledger/structure.yaml puts each old chapter, or each piece of a split one, into a chapter of
Volumes 3 to 15, grouped by subject. The entries of a chapter come in the order of the walk of the dominator tree
from the top, larger subtrees first, one old chapter after the other.

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

# The first grouping of the entries: by the branch of the spine (layer) or else by the Lean folder, as
# (old volume number, the branches, the Lean folders). In an old volume the chapter is the Lean folder of the entry.
# It gives each entry its old chapter key `<old volume>/<chapter id>`, and ledger/structure.yaml maps these keys to
# the chapters of Volumes 3 to 15.
BRANCHES = [
    (3, [GAL], []),
    (4, [VWIN], []),
    (5, [COVOL], []),
    (6, [THETA, GREEN], []),
    (7, [HYPS, ONTO, OPEN0], []),
    (8, [], ["Development.AutomorphicArithmetic"]),
    (9, [], ["Development.AbelianVarietyTheory"]),
    (10, [], ["Development"]),
    (11, [], ["Formalism"]),
    (12, [], ["GroundTheory", "ReciprocityTheory", "CompanionTheory", "PositivityTheory", "Lemmata", "Supplements",
              "Statements", "Main", "BuildAid"]),
]

STRUCTURE = os.path.join(ROOT, "ledger", "structure.yaml")


def load_volumes(path: str = STRUCTURE) -> list[dict]:
    """The development volumes, from ledger/structure.yaml (key `volumes`): number, id, title, summary and the
    chapters, each with `from` (the old chapter keys it takes), and for an old chapter that is split, `roots` (the
    root declarations of the piece) or `folders` (its Lean subfolders)."""
    with open(path, encoding="utf-8") as f:
        return (yaml.safe_load(f) or {}).get("volumes") or []


VOLUMES = load_volumes() if os.path.exists(STRUCTURE) else []


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


def short_ids(names: list[str]) -> dict[str, str]:
    """An id for each name from the end of the name: the last part, and the parts before it only when two names
    would get the same id. The ids are made over all names of tier 3, so that they do not change when a tier is
    added."""
    out, k = {}, 1
    todo = list(names)
    while todo:
        cand = collections.defaultdict(list)
        for n in todo:
            parts = n.split(".")
            cand[slug(".".join(parts[-k:]))].append(n)
        todo = []
        for c, ns in cand.items():
            if len(ns) == 1 or k >= max(len(n.split(".")) for n in ns):
                for i, n in enumerate(ns):
                    out[n] = c if i == 0 else f"{c}-{i + 1}"
            else:
                todo.extend(ns)
        k += 1
    return out


def old_chapters(rows: list[dict], minsize: int, by: dict, order: dict) -> dict[str, dict]:
    """The planned entries in their old chapters, keyed `<old volume>/<chapter id>`: each with its Lean folder and
    its entries in reading order. The old volume is the branch of the spine of the entry, else its Lean folder; the
    chapter is the Lean folder at depth 4, merged up while a chapter has fewer than 4 entries."""
    trunk = {r["name"] for r in rows if r.get("layer") == "trunk"}
    layer_vol = {la: num for num, layers, folders in BRANCHES for la in layers}
    folder_vols = sorted(((f, num) for num, layers, folders in BRANCHES for f in folders), key=lambda x: -len(x[0]))

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

    vols = collections.defaultdict(list)
    for r in rows:
        if r["size"] >= minsize:
            vols[volume_of(r)].append(r)
    out = {}
    far = len(order)
    for num, layers, folders in BRANCHES:
        entries = vols.get(num, [])
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
        seen = collections.Counter()   # chapter ids unique in a volume
        for folder, es in sorted(chapters.items(), key=lambda kv: min(order.get(r["name"], far) for r in kv[1])):
            es.sort(key=lambda r: order.get(r["name"], far))
            cid = slug(folder.split(".")[-1]) or "top"
            seen[cid] += 1
            if seen[cid] > 1:
                cid += f"-{seen[cid]}"
            out[f"{num}/{cid}"] = {"folder": folder, "entries": es}
    return out


def split_chapter(key: str, old: dict, pieces: list[tuple]) -> tuple[dict, list[str]]:
    """Divide the entries of a split old chapter among the new chapters that take a piece of it. A piece names its
    root declarations (`roots`) or its Lean subfolders (`folders`). An entry goes to the piece of the nearest root
    on its chain of immediate dominators inside the old chapter, or to the piece of its subfolder. An entry under no
    named root goes to the piece that names none, or if every piece names some, to the piece with the most
    entries. Returns the new chapter of each entry and the names under no named root."""
    names = {r["name"]: r for r in old["entries"]}
    root_of, folder_of, plain = {}, {}, []
    for where, roots, folders in pieces:
        for n in roots or []:
            if n not in names:
                raise SystemExit(f"structure.yaml: {key}: the root {n} is not an entry of the old chapter")
            root_of[n] = where
        for f in folders or []:
            folder_of[f] = where
        if not roots and not folders:
            plain.append(where)
    if len(plain) > 1:
        raise SystemExit(f"structure.yaml: {key}: more than one piece names no root")
    out, rest = {}, []
    for r in old["entries"]:
        where = None
        if folder_of:
            m = r["module"]
            tail = m[len(old["folder"]) + 1:] if m.startswith(old["folder"] + ".") else ""
            where = folder_of.get(tail.split(".")[0])
        else:
            x = r
            while x is not None and where is None:
                where = root_of.get(x["name"])
                x = names.get(x["idom"])
        if where is None:
            rest.append(r["name"])
        out[r["name"]] = where
    if rest:
        if plain:
            fill = plain[0]
        else:
            fill = collections.Counter(w for w in out.values() if w).most_common(1)[0][0]
        for n in rest:
            out[n] = fill
    return out, rest


def plan(rows: list[dict], minsize: int) -> dict:
    """The planned entries in the volumes of ledger/structure.yaml. Each entry keeps its id; `from` is the key of
    its old chapter. In a new chapter the entries come in the order of the old chapters in `from`, and in an old
    chapter in the order of the walk."""
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
    ids = short_ids(sorted(r["name"] for r in rows if r["size"] >= min(100, minsize)))
    old = old_chapters(rows, minsize, by, order)
    vols = load_volumes()
    # who takes each old chapter: the new chapters (number, id) with the roots or folders of their piece
    takers = collections.defaultdict(list)
    for v in vols:
        for c in v["chapters"]:
            for k in c["from"]:
                takers[k].append(((v["number"], c["id"]), (c.get("roots") or {}).get(k),
                                  (c.get("folders") or {}).get(k)))
    missing = sorted(set(old) - set(takers))
    unknown = sorted(set(takers) - set(old))
    if missing or unknown:
        raise SystemExit(f"structure.yaml: old chapters with no new chapter {missing}; unknown keys {unknown}")
    home, fallback = {}, {}
    for k, ts in takers.items():
        if len(ts) == 1:
            for r in old[k]["entries"]:
                home[r["name"]] = ts[0][0]
        else:
            got, rest = split_chapter(k, old[k], ts)
            home.update(got)
            if rest:
                fallback[k] = rest
    out = {}
    for v in vols:
        chs = []
        for c in v["chapters"]:
            es = [(k, r) for k in c["from"] for r in old[k]["entries"] if home[r["name"]] == (v["number"], c["id"])]
            chs.append({"id": c["id"], "title": c["title"], "from": list(c["from"]),
                        "entries": [{"name": r["name"], "id": ids[r["name"]], "kind": r["kind"],
                                     "module": r["module"], "size": r["size"], "fanin": r.get("fanin", 0),
                                     "idom": r["idom"], "from": k,
                                     "tier": 1 if r["size"] >= 1000 else 2 if r["size"] >= 300 else 3}
                                    for k, r in es]})
        out[v["number"]] = {"number": v["number"], "id": v["id"], "title": v["title"], "summary": v["summary"],
                            "chapters": chs}
    placed = collections.Counter(e["name"] for v in out.values() for c in v["chapters"] for e in c["entries"])
    planned = sum(len(o["entries"]) for o in old.values())
    if sum(placed.values()) != planned or any(n > 1 for n in placed.values()):
        raise SystemExit(f"ledger: {sum(placed.values())} placements for {planned} entries")
    return {"min": minsize, "spine": len(rows), "trunk": trunk, "volumes": out, "_by": by, "_kids": kids,
            "_fallback": fallback}


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
    fb = p["_fallback"]
    if fb:
        lines += ["", f"Entries of a split old chapter under none of the named roots or folders, placed in the piece "
                      f"that names none: {sum(len(x) for x in fb.values())}, from "
                      + ", ".join(f"{k} ({len(x)})" for k, x in sorted(fb.items())) + "."]
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
            vy = {"number": num, "title": v["title"], "summary": v["summary"],
                  "chapters": [{"id": c["id"], "title": c["title"], "from": c["from"],
                                "entries": [e["id"] for e in c["entries"]]} for c in v["chapters"]]}
            with open(os.path.join(d, "volume.yaml"), "w") as f:
                f.write("# Written by `rhb ledger --write` from ledger/structure.yaml and the spine. Edit the titles "
                        "in ledger/structure.yaml.\n")
                yaml.safe_dump(vy, f, sort_keys=False, allow_unicode=True, width=200)
    return 0
