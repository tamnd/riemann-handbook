---
id: lie-sheaf-semi-abelian-semi-neg-of-is-alg-closed
title: The Lie algebra of a semi-abelian scheme is seminegative over an algebraically closed field
kind: theorem
decl: GlobalTheory.T.lieSheaf_semiAbelian_semiNeg_of_isAlgClosed
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.LieSheafSemiAbelianSemiNegOfIsAlgClosedStatement
covers: 424
status: drafted
drafted_by: writer@claude
---
This theorem is a second name. It restates [semiNeg_lie_of_isAlgClosed](/entry/semi-neg-lie-of-is-alg-closed/) with the same type and proves it by that theorem. Its one use is step 2 of the proof of [the case over any field of characteristic 0](/entry/semi-abelian-lie-seminegative/), which applies it over an algebraic closure. The real content is in `semiNeg_lie_of_isAlgClosed` (423 of the 424 declarations below this one).

## Statement

Let $k$ be an algebraically closed field of characteristic $0$, and let $C$ be a smooth projective geometrically connected curve over $k$ (`IsCurve k C`). Let $G$ be a semi-abelian group scheme over $C$. Then $\mathrm{Lie}\,G$ is seminegative: each vector bundle $W$ with a monomorphism $W \to \mathrm{Lie}\,G$ has $\deg \det W \leq 0$.

The words "semi-abelian" and "seminegative" are defined in [the entry above](/entry/semi-abelian-lie-seminegative/).

## Proof

The proof is `GlobalTheory.Nef.semiNeg_lie_of_isAlgClosed`, with no change.

## In the Lean code

The theorem is at [LieSheafSemiAbelianSemiNegOfIsAlgClosedStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LieSheafSemiAbelianSemiNegOfIsAlgClosedStatement.lean#L13). The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)`, and each branch calls the same theorem. The file imports `Mathlib` twice, at lines 1 and 3. This has no effect.
