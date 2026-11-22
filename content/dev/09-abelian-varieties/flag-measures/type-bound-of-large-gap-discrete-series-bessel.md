---
id: type-bound-of-large-gap-discrete-series-bessel
title: The type bound from the gap hypotheses and Bessel realization, statement form
kind: theorem
decl: GlobalTheory.T.typeBound_of_largeGap_discreteSeries_bessel
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.TypePOfLargeGapDiscreteSeriesBesselStatement
covers: 2510
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`typeBound_of_gap`](/entry/type-bound-of-gap/). Its only user is [`rowsPos_typeP`](/entry/rows-pos-type-p/), which supplies both hypotheses. The content is in [`typeBound_of_gap`](/entry/type-bound-of-gap/).

## Statement

**Theorem.** If the gap bundle `GapIn.Hyp` holds and the Bessel realization `BesselOfW` holds, then the type bound `TypeP` holds.

`GapIn.Hyp` is the conjunction of four propositions: `BranchingSupport.HypsG`, the uniqueness `UniqGap` of Bessel maps for discrete series with a large gap, `LowKMultOneG` and `DsigHC`. `BesselOfW` says that a suitable equivariant function is a matrix coefficient composed with a Bessel map. `TypeP` is stated in full in [the entry above](/entry/rows-pos-type-p/).

## Proof

The proof is the term `GlobalTheory.TypeAsm.TopGap.typeBound_of_gap`. There is nothing else.

## In the Lean code

The theorem is at [TypePOfLargeGapDiscreteSeriesBesselStatement.lean line 6](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/TypePOfLargeGapDiscreteSeriesBesselStatement.lean#L6). The proof is a tactic `first | exact @… | exact … | (intros; apply … <;> assumption)` that tries three ways to close the goal with `typeBound_of_gap`. The two statements are the same, so the first way already fits. The file sets `maxHeartbeats` to 1,000,000 for this one line.
