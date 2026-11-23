---
id: frame-ex-of-fin
title: Frames exist, given the unitary side and finiteness of candidates
kind: theorem
decl: UpperTheory.HeckeLevelFrameExistence.frameEx_of_fin
module: Development.AutomorphicArithmetic.Foundations.BaseChangeIdentities.FrameMatching.HeckeEigenvalueFiniteness.FrameExOfFin
covers: 1271
status: drafted
drafted_by: writer@claude
---
This theorem is a special case of `frameEx_of`. It fills 16 of the 18 hypotheses of that theorem and passes the other two along. The two callers prove the isobaric base change identity of the step [Isobaric base change holds](/step/base-change-n/), which lies below [EveryCharacter from the Galois row](/step/every-character/). The real content is in `frameEx_of`, which has no entry in the outline.

## Statement

Let $\mathrm{USide}$ say that the automorphic representations of the unitary group $U_n$ of a given weight and level form a finite family, and that the sum over this family of the products of the local twisted traces equals a geometric sum. Let $\mathrm{CandFin}$ be the finiteness of candidates, as in the step above.

**Theorem.** If $\mathrm{USide}$ and $\mathrm{CandFin}$ hold, then $\mathrm{FrameEx}$ holds: assume the reading limit `ReadLimit`; then for each CM field $E$ unramified over $E^+$ at every finite place, each $n \ge 1$, each automorphic representation $\pi$ of $U_n$, each finite set $S$ of places with a frame $F_0$ for $\pi$ and $S$, and each finite set $T$ of places, there is a run frame over $F_0$ and $T$.

A run frame (`RunFrame`) holds local data, a nonempty set of inert unramified places, a family of representations, an index $i_0$ whose components agree with $\pi$, and a nonzero vector that an operator $u$ fixes and that is an eigenvector of the block diagonal operators.

## Proof

The proof is `frameEx_of`, which has 18 hypotheses. This theorem gives 16 of them from proved lemmas, some used more than once: `locAlg`, `frameInert_all`, `coneEigOf eigInert LemB.bcWeyl` (see [the inert eigenvalues](/entry/eig-inert/)), `satCompAt`, `candIndep`, `mok0`, `coneTwo'`, `locC`, `locE`, `muVal`, `powEig`, and `gcHecke`. The last one is proved in the same file: a finite sum of Hecke functions is a Hecke function. The two other hypotheses are $\mathrm{USide}$ and $\mathrm{CandFin}$.

## In the Lean code

The theorem is in [FrameExOfFin.lean](lean:Development/AutomorphicArithmetic/Foundations/BaseChangeIdentities/FrameMatching/HeckeEigenvalueFiniteness/FrameExOfFin.lean#L43). The general theorem `frameEx_of` is in [KUEqKLOfNotMemBad.lean](lean:Development/AutomorphicArithmetic/Foundations/BaseChangeIdentities/FrameMatching/HeckeEigenvalueFiniteness/KUEqKLOfNotMemBad.lean#L116). `FrameEx` is in [FrameBound.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/UniformizerValuations/FrameBoundSpaces/FrameBound.lean#L29).

Both callers discharge the hypotheses. `baseChangeN_of` in [FillPre.lean](lean:Development/AutomorphicArithmetic/Foundations/BaseChangeIdentities/FillPre.lean#L7) gives `uSide` and keeps $\mathrm{CandFin}$ as its own hypothesis. `baseChangeNB` in [BaseChangeNB.lean](lean:Development/AutomorphicArithmetic/Foundations/BaseChangeIdentities/BaseChangeNB.lean#L7) gives `uSide` and `candFin_of_jEigFin jEigFin`.

A second `FrameEx` with a different statement is in [DescentOffTorusOfFrame.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/UniformizerValuations/GrowthWeightBounds/DescentOffTorusOfFrame.lean#L69).
