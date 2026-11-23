---
id: rs-nm-partial-l-eq-div
title: The Rankin-Selberg integral for GL(n) × GL(m) with m < n gives the partial L-function as a ratio of entire functions
kind: theorem
decl: GlobalTheory.RSnmUnf.rs_nm_partialL_eq_div
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.RankinSelbergGLnGLmPartialLEqDivEntire
covers: 428
status: drafted
drafted_by: writer@claude
---
This theorem proves [the ratio statement for the partial Rankin-Selberg L-function](/entry/rankin-selberg-gln-glm-partial-l-eq-div-entire/) by the integral of Jacquet, Piatetski-Shapiro and Shalika (Amer. J. Math. 105, 1983). The numerator is a global Rankin-Selberg integral. The result goes to [the off-diagonal case](/entry/rsnonvan-off-diag/) of [the nonvanishing at $s = 1$](/entry/tendsto-partial-l-ne-zero/).

## Statement

The statement of [the second name](/entry/rankin-selberg-gln-glm-partial-l-eq-div-entire/), word for word: for $1 \le m < n$, unitary cuspidal $\sigma$, $\sigma'$ of $\mathrm{GL}_n$, $\mathrm{GL}_m$ with Satake parameters $\alpha_w$, $\beta_w$ outside $T$, there are entire $F$, $H$ with $H > 0$ on $\mathbb{R}$ and
$$\prod_{w \notin T} \prod_{i,j} \bigl(1 - \alpha_{w,i}\overline{\beta_{w,j}}\, q_w^{-x}\bigr)^{-1} = \frac{F(x)}{H(x)} \qquad (x > 1).$$

## Proof

For a partition $\lambda$ let $s_\lambda$ be the Schur polynomial and $|\lambda| = \sum_i \lambda_i$. Fix Haar measures and measurable fundamental domains $\mathcal{F}$ for $\mathrm{GL}_m(E)$ and $\mathcal{F}_0$ for the upper unitriangular group $N_m(E)$ in $\mathrm{GL}_m(\mathbb{A})$.

1. **Satake parameters.** `unfolded_theta_integral_eq_mul_schur_euler_product`, applied to $\sigma$ and to $\sigma'$, gives cuspidal representatives $\pi$, $\pi'$, the $\alpha_w$, $\beta_w$, and for $x > 1$ the finiteness of $\prod_{w}\sum_{\lambda} |s_\lambda(\alpha_w)|^2 Nw^{-|\lambda| x}$ and of the same product for $\beta$.
2. **Matched vectors.** `exists_matchedWhittakerVectors_shintaniRelations` gives $\varphi$ in the span `mspanR` of $\pi$, $\varphi'$ in that of $\pi'$, and a continuous $\kappa \ge 0$ on $\mathrm{GL}_m(\mathbb{A})$. Both are spherical outside $T$, with Whittaker relations of Shintani type there. Also $W_\varphi(\mathrm{diag}(h, 1)) = \kappa(h) W_{\varphi'}(h)$ for $h$ trivial at the finite places outside $T$, and $\kappa > 0$ at a point where $W_{\varphi'} \ne 0$. This lemma uses [the Kirillov bump](/entry/kirillov-semilocal-smooth-bump/).
3. **Unfolded integral.** `unfolded_rankinSelberg_cellIntegral_matchedVectors` gives a Schwartz-Bruhat function $\Phi$ on $\mathbb{A}^m$ and measurable $f \ge 0$, $t$ with $0 < \int_{\mathcal{F}_0} f < \infty$, such that for $x > 1$, summing over finitely supported families $(\lambda_w)_{w \notin T}$ of partitions: $$\begin{aligned}&\int_{\mathcal{F}_0} W_\varphi(\mathrm{diag}(h,1))\,\overline{W_{\varphi'}(h)}\,\hat\Phi(e_m h)\,|\det h|^{x - \frac{n-m}{2}}\,dh \\ &\quad = \Bigl(\int_{\mathcal{F}_0} f\,e^{x t}\Bigr) \sum_{(\lambda_w)} \prod_{w} s_{\lambda_w}(\alpha_w)\,\overline{s_{\lambda_w}(\beta_w)}\,Nw^{-|\lambda_w| x}.\end{aligned}$$
4. **Unfolding.** `rankinSelbergGLnGLm_unfolding_to_mirabolic` gives $c > 0$ such that the left side of step 3 is $c^{-1} Z(x)$, where $Z(s) = \int_{\mathcal{F}} (\mathbb{P}\varphi_\Phi)(\mathrm{diag}(h,1))\,\overline{\varphi'(h)}\,|\det h|^{s - \frac{n-m}{2}}\,dh$. Here $\varphi_\Phi$ is $\varphi$ averaged against $\Phi$ along a column, and $\mathbb{P}$ is `partialCoeff`.
5. **Entire functions.** `rsIntegral_entire_good` shows that $F = Z$ is entire, with `mspanR_le_goodFns` as input. `exp_integral_entire_real_pos` shows that $H(s) = c\int_{\mathcal{F}_0} f e^{s t}$ is entire and positive on $\mathbb{R}$.
6. **Euler product.** `eulerProduct_rankinSelbergGLnGLm_dirichletSeries` shows that for $x > 1$ the Euler product and the series of step 3 have the same value $P$. At each place this is the Cauchy identity $\sum_\lambda s_\lambda(\alpha)s_\lambda(\bar\beta)\,u^{|\lambda|} = \prod_{i,j}(1 - \alpha_i\bar\beta_j u)^{-1}$ (Macdonald, *Symmetric Functions and Hall Polynomials*, I (4.3)).

So $F(x) = H(x)\,P$. The rest is bookkeeping.

## In the Lean code

The theorem is at [line 30 of RankinSelbergGLnGLmPartialLEqDivEntire.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/RankinSelbergGLnGLmPartialLEqDivEntire.lean#L30). The lemmas of steps 1 to 6 are called at [lines 35](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/RankinSelbergGLnGLmPartialLEqDivEntire.lean#L35), 80, 81, 82, 84, 86 and 113. We have not unfolded the proofs of these lemmas, nor the spherical Whittaker values `sphW` in the Shintani relations.

The Dirichlet coefficient `rsTermNM` pads $\lambda$ with zeros to $n$ parts for $s_\lambda(\alpha)$ and is zero unless $\lambda$ is a partition. From step 1 the proof keeps only the Satake lists and the finiteness of `eulD`; it discards the theta integral identity that the lemma is named for. So the convergence for $x > 1$ is taken from a lemma about theta integrals for $\sigma \times \tilde\sigma$. The statement conjugates the Satake parameters of $\sigma'$ and does not mention the contragredient.
