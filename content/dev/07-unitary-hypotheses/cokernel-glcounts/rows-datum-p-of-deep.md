---
id: rows-datum-p-of-deep
title: The row datum from the three deep inputs
kind: theorem
decl: Formalism.L2.SG.Pf.Coef.rowsDatumP_of_deep
module: Formalism.LocalToGlobal.SiegelLatticeTheory.CokernelGLCounts.RankPointCounts.CoefCutDeep
covers: 2469
status: drafted
drafted_by: writer@claude
---
This theorem is a relay that only passes hypotheses along. The real content is in [the local cut from the deep inputs](/entry/cut-at-of-deep/). Its hypothesis is proved outright in [the deep inputs, outright](/entry/cut-leaves-deep-outright/). Its result goes to [the theorem S leaves from the carrier gap](/entry/theorem-s-leaves-of-carrier-g/), which turns it into the positivity of the row kernels.

## Statement

Let $D$ be a datum of the unitary setting.

**Theorem.** If $\mathrm{CutLeavesDeep}(D)$ holds, then $\mathrm{RowsDatumP}(D)$ holds.

$\mathrm{CutLeavesDeep}(D)$ gives three inputs (`StepsU`, `StabApprox`, `FStarC`) for all local data that agree with $D$, all pairs of words with the congruence and the prime hypothesis, and all row representatives. See [the local cut](/entry/cut-at-of-deep/). $\mathrm{RowsDatumP}(D)$ says, for the same data: the densities in a set $\mathrm{densSet}$ are nonnegative, and there are local classes $\mathrm{th}(\gamma)$ and densities $\mathrm{dn}(\gamma) \in \mathrm{densSet}$ on terms, such that the classes are restricted off a finite set of places and two sums (`PartnerSumC`, `FiberCntC`) have the stated values.

## Proof

Take the three inputs from the hypothesis. `cutAt_of_deep` gives the local cut `CutAt`. Then `rowsDatum_at` gives the conclusion from `CutAt`, the finiteness of eligible terms (`eligFinite_of`) and the row representatives.

## In the Lean code

The theorem is in [CoefCutDeep.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/CoefCutDeep.lean#L72). The proof repeats the proof of `LsDatumB.rowsDatumP_of` in [LsDatumBCut.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/LsDatumBCut.lean#L201), with `cutAt_of_deep` added. The hypothesis is redundant: its only use, in [OffK0Closed.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/OffK0Closed.lean#L648), supplies `CutLeavesDeep_outright D`.
