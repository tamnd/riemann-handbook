---
id: lg1-s-lp-s-o-h-tf
title: Three rows in the large base form, from Siegel-Weil
kind: theorem
decl: GlobalTheory.LocalRows.lg1_sLp_sO_hTF
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.AtChoice
covers: 13601
status: drafted
drafted_by: writer@claude
---
This theorem is a wrapper. It puts the three rows of [`sLp_sO_hTF_of_siegelWeil`](/entry/s-lp-s-o-h-tf-of-siegel-weil/) into the form `Lg1`, which the record `AllRowsAlt` asks for. Its user is [`allRows_of_open0_alt`](/entry/all-rows-of-open0-alt/), which takes the fields `sLp`, `sO` and `hTF` from it. The real content is in [`at_choice_alt`](/entry/at-choice-alt/) and, below that, in [`offDiag`](/entry/carrier-gap-off-diag/).

## Statement

Assume `SiegelWeilUnitaryConvergent` (in `HeckeCharacterZeroLocus.SiegelWeilU`). Let `KP` be a property of bases, $Q, Q'$ slots and $L_k$ a linkage of bundles. Then the three statements

`Lg1 KP Q Q' (fun S => SlotLpCondition S Lk)`, `Lg1 KP Q Q' (fun S => SlotOrderCondition S Lk)`, `Lg1 KP Q Q' (fun S => SlotTorsionFreeCondition S Lk)`

hold. Here `Lg1 KP Q Q' r` means: there is a slot $R$ with `LargeBaseCondition KP Q R` and $r(Q' \wedge R)$. The three rows are stated in the entry [`sLp_sO_hTF_of_siegelWeil`](/entry/s-lp-s-o-h-tf-of-siegel-weil/).

## Proof

Take for $R$ the slot that is always true. `largeBaseProperty_true` proves `LargeBaseCondition KP Q R` for it. Then `sLp_sO_hTF_of_siegelWeil` gives each row at the slot $Q' \wedge R$. The rest is bookkeeping.

## In the Lean code

The theorem is at [AtChoice.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AtChoice.lean#L27). It calls `sLp_sO_hTF_of_siegelWeil` (line 24) and `largeBaseProperty_true` in [EventuallyAllScaleContextsAndOfBoth.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/EventuallyAllScaleContextsAndOfBoth.lean#L91).

The statement holds for every `KP`, $Q$, $Q'$ and $L_k$. This is possible because the large base condition is free for the true slot, and because the rows below hold for every slot and linkage. So the proof uses no property of the slots or of the linkage. The name lists the three fields `sLp`, `sO` and `hTF` that it fills.
