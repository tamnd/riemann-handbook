---
id: has-semi-abelian-uniformisation-of-finite-ext
title: A uniformisation after a finite extension gives one over the base (statement)
kind: theorem
decl: GlobalTheory.T.hasSemiAbelianUniformisation_of_finiteExt
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.HasSemiAbelianUniformisationOfFiniteExtStatement
covers: 443
status: drafted
drafted_by: writer@claude
---
This theorem is a restatement of [`Mum.has_of_hasFin`](/entry/has-of-has-fin/), which has the real content. Its proof only calls that theorem. It is used twice in [`Mum.has_of_base`](/entry/has-of-base/): in step 5, for the data $D'$ of unitary PEL type, and in step 7, for the original data $D$.

## Statement

Let $R$ be a local domain that is noetherian, integrally closed, complete for its maximal ideal $\mathfrak{m}$ and of characteristic zero (`Base R`). Let $D$ be degeneration data over $R$ for $\mathfrak{m}$. Suppose `HasFin D`: there are a finite injective map $R \to R'$ to a local domain $R'$ that is again noetherian, normal and complete (`FinExt`), and a pullback $D'$ of $D$ over $R'$, such that `Has D'`. Then `Has D`: there are a semi-abelian scheme $G$ over $R$, a polarised abelian variety $A$ over the fraction field of $R$, and a uniformisation of $G$ by $D$.

The [entry for `has_of_base`](/entry/has-of-base/) unfolds `DegData` and `Has`.

## Proof

The proof is `Mum.has_of_hasFin`. It passes to a Galois closure of $R'$ over $R$ and descends the uniformised group along it.

## In the Lean code

The theorem is in [HasSemiAbelianUniformisationOfFiniteExtStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasSemiAbelianUniformisationOfFiniteExtStatement.lean#L12). The proof is the tactic `first | exact @GlobalTheory.Mum.has_of_hasFin | ...`. The two statements are identical, so `exact` with that theorem closes the goal. `Base`, `FinExt`, `Has` and `HasFin` are in [ExistsToricRankOne.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ExistsToricRankOne.lean#L25).
