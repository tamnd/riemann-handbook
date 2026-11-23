---
id: bundle-both-parts-of-standard-kernel-of-global-artin-reciprocity
title: The service row from Artin reciprocity, restated
kind: theorem
decl: GlobalTheory.T.bundle_bothParts_of_standardKernel_of_globalArtinReciprocity
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.BundleBothPartsOfStandardKernelOfGlobalArtinReciStatement
covers: 10812
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`servH_row_of_artin`](/entry/serv-h-row-of-artin/). It has the same statement, and its proof applies that theorem. Its user is [`servH_row_linkR_alt`](/entry/serv-h-row-link-r-alt/), which applies it to the reciprocity linkage and so gives the service row of the record `AllRowsAlt` in [the unitary hypotheses node](/proof/unitary-hypotheses/). The content is in `servH_row_of_artin`, which dominates 10,811 of the 10,812 declarations below this theorem.

## Statement

Assume `GlobalArtinReciprocity`. Let $Q$ be a slot of constructed points, $L_k$ a linkage of bundles and `ker` a map that sends each bundle to a tied kernel entry. Suppose that every point of $Q$ has a part (`positionOf HasPart`), and that eventually every bundle that $L_k$ links has a standard tie for its kernel entry (`StdTie`). Then the row `Row Q Lk (ServH ker)` holds. The notions are explained in the entry [`servH_row_of_artin`](/entry/serv-h-row-of-artin/).

## Proof

Apply `servH_row_of_artin`. Nothing else is used.

## In the Lean code

The theorem is at [BundleBothPartsOfStandardKernelOfGlobalArtinReciStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/BundleBothPartsOfStandardKernelOfGlobalArtinReciStatement.lean#L7). Its proof is the tactic

```
first | exact @servH_row_of_artin | exact servH_row_of_artin | (intros; apply servH_row_of_artin <;> assumption)
```

(namespaces shortened), under `set_option maxHeartbeats 1000000`. The two statements are the same, so the first branch closes the goal and the theorem is a renaming. The name reads: the bundle has both parts (the two conjuncts of `ServH`) when its kernel is standard (`StdTie`), from global Artin reciprocity. The file name is cut short ("GlobalArtinReci").
