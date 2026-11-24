---
title: Hilbert-Schmidt bounds by the formal degree
decls:
  - GlobalTheory.T.besselOrbitalIntegral_eq_inv_deg_smul
  - GlobalTheory.SgInf.OO_eq_inv_deg_smul_Iint
  - GlobalTheory.T.lintegral_hsNormSq_doubleCoset_le_fatou
  - GlobalTheory.SgInf.lintegral_hsNormSq_Iint_le
  - GlobalTheory.T.lintegral_hsNormSq_matrixCoeff_le_formalDegree
  - GlobalTheory.SgInf.EllBound.lintegral_hsNormSq_ell_le
  - GlobalTheory.T.lintegral_hilbertSchmidtNormSq_besselAmplitude_le
  - GlobalTheory.Amp.SchurNorm.lintegral_hsNormSq_ampJ_le
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Hilbert-Schmidt bounds by the formal degree

The archimedean amplitude of a term is an operator from $W_q$ to $W_p$ that depends on a double coset of $G$ for the two Bessel subgroups. This section proves that its squared Hilbert-Schmidt norm, integrated over the double cosets, is at most $\dim W_p \dim W_q / d$, where $d$ is the formal degree. This is the archimedean input of the step [HypsAlt is nonempty from the closed bound](/step/nonempty-hyps/). The proof has four steps. First, the orbital integral of two Bessel functions is a two-sided integral of one matrix coefficient. Second, the integral over the double cosets of the squared norm of this two-sided integral is bounded by the Bessel forms, with a Følner truncation and Fatou's lemma. Third, for rank one Bessel functionals the bound becomes $1/d$. Fourth, a given pair of Bessel maps is a pair of multiples of rank one functionals, by the [last section](/entry/exists-is-ell-smul/).

