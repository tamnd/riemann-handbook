---
id: loop-rows-of-rows-fin-dim-alt
title: The loop row bound for a selection of spectral ties
kind: theorem
decl: GlobalTheory.LoopRowsByName.loopRows_of_rowsFinDim_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.LoopRowsOfRowsFinDim
covers: 551
status: drafted
drafted_by: writer@claude
---
This theorem is a pass-through. It proves the loop row statement `LoopRowS 3 𝒞 sel`, which [`at_choice_alt`](/entry/at-choice-alt/) uses for `SelectionLpBound`. It passes its hypotheses to [`loopRows_of_large_gap_discreteSeries`](/entry/loop-rows-of-large-gap-discrete-series/), which dominates 549 of the 551 declarations below it. The content is in [`loop_rows_closed_gap`](/entry/loop-rows-closed-gap/).

## Statement

Let $\mathcal C$ be a family class. Assume `RowsFinDim`, `MassRatioUnderVolume D` for each datum $D$, a twist selection on $\mathcal C$, a selection `sel` of spectral ties, and `TuSize F` for each $F$ in $\mathcal C$. Then `LoopRowS 3 𝒞 sel` holds: it is [closed](/step/closed-def/) on $\mathcal C$ that, eventually, the sums of $|\langle v_{p_1}, v_{p_2} \rangle|$ over big pairs and over non-scalar pairs are small.

## Proof

One call to `loopRows_of_large_gap_discreteSeries`. Four inputs are theorems with no hypotheses: `hyp_of_uniqGap` and `BesselOfW` from `bessel_multiplicity_one_large_gap_and_whittaker_bessel`, `discreteSeriesCoef_pointwiseBound_unconditional` and `wuDecayOfGap`. The rank bound is the first part of `ranks_and_frame_of_tied_class_alt`, applied to the mass ratio and the twist selection. The other hypotheses go in directly.

## In the Lean code

The theorem is at [LoopRowsOfRowsFinDim.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LoopRowsOfRowsFinDim.lean#L11). It copies `loopRows_of_rowsFinDim` ([LoopRowOfFiniteDim.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/LoopRowOfFiniteDim.lean#L27)), with `TwistSelection` in place of `TSel`. The name mentions one of five inputs.
