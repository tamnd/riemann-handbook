---
title: Pairs of the same degree
decls:
  - GlobalTheory.ZEul.Smooth.zint_eq_mul_partialL_smooth
  - GlobalTheory.T.unfoldedThetaIntegral_eq_mul_partialRankinSelbergL
  - GlobalTheory.RSNonvan.samedeg_continuation
  - GlobalTheory.T.rankinSelberg_sameDegree_meromorphic_continuation
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Pairs of the same degree

Let $\sigma$ and $\sigma'$ be unitary cuspidal representations of the same group $\mathrm{GL}_a$. This section proves that $(x - 1)L^T(x, \sigma \times \bar\sigma')$ extends to a function $F$ that is analytic at every real point $x > 0$, and that $F(1) = 0$ when $\sigma \neq \sigma'$. This is the theorem of Jacquet and Shalika on the pole at $s = 1$ ([Rankin-Selberg integrals](/learn/trace-formula/#rankin-selberg-integrals)), in the form that [the off-diagonal lemma](/entry/rsnonvan-off-diag/) needs for pairs of equal degree. The proof has two steps: the theta integral $Z$ of [the unfolding section](/entry/lintegral-unfolded-eq/) is a positive entire function times the partial L-function, and $Z$ times $x - 1$ continues across $x = 1$, with value at $1$ a multiple of a Petersson inner product.

We keep the notation of the previous sections. In particular $Z(\phi, \phi', x)$ is the theta integral of [the unfolding section](/entry/theta-z-eq-mul-eul-d/), formed with a function $\Phi$ on $\mathbb{A}_\infty^a$, a fractional ideal $J$ and a vector $\eta \in \mathbb{A}_f^a$. Here we always take $J = N\mathcal{O}_E$ for an integer $N \ge 1$, and $\eta = e_a$, the last basis vector.

**Definition 8.5.1 (Good set of places).** A finite set $T$ of finite places of $E$ is *good* if:

1. it is saturated: if $w \in T$ and $w'$ lies over the same rational prime as $w$, then $w' \in T$;
2. for every finite $w \notin T$ the character $\psi_w$ has conductor $\mathcal{O}_w$.

Every finite set of finite places lies in a good one: add all places above the rational primes of the set and the finitely many places where $\psi_w$ is ramified.

**Theorem 8.5.2 (Theta integral as an Euler product).** Let $a \ge 1$ and let $\sigma$, $\sigma'$ be unitary cuspidal representations of $\mathrm{GL}_a$ over $E$, unramified outside a good set $T$. Then there are an integer $N \ge 1$, a $C^\infty$ function $\Phi$ on $\mathbb{A}_\infty^a$ with compact support contained in the set where $u_{a, v} \neq 0$ for every archimedean $v$, spaces of cusp forms $\pi$ and $\pi'$ in the classes $\sigma$ and $\sigma'$, and nonzero $\phi$, $\phi'$ in the smooth spans of $\pi$ and $\pi'$, with the following property. For every Haar measure on $\mathrm{GL}_a(\mathbb{A})$ and every measurable fundamental domain $\mathcal{F}$ of $\mathrm{GL}_a(E)$ there is an entire function $H$, with $H(x)$ real and positive for real $x$, such that for all real $x > 1$
$$\begin{aligned} Z(\phi, \phi', x) &= H(x)\, L^T(x, \sigma \times \bar\sigma'), \\ Z(\phi, \phi, x) &= H(x)\, L^T(x, \sigma \times \bar\sigma), \\ Z(\phi', \phi', x) &= H(x)\, L^T(x, \sigma' \times \bar\sigma'). \end{aligned}$$

Lean: `GlobalTheory.ZEul.Smooth.zint_eq_mul_partialL_smooth` (also `GlobalTheory.T.unfoldedThetaIntegral_eq_mul_partialRankinSelbergL`, a wrapper).

*Proof.* The proof follows that of [the $\mathrm{GL}_n \times \mathrm{GL}_m$ theorem](/entry/rs-nm-partial-l-eq-div/), with the theta integral in place of the mirabolic integral. Apply [the unfolded theta integral](/entry/theta-z-eq-mul-eul-d/) to $\sigma$ and to $\sigma'$. This gives the spaces $\pi$, $\pi'$, ordered Satake parameters $\alpha_w$, $\alpha'_w$ for $w \notin T$, and the finiteness of $D^T(\alpha, x)$ and $D^T(\alpha', x)$ for $x > 1$.

