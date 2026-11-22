---
id: rsnonvan-off-diag
title: The partial Rankin-Selberg L-function of two distinct representations is analytic on the positive reals
kind: theorem
decl: GlobalTheory.RSNonvan.offDiag
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.RankinSelbergPartialLTendstoNeZeroAtOne
covers: 430
status: drafted
drafted_by: writer@claude
---
This lemma says that for distinct unitary cuspidal representations $\sigma, \sigma'$ the partial L-function $L^T(s, \sigma \times \tilde\sigma')$ extends to a function analytic at each real $s > 0$, with no pole at $1$. It is step 2 of [the nonvanishing theorem](/entry/tendsto-partial-l-ne-zero/), which applies it to $(\sigma, \sigma')$ and to $(\sigma', \sigma)$. The proof splits by the sizes $a$ and $b$ and takes the continuation from two other statements.

## Statement

Let $E$ be a totally complex number field and $T$ a good finite set of primes (`IsGood`, see [the nonvanishing theorem](/entry/tendsto-partial-l-ne-zero/)). Let $\sigma$ on $\mathrm{GL}_a$ and $\sigma'$ on $\mathrm{GL}_b$ be unitary [[cuspidal representations|9AZ164C298]] over $E$, with $a, b \geq 1$, $(a, \sigma) \neq (b, \sigma')$, and Satake parameters at each $w \notin T$. Let $L^T(\sigma, \sigma', s) = \prod_{w \notin T} \prod_{\alpha, \beta} (1 - \alpha\bar\beta\, Nw^{-s})^{-1}$, as in the [entry on the limit at $1$](/entry/rankin-selberg-partial-l-tendsto-ne-zero-at-one/).

**Theorem.** There is $G \colon \mathbb{C} \to \mathbb{C}$, analytic at each real $x > 0$, such that the product $L^T(\sigma, \sigma', x)$ converges to $G(x)$ for each real $x > 1$.

## Proof

Compare $a$ and $b$.

1. **$a > b$.** By [`rankinSelberg_GLn_GLm_partialL_eq_div_entire`](/entry/rankin-selberg-gln-glm-partial-l-eq-div-entire/), there are entire $F$ and $H$ with $H(x)$ real and positive for real $x$, and $L^T(\sigma, \sigma', x) = F(x)/H(x)$ for $x > 1$. Take $G = F/H$. It is analytic where $H \neq 0$, so at each real point.
2. **$a < b$.** Apply the same statement to $(\sigma', \sigma)$: $L^T(\sigma', \sigma, x) = F(x)/H(x)$. By `partial_rankinSelberg_product_conj_swap_real`, $L^T(\sigma, \sigma', x) = \overline{L^T(\sigma', \sigma, x)}$ for real $x > 1$. Take $G(z) = \overline{F(\bar z)/H(\bar z)}$, which is again analytic at real points.
3. **$a = b$.** Then $\sigma \neq \sigma'$. By `rankinSelberg_sameDegree_meromorphic_continuation`, there is $F$, analytic at each real $x > 0$, with $F(1) = 0$ and $L^T(\sigma, \sigma', x) = F(x)/(x - 1)$ for $x > 1$. Take $G$ to be the difference quotient $(F(z) - F(1))/(z - 1)$, extended at $z = 1$ (Mathlib's `dslope F 1`). It is analytic at each $x > 0$ by `analyticAt_dslope'`.

The convergence of the product for $x > 1$ comes from `localRankinSelberg_logarithm_formula`.

## In the Lean code

- The lemma is at [line 66 of RankinSelbergPartialLTendstoNeZeroAtOne.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/RankinSelbergPartialLTendstoNeZeroAtOne.lean#L66). `analyticAt_dslope'` is at line 23 of the same file.
- The lemmas it calls: `GlobalTheory.T.rankinSelberg_GLn_GLm_partialL_eq_div_entire` (for $n > m$; it needs only the second half of `IsGood`, the unramified additive character), `GlobalTheory.T.rankinSelberg_sameDegree_meromorphic_continuation`, `GlobalTheory.T.partial_rankinSelberg_product_conj_swap_real` and `GlobalTheory.T.localRankinSelberg_logarithm_formula`. Each is a one-line wrapper, of `RSnmUnf.rs_nm_partialL_eq_div`, `RSNonvan.samedeg_continuation`, `RSConj.partial_conj` and `JSLog.logRankinSelberg`.
- The name says "off diagonal": the case $\sigma \neq \sigma'$. The diagonal case $\sigma = \sigma'$, with the pole, is the same-degree statement with $\sigma' = \sigma$.
- The conclusion is weaker than an analytic continuation to $\operatorname{Re} s > 0$: $G$ is analytic only at the real points $x > 0$. This is all that Landau's lemma in [the nonvanishing theorem](/entry/tendsto-partial-l-ne-zero/) needs.
