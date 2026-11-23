---
id: rankin-selberg-gln-glm-partial-l-eq-div-entire
title: The partial Rankin-Selberg L-function for two ranks m < n as a ratio of entire functions
kind: theorem
decl: GlobalTheory.T.rankinSelberg_GLn_GLm_partialL_eq_div_entire
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.RankinSelbergGLnGLmPartialLEqDivEntireStatement
covers: 429
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the Rankin-Selberg argument](/entry/rs-nm-partial-l-eq-div/), which has the real content. [The off-diagonal lemma](/entry/rsnonvan-off-diag/) uses it in its cases $a > b$ and $a < b$.

## Statement

Let $E$ be a totally complex number field and $1 \le m < n$. Let $\sigma$ and $\sigma'$ be unitary [[cuspidal representations|9AZ164C298]] of $\mathrm{GL}_n$ and $\mathrm{GL}_m$ over $E$ (classes up to isomorphism, with unitary central character). Let $T$ be a finite set of finite places such that for each $w \notin T$ the additive character $\psi_w$ has conductor $\mathcal{O}_w$, and $\sigma$, $\sigma'$ have Satake parameters $\alpha_w \in (\mathbb{C}^\times)^n$, $\beta_w \in (\mathbb{C}^\times)^m$ at $w$.

**Theorem.** There are entire functions $F$ and $H$ such that $H(x)$ is real and positive for each real $x$, and for each real $x > 1$
$$\prod_{w \notin T} \prod_{i=1}^{n} \prod_{j=1}^{m} \bigl(1 - \alpha_{w,i}\,\overline{\beta_{w,j}}\, Nw^{-x}\bigr)^{-1} = \frac{F(x)}{H(x)},$$
the product converging unconditionally.

## Proof

The proof is `exact RSnmUnf.rs_nm_partialL_eq_div`. See [the Rankin-Selberg argument](/entry/rs-nm-partial-l-eq-div/).

## In the Lean code

The theorem is in [RankinSelbergGLnGLmPartialLEqDivEntireStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/RankinSelbergGLnGLmPartialLEqDivEntireStatement.lean#L7). Its statement is the statement of `GlobalTheory.RSnmUnf.rs_nm_partialL_eq_div`, word for word. The proof is a `first` combinator around `exact`. The local factor is `locL` with `sat σ w` and the complex conjugates of `sat σ' w`; unconditional convergence is Mathlib's `HasProd`.
