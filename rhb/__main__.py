"""rhb: build The Riemann Handbook from tamnd/riemann, tamnd/riemann-lean and the entries in content/.

    python -m rhb survey  [--riemann ../riemann] [--lean ../riemann-lean]
    python -m rhb check   [--volume N|all]
    python -m rhb build   [--volume N|all] [--formats tex,pdf,epub] [--out build]
    python -m rhb ledger  --records /tmp/rr/records [--min 1000] [--write]
"""

from __future__ import annotations

import argparse
import datetime
import glob
import json
import os
import re
import sys
import time

from .book import Book

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def edition() -> dict:
    """The file EDITION: 'version 0.1.0' and 'riemann <commit>'."""
    out = {"version": "0.1.0", "riemann": ""}
    p = os.path.join(ROOT, "EDITION")
    if os.path.exists(p):
        for line in open(p):
            k, _, v = line.strip().partition(" ")
            if k:
                out[k] = v.strip()
    return out


def load(args) -> Book:
    t = time.time()
    book = Book(os.path.abspath(args.riemann), os.path.abspath(args.lean), os.path.join(ROOT, "content"),
                edition().get("lean", "main"))
    print(f"riemann {book.r.commit()[:8]}, riemann-lean {book.lean_commit[:8]}: {len(book.r.paths)} Learn pages, "
          f"{len(book.r.chapters)} chapters, {len(book.r.steps)} steps, {len(book.dev)} development volumes, "
          f"loaded in {time.time() - t:.1f}s", file=sys.stderr)
    return book


def pick(book: Book, which: str):
    if which == "all":
        return list(book.volumes)
    nums = {int(x) for x in which.split(",")}
    return [v for v in book.volumes if v.number in nums]


def cmd_survey(args):
    book = load(args)
    for v in book.volumes:
        md, st = book.markdown(v)
        print(f"{v.number:>2} {v.title:<40} words {st['words']:>9,}  unresolved links {len(st['unresolved']):>4}")


BANNED = (r"\b(leverag(?:e|es|ed|ing)|showcas(?:e|es|ed|ing)|powerful|elegant(?:ly)?|seamless(?:ly)?|crucial(?:ly)?|"
          r"delv(?:e|es|ed|ing)|journey|landscape|tapestry|realm|intricate|pivotal|robust|underscores?|"
          r"notably|furthermore|moreover)\b")


def check_entries(book: Book) -> list[str]:
    """Problems in content/: entries with no front matter, no decl, no Lean name in the index, the words of
    the banned list, dashes, and missing sections."""
    probs = []
    for f in sorted(glob.glob(os.path.join(book.content, "**", "*.md"), recursive=True)):
        rel = os.path.relpath(f, book.content)
        t = open(f, encoding="utf-8").read()
        prose = re.sub(r"\$\$.*?\$\$|\$[^$\n]*\$|`[^`\n]*`|```.*?```", " ", t, flags=re.S)
        prose = re.sub(r"\]\([^)]*\)", "]", prose)
        for w in sorted(set(re.findall(BANNED, prose, flags=re.I))):
            probs.append(f"{rel}: style: '{w}'")
        if re.search("[–—]", prose):
            probs.append(f"{rel}: style: an en or em dash")
        if "/dev/" in f and re.match(r"[0-9][0-9]-", os.path.basename(f)):   # a section of a chapter
            from .corpus import front
            fm, body = front(t)
            for k in ("title", "decls"):
                if not fm.get(k):
                    probs.append(f"{rel}: front matter has no {k}")
            if not re.match(r"\s*## ", body):
                probs.append(f"{rel}: a section must open with a ## heading")
            if re.search(r"^\*\*(?:Theorem|Proposition|Lemma|Corollary)", body, flags=re.M) and "Lean:" not in body:
                probs.append(f"{rel}: no 'Lean:' line under its statements")
        elif "/dev/" in f and not os.path.basename(f) == "intro.md":
            from .corpus import front
            fm, body = front(t)
            for k in ("id", "title", "kind", "decl"):
                if not fm.get(k):
                    probs.append(f"{rel}: front matter has no {k}")
            for h in ("## Statement", "## Proof", "## In the Lean code"):
                if h not in body:
                    probs.append(f"{rel}: no section '{h[3:]}'")
    return probs


def cmd_check(args):
    book = load(args)
    probs = check_entries(book)
    for v in pick(book, args.volume):
        md, st = book.markdown(v)
        for u in st["unresolved"]:
            probs.append(f"volume {v.number}: unresolved link {u}")
    for p in probs:
        print(p)
    print(f"{len(probs)} problems", file=sys.stderr)
    return 1 if [p for p in probs if "unresolved" not in p] else 0


def cmd_build(args):
    from . import epub, latex
    book = load(args)
    ed = edition()
    version = ed["version"]
    date = args.date or datetime.date.today().isoformat()
    fmts = set(args.formats.split(","))
    report = {}
    for v in pick(book, args.volume):
        md, st = book.markdown(v)
        d = os.path.join(args.out, f"{v.number:02d}-{v.id}")
        os.makedirs(d, exist_ok=True)
        info = {"words": st["words"], "unresolved": len(st["unresolved"])}
        if fmts & {"tex", "pdf"}:
            info.update(latex.build(book, v, md, d, version, date, pdf="pdf" in fmts))
        if "epub" in fmts:
            info.update(epub.build(book, v, md, d, version, date))
        name = f"riemann-handbook-{v.number:02d}-{v.id}-{version}"
        for ext in ("pdf", "epub"):
            src = os.path.join(d, f"main.{ext}")
            if ext in fmts and os.path.exists(src):
                dst = os.path.join(args.out, f"{name}.{ext}")
                os.replace(src, dst) if args.move else __import__("shutil").copy(src, dst)
                info[ext] = dst
        report[v.number] = info
        err = info.pop("error", None)
        print(f"volume {v.number} {v.title}: " + json.dumps(info), file=sys.stderr)
        if err:
            print(err, file=sys.stderr)
    json.dump(report, open(os.path.join(args.out, "report.json"), "w"), indent=1)
    bad = [n for n, i in report.items() if i.get("ok") is False or i.get("epub_ok") is False]
    return 1 if bad else 0


def cmd_ledger(args):
    from . import ledger
    book = load(args)
    return ledger.run(book, args)


def main(argv=None):
    ap = argparse.ArgumentParser(prog="rhb")
    ap.add_argument("--riemann", default=os.path.join(ROOT, "..", "riemann"))
    ap.add_argument("--lean", default=os.path.join(ROOT, "..", "riemann-lean"))
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("survey")
    c = sub.add_parser("check")
    c.add_argument("--volume", default="all")
    b = sub.add_parser("build")
    b.add_argument("--volume", default="all")
    b.add_argument("--formats", default="pdf,epub")
    b.add_argument("--out", default=os.path.join(ROOT, "build"))
    b.add_argument("--date", default="")
    b.add_argument("--move", action="store_true")
    lg = sub.add_parser("ledger")
    lg.add_argument("--records", default="/tmp/rr/records")
    lg.add_argument("--min", type=int, default=1000)
    lg.add_argument("--write", action="store_true")
    args = ap.parse_args(argv)
    return {"survey": cmd_survey, "check": cmd_check, "build": cmd_build, "ledger": cmd_ledger}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main() or 0)
