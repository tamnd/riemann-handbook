---
title: Galois conjugation of lattice values
decls:
  - GlobalTheory.LatConjEll.latConj
  - GlobalTheory.T.latticeValueConjugation_of_ellipticCM_theorems
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Galois conjugation of lattice values

This section computes how an automorphism $g$ of $\mathbb{C}$ acts on the value at $0$ of a CM lattice sum, after division by a power of a period. The answer is a reciprocity law of Shimura's type. The conjugate value is the value for a second lattice, which is the first one divided by an idele $t$ that describes $g$ on torsion points, with the weights permuted as $g$ permutes the CM type, and with the period changed. The proof expresses the value through CM values of $G_2^*$, of a Weierstrass function and of holomorphic Hilbert modular jets, and moves each factor with $g$. The law is one of the five inputs of the [toric denominator bounds](/entry/join-out-of-five/).

We keep the notation of the two previous sections. The published inputs are those stated before the [Theorem 1.3.7](/entry/cm-lattice-divided-power-jet-integrality-of-elliptic-cm/) on integrality of CM jets.

### Torsion transport

Let $K$ be a number field of degree $2$, $\iota : K \to \mathbb{C}$ an embedding, $d > 0$ an integer and $\delta \in K$ with $\delta^2 = -d$. So $K$ is imaginary quadratic. Let $\mathbb{A}_{K,f}$ be its ring of finite adeles. For $t \in \mathbb{A}_{K,f}^\times$ put $\|t\| = \prod_v N v^{-\operatorname{ord}_v(t_v)}$, the product over the finite primes of $K$.

For a lattice $\Lambda \subset \mathbb{C}$ let $g_2(\Lambda)$, $g_3(\Lambda)$, $\wp_\Lambda$ and $\wp'_\Lambda$ be its invariants and its Weierstrass functions, and let $\Delta(\Lambda) = g_2^3 - 27 g_3^2$ ([lattices and the Weierstrass function](/learn/elliptic-curves/#lattices-and-the-weierstrass-function)).

**Definition 1.4.1 (torsion transport).** Let $g$ be a ring automorphism of $\mathbb{C}$, $t \in \mathbb{A}_{K,f}^\times$, $\Lambda_0, \Lambda_1 \subset \mathbb{C}$ lattices and $\Omega_0, \Omega_1 \in \mathbb{C}$. We say that $(g, t)$ *transports* $(\Lambda_0, \Omega_0)$ to $(\Lambda_1, \Omega_1)$ if:

1. $\Omega_0 \neq 0$, $\Omega_1 \neq 0$, and $g(\iota x) = \iota x$ for all $x \in K$;
2. $\Lambda_0 = \iota(\mathcal{O}_K)$, and $\Lambda_1 = \iota(\mathfrak{a})$, where $\mathfrak{a}$ is the fractional ideal of the $x \in K$ with $t x$ integral at every prime;
3. $g(g_2(\Lambda_0)/\Omega_0^4) = g_2(\Lambda_1)/\Omega_1^4$ and $g(g_3(\Lambda_0)/\Omega_0^6) = g_3(\Lambda_1)/\Omega_1^6$;
4. for all $x, x' \in K$ with $\iota x \notin \Lambda_0$ and $t x' - x$ integral at every prime,
$$g\Bigl(\frac{\wp_{\Lambda_0}(\iota x)}{\Omega_0^2}\Bigr) = \frac{\wp_{\Lambda_1}(\iota x')}{\Omega_1^2}, \qquad g\Bigl(\frac{\wp'_{\Lambda_0}(\iota x)}{\Omega_0^3}\Bigr) = \frac{\wp'_{\Lambda_1}(\iota x')}{\Omega_1^3}.$$

So $g$ moves the curve $\mathbb{C}/\Lambda_0$ to $\mathbb{C}/\Lambda_1$, with the differential scaled by $\Omega_0$ and $\Omega_1$, and it moves the torsion point $\iota x$ to $\iota x'$. The main theorem of complex multiplication gives such data when $g$ acts on $K^{ab}$ as the Artin symbol of an idele with finite part $t$ ([the main theorem of complex multiplication](/learn/theta-functions-cm/#the-main-theorem-of-complex-multiplication)). Note that $\|t\| = N\mathfrak{a}$.

**Definition 1.4.2 (CM datum).** Let $E$ be a CM field containing $K$, with real subfield $F$ of degree $g_F$, and $\varphi = (\varphi_i)_{i \in I}$ a family of embeddings $E \to \mathbb{C}$. A *CM datum* for $\iota$ is $(\varphi, s, \mathfrak{f}, Q)$ such that $E/F$ is unramified at all finite primes, $\varphi$ is a CM type, $\varphi_i|_K = \iota$ for all $i$, $s \geq 1$, $\mathfrak{f}$ is an admissible conductor and $Q$ is admissible for $\mathfrak{f}$. Put $\mathfrak{c} = \mathfrak{c}(\mathfrak{f}, Q)$.

