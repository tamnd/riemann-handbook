---
id: supp-bc-outright
title: Depth-zero components become tame principal series after base change
kind: theorem
decl: UpperTheory.Gal.InertialTypesAlt.suppBC_outright
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.RegularSemisimpleFibres.Closed
covers: 1313
status: drafted
drafted_by: writer@claude
---
This theorem proves `SuppBC` with no hypothesis. It is the main input of [toTor_holds](/entry/to-tor-holds/). The proof only discharges the one hypothesis of [the conditional form](/entry/supp-bc-holds/), which has the real content. Below this theorem are 1,313 declarations: 1,142 below the conditional form and 110 below the matching statement.

## Statement

**Theorem.** `SuppBC` holds.

`SuppBC` is stated in full in [the conditional form](/entry/supp-bc-holds/). In short: let $E$ be totally complex, $\pi$ cuspidal on $\mathrm{GL}_n(\mathbb{A}_E)$, and let $(K, \pi_K)$ be reached from $(E, \pi)$ by a chain of prime-degree base changes. Let $v$ be a place of $E$ with $E_v \cong \mathbb{Q}_g$ and inertia trivial on $K$, and let $w$ be a place of $K$ above $v$ with $N(w) = g^f$. Suppose that $\pi_v$ has a nonzero vector fixed by $K_1$, and that $f$ is divisible by the size of each member of its cuspidal support. Then the support of $\pi_{K,w}$ is a set of tame characters $\xi_1, \dots, \xi_n$, each $t$ in the inertia group over $K$ has the characteristic polynomial $\prod_j (X - \xi_j(a(t)))$ on $\mathrm{rec}(\pi_v)$, for each $\mathrm{rec}$ with `IsRecT` and each local Artin map $a$ at $w$, and if $\pi_v$ is mixed then no two $\xi_j$ are linked by $|\cdot|$.

## Proof

The proof is `suppBC_holds L.inflMatch`. The lemma `inflMatch` (110 declarations) proves `InflMatching`: for inflated level-zero functions, the twisted orbital integrals along an unramified extension $K/k$ of local fields match the orbital integrals over $k$, and each regular semisimple element with a nonzero orbital integral is a norm.

## In the Lean code

The theorem is in [Closed.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/RegularSemisimpleFibres/Closed.lean#L6). `SuppBC` is in [NumberField.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/RegularSemisimpleFibres/NumberField.lean#L166), `suppBC_holds` in [TypeOfLblHolds.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/RegularSemisimpleFibres/TypeOfLblHolds.lean#L141), and `InflMatching` in [IntersectionFamilySymmetric.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IntersectionFamilySymmetric.lean#L30). The word "outright" in the name means only that the hypothesis `InflMatching` is proved.
