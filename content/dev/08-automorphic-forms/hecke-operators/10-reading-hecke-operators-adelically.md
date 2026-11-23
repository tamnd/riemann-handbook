---
title: Reading Hecke operators on the adelic group
decls:
  - GlobalTheory.HeckeReadProof.heckeReadTie
  - GlobalTheory.T.heckeReading_kernels_match_cosets_through_frame
  - GlobalTheory.HeckeTerm.heckeTerm
  - GlobalTheory.T.heckeKernel_complex_point_matches_cosets
  - GlobalTheory.HeckeTermIdent.heckeKernelCoset
  - GlobalTheory.T.heckeTerm_generator_constant_via_frame
  - GlobalTheory.HeckeGenConst.generator_constant
  - GlobalTheory.HeckeGeoRead.theta_trace_read
  - GlobalTheory.T.heckePointThetaTrace_eq_phasedTranslateSum
  - GlobalTheory.HeckeGeoRead.theta_trace_eq_phased_sum
  - GlobalTheory.HeckeGeomSum.theta_prod_eq_phased_sum
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Reading Hecke operators on the adelic group

The previous section defined Hecke operators on algebraic sections as sums over isogenies. This section compares them with the adelic Hecke operators, which are sums over coset representatives of a double coset. The comparison passes through the complex uniformization and through theta functions: a section is read as a function $\varphi_f$ on the adelic unitary group, and the theta line of each abelian variety is pinned to a theta kernel of the Weil representation. The result, the reading theorem, is the third part of [the Hecke integrality, transform and reading facts](/entry/hecke-int-transform-read-tie/). The classical case is the identity between the Hecke operator on modular forms and the convolution operator of a double coset on $\mathrm{GL}_2(\mathbb{A})$ ([automorphic forms on adelic groups](/learn/automorphic-forms/#automorphic-forms-on-adelic-groups)).

### The dictionary

Fix a theta datum with chain index $i$, the base embedding $\sigma_0$ of the coefficient field, and an identification of the Hermitian space of the moduli problem at $\sigma_0$ with the weight space $W_i$. Let $G = \mathrm{U}(W_i)$ and $V = V_i$ the companion space of the dual pair $(\mathrm{U}(V), \mathrm{U}(W))$, with the Weil representation $\omega$ on Schwartz functions of $V \otimes W$ and the vacuum vector $\phi_0$ of the self-dual lattices ([the Schrödinger model](/learn/theta/#the-schrödinger-model)). The complex uniformization gives, for each $h \in G(\mathbb{A})$, a component $k(h)$ and a frame $x(h)$ on it, hence a framed point $y_h$ over $\mathbb{C}$ whenever $x(h)$ lies in the domain of the component. For a section $f$ of weight $\kappa_i$, put
$$\varphi_f(h) = \lambda\, c(h)\, \mu(h)\, f(y_h),$$
where $c(h)$ is the scalar of the component, $\mu(h)$ is the scalar of the multiplier, and $\lambda$ is a fixed factor.

**Definition 6.10.1 (Frame pin).** The *frame pin* at $i$ holds if there are a phase $\varepsilon$ with $|\varepsilon| = 1$ and an orthonormal lattice basis $b$ of $V$ such that the following holds. For every $h$ and every rational $\gamma \in G(F)$ for which $\gamma h$ is the frame at $h$, and every unit chart $Y$ of the abelian variety at $y_h$ with period map $\mathrm{per}$, Hermitian form $H_Y$ and theta generator $\theta_Y$: for every $X \in \mathrm{Mat}(W, V)(E)$, with $z_a = \mathrm{per}(X b_a)$,
$$e^{\frac{\pi}{2} \sum_a H_Y(z_a, z_a)}\ \Theta(\gamma h)(X) = \varepsilon\, c(h)\mu(h) \prod_a \theta_Y(z_a),$$
where $\Theta(g)(X) = \omega(1, g)\phi_0(X)$ is the theta kernel at the real point of $X$.

So the frame pin says that the adelic theta kernel and the analytic theta function of the abelian variety agree up to a phase and the scalars $c(h)\mu(h)$, once both are normalized by the Gaussian factor ([theta kernels](/learn/theta/#theta-kernels)).

**Definition 6.10.2 (Hecke data at a split prime).** *Hecke data* at a prime $\mathfrak{P}$ of $E$ are $(p_0, k, \alpha, R_c)$ such that $\mathfrak{P}$ is split off the bad set, $p_0$ is a prime in $\mathfrak{P}$ not dividing the level, $k \le r$, $\alpha \in G(\mathbb{A})$ is a Hecke element at $\mathfrak{P}$ of degree $k$, and $R_c$ is a finite set of representatives of $K \alpha K / K$ for the level group $K$. Write $\mu_i(\mathfrak{P})$ for the value at $\mathfrak{P}$ of the unramified character $\mu_{0,i}$ of the datum.

In all results below we assume the four point laws, the split linear model and the fixed vacuum (the vacuum is fixed by the integral points at the split places), the level, group, family, model and theta conditions on the datum, the tie between the core and the datum, $\sigma = \sigma_0$, and the frame pin at $i$.

### Theta functions at Hecke points

Let $(\mathfrak{P}, p_0, k, \alpha, R_c)$ be Hecke data, $h \in G(\mathbb{A})$ with $y_h$ defined, $a \in R_c$, $C$ a Hecke kernel at $y_h$ with Hecke point $z$, and suppose $z$ is obtained from $y_{ha}$ by a torus change $t$ whose entries are $1$ except the theta entry $t_0$. Let $Y'$ be a unit chart at $y_{ha}$, with period vectors $z'_a$ built from $X$ and $b$ as above. Let $e$ be the idempotent of the adeles at $\mathfrak{P}$, and $\Delta$ a set of half representatives for the action of $a$ on the lattice of $V \otimes W$ at $\mathfrak{P}$; for $x \in \Delta$, let $\ell(x) \in \mathrm{Mat}(W, V)(E)$ be its rational lift. Write $\langle\ ,\ \rangle$ for the symplectic form on $V \otimes W$ and $\psi$ for the additive character.

**Lemma 6.10.3 (Theta product as a phased sum).** For a rational $\gamma'$ with $\gamma'(ha)$ the frame at $ha$,
$$t_0^{\dim V}\, \varepsilon\, c(h)\mu(h) \prod_a e^{-\frac{\pi}{2} H_{Y'}(z'_a, z'_a)}\, \theta_{Y'}(z'_a) = \sum_{x \in \Delta} \psi\bigl(-\langle \ell(x), X - \ell(x) \rangle\bigr)\ \Theta(\gamma' h)(X - \ell(x)).$$

Lean: `GlobalTheory.HeckeGeoRead.theta_trace_eq_phased_sum` (also `GlobalTheory.T.heckePointThetaTrace_eq_phasedTranslateSum`, a second name, and `GlobalTheory.HeckeGeomSum.theta_prod_eq_phased_sum`, the product identity it uses).

*Proof.* The Hecke isogeny with kernel $C$ carries the theta generator by the trace. On the uniformization, the trace of a theta function along an isogeny of degree $(\mathrm{N}\mathfrak{P})^{k}$ is the sum of its translates by the $(\mathrm{N}\mathfrak{P})^{k}$ period vectors of the kernel, each multiplied by the factor of automorphy. With the Gaussian normalization these factors become phases. Each translate is matched with an element $x \in \Delta$, and the translate of the theta kernel is the Heisenberg translate of the vacuum by $x$. In the Schrödinger model, the Heisenberg element $\ell(x)$ acts by a shift and the phase $\psi(-\langle \ell(x), X - \ell(x)\rangle)$. A change of frame between $h$ and $ha$ moves the frame pin from $y_h$ to the translated points, and the product identity then gives the sum. $\square$

**Lemma 6.10.4 (Theta trace read).** In the same situation,
$$t_0^{\dim V}\, \varepsilon\, c(h)\mu(h) \prod_a e^{-\frac{\pi}{2} H_{Y'}(z'_a, z'_a)}\, \theta_{Y'}(z'_a) = \sum_{x \in \Delta} \omega(1, \gamma' h)\bigl(\rho(x)\phi_0\bigr)(X),$$
where $\rho$ is the Heisenberg action.

Lean: `GlobalTheory.HeckeGeoRead.theta_trace_read`.

*Proof.* The elements of $\Delta$ have trivial archimedean part, since $e$ is a split idempotent. Each $x$ has a rational lift $\ell(x)$ and a finite part $w$ that fixes the vacuum. The Heisenberg translate of $\phi_0$ by $x$, evaluated at $X$, is then the phased translate of the lemma above. $\square$

**Lemma 6.10.5 (Generator constant).** For $a \in R_c$, a Hecke kernel $C$ at $y_h$, a Hecke point $z$, and a torus change $t$ from $y_{ha}$ to $z$ with entries $1$ off the theta entry,
$$t_0^{\,n}\ c(h)\mu(h)\ \sigma_0\bigl((\mathrm{N}\mathfrak{P})^{-\lfloor k\, n_V/2 \rfloor}\bigr) = \mu_i(\mathfrak{P})^{-k}\ c(ha)\mu(ha),$$
where $n = n(\kappa_i)$ is the theta weight and $n_V = \dim V$.

Lean: `GlobalTheory.HeckeGenConst.generator_constant` (also `GlobalTheory.T.heckeTerm_generator_constant_via_frame`, a second name).

*Proof.* The Hecke element $a$ acts on the vacuum by $\omega(1, a)\phi_0 = \mu_i(\mathfrak{P})^{k}(\mathrm{N}\mathfrak{P})^{-\lfloor kn_V/2 \rfloor}$ times the sum of the Heisenberg translates of $\phi_0$ over $\Delta$, a set of $(\mathrm{N}\mathfrak{P})^{kn_V}$ elements with trivial archimedean part. This is the computation of the Weil representation on the vacuum at a split prime. Evaluate the frame pin at $ha$ on one side and the theta trace read on the other, at a matrix $X$ for which the theta product does not vanish. The Gaussian factors cancel, the phases cancel, and the product of the theta values cancels. What remains is the stated identity of scalars, with the weight of the theta entry fixed by the tie. $\square$

### Kernels and cosets

**Lemma 6.10.6 (Kernels match cosets).** For Hecke data and $h$ with $y_h$ defined, there is a bijection $e$ from the Hecke kernels at $y_h$ to $R_c$ such that, for each kernel $C$ and each Hecke point $z$ of $C$, the framed point $y_{h e(C)}$ is defined and $z$ is obtained from it by a torus change $t$ whose entries are $1$ off the theta entry.

Lean: `GlobalTheory.HeckeTermIdent.heckeKernelCoset` (also `GlobalTheory.T.heckeKernel_complex_point_matches_cosets`, a second name).

*Proof.* Since $\mathfrak{P} \ne \bar{\mathfrak{P}}$, the prime is a Hecke prime. On the uniformization, a Hecke kernel at $y_h$ is the image of a lattice $L'$ with $L \subset L' $ and $L'/L$ of the type of $\mathfrak{P}$ and degree $k$. These lattices correspond to the cosets $h a K$ with $a \in R_c$. For each $a$, the framed point of $ha$ and the Hecke point of the matching kernel have the same lattice and the same tangent bases, so they differ only in the theta generator, which is the torus change $t_0$. $\square$

**Theorem 6.10.7 (Term identity).** For Hecke data and $h$ with $y_h$ defined, there is a bijection $e$ from the Hecke kernels at $y_h$ to $R_c$ such that each kernel $C$ has a Hecke point, and for each Hecke point $z$ of $C$ and each section $f$ of weight $\kappa_i$,
$$\lambda\, c(h)\mu(h)\, (\mathrm{N}\mathfrak{P})^{-\lfloor kn_V/2 \rfloor} f(z) = \mu_i(\mathfrak{P})^{-k}\, \varphi_f\bigl(h\, e(C)\bigr).$$

Lean: `GlobalTheory.HeckeTerm.heckeTerm` (also `GlobalTheory.T.heckeReading_kernels_match_cosets_through_frame`, a second name).

*Proof.* Take $e$ from the lemma on kernels and cosets. A Hecke point exists by the total law. For $z$ and $t$ as in that lemma, the weight law gives $f(z) = t_0^{\,n} f(y_{he(C)})$, since the other entries of $t$ are $1$. Multiply the generator constant by $\lambda f(y_{he(C)})$. $\square$

**Theorem 6.10.8 (Hecke reading).** Assume the split linear model and the fixed vacuum for all data, and the frame pin at $i$. For Hecke data $(\mathfrak{P}, p_0, k, \alpha, R_c)$, every $c_q$, and sections $f, g$ of weight $\kappa_i$ with $g = c_q (\mathrm{N}\mathfrak{P})^{-\lfloor kn_V/2 \rfloor} T_{\mathfrak{P}, k} f$ at all geometric points,
$$\varphi_g(h) = \sigma_0(c_q)\, \mu_i(\mathfrak{P})^{-k} \sum_{a \in R_c} \varphi_f(ha) \qquad \text{for all } h \in G(\mathbb{A}).$$

Lean: `GlobalTheory.HeckeReadProof.heckeReadTie`.

*Proof.* Fix $h$; the framed point $y_h$ is defined for every $h$. By definition $\varphi_g(h) = \lambda c(h)\mu(h) g(y_h)$, and $g(y_h)$ is $\sigma_0(c_q)(\mathrm{N}\mathfrak{P})^{-\lfloor kn_V/2 \rfloor}$ times the sum over the Hecke kernels of the terms of $f$. The term identity turns each term into $\mu_i(\mathfrak{P})^{-k}\varphi_f(h e(C))$. Reindex the sum by the bijection $e$. $\square$

**Remark 6.10.9 (Formalization).** The reading theorem is at [HeckeReadTie.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/HeckeReadTie.lean#L34); its hypothesis that $g$ has weight $\kappa_i$ (line 37) is never used. The point laws are hypotheses of the lemmas, and the reading theorem supplies the proved laws. The exponent $kn_V/2$ is a division of natural numbers ([LiftLaSpec.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/LiftLaSpec.lean#L57)), so it rounds down when $kn_V$ is odd. The term identity lives in a module named after its second name ([HeckeReadingKernelsMatchCosetsThroughFrame.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/HeckeReadingKernelsMatchCosetsThroughFrame.lean#L41)), and the file of that second name imports Mathlib twice ([HeckeReadingKernelsMatchCosetsThroughFrameStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/HeckeReadingKernelsMatchCosetsThroughFrameStatement.lean#L1), lines 1 and 3). The product identity is in a module named after a different theorem, the admissibility of split Hecke primes ([IsAdmissibleSplitHeckePrimeOfConjNe.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/IsAdmissibleSplitHeckePrimeOfConjNe.lean#L319)), which is at line 243. The computation of the Weil representation on the vacuum is in a module named after an unrelated square root identity ([SqrtDivMulEqSqrtMul.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/SqrtDivMulEqSqrtMul.lean#L359)). This computation, the frame change and the bijection of kernels with cosets were used as inputs and not unfolded; the proofs above follow their statements. The lemmas carry the full list of hypotheses of the datum, most of which are only passed down.
