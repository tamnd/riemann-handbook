---
id: exists-dual-abelian-scheme-poincare
title: An abelian scheme has a dual with a Poincaré bundle, second name
kind: theorem
decl: GlobalTheory.T.exists_dual_abelianScheme_poincare
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsDualAbelianSchemePoincareStatement
covers: 800
status: drafted
drafted_by: writer@claude
---
This theorem is a second name. It restates [exists_dual](/entry/exists-dual/) with the same type and proves it by that theorem. The real content is there (799 of the 800 declarations below this one). It is step 1 of the proof of [the dual abelian scheme with biduality](/entry/dual-abelian-scheme/). Two more theorems call it: `BidualAbelian.isDual_swap`, which applies it to the dual $B$ to get biduality, and `DualInjPull.triv_of_triv_pull`, over an algebraically closed field.

## Statement

Let $A$ be an abelian scheme over a scheme $S$. Then there are an abelian scheme $B$ over $S$ and a line bundle $P$ on $A \times_S B$ such that:

1. $P$ makes $B$ the dual of $A$ (`IsDual A B P`);
2. `DimLe A B`: for each morphism $T \to S$ and each $g$, if $A_T \to T$ is smooth of relative dimension $g$, then so is $B_T \to T$.

`IsDual` is defined in [the entry on the dual abelian scheme](/entry/dual-abelian-scheme/). That entry also notes that the statement asks for a scheme over every base, which may be more than the published results give.

## Proof

The proof is `GlobalTheory.DualExist.exists_dual`, with no change.

## In the Lean code

The theorem is at [ExistsDualAbelianSchemePoincareStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsDualAbelianSchemePoincareStatement.lean#L10). The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)`, and each branch calls the same theorem. The callers are at [DualAbelianSchemeExistsBiduality.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/DualAbelianSchemeExistsBiduality.lean#L31), [IsDualAbelianSchemePoincareSwap.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsDualAbelianSchemePoincareSwap.lean#L97) and [AdditiveFamilyTrivialOfQuotientPullbackTrivial.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/AdditiveFamilyTrivialOfQuotientPullbackTrivial.lean#L52).
