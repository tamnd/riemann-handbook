---
id: has-type-all-of-k-types
title: A function whose K-projections are coefficients is a coefficient series
kind: theorem
decl: GlobalTheory.TypeSum.KSeries.hasTypeAll_of_kTypes
module: Development.AbelianVarietyTheory.Proofs.HeightProofs.DiscreteSeriesCoeffSeriesOfKTypeProjections
covers: 447
status: drafted
drafted_by: writer@claude
---
This theorem puts the $K$-projections of a function back together. If each projection $f_e$ of $f$ is a finite sum of [[matrix coefficients|J85Q7QGGHS]] of $\sigma$, then $f$ is an absolutely convergent series of such coefficients. It carries the content of [`discreteSeriesCoeffSeries_of_kTypeProjections`](/entry/discrete-series-coeff-series-of-k-type-projections/), and through it step 2 of [`hasTypeAll_of_closure`](/entry/has-type-all-of-closure/).

## Statement

The statement is the one in [`discreteSeriesCoeffSeries_of_kTypeProjections`](/entry/discrete-series-coeff-series-of-k-type-projections/), with the notation of [`hasTypeAll_of_closure`](/entry/has-type-all-of-closure/). In short: under `HarishChandraModules`, `CasselmanWallach` and `Std` for $\sigma$, if $f$ is continuous and of uniform moderate growth on $G = U(p,q)$, and each $f_e(y) = \int_K e(k) f(yk)\, dk$ ($e$ continuous and $K$-finite) equals $\sum_j \ell_j(\sigma(y) x_j)$ with $\ell_j$ Sobolev and $x_j$ $K$-finite, then `HasTypeAll` $(\sigma, f)$.

## Proof

Write $\mathfrak{k}$ for the $X \in \mathfrak{g}$ with $X^* = -X$. Such $X$ commute with $J$, so $\mathfrak{k}$ is the Lie algebra of $K$.

1. `exists_rightKFourierSeries_unitary_moderateGrowth` gives continuous $K$-finite $e_0, e_1, \dots$ on $K$ (fixed, not depending on $f$). For our $f$ it gives $N$, constants $B_i(k)$ with $\sum_i B_i(k) < \infty$ for each $k$, and $f(y) = \sum_i f_{e_i}(y)$ on $G$. It also gives functions $\Phi_i(w, \cdot)$, one for each word $w$ in $\mathfrak{k}$, with $\Phi_i(\emptyset, \cdot) = f_{e_i}$, each $\Phi_i(Xw, \cdot)$ the derivative of $\Phi_i(w, \cdot)$ along $X$ on the right, and $\lvert \Phi_i(w, y) \rvert \leq B_i(k) (1 + \sum \lvert y_{ab} \rvert^2)^N$ when $w$ has length at most $k$ and letters of norm at most 1.
2. The hypothesis gives $f_{e_i} = \sum_j \ell_{ij}(\sigma(y) x_{ij})$.
3. `coef_eq_fam`, by induction on $w$: $\Phi_i(w, y) = \sum_j \ell_{ij}(\sigma(y)\, d\sigma(w) x_{ij})$. So these sums satisfy the bound of step 1.
4. `exists_common_growth_exponent_gK_discreteSeries`, with the literature statements, gives one list $S$ and functions $m$, $A$, all fixed by $N$ only. Each finite sum with such bounds can be rewritten as $\sum_r \ell'_{ir}(\sigma(y) x'_{ir})$ with $x'_{ir}$ smooth, $\lvert \ell'_{ir}(w) \rvert \leq c_{ir} \lVert w \rVert_S$, and $\sum_r c_{ir} \lVert x'_{ir} \rVert_{S'} \leq A(S') B_i(m(S'))$ for every list $S'$.
5. `exists_ctrl` gives $S_1$ and $A_0 \geq 0$ with $\lVert w \rVert_S \leq A_0 \lVert w \rVert_{S_1}$ and $\lVert \sigma(g) w \rVert_{S_1} \leq B_c(g) \lVert w \rVert_{S_1}$ for a continuous $B_c$.
6. `pad` puts the terms $(i, r)$ into one family on $\mathbb{N} \times \mathbb{N}$, with zeros for $r \geq q_i$. Step 4 and $\sum_i B_i(k) < \infty$ make $\sum_{i,r} A_0 c_{ir} \lVert x'_{ir} \rVert_{S'}$ finite. Step 5 bounds term $(i, r)$ at $g$ by $B_c(g)$ times the term for $S' = S_1$. So the double series converges absolutely, and `pad_hasSum` gives the sum $\sum_i f_{e_i}(g) = f(g)$.
7. `Nat.pairEquiv` turns $\mathbb{N} \times \mathbb{N}$ into $\mathbb{N}$, with the list $S_1$ and constants $A_0 c_{ir}$.

## In the Lean code

The theorem is in [DiscreteSeriesCoeffSeriesOfKTypeProjections.lean](lean:Development/AbelianVarietyTheory/Proofs/HeightProofs/DiscreteSeriesCoeffSeriesOfKTypeProjections.lean#L99). `coef_eq_fam` is at line 28 and `pad` at line 58. `exists_ctrl` is in [ContinuousCf.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ContinuousCf.lean#L100). We have not opened the proofs of the two lemmas of steps 1 and 4. The Fourier series of step 1 and its derivative bounds use only directions in $\mathfrak{k}$. The step from these bounds to the bounds for every $S'$ in $\mathfrak{g}$ is in step 4.
