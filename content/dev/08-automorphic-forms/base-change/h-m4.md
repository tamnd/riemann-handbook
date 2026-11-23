---
id: h-m4
title: The Iwahori matching at an inert place, second name
kind: theorem
decl: PositivityTheory.Rg.BcB.F.MatchAll.hM4
module: Development.WeilBound.RepresentationTheoryGL.ArchimedeanBaseChange.ArchimedeanBaseChangeProof.SatakeExponents.UniformizerValuations.AdelicHeckeBlocks.MatchAll
covers: 316
status: drafted
drafted_by: writer@claude
---
This theorem is a second name. It proves the statement `M4` by [`archimedean_base_change_fourth`](/entry/archimedean-base-change-fourth/), which is itself a second name for the theorem [`M4.m4`](/entry/m4/). The mathematics is in the entry [`m4`](/entry/m4/). [The local matching at the places of a frame](/entry/positivity-theory-rg-bc-b-f-match-all-match-lmb2-2/) uses `hM4` for its places in $T$.

## Statement

**Theorem** (`M4`). Let $E$ be a CM field with each finite place unramified over the maximal real subfield, and $w$ a finite place of $E$ that does not split. Let $a \le n$, let $b$ satisfy `IsWitt`, let $\varpi$ satisfy `IsUnifAt`, and let $x \in \mathbb{Z}^n$ be strictly decreasing with $l = $ `lOf x` in `Cone`. Then the indicator $f_U$ of an Iwahori double coset in the unitary group matches the explicit function $\phi_x$ on $\mathrm{GL}_a \times \mathrm{GL}_{n-a}$ with the trivial character, and $\phi_x$ is supported on elements with regular norms (`RegAt2`).

See [`m4`](/entry/m4/) for the definitions of $f_U$ and $\phi_x$.

## Proof

The proof is the term `archimedean_base_change_fourth`, with no other step.

## In the Lean code

The theorem is in [MatchAll.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/UniformizerValuations/AdelicHeckeBlocks/MatchAll.lean#L26). `M4` is in [SymIdx.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/IwahoriFactorisation/SymIdx.lean#L50).

The same file does not use `hM4` everywhere. `matchT`, at line 32, applies `archimedean_base_change_fourth` directly, and `matchLMB2` takes `M4` as a hypothesis. So the statement has three names in use: `M4.m4`, `archimedean_base_change_fourth` and `hM4`.
