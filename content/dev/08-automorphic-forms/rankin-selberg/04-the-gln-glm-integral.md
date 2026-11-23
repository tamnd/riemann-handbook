---
title: The integral for GL(n) × GL(m)
decls:
  - GlobalTheory.RSnmUnf.rs_nm_partialL_eq_div
  - GlobalTheory.T.rankinSelberg_GLn_GLm_partialL_eq_div_entire
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The integral for GL(n) × GL(m)

Let $\sigma$ and $\sigma'$ be unitary cuspidal representations of $\mathrm{GL}_n$ and $\mathrm{GL}_m$ with $m < n$. This section proves that the partial Rankin-Selberg product $L^T(x, \sigma \times \bar\sigma')$ is, for real $x > 1$, the quotient $F(x)/H(x)$ of two entire functions, where $H$ is real and positive on the real line. The numerator is the global integral of Jacquet, Piatetski-Shapiro and Shalika, which needs no Eisenstein series when $m < n$ ([Rankin-Selberg integrals](/learn/trace-formula/#rankin-selberg-integrals)). The denominator collects the archimedean and ramified data. The result is the input to [the off-diagonal lemma](/entry/rsnonvan-off-diag/), which treats pairs of different degrees.

We keep the notation of the previous sections: $E$ is a totally complex number field, $T$ a finite set of finite places, $\iota(h) = \mathrm{diag}(h, 1_{n-m})$, and $L_q(A, B, s)$ and $D^T(\alpha, x)$ are as in [the first section](/entry/cell-lintegral/). For a fundamental domain we write $\mathcal{F}$ for $\mathrm{GL}_m(E)$ in $\mathrm{GL}_m(\mathbb{A})$ and $\mathcal{F}_0$ for $N_m(E)$ in $\mathrm{GL}_m(\mathbb{A})$.

**Definition 8.4.1 (The global integral).** Let $\Phi$ be a Schwartz-Bruhat function on $\mathbb{A}^m$, let $\phi$ be a function on $\mathrm{GL}_n(\mathbb{A})$ and $\phi'$ a function on $\mathrm{GL}_m(\mathbb{A})$. Put
$$\phi_\Phi(g) = \int_{\mathbb{A}^m} \Phi(y)\, \phi\big(g\, c(y)\big)\, dy,$$
where $c(y) \in N_n(\mathbb{A})$ is the unipotent element that carries $y$ in one column. Let $\mathbb{P}\phi_\Phi$ be its partial Whittaker coefficient of level $m + 1$: the function obtained from $\phi_\Phi$ by taking, one column at a time for the columns $n, n - 1, \dots, m + 2$, the Fourier coefficient along the column at the character $\psi$ of the entry just above the diagonal. For $s \in \mathbb{C}$ put
$$Z(s) = \int_{\mathcal{F}} \mathbb{P}\phi_\Phi\big(\iota(h)\big)\, \overline{\phi'(h)}\, |\det h|^{s - \frac{n - m}{2}}\, dh.$$

The projection $\mathbb{P}$ is the operator that restricts a cusp form on $\mathrm{GL}_n$ to the mirabolic subgroup of $\mathrm{GL}_{m+1}$, as in the Remark of [Rankin-Selberg integrals](/learn/trace-formula/#rankin-selberg-integrals). The smoothing by $\Phi$ along a column supplies the Schwartz-Bruhat function that appears in the unfolded integral below. For cusp forms the integral converges for every $s$, because $\phi$ and $\phi'$ decay rapidly on a Siegel set.

**Theorem 8.4.2 (Rankin-Selberg for $\mathrm{GL}_n \times \mathrm{GL}_m$).** Let $1 \le m < n$. Let $\sigma$ and $\sigma'$ be unitary cuspidal representations of $\mathrm{GL}_n$ and $\mathrm{GL}_m$ over $E$, both unramified outside $T$. Assume that for every finite $w \notin T$ the character $\psi_w$ has conductor $\mathcal{O}_w$. Then there are entire functions $F$ and $H$ on $\mathbb{C}$ such that, for every real $x$, $H(x)$ is real and $H(x) > 0$, and for every real $x > 1$ the product
$$\prod_{w \notin T} L_{Nw}\big(\mathrm{sat}(\sigma, w), \overline{\mathrm{sat}(\sigma', w)}, x\big)$$
converges unconditionally to $F(x)/H(x)$.

Lean: `GlobalTheory.RSnmUnf.rs_nm_partialL_eq_div` (also `GlobalTheory.T.rankinSelberg_GLn_GLm_partialL_eq_div_entire`, a wrapper).

*Proof.* Write $m = m_0 + 1$ and $n = m_0 + r + 2$. Fix Haar measures and the fundamental domains $\mathcal{F}$ and $\mathcal{F}_0$; they exist since $\mathrm{GL}_m(E)$ and $N_m(E)$ are discrete in $\mathrm{GL}_m(\mathbb{A})$.

Step 1 (Satake parameters and finiteness). Apply [the unfolded theta integral](/entry/theta-z-eq-mul-eul-d/) to $\sigma$ and to $\sigma'$. It gives spaces of cusp forms $\pi$ and $\pi'$ in the classes $\sigma$ and $\sigma'$, ordered Satake parameters $\alpha_w \in (\mathbb{C}^\times)^n$ and $\beta_w \in (\mathbb{C}^\times)^m$ for $w \notin T$, whose multisets of entries are $\mathrm{sat}(\sigma, w)$ and $\mathrm{sat}(\sigma', w)$, and the finiteness of $D^T(\alpha, x)$ and $D^T(\beta, x)$ for $x > 1$. We use nothing else from that theorem.

Step 2 (Matched vectors). Apply [the matched vectors theorem](/entry/matched-vectors/) with $S = T$. It gives $\phi$ in the smooth span of $\pi$, $\phi'$ in the smooth span of $\pi'$ and a weight $\kappa \ge 0$, with Shintani's formula at every $w \notin T$ and $W_\phi(\iota(h)) = \kappa(h)W_{\phi'}(h)$ on $G_m(T)$.

Step 3 (The unfolded integral as a Dirichlet series). For $\lambda \in \mathbb{Z}^m$ and $w \notin T$ put
$$a_w(\lambda, x) = s_{\bar\lambda}(\alpha_w)\, \overline{s_\lambda(\beta_w)}\, Nw^{-|\lambda| x}$$
if $\lambda$ is a partition, where $\bar\lambda \in \mathbb{N}^n$ is $\lambda$ padded with zeros, and $a_w(\lambda, x) = 0$ otherwise. We take the following computation as given. There are a Schwartz-Bruhat function $\Phi$ on $\mathbb{A}^m$ and, for the chosen Haar measure and $\mathcal{F}_0$, measurable real functions $f \ge 0$ and $t$ on $\mathrm{GL}_m(\mathbb{A})$ with $f$ integrable on $\mathcal{F}_0$, $\int_{\mathcal{F}_0} f > 0$ and $t$ bounded on the support of $f$, such that for every $x > 1$ with $D^T(\alpha, x)$ and $D^T(\beta, x)$ finite: the integrals
$$\int_{\mathcal{F}_0} |W_\phi(\iota(h))|^2\, |\hat\Phi(e_m h)|\, |\det h|^{x - r - 1}\, dh, \qquad \int_{\mathcal{F}_0} |W_{\phi'}(h)|^2\, |\hat\Phi(e_m h)|\, |\det h|^{x}\, dh$$
are finite, and
$$\begin{aligned} \int_{\mathcal{F}_0} W_\phi(\iota(h))\, \overline{W_{\phi'}(h)}\, \hat\Phi(e_m h)\, |\det h|^{x - \frac{n - m}{2}}\, dh &= \Big(\int_{\mathcal{F}_0} f(g)\, e^{x t(g)}\, dg\Big) \\ &\quad \times \sum_{(\lambda_w)} \prod_{w} a_w(\lambda_w, x), \end{aligned}$$
the sum over finitely supported families $(\lambda_w)_{w \notin T}$ in $\mathbb{Z}^m$. This is the cell argument of [the unfolding section](/entry/lintegral-unfolded-eq/) for the pair $(\phi, \phi')$: $\kappa$ and the data at $T$ and at infinity go into $f$ and $t$, and the matched Shintani formulas of Step 2 give the product of $a_w$ on the cell of $(\lambda_w)$.

Step 4 (Unfolding). We also take as given the unfolding of the global integral: there is a constant $c > 0$, depending only on $m$, $r$ and the Haar measure, such that for all $\phi$, $\phi'$ in the smooth spans, every Schwartz-Bruhat $\Phi$ and every real $x$ for which the two integrals of Step 3 are finite, $Z(x)$ equals $c$ times the left side of Step 3. This is the unfolding of Jacquet, Piatetski-Shapiro and Shalika: the Fourier expansion of $\mathbb{P}\phi_\Phi$ along $N_m$ replaces $\mathcal{F}$ by $\mathcal{F}_0$ and $\phi$ by $W_\phi$, and the column integral turns $\Phi$ into $\hat\Phi$.

Step 5 (Entire functions). Put $F = Z$. Every vector of the smooth span of a unitary cuspidal representation is continuous and decays rapidly, with its contragredient, so the integral $Z(s)$ converges absolutely for every $s$ and is analytic in $s$. Put
$$H(s) = c \int_{\mathcal{F}_0} f(g)\, e^{s t(g)}\, dg.$$
Since $f \ge 0$ is integrable and $|t| \le R$ on the support of $f$, the integrand is bounded by $f e^{R|s|}$, and differentiation under the integral shows that $H$ is entire. For real $x$, $H(x)$ is real and $H(x) \ge c\, e^{-R|x|} \int_{\mathcal{F}_0} f > 0$.

Step 6 (The Cauchy identity). Let $x > 1$. We take as given: if $D^T(\alpha, x)$ and $D^T(\beta, x)$ are finite, then the product $\prod_{w \notin T} L_{Nw}(\alpha_w, \bar\beta_w, x)$ converges unconditionally to a number $P$, and the series $\sum_{(\lambda_w)} \prod_w a_w(\lambda_w, x)$ converges to the same $P$. At each place this is the Cauchy identity
$$\sum_{\lambda} s_\lambda(\alpha_1, \dots, \alpha_n)\, s_\lambda(\bar\beta_1, \dots, \bar\beta_m)\, u^{|\lambda|} = \prod_{i = 1}^n \prod_{j = 1}^m (1 - \alpha_i \bar\beta_j u)^{-1},$$
the sum over partitions of length at most $m$ (Macdonald, Chapter I, (4.3)), with $u = Nw^{-x}$; note $\overline{s_\lambda(\beta)} = s_\lambda(\bar\beta)$ since $s_\lambda$ has integer coefficients. The finiteness of $D^T$ and the Cauchy-Schwarz inequality give the absolute convergence of the product of the local series.

Conclusion. For $x > 1$, Steps 3, 4 and 6 give $F(x) = Z(x) = c \int_{\mathcal{F}_0} f e^{xt} \cdot P = H(x) P$. Since $H(x) \neq 0$, $P = F(x)/H(x)$, and the Euler product of the theorem is $\prod_w L_{Nw}(\alpha_w, \bar\beta_w, x)$, because the multiset of entries of $\alpha_w$ is $\mathrm{sat}(\sigma, w)$ and that of $\beta_w$ is $\mathrm{sat}(\sigma', w)$. $\square$

**Remark 8.4.3 (Formalization).** The proof, in [RankinSelbergGLnGLmPartialLEqDivEntire.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/RankinSelbergGLnGLmPartialLEqDivEntire.lean#L34), calls the theta integral theorem at lines 34 to 37 and keeps only the Satake lists and the finiteness of $D^T$; the theta identity itself is discarded. The cell computation of Step 3, the unfolding of Step 4 and the Cauchy identity of Step 6 are separate statements (`unfolded_rankinSelberg_cellIntegral_matchedVectors`, `rankinSelbergGLnGLm_unfolding_to_mirabolic`, `eulerProduct_rankinSelbergGLnGLm_dirichletSeries`), cited by the proof; we have opened their statements, not their proofs. Step 5 uses `rsIntegral_entire_good` with the class `goodFns`, which we have not unfolded, and `exp_integral_entire_real_pos`. The column element $c(y)$ (`colGL`) is also not unfolded. The statement uses the complex conjugates of the Satake parameters of $\sigma'$, not the contragredient, and it uses only the conductor condition at the places outside $T$, not a full goodness condition on $T$. The wrapper raises `maxHeartbeats` to 1000000.
