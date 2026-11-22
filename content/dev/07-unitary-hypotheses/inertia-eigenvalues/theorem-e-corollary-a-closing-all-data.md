---
id: theorem-e-corollary-a-closing-all-data
title: The local lifting theorem and its corollary for all data, a second name
kind: theorem
decl: GlobalTheory.T.theoremE_corollaryA_closing_all_data
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.TheoremECorollaryAClosingAllDataStatement
covers: 1821
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the local lifting theorem and its corollary](/entry/thm-ecor-a-closing/). That entry has the content. Its user is [the fifteen local bounds along a family](/entry/nlink-close-main-alt-alt/), which applies it with the three literature hypotheses of the [third place hypotheses](/step/unitary-group-third-place-hypotheses-def/).

## Statement

**Theorem.** Assume `BlochKatoLocal`, local Tate duality `LocalTateDualityK` and the local Euler characteristic formula `LocalEulerCharK`. Then there is a real $C_0$ such that for each datum $D$ and all local data $HW$, $F$, $Cm$ over it:

1. `Conclusion1 D 800` holds: a lifting theorem for surjections of crystalline lattices, with an exponent bounded with the constant 800;
2. `Conclusion2 D C₂` holds for each $C_2 \ge C_0$: a bound on the cokernel of the map on $H^1_f$.

Both are stated in [the local lifting theorem and its corollary](/entry/thm-ecor-a-closing/).

## Proof

The proof applies `GlobalTheory.ThmECorA.closing`, which has the same statement. Nothing else happens.

## In the Lean code

The theorem is in [TheoremECorollaryAClosingAllDataStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TheoremECorollaryAClosingAllDataStatement.lean#L8). The proof is a `first | exact ... | ...` combinator with three tries. Each try applies the same lemma. The file has `set_option maxHeartbeats 1000000` (line 7), which a one-line proof does not need. The file is named as a statement file, but it imports the proof module (line 2) and only renames it.
