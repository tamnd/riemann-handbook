---
id: exists-finite-scheme-adjoint-actions-abelian
title: Adjoint actions of an order are represented by a finite scheme (statement)
kind: theorem
decl: GlobalTheory.T.exists_finite_scheme_adjoint_actions_abelian
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsFiniteSchemeAdjointActionsAbelianStatement
covers: 599
status: drafted
drafted_by: writer@claude
---
This theorem is the statement form of [the finiteness of the scheme of adjoint actions](/entry/exists-act-rep-finite/). Its proof only calls that theorem. It gives the finiteness half of [the finite unramified result](/entry/act-rep-finite-unramified/).

## Statement

Use $S$, $A$, $Q$, $O$, $\bar{\ }$, $e_1, \dots, e_r$, $W$ and $d$ as in [the finite unramified result](/entry/act-rep-finite-unramified/), with the same hypotheses.

**Theorem.** There is a scheme $\pi \colon H \to S$ with a universal adjoint action of $O$ on $A_H$, and $\pi$ is finite.

The conclusion is the one of the parent without "formally unramified".

## Proof

The proof is one tactic line. It tries `exact GlobalTheory.ActFin.exists_actRep_finite` in two forms, and as a last choice introduces the variables and applies the same theorem. The real content is in [the finiteness entry](/entry/exists-act-rep-finite/).

## In the Lean code

The theorem is in [ExistsFiniteSchemeAdjointActionsAbelianStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsFiniteSchemeAdjointActionsAbelianStatement.lean#L11). It calls only `GlobalTheory.ActFin.exists_actRep_finite`. The two declarations have the same type, word for word. The file raises `maxHeartbeats` to 1,000,000 for this one line.