**Definition 1.4.3 (conjugate weights).** Let $\kappa, \kappa' \in \mathbb{N}^I$. They are *conjugate under $g$* if $\kappa'_j = \kappa_i$ whenever $g \circ \varphi_i = \varphi_j$.

**Definition 1.4.4 (normalized coordinate).** For $k = 2s$ and $\kappa \in \mathbb{N}^I$ put $|\kappa| = \sum_i \kappa_i$, $w(\kappa) = 2s|I| + 2|\kappa|$ and
$$C(\kappa) = d_F^{(2s-1)/2} \prod_{i \in I} \Gamma(2s + \kappa_i) \Bigl(\frac{2\pi}{\sqrt d}\Bigr)^{|\kappa|},$$
where $d_F = |\operatorname{disc} F|$. For $\Omega, T \in \mathbb{C}$ the *normalized coordinate* is $\operatorname{co}_\kappa(\Omega, T) = C(\kappa)\, T/\Omega^{w(\kappa)}$.

For $t \in \mathbb{A}_{K,f}^\times$ we write $t$ also for its image in $\mathbb{A}_{E,f}^\times$.

### The theorem

**Theorem 1.4.5 (Galois conjugation of CM lattice values).** Assume the theorems of Siegel-Klingen and Deligne-Ribet, the functional equation of partial zeta functions, the Hilbert class field theorem and the main theorem of complex multiplication. Let $K$, $\iota$, $d$, $\delta$ be as above. Let $g$ be a ring automorphism of $\mathbb{C}$, $t \in \mathbb{A}_{K,f}^\times$, and $(\Lambda_0, \Omega_0)$, $(\Lambda_1, \Omega_1)$ such that $\Omega_0^{12} = \Delta(\Lambda_0)$ and $(g, t)$ transports $(\Lambda_0, \Omega_0)$ to $(\Lambda_1, \Omega_1)$. Let $(\varphi, s, \mathfrak{f}, Q)$ be a CM datum for $\iota$ on a CM field $E \supset K$, and let $\kappa, \kappa'$ be conjugate under $g$. Let $y \in \mathbb{A}_{E,f}^\times$, let $S$ be a lattice sum of type $(2s, \kappa)$ for $L(\mathfrak{c}, y)$, and let $S'$ be a lattice sum of type $(2s, \kappa')$ for $L(\mathfrak{c}, y t^{-1})$. Then
$$g\bigl(\operatorname{co}_\kappa(\Omega_0, S(0))\bigr) = \operatorname{co}_\kappa\bigl(\Omega_1,\ \|t\|^{-|\kappa|}\, S'(0)\bigr).$$

Lean: `GlobalTheory.T.latticeValueConjugation_of_ellipticCM_theorems` (also `GlobalTheory.LatConjEll.latConj`, a second name).

The right side uses $\kappa$, not $\kappa'$. This is no loss: we show below that $C(\kappa) = C(\kappa')$ and $|\kappa| = |\kappa'|$.

We need the holomorphic jets. Let $L' \subset F^2$ be an $\mathcal{O}_F$-lattice of level $N$, $\mu \in \mathbb{N}^{I}$, and $h : \mathbb{H} \to \mathbb{C}$. Let $H_\mu(L', h)(\tau)$ be the jet of order $\mu$ of weight $2s$ for $L'$ at $\tau$ (as in the [previous section](/entry/cm-lattice-divided-power-jet-integrality-of-elliptic-cm/)), formed with $(2\pi i)^2 h(\tau)$ and $-2\pi i$ in place of $1$ and $\bar\tau - \tau$, and divided by $(2\pi i)^{2s g_F + 2|\mu|}$. For a nonzero $v \in (\mathbb{Z}/N)^2$ let $\wp_N(v, \tau)$ be the Weierstrass function of $\mathbb{Z}\tau + \mathbb{Z}$ at the torsion point $v$, and let $h_v$ be the holomorphic function with $(\pi/\operatorname{Im}\tau)/(2\pi i)^2 - h_v(\tau) = -(G_2^*(\tau)/(2\pi i)^2 + \wp_N(v, \tau))$. Put $r(n, m) = (-1)^{n-m}\binom{n}{m}(2s + m)(2s + m + 1)\cdots(2s + n - 1)$.

