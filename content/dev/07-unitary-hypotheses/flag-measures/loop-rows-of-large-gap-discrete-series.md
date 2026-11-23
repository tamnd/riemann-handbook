---
id: loop-rows-of-large-gap-discrete-series
title: The loop row bound from the gap and discrete series inputs (renaming)
kind: theorem
decl: GlobalTheory.T.loopRows_of_large_gap_discreteSeries
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.LoopRowsOfLargeGapDiscreteSeriesStatement
covers: 549
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`loop_rows_closed_gap`](/entry/loop-rows-closed-gap/). It adds no mathematics. Its only user is [the loop row bound for a selection of spectral ties](/entry/loop-rows-of-rows-fin-dim-alt/), which supplies four of its five inputs from theorems with no hypotheses. The proof is in the entry of the original.

## Statement

Assume the five inputs `GapIn.Hyp`, `BesselOfW`, `ThmBpDS`, `WuDecayOfGap` and `RowsFinDim`. Let $\mathcal C$ be a family class and `sel` a selection of spectral ties on $\mathcal C$. Assume `TuSize F` for each family $F$ in $\mathcal C$, and that the rank hypothesis `PX.RanksF F 3 (C_YL + 1) (1/4) 3 (1/2) C_Tu` is [closed](/step/closed-def/) on $\mathcal C$. Then `LoopRowS 3 𝒞 sel` holds.

`LoopRowS` is stated in the entry of the [original](/entry/loop-rows-closed-gap/).

## Proof

The proof is the term `loop_rows_closed_gap`, tried in three forms by a `first | exact @X | exact X | (intros; apply X <;> assumption)` tactic. The two statements are the same, so the first form works.

## In the Lean code

The theorem is at [LoopRowsOfLargeGapDiscreteSeriesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/LoopRowsOfLargeGapDiscreteSeriesStatement.lean#L16). The original is `GlobalTheory.LoopRowsCloseGap.loop_rows_closed_gap` in [LoopRowsOfLargeGapDiscreteSeries.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/LoopRowsOfLargeGapDiscreteSeries.lean#L121). The name points to two of the inputs: the gap hypothesis `GapIn.Hyp`, and `ThmBpDS`, whose file is in the folder `Statements/DiscreteSeriesShifts`. We have not unfolded `ThmBpDS`.
