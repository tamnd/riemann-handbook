---
id: iwasawa-constant
title: The constant of the flag integration formula
kind: theorem
decl: GlobalTheory.IwConst.iwasawa_constant
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.IwasawaIntegrationFormulaConstant
covers: 326
status: drafted
drafted_by: writer@claude
---
This theorem computes the constant in the integration formula of [`iwasawaFormula`](/entry/iwasawa-formula/), once the formula is known up to a constant. Its statement is renamed as [`iwasawa_integration_formula_constant`](/entry/iwasawa-integration-formula-constant/). The method is to compare both sides on small balls around $1$.

## Statement

Take the setting and notation of [`iwasawaFormula`](/entry/iwasawa-formula/): $G = \mathrm{U}(p,q)$, $n = p+q$, an isotropic flag with steps $j_i \ge 1$ and $s = \sum_i j_i$, the subgroups $N$, $M$, $K$, the gauge measures $\mu_N$, $\mu_M$, the probability measure $\mu_K$ on $K$ and the factor $\delta$. Let

$$V(i) = 2^{i(i-1)/2} \prod_{l=1}^{i} \frac{2\pi^l}{(l-1)!}, \qquad c_{Iw}(p,q,j) = \frac{2^{-\dim N/2}\, V(p)\, V(q)}{\prod_i V(j_i)\, 2^{j_i^2/2} \cdot V(p-s)\, V(q-s)}.$$

**Theorem.** Let $c$ be a gauge constant for $\mu_G$ and $\kappa \in [0,\infty]$. If $\int_G \varphi\, d\mu_G = \kappa \int_N \int_M \delta(m) \int_K \varphi(umk)\, d\mu_K\, d\mu_M\, d\mu_N$ for every measurable $\varphi \ge 0$, then $c\,\kappa = c_{Iw}(p,q,j)$.

## Proof

Let $L = K \cap M$, let $\omega(d)$ be the volume of the unit ball of $\mathbb{R}^d$, and let $B_r = \{g : \|g - 1\|_{HS} \le r\}$.

1. **Dimensions.** `isotropicFlag_dimension_count` gives $n^2 = 2\dim N + \dim M$ and $p^2 + q^2 = \dim N + \dim L$, with $\dim L = (p-s)^2 + (q-s)^2 + \sum_i j_i^2$.
2. **Lie algebras.** Four existence lemmas give real subalgebras for $N$, $M$, $K$, $L$ with orthonormal bases. `iwasawa_lieAlgebras_relative_position` relates them. `iwasawaGauge_definite_and_unitBody_volume` shows that a gauge `gau` built from the four bases is definite, and that its unit body has volume $2^{\dim N/2}\,\omega(2\dim N + \dim M)\,\omega(\dim L)$.
3. **Compact volumes.** `exists_riemannianHaar_unitaryJSubgroupOfAlgebra` gives gauge measures $\mu_0$ on $K$ and $\nu_L$ on $L$. Then $\mu_0(K) = V(p)V(q)$ (`volume_unitaryMaximalCompact_eq_prod`) and $\nu_L(L) = \prod_i V(j_i)2^{j_i^2/2} \cdot V(p-s)V(q-s)$ (`volume_maximalCompact_inter_isotropicFlagLevi`). The Hilbert-Schmidt norm is invariant under unitary conjugation, so $\mu_0$ is also right $K$-invariant. Hence $\mu_0 = V(p)V(q)\,\mu_K$ (`right_invariant_eq_smul_left_invariant_probability`).
4. **Left side.** Take $\varphi = 1_{B_r}$. By `riemannianHaarGauge_whole_group`, $c\,\mu_G(B_r) \sim \omega(n^2)\, r^{n^2}$ as $r \to 0^+$.
5. **Right side.** Let $F(r)$ be the triple integral of $1_{B_r}$ with $\mu_0$ in place of $\mu_K$. Insert a cutoff on $k$ in the $L$ direction (the set `slab`) and call the result $S(r)$. The unfolding lemma `iwasawa_lintegral_unfold_compact_levi` (with the right $L$-invariance of $\mu_M$ and $\delta$) and `slab_measure_squeeze'` give, for each $\eta > 0$ and small $r$,
$$\nu_L(B_{r/(1+\eta)})\, F(r) \le \nu_L(L)\, S(r) \le \nu_L(B_{(1+\eta)r})\, F(r).$$
By `localisedIwasawaIntegral_smallBall_asymptotics`, $S(r) / r^{\dim N + \dim M + \dim K}$ tends to the volume of the unit body of step 2.
6. **Comparison.** Since $c\kappa F(r) = V(p)V(q)\, c\,\mu_G(B_r)$ and $\nu_L(B_r) \sim \omega(\dim L)\, r^{\dim L}$, the squeeze `tendsto_small_ball_density_of_squeeze` and uniqueness of limits give
$$c\kappa\, \nu_L(L)\, 2^{\dim N/2}\, \omega(n^2)\, \omega(\dim L) = V(p)V(q)\, \omega(n^2)\, \omega(\dim L).$$
Cancel the ball volumes and divide by $\nu_L(L)\, 2^{\dim N/2} > 0$. This gives $c\kappa = c_{Iw}(p,q,j)$.

The rest is bookkeeping in $[0,\infty]$.

## In the Lean code

The theorem is in [IwasawaIntegrationFormulaConstant.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/IwasawaIntegrationFormulaConstant.lean#L157). $V$ is `volU` in [DefClassNum.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/DefClassNum.lean#L15) and $c_{Iw}$ is `cIw` in [IsGaugeAll.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/IsGaugeAll.lean#L24). The cutoff, the gauge and $\delta$ (`slab`, `gau`, `dlt`) are in [MeasurableSetHsBall.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/MeasurableSetHsBall.lean#L37).

The lemmas named above are all `GlobalTheory.T.*` statements; we read their statements, not their proofs. The local helper `map_mul_right_eq_of_isGaugeSub` (line 97) proves the right invariance from the uniqueness part of `gaugeMeasure_matrixAlgebraSubgroup_local_asymptotics`.

The hypothesis does not ask $\kappa < \infty$; the conclusion forces it. The left $K$-invariance of $\mu_K$ is used only in step 3.