We take three results as given. First, there is one Whittaker bump with Shintani's formula: a function on $\mathrm{GL}_a(\mathbb{A})$ such that each of $\pi$ and $\pi'$ contains, in its smooth span, a vector $\phi$ (resp. $\phi'$) whose Whittaker function equals this bump times Shintani's formula outside $T$, with the parameters $\alpha_w$ (resp. $\alpha'_w$), and which is right invariant under $K_w$ for $w \notin T$ and under an open subgroup at $T$. Second, with these vectors there are $N$ and $\Phi$ as in the theorem and, for each Haar measure and each fundamental domain $\mathcal{F}_0$ of $N_a(E)$, measurable $f \ge 0$ and $t$ with $f$ integrable, $\int_{\mathcal{F}_0} f > 0$ and $t$ bounded on the support of $f$, such that for $x > 1$ each of the three unfolded integrals
$$\int_{\mathcal{F}_0} \Psi_{W_{\phi_1}, W_{\phi_2}}(g, e_a g)\, |\det g|^x\, dg, \qquad (\phi_1, \phi_2) \in \{(\phi, \phi'), (\phi, \phi), (\phi', \phi')\},$$
with $\Psi$ formed with $\Phi$, $J = N\mathcal{O}_E$ and $\eta = e_a$, converges absolutely and equals $\int_{\mathcal{F}_0} f e^{xt}$ times the Schur series $\sum_{(\lambda_w)} \prod_w s_{\lambda_w}(\alpha_{1,w})\overline{s_{\lambda_w}(\alpha_{2,w})} Nw^{-|\lambda_w| x}$ of the corresponding parameters. This is the cell argument of [the unfolding section](/entry/lintegral-unfolded-eq/), applied to a polarized pair: the Whittaker functions of $\phi$ and $\phi'$ have the same bump, so the same $f$ and $t$ serve the three pairs. Third, there is $c > 0$ such that $Z(\phi_1, \phi_2, x) = c$ times the unfolded integral, for $x > 1$, by the unfolding of [the unfolding section](/entry/theta-z-eq-mul-eul-d/).

Put $H(s) = c\int_{\mathcal{F}_0} f(g) e^{s t(g)}\, dg$. As in [the $\mathrm{GL}_n \times \mathrm{GL}_m$ theorem](/entry/rs-nm-partial-l-eq-div/), $H$ is entire, real on the real line and positive there. Finally, the Cauchy identity (Macdonald, Chapter I, (4.3)) at each place, with the finiteness of $D^T$, shows that the Schur series equals the product $\prod_{w \notin T} L_{Nw}(\alpha_{1,w}, \bar\alpha_{2,w}, x)$. Since the multisets of entries of $\alpha_w$ and $\alpha'_w$ are the Satake parameters of $\sigma$ and $\sigma'$, this product is $L^T(x, \sigma_1 \times \bar\sigma_2)$. $\square$

The second theorem uses one more result, which we take as given: the continuation of the theta integral by Poisson summation, as in the Background theorem of Jacquet, Piatetski-Shapiro and Shalika on the mirabolic Eisenstein series. We state the form we use. Let $z$ be the central element of $\mathrm{GL}_a(\mathbb{A})$ that is the scalar $e$ at every archimedean place and $1$ at the finite places, and let $\mathcal{F}'$ be a fundamental domain for the group generated by $\mathrm{GL}_a(E)$ and $z$.

**Theorem 8.5.3 (Continuation of the theta integral).** Let $\Phi$, $J$, $\eta$, a Haar measure, $\mathcal{F}$ and $\mathcal{F}'$ be as above. Then there is a constant $c \in \mathbb{C}$ with the following property. Let $\pi$ and $\pi'$ be spaces of cusp forms with unitary central characters $\omega$ and $\omega'$, and let $\phi$ and $\phi'$ be bounded smooth vectors, each in its space or in its smooth span. Then there is a function $F_Z$, analytic at every real $x > 0$, with $F_Z(x) = (x - 1)Z(\phi, \phi', x)$ for $x > 1$, with $F_Z(1) = c\int_{\mathcal{F}'} \phi\bar\phi'$ when $\omega = \omega'$, and with $F_Z(1) = 0$ when $\omega \neq \omega'$.

Lean: `GlobalTheory.T.thetaIntegral_continuation_nearRealHalfLine_poleOne`.

**Theorem 8.5.4 (Same-degree continuation).** Let $a \ge 1$, let $T$ be good, and let $\sigma$, $\sigma'$ be unitary cuspidal representations of $\mathrm{GL}_a$ over $E$, unramified outside $T$. Then there is a function $F$ on $\mathbb{C}$ such that:

1. $F$ is analytic at every real $x > 0$;
2. if $\sigma \neq \sigma'$, then $F(1) = 0$;
3. for every real $x > 1$ the product $\prod_{w \notin T} \ell_w(\sigma, \sigma', x)$ converges unconditionally to $F(x)/(x - 1)$.

Lean: `GlobalTheory.RSNonvan.samedeg_continuation` (also `GlobalTheory.T.rankinSelberg_sameDegree_meromorphic_continuation`, a wrapper).

*Proof.* Take $N$, $\Phi$, $\pi$, $\pi'$, $\phi$ and $\phi'$ from the [theta Euler product](/entry/zint-eq-mul-partial-l-smooth/), and fix a Haar measure and fundamental domains $\mathcal{F}$ and $\mathcal{F}'$. Let $H$ be the entire function given there. The vectors of the smooth span of a unitary cuspidal representation are bounded, so the continuation theorem applies to $\phi$ and $\phi'$ and gives $F_Z$. Put $F = F_Z/H$. Since $H$ is entire and $H(x) > 0$ for real $x$, $F$ is analytic at every real $x > 0$.

Let $\sigma \neq \sigma'$. If $\omega \neq \omega'$, then $F_Z(1) = 0$. If $\omega = \omega'$, then $F_Z(1) = c\int_{\mathcal{F}'} \phi\bar\phi'$. Distinct spaces of cusp forms with the same central character are orthogonal for the Petersson inner product, and the orthogonality passes to the smooth spans, since right translation and archimedean convolution preserve the orthogonal complement of $\pi'$. So $F_Z(1) = 0$ in both cases, and $F(1) = 0$.

Let $x > 1$. By the theta Euler product,
$$\frac{F(x)}{x - 1} = \frac{Z(\phi, \phi', x)}{H(x)} = \prod_{w \notin T} \ell_w(\sigma, \sigma', x),$$
where the product means the limit over finite sets of places. Part 2 of the logarithm lemma of [the first section](/entry/cell-lintegral/) says that this product converges unconditionally for unitary $\sigma$ and $\sigma'$ and $x > 1$. So the product converges unconditionally to $F(x)/(x - 1)$. $\square$

**Remark 8.5.5 (Formalization).** The integral $Z$ with $J = N\mathcal{O}_E$ and $\eta = e_a$ is `Zint`; the identity with the theta integral of the unfolding section is `zint_eq_thetaZ` in [RankinSelbergSameDegreeMeromorphicContinuation.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/RankinSelbergSameDegreeMeromorphicContinuation.lean#L91). Good sets are `IsGood` in [IsGoodEmptyIff.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/IsGoodEmptyIff.lean#L16); the theta Euler product takes its two parts as separate hypotheses. The fundamental domain $\mathcal{F}'$ is for `latticeGL`, the group generated by $\mathrm{GL}_a(E)$ and the archimedean scalar $e$. The theta Euler product is stated with `tprod`, a value that exists even when a product does not converge; the unconditional convergence in the second theorem comes from the logarithm lemma. The proof of the theta Euler product, at [line 34](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/UnfoldedThetaIntegralEqMulPartialRankinSelbergL.lean#L34), calls the unfolded theta integral theorem and keeps only the Satake lists and the finiteness of $D^T$. The bump, the cell computation for polarized pairs, the unfolding constant and the continuation are cited statements whose proofs we have not opened. The continuation also says that $c \neq 0$ when $\Phi$ is real, nonnegative and nonzero; this part is not used here. Both wrappers raise `maxHeartbeats` to 1000000.
