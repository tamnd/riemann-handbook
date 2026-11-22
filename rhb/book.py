"""The volumes of the handbook and the Markdown of each.

Volume 0, Guide: the front pages of content/front, the named results and their sources, and the index of Lean names.
Volume 1, Background: the 17 chapters of Part I of Learn, in the order to read them.
Volume 2, The proof: the chapters of the written proof, each with its guide from Part II of Learn and its steps.
Volume 3 and later: the Lean development, written for this book in content/dev.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field

import yaml

from .corpus import Riemann, anchor, commit, front, load_dev
from .md import Converter, Labels, label_id, strip_title


@dataclass
class Volume:
    number: int
    id: str
    title: str
    summary: str
    parts: list = field(default_factory=list)   # what make() reads
    kind: str = ""
    squares: list = field(default_factory=list)   # the cover: one square per chapter, filled 0 to 1


FRONT = ["preface", "reading", "status", "notation"]


class Book:
    def __init__(self, riemann_dir: str, lean_dir: str, content_dir: str, lean_pin: str = "main"):
        self.r = Riemann.load(riemann_dir)
        self.lean_dir = lean_dir
        self.content = content_dir
        self.lean_commit = commit(lean_dir) if os.path.isdir(lean_dir) else (lean_pin or "main")
        self.dev = load_dev(content_dir)
        self.labels = Labels()
        self.volumes = self._volumes()
        self._register()

    # ------------------------------------------------------------------ structure
    def _volumes(self) -> list[Volume]:
        vs = [Volume(0, "guide", "Guide",
                     "How to read the handbook, the status of the claim, the notation, the named results and the "
                     "index of the Lean names.", kind="guide"),
              Volume(1, "background", "Background",
                     "The mathematics that the proof uses, from linear algebra to periods of automorphic forms, "
                     "in the order to learn it.", kind="background"),
              Volume(2, "proof", "The proof",
                     "The written proof of the Lean code, from the Riemann Hypothesis down to its large inputs, "
                     "with a guide to each chapter and its steps.", kind="proof")]
        for d in self.dev:
            vs.append(Volume(d.number, d.id, d.title, d.summary, kind="dev", parts=[d]))
        return vs

    def volume(self, n: int) -> Volume:
        return next(v for v in self.volumes if v.number == n)

    def _register(self):
        L = self.labels
        for k, p in enumerate(self.r.part1(), 1):
            L.add(f"/learn/{p.id}/", 1, str(k), f"learn-{p.id}")
            for sec, title in enumerate(_h2(p.body), 1):
                L.add(f"/learn/{p.id}/#{anchor(title)}", 1, f"{k}.{sec}", label_id(f"learn-{p.id}", anchor(title)))
            for title in _h3(p.body):
                L.add(f"/learn/{p.id}/#{anchor(title)}", 1, "", label_id(f"learn-{p.id}", anchor(title)))
        L.add("/learn/", 1, "", "volume-1")
        for p in self.r.paths.values():
            if p.order is None:   # a Part II guide: its page is the guide section of its chapter
                for slug in p.for_:
                    if slug != "overview":
                        L.add(f"/learn/{p.id}/", 2, self._chapter_num(slug), f"guide-{p.id}")
        for c in self.r.chapters:
            n = str(c.num)
            L.add("/proof/" if c.slug == "overview" else f"/proof/{c.slug}/", 2, n, f"proof-{c.slug}")
            if c.slug == "overview":
                L.add("/proof/overview/", 2, n, f"proof-{c.slug}")
            secs = _h2(c.body)
            for s, title in enumerate(secs, 1):
                L.add(("/proof/" if c.slug == "overview" else f"/proof/{c.slug}/") + f"#{anchor(title)}", 2,
                      f"{n}.{s}", label_id(f"proof-{c.slug}", anchor(title)))
            for j, st in enumerate(self.chapter_steps(c.slug), len(secs) + 2):
                L.add(f"/step/{st.id}/", 2, f"{n}.{j}", f"step-{st.id}")
                if st.decl:
                    L.by_decl.setdefault(st.decl, []).append((2, f"{n}.{j}", f"step-{st.id}", st.title))
            for item in c.fm.get("lean") or []:
                L.by_decl.setdefault(item["name"], []).append((2, n, f"proof-{c.slug}", c.title))
        for d in self.dev:
            for ci, ch in enumerate(d.chapters, 1):
                L.add(f"/entry/{d.id}/{ch.id}/", d.number, str(ci), f"dev-{d.id}-{ch.id}")
                for ei, e in enumerate(ch.entries, 1):
                    L.add(f"/entry/{e.id}/", d.number, f"{ci}.{ei}", f"entry-{e.id}")
                    L.web[f"/entry/{e.id}/"] = ("https://github.com/tamnd/riemann-handbook/blob/main/"
                                               + os.path.relpath(e.path, os.path.dirname(self.content)))
                    if e.decl:
                        L.by_decl.setdefault(e.decl, []).append((d.number, f"{ci}.{ei}", f"entry-{e.id}", e.title))

    def _chapter_num(self, slug: str) -> str:
        for c in self.r.chapters:
            if c.slug == slug:
                return str(c.num)
        return ""

    def chapter_steps(self, slug: str):
        """The steps of a chapter, in the order of the timeline when there is one, else by id."""
        steps = [s for s in self.r.steps.values() if s.chapter == slug]
        order = self._step_order()
        return sorted(steps, key=lambda s: (order.get(s.id, 10 ** 6), s.id))

    def _step_order(self) -> dict[str, int]:
        if hasattr(self, "_order"):
            return self._order
        self._order = {}
        p = os.path.join(self.r.root, "proof", "timeline.yaml")
        if os.path.exists(p):
            text = open(p, encoding="utf-8").read()
            for i, sid in enumerate(re.findall(r"(?m)^\s*-?\s*(?:step|id):\s*([a-z0-9-]+)", text)):
                self._order.setdefault(sid, i)
        return self._order

    # ------------------------------------------------------------------ Markdown
    def markdown(self, v: Volume) -> tuple[str, dict]:
        conv = Converter(self.labels, v.number, self.lean_commit)
        md = {"guide": self._guide, "background": self._background, "proof": self._proof,
              "dev": self._dev}[v.kind](v, conv)
        stats = {"unresolved": sorted(set(conv.unresolved)), "pending": sorted(set(conv.pending)), "words": len(re.findall(r"\b\w+\b", md))}
        return md, stats

    def _background(self, v: Volume, conv: Converter) -> str:
        out = [self._front_file("background-intro", "Introduction", "background-intro", conv)]
        for k, p in enumerate(self.r.part1(), 1):
            out.append(f"# {conv.inline(p.title)} {{#learn-{p.id} num=\"{k}\"}}\n")
            if p.lead:
                out.append(f"::: {{latex-env=\"hblead\"}}\n{conv.inline(p.lead)}\n:::\n")
            out.append(conv.page(p.body, shift=0, prefix=f"learn-{p.id}", numbering=str(k)))
            srcs = []
            for it in p.items:
                t = (it.get("text") or "").strip()
                if t and t not in srcs:
                    srcs.append(t)
            if srcs:
                out.append(f"\n## Sources {{#learn-{p.id}-sources-of-the-chapter}}\n")
                out.append("\n".join(f"- {conv.inline(s)}" for s in srcs) + "\n")
        return "\n\n".join(out)

    def _proof(self, v: Volume, conv: Converter) -> str:
        out = [self._front_file("proof-intro", "Introduction", "proof-intro", conv)]
        for c in self.r.chapters:
            n = str(c.num)
            out.append(f"# {conv.inline(c.title)} {{#proof-{c.slug} num=\"{n}\"}}\n")
            if c.lead:
                out.append(f"::: {{latex-env=\"hblead\"}}\n{conv.inline(c.lead)}\n:::\n")
            g = self.r.guide_for(c.slug) if c.slug != "overview" else None   # the trunk guide serves both
            secs = _h2(c.body)
            if g is not None:
                out.append(f"## A guide to this chapter {{#guide-{g.id}}}\n")
                out.append(conv.page(g.body, shift=1, prefix=f"guide-{g.id}"))
            out.append(conv.page(c.body, shift=0, prefix=f"proof-{c.slug}", numbering=n))
            steps = self.chapter_steps(c.slug)
            if steps:
                j0 = len(secs) + 1
                out.append(f"## The steps {{#proof-{c.slug}-steps num=\"{n}.{j0}\"}}\n")
                out.append("The steps below state each result of the chapter that has a page of its own, "
                           "with its proof in words.\n")
                for j, st in enumerate(steps, j0 + 1):
                    out.append(f"## {conv.inline(st.title)} {{#step-{st.id} num=\"{n}.{j}\"}}\n")
                    meta = [f"Lean: `{st.decl}`"] if st.decl else []
                    meta.append(f"status: {st.status}")
                    out.append(f"*{'. '.join(meta)}.*\n")
                    out.append(conv.page(st.body, shift=1, prefix=f"step-{st.id}"))
        return "\n\n".join(out)

    def _dev(self, v: Volume, conv: Converter) -> str:
        d = v.parts[0]
        out = []
        if d.intro.strip():
            out.append(f"# Introduction {{#dev-{d.id}-intro}}\n")
            out.append(conv.page(strip_title(d.intro), shift=0, prefix=f"dev-{d.id}-intro"))
        for ci, ch in enumerate(d.chapters, 1):
            out.append(f"# {conv.inline(ch.title)} {{#dev-{d.id}-{ch.id} num=\"{ci}\"}}\n")
            if ch.intro.strip():
                out.append(conv.page(strip_title(ch.intro), shift=0, prefix=f"dev-{d.id}-{ch.id}"))
            for ei, e in enumerate(ch.entries, 1):
                out.append(f"## {conv.inline(e.title)} {{#entry-{e.id} num=\"{ci}.{ei}\"}}\n")
                meta = [e.kind.capitalize()]
                if e.decl:
                    meta.append(f"Lean: `{e.decl}`")
                if e.fm.get("covers"):
                    meta.append(f"{int(e.fm['covers']):,} declarations below it")
                meta.append(f"status: {e.status}")
                out.append(f"*{'. '.join(meta)}.*\n")
                out.append(conv.page(e.body, shift=1, prefix=f"entry-{e.id}"))
        return "\n\n".join(out)

    def _guide(self, v: Volume, conv: Converter) -> str:
        out = []
        for i, name in enumerate(FRONT):
            p = os.path.join(self.content, "front", name + ".md")
            if os.path.exists(p):
                fm, body = front(open(p, encoding="utf-8").read())
                title = fm.get("title", name.capitalize())
                out.append(f"# {title} {{#front-{name}}}\n")
                out.append(conv.page(body, shift=0, prefix=f"front-{name}"))
        out.append(self._volume_list(conv))
        out.append(self._named_results(conv))
        out.append(self._lean_index(conv))
        return "\n\n".join(out)

    def _front_file(self, name: str, title: str, label: str, conv: Converter) -> str:
        p = os.path.join(self.content, "front", name + ".md")
        if not os.path.exists(p):
            return ""
        fm, body = front(open(p, encoding="utf-8").read())
        return f"# {fm.get('title', title)} {{#{label}}}\n\n" + conv.page(body, shift=0, prefix=label)

    def _volume_list(self, conv: Converter) -> str:
        rows = ["# The volumes {#front-volumes}\n", "| | Volume | What it has |", "|---|---|---|"]
        for v in self.volumes:
            rows.append(f"| {v.number} | {v.title} | {v.summary} |")
        return "\n".join(rows) + "\n"

    def _named_results(self, conv: Converter) -> str:
        out = ["# The named results {#front-named-results}\n",
               "The written proof cites a published result in place of a step at these places. The Lean code "
               "proves each of them; the citation says where the same mathematics is published, and the note says "
               "how the Lean statement differs from it.\n"]
        for i, r in enumerate(self.r.literature, 1):
            out.append(f"## {conv.inline(r.get('result', r['name']))} {{#named-{i} num=\"{i}\"}}\n")
            out.append(f"Lean: `{r['name']}`.\n")
            if r.get("says"):
                out.append(conv.inline(r["says"]) + "\n")
            for c in r.get("cite") or []:
                au = ", ".join(c.get("authors") or [])
                bits = [au, f"*{c.get('title', '')}*", c.get("venue", ""), str(c.get("year", ""))]
                ref = ". ".join(b for b in bits if b)
                if c.get("doi"):
                    ref += f". <https://doi.org/{c['doi']}>"
                out.append(f"- {conv.inline(ref)}.")
            if r.get("note"):
                out.append("\n" + conv.inline(r["note"]) + "\n")
        return "\n".join(out)

    def _lean_index(self, conv: Converter) -> str:
        out = ["# The Lean names {#front-lean-index}\n",
               "Each Lean declaration that a page of the handbook explains, with the volume and the number of the page.\n"]
        for name in sorted(self.labels.by_decl, key=str.lower):
            places = "; ".join(f"Vol. {vol}, {num} *{conv.inline(t)}*" if num else f"Vol. {vol} *{conv.inline(t)}*"
                               for vol, num, lab, t in self.labels.by_decl[name])
            out.append(f"- `{name}`: {places}.")
        return "\n".join(out) + "\n"


def _headings(body: str, level: int) -> list[str]:
    out, fence = [], False
    pre = "#" * level + " "
    for ln in body.split("\n"):
        if re.match(r"^(`{3,}|~{3,})", ln):
            fence = not fence
            continue
        if not fence and ln.startswith(pre):
            out.append(ln[len(pre):].strip())
    return out


def _h2(body: str) -> list[str]:
    return _headings(body, 2)


def _h3(body: str) -> list[str]:
    return _headings(body, 3)
