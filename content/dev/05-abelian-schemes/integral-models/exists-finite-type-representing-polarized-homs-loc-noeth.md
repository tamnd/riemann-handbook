---
id: exists-finite-type-representing-polarized-homs-loc-noeth
title: Homomorphisms that respect two line bundles form a scheme of finite type (statement)
kind: theorem
decl: GlobalTheory.T.exists_finiteType_representing_polarizedHoms_locNoeth
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsFiniteTypeRepresentingPolarizedHomsLocNoetStatement
covers: 455
status: drafted
drafted_by: writer@claude
---
This theorem is the statement form of [the gluing over affine opens](/entry/hom-fix-finite-type/). Its proof only calls that theorem. It is step 1 of [the finiteness of polarized homomorphisms](/entry/exists-finite-unramified/), which adds properness and unramifiedness to get a finite scheme.

## Statement

Let $S$, $A$, $B$, $L$, $M$ be as in [the statement of the finite case](/entry/exists-finite-unramified-representing-polarized-homs/): $S$ locally noetherian, $A$ and $B$ abelian schemes over $S$, $L$ and $M$ rigidified and relatively ample line bundles on them.

**Theorem.** There is a scheme $\pi \colon H \to S$ that represents the homomorphisms $\Phi \colon A_T \to B_T$ with $\Phi^*M_T \cong L_T$ (a `HomFixRep A B L M`), with $\pi$ quasi-compact, separated and locally of finite type.

## Proof

The proof is one tactic line that applies `GlobalTheory.HomFixGlue.homFix_finiteType`, which has the same type. The content is in [that entry](/entry/hom-fix-finite-type/).

## In the Lean code

The theorem is in [ExistsFiniteTypeRepresentingPolarizedHomsLocNoetStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsFiniteTypeRepresentingPolarizedHomsLocNoetStatement.lean#L11). It calls only `GlobalTheory.HomFixGlue.homFix_finiteType`. The suffix "locNoeth" refers to the hypothesis that $S$ is locally noetherian; the module name shortens it to "LocNoet".
