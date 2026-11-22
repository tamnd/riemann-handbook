---
id: tendsto-partial-l-ne-zero
title: Nonvanishing at 1 of the partial Rankin-Selberg L-function, by positivity
kind: theorem
decl: GlobalTheory.RSNonvan.tendsto_partialL_ne_zero
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.RankinSelbergPartialLTendstoNeZeroAtOne
covers: 767
status: drafted
drafted_by: writer@claude
---
This theorem proves that $L^T(x, \sigma \times \tilde\sigma')$ tends to a nonzero limit as $x \to 1^{+}$ for distinct unitary cuspidal representations $\sigma, \sigma'$. Its statement is given in the [entry under the second name](/entry/rankin-selberg-partial-l-tendsto-ne-zero-at-one/), which passes it to [the bound on the logarithm](/entry/abs-re-log-rs-bdd/). The proof is a positivity argument: the Rankin-Selberg L-function of $\sigma \boxplus \sigma'$ with its own contragredient has a Dirichlet series with nonnegative coefficients, and a zero at $1$ would make this series converge too far to the left.

## Statement

Let $E$, $T$, $\sigma$ on $\mathrm{GL}_a$ and $\sigma'$ on $\mathrm{GL}_b$ be as in the [second name](/entry/rankin-selberg-partial-l-tendsto-ne-zero-at-one/): unitary, cuspidal, $a, b \geq 1$, $(a, \sigma) \neq (b, \sigma')$, with Satake parameters outside $T$. Write $L^T(\sigma, \sigma', x)$ for the partial product of the local factors $\prod_{\alpha, \beta} (1 - \alpha\bar\beta\, Nw^{-x})^{-1}$ over $w \notin T$.

**Theorem.** There is $z \neq 0$ with $L^T(\sigma, \sigma', x) \to z$ as $x \to 1^{+}$.

## Proof

1. **Enlarge $T$.** `exists_goodRankinSelbergPlaceSet_superset_totallyComplex` gives a finite $T' \supseteq T$ that is good (`IsGood`): it is a union of full fibres over rational primes, and the fixed additive character is unramified outside $T'$.
2. **Continuation.** By [`offDiag`](/entry/rsnonvan-off-diag/), applied to $(\sigma, \sigma')$ and to $(\sigma', \sigma)$, there are $G$ and $G'$, analytic at each real $x > 0$, with $L^{T'}(\sigma, \sigma', x) = G(x)$ and $L^{T'}(\sigma', \sigma, x) = G'(x)$ for $x > 1$. By `rankinSelberg_sameDegree_meromorphic_continuation`, there are $D$ and $D'$, analytic at each $x > 0$, with $L^{T'}(\sigma, \sigma, x) = D(x)/(x-1)$ and $L^{T'}(\sigma', \sigma', x) = D'(x)/(x-1)$.
3. **Suppose $G(1) = 0$.** By `partial_rankinSelberg_product_conj_swap_real`, $L^{T'}(\sigma', \sigma, x) = \overline{L^{T'}(\sigma, \sigma', x)}$, so $G'(1) = 0$ too. Then
$$P = D \cdot D' \cdot \frac{G}{x-1} \cdot \frac{G'}{x-1}$$
is analytic at each $x > 0$.
4. **Positivity.** By `dirichlet_series_exponential_sum_converges`, for $x > 1$ the product of the four L-functions is $\exp \sum_{w \notin T'} \sum_{r \geq 0} c_{w,r}\, Nw^{-(r+1)x}$, with
$$c_{w,r} = \frac{|p_{r+1}(\sigma, w) + p_{r+1}(\sigma', w)|^2}{r+1} \geq 0,$$
where $p_k$ is the $k$-th power sum of the Satake parameters. Landau's lemma `landau_exp_hasSum_of_analyticAt` says: an exponential of a series with nonnegative coefficients that extends analytically to $x > 0$ is still the exponential of the convergent series there. So the series converges at $x = 1/(a+b)$.
5. **Contradiction.** The multiset $\mathrm{sat}(\sigma, w) + \mathrm{sat}(\sigma', w)$ has $a + b$ elements with product of norm $1$ (`norm_prod_satakeParameters_unitary_eq_one`). So some power sum $p_k$ with $k \leq a + b$ has norm at least $1$, and `not_summable_psum_sq` shows that the series diverges at $1/(a+b)$, by comparison with $\sum_w Nw^{-1}$. So $G(1) \neq 0$.
6. **Back to $T$.** $L^T = \prod_{w \in T' \setminus T} L_w \cdot L^{T'}$. Each $L_w(x)$ tends to a nonzero $L_w(1)$, by `localRankinSelbergFactor_conj_tendsto_one_ne_zero`, since $|\alpha|^2 < Nw$ for all Satake parameters (`satakeParameter_normSq_lt_absNorm_unitaryCusp`). So $z = \prod_{w \in T' \setminus T} L_w(1) \cdot G(1)$.

## In the Lean code

- The theorem is at [line 117 of RankinSelbergPartialLTendstoNeZeroAtOne.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/RankinSelbergPartialLTendstoNeZeroAtOne.lean#L117). `lfac`, `IsGood`, `dcoef` and `dexp` are in [IsGoodEmptyIff.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/IsGoodEmptyIff.lean#L13). Landau's lemma is in [GenDirichletHasSumIteratedDeriv.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/GenDirichletHasSumIteratedDeriv.lean#L267), and `not_summable_psum_sq` in [ExistsOneLeNormPsumMultiset.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsOneLeNormPsumMultiset.lean#L123).
- The `GlobalTheory.T` lemmas are one-line `...Statement` wrappers. Under them are `RSNonvan.samedeg_continuation`, `RSNonvan.fourProd_eq_exp`, `RSConj.partial_conj`, `RSNonvan.exists_isGood_superset_all`, `JSW.locL_conj_tendsto_one_and_ne_zero`, `RSStrict.norm_sq_lt_absNorm` and `RSNonvan.norm_prod_sat_eq_one`. We have not unfolded their proofs.
