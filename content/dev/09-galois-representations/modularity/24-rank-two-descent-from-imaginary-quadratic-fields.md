---
title: Rank two descent from imaginary quadratic fields
decls:
  - UpperTheory.ConvolutionTheory.RankTwoDescent.fac_of
  - UpperTheory.ConvolutionTheory.RankTwoDescent.asaiNV
  - UpperTheory.ConvolutionTheory.RankTwoDescent.rev_holds
  - UpperTheory.ConvolutionTheory.RankTwoDescent.downN
  - UpperTheory.ConvolutionTheory.RankTwoDescent.descS
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Rank two descent from imaginary quadratic fields

This section proves the converse of section 23 over $\mathbb{Q}$. Let $M$ be an imaginary quadratic field and $P$ a cuspidal representation of $\mathrm{GL}_2(\mathbb{A}_M)$ whose Satake parameters at two conjugate places agree, for almost all places. Then $P$ comes from a cuspidal representation $\pi$ of $\mathrm{GL}_2(\mathbb{A}_{\mathbb{Q}})$: the Satake parameters of $\pi$ and of $P$ agree at almost all places of degree one, and so do the infinitesimal characters. The proof uses the same theta correspondence in the other direction. A nonvanishing period of $P$ gives a nonzero pairing of $P$ with a theta lift from $\mathrm{SL}_2$ over $\mathbb{Q}$, and the period does not vanish because of a pole of the Asai $L$-function. The descent is one of the two forms of the cyclic base change hypothesis in section 25.

Let $E$ be an imaginary quadratic field with a datum $D = (\delta, \theta, \sigma)$ over $\mathbb{Q}$ as in section 23, a Weil representation $W$ with quadratic character $\eta$ of $E/\mathbb{Q}$, and measures on $\mathrm{SL}_2(\mathbb{A}_{\mathbb{Q}})$ and $\mathrm{SL}_2(\mathbb{A}_E)$. Let $P$ be a cuspidal representation of $\mathrm{GL}_2(\mathbb{A}_E)$.

**Definition 8.24.1 (Conjugation invariance and central character).** The representation $P$ is conjugation invariant if for almost all finite places $w$ of $E$, and each $w'$ above the same prime as $w$, the Satake parameters of $P$ at $w$ and at $w'$ are equal. A Hecke character $\omega$ of $\mathbb{Q}$ is a central character of $P$ over $\mathbb{Q}$ if $\varphi(z g) = \omega(N_{E/\mathbb{Q}} z)\, \varphi(g)$ for each $\varphi \in P$ and each idele $z$ of $E$.

**Definition 8.24.2 (Periods).** Let $\upsilon$ be a probability measure on the norm one ideles of $\mathbb{Q}$ and $\chi$ a Hecke character of $\mathbb{Q}$. For a function $\varphi$ on $\mathrm{GL}_2(\mathbb{A}_E)$, the $\chi$-period of $\varphi$ is

$$\mathcal{P}_\chi(\varphi) = \int \chi(t) \int_{D} \varphi\bigl(g\, d(t)\bigr)\, dg\, d\upsilon(t),$$

where $D$ is a fundamental domain for $\mathrm{SL}_2(\mathbb{Q})$ in $\mathrm{SL}_2(\mathbb{A}_{\mathbb{Q}})$ and $d(t) = \mathrm{diag}(1, t)$. The representation $P$ has no $\chi$-period if $\mathcal{P}_\chi$ vanishes on all translates of all $\varphi \in P$.

The periods over $\mathrm{GL}_2(\mathbb{Q}) \backslash \mathrm{GL}_2(\mathbb{A}_{\mathbb{Q}})$ are the classical test for descent: a cuspidal $P$ with a nonzero period of this kind is distinguished, and distinguished representations are base changes.

**Theorem 8.24.3 (Factorization of the zeta integral).** Let $P$ have central character $\omega$ over $\mathbb{Q}$ with $|\omega| = 1$, and let $\chi$ be a Hecke character with $(\chi \omega)^{2} = 1$. Let $L$, $N$ be positive integers, with $\chi$ trivial on the unit ideles that are $1$ modulo $N$. Then there is $c \ne 0$ with the following property. Let $\varphi$ be an admitted function, good for $(L, N)$, and let $(a_n)$ be a sequence of Asai coefficients of $P$ for $\chi$ and $N$. Let $e \ge 0$, $p$ a homogeneous polynomial of degree $2e$ in two variables, and $\mathrm{Re}(s) > 4$ with $\sum a_n n^{-s}$ absolutely convergent. Then

$$\begin{aligned} Z(\varphi, \Phi_{N,p}, s) = c\, \pi^{-(s+e)} \Gamma(s + e) &\sum_{n \ge 1} a_n n^{-s} \\ &\cdot M(\varphi, p, s). \end{aligned}$$

