---
id: exists-finite-unramified
title: Homomorphisms that respect two line bundles form a finite unramified scheme
kind: theorem
decl: GlobalTheory.EndLoc.HomFixFinite.exists_finite_unramified
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsFiniteUnramifiedRepresentingPolarizedHoms
covers: 469
status: drafted
drafted_by: writer@claude
---
This theorem proves [its statement form](/entry/exists-finite-unramified-representing-polarized-homs/): the homomorphisms $\Phi \colon A \to B$ of abelian schemes with $\Phi^*M \cong L$ form a scheme that is finite and formally unramified over the base. It gets finiteness from three properties: finite type, properness and unramifiedness. [The scheme of adjoint actions](/entry/exists-act-rep-finite/) is cut out of this scheme.

## Statement

Let $S$, $A$, $B$, $L$, $M$ be as in [the statement form](/entry/exists-finite-unramified-representing-polarized-homs/): $S$ locally noetherian, $A$ and $B$ abelian schemes over $S$, $L$ and $M$ rigidified and relatively ample line bundles on them.

**Theorem.** There is a scheme $\pi \colon H \to S$ that represents the homomorphisms $\Phi \colon A_T \to B_T$ with $\Phi^*M_T \cong L_T$, and $\pi$ is [[finite|N9C4X7XKE4]] and [[formally unramified|1JQX6HD8E5]].

## Proof

1. [The finite type entry](/entry/exists-finite-type-representing-polarized-homs-loc-noeth/) gives a representing object $H$ with $\pi$ quasi-compact, separated and locally of finite type.
2. `GlobalTheory.EndLoc.HomFixProper.isProper_of_finiteType` proves that such a $\pi$ is [[proper|9537RKBZPP]]. It uses that $A$, $B$ are abelian, $L$, $M$ are rigidified line bundles, and $S$ is locally noetherian. It does not use the ampleness.
3. `GlobalTheory.T.formallyUnramified_homWithFixedPullback_scheme` proves that $\pi$ is formally unramified, for every representing object. It uses only that $A$ and $B$ are abelian.
4. `GlobalTheory.PropFin.isFinite_of_isProper_of_formallyUnramified`: over a locally noetherian base, a proper and formally unramified morphism is finite. Its proof shows that $\pi$ is locally quasi-finite (formally unramified and of finite type) and then applies Mathlib's `IsFinite.of_isProper_of_locallyQuasiFinite`, that is, a proper and quasi-finite morphism is finite (EGA IV$_3$, Théorème 8.11.1).

## In the Lean code

The theorem is in [ExistsFiniteUnramifiedRepresentingPolarizedHoms.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsFiniteUnramifiedRepresentingPolarizedHoms.lean#L16). The lemmas it calls:

- `GlobalTheory.T.exists_finiteType_representing_polarizedHoms_locNoeth`;
- `GlobalTheory.EndLoc.HomFixProper.isProper_of_finiteType`, in [IsProperOfFiniteType.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsProperOfFiniteType.lean#L32), whose proof we have not read;
- `GlobalTheory.T.formallyUnramified_homWithFixedPullback_scheme`, whose proof we have not opened;
- `GlobalTheory.PropFin.isFinite_of_isProper_of_formallyUnramified`, in [IsFiniteOfIsProperOfFormallyUnramified.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsFiniteOfIsProperOfFormallyUnramified.lean#L15).

The relative ampleness of $L$ and $M$ enters only through step 1.
