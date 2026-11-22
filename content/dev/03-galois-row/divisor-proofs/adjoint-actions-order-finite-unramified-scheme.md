---
id: adjoint-actions-order-finite-unramified-scheme
title: The scheme of adjoint actions of an order is finite and unramified (statement form)
kind: theorem
decl: GlobalTheory.T.adjointActions_order_finite_unramified_scheme
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.AdjointActionsOrderFiniteUnramifiedSchemeStatement
covers: 605
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [the finiteness of the scheme of adjoint actions](/entry/act-rep-finite-unramified/); the finiteness itself is proved in [`exists_actRep_finite`](/entry/exists-act-rep-finite/). Its users, under [the quasi-projective representing family](/entry/exists-rep-fam-qproj/), are [the representability of principal Siegel objects with an order action](/entry/act-sieg-exists-rep/) and `GlobalTheory.UPel.HT.exists_finite_rep_oActN_rosati`.

## Statement

Let $S$ be locally noetherian and $A/S$ an abelian scheme with a line bundle $Q$ on $A \times_S A$, rigidified along $0 \times A$ and $A \times 0$, symmetric, with $\Delta^* Q$ relatively ample. Let $O$ be a ring with an additive map $a \mapsto \bar a$, a $\mathbb{Z}$-spanning family $b_1, \dots, b_r$, and an integer matrix $W$ with $W + W^{\mathsf T}$ positive definite and $\sum_{i,j} W_{ij}\, b_j \bar b_i = d > 0$.

**Theorem.** There is a finite, formally unramified $H \to S$ that represents right actions of $O$ on pullbacks of $A$ that are adjoint to the bar map for $Q$, in the sense of [the Zarhin data](/entry/exists-zarhin-data-sieg-ker-by/).

## Proof

The statement is the same as that of `GlobalTheory.EndLoc.actRep_finite_unramified`, and the proof applies it.

## In the Lean code

The theorem is in [AdjointActionsOrderFiniteUnramifiedSchemeStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/AdjointActionsOrderFiniteUnramifiedSchemeStatement.lean#L11); the proof is `first | (exact @GlobalTheory.EndLoc.actRep_finite_unramified) | ...`. $H$ is the structure `ActRep` in [ToRingActOpOfRingAct.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ToRingActOpOfRingAct.lean#L22).

Both users discard "formally unramified": the patterns are `⟨R, hfin, -⟩` in [ExistsFiniteRepRosatiOrderActionsSiegel.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsFiniteRepRosatiOrderActionsSiegel.lean#L47) and `⟨R, hRf, -⟩` in [ExistsRepPrincipalSiegelAdjointOrderAction.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsRepPrincipalSiegelAdjointOrderAction.lean#L125).
