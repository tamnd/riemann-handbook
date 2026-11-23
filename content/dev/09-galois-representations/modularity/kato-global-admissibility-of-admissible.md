---
id: kato-global-admissibility-of-admissible
title: An admissible functional on the tower, from an admissible Hecke projection
kind: theorem
decl: UpperTheory.V.Z.Kato.Joint.kato_global_admissibility_of_admissible
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.KatoQuadraticCharacters.FrobeniusHodgeTateLaws.KatoGlobalAdmissibilityOfAdmissible
covers: 1405
status: drafted
drafted_by: writer@claude
---
This theorem turns the statement $\mathrm{AdmTop}$ into the statement $\mathrm{AdmFR}$. [The theorem on zeta classes with Iwasawa data](/entry/kato-global-unit-law-of-smoothed-classes/) uses $\mathrm{AdmFR}$ as one input of `glue2`. The proof only passes its hypothesis to `admissibleFunctional_of_projection`, with two proved statements and 13 further proved inputs. The main input is [the Hecke projector onto the newform part](/entry/hecke-projector-newform-galois-image/).

## Statement

**Theorem.** If $\mathrm{AdmTop}$ holds, then $\mathrm{AdmFR}$ holds.

$\mathrm{AdmTop}$ says: a Hecke idempotent on the cohomology of a modular tower, with equivariant projections and sections, and a functional with Hecke eigen congruences, give an integral, Galois equivariant projection to $\overline{\mathbb{Q}}_\ell^2$ with the Hecke eigenvalues of the newform.

$\mathrm{AdmFR}$ says: for an ordinary normal form $W$, an ordinary newform $g$ of weight $2e+1$ attached to a twist of $W$, and an Eisenstein eigenform of level $N \ge 5$ with $\ell \nmid N$, there are an integral, $\mathbb{Z}_\ell$-linear, Galois equivariant projection with eigenvalues $a_q(g)$ for $T_q$ and $\alpha$ for $U_\ell$, a diamond character, an admissible functional $\lambda$ and a constant $\kappa \neq 0$.

## Proof

Apply `admissibleFunctional_of_projection` to $\mathrm{AdmTop}$ and to:

- `heckeProjector_newform_galoisImage`: a newform of odd weight $k \ge 3$ with an ordinary root $\alpha$ and an irreducible Galois representation with its Frobenius traces has a Hecke projector onto its part of the tower cohomology. It only calls `heckeProj_newform`.
- `untwisted_representation_ordinary_triangular_shape`: the untwisted representation is continuous and upper triangular on the decomposition group, with the expected diagonal on inertia.

## In the Lean code

The theorem is in [KatoGlobalAdmissibilityOfAdmissible.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/FrobeniusHodgeTateLaws/KatoGlobalAdmissibilityOfAdmissible.lean#L35). $\mathrm{AdmTop}$ and $\mathrm{AdmFR}$ are in [ThickFrames.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/FrobeniusHodgeTateLaws/ThickFrames.lean#L54).

- `admissibleFunctional_of_projection`, in [AdmissibleFunctionalOfProjection.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/FrobeniusHodgeTateLaws/AdmissibleFunctionalOfProjection.lean#L36). Its type $\mathrm{AdmOf2}$ has 16 hypotheses.
- `GlobalTheory.T.heckeProjector_newform_galoisImage`, in [HeckeProjectorNewformGaloisImageStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/HeckeProjectorNewformGaloisImageStatement.lean#L9).
- `GlobalTheory.T.untwisted_representation_ordinary_triangular_shape`, in [UntwistedRepresentationOrdinaryTriangularShapeStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/UntwistedRepresentationOrdinaryTriangularShapeStatement.lean#L8).
- 13 further inputs, from `jEx` to `aqBd`, which we have not opened.

This is a pass-through. Despite its name, it adds no argument of its own.
