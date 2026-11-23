---
id: kernels-integral-inert
title: The theta kernels are integral at inert primes
kind: theorem
decl: Formalism.L2.KerInert.kernels_integral_inert
module: Formalism.LocalToGlobal.InertKernelTheory.KernelsIntegralInert
covers: 793
status: drafted
drafted_by: writer@claude
---
This theorem proves `IntInert`: at an inert prime $p \ge 5$, the Taylor coefficients of the theta kernels, in the formal logarithm of a good model, are $p$-adic integers. It is a pass-through. It gives two proved facts to [`integral_inert_of_approx_basis`](/entry/integral-inert-of-approx-basis/), and the real proof is in [`integral_inert_of_weakApprox`](/entry/integral-inert-of-weak-approx/). Its user `intInert_of_complexMultiplication_condition` gives `IntInert` to [`servH_row_of_artin`](/entry/serv-h-row-of-artin/).

## Statement

Assume `CM2` (the good model condition for lattices with complex multiplication, stated in [`servH_row_of_artin`](/entry/serv-h-row-of-artin/)).

**Theorem.** `IntInert` holds.

`IntInert` says this. Take a datum $D$, an ideal $c$ of $O_K$ with norm prime to $2d$, $\delta$ with $\delta^{12}$ the discriminant of the lattice of $c$, a character $\chi$, a prime $p \ge 5$ with $\left(\frac{-d}{p}\right) = -1$, and self-dual lattices $L \subset E^N$, $L' \subset E^{N'}$ with $N, N'$ even. Let $F$ be an integral combination of translated theta kernels (`IsComb`), $C$ a change of variables to a model with integral coefficients and unit discriminant, and $b$ a local orthonormal basis at $p$. Then all coefficients of `atLog b F * ePh` have norm at most $1$. Here `atLog` substitutes the formal logarithm of the model along $b$. We have not unfolded `ePh`.

## Proof

Apply `integral_inert_of_approx_basis` to `weak_approximation_places` ([IntWAPlaces.lean](lean:Formalism/LocalToGlobal/InertKernelTheory/InertCoprimeLemmas/IntWAPlaces.lean#L465)) and `local_orthonormal_basis` ([FrLocB.lean](lean:Formalism/LocalToGlobal/InertKernelTheory/InertCoprimeLemmas/FrLocB.lean#L669)).

## In the Lean code

The theorem is at [KernelsIntegralInert.lean](lean:Formalism/LocalToGlobal/InertKernelTheory/KernelsIntegralInert.lean#L9). `IntInert` and `IntFirst` are in [StatementInt.lean](lean:Formalism/LocalToGlobal/InertKernelTheory/StatementInt.lean#L18).

The hypothesis `CM2` is hidden: it comes from `variable [Fact CM2] in` at line 7, so the statement shows no hypothesis. In the folder `InertKernelTheory`, the only place that reads it is the call to `cm2` in [GenusOneDatumExistence.lean](lean:Formalism/LocalToGlobal/InertKernelTheory/InertCoprimeLemmas/GenusOneDatumExistence.lean#L184).
