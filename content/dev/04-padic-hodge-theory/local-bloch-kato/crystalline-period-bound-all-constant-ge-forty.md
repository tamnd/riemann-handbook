---
id: crystalline-period-bound-all-constant-ge-forty
title: The local lifting exponent for potentially crystalline lattices, restated
kind: theorem
decl: GlobalTheory.T.crystallinePeriodBound_all_constant_ge_forty
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.CrystallinePeriodBoundAllConstantGeFortyStatement
covers: 3069
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [the local lifting exponent](/entry/theorem-t-all-records/). It sits below [the closing of the local inputs](/entry/closing-local-inputs-main-alt-alt/). Its callers use it to get the local hypothesis `admT CT` for a constant $C_T \ge 40$. The content is in [the lifting step](/entry/lifting-step-theorem-t-of-bhatt-scholze-fontaine/) and [its proof](/entry/theorem-tclosing-main/).

## Statement

**Theorem.** Assume `BhattScholzeIntegral`, `FontaineBcris`, `BlochKatoLocal`, `LocalTateDualityK` and `LocalEulerCharK`. Then for each datum $D$, all local data $HW$, $F$, $Cm$ over it, and each integer $C \ge 40$, the statement `Conclusion2 D C` holds.

`Conclusion2 D C` says: for each prime $\ell$, a surjection $f \colon T_1 \to T_2$ of potentially crystalline lattices over $\mathbb{Q}_\ell$, with inertia acting through a set of at most $N$ characters and Hodge-Tate jumps in a set of at most $N + 1$ integers in $[-\eta, H]$, is onto on $H^1_f$ up to the factor $\ell^{C(Nr' + \eta(N + r'))}$, once $\ell > C(HN^2 + N^3)$. It is stated in full in [the local lifting exponent](/entry/theorem-t-all-records/).

## Proof

The proof is the term `GlobalTheory.InertiaEigenvalues.theoremT_all_records`. There is nothing else.

## In the Lean code

The theorem is at [CrystallinePeriodBoundAllConstantGeFortyStatement.lean line 11](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CrystallinePeriodBoundAllConstantGeFortyStatement.lean#L11). Its type is the type of `theoremT_all_records`, word for word. It is called in [Conclusion41OfHyp.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/Conclusion41OfHyp.lean#L35) and in [AdmG14OfAux.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AdmG14OfAux.lean#L25).

- The name speaks of a "crystalline period bound". The statement bounds a lifting exponent for $H^1_f$, not a period.
- Three of the five assumptions (`BlochKatoLocal`, `LocalTateDualityK`, `LocalEulerCharK`) and the datum $Cm$ are not needed: the proof one level down uses them only for a hypothesis that is then discarded. See [the local lifting exponent](/entry/theorem-t-all-records/).
