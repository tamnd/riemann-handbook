---
id: pm-ex-of-prints-h
title: Existence of potential modularity towers from the published hypotheses
kind: theorem
decl: UpperTheory.V.HV.DescentVanishingReductions.pmEx_of_printsH
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.AdjointLiftingOfCohomology
covers: 389
status: drafted
drafted_by: writer@claude
---
This theorem proves `PMExAlt`, the existence of potential modularity towers, from the published hypotheses `HypothesesH'`. Its result goes to [`sp4In0_alt`](/entry/sp4-in0-alt/), which gives it to [`main4_alt`](/entry/main4-alt/) for the [chapter on VWin](/proof/vwin/). The proof only passes hypotheses along. The real content is in [`pm_exists_of_unramified_adjoint_lifting`](/entry/pm-exists-of-unramified-adjoint-lifting/).

## Statement

**Theorem.** `HypothesesH'` implies `PMExAlt`.

`PMExAlt` is stated in [`pm_exists_of_unramified_adjoint_lifting`](/entry/pm-exists-of-unramified-adjoint-lifting/). In short, it says that for each datum $D$, each tower of $D$ with the conditions `Fit` and `Deep` and each $\iota$, every space of deformations over a large enough coefficient ring has an ideal $J$ that makes it a potential modularity tower.

## Proof

The proof applies `pm_exists_of_unramified_adjoint_lifting` to two inputs.

1. `adjoint_lift_of_prints` builds the bundle `UnramifiedInputs` from `HypothesesH'`. The cohomology fields come from the literal automorphy part `hH.litN` and from `locPrints_of_litN`. The other fields come from `modU_of_printsH`, `levEx`, `lamEx` (with `local_class_field_theory_all_of_literal_automorphy`) and `b0Ex (phiAll (cohP_alt hN))`.
2. `adjoint_lifting_of_cohomology` proves `AdjointLiftingTheorem`, the vanishing of Bloch-Kato classes of the adjoint. It calls the lemma of the same name in `Th`, with `cohP_alt hH.litN`. That lemma calls `adjointLiftingTheorem_of_locPrints_of_core` with [`core_alt_bis`](/entry/core-alt-bis/).

We have not unfolded `modU_of_printsH`, `levEx`, `lamEx` and `b0Ex`.

## In the Lean code

The theorem is in [AdjointLiftingOfCohomology.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/AdjointLiftingOfCohomology.lean#L32). The two helpers are in the same file, at lines 27 and 31. The lemma `Th.adjoint_lifting_of_cohomology` is in [ThFinal.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/ThFinal.lean#L18). The two helpers are also used in the same file by `countII_and_countIII_of_printsH_of_sp4In`, which gives them to `rigSp4_alt`.
