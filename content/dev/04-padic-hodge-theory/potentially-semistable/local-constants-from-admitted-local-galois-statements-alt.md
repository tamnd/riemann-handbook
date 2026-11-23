---
id: local-constants-from-admitted-local-galois-statements-alt
title: The local lifting statements from the admitted conditions, the proof term
kind: theorem
decl: GlobalTheory.localConstants_from_admitted_local_Galois_statements_alt
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.LocalConstantsFromAdmittedLocalGaloisStatements
covers: 542
status: drafted
drafted_by: writer@claude
---
This theorem is the proof of [`localConstants_from_admitted_local_Galois_statements`](/entry/local-constants-from-admitted-local-galois-statements/), which has the same statement. It passes its data to [`frobenius_lifting`](/entry/frobenius-lifting/) together with a proof that the admitted conditions hold. `frobenius_lifting` is only a pass-through to [`local_theory_of_admitted`](/entry/local-theory-of-admitted/). The real content is in `local_parts_of_admitted`, in `lifting_all_parts_of_admitted` and in the proof of the admitted conditions.

## Statement

The same as [the parent entry](/entry/local-constants-from-admitted-local-galois-statements/): under `BlochKatoLocal`, `LocalTateDualityK` and `LocalEulerCharK`, for each datum $D$ of type `D7` and local data $HW$, $F$, $Cm$ over it, the statement `LiftingTheory.aux₃ D HW F 10 23 32 32` holds.

## Proof

The three hypotheses are discarded. Fix $D$, $HW$, $F$, $Cm$.

1. `liftingTheorem_wachModuleLemma_hypotheses_admitted` proves `LiftingTheory.admitted D HW F Cm` and `CrystallineLiftingBounds.admitted D HW F Cm`. It is a second name of `LiftAdmitted.all_admitted`, which proves the 23 conditions `adm1`, …, `adm23` from `wachLattice_laterClauses_hold`, `HerrExtUnit.main`, `herr_part_a_every_record`, a Fontaine bound and `jumps_exact_adm`. Only the first conjunct is kept.
2. `frobenius_lifting D HW F Cm` is the implication `admitted → aux₃` with the constants $10, 23, 32, 32$. It is `local_theory_of_admitted`.

Apply 2 to 1.

## In the Lean code

The theorem is in [LocalConstantsFromAdmittedLocalGaloisStatements.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalConstantsFromAdmittedLocalGaloisStatements.lean#L11). The callees are `LiftingTheory.frobenius_lifting` in [BaseChangePreservesUnitaryOf.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/BaseChangePreservesUnitaryOf.lean#L4841) and `LiftAdmitted.all_admitted` in [LiftingTheoremWachModuleLemmaHypothesesAdmitted.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LiftingTheoremWachModuleLemmaHypothesesAdmitted.lean#L20). The conjunction `admitted` is in [LiftingTheory.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/LiftingTheory.lean#L653).

The proof is `fun _ _ _ D HW F Cm => …`: the hypotheses `BlochKatoLocal`, `LocalTateDualityK` and `LocalEulerCharK` are never used, and `all_admitted` does not take them. So the conclusion holds with no hypothesis, and the name "from admitted local Galois statements" is misleading. The admitted conditions are proved inside the Lean code by `all_admitted`; they are not hypotheses.
