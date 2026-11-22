---
id: global-lattice-index-theorem-of-length-bound-at-places
title: The congruence length bound at a point (named form)
kind: theorem
decl: GlobalTheory.T.globalLatticeIndexTheorem_of_lengthBoundAtPlaces
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.SelmerLengthBoundAtPointStatement
covers: 2223
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It gives the theorem [`SelmerBoundAtPoint.main`](/entry/selmer-bound-at-point-main/), which has the real content, a second name in the namespace `GlobalTheory.T`. It sits below the trunk step [EveryCharacter from theta integrals and local matching](/step/theta-local-matching/), which dominates it. Two lemmas call it: `splitCase_bound_at_point_of_admitted_items` and `boundAtPoint_all_localisations_of_objectConditions`, both in the folder `InertiaEigenvalues`.

## Statement

Assume global Artin reciprocity, local Tate duality and the local Euler characteristic formula for finite $\ell$-power torsion Galois modules over finite extensions of $\mathbb{Q}_\ell$. Let $D$ be a datum of type `D7`, $i$ a local index with prime $\ell$, $r$ and $\rho$ two families of representations of $G_E$ over a discrete valuation ring $\mathcal{O}$, $\pi$ a point, and $(\mathrm{row}, \mathrm{col})$ a partition of the places of $E$ above $\ell$. Assume the nineteen conditions of `SelmerBoundAtPoint.main` on these objects, among them the local length bound `LengthBoundAtPlaces` at the row places and the lift exponent bound `LiftExponentAtPlaces` at the column places. Then `GlobalLatticeIndexTheorem` holds: the congruence length of $\pi$ is at most the length of a Selmer group plus a sum of local terms.

The entry [`SelmerBoundAtPoint.main`](/entry/selmer-bound-at-point-main/) states the hypotheses and the bound in full.

## Proof

The proof is the term `GlobalTheory.SelmerBoundAtPoint.main`. Nothing else happens.

## In the Lean code

The theorem is in [SelmerLengthBoundAtPointStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SelmerLengthBoundAtPointStatement.lean#L11). The proof is the tactic `first | exact @GlobalTheory.SelmerBoundAtPoint.main | ...`, and the first branch closes the goal. The statement is word for word that of `SelmerBoundAtPoint.main`. The name says "global lattice index theorem", but the conclusion bounds a congruence length; no lattice index appears in it by that name. The name of the file says "Selmer length bound", which is closer to the content.
