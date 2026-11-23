---
id: sum-pt-of-wt-pt-num-pt
title: The oscillation bound from weight and number bounds, renamed
kind: theorem
decl: GlobalTheory.T.sum_pt_of_wt_pt_num_pt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.SumPtOfSizesStatement
covers: 704
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It restates [sumPt_of_sizes_alt](/entry/sum-pt-of-sizes-alt/) with the same statement. Its only caller is [sumPt_of_size_alt](/entry/sum-pt-of-size-alt/), which feeds it the two level statements `WtPtAlt` and `NumPtAlt`. Below this theorem are 704 declarations.

## Statement

**Theorem.** `WtPtAlt` and `NumPtAlt` imply `SumPtAlt`.

`SumPtAlt` is stated in [sum_pt_of_size](/entry/sum-pt-of-size/). `WtPtAlt` bounds the entries of each weight $u$ with `Quo` against the scale $b$, and `NumPtAlt` relates the scales of the point to `unitE`. Both are stated in full in [sumPt_of_sizes_alt](/entry/sum-pt-of-sizes-alt/).

## Proof

The proof is `first | exact @sumPt_of_sizes_alt | ...`. The tactic tries `exact` with [sumPt_of_sizes_alt](/entry/sum-pt-of-sizes-alt/) first. There is no other step.

## In the Lean code

The theorem is at [SumPtOfSizesStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SumPtOfSizesStatement.lean#L12).

- The name says "wt pt" and "num pt" for `WtPtAlt` and `NumPtAlt`. The file name says "sizes", as in `sumPt_of_sizes_alt`.
- The content is in [sumAt_of_sizes](/entry/sum-at-of-sizes/), which proves the bound at one point.
