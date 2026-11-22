---
id: div-all-holds
title: One small representation for every geometric representation
kind: theorem
decl: UpperTheory.Gal.Int.Div.divAll_holds
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.IntegralStructures.ZetaCharacterDivisibility.DivisionOneGeometricRepresentation
covers: 661
status: drafted
drafted_by: writer@claude
---
This theorem proves `DivAll`. Its user is [seedFinOdd_of_geoOne](/entry/seed-fin-odd-of-geo-one/), which gets each representation $\rho$ from [GeoOne](/step/geo-one-def/). `DivAll` gives one representation $r$ of dimension $a$, and it moves each local property of each $\rho$ to this single $r$. The construction of $r$ from one $\rho$ is in [divOne_holds](/entry/div-one-holds/). This theorem adds the determinant, the uniqueness of $r$, and the transfer of the local clauses. Below it are 661 declarations.

## Statement

Let $E$ be a CM field, $\ell$ a prime, $\iota : \overline{\mathbb{Q}}_\ell \cong \mathbb{C}$, $a \geq 1$, $d$ with `ImQ E d`, and $U$ an automorphic space on $U_a$. Suppose that some $\rho$ has `VBase ι d U ρ`.

**Theorem.** There is $r : G_E \to \mathrm{GL}_a(\overline{\mathbb{Q}}_\ell)$ with `IsDivRep ι d U r` such that, for each $\rho$ with `VBase ι d U ρ` and each place $w$:

1. if $w$ is split and prime to $\ell$, $B$ is a Satake parameter of $U$ at $w$ with `GenericMul B`, and `ESAt` holds for $\rho$ at $w$, then `FrobEig` holds for $r$ at $w$;
2. if `CrysAt ρ w` and `JumpsOcc U ι ρ w`, then `CrysDRU U ι r w`;
3. if $w$ is split, `GenericMul B` holds, and `PhiKilled ι ρ w a B`, then `CrysAt r w` and `PhiPol ι r w B`.

`IsDivRep` says: $r$ is continuous and semisimple, and there are an open dense set $V$ and a finite set $X$ of places such that, at each place `UsPl d` outside $X$ and prime to $\ell$, $r$ is trivial on inertia and $\det(X - \iota\, r(s^{-1})) = \prod (X - \mathrm{algSat})$ for each Frobenius $s \in V$. `PhiPol` says that the characteristic polynomials of the Weil-Deligne class of $r$ and of the unramified class match at each Weil element.

## Proof

The proof is `divAll_of` applied to nine facts. The proof of `divAll_of` goes like this.

1. `DetEx` gives a character $\psi$ attached to $U$.
2. `DivOne` applied to the given $\rho_0$ and $\psi$ gives $r$ with `IsDivRep`. `DivDet` gives $\det r = \psi$.
3. For another $\rho$, `DivOne` gives $r'$ with `Inside r' ρ` and `Covers r' ρ`. `DivUniq` says $r' \cong r$, and `IsoMove` moves `Inside` and `Covers` to $r$.
4. Clause 1 comes from `FrobeniusCondition`. Clause 3 comes from `PhiSeed`. Clause 2 comes from `JumpCondition`, with `SubLoc` to pass the crystalline property from $\rho$ to the subrepresentation $r$.

`Inside r ρ` says that $r$ is a subrepresentation of $\rho$. `Covers r ρ` says that $\rho$ is a quotient of a sum of copies of $r$. We have not unfolded `FrobeniusCondition`, `JumpCondition` or `SubLoc`.

## In the Lean code

The theorem is in [DivisionOneGeometricRepresentation.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/ZetaCharacterDivisibility/DivisionOneGeometricRepresentation.lean#L54). `DivAll` and `IsDivRep` are in [InsideRefl.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/ZetaCharacterDivisibility/InsideRefl.lean#L107). `divAll_of`, `DivOne`, `DivUniq` and `DivDet` are in [PhiOfDivOf.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/ZetaCharacterDivisibility/PhiOfDivOf.lean#L166). The file of the theorem also proves `subLoc_holds`, `phiSeed_holds`, `centU_holds`, `detEx_holds` and `divDet_holds` at lines 46 to 50, and `divAll_holds` uses four of them directly.
