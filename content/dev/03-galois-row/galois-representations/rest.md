---
id: rest
title: The Galois row from the spherical core
kind: theorem
decl: UpperTheory.Gal.Int.rest
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.IntegralStructures.Development
covers: 1944
status: drafted
drafted_by: writer@claude
---
This theorem proves the Galois row $\mathrm{Row0}$ from the statement $\mathrm{CoreAll}$, which gives the representations and their behaviour at spherical places. It is step 4 of the [Galois row chapter](/proof/galois-row/). Its result goes to [the Galois row from geometry and the theta lift](/entry/galois-local-global-of-geometry-lift/), which is `rest (coreAll_of ...)`. The proof is an assembly of three lemmas. Below this theorem are 1,944 declarations.

## Statement

$\mathrm{CoreAll}$ is the conjunction of two facts. Let $E$ be a CM field, $\ell$ a prime with $\iota \colon \overline{\mathbb{Q}}_\ell \to \mathbb{C}$, and $\pi$ a regular algebraic cuspidal representation of $\mathrm{GL}_n(\mathbb{A}_E)$ that is part of a polarized pair $(\pi, \chi)$.

1. There is a continuous representation $r \colon G_E \to \mathrm{GL}_n(\overline{\mathbb{Q}}_\ell)$ attached to $\pi$ (`Weak`: $r$ is continuous and semisimple, and its Frobenius characteristic polynomials match the Satake parameters of $\pi$ at almost all places).
2. For each such $r$ and each place $w$ where $\pi_w$ has Satake parameters $B$, four clauses hold: Frobenius eigenvalues given by $B$ (away from $\ell$), de Rham with the expected Hodge-Tate jumps, crystalline, and a crystalline Frobenius with the characteristic polynomial of the unramified class of $B$ (above $\ell$).

$\mathrm{Row0}$ is the variant of the Galois row that the [chapter](/proof/galois-row/) describes, with a slightly stronger local clause. The parameter `recT` restricts the local Langlands maps to those that satisfy [IsRecT](/step/is-rect-def/).

**Theorem.** $\mathrm{CoreAll}$ implies $\mathrm{Row0}(\mathrm{recT})$.

## Proof

1. `galoisCompat_unlinkedSupport_of_spherical` proves `R1` from $\mathrm{CoreAll}$ (238 declarations). `R1` is the compatibility at places $w$ where $\pi_w \otimes |\det|^{(1-n)/2}$ has a cuspidal support of characters with no two linked by $|\cdot|$.
2. `localGlobalCompatAtIwahoriFixed_of_unlinked` ([its entry](/entry/local-global-compat-at-iwahori-fixed-of-unlinked/)) proves the depth-zero clause `LocalGlobalCompatAtIwahoriFixedPlaces` from `R1` (1,522 declarations).
3. `galoisLocalGlobal_of_localGlobalCompatibility` combines $\mathrm{CoreAll}$, `R1` and the depth-zero clause into $\mathrm{Row0}$ (116 declarations). It takes $r$ from the first part of $\mathrm{CoreAll}$ and fills the local clauses from the three inputs.

Almost all of the content is in step 2.

## In the Lean code

The theorem is in [Development.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/Development.lean#L24). The proof is one term:

```
galoisLocalGlobal_of_localGlobalCompatibility h (galoisCompat_unlinkedSupport_of_spherical h)
  (localGlobalCompatAtIwahoriFixed_of_unlinked (galoisCompat_unlinkedSupport_of_spherical h))
```

The definitions:

- `CoreAll` in [CyclicStrongAtCusp.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/CyclicStrongAtCusp.lean#L96);
- `R1` in [IsQg.lean](lean:Development/AbelianVarietyTheory/Statements/EllipticCurveLevels/IsQg.lean#L13);
- the assembly lemma in [GaloisLocalGlobalOfLocalGlobalCompatibility.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/InertCharpoly/GaloisLocalGlobalOfLocalGlobalCompatibility.lean#L192).

The proof writes the term `galoisCompat_unlinkedSupport_of_spherical h` twice instead of naming it once. This is harmless. We have not unfolded `Row0`, `Props` and `exists_weights`.
