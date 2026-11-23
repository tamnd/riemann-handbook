---
id: div-one-holds
title: A small representation inside one geometric representation
kind: theorem
decl: UpperTheory.Gal.Int.Div.divOne_holds
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.IntegralStructures.ZetaCharacterDivisibility.DivisionOneGeometricRepresentation
covers: 501
status: drafted
drafted_by: writer@claude
---
This theorem proves `DivOne`. Its user is [divAll_holds](/entry/div-all-holds/), which explains `VBase`, `IsDivRep`, `Inside` and `Covers`. `DivOne` takes one representation $\rho$ from [GeoOne](/step/geo-one-def/) and gives a representation $r$ of dimension $a$ inside it, with the Satake polynomials as Frobenius characteristic polynomials. The group theory is in [divSet_holds](/entry/div-set-holds/). This theorem supplies the dense set of Frobenius elements that `DivSet` needs, and reads off the characteristic polynomials. Below it are 501 declarations.

## Statement

Let $E$ be a CM field, $\ell$ a prime, $a, d \in \mathbb{N}$ with `ImQ E d`, $U$ an automorphic space on $U_a$, and $\psi$ a character with `IsDetChar ι U ψ`.

**Theorem.** For each $\rho$ with `VBase ι d U ρ` there is $r : G_E \to \mathrm{GL}_a(\overline{\mathbb{Q}}_\ell)$ with `IsDivRep ι d U r`, `Inside r ρ` and `Covers r ρ`.

## Proof

The proof is `divOne_of` applied to `divSet_holds` and four facts. The proof of `divOne_of` goes like this.

1. `VBase` gives a finite set $X$ of places and the condition `ESAt` outside $X$. The Satake multiset `algSat` has $a$ elements, by `HasSatGL.card`.
2. `DenseUs` says that the Frobenius elements at the places `UsPl d` outside $X$, prime to $\ell$ and with Satake parameters, are dense in $G_E$. So their inverses are dense too.
3. For such an inverse $g$, take $Q = \prod (X - \iota^{-1} b)$ over `algSat`. It is monic of degree $a$, and `ESAt` says that $Q(\rho(g)) = 0$. `DetFrob` says that $\iota\,\psi(g) = \prod b$, and this gives $\psi(g) = (-1)^a Q(0)$.
4. `DivSet` then gives $r$ with `Inside r ρ` and `Covers r ρ`, and with an open dense set of $g$ where the characteristic polynomial of $r(g)$ is separable. Take $V$ as the inverse of this set.
5. `InFacts` says that the kernel of $\rho$ is in the kernel of $r$, and that a polynomial that kills $\rho(g)$ kills $r(g)$. So $r$ is trivial on inertia, and $Q$ kills $r(s^{-1})$ for a Frobenius $s$.
6. `SepPin` says that if a monic $Q$ of degree $a$ kills a matrix with a separable characteristic polynomial, then $Q$ is that polynomial. This gives the characteristic polynomial of $r(s^{-1})$ for $s \in V$.

## In the Lean code

The theorem is in [DivisionOneGeometricRepresentation.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/ZetaCharacterDivisibility/DivisionOneGeometricRepresentation.lean#L53). `divOne_of` is in [PDivOne.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/ZetaCharacterDivisibility/PDivOne.lean#L35). `DivOne`, `DenseUs`, `DetFrob`, `InFacts` and `SepPin` are in [PhiOfDivOf.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/ZetaCharacterDivisibility/PhiOfDivOf.lean#L131). `SepPin` has an elementary proof in [PSepPin.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/ZetaCharacterDivisibility/PSepPin.lean#L8). We have not opened the proofs of `DenseUs` and `DetFrob`. By its statement, `DenseUs` is a density result of Chebotarev type for this set of places.
