---
id: bundle-both-parts-of-standard-kernel-and-six-hypotheses
title: The service row from six hypotheses, restated
kind: theorem
decl: GlobalTheory.T.bundle_bothParts_of_standardKernel_and_six_hypotheses
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.BundleBothPartsOfStandardKernelAndSixHypothesesStatement
covers: 5806
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`servH_row`](/entry/serv-h-row/). It has the same statement, and its proof applies that theorem. Its user is [`servH_row_of_artin`](/entry/serv-h-row-of-artin/), which proves the six hypotheses from global Artin reciprocity and then applies this theorem. The content is in `servH_row`, which dominates 5,805 of the 5,806 declarations below this theorem.

## Statement

Assume the six statements `AlgTAll`, `GenusOneModelExistsLattice`, `CurveDict`, `IntInert`, `AdmAtEnt2` and `CurveEx`. Let $Q$ be a slot of constructed points, $L_k$ a linkage of bundles and `ker` a map from bundles to tied kernel entries. Suppose that every point of $Q$ has a part (`positionOf HasPart`), and that eventually every bundle that $L_k$ links has a standard tie for its kernel entry (`StdTie`). Then the row `Row Q Lk (ServH ker)` holds. The six statements are described in [`servH_row`](/entry/serv-h-row/), and `Row` and `ServH` in [`servH_row_of_artin`](/entry/serv-h-row-of-artin/).

## Proof

Apply `servH_row`. Nothing else is used.

## In the Lean code

The theorem is at [BundleBothPartsOfStandardKernelAndSixHypothesesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/BundleBothPartsOfStandardKernelAndSixHypothesesStatement.lean#L11). Its proof is the tactic

```
first | exact @servH_row | exact servH_row | (intros; apply servH_row <;> assumption)
```

(namespaces shortened), under `set_option maxHeartbeats 1000000`. The first branch closes the goal, so the theorem is a renaming. In `servH_row` the six hypotheses are named arguments; here they are unnamed arrows, in the same order.
