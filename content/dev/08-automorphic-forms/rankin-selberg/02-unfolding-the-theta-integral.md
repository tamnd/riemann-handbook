---
title: Unfolding the theta integral
decls:
  - GlobalTheory.RSCell.lintegral_unfolded_eq
  - GlobalTheory.T.unfoldedWhittakerIntegral_eq_eulerProduct_schurSums
  - GlobalTheory.RSEulerId.thetaZ_eq_mul_eulD
  - GlobalTheory.T.unfolded_theta_integral_eq_mul_schur_euler_product
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Unfolding the theta integral

This section writes the Rankin-Selberg integral of a cusp form against itself, with a theta series in the mirabolic variable, as a positive smooth function times the Schur Dirichlet series $D^T$ of the [previous section](/entry/cell-lintegral/). The integral is that of [Rankin-Selberg integrals](/learn/trace-formula/#rankin-selberg-integrals) for $\mathrm{GL}_a \times \mathrm{GL}_a$, written with a sum over $E^a \setminus \{0\}$ in place of an Eisenstein series. The result shows that the theta integral is finite and that the Schur Euler product $D^T$ is finite for $x > 1$. Both later proofs, [the $\mathrm{GL}_n \times \mathrm{GL}_m$ integral](/entry/rs-nm-partial-l-eq-div/) and [the same-degree integral](/entry/zint-eq-mul-partial-l-smooth/), use it to choose their data.

We keep the notation of the previous section, and we put $G = \mathrm{GL}_a$ with $a \ge 1$. We index rows by $1, \dots, a$, so $e_a$ is the last basis row vector and $e_a g$ is the last row of $g$. Let $\mathbb{A}_\infty = \prod_{v \mid \infty} E_v$ and $\mathbb{A}_f$ be the archimedean and finite parts of $\mathbb{A}$.

**Definition 8.2.1 (Whittaker coefficient).** Fix a nontrivial additive character $\psi$ of $\mathbb{A}/E$ and put $\psi_N(u) = \psi(u_{12} + u_{23} + \dots + u_{a-1,a})$ for $u \in N(\mathbb{A})$. For a continuous function $\phi$ on $G(E) \backslash G(\mathbb{A})$ its Whittaker coefficient is
$$W_\phi(g) = \int_{N(E) \backslash N(\mathbb{A})} \phi(ug)\, \overline{\psi_N(u)}\, du.$$

So $W_\phi(ug) = \psi_N(u) W_\phi(g)$ for $u \in N(\mathbb{A})$, and $|W_\phi|$ is left $N(\mathbb{A})$-invariant. See [Whittaker functions](/learn/automorphic-forms/#fourier-coefficients-and-whittaker-functions).

**Definition 8.2.2 (Smooth span).** Let $\pi_0$ be an irreducible space of cusp forms. Its *smooth span* is the smallest space of functions on $G(\mathbb{A})$ that contains $\pi_0$, is stable under right translations, and is stable under the operators $F \mapsto \int k(y) F(g\gamma(y))\, d\nu(y)$ with rapidly decreasing kernels $k$.

The smooth span contains the vectors of $\pi_0$ smoothed at the archimedean places, and its elements are still left $G(E)$-invariant. We need it because the bump vectors of the proofs are built by such integrals.

**Definition 8.2.3 (Theta kernel).** For $u \in \mathbb{A}_\infty^a$ with $u_a$ invertible, let $r(u) \in G(\mathbb{A}_\infty)$ be the identity matrix with its last row replaced by $u$. Let $\phi, \phi'$ be functions on $G(\mathbb{A})$, let $\Phi$ be a function on $\mathbb{A}_\infty^a$ supported in the set where $u_{a, v} \neq 0$ for every archimedean $v$, let $J$ be a fractional ideal of $E$ with closure $\hat J \subset \mathbb{A}_f$, and let $\eta \in \mathbb{A}_f^a$. For $g \in G(\mathbb{A})$ and $y = (y_\infty, y_f) \in \mathbb{A}^a$ put
$$\Psi(g, y) = \phi\big(g\, r(y_\infty)^{-1}\big)\, \overline{\phi'\big(g\, r(y_\infty)^{-1}\big)}\, \Phi(y_\infty)\, \mathbf{1}_{\eta + \hat J^a}(y_f),$$
and for a measurable fundamental domain $\mathcal{F}$ of $G(E)$ in $G(\mathbb{A})$ and $x \in \mathbb{R}$ put
$$Z(\phi, \phi', x) = \int_{\mathcal{F}} \sum_{\xi \in E^a \setminus 0} \Psi(g, \xi g)\, |\det g|^x \, dg.$$

The inner sum is a theta series in $\xi$. The integral $Z$ is the Rankin-Selberg integral of $\phi$ against $\bar\phi'$; the factor $r(y_\infty)^{-1}$ moves the archimedean part of the row $\xi g$ back to $e_a$ in the Whittaker model. The orbit of $e_a$ under $G(E)$ is $E^a \setminus 0$, so $Z$ unfolds to an integral over $P(E) \backslash G(\mathbb{A})$, where $P$ is the stabilizer of $e_a$ (the mirabolic subgroup), and then, by the Fourier expansion of a cusp form along $P$, to an integral of Whittaker functions over $N(E) \backslash G(\mathbb{A})$. We use this unfolding below as a lemma.

**Theorem 8.2.4 (Unfolded Whittaker integral).** Let $\pi$ be a unitary cuspidal representation of $\mathrm{GL}_a$ over $E$, $a \ge 1$, unramified outside $T$. Then there are:

- a family $\alpha_w \in (\mathbb{C}^\times)^a$, $w \notin T$, whose multiset of entries is $\mathrm{sat}(\pi, w)$;
- a space of cusp forms $\pi_0$ in the class $\pi$ with unitary central character $\omega$;
- a nonzero $\phi$ that lies in $\pi_0$ or in its smooth span;
- a smooth compactly supported $\Phi \neq 0$ on $\mathbb{A}_\infty^a$ with real values $\ge 0$ and support in the set where $u_{a, v} \neq 0$ for all archimedean $v$;
- a fractional ideal $J$ and $\eta \in \mathbb{A}_f^a$,

such that the following holds. For every Haar measure $dg$ on $G(\mathbb{A})$ and every measurable fundamental domain $\mathcal{F}_0$ of $N(E)$ there is $H \colon \mathbb{R} \to \mathbb{R}$, continuous from the right at $1$, with $H(1) > 0$, and for all $x > 1$, $H(x) > 0$ and
$$\int_{\mathcal{F}_0} \big|\Psi_{W_\phi, W_\phi}(g, e_a g)\big|\, |\det g|^x\, dg = H(x)\, D^T(\alpha, x) \quad \text{in } [0, \infty].$$

Lean: `GlobalTheory.RSCell.lintegral_unfolded_eq` (also `GlobalTheory.T.unfoldedWhittakerIntegral_eq_eulerProduct_schurSums`, a wrapper).

*Proof.* Write $a = m + 1$. Choose $\pi_0$, $\omega$ and the ordered parameters $\alpha_w$. Choose a vector $F$ in the smooth span of $\pi_0$, an open compact subgroup $U$ of $G(\mathbb{A}_f)$ that fixes $F$ on the right, and a shift $l_0 \in \Lambda_T$ with last coordinates $0$, such that $W_F(1) \neq 0$, $F$ is right invariant under the elements of $U_T$ that are $1$ at the archimedean places and at $T$, and $W_F$ obeys Shintani's formula shifted by $l_0$: for $p$ in the mirabolic part of $G(\mathbb{A})$ with $p_w = 1$ for $w \notin T$ finite, and for $l \in \Lambda_T$ with nonnegative last coordinates,
$$W_F(p\, t_{l_0 + l}) = W_F(p\, t_{l_0}) \prod_{w} c_w(l_w),$$
where $c_w(l_w)$ is the Shintani value $Nw^{-\langle \rho, l_w \rangle} s_{l_w}(\alpha_w)$ if $l_w$ is a partition and $0$ otherwise (with $\langle \rho, l \rangle = \sum_i \frac{a + 1 - 2i}{2} l_i$). Then $F$ is continuous, since a right translate by an open subgroup fixes it, and $|W_F|$ is continuous and left $N(\mathbb{A})$-invariant. Choose $\Phi$ and $J$ so that the support of $\Phi$ and the lattice $e_a + \hat J^a$ are compatible with $U$, and put $\eta = e_a$, $\phi = F$.

Let $B_x(g) = |\Psi_{W_F, W_F}(t_{l_0} g, e_a t_{l_0} g)|\, |\det t_{l_0} g|^x$, a continuous left $N(\mathbb{A})$-invariant function, since $t_{l_0}$ normalizes $N(\mathbb{A})$. Apply [the cell decomposition](/entry/cell-lintegral/) to the integrand, with $S = T$. On a cell, the Shintani formula and the invariance under $U$ and $U_T$ give, for $g \in C_0$,
$$d(l) \cdot \big(\text{integrand at } t_l g\big) = d(l_0)\, B_x(g)\, c_x(l - l_0),$$
where $c_x(l) = \prod_{w} c_{x,w}(l_w)$, with $c_{x,w}(l_w) = |s_{l_w}(\alpha_w)|^2 Nw^{-|l_w| x}$ if $l_w$ is a partition and $0$ otherwise. As $l$ runs over $\Lambda_T$, so does $l - l_0$, and the sum of a product of local terms over finitely supported families is the product of the local sums. So $\sum_{l \in \Lambda_T} c_x(l - l_0) = D^T(\alpha, x)$. So the integral equals $D^T(\alpha, x)$ times $H(x) = d(l_0) \int_{\mathcal{F}_0 \cap C_0} B_x\, dg$. Last, $B_x$ is continuous and $\ge 0$, $B_x(1) > 0$ because $W_F(1) \neq 0$ and $\Phi(e_a) \neq 0$, and $B_x$ is supported in $N(\mathbb{A}) K$ for a compact $K$ on $C_0$. An integral of such a function over $\mathcal{F}_0 \cap C_0$ is positive, finite and continuous in $x$; this gives the properties of $H$. $\square$

**Theorem 8.2.5 (Unfolded theta integral).** Let $\pi$ be a unitary cuspidal representation of $\mathrm{GL}_a$ over $E$, $a \ge 1$, unramified outside $T$. Then there are $\alpha$, $\pi_0$, $\omega$, $\phi$, $\Phi$, $J$, $\eta$ with the properties listed in the previous theorem, such that for every Haar measure $dg$ on $G(\mathbb{A})$ and every measurable fundamental domain $\mathcal{F}$ of $G(E)$ there is $H \colon \mathbb{R} \to \mathbb{R}$, continuous from the right at $1$, with $H(1) > 0$, and for all $x > 1$: $H(x) > 0$, $D^T(\alpha, x) < \infty$, and
$$Z(\phi, \phi, x) = H(x)\, D^T(\alpha, x).$$

Lean: `GlobalTheory.RSEulerId.thetaZ_eq_mul_eulD` (also `GlobalTheory.T.unfolded_theta_integral_eq_mul_schur_euler_product`, a wrapper).

*Proof.* Take the data of [the unfolded Whittaker integral](/entry/unfolded-whittaker-integral-eq-euler-product-schur-sums/), and a fundamental domain $\mathcal{F}_0$ of $N(E)$; let $H$ be its function. The vector $\phi$ lies in the smooth span of $\pi_0$, and $\pi_0$ is unitary, so $\phi$ is continuous. The unfolding lemma above gives
$$\int_{\mathcal{F}} \sum_{\xi \neq 0} \Psi_{\phi, \phi}(g, \xi g)\, |\det g|^x\, dg = \int_{\mathcal{F}_0} \big|\Psi_{W_\phi, W_\phi}(g, e_a g)\big|\, |\det g|^x\, dg$$
as integrals in $[0, \infty]$; here $\Psi_{\phi,\phi}$ is $\ge 0$ because $\Phi \ge 0$. A separate estimate, from the rapid decay of cusp forms in the smooth span, shows that the left side is finite for $x > 1$. So $H(x) D^T(\alpha, x) < \infty$, and since $H(x) > 0$, $D^T(\alpha, x) < \infty$. Last, because the theta integrand is $\ge 0$ and integrable, its Lebesgue integral $Z(\phi, \phi, x)$ is the real number of the integral in $[0, \infty]$. $\square$

**Remark 8.2.6 (Formalization).** The unfolding lemma, the finiteness estimate, the choice of the bump data, the shifted Shintani formula, the cell identity and the summation lemma are separate statements: `lintegral_rankinSelbergTheta_eq_whittakerUnfolding`, `lintegral_theta_self_cusp_rapid_span_ne_top`, `exists_cuspRep_bump_data_satake_unitary`, `exists_shifted_vector_shintani_formula_ramified`, `cell_identity_rankinSelberg_torus_translate` and `tsum_schurSquareCellProduct_eq_eulerProduct`. We did not open their proofs. The factor $c_x$ is `cellProd` in [LocFacOfNeg.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocFacOfNeg.lean#L22). The first theorem needs `maxHeartbeats 4000000` ([line 39](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/UnfoldedWhittakerIntegralEqEulerProductSchurSums.lean#L39)). The function $H$ is only a real function, continuous from the right at $1$; it is not claimed analytic. The theorems choose the vector $\phi$ and the data; they say nothing about an arbitrary vector of $\pi$. The second theorem drops the condition that the theta row is the last one, but its proof takes the last row.
