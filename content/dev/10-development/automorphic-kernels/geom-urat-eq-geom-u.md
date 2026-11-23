---
id: geom-urat-eq-geom-u
title: The rational geometric side of the unitary trace formula
kind: theorem
decl: GlobalTheory.PreStabU.geomURat_eq_geomU
module: Development.WeilBound.CoreStatements.AutomorphicKernels.IsobaricBaseChange.IntegralCoefficientBaseChange.UnitaryBaseChangeCharacters.UnitaryBaseChangeLinks.UnitaryGeometricSideSeparableTest
covers: 540
status: drafted
drafted_by: writer@claude
---
This theorem rewrites the geometric side of a twisted trace formula for a unitary group, written as a sum over rational conjugacy classes, as the sum `geomU` over pairs of coprime polynomials. `geomU` is the geometric side of the unitary trace identity `USide`. It is below the step [EveryCharacter](/step/every-character/). The work for one characteristic polynomial is in [the class count for one polynomial](/entry/fixed-p/).

## Statement

Let $E$ be a CM field such that $E/E^+$ is unramified at all finite places. Let $n \ge 1$. Let $S$ be a set of finite places of $E$ with exactly one place above each place of $E^+$. Let $U$ be the unitary group over $E$ in $n$ variables, $U_w$ its local group ($\mathrm{GL}_n$ at a split place) and $K_w$ its compact subgroup `KL`. Let $\lambda$ be a family of dominant weights at the infinite places, and let $f = (f_w)$ be a test function for a family of level subgroups $K'_w$.

Let $\mathrm{Ell}_n$ be the set of monic separable polynomials of degree $n$ over $E$ whose roots have absolute value $1$ under every complex embedding. For $P \in \mathrm{Ell}$, let $\kappa(P)$ be the mass of the twisted centralizer of a $\delta \in \mathrm{GL}_n(E)$ such that $\delta\theta(\delta)$ has characteristic polynomial $P$, divided by $2^{\mathrm{nfac}(P)}$, where $\mathrm{nfac}(P)$ is the number of irreducible factors (`kap`). Let $\chi_\lambda(P)$ be the product over the infinite places $v$ of the complex conjugate of the character of weight $\lambda_v$ at an element with characteristic polynomial $P$ (`chW`). Let $O_w(\gamma)$ be the orbital integral of $f_w$ at $\gamma$ (`twOrb` with the trivial twist), and let $O^\kappa_w(P_1, P_2)$ be the sum over the local classes with characteristic polynomial $P_1 P_2$, with the sign $\kappa_w(P_1, \cdot)$ (`kapOrb`).

**Theorem.** Assume also that $f_w$ is supported on elements with separable characteristic polynomial for some $w \in S$. Then

$$\sum_{\substack{c \text{ rational class} \\ \chi_c \text{ separable}}} \mathrm{mass}(c)\, \chi_\lambda(\chi_c) \prod_{w \in S} O_w(c) = \sum_{a=0}^{n} \sum_{\substack{P_1 \in \mathrm{Ell}_a,\ P_2 \in \mathrm{Ell}_{n-a} \\ \gcd(P_1, P_2) = 1}} \kappa(P_1P_2)\, \chi_\lambda(P_1P_2) \prod_{w \in S} O^\kappa_w(P_1, P_2),$$

Here $\chi_c$ is the characteristic polynomial of $c$.

## Proof

Let $F$ be the finite set of $P \in \mathrm{Ell}_n$ for which each $f_w$, $w \in S$, takes a nonzero value at an element with characteristic polynomial $P$ (`finite_elliptic_charpolys_support`).

1. **Left side.** A separable characteristic polynomial of a rational class is in $\mathrm{Ell}_n$ (`local_points_integral_almost_all`), and then $\mathrm{mass}(c) = \kappa(P)\, 2^{\mathrm{nfac}(P)}$ (`unitary_mass_formula`). Group the classes by $P$. Only $P \in F$ give nonzero terms (`orb_support`).
2. **Right side.** For coprime $P_1 \in \mathrm{Ell}_a$, $P_2 \in \mathrm{Ell}_{n-a}$, the product is in $\mathrm{Ell}_n$ (`kappaConstant_mul_of_coprime_ellipticPolynomials`). Conversely the monic factors of $P \in \mathrm{Ell}_n$ are in $\mathrm{Ell}$ and coprime (`ell_of_dvd`, `coprime_of_sep`). So the right side is a sum over $P \in F$ of the sum over ordered factorizations $P = P_1 P_2$ (`kapOrb_support`).
3. **Each $P$.** The two inner sums agree by [`fixedP`](/entry/fixed-p/).

The rest is bookkeeping with finite sums.

## In the Lean code

The theorem is in [UnitaryGeometricSideSeparableTest.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/IsobaricBaseChange/IntegralCoefficientBaseChange/UnitaryBaseChangeCharacters/UnitaryBaseChangeLinks/UnitaryGeometricSideSeparableTest.lean#L453). The definitions are in [SimpleTwistedTraceFormulaStable.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/SimpleTwistedTraceFormulaStable.lean#L235) and [IsUnifAt.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsUnifAt.lean#L193).

The separability hypothesis on $f_w$ is never used: the proof introduces it as `_`. The theorem holds without it, because `geomURat` already keeps only the classes with separable characteristic polynomial.
