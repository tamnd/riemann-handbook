---
id: discrete-series-coeff-series-of-k-type-projections
title: Coefficient series from K-type projections, restated
kind: theorem
decl: GlobalTheory.T.discreteSeriesCoeffSeries_of_kTypeProjections
module: Development.AbelianVarietyTheory.Proofs.HeightProofs.DiscreteSeriesCoeffSeriesOfKTypeProjectionsStatement
covers: 448
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`hasTypeAll_of_kTypes`](/entry/has-type-all-of-k-types/), with the same statement. The real content is in that entry. Its only use here is step 2 of [`hasTypeAll_of_closure`](/entry/has-type-all-of-closure/), which reduces a coefficient expansion of $f$ to one for each $K$-projection of $f$.

## Statement

We use the notation of [`hasTypeAll_of_closure`](/entry/has-type-all-of-closure/). Assume `HarishChandraModules` and `CasselmanWallach`. Let $\sigma$ satisfy `Std` (unitary, irreducible, $K$-finite vectors smooth, a formal degree, a nonzero $K$-finite vector). Let $f$ be continuous on $G = U(p,q)$ and of uniform moderate growth. Suppose that for each continuous $K$-finite function $e$ on $K$ there are Sobolev forms $\ell_1, \dots, \ell_m$ and $K$-finite vectors $x_1, \dots, x_m$ with
$$\int_K e(k) f(yk)\, dk = \sum_j \ell_j(\sigma(y) x_j) \quad (y \in G).$$
Then $f$ is an absolutely convergent series of [[matrix coefficients|J85Q7QGGHS]] of $\sigma$ in the sense of `HasTypeAll`.

## Proof

The proof is the term `hasTypeAll_of_kTypes`. The rest is bookkeeping.

## In the Lean code

The statement is in [DiscreteSeriesCoeffSeriesOfKTypeProjectionsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/HeightProofs/DiscreteSeriesCoeffSeriesOfKTypeProjectionsStatement.lean#L20). The name speaks of discrete series, but the hypothesis is `Std`, not `IsDS`. The caller makes `Std` from `IsDS` with `std_of_isDS`.
