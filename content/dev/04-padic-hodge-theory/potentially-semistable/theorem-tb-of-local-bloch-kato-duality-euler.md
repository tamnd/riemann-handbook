---
id: theorem-tb-of-local-bloch-kato-duality-euler
title: Theorem TB from Bloch-Kato, Tate duality and the Euler characteristic, a second name
kind: theorem
decl: GlobalTheory.T.theorem_tb_of_local_blochKato_duality_euler
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.TheoremTbOfLocalBlochKatoDualityEulerStatement
covers: 627
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [theorem TB from three local inputs](/entry/aux-of-bloch-kato-tate-duality-euler-char/). That entry has the content. Five declarations below the step [EveryCharacter from theta integrals and local matching](/step/theta-local-matching/) use this name. Among them are [the closing of the twisted place bound](/entry/twisted-place-bound-closing/), where it is the input `admTB`, and [the closing of the local inputs](/entry/closing-local-inputs-main-alt-alt/).

## Statement

**Theorem.** Assume the local Bloch-Kato package (`BlochKatoLocal`), local Tate duality (`LocalTateDualityK`) and Tate's local Euler characteristic formula (`LocalEulerCharK`). Then for each datum $D$ (`D7`) and all local data $HW$, $F$, $Cm$ over it, `LocalSituation.Conclusion4 D HW F` holds.

`Conclusion4` says that two local statements, `TBat` and `TBeAt`, hold at each prime $\ell$ and each good triple $(K, s, L)$. They bound torsion classes in the cohomology of rank one twists. They are described in [the entry with the content](/entry/aux-of-bloch-kato-tate-duality-euler-char/).

## Proof

The proof applies `GlobalTheory.TheoremTBRecords.aux_of_blochKato_tateDuality_eulerChar`, which has the same statement. Nothing else happens.

## In the Lean code

The theorem is in [TheoremTbOfLocalBlochKatoDualityEulerStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TheoremTbOfLocalBlochKatoDualityEulerStatement.lean#L8). The proof is a `first | exact ... | ...` combinator with three tries. Each try applies the same lemma. The file has `set_option maxHeartbeats 1000000` (line 7), which a one-line proof does not need.

The statement takes $Cm$ (`CmpOf`), but `Conclusion4` does not mention it.