*Proof.* *Inputs.* By the Siegel-Klingen theorem there is $z : \operatorname{Cl}(F) \to \mathbb{Q}$ such that each $z(C)$ is the value at $1 - 2s$ of a partial zeta function of $C$. By the functional equation, the [Theorem 1.1.10](/entry/hecke-weight-two-of-fe/) on Hecke's series holds. So the [derivative formula and the homothety rule](/entry/cm-lattice-deriv-class-invariance-of-hecke/) hold in weight $2s$, and the Hilbert Eisenstein series of weight $2s$ exist with their $q$-expansions.

*Bases.* There are $\theta_0 \in K$ and $\tau_0 \in \mathbb{H}$ with $\iota\theta_0 = \tau_0$ and $\mathcal{O}_K = \mathbb{Z}\theta_0 + \mathbb{Z}$. Let $\mathfrak{a}$ be the ideal of the transport; then $\mathfrak{a} \neq 0$ since $\Lambda_1$ is a lattice. There are a rational $c_1 > 0$, $\theta_1 \in K$ and $\tau_1 \in \mathbb{H}$ with $\iota\theta_1 = \tau_1$ and $\mathfrak{a} = c_1(\mathbb{Z}\theta_1 + \mathbb{Z})$. Comparing covolumes gives $c_1^2 \operatorname{Im}\tau_1 = N\mathfrak{a}\,\operatorname{Im}\tau_0$, and $N\mathfrak{a} = \|t\|$. Since $\delta \in \mathcal{O}_K$, the number $q = 2\operatorname{Im}\tau_0/\sqrt d$ is rational. So
$$\frac{2\operatorname{Im}\tau_1}{\sqrt d}\, c_1^2 = \|t\|\, q.$$

*Level.* There are integers $n \geq 1$ and $N$ with $2 \mid N$, and an $\mathcal{O}_F$-lattice $L_0 \subset F^2$ of level $N$, such that $x \in L_0$ if and only if $n y' = x_0\theta_0 + x_1$ for some $y' \in L(\mathfrak{c}, y)$. Here $F$ is embedded in $F^2$ through the real places, and $\theta_0$ is viewed in $E$.

*Transport of modular values.* Put $\omega_0 = \Omega_0/(2\pi i)$ and $\omega_1 = \Omega_1 c_1/(2\pi i)$. The transport and the bases give
$$g\Bigl(\frac{E_4(\tau_0)}{\omega_0^4}\Bigr) = \frac{E_4(\tau_1)}{\omega_1^4}, \quad g\Bigl(\frac{E_6(\tau_0)}{\omega_0^6}\Bigr) = \frac{E_6(\tau_1)}{\omega_1^6}, \quad g\Bigl(\frac{G_2^*(\tau_0)}{(2\pi i)^2\omega_0^2}\Bigr) = \frac{G_2^*(\tau_1)}{(2\pi i)^2\omega_1^2}.$$
There is $A \in \operatorname{GL}_2(\mathbb{Z}/N)$ with $g(\wp_N(v, \tau_0)/\omega_0^2) = \wp_N(vA, \tau_1)/\omega_1^2$ for all $v$, and the same for $\wp'_N$ with $\omega^3$.