Here $Z$ is the zeta integral of the Whittaker function of $\varphi$ against the Schwartz function $\Phi_{N,p}$ (the polynomial $p$ times a Gaussian at infinity and the characteristic function of the lattice of level $N$), and $M(\varphi, p, s)$ is the integral of the archimedean Whittaker function of $\varphi$ along the rotations, weighted by $p(\sin t, \cos t)$. The constant is

$$c = \frac{c_K}{2 \pi}\, c_T(L)\, c_T(N),$$

where $c_K$ is the volume of the level $N$ part of the maximal compact subgroup and $c_T$ is the volume of a congruence set of finite ideles.

Lean: `UpperTheory.ConvolutionTheory.RankTwoDescent.fac_of`.

*Proof.* A function that is good for $(L, N)$ has $N > 0$ and $L \mid N$, so $L > 0$. The three volumes are positive, so $c \ne 0$. At the places prime to $N$, $\varphi$ is a Hecke eigenfunction, and its Whittaker coefficients are given by the Hecke eigenvalues $\mu_n$; the $n$-th coefficient of the zeta integral is the convolution of $\mu$ with the squares prime to $N$, and this convolution is the Asai coefficient $a_n$. So the zeta integral, integrated first over the ideles, is a sum of the Dirichlet series $\sum a_n n^{-s}$ against a function of the rotation $k$. That function is measurable and bounded, and the weight $p(\sin t, \cos t)$ is bounded, so Fubini's theorem applies. The integral over $z$ in $Z$ gives $\pi^{-(s+e)} \Gamma(s+e)$ and the factor $c_T(N)$, the integral over the level subgroup gives $c_K / (2\pi)$ and $c_T(L)$, and the remaining integral over the rotations is $M(\varphi, p, s)$. $\square$

**Theorem 8.24.4 (Nonvanishing of the Asai periods).** Let $E$ be imaginary quadratic with a datum over $\mathbb{Q}$, and $P$ cuspidal on $\mathrm{GL}_2(\mathbb{A}_E)$, conjugation invariant, with central character $\omega$ over $\mathbb{Q}$ and $|\omega| = 1$. Let $\eta$ be the quadratic character of $E/\mathbb{Q}$. Then $P$ has an $\omega^{-1}$-period or an $(\omega \eta)^{-1}$-period.

Lean: `UpperTheory.ConvolutionTheory.RankTwoDescent.asaiNV`.

