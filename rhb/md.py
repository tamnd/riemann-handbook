"""The conversion of the Markdown of the site into the Markdown of a volume.

The site writes links to its own pages (/learn/algebra/#matrices, /proof/vwin/, /step/rh-of-right/), to the Lean
source (lean:File.lean#L4) and to Math 2.0 ([[Name|TAG]]). A volume turns a link to a page in the same volume into
a link inside the book, followed by the number of the target, and a link to a page in another volume into a link
to the site, followed by the volume and the number. The other two kinds become links to the web.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from .corpus import anchor

SITE = "https://riemann.tamnd.com"
LEAN = "https://github.com/tamnd/riemann-lean/blob/{commit}/lean/src/{file}"
MATH2 = "https://math2.tamnd.com/search/?q={tag}"
# pages of the site that the book does not print: a link to them goes to the site
SITE_ONLY = {"/proof/timeline/", "/trust/", "/search/", "/graph/", "/about/"}


@dataclass
class Target:
    volume: int
    number: str      # "3.4", "" for a page with no number
    label: str       # the identifier in the book


@dataclass
class Labels:
    """Every place a link can point to: a site path (with its anchor) → its volume, number and label."""
    by_path: dict[str, Target] = field(default_factory=dict)
    by_decl: dict[str, list[tuple[int, str, str, str]]] = field(default_factory=dict)  # decl → (vol, num, label, title)
    web: dict[str, str] = field(default_factory=dict)   # a path with no page on the site → its URL

    def add(self, path: str, volume: int, number: str, label: str):
        self.by_path.setdefault(path, Target(volume, number, label))


def label_id(*parts: str) -> str:
    return "-".join(p for p in parts if p).replace("_", "-")


_FENCE = re.compile(r"^(`{3,}|~{3,})")
_MATH = re.compile(r"\$\$.*?\$\$|(?<![\\$])\$[^$\n]+\$", re.S)
_LINK = re.compile(r"(?<!!)\[((?:[^\[\]]|\[[^\]]*\])*)\]\(([^)\s]+)\)")
_WIKI = re.compile(r"\[\[([^\[\]|]+)\|([0-9A-Z]{6,12})\]\]")
_BARE_WIKI = re.compile(r"\[\[([0-9A-Z]{6,12})\]\]")
_NUMBERED = re.compile(r"\b[0-9]+\.[0-9]+(?:\.[0-9]+)*(?: of Volume [0-9]+)?$")
_STMT = re.compile(r"^\*\*(Definition|Theorem|Proposition|Lemma|Corollary|Example|Remark|Conjecture)"
                   r"((?: [a-z]+)?)(?: [0-9]+(?:\.[0-9]+)*)?((?: \((?:[^()]|\([^()]*\))*\))?)\.\*\*")


class Converter:
    """Converts the Markdown of one page for one volume."""

    def __init__(self, labels: Labels, volume: int, lean_commit: str):
        self.labels = labels
        self.volume = volume
        self.lean_commit = lean_commit
        self.unresolved: list[str] = []
        self.pending: list[str] = []

    # -- links
    def resolve(self, dest: str, text: str) -> str:
        if dest.startswith("lean:"):
            file, _, frag = dest[5:].partition("#")
            url = LEAN.format(commit=self.lean_commit, file=file) + (f"#{frag}" if frag else "")
            return f"[{text}]({url})"
        if dest.startswith("m2node:"):
            return f"[{text}]({MATH2.format(tag=dest[7:])})"
        if dest.startswith("/"):
            path, _, frag = dest.partition("#")
            if not path.endswith("/"):
                path += "/"
            key = path + (f"#{frag}" if frag else "")
            t = self.labels.by_path.get(key) or (self.labels.by_path.get(path) if frag else None)
            if t is None and path.startswith("/entry/"):
                self.pending.append(dest)   # an entry of the plan that is not written yet: the text stays
                return text
            if t is None:
                if path not in SITE_ONLY:
                    self.unresolved.append(dest)
                return f"[{text}]({SITE}{dest})"
            num = t.number
            if num and _NUMBERED.search(text):   # the text already has the number: "Theorem 3.1.4"
                if t.volume == self.volume:
                    return f"[{text}](#{t.label})"
                return f"[{text}]({self.labels.web.get(path, SITE + dest)})"
            if t.volume == self.volume:
                ref = f" [{num}]{{.ref}}" if num else ""
                return f"[{text}](#{t.label}){ref}"
            where = f"Vol. {t.volume}" + (f", {num}" if num else "")
            url = self.labels.web.get(path, SITE + dest)   # entries have no page on the site: their source
            return f"[{text}]({url}) [{where}]{{.ref}}"
        return f"[{text}]({dest})"

    def inline(self, s: str) -> str:
        """Links and Math 2.0 names in one line of prose, outside code and mathematics."""
        keep: list[str] = []

        def hold(m: re.Match) -> str:
            keep.append(m.group(0))
            return f"\x00{len(keep) - 1}\x00"

        s = re.sub(r"`[^`\n]*`", hold, s)
        s = _MATH.sub(hold, s)
        s = _WIKI.sub(lambda m: f"[{m[1]}]({MATH2.format(tag=m[2])})", s)
        s = _BARE_WIKI.sub(lambda m: m[1], s)
        s = _LINK.sub(lambda m: self.resolve(m[2], m[1]), s)
        while "\x00" in s:
            s = re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m[1])], s)
        return s

    # -- headings and statements
    def page(self, md: str, *, shift: int, prefix: str, numbering: str | None = None,
             sections: dict | None = None) -> str:
        """Convert a page. `shift` moves every heading down (## becomes ### for shift 1). Headings get the
        identifier `prefix-<anchor>`. With `numbering` ("3"), each ## heading gets a number 3.1, 3.2, … and each
        bold statement head the number of its section and its place there: Definition 3.2.1."""
        out, fence = [], None
        sec = 0
        stmt = 0
        for ln in md.split("\n"):
            f = _FENCE.match(ln)
            if f:
                fence = None if fence == f.group(1)[0] else (fence or f.group(1)[0])
                out.append(ln)
                continue
            if fence:
                out.append(ln)
                continue
            m = re.match(r"^(#{1,6}) +(.*?)\s*$", ln)
            if m:
                level = len(m.group(1))
                title = m.group(2)
                lab = label_id(prefix, anchor(title))
                head = "#" * min(6, level + shift)
                if numbering and level == 2:
                    sec += 1
                    stmt = 0
                    out.append(f"{head} {self.inline(title)} {{#{lab} num=\"{numbering}.{sec}\"}}")
                else:
                    out.append(f"{head} {self.inline(title)} {{#{lab}}}")
                continue
            m = _STMT.match(ln)
            if m and numbering:
                stmt += 1
                kind, more, name = m.group(1), m.group(2), m.group(3)
                num = f"{numbering}.{sec}.{stmt}"
                rest = ln[m.end():]
                lab = label_id(prefix, "st", str(sec), str(stmt))
                name = self.inline(name)
                head = f"[{kind}{more} {num}{name}.]{{latex-cmd=\"hbsthead\"}}"
                if not out or not out[-1].strip():   # a paragraph of its own: a little space above it
                    out.append("```{=latex}\n\\hbstskip\\hbnoindentnext\n```\n")
                out.append(f"[]{{#{lab}}}{head}{self.inline(rest)}")
                continue
            lm = re.match(r"^\*?Lean:\*? (.*)$", ln)
            if lm and numbering:   # the source line under a statement of a chapter written as mathematics
                out.append(f"[Lean: {self.inline(lm.group(1))}]{{latex-cmd=\"hblean\"}}")
                continue
            out.append(self.inline(ln))
        return "\n".join(out)


def strip_title(md: str) -> str:
    """Drop a leading # title line: the volume makes its own chapter heading."""
    lines = md.lstrip("\n").split("\n")
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    return "\n".join(lines)