We keep the [archimedean setting](/entry/exists-bessel-ext/) of the last section: the group $G$, the standard data $(\sigma, w, a, \mu_G, d)$, the matrix coefficients $c_{u,v}(g) = \langle v, \sigma(g)u\rangle$, the span $D(w)$, and side data with the Bessel form $\beta$. We now have two side data $(z, \pi, \mu_S)$ on $W_p$ and $(z', \pi', \mu_{S'})$ on $W_q$, with characters $\psi$, $\psi'$, maps $\Pi$, $\Pi'$ and Bessel forms $\beta$, $\beta'$. For $a \in W_p$ and $b \in W_q$ write $a \otimes b^*$ for the rank one operator $\xi \mapsto \langle b, \xi\rangle a$ from $W_q$ to $W_p$. For an operator $A \colon W_q \to W_p$ let $\|A\|_{HS}^2 = \sum_i \|A e_i\|^2$ for an orthonormal basis $(e_i)$ of $W_q$.

### Double cosets and the two-sided integral

**Definition 2.18.1 (Regular double cosets and disintegration).** The *regular set* $G_{\mathrm{reg}} \subseteq G$ for $(z, z')$ is the set of $\gamma \in G$ such that a fixed sequence of $r + 1$ minors of $\gamma$, formed with $z$ and $z'$, and a fixed Gram determinant of $\gamma$ are all nonzero. The group $S_z \times S_{z'}$ acts on $G$ by $(p_1, p_2) \cdot \gamma = p_1 \gamma p_2^{-1}$. A measure $\nu$ on $G$ *disintegrates* $\mu_G$ over the regular double cosets if $\nu$ is $\sigma$-finite, $\nu$-almost every $\gamma$ lies in $G_{\mathrm{reg}}$, and for every measurable $f \ge 0$ on $G$,
$$\int_G f\, d\mu_G = \int \int_{S_z \times S_{z'}} f(p_1 \gamma p_2^{-1})\, d(\mu_S \times \mu_{S'})(p_1, p_2)\, d\nu(\gamma).$$

**Definition 2.18.2 (Two-sided integral and orbital integral).** For $x, y \in H$, $\xi \in W_p$, $\xi' \in W_q$ and $\gamma \in G$ the *two-sided integral* is
$$\begin{aligned} I_{x,y}(\xi, \xi'; \gamma) = \int_{S_z \times S_{z'}} {}& c_{x,y}(p_1 \gamma p_2^{-1}) \\ & \cdot \Pi(p_1^{-1})\xi \otimes (\Pi'(p_2^{-1})\xi')^* \, d(p_1, p_2). \end{aligned}$$
For functions $\Phi \colon G \to W_p$ and $\Phi' \colon G \to W_q$ the *orbital integral* is
$$O(\Phi, \Phi')(\gamma) = \int_G \Phi(x) \otimes \Phi'(\gamma^{-1} x)^*\, d\mu_G(x).$$

The function $A_{u,v,\xi}(x) = \beta(\sigma(x) u, v)\xi$ is the Bessel function of $u$ for the second vector $v$ and the vector $\xi$; it satisfies $A(h m x) = \psi(m)\pi(h) A(x)$.

**Proposition 2.18.3 (Orbital integrals of Bessel functions).** Let $(\sigma, w, a, \mu_G, d)$ be standard and let $(z, \pi, \mu_S)$ and $(z', \pi', \mu_{S'})$ be side data, with $c, c' \in \mathbb{C}^r$. Let $w_0, w'_0 \in D(w)$, $\xi \in W_p$, $\xi' \in W_q$ and $\gamma \in G_{\mathrm{reg}}$. Then the integrands of $I_{w'_0, w_0}(\xi, \xi'; \gamma)$ and of $O(A_{w,w_0,\xi}, A'_{w,w'_0,\xi'})(\gamma)$ are integrable, and
$$O(A_{w,w_0,\xi}, A'_{w,w'_0,\xi'})(\gamma) = \frac{1}{d}\, I_{w'_0, w_0}(\xi, \xi'; \gamma).$$

Lean: `GlobalTheory.SgInf.OO_eq_inv_deg_smul_Iint` (also `GlobalTheory.T.besselOrbitalIntegral_eq_inv_deg_smul`, a second name).

*Proof.* The matrix coefficients of $D(w)$ satisfy $|c_{u,v}(g)| \le C \|g\|^{-a}$. For $\gamma$ regular, the integral of $\|p_1 \gamma p_2^{-1}\|^{-a}$ over $S_z \times S_{z'}$ is finite, because $a$ is large. This gives the integrability of the first integrand. Write each Bessel function as an integral over its Bessel subgroup:
$$A_{w,w_0,\xi}(x) = \int_{S_z} \langle \sigma(p_1^{-1}) w_0, \sigma(x) w\rangle\, \Pi(p_1^{-1})\xi \, dp_1,$$
and similarly for $A'$ at $\gamma^{-1}x$, with $\sigma(p_2 \gamma^{-1} x) = \sigma(p_2\gamma^{-1})\sigma(x)$. The product of the two absolute integrands is integrable on $G \times S_z \times S_{z'}$ by Schur orthogonality and the decay bound, so Fubini's theorem applies and gives the integrability of the second integrand. Integrate first over $x \in G$. By Schur orthogonality with formal degree $d$ and $\|w\| = 1$,
$$\int_G c_{w, \sigma(p_1^{-1})w_0}(x)\, \overline{c_{w, \sigma(\gamma p_2^{-1}) w'_0}(x)}\, dx = \frac{c_{w'_0, w_0}(p_1 \gamma p_2^{-1})}{d}.$$
The rank one operator is linear in its first vector and conjugate linear in its second vector, so the remaining integral over $S_z \times S_{z'}$ is $d^{-1} I_{w'_0, w_0}(\xi, \xi'; \gamma)$. $\square$

### The Fatou bound

**Theorem 2.18.4 (Integral of the two-sided integral).** Let $(\sigma, w, a, \mu_G, d)$ be standard, let $(z, \pi, \mu_S)$ and $(z', \pi', \mu_{S'})$ be side data, and let $\nu$ disintegrate $\mu_G$ over the regular double cosets. For $x, y \in D(w)$, $\xi \in W_p$ and $\xi' \in W_q$,
$$\begin{aligned} \int \|I_{x,y}(\xi, \xi'; \gamma)\|_{HS}^2\, d\nu(\gamma) \le {}& \frac{1}{d}\, \operatorname{Re}\langle \xi, \beta(y, y)\xi\rangle \\ & \cdot \operatorname{Re}\langle \xi', \beta'(x, x)\xi'\rangle. \end{aligned}$$

Lean: `GlobalTheory.SgInf.lintegral_hsNormSq_Iint_le` (also `GlobalTheory.T.lintegral_hsNormSq_doubleCoset_le_fatou`, a second name).

*Proof.* Since $n \ge 2$ and $a \ge 2n^5$, we have $a > 2n^2$. Then $\|s\|^{-a}$ is integrable on each Bessel subgroup, and so the coefficients $c_{y,y}$ on $S_z$ and $c_{x,x}$ on $S_{z'}$ are integrable. Choose Følner sequences $(\Omega_j)$ in $S_z$ and $(\Omega'_j)$ in $S_{z'}$: bounded measurable sets of finite positive measure whose translates overlap almost fully. Let $I^{(j)}$ be the two-sided integral with $\mu_S$ and $\mu_{S'}$ restricted to $\Omega_j$ and $\Omega'_j$. Its integrand has compact support, and the two-sided Bessel functional formula gives, for each $j$,
$$\int_G \|I^{(j)}(g)\|_{HS}^2\, d\mu_G(g) = \frac{1}{d}\, b_j\, b'_j,$$
where $b_j$ and $b'_j$ are overlap integrals of the coefficients of $y$ and $x$ over $\Omega_j$ and $\Omega'_j$. The function $g \mapsto \|I^{(j)}(g)\|_{HS}^2$ is continuous and nonnegative, so by the disintegration
$$\int_G \|I^{(j)}\|_{HS}^2\, d\mu_G = \int g_j(\gamma)\, d\nu(\gamma),$$
with $g_j(\gamma)$ the integral of $\|I^{(j)}(p_1 \gamma p_2^{-1})\|_{HS}^2$ over $S_z \times S_{z'}$. Three limits now combine. The Følner averages $b_j / \mu_S(\Omega_j)$ tend to $\langle \xi, \beta(y, y)\xi\rangle$, and $b'_j / \mu_{S'}(\Omega'_j)$ tends to $\langle \xi', \beta'(x, x)\xi'\rangle$. These limits are real, because $\beta(y, y)$ is self-adjoint. For each regular $\gamma$,
$$\|I_{x,y}(\xi, \xi'; \gamma)\|_{HS}^2 \le \liminf_{j} \frac{g_j(\gamma)}{\mu_S(\Omega_j)\, \mu_{S'}(\Omega'_j)}.$$
This holds for $\nu$-almost every $\gamma$. By Fatou's lemma, the integral of the left side for $\nu$ is at most the limit of
$$\frac{1}{\mu_S(\Omega_j)\, \mu_{S'}(\Omega'_j)} \int g_j\, d\nu = \frac{1}{d}\, \frac{b_j}{\mu_S(\Omega_j)}\, \frac{b'_j}{\mu_{S'}(\Omega'_j)},$$
and this limit is the right side of the Theorem. $\square$

### Rank one functionals and Bessel amplitudes

**Corollary 2.18.5 (Bound by the formal degree).** Let $(\sigma, w, a, \mu_G, d)$ be standard, let $(z, \pi, \mu_S)$ and $(z', \pi', \mu_{S'})$ be side data, let $\nu$ disintegrate $\mu_G$ over the regular double cosets, and let $\ell$ and $\ell'$ be rank one Bessel functionals on $D(w)$ for the two side data. Then
$$\int \big\| d \cdot O(\ell \circ \sigma(\cdot) w,\ \ell' \circ \sigma(\cdot) w)(\gamma) \big\|_{HS}^2\, d\nu(\gamma) \le \frac{1}{d}.$$

Lean: `GlobalTheory.SgInf.EllBound.lintegral_hsNormSq_ell_le` (also `GlobalTheory.T.lintegral_hsNormSq_matrixCoeff_le_formalDegree`, a second name).

*Proof.* Choose $w_0 \in D(w)$ with $\ell(w_0) \ne 0$, and put $\xi = \ell(w_0)/\|\ell(w_0)\|^2$, so that $\langle \ell(w_0), \xi\rangle = \langle \xi, \ell(w_0)\rangle = 1$. Then
$$\langle \xi, \beta(w_0, w_0)\xi\rangle = \langle \ell(w_0), \xi\rangle\, \langle \xi, \ell(w_0)\rangle = 1.$$
In the same way choose $w'_0$ and $\xi'$ for $\ell'$. Apply the [Theorem 2.18.4](/entry/lintegral-hs-norm-sq-iint-le/) with $x = w'_0$ and $y = w_0$; the right side is $1/d$. For the left side, $\beta(\sigma(g) w, w_0)\xi = \langle \ell(w_0), \xi\rangle\, \ell(\sigma(g) w) = \ell(\sigma(g) w)$, so the Bessel function $A_{w,w_0,\xi}$ is $\ell \circ \sigma(\cdot) w$, and $A'_{w,w'_0,\xi'}$ is $\ell' \circ \sigma(\cdot) w$. By the [Proposition 2.18.3](/entry/oo-eq-inv-deg-smul-iint/), for regular $\gamma$,
$$I_{w'_0, w_0}(\xi, \xi'; \gamma) = d \cdot O(\ell \circ \sigma(\cdot) w,\ \ell' \circ \sigma(\cdot) w)(\gamma).$$
This holds for $\nu$-almost every $\gamma$, so the two integrals over $\nu$ are equal. $\square$

**Definition 2.18.6 (Bessel amplitude).** For $c > 0$ and functions $\Phi \colon G \to W_p$, $\Phi' \colon G \to W_q$, the *Bessel amplitude* is
$$J_c(\Phi, \Phi')(\gamma) = \frac{1}{c} \int_G \Phi(\gamma x) \otimes \Phi'(x)^*\, d\mu_G(x).$$

By left invariance of $\mu_G$, $J_1(\Phi, \Phi')(\gamma) = O(\Phi, \Phi')(\gamma)$.

**Theorem 2.18.7 (Hilbert-Schmidt bound for Bessel amplitudes).** Let $v_0 \in H$ be nonzero and $w = v_0/\|v_0\|$, and let $(\sigma, w, a, \mu_G, d)$ be standard and smooth. Let $(z, \pi, \mu_S)$ and $(z', \pi', \mu_{S'})$ be irreducible side data with multiplicity one, with quotient measures $\nu_S$ and $\nu_{S'}$. Let $B$ and $B'$ be smooth Bessel maps for the two side data, and let $c_0 > 0$. Assume
$$\begin{aligned} \|B(\sigma(\cdot) v_0)\|_{L^2(\nu_S)}^2 &= c_0 \dim W_p, \\ \|B'(\sigma(\cdot) v_0)\|_{L^2(\nu_{S'})}^2 &= c_0 \dim W_q, \end{aligned}$$
and that for each of $B$ and $B'$ the $L^2$ norm of $B(\sigma(\cdot) v)$ is proportional to $\|v\|^2$ on smooth vectors, as in the [last section](/entry/exists-is-ell-smul/). Let $\nu$ disintegrate $\mu_G$ over the regular double cosets. Then
$$\int \big\| J_{c_0}\big(B \circ \sigma(\cdot) v_0,\ B' \circ \sigma(\cdot) v_0\big)(\gamma) \big\|_{HS}^2\, d\nu(\gamma) \le \frac{\dim W_p \dim W_q}{d}.$$

Lean: `GlobalTheory.Amp.SchurNorm.lintegral_hsNormSq_ampJ_le` (also `GlobalTheory.T.lintegral_hilbertSchmidtNormSq_besselAmplitude_le`, a second name).

*Proof.* By the [Proposition 2.17.7](/entry/exists-is-ell-smul/) of the last section, applied to each side, there are rank one Bessel functionals $\ell$, $\ell'$ on $D(w)$ and scalars $t$, $t'$ with
$$B(\sigma(g) v_0) = t\, \ell(\sigma(g) w), \qquad B'(\sigma(g) v_0) = t'\, \ell'(\sigma(g) w),$$
and $|t|^2 = c_0 d \dim W_p$, $|t'|^2 = c_0 d \dim W_q$. The amplitude is linear in $\Phi$ and conjugate linear in $\Phi'$, so
$$J_{c_0}(t\Phi, t'\Phi') = \frac{t\, \overline{t'}}{c_0}\, J_1(\Phi, \Phi') = \frac{t\, \overline{t'}}{c_0}\, O(\Phi, \Phi').$$
The squared Hilbert-Schmidt norm scales by $|t|^2 |t'|^2 / c_0^2 = d^2 \dim W_p \dim W_q$. Hence
$$\|J_{c_0}(\ldots)(\gamma)\|_{HS}^2 = \dim W_p \dim W_q\, \big\|d \cdot O(\ell \circ \sigma(\cdot) w, \ell' \circ \sigma(\cdot) w)(\gamma)\big\|_{HS}^2,$$
and the [Corollary 2.18.5](/entry/lintegral-hs-norm-sq-ell-le/) gives the bound $\dim W_p \dim W_q / d$. $\square$

**Remark 2.18.8 (Formalization).** The regular set is `Greg`, defined with the minors `Dmin` and the determinant `Gf`, and the disintegration is `IsDis` ([MatrixOfBesselTwoSidedAction.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/MatrixOfBesselTwoSidedAction.lean#L77)); the minors are not unfolded here. The Fatou theorem uses only $a > 2n^2$, which it derives from the assumption $a \ge 2n^5$ in `Std` ([LintegralHsNormSqDoubleCosetLeFatou.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/LintegralHsNormSqDoubleCosetLeFatou.lean#L136)). The Corollary needs only side data, but the last theorem asks for irreducible side data, because it uses the rank one factorization. In the last theorem the constant $c_0$ cancels, and the decay exponent $a$ is only passed on ([LintegralHilbertSchmidtNormSqBesselAmplitudeLe.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/LintegralHilbertSchmidtNormSqBesselAmplitudeLe.lean#L121)). The amplitude `ampJ` is defined with the variable $\gamma x$ in the first factor, and the orbital integral `OO` with $\gamma^{-1} x$ in the second factor; the proof identifies them by a change of variables.
