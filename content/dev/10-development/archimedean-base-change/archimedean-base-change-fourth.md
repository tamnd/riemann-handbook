---
id: archimedean-base-change-fourth
title: The Iwahori matching at an inert place, under the name of a base change step
kind: theorem
decl: PositivityTheory.Rg.Bc.ArchbcB.B.archimedean_base_change_fourth
module: Development.WeilBound.RepresentationTheoryGL.ArchimedeanBaseChange.ArchimedeanBaseChangeProof.IwahoriFactorisation.TwistedConjugationNorms.ArchimedeanBaseChangeFourth
covers: 315
status: drafted
drafted_by: writer@claude
---
This theorem is a second name. It proves the statement `M4` by the theorem [`M4.m4`](/entry/m4/), with no other step. The mathematics is in the entry [`m4`](/entry/m4/). The theorem [`hM4`](/entry/h-m4/) is a further name for this one.

## Statement

**Theorem** (`M4`). Let $E$ be a CM field with each finite place unramified over the maximal real subfield, and let $w$ be a finite place of $E$ that does not split. Let $a \le n$, let $b \in \mathrm{GL}_n(\mathcal{O}_w)$ satisfy $\bar b^{\mathsf T} b = J$ (`IsWitt`), and let $\varpi$ be a uniformizer with $\bar\varpi = \varpi$ (`IsUnifAt`). Let $x \in \mathbb{Z}^n$ be strictly decreasing, with $l_i = x_i - x_{n-1-i}$ in `Cone`. Then:

1. the indicator $f_U$ of the Iwahori double coset of $b\, t_l\, b^{-1}$ in the unitary group and the function $\phi_x$ on $\mathrm{GL}_a \times \mathrm{GL}_{n-a}$ match with the trivial character (`Match`);
2. $\phi_x$ is nonzero only at elements whose norms have separable characteristic polynomials (`RegAt2`).

The entry [`m4`](/entry/m4/) gives $f_U$, $\phi_x$ and `Match` in full.

## Proof

The proof is the term `M4.m4`.

## In the Lean code

The theorem is in [ArchimedeanBaseChangeFourth.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/IwahoriFactorisation/TwistedConjugationNorms/ArchimedeanBaseChangeFourth.lean#L3). This is the only declaration in the file. `M4` is in [SymIdx.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/IwahoriFactorisation/SymIdx.lean#L50), and `m4` is in [Development.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/IwahoriFactorisation/TwistedConjugationNorms/Development.lean#L1166).

The name is misleading. `M4` is a statement at a finite place $w$ of $E$, with Iwahori subgroups and a uniformizer. No archimedean place occurs in it. `MatchAll.lean` uses this name at line 26 for `hM4` and at line 32 for `matchT`.
