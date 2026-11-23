---
id: theorem-i-of-contraction
title: The base-level projection bound from the contraction statement
kind: theorem
decl: Formalism.MainNotions.flipOneThree.Pf.theorem_I_of_contraction
module: Formalism.SharpRestriction.GrowthBounds.HermitianTensor.ModelIdentificationHolds
covers: 922
status: drafted
drafted_by: writer@claude
---
This theorem reduces `SecondPartClosed D` to `ContractionStandardLattice`. It is a pass-through. It fills three inputs of [the version with two-letter clauses](/entry/theorem-i-of-two-letter-clauses-contraction/) with proved theorems and passes the contraction statement on. That theorem holds 921 of the 922 declarations below. The only caller is [the projection bound from a GL-invariant pairing](/entry/theorem-i-of-pairing-gl/), which proves the contraction statement by `contraction_of_pairing_GL`.

## Statement

`SecondPartClosed D` says that the admitted statements `AdmBE D` imply the base-level projection bound for $D$, with constants that can be taken large ([the closed form](/entry/theorem-i-closed-form-holds/)). `ContractionStandardLattice` is the statement described in [the parent entry](/entry/theorem-i-of-pairing-gl/): a $\mathrm{GL}$-equivariant contraction of dual Weyl modules, integral on lattices, with dual families $s_b, s'_b$.

**Theorem.** For each datum $D$, `ContractionStandardLattice` implies `SecondPartClosed D`.

## Proof

The proof is one line. It applies `theorem_I_of_two_letter_clauses_contraction` to $D$, to three theorems and to the hypothesis:

- `explicit_map_injective`: the substitution map $\Psi$ is injective;
- `explicit_map_onto_two_letter_space`: $\Psi$ maps the bihomogeneous polynomials of bidegree $(P, Q)$ onto the two-letter space;
- `two_letter_lattice_gauss_inverse`: a lattice condition on $\Psi(f)$ is the Gauss lattice condition on $f$ after the change of variables $g^{-1}$.

These three statements are spelled out in [the child entry](/entry/theorem-i-of-two-letter-clauses-contraction/).

## In the Lean code

The theorem is in [ModelIdentificationHolds.lean](lean:Formalism/SharpRestriction/GrowthBounds/HermitianTensor/ModelIdentificationHolds.lean#L22). The three statements are in [TieDefs.lean](lean:Formalism/SharpRestriction/GrowthBounds/HermitianTensor/TieDefs.lean#L13). The proofs are in [ExplicitMapOntoTwoLetterSpace.lean](lean:Formalism/SharpRestriction/GrowthBounds/HermitianTensor/ExplicitMapOntoTwoLetterSpace.lean#L34) (lines 34 and 144) and [TwoLetterLatticeGaussInverse.lean](lean:Formalism/SharpRestriction/GrowthBounds/HermitianTensor/TwoLetterLatticeGaussInverse.lean#L86).
