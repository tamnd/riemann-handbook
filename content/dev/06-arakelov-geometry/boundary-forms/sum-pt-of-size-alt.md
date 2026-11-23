---
id: sum-pt-of-size-alt
title: The oscillation bound from the weight and number bounds
kind: theorem
decl: GlobalTheory.RefSum.sumPt_of_size_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.SumPtOfSize
covers: 732
status: drafted
drafted_by: writer@claude
---
This theorem proves `SumPtAlt`, the oscillation bound at the core level, from `SizeCondition`. Its only user is its renaming [sum_pt_of_size](/entry/sum-pt-of-size/), step 1 of [the reference exponent bound](/entry/refined-sum-weight-of-size-alt/). The proof combines two level statements and passes them to [sum_pt_of_wt_pt_num_pt](/entry/sum-pt-of-wt-pt-num-pt/). Below this theorem are 732 declarations.

## Statement

**Theorem.** `SizeCondition` implies `SumPtAlt`.

`SumPtAlt` is stated in [sum_pt_of_size](/entry/sum-pt-of-size/). `SizeCondition` is the level statement $\mathrm{Lifts}$ of `SizeAt`, a list of bounds for the scales of the point, for the main term $\mathrm{mainT}_i$, and for $L$ (`lenT`) and the weights with `Quo`.

## Proof

The proof is one term:

```
fun h => sum_pt_of_wt_pt_num_pt (weight_pt_of_size h) (numerical_point_statement_of_size h)
```

1. `weight_pt_of_size` gives `WtPtAlt`, bounds on the entries of each weight $u$ with `Quo`. It restates `DivWt.wt_pt_of_cov_size`.
2. `numerical_point_statement_of_size` gives `NumPtAlt`, bounds that relate the scales of the point to `unitE`. It restates `NumSizes.numPt_of_size'`.
3. [sum_pt_of_wt_pt_num_pt](/entry/sum-pt-of-wt-pt-num-pt/) turns the two into `SumPtAlt`.

The two statements of steps 1 and 2 are given in [sumPt_of_sizes_alt](/entry/sum-pt-of-sizes-alt/).

## In the Lean code

The theorem is at [SumPtOfSize.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SumPtOfSize.lean#L14).

- The hypothesis `SizeCondition` is not used. Both `wt_pt_of_cov_size` ([WtPtOfSize.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/WtPtOfSize.lean#L25)) and `numPt_of_size'` ([NumPtOfSize.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/NumPtOfSize.lean#L25)) are `fun _ => ...`. The first calls `wtPt_of_wtN_alt lift_weight_numerator`, the second `numPt_alt`; neither takes a hypothesis. So `SumPtAlt` holds outright, and the name "of size" says more than the proof uses.
- A copy with the older names is `sumPt_of_size : Size → SumPt` in [SumPointOfSize.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SumPointOfSize.lean#L10).
- The content is in [sumAt_of_sizes](/entry/sum-at-of-sizes/).