*The second lattice.* Let $L_0^A$ be the twist of $L_0$ by $A$. Then $x \in L_0^A$ if and only if $n y' = x_0\theta_1 + x_1$ for some $y' \in c_1^{-1} L(\mathfrak{c}, y t^{-1})$. By the homothety rule, $c_1^{-1}L(\mathfrak{c}, yt^{-1})$ has a lattice sum of type $(2s, \kappa')$ whose value at $0$ is $\lambda_\infty(c_1^{-1})^{-1} S'(0) = c_1^{2s g_F} S'(0)$.

*The CM type.* Since $g$ fixes $\iota(K)$ and $\iota(K) \not\subset \mathbb{R}$, there is a permutation $\pi$ of $I$ with $g \circ \varphi_i = \varphi_{\pi(i)}$. So $\kappa'_{\pi(i)} = \kappa_i$, $|\kappa'| = |\kappa|$ and $C(\kappa') = C(\kappa)$. Under the bijection of $I$ with the real places of $F$, $\pi$ gives the permutation $\sigma$ by which $g$ acts on the real conjugates of $F$.

*Value formula.* Let $\Lambda \subset E$, $\theta \in E$ with $\varphi_i(\theta) = \tau$ for all $i$, and $L$ a lattice of level $N$ with $x \in L$ if and only if $n y' = x_0\theta + x_1$ for some $y' \in \Lambda$. Let $S_\Lambda$ be a lattice sum of type $(2s, \kappa)$ for $\Lambda$, and let $c \neq 0$ and $\omega = \Omega c/(2\pi i)$. Write $X = -(G_2^*(\tau)/(2\pi i)^2 + \wp_N(v, \tau))$. The derivative formula, together with the expansion of derivatives of Hilbert Eisenstein series in holomorphic jets, gives
$$\begin{aligned} \operatorname{co}_\kappa(\Omega, S_\Lambda(0)) &= (-1)^{|\kappa|}\Bigl(\frac{2\operatorname{Im}\tau}{\sqrt d}\Bigr)^{|\kappa|} n^{2s g_F}\, c^{w(\kappa)} \\ &\quad \cdot \frac{1}{\omega^{w(\kappa)}}\sum_{\mu \leq \kappa} \prod_i r(\kappa_i, \mu_i)\, X^{|\kappa - \mu|}\, H_\mu(L, h_v)(\tau). \end{aligned}$$
We use it twice with $v = (1, 0)$: once for $L(\mathfrak{c}, y)$, $L_0$, $\tau_0$, $c = 1$, and once for $c_1^{-1}L(\mathfrak{c}, yt^{-1})$, $L_0^A$, $\tau_1$, $c = c_1$, with $\kappa'$ and $vA$.

*Term by term.* By the transport of $G_2^*$ and $\wp_N$, $g(X_0/\omega_0^2) = X_1/\omega_1^2$. For the jets, $g$ acts on $N$-th roots of unity as $\zeta \mapsto \zeta^a$ for a unit $a$ of $\mathbb{Z}/N$. The $q$-expansion of $H_\mu(L_0^\beta, h_{v\beta})$ for $\beta \in \operatorname{GL}_2(\mathbb{Z}/N)$ has its coefficients moved by $g$ to those of the corresponding function for $\beta\operatorname{diag}(1, a)$, with $\mu$ moved by $\sigma$. Here the rationality of the zeta values $z$ is used for the constant terms. The family over $\operatorname{GL}_2(\mathbb{Z}/N)$ is modular, so the transport of $E_4$, $E_6$ and $\wp_N$ gives
$$g\Bigl(\frac{H_\mu(L_0, h_v)(\tau_0)}{\omega_0^{2s g_F + 2|\mu|}}\Bigr) = \frac{H_{\mu \circ \sigma^{-1}}(L_0^A, h_{vA})(\tau_1)}{\omega_1^{2s g_F + 2|\mu|}}.$$
The map $\mu \mapsto \mu \circ \sigma^{-1}$ is a bijection from $\{\mu \leq \kappa\}$ to $\{\mu \leq \kappa'\}$, and it keeps the coefficients $\prod_i r(\kappa_i, \mu_i)$ and the exponents $|\kappa - \mu|$. So $g$ maps the sum for $\tau_0$, divided by $\omega_0^{w}$, to the sum for $\tau_1$, divided by $\omega_1^{w}$.

*Assembly.* The factors $(-1)^{|\kappa|}$, $q^{|\kappa|}$ and $n^{2sg_F}$ are rational, so $g$ fixes them. The second use of the value formula has the factor $c_1^{w(\kappa)}(2\operatorname{Im}\tau_1/\sqrt d)^{|\kappa|}$ and the value $c_1^{2sg_F}S'(0)$ in place of $S'(0)$, by the homothety rule. Since $c_1^{w(\kappa)} = c_1^{2sg_F} c_1^{2|\kappa|}$ and $(2\operatorname{Im}\tau_1/\sqrt d)\,c_1^2 = \|t\|\,q$, we get
$$g\bigl(\operatorname{co}_\kappa(\Omega_0, S(0))\bigr) = \operatorname{co}_\kappa(\Omega_1, \|t\|^{-|\kappa|} S'(0)),$$
after cancelling the nonzero factor $\|t\|^{|\kappa|} c_1^{2sg_F}$. $\square$

**Remark 1.4.6 (Formalization).** The first name is proved from the second by `first | exact @…`. The proof uses the Siegel-Klingen part of the first input and the functional equation; the Hilbert class field theorem and the main theorem of complex multiplication are hypotheses that are not used ([LatticeValueConjugationOfEllipticCMTheorems.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LatticeValueConjugationOfEllipticCMTheorems.lean#L206)). The hypothesis $\Omega_0^{12} = \Delta(\Lambda_0)$ is also not used (line 211). The ring automorphism $g$ need not be continuous. The transport lemma for $E_4$, $E_6$, $G_2^*$ and $\wp_N$, the level lemma, the twist lemma, the expansion in holomorphic jets and the Galois action on $q$-expansions are proved elsewhere; we have read their statements, not their proofs.
