---
id: cm-family-functionals-detect-low-coefficients
title: The CM family functionals detect the low coefficients, as a named statement
kind: theorem
decl: GlobalTheory.T.cmFamilyFunctionals_detect_lowCoefficients
module: Development.AbelianVarietyTheory.Proofs.ThetaShiftProofs.CmFamilyFunctionalsDetectLowCoefficientsStatement
covers: 803
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`detectQ_of_known`](/entry/detect-q-of-known/). It has the same statement, and its proof only applies that lemma. It sits below [`inputsNet_recPlus`](/entry/inputs-net-rec-plus/), in branch 2 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). Its two direct users are [`RunJoin.qAt_run`](/entry/q-at-run/), the proof of [`recursive_page_lattice_bound`](/entry/recursive-page-lattice-bound/), and `RunJoin.onto_of_page`. The real content is in the entry for `detectQ_of_known`.

## Statement

**Theorem.** Assume `Known`. Let $T$ be a core record with laws $h$, let $j$ be an index with `InR D j` and $j < m$, let $\kappa$ be a weight, and let $C_R$, $T_t$, $c$ be reals with $T_t > 0$ and $c > 0$. Assume `GamAt T` and $r \ge 3$. Then `DetectQ h j κ C_R T_t c` holds.

`DetectQ` says: a cusp form of weight $\kappa$ at level $j$ that is killed by the coefficient functional of every arc datum of the CM family has all its low Fourier-Jacobi coefficients equal to $0$. The entry for `detectQ_of_known` states it in full.

## Proof

The proof is `detectQ_of_known`, applied to the same arguments.

## In the Lean code

The theorem is in [CmFamilyFunctionalsDetectLowCoefficientsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/CmFamilyFunctionalsDetectLowCoefficientsStatement.lean#L9). The proof is `first | exact @GlobalTheory.ArcCM.detectQ_of_known | ...`, so the two statements are the same up to elaboration. `DetectQ` is in [CarchAt.lean](lean:Development/AbelianVarietyTheory/Definitions/ArchimedeanThetaValues/CarchAt.lean#L34).
