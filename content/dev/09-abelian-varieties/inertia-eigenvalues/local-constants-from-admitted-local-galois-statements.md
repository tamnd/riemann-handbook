---
id: local-constants-from-admitted-local-galois-statements
title: The local lifting statements with fixed constants
kind: theorem
decl: GlobalTheory.T.localConstants_from_admitted_local_Galois_statements
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.LocalConstantsFromAdmittedLocalGaloisStatementsStatement
covers: 543
status: drafted
drafted_by: writer@claude
---
This theorem gives a family of local statements about Wach modules and lifts of lattice maps, with the constants $C = 10$, $C_A = 23$, $C_B = 32$, $C_K = 32$. It is a second name of [`localConstants_from_admitted_local_Galois_statements_alt`](/entry/local-constants-from-admitted-local-galois-statements-alt/). Eight theorems call it. It is in the spine under the trunk step [EveryCharacter from theta integrals and local matching](/step/theta-local-matching/). Its callers take the three hypotheses from fields `bk`, `tate` and `euler` of a record.

## Statement

**Theorem.** Assume `BlochKatoLocal`, local Tate duality `LocalTateDualityK` and the local Euler characteristic formula `LocalEulerCharK`. Let $D$ be a datum of type `D7`, and let $HW$, $F$, $Cm$ be local data over $D$ (a Wach module datum, a Fontaine datum and a comparison datum at each prime $\ell$). Then `LiftingTheory.aux₃ D HW F 10 23 32 32` holds.

`aux₃` is a conjunction of eight statements about the Wach module datum `(HW l).W K s LL h`, for all primes $\ell$, finite extensions $K$ of $\mathbb{Q}_\ell$, integers $s$ and coefficient fields $L$ with `Good K s LL`. They are `ConclusionL`, `ConclusionW`, `WachAnnihilatorAll`, `WachExponentRecursionAll`, `WachResultConstant` (with $C = 10$), `ConclusionH`, `ExistsUnitClasses` and `LiftTheoremAllCases`. The last one says that in cases A and B a surjective map of lattices with given jumps lifts with an explicit exponent, that the exponents are bounded with $C_A$, $C_B$, $C_K$, and that the lifts descend to subfields.

## Proof

The tactic `first | exact @X | …` closes the goal with $X$ = `localConstants_from_admitted_local_Galois_statements_alt`. Nothing else happens.

## In the Lean code

The theorem is in [LocalConstantsFromAdmittedLocalGaloisStatementsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalConstantsFromAdmittedLocalGaloisStatementsStatement.lean#L8). `aux₃` is in [LiftingTheory.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/LiftingTheory.lean#L589). We have not unfolded the eight clauses past their first level.

The name says "from admitted local Galois statements", but the three hypotheses are not used. See [the second name](/entry/local-constants-from-admitted-local-galois-statements-alt/). The real content is in [`frobenius_lifting`](/entry/frobenius-lifting/).
