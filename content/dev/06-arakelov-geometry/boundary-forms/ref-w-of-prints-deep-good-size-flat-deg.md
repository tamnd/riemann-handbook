---
id: ref-w-of-prints-deep-good-size-flat-deg
title: The reference exponent bound, renamed
kind: theorem
decl: GlobalTheory.T.refW_of_prints_deepGood_size_flatDeg
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.RefinedSumWeightOfSizeLe
covers: 1367
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It restates [refinedSum_weight_of_size_alt](/entry/refined-sum-weight-of-size-alt/), in the same file, with the same statement. Its only caller is [the height lower bound](/entry/height-lower-bound-general-alt/), where it feeds the multiplicity constant. The content is in [refinedSum_weight_of_size_alt](/entry/refined-sum-weight-of-size-alt/). Below this theorem are 1,367 declarations, one more than below the theorem that it restates.

## Statement

**Theorem.** If `PublishedHodgeBundleTheorems`, `DeepGoodness`, `SizeCondition` and `FlatDegreeCondition` hold, then `ReferenceWeight` holds.

`ReferenceWeight` says: on each good cover $Y$ of a point at a level $i$, and for each weight $u$ with `Quo`, the reference exponents $r_q$ of the weight $u$ are bounded by numbers $e_q \ge 0$ with $L \sum_q e_q \log q \le C\,\mathrm{unitE}$. See [refinedSum_weight_of_size_alt](/entry/refined-sum-weight-of-size-alt/) for the full statement.

## Proof

The proof is the tactic

```
first | exact @refinedSum_weight_of_size_alt | exact refinedSum_weight_of_size_alt | (intros; apply refinedSum_weight_of_size_alt <;> assumption)
```

The first branch closes the goal. There is nothing else.

## In the Lean code

The theorem is at [RefinedSumWeightOfSizeLe.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RefinedSumWeightOfSizeLe.lean#L23).

- The name lists four inputs: "prints" (the bundle `PublishedHodgeBundleTheorems`), "deepGood", "size" and "flatDeg". The input `DeepGoodness` is not used by the theorem that this one restates: that theorem is the term `fun hP _ hS hF => ...`, which discards it. The term chains `sum_pt_of_size`, `reference_core_of_size_and_sum_point`, `refTheta_of_size_refCore` and `refW_of_prints_size_flatDeg_refTheta`.
- The `first | exact ...` pattern is the same in many `GlobalTheory.T` theorems of this folder. Each one gives a second name to a theorem in another namespace.
