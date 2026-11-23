---
id: mumford-formal-endomorphism-algebraic
title: Formal endomorphisms of a Mumford uniformization are algebraic, second name
kind: theorem
decl: GlobalTheory.T.mumford_formalEndomorphism_algebraic
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.MumfordFormalEndomorphismAlgebraicStatement
covers: 380
status: drafted
drafted_by: writer@claude
---
This theorem is a second name. It restates [formalEnd_algebraic](/entry/formal-end-algebraic/) with the same type and proves it by that theorem. The real content is there (379 of the 380 declarations below this one). It lies below [EveryCharacter from the literature](/step/every-character-of-literature/). Its direct users are `GlobalTheory.Mum.GenericEnd.main`, about a ring that acts on the degeneration datum, and `GlobalTheory.MumAdj.exists_linHom_end`.

## Statement

Let $R$ be a complete noetherian normal local domain of characteristic $0$, with maximal ideal $\mathfrak m$ and fraction field $K$. Let $D$ be a degeneration datum over $R$, $A$ a polarized abelian variety over $K$, and $G$ a commutative semi-abelian group scheme over $R$ with a uniformization $U$ of $G$ by $D$ with generic fibre $A$. Let $(a, a', h, h')$ be an endomorphism datum of $D$, and let $b = (b_e)_{e \geq 0}$ be a formal endomorphism of $G$ over the thickenings $\operatorname{Spec} R/\mathfrak m^{e+1}$ that is compatible with $a$ and $h'$. Then there is a group endomorphism $g$ of $G$ whose restriction to each thickening is $b_e$.

The objects are defined in [the entry for formalEnd_algebraic](/entry/formal-end-algebraic/).

## Proof

The proof is `GlobalTheory.Mum.formalEnd_algebraic`, with no change.

## In the Lean code

The theorem is at [MumfordFormalEndomorphismAlgebraicStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/MumfordFormalEndomorphismAlgebraicStatement.lean#L12). The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)`, and each branch calls the same theorem. The users are at [ExistsGenericEndomorphismMumfordRingAction.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsGenericEndomorphismMumfordRingAction.lean#L18) and [UniformisedGroupsAdjointHomPairClosedForm.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UniformisedGroupsAdjointHomPairClosedForm.lean#L43).
