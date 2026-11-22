---
id: s-lp-s-o-h-tf-of-siegel-weil
title: Three rows at every slot, from Siegel-Weil
kind: theorem
decl: GlobalTheory.LocalRows.sLp_sO_hTF_of_siegelWeil
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.AtChoice
covers: 13600
status: drafted
drafted_by: writer@claude
---
This theorem is a wrapper. It turns the three properties of [`at_choice_alt`](/entry/at-choice-alt/), which hold for every selection, into three rows, which hold for every slot and linkage. Its user is [`lg1_sLp_sO_hTF`](/entry/lg1-s-lp-s-o-h-tf/). The real content is in `at_choice_alt`, and most of it in [`offDiag`](/entry/carrier-gap-off-diag/).

## Statement

Assume `SiegelWeilUnitaryConvergent` (in `HeckeCharacterZeroLocus.SiegelWeilU`). Let $Q$ be a slot and $L_k$ a linkage of bundles. Then

1. `SlotLpCondition Q Lk`, that is `Row Q Lk SelectionLpBound`;
2. `SlotOrderCondition Q Lk`, that is `Row Q Lk SelectionOrderBound`;
3. `SlotTorsionFreeCondition Q Lk`, that is `Row Q Lk (fun 𝒜 _ => H_hTF 𝒜)`.

`Row Q Lk H` says: there is a property $E$ of bundles that, eventually, each bundle at a point of $Q$ linked by $L_k$ has; and $H(\mathcal A, \sigma)$ holds for each family class $\mathcal A$ and each selection $\sigma$ of such bundles with property $E$. The three properties $H$ are stated in the entry [`at_choice_alt`](/entry/at-choice-alt/).

## Proof

`Row.of_sel` proves `Row Q Lk H` when $H(\mathcal A, \sigma)$ holds for each selection $\sigma$ built from bundles of $Q$ and $L_k$. It takes for $E$ the property that is always true. `at_choice_alt` gives each of the three properties for every $\mathcal A$ and every $\sigma$, so `Row.of_sel` applies three times. The rest is bookkeeping.

## In the Lean code

The theorem is at [AtChoice.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AtChoice.lean#L24). The three rows are defined in [CountsIrreducibilityConstants.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CountsIrreducibilityConstants.lean#L95). `Row.of_sel` is in [ValidForConstructedPointClassesEventuallyWorking.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/ValidForConstructedPointClassesEventuallyWorking.lean#L324).

The proof ignores the fact that $\sigma$ is a selection for $Q$ and $L_k$. So the slot and the linkage play no role: the rows hold because the properties hold for every selection. The third property does not depend on $\sigma$ at all.
