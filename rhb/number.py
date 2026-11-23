"""Write the numbers of the build into the Markdown of the chapters written as mathematics.

A statement head **Theorem (Name).** becomes **Theorem 3.2.4 (Name).**: chapter 3 of its volume (its place in
volume.yaml), section 2 of the chapter (the second ## heading), statement 4 of the section. A link whose text is
a kind of statement, [Theorem](/entry/<id>/) or [Lemma 1.1.2](/entry/<id>/), gets the number of its target:
[Theorem 3.2.4](/entry/<id>/), or [Theorem 3.2.4 of Volume 5](/entry/<id>/) for a target in another volume.
So the source on GitHub reads as the book does.

    python -m rhb number           # list the files that would change
    python -m rhb number --write   # change them
"""

from __future__ import annotations

import re

from .md import _FENCE, _STMT

_HEAD = re.compile(r"^(\*\*(?:Definition|Theorem|Proposition|Lemma|Corollary|Example|Remark|Conjecture)"
                   r"(?: [a-z]+)?)(?: [0-9]+(?:\.[0-9]+)*)?")
_KINDS = ("Definition|Theorem|Proposition|Lemma|Corollary|Example|Remark|Conjecture|Section|Chapter|"
          "Definitions|Theorems|Propositions|Lemmas|Corollaries|Examples|Remarks|Sections")
_REF = re.compile(r"\[(" + _KINDS + r")(?: [0-9]+(?:\.[0-9]+)*)?(?: of Volume [0-9]+)?\]\((/[^)\s]+)\)")


def _stamp_heads(text: str, ci: int, sec: int) -> tuple[str, int]:
    out, fence = [], None
    stmt = 0
    for ln in text.split("\n"):
        f = _FENCE.match(ln)
        if f:
            fence = None if fence == f.group(1)[0] else (fence or f.group(1)[0])
        elif not fence:
            if re.match(r"^## ", ln):
                sec += 1
                stmt = 0
            elif _STMT.match(ln):
                stmt += 1
                ln = _HEAD.sub(lambda m: f"{m.group(1)} {ci}.{sec}.{stmt}", ln, count=1)
        out.append(ln)
    return "\n".join(out), sec


def _stamp_refs(text: str, labels, volume: int) -> str:
    def rep(m: re.Match) -> str:
        kind, dest = m.group(1), m.group(2)
        path, _, frag = dest.partition("#")
        if not path.endswith("/"):
            path += "/"
        t = labels.by_path.get(path + (f"#{frag}" if frag else "")) or labels.by_path.get(path)
        if t is None or not t.number:
            return m.group(0)
        where = "" if t.volume == volume else f" of Volume {t.volume}"
        return f"[{kind} {t.number}{where}]({dest})"
    out, fence = [], None
    for ln in text.split("\n"):
        f = _FENCE.match(ln)
        if f:
            fence = None if fence == f.group(1)[0] else (fence or f.group(1)[0])
        elif not fence and not ln.startswith("---"):
            ln = _REF.sub(rep, ln)
        out.append(ln)
    return "\n".join(out)


def run(book, write: bool) -> int:
    labels = book.labels
    changed = []
    for d in book.dev:
        for ch in d.chapters:
            if not ch.files:
                continue
            sec = 0
            for p in ch.files:
                src = open(p, encoding="utf-8").read()
                fm_end = 0
                if src.startswith("---\n"):
                    fm_end = src.index("\n---\n", 4) + 5
                body, sec = _stamp_heads(src[fm_end:], ch.num, sec)
                body = _stamp_refs(body, labels, d.number)
                new = src[:fm_end] + body
                if new != src:
                    changed.append(p)
                    if write:
                        open(p, "w", encoding="utf-8").write(new)
            # intro.md: references only
            import os
            ip = os.path.join(os.path.dirname(ch.files[0]), "intro.md")
            if os.path.exists(ip):
                src = open(ip, encoding="utf-8").read()
                new = _stamp_refs(src, labels, d.number)
                if new != src:
                    changed.append(ip)
                    if write:
                        open(ip, "w", encoding="utf-8").write(new)
    for p in changed:
        print(("numbered " if write else "would number ") + p)
    print(f"{len(changed)} files")
    return 0
