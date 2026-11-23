# The Riemann Handbook

On 20 November 2026 Levent Alpöge released a proof of the Riemann Hypothesis, written in Lean ([remark.pdf](https://alpo.ge/remark.pdf)). The proof has about 17 million lines in 175,187 files. This handbook writes that proof out as mathematics, for a student who knows some number theory and does not read Lean. It comes as a set of books in PDF and EPUB. The Lean source that we follow is in [tamnd/riemann-lean](https://github.com/tamnd/riemann-lean), and the web version is at [riemann.tamnd.com](https://riemann.tamnd.com).

## The status of the proof

The Lean proof has been checked by machine, by several groups and with several independent checkers. People have not yet read and explained the mathematics behind it.

On 21 November 2026 the Lean and Mathlib communities published [a joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/), with the endorsement of the Lean FRO and the Mathlib Initiative: "We hereby certify that both the statement and the proof of the Riemann Hypothesis are correct." The theorem that is proved is the statement [`RiemannHypothesis`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/RiemannZeta.html#RiemannHypothesis) of Mathlib. The checks follow the criteria in the Xena Project post [*…and the proof is checked in Lean*](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/): the statement is the right one, the code compiles, `lake comparator` matches the theorem to a trusted statement, and more than one kernel accepts the proof.

Andrew Sutherland keeps [the list of the checks](https://math.mit.edu/~drew/grh/), with their logs. On 22 November 2026 it gave these results:

- All 175,187 modules compile with Lean v4.33.1, with no errors.
- The five main theorems depend only on the three standard axioms `propext`, `Classical.choice` and `Quot.sound`.
- A second build on a separate machine, with no network and a read-only source, gave an export of 61,570,595,788 bytes. It is the same, byte for byte, as the published export.
- The proof is accepted by the Lean kernel (`leanchecker`, each module), by [lean4lean](https://github.com/digama0/lean4lean), by nanoda (a kernel written in Rust), and by [con-leche](https://github.com/leanprover/con-leche) and [con-ron](https://github.com/leanprover/con-ron). The last two also confirm that the theorems proved are the theorems stated.
- Two runs had not finished: the default and paranoid Lean kernels on the full export, which run on one thread, and a full `lake comparator` run.

Some limits are stated by the checkers themselves. The checks show that the Lean code proves the Mathlib statement. They depend on the kernels and on the definitions of Mathlib meaning what they are meant to mean. They do not explain the ideas of the proof, and the joint statement looks forward to work that "will help explain the new ideas". Sutherland's page also notes that Dedekind zeta functions, Hecke $L$-functions and automorphic $L$-functions in general are not among the statements checked. On 23 November 2026 the Clay Mathematics Institute still lists the problem as [unsolved](https://www.claymath.org/millennium/riemann-hypothesis/).

This handbook is not one more check. It is a guide to the mathematics: what each part of the Lean code proves, said as a textbook says it. [What is checked](https://riemann.tamnd.com/trust/) on the site gives more detail.

## The volumes

| | Volume | Chapters |
|---|---|---|
| 0 | Guide: how to read, the status of the claim, notation, the named results, an index of Lean names | |
| 1 | Background: the mathematics that the proof uses | 17 |
| 2 | The proof: its top, its chapters and its steps | |
| 3 | The Galois row | 13 |
| 4 | The window bound | 21 |
| 5 | Volume estimates and positivity | 19 |
| 6 | Theta integrals and the green window | 22 |
| 7 | The unitary hypotheses | 50 |
| 8 | Automorphic arithmetic | 8 |
| 9 | Abelian varieties | 22 |
| 10 | The Weil bound, the spectrum and resolution | 26 |
| 11 | The formalism | 41 |
| 12 | Ground theory | 33 |

Volumes 0 to 2 come from [tamnd/riemann](https://github.com/tamnd/riemann). Volumes 3 to 12 are written for this book, in `content/dev/`. The books are in the [releases](https://github.com/tamnd/riemann-handbook/releases).

## The plan

Volume 1 is the model for the rest. Each chapter defines its objects, states its results in standard notation with numbers (Theorem 3.1.4), proves them, and ends with notes and references.

The first drafts of Volumes 3 to 12 gave a short note to each large declaration of the Lean code. The notes were accurate, but they read as notes on code, not as mathematics. We are now writing these volumes again as chapters of a textbook. A chapter takes one part of the proof and does the following:

- It defines each object before it uses it, or links to its definition in Volume 1.
- It states a known theorem in its usual form, with a source, and then says how the Lean form differs.
- It gives each proof as a mathematician gives it: the main steps, and the earlier result that each step uses.
- It puts a line `Lean:` under each statement, with the names of the declarations that prove it. Small lemmas and second names of a result go into that line or into a proof.
- It notes what is odd in the Lean code, such as a hypothesis that is never used or a name that says something else, in a short remark.

The ledger `ledger/outline.yaml` divides the proof into 255 chapters, which cover 5,756 declarations: those whose subtree in the proof has 100 or more declarations. Each declaration belongs to the subtree of exactly one other, its immediate dominator in the graph of uses from `riemannHypothesis`. `ledger/coverage.md` has the numbers.

The work is in the milestone [M10 Mathematical chapters](https://github.com/tamnd/riemann-handbook/milestone/11), with one issue for each volume (#65 to #74). The brief for the writers is `prompts/chapter.md`. The first chapter in this form is *Étale clopen descent*, in Volume 3.

A chapter is a folder `content/dev/NN-volume/<chapter>/`. It has an optional `intro.md` and one file `NN-<slug>.md` for each section. A section file has `title` and `decls` in its front matter, and its text starts with a `##` heading. The build numbers the statements, and turns a link `/entry/<id>/` into the number of the statement that proves the declaration.

## Build

You need Python 3.11 or later, [pandoc](https://pandoc.org) 3.8 or later and [Tectonic](https://tectonic-typesetting.github.io). Put tamnd/riemann and tamnd/riemann-lean next to this repository.

```sh
pip install .
python -m rhb survey
python -m rhb check
python -m rhb build --volume 0,1,2,3 --formats pdf,epub
```

The books go to `build/`. The pipeline is that of [The Handbook of Algorithms](https://github.com/tamnd/algorithm-handbook): Markdown, then pandoc with `filters/rhb.lua`, then LaTeX with `tex/handbook.sty`, then Tectonic. The EPUB is EPUB 3 with MathML.

## Licence

The text is licensed under [CC BY 4.0](LICENSE-CONTENT), as the text of tamnd/riemann. The builder is licensed under the [MIT licence](LICENSE).

Please report errors at [issues](https://github.com/tamnd/riemann-handbook/issues).
