"""The sources of the handbook: the content of tamnd/riemann, the Lean tree of tamnd/riemann-lean and the
written entries of this repository (content/)."""

from __future__ import annotations

import glob
import os
import re
import subprocess
from dataclasses import dataclass, field

import yaml


def front(text: str) -> tuple[dict, str]:
    """Split a Markdown file into its YAML front matter and its body."""
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end > 0:
            return yaml.safe_load(text[4:end]) or {}, text[end + 5:]
    return {}, text


def commit(path: str) -> str:
    try:
        return subprocess.run(["git", "-C", path, "rev-parse", "HEAD"], capture_output=True, text=True,
                              check=True).stdout.strip()
    except Exception:
        return "unknown"


@dataclass
class Path:
    """A Learn page of tamnd/riemann: a Part I chapter (order set) or a Part II guide (for set)."""
    id: str
    title: str
    lead: str
    order: int | None
    for_: list[str]
    needs: list[str]
    items: list[dict]
    body: str


@dataclass
class Chapter:
    """A chapter of the written proof, proof/NN-slug.md."""
    num: int
    slug: str
    title: str
    lead: str
    fm: dict
    body: str


@dataclass
class Step:
    """A step of the written proof, proof/steps/<id>.md."""
    id: str
    title: str
    decl: str
    chapter: str
    status: str
    fm: dict
    body: str


@dataclass
class Riemann:
    root: str
    paths: dict[str, Path] = field(default_factory=dict)
    chapters: list[Chapter] = field(default_factory=list)
    steps: dict[str, Step] = field(default_factory=dict)
    literature: list[dict] = field(default_factory=list)
    math2: dict[str, str] = field(default_factory=dict)

    @classmethod
    def load(cls, root: str) -> "Riemann":
        r = cls(root)
        for y in sorted(glob.glob(os.path.join(root, "paths", "*.yaml"))):
            d = yaml.safe_load(open(y, encoding="utf-8")) or {}
            md = y[:-5] + ".md"
            body = open(md, encoding="utf-8").read() if os.path.exists(md) else ""
            r.paths[d["id"]] = Path(d["id"], d.get("title", d["id"]), d.get("lead", ""), d.get("order"),
                                    list(d.get("for") or []), list(d.get("needs") or []), list(d.get("items") or []),
                                    body)
        for f in sorted(glob.glob(os.path.join(root, "proof", "[0-9][0-9]-*.md"))):
            fm, body = front(open(f, encoding="utf-8").read())
            base = os.path.basename(f)[:-3]
            num, slug = int(base[:2]), base[3:]
            r.chapters.append(Chapter(num, slug, fm.get("title", slug), fm.get("lead", ""), fm, body))
        for f in sorted(glob.glob(os.path.join(root, "proof", "steps", "*.md"))):
            fm, body = front(open(f, encoding="utf-8").read())
            sid = fm.get("id") or os.path.basename(f)[:-3]
            r.steps[sid] = Step(sid, fm.get("title", sid), fm.get("decl", ""), fm.get("chapter", ""),
                                fm.get("status", "drafted"), fm, body)
        lit = os.path.join(root, "links", "literature.yaml")
        if os.path.exists(lit):
            d = yaml.safe_load(open(lit, encoding="utf-8"))
            r.literature = d if isinstance(d, list) else (d or {}).get("results", []) or []
        m2 = os.path.join(root, "links", "math2.yaml")
        if os.path.exists(m2):
            r.math2 = (yaml.safe_load(open(m2, encoding="utf-8")) or {}).get("decls", {}) or {}
        return r

    def part1(self) -> list[Path]:
        return sorted((p for p in self.paths.values() if p.order is not None), key=lambda p: p.order)

    def guide_for(self, slug: str) -> Path | None:
        for p in self.paths.values():
            if slug in p.for_:
                return p
        return None

    def commit(self) -> str:
        return commit(self.root)


@dataclass
class Entry:
    """An entry written for the handbook from the Lean code: content/dev/<volume>/<chapter>/<id>.md."""
    id: str
    title: str
    kind: str
    decl: str
    status: str
    fm: dict
    body: str
    path: str


@dataclass
class DevChapter:
    id: str
    title: str
    intro: str
    entries: list[Entry]
    text: str = ""          # a chapter written as mathematics: its section files, joined in order
    decls: list = field(default_factory=list)


@dataclass
class DevVolume:
    """A volume on the Lean development: content/dev/NN-<id>/volume.yaml and its chapters."""
    number: int
    id: str
    title: str
    summary: str
    intro: str
    chapters: list[DevChapter]


def load_dev(content: str) -> list[DevVolume]:
    out = []
    for d in sorted(glob.glob(os.path.join(content, "dev", "[0-9][0-9]-*"))):
        vy = os.path.join(d, "volume.yaml")
        if not os.path.exists(vy):
            continue
        v = yaml.safe_load(open(vy, encoding="utf-8")) or {}
        base = os.path.basename(d)
        intro_p = os.path.join(d, "intro.md")
        chapters = []
        for c in v.get("chapters") or []:
            cdir = os.path.join(d, c["id"])
            entries = []
            for eid in c.get("entries") or []:
                p = os.path.join(cdir, eid + ".md")
                if not os.path.exists(p):
                    continue
                fm, body = front(open(p, encoding="utf-8").read())
                entries.append(Entry(fm.get("id", eid), fm.get("title", eid), fm.get("kind", "theorem"),
                                     fm.get("decl", ""), fm.get("status", "drafted"), fm, body, p))
            ip = os.path.join(cdir, "intro.md")
            # a chapter written as mathematics: section files NN-<slug>.md, each opening with a ## heading
            secs = sorted(glob.glob(os.path.join(cdir, "[0-9][0-9]-*.md")))
            text, decls = [], []
            for sp in secs:
                fm, body = front(open(sp, encoding="utf-8").read())
                text.append(body.strip("\n"))
                decls += fm.get("decls") or []
            if secs:
                entries = []   # the section files replace the entries of the chapter
            if not entries and not secs:   # a chapter of the plan with nothing written yet
                continue
            chapters.append(DevChapter(c["id"], c.get("title", c["id"]),
                                       open(ip, encoding="utf-8").read() if os.path.exists(ip) else "", entries,
                                       "\n\n".join(text), decls))
        if not chapters:
            continue
        out.append(DevVolume(int(base[:2]), base[3:], v.get("title", base), v.get("summary", ""),
                             open(intro_p, encoding="utf-8").read() if os.path.exists(intro_p) else "", chapters))
    return out


_SLUG = re.compile(r"[^a-z0-9 -]")


def anchor(heading: str) -> str:
    """The anchor of a heading, as the riemann site makes it: lower case, spaces become hyphens, other
    punctuation goes. Math in dollars is kept as its letters ($L^2$ spaces → l2-spaces)."""
    s = heading.strip().lower()
    s = _SLUG.sub("", s)
    return re.sub(r" +", "-", s).strip("-")
