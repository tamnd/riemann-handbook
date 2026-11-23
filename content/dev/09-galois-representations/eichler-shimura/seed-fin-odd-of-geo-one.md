---
id: seed-fin-odd-of-geo-one
title: The seed statement for odd rank from the geometric realization
kind: theorem
decl: UpperTheory.Gal.Int.Div.seedFinOdd_of_geoOne
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.IntegralStructures.ZetaCharacterDivisibility.MainFin
covers: 707
status: drafted
drafted_by: writer@claude
---
This theorem proves `SeedFinOdd` from the geometric realization [GeoOne](/step/geo-one-def/). It is the first hypothesis of [coreAll_of](/entry/core-all-of/), and its user is [galoisLocalGlobal_of_geometry_lift](/proof/galois-row/). `GeoOne` gives representations $\rho$ of some dimension $dd$, where the Satake polynomial of $U$ only kills $\rho$ of a Frobenius element. This theorem gets from $\rho$ a representation $r$ of dimension $a$ whose characteristic polynomials are the Satake polynomials. The cutting is done by [divAll_holds](/entry/div-all-holds/). This theorem moves the data of `GeoOne` to the places where it is needed. Below it are 707 declarations.

## Statement

**Theorem.** If `GeoOne` holds, then `SeedFinOdd` holds.

`SeedFinOdd` is `SeedWU4 Odd TyEll (GenOf DGen) WtLac`. In short: take a CM field $E$, a prime $\ell$, an odd $a \geq 1$, $d$ with `FieldOK E l d`, a finite set $T$ of non-split places, and split places $w_0, v'$ above $\ell$ that are apart. Then there is a finite set $Z_0$ of places with this property. For each $U'$ that is automorphic off $T$, has type `TyEll` at $w_0$, has the weight `WtLac`, is spherical off $w_0$ and $S$, has Satake parameters at $v'$ and is generic at $Z_0$, there is a continuous semisimple $r : G_E \to \mathrm{GL}_a(\overline{\mathbb{Q}}_\ell)$. Its Frobenius characteristic polynomials match the Satake parameters of $U'$ at almost all places `UsPl d`. At the places in $Y$, $r$ also has the Frobenius eigenvalue clause `FrobEig`, the crystalline and de Rham clause `CrysDRU`, and the clause `PhiAt`.

## Proof

The proof is `seedFinOdd_of` applied to `divAll_holds`, to seven facts on conjugate places and lacunary weights, and to `GeoOne`. In `seedFinOdd_of`:

1. It takes $Z_0 = \emptyset$. So the genericity hypothesis on $Z_0$ is empty.
2. `GapLac` turns the weight `WtLac` at $v'$ into `LacWtAt`.
3. For each $w$ above $\ell$, the lemma `move` picks $u_0 \in \{w_0, \bar w_0\}$ and $u' \in \{v', \bar v'\}$. Here $\bar w$ is the conjugate place `cpl w`, and $u'$ is chosen with `SameK x u' w`. The facts `TyConj`, `SatConj` and `LacConj` move the type, the Satake parameters and the lacunary weight to the conjugate place. Then `GeoOne` applies at $(u_0, u')$.
4. `GeoOne` at $v'$ gives a `VBase` representation $\rho$. `DivAll` applied to $\rho$ gives $r$ and its Frobenius clause.
5. Each clause at $w$ comes from the matching clause of `DivAll` for the $\rho$ that `GeoOne` gives at $w$. `DGenMul` turns `GenOf DGen` into `GenericMul`. The places above $\ell$ are split, because `FieldOK` says that the non-split places are prime to $\ell$.

## In the Lean code

The theorem is in [MainFin.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/ZetaCharacterDivisibility/MainFin.lean#L13). `seedFinOdd_of` is in [SeedFinOddOf.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/ZetaCharacterDivisibility/SeedFinOddOf.lean#L44), and the facts on conjugate places in [StConj.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/ZetaCharacterDivisibility/StConj.lean). `SeedWU4` and `SeedFinOdd` are in [LimWU4OfLimWU3.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/LimWU4OfLimWU3.lean#L15). The proof does not use the hypothesis that $w$ is in $Y$, so the clauses hold at all such places. The choice $Z_0 = \emptyset$ makes `SeedFinOdd` stronger than its form suggests.
