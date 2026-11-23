---
id: frobenius-lifting
title: The local lifting statements from the admitted conditions
kind: theorem
decl: Formalism.MainNotions.LiftingTheory.frobenius_lifting
module: Formalism.SharpRestriction.LevelLetterCocycles.BaseChangePreservesUnitaryOf
covers: 541
status: drafted
drafted_by: writer@claude
---
This theorem gives the local theory with the constants $10, 23, 32, 32$. Its callers are [the local constants from the admitted local Galois statements](/entry/local-constants-from-admitted-local-galois-statements-alt/) and `local_theory_closed_form`, which puts the four constants into the existential statement `RealisationStatementAll`. The proof is one application of [the local theory from the admitted conditions](/entry/local-theory-of-admitted/).

## Statement

Let $D$ be a datum of type `D7`, and let `HW`, `F` and `Cm` be data of types `HWOf`, `FonOf` and `CmpOf` over it. The condition `admitted D HW F Cm` is the conjunction of the 23 conditions `adm1` to `adm23`. The conclusion `aux₃` is a conjunction of eight local statements, listed in [the next entry](/entry/local-theory-of-admitted/).

**Theorem.** For all `D`, `HW`, `F` and `Cm`, `Stmt D HW F Cm 10 23 32 32` holds, that is `admitted D HW F Cm` implies `aux₃ D HW F 10 23 32 32`.

## Proof

The proof is `fun h => local_theory_of_admitted D HW F Cm h`.

## In the Lean code

The theorem is in [BaseChangePreservesUnitaryOf.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/BaseChangePreservesUnitaryOf.lean#L4841). `Stmt`, `admitted` and `aux₃` are in [LiftingTheory.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/LiftingTheory.lean#L658).

The parent entry says that the real content is in `frobenius_lifting`. But this theorem is a pass-through, and `local_theory_of_admitted` is an assembly. The content is in the lemmas that the assembly calls. The namespace `CrystallineLiftingBounds` in the same file has a second `frobenius_lifting` at line 4859, with the three constants $23, 32, 32$ and a different `Stmt`.
