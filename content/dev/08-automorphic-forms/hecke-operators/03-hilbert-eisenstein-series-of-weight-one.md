---
title: Hilbert Eisenstein series of weight one
decls:
  - UpperTheory.HilbertEisensteinWeightOne.FourierExpansionEisenstein.local_expansion_holds
  - UpperTheory.HilbertEisensteinWeightOne.fourier_expansion_holds
  - UpperTheory.V.Published.hilbert_eisenstein_weight_one_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Hilbert Eisenstein series of weight one

This section constructs, for an odd character $\omega$ of finite order of a totally real field $F$, a holomorphic Hilbert modular form of parallel weight one whose $\mathfrak{m}$-th Fourier coefficient is the divisor sum $\sum_{\mathfrak{r} \mid \mathfrak{m}} \omega(\mathfrak{r})$. This is the weight one Eisenstein series of Hecke. It is the seed of a family of ordinary forms in [the seed of the second family](/entry/seed-iis-alt/). The form is built as a Tate integral of a theta series ([Eisenstein series](/learn/automorphic-forms/#eisenstein-series), [Tate's thesis](/learn/class-field-theory/#tates-thesis-and-hecke-l-functions)), and the main work is the Fourier expansion.

### Holomorphic forms of weight $k$ and level $\mathfrak{c}$

Let $F$ be totally real of degree $r$, with real places $v_1, \dots, v_r$, ring of integers $\mathcal{O}$ and different $\mathfrak{d}$. Let $\omega$ be a Hecke character of $F$, that is, a continuous character of $\mathbb{A}_F^\times / F^\times$ ([Hecke characters](/learn/class-field-theory/#hecke-characters)). For a finite place $w$ let $\mathfrak{p}_w$ be its prime and $\varpi_w$ a uniformizer.

**Definition 6.3.1 (Conductor exponent).** The *conductor exponent* $c_w$ of $\omega$ at $w$ is the least $n \ge 0$ such that $\omega_w(x) = 1$ for every unit $x \in \mathcal{O}_w^\times$ with $x \equiv 1 \bmod \mathfrak{p}_w^n$. The character is *ramified at $w$* if $c_w > 0$.

For $c \ge 0$ let $K_1(\mathfrak{p}_w^c)$ be the group of $g \in \mathrm{GL}_2(\mathcal{O}_w)$ whose bottom row is congruent to $(0, 1)$ modulo $\mathfrak{p}_w^c$. Write $E_{ij}$ for the matrix units in the Lie algebra of $\mathrm{GL}_2(F_v)$ at a real place $v$, acting on smooth functions by right derivatives.

**Definition 6.3.2 (Holomorphic form).** Let $k \ge 1$, let $c = (c_w)$ be exponents and $\omega$ a Hecke character. A smooth function $\varphi$ on $\mathrm{GL}_2(\mathbb{A}_F)$ is *holomorphic of weight $k$, level $c$ and central character $\omega$* if:

- $\varphi$ is an automorphic form ([automorphic forms](/learn/automorphic-forms/#automorphic-forms-on-adelic-groups));
- $\varphi$ is right invariant under $K_1(\mathfrak{p}_w^{c_w})$ for every finite $w$;
- $\varphi(zg) = \omega(z)\varphi(g)$ for every idele $z$, viewed as a scalar matrix;
- at each real place $v$, $(E_{12} - E_{21})\varphi = i k\, \varphi$, so $\varphi$ has weight $k$ under $\mathrm{SO}_2(\mathbb{R})$;
- at each real place $v$, $(E_{11} - E_{22})\varphi = i (E_{12} + E_{21})\varphi$, so $\varphi$ is killed by the lowering operator.

The last two conditions say that $\varphi(g_\infty \cdot)$ comes from a holomorphic function on $\mathfrak{H}^r$, which is the adelic form of a classical Hilbert modular form.

For $y \in (F \otimes \mathbb{R})^\times$ and $x \in F \otimes \mathbb{R}$ let $a(y, x) = \begin{pmatrix} y & x \\ 0 & 1 \end{pmatrix}$, and similarly for finite ideles. Write $|y_f|$ for the norm of a finite idele and $N(y) = \prod_v y_v$.

**Definition 6.3.3 (Fourier expansion).** Let $c_0$ be a function on finite ideles and $a$ a function on nonzero ideals of $\mathcal{O}$. We say that $\varphi$ *has Fourier expansion $(c_0, a)$ in weight $k$* if for all $x \in F \otimes \mathbb{R}$, all totally positive $y$ and all finite ideles $y_f$,
$$\begin{aligned} \frac{\varphi\bigl(a(y, x)_\infty \, a(y_f, 0)_f\bigr)}{(N(y)\,|y_f|)^{k/2}} - c_0(y_f) = \sum_{\xi \gg 0} \; & a\bigl([\xi y_f]\bigr) \\ & \cdot \exp\Bigl(2\pi i \sum_v \xi_v (x_v + i y_v)\Bigr). \end{aligned}$$
The sum runs over the totally positive $\xi \in F$. Here $a([t])$ means $a(\mathfrak{m})$ if the finite idele $t$ generates the fractional ideal $\mathfrak{m}\mathfrak{d}^{-1}$ with $\mathfrak{m} \ne 0$ integral, and $0$ if there is no such $\mathfrak{m}$.

For $\omega$ and its conductor exponents $c$, put $\chi(\mathfrak{p}_w) = \omega_w(\varpi_w)$ if $c_w = 0$ and $\chi(\mathfrak{p}_w) = 0$ if $c_w > 0$, and extend $\chi$ multiplicatively to integral ideals. This is the ideal character of $\omega$, set to $0$ on the ramified primes.

### The weight one Eisenstein series

**Theorem 6.3.4 (Hecke's weight one Eisenstein series).** Let $F$ be totally real and let $\omega$ be a Hecke character of finite order with $\omega_v(-1) = -1$ at every real place $v$. Let $c$ be its conductor exponents and assume that $\omega$ is ramified at some finite place. Then there are a function $\varphi$, holomorphic of weight $1$, level $c$ and central character $\omega$, and a constant $L \in \mathbb{C}$, such that $\varphi$ has Fourier expansion $(L, a)$ in weight $1$ with
$$a(\mathfrak{m}) = \sum_{\mathfrak{r} \mid \mathfrak{m}} \chi(\mathfrak{r}).$$

Lean: `UpperTheory.V.Published.hilbert_eisenstein_weight_one_holds`.

Since $a(\mathcal{O}) = 1$, the form $\varphi$ is not zero. The constant term $L$ is a constant: it does not depend on $y_f$.

The form is the Eisenstein series of a Schwartz function on $\mathbb{A}_F^2$. Let $\Phi = \Phi_\infty \otimes \Phi_f$ with
$$\Phi_\infty(\xi_0, \xi_1) = \prod_v (\xi_{0,v} + i\xi_{1,v})\, e^{-\pi(\xi_{0,v}^2 + \xi_{1,v}^2)},$$
and $\Phi_f$ the characteristic function of the set of $(\xi_0, \xi_1)$ with $\xi_0 \in \mathfrak{p}_w^{c_w}$ and $\xi_1 \in 1 + \mathfrak{p}_w^{c_w}$ at every finite $w$ (read $1 + \mathfrak{p}_w^0$ as $\mathcal{O}_w$). The archimedean factor has weight one under $\mathrm{SO}_2(\mathbb{R})$, and the finite factor is invariant under $K_1(\mathfrak{p}_w^{c_w})$. Let $\Theta_\Phi(h) = \sum_{\xi \in F^2 \setminus 0} \Phi(\xi h)$ and
$$E(g) = |\det g|^{1/2} \int_{\mathbb{A}_F^\times / F^\times} \Theta_\Phi(t g)\, \omega(t)^{-1}\, |t|\, d^\times t.$$

**Proposition 6.3.5 (Fourier expansion of the Eisenstein series).** Let $\omega$ and $c$ be as in the theorem. Assume the Poisson summation formula $\Theta_\Phi(h) = C\, |\det h|^{-1}\, \Theta_{\hat\Phi}({}^t h^{-1})$ for some constant $C$ and an explicit Schwartz function $\hat\Phi$ of the same shape as $\Phi$, with both series absolutely convergent, and assume that the integrand of $E(g)$ is integrable for every $g$. Then there are a constant $C_0 \ne 0$ and $L \in \mathbb{C}$ such that $E$ has Fourier expansion $(L, C_0 a)$ in weight $1$, with $a$ the divisor sum above.

Lean: `UpperTheory.HilbertEisensteinWeightOne.fourier_expansion_holds`.

*Proof.* Insert $g = a(y, x)_\infty a(y_f, 0)_f$ and split the sum over $\xi = (\xi_0, \xi_1) \in F^2 \setminus 0$ into the terms with $\xi_1 = 0$ and those with $\xi_1 \ne 0$. Poisson summation in $\xi_0$ turns the second part into a sum over $\eta \in F$ of the partial Fourier transform of $\Phi$; this gives a term with $\eta = 0$ and a sum over $\eta \ne 0$ of $e(\eta x)$ times a coefficient. The terms with $\xi_1 = 0$ depend only on $y$ and $y_f$ through the norm, and give the constant $L$. The term with $\eta = 0$ integrates to $0$ against $\omega^{-1}$ (this is where $\omega$ ramified is used: the integral of a ramified character over the units vanishes). The remaining series converges absolutely, so we may exchange the sum and the integral and unfold: the sum over $\xi_1 \in F^\times$ and the integral over $\mathbb{A}^\times / F^\times$ combine to one integral over $\mathbb{A}^\times$. That integral factors into local integrals, computed in the lemma below. $\square$

**Lemma 6.3.6 (Local integrals).** Let $\omega$ and $c$ be as in the theorem. Assume that $\omega$ is ramified at only finitely many places, and that the adelic Fourier transform of each slice of $\Phi$ (fix one coordinate, transform in the other) is $\kappa \ne 0$ times an explicit product kernel $k$. Then the idele integral of $k$ against $\omega^{-1}(t)|t|$ equals
$$C_0 \cdot [\xi \gg 0] \cdot a([\xi y_f]) \cdot e^{-2\pi \sum_v \xi_v y_v}, \qquad C_0 = \kappa \cdot 2^{r} \cdot C_f,$$
where $[\xi \gg 0]$ is $1$ if $\xi$ is totally positive and $0$ otherwise, and $C_f \ne 0$ is a product of local constants at the ramified places.

Lean: `UpperTheory.HilbertEisensteinWeightOne.FourierExpansionEisenstein.local_expansion_holds`.

*Proof.* The integral is a product over all places. At a real place $v$ the integral of $t (\xi t + i y)\, e^{-\pi(\dots)}$ against the sign character, over $t \in \mathbb{R}^\times$, is $2 e^{-2\pi \xi y}$ if $\xi > 0$ and $0$ if $\xi < 0$; the oddness $\omega_v(-1) = -1$ makes the two halves add for the right sign and cancel for the other. This gives $2^r$ and the condition $\xi \gg 0$. At an unramified finite $w$, the integral over $t$ with $t \xi y_f \in \mathfrak{d}_w^{-1}$ is the finite geometric sum $\sum_{j=0}^{m} \omega_w(\varpi_w)^j$, where $m$ is the order of $\xi y_f \mathfrak{d}$ at $w$. The product of these sums is the divisor sum $a(\mathfrak{m})$. At a ramified $w$ the condition $\xi_1 \in 1 + \mathfrak{p}_w^{c_w}$ picks a Gauss sum, a nonzero constant times the indicator that $\xi y_f \mathfrak{d}$ is a unit at $w$; this is consistent with $\chi(\mathfrak{p}_w) = 0$. The product of these constants is $C_f$. $\square$

*Proof of the theorem.* Let $\varphi = C_0^{-1} E$. The proposition gives the Fourier expansion $(C_0^{-1}L, a)$. It remains to check that $E$ is holomorphic of weight $1$, level $c$ and central character $\omega$. Left invariance under $\mathrm{GL}_2(F)$ holds since $\Theta_\Phi$ is a sum over $F^2 \setminus 0$. The integral converges and is smooth of moderate growth. Right invariance under $K_1(\mathfrak{p}_w^{c_w})$ and the central character come from the invariance of $\Phi_f$ and the change of variable $t \mapsto tz$. The weight and the lowering condition come from $\Phi_\infty$, whose factors $(\xi_0 + i\xi_1)e^{-\pi|\xi|^2}$ are of weight $1$ and killed by the lowering operator. Finally $E$ is finite under $K_\infty$ and under the center of the enveloping algebra. Scaling by $C_0^{-1}$ keeps all of these. $\square$

**Remark 6.3.7 (Formalization).** The theorem is assembled from fourteen inputs, one for each property of $E$ (Poisson summation, convergence, growth, smoothness, left invariance, level, openness, central character, $K$-finiteness, weight, lowering, $\mathcal{Z}$-finiteness, the expansion and the scaling). The proposition takes three inputs but does not use the input on smoothness ([FourierExpansionHolds.lean](lean:PositivityTheory/AutomorphicForms/PublishedInputs/HilbertEisenstein/FourierExpansionHolds.lean#L258)). The local lemma takes as hypotheses the finiteness of the ramified set (a fact, which could be proved) and the formula for the Fourier transform of the slice; the kernel $k$ is defined there and we did not unfold it ([LocalExpansionHolds.lean](lean:PositivityTheory/AutomorphicForms/PublishedInputs/HilbertEisenstein/LocalExpansionHolds.lean#L282)); the local computations at the real and finite places are inputs whose proofs we did not unfold. The weight and the lowering conditions are written with the four matrix units, not with the operators $H$, $X_\pm$.
