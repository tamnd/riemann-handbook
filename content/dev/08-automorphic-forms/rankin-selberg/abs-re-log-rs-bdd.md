---
id: abs-re-log-rs-bdd
title: The real part of the Rankin-Selberg logarithm is bounded near 1 for distinct representations
kind: theorem
decl: GlobalTheory.JSW.Rigid.abs_re_logRS_bdd
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.JacquetShalikaRigidityHolds
covers: 769
status: drafted
drafted_by: writer@claude
---
This lemma is step 3 of [the vanishing lemma](/entry/vanish/): for two distinct unitary cuspidal representations, the real part of $\log RS_T(\sigma, \sigma', x)$ stays bounded as $x \to 1^{+}$. It is a short consequence of the [nonvanishing of the partial Rankin-Selberg L-function at $1$](/entry/rankin-selberg-partial-l-tendsto-ne-zero-at-one/). That theorem, through [its proof](/entry/tendsto-partial-l-ne-zero/), has the analytic content.

## Statement

Let $E$ be a totally complex number field, and $T$ a finite set of primes of $E$. Let $\sigma$ be a unitary [[cuspidal representation|9AZ164C298]] of $\mathrm{GL}_a$ over $E$ and $\sigma'$ one of $\mathrm{GL}_b$, with $a, b \geq 1$, both with Satake parameters at each prime $w \notin T$. Suppose $(a, \sigma) \neq (b, \sigma')$. Let $\log RS_T(\sigma, \sigma', x)$ be the double series of [the vanishing lemma](/entry/vanish/).

**Theorem.** There is $C$ such that $|\operatorname{Re} \log RS_T(\sigma, \sigma', x)| \leq C$ for all $x > 1$ near $1$.

## Proof

For $x > 1$ put
$$L^T(x) = \prod_{w \notin T} \prod_{\alpha, \beta} \bigl(1 - \alpha \bar\beta\, Nw^{-x}\bigr)^{-1},$$
with $\alpha$ running over the Satake parameters of $\sigma$ at $w$ and $\beta$ over those of $\sigma'$. This is the partial L-function $L^T(x, \sigma \times \tilde\sigma')$.

1. By [`rankinSelberg_partialL_tendsto_ne_zero_at_one`](/entry/rankin-selberg-partial-l-tendsto-ne-zero-at-one/), $L^T(x) \to z$ as $x \to 1^{+}$, for some $z \neq 0$.
2. By `hasProd_exp_logRS`, $L^T(x) = \exp(\log RS_T(\sigma, \sigma', x))$ for $x > 1$. This comes from `localRankinSelberg_logarithm_formula`.
3. So $\operatorname{Re} \log RS_T = \log |L^T(x)| \to \log |z|$.
4. Near $1$ the real part lies in $[\log|z| - 1, \log|z| + 1]$. Take $C = |\log |z|| + 1$.

## In the Lean code

- The lemma is at [line 62 of JacquetShalikaRigidityHolds.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/JacquetShalikaRigidityHolds.lean#L62). `hasProd_exp_logRS` is at line 18 of the same file.
- The lemmas it calls: `GlobalTheory.T.rankinSelberg_partialL_tendsto_ne_zero_at_one` and `hasProd_exp_logRS`.
- "Near $1$" is the filter $\mathcal{N}_{>}(1)$ of right neighbourhoods of $1$. The bound is on the real part only. The imaginary part is a branch of the argument and is not controlled here, and the vanishing lemma does not need it.
