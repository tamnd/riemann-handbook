---
id: local-lifting-theorem-b-hypotheses-admitted
title: The admitted conditions of theorem B, a second name
kind: theorem
decl: GlobalTheory.T.localLifting_theoremB_hypotheses_admitted
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.LocalLiftingTheoremBHypothesesAdmittedStatement
covers: 865
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`admissible_ranks_of_CMDatum`](/entry/admissible-ranks-of-cmdatum/), which has the proof. It is step 3 of [local lifting theorem B](/entry/theorem-b-closing/): it proves the 13 conditions `admitted` with fixed constants, so that the bound of theorem B can be applied.

## Statement

Assume `BlochKatoLocal` (a dimension formula, a rational duality and an integral duality at each local datum), local Tate duality `LocalTateDualityK`, and the local Euler characteristic formula `LocalEulerCharK` (Serre, *Galois Cohomology*, Chapter II, Section 5).

**Theorem.** For each datum $D$, Wach modules $HW$, Fontaine data $F$ and comparison data $C_m$, the conditions `admitted` hold with the constants

$$(C_R, C_A, C_B, C_K, C_\kappa) = (10, 23, 32, 32, 8).$$

The 13 conditions are listed in the entry of [`admissible_ranks_of_CMDatum`](/entry/admissible-ranks-of-cmdatum/).

## Proof

The proof is `exact admissible_ranks_of_CMDatum`, inside a `first` combinator with two fallback forms. The statements are the same, so the first form applies.

## In the Lean code

The theorem is in [LocalLiftingTheoremBHypothesesAdmittedStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalLiftingTheoremBHypothesesAdmittedStatement.lean#L8). The target is in [LocalLiftingTheoremBHypothesesAdmitted.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalLiftingTheoremBHypothesesAdmitted.lean#L26). `admitted` is defined in [ArcLiftingSetup.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/ArcLiftingSetup.lean#L527).

The name is accurate. The name of the target, which speaks of ranks and CM data, is not.
