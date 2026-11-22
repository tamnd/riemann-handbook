---
id: row-counts-of-labels-alt
title: The counting row from the label row, in the large base form
kind: theorem
decl: GlobalTheory.CountRowByName.row_counts_of_labels_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.RowCountsOfLabels
covers: 2598
status: drafted
drafted_by: writer@claude
---
This theorem moves [`row_counts_of_ties_alt`](/entry/row-counts-of-ties-alt/) into the form `Lg1`, which the record `AllRowsAlt` asks for. Its user is [`allRows_of_open0_alt`](/entry/all-rows-of-open0-alt/), which gets the field `c30` from it and from the open label row `o.lab`. That field gives the constants `c30` and `cIc` of [HypsAlt](/step/hyps-alt-def/), in branch 1 of [the unitary hypotheses node](/proof/unitary-hypotheses/). The real content is in `row_counts_of_ties_alt` and below it.

## Statement

Assume `SiegelWeilUnitaryConvergent` (in `HeckeCharacterZeroLocus.SiegelWeilU`). Let `KP` be a property of bases, $Q, Q'$ slots and $L_k$ a linkage of bundles. If `Lg1 KP Q Q' (fun S => RowLabelCondition S Lk)` holds, then `Lg1 KP Q Q' (fun S => CountsIrreducibilityConstants' S Lk)` holds.

Here `Lg1 KP Q Q' r` means: there is a slot $R$ with `LargeBaseCondition KP Q R` and $r(Q' \wedge R)$. The label row and the counting row are stated in the entry [`row_counts_of_ties_alt`](/entry/row-counts-of-ties-alt/).

## Proof

Keep the slot $R$ and the proof of the large base condition. Apply `row_counts_of_ties_alt` at the slot $Q' \wedge R$. This works because `RowLabelCondition S Lk` unfolds to the hypothesis of that theorem.

## In the Lean code

The theorem is at [RowCountsOfLabels.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowCountsOfLabels.lean#L13). The whole proof is the term

```
fun hSW _ _ _ Lk ⟨R, hR, h⟩ => ⟨R, hR, CountRow.row_counts_of_ties_alt hSW _ Lk h⟩
```

So the theorem only passes its hypotheses along. `RowLabelCondition` is defined at [RowGood.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowGood.lean#L27). The call site is [LinkROfIsLinked.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkROfIsLinked.lean#L79).