*Proof.* Choose a good function $\varphi$ with $W(\varphi)(1) \ne 0$, and Asai coefficients $(a_n)$ for $\omega^{-1}$ and $(a'_n)$ for $(\omega\eta)^{-1}$, whose Dirichlet series converge for $\mathrm{Re}(s) > 4$. If $P$ has no $\chi$-period, then the Dirichlet series of the Asai coefficients for $\chi$ extends to an entire function: by the Rankin-Selberg unfolding, the $\chi$-period of $P$ against a theta series is the zeta integral, and the [Theorem 8.24.3](/entry/fac-of/) writes the zeta integral as the Dirichlet series times factors that do not vanish. Suppose that $P$ has neither period. Then both Dirichlet series are entire. Since $P$ is conjugation invariant and $\eta$ is the quadratic character of $E/\mathbb{Q}$ at the good places, the two series combine to a Dirichlet series with nonnegative coefficients and first coefficient $1$, and Landau's theorem on such series gives a contradiction. $\square$

**Theorem 8.24.5 (Reversal of the theta lift).** Let $P$ be cuspidal on $\mathrm{GL}_2(\mathbb{A}_E)$. Suppose that some translate of some $\varphi \in P$ has a nonzero period over the norm one ideles of $E$ and $\mathrm{SL}_2(\mathbb{A}_{\mathbb{Q}})$. Then there is a cuspidal $\pi$ on $\mathrm{GL}_2(\mathbb{A}_{\mathbb{Q}})$, invariant under the positive reals in the centre, and $f \in \pi$, $\varphi_0$ in the Fock space and $\varphi \in P$, such that the integral of $\theta(f, \varphi_0)\, \varphi$ over the same subgroup is not zero.

Lean: `UpperTheory.ConvolutionTheory.RankTwoDescent.rev_holds`.

*Proof.* Expand the period of $\varphi$ by the spectral decomposition of $L^{2}(\mathrm{SL}_2(\mathbb{Q}) \backslash \mathrm{SL}_2(\mathbb{A}_{\mathbb{Q}}))$, seen through the theta kernel. The constant term of the theta lift is its anisotropic part, since the terms of the other orbits have mean zero and the rank one terms are controlled by a majorant of the theta series. With the coefficients of the theta kernel, the pairing of $\varphi$ with the lifts of the constant term is cuspidal, and by density and Fubini's theorem the period of $\varphi$ is a sum of pairings of $\varphi$ with lifts of cusp forms. Since the period is not zero, one pairing is not zero. $\square$

**Theorem 8.24.6 (Descent of normalised representations).** Let $E$ be imaginary quadratic and $P$ a normalised cuspidal representation of $\mathrm{GL}_2(\mathbb{A}_E)$ that is conjugation invariant. Then there is a cuspidal $\pi$ on $\mathrm{GL}_2(\mathbb{A}_{\mathbb{Q}})$ with two properties: for almost all places $w$ of $E$ of degree one over $p$, $\pi_p$ and $P_w$ have the same Satake parameters, and for each complex place $\tau$ of $E$, if $P$ has infinitesimal character $m$ at $\tau$, so has $\pi$ at the real place.

Lean: `UpperTheory.ConvolutionTheory.RankTwoDescent.downN`.

*Proof.* Choose a datum, a Weil representation and measures. The representation $P$ has a central character $\omega$ over $\mathbb{Q}$. Since $P$ is normalised, it is unitary, so $|\varphi(a g)| = |\varphi(g)|$ for $a$ in the centre. For an idele $a$ of $\mathbb{Q}$, $N_{E/\mathbb{Q}}(a) = a^{2}$, so $|\omega(a)|^{2} = 1$ and $|\omega| = 1$. By the [Theorem 8.24.4](/entry/asai-nv/) on Asai periods, $P$ has an $\omega^{-1}$-period or an $(\omega\eta)^{-1}$-period. In both cases some translate of some $\varphi \in P$ has a nonzero period over the norm one ideles. The [Theorem 8.24.5](/entry/rev-holds/) on reversal gives a cuspidal $\pi$ over $\mathbb{Q}$ and a nonzero pairing of $P$ with a theta lift of $\pi$. This pairing is refined to a nonzero pairing over the diagonal torus for a cuspidal $\pi'$, and the nonzero pairing with the lift of $\pi'$ forces the agreement of Satake parameters at the split places and of infinitesimal characters. $\square$

**Theorem 8.24.7 (Descent from imaginary quadratic fields).** Let $M$ be an imaginary quadratic field and $P$ a cuspidal representation of $\mathrm{GL}_2(\mathbb{A}_M)$ such that, for almost all $w$ and each $w'$ above the same prime, the Satake parameters of $P$ at $w$ and $w'$ agree. Then there is a cuspidal representation $\pi$ of $\mathrm{GL}_2(\mathbb{A}_{\mathbb{Q}})$ such that for almost all $w$ of degree one over $p$ the Satake parameters of $\pi_p$ and $P_w$ agree, and the infinitesimal character of $P$ at each complex place is that of $\pi$ at the real place.

Lean: `UpperTheory.ConvolutionTheory.RankTwoDescent.descS`.

*Proof.* Twist $P$ by $|\cdot|^{s}$ with $s \in \mathbb{C}$ chosen so that $P \otimes |\cdot|^{s}$ is normalised. Conjugate places $w$, $w'$ have the same norm, so $|\cdot|^{s}$ has the same value at $w$ and at $w'$, and the twist is still conjugation invariant. The [Theorem 8.24.6](/entry/down-n/) on descent gives $\pi'$ over $\mathbb{Q}$. Put $\pi = \pi' \otimes |\cdot|^{-s}$. At a place $w$ of degree one over $p$, $N w = p$, so the twists by $|\cdot|^{s}$ at $w$ and $|\cdot|^{-s}$ at $p$ cancel, and the Satake parameters of $\pi_p$ and $P_w$ agree. The infinitesimal characters move by the same shift on both sides. $\square$

**Remark 8.24.8 (Formalization).** The statement of descent asks that the infinitesimal characters of $P$ be regular and have a gap (the conditions `RegInf` and `Gap2`), and these are not used in the proof ([AbsNormConj.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/SplitEigenfunctions/AbsNormConj.lean#L42)). The cuspidal datum over $M$ may also be of the totally real kind, and lines 45 to 48 of that file close this case by the contradiction that $M$ is both totally real and totally complex. In the factorization ([FacOf.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/SplitEigenfunctions/InfinitePlaceGluing/FacOf.lean#L67)) the case where $L$ or $N$ is not positive is vacuous and is closed at lines 67 to 70 with $c = 1$. Our proofs of the Asai nonvanishing, of the reversal and of the last step of descent read the names of the lemmas that the formal proofs combine (unfolding, Landau's theorem, majorants, mean zero, density); we have not unfolded those lemmas, nor the notions of a normalised representation, an admitted function, a good function and Asai coefficients beyond their first fields.
