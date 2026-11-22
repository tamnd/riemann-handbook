---
id: uniform-bessel-rank-three-of-inputs
title: The weighted bound on rotated points with the cubic threshold filled in
kind: theorem
decl: CompanionTheory.WaveGrid.uniform_bessel_rank_three_of_inputs
module: CompanionTheory.AutomorphicTheory.BesselWaveGrids.WeightedBoundRotatedUniformOfCubicThreshold
covers: 1165
status: drafted
drafted_by: writer@claude
---
This theorem proves the [weighted bound on rotated points](/entry/weighted-bound-rotated-uniform/) from two inputs. It fills in the threshold function of [the bound from a cubic threshold](/entry/weighted-bound-rotated-uniform-of-cubic-threshold/) with one explicit function and proves the three facts that this function must satisfy. Its caller is [the bound from HypsG](/entry/weighted-bound-rotated-uniform-of-hyps-g/).

## Statement

Let $C_{gf}$ be real. Assume `In91` (families of discrete series, and an expansion and a moment bound for local Bessel functions) and `OneBesselTor D C_gf` for every datum $D$. Then `WeightedBoundRotatedUniform` holds.

## Proof

For a signature $\varepsilon \colon \{1, \dots, n\} \to \{\text{true}, \text{false}\}$, let $p$ and $q$ be the numbers of values true and false, and let $q_0 = \min(p, q)$. Put

$$t(n, \varepsilon) = \max\bigl(2n,\ 16 n q_0 + 8\sqrt{2 q_0}\bigr).$$

The proof applies the bound from a cubic threshold with this $t$ and $C_t = 43$. It proves three facts.

1. **The cubic bound.** `thrS_le` proves $t(n, \varepsilon) \leq 43 n^3$ for $n \geq 1$. It comes from `thrS_lt`, which proves the stronger $t(n, \varepsilon) + 1 < 43 n^2$ from $q_0 \leq n$ and $\sqrt{2q_0} \leq 2n$.
2. **Tensoring up.** `zuckT_thrS` proves `ZuckT t`. Let $\sigma$ be a discrete series with Harish-Chandra parameter $\mu$. Suppose that $|\mu_a - \mu_b| \geq h$ whenever $\varepsilon(a) \neq \varepsilon(b)$, with $t(n, \varepsilon) + 1 < h$. Then there is a structure `TensorDS`: a set $S$ of indices and, for each $s \in S$, a discrete series $\sigma_s$ with parameter $\mu + e_s$, pairwise inequivalent. Each product of a $K$-finite matrix coefficient of $\sigma$ with a matrix coefficient $g \mapsto y^* g x$ of the standard representation is a finite sum of $K$-finite matrix coefficients of the $\sigma_s$ (field `toSum`), and each $K$-finite matrix coefficient of a $\sigma_s$ is a finite sum of such products (field `ofSum`).
3. **Tensoring down.** `zuckDualT_thrS` proves `ZuckDualT t`, the same with $\mu - e_s$ and the dual representation.

Both 2 and 3 come from `zuckerman_tensor_exists` and `zuckerman_dual_tensor_exists`, and keep only the existence part. These have the shape of Zuckerman's theorem on tensor products with finite-dimensional representations (Ann. of Math. 106, 1977). We have not unfolded `IsDS`, so we do not claim that the match is exact.

## In the Lean code

The theorem is in [WeightedBoundRotatedUniformOfCubicThreshold.lean](lean:CompanionTheory/AutomorphicTheory/BesselWaveGrids/WeightedBoundRotatedUniformOfCubicThreshold.lean#L54), with `thrS_lt` and `thrS_le` in the same file. The function $t$ is `ReciprocityTheory.ChartRestriction.DS.G2.thrS` in [Transported.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/ExceptionalGroupG2/TensorProductsG2/Transported.lean#L10). `zuckT_thrS` and `zuckDualT_thrS` are in [ZuckDualTThrS.lean](lean:CompanionTheory/AutomorphicTheory/ZuckermanCommutation/ZuckermanFunctors/ZuckDualTThrS.lean#L6), and `ZuckT`, `ZuckDualT` in [ZuckDualTOfZuckDual.lean](lean:CompanionTheory/AutomorphicTheory/SchurLimitBounds/ZuckermanDuality/ZuckDualTOfZuckDual.lean#L34).

The name says "rank three", but neither the statement nor the proof has a rank-three condition. The only "three" is the exponent in the cubic bound. The function $t$ and the two tensor theorems sit in a folder `ExceptionalGroupG2` and a namespace `G2`, and `zuckerman_tensor_exists` is in a file `FormalDegreeConstantDiscrete.lean`. The statements are about signatures $\varepsilon$ of size $n$, not about $G_2$ or formal degrees. The cubic bound is weaker than the quadratic bound that `thrS_lt` proves; the caller asks only for the cubic one.
