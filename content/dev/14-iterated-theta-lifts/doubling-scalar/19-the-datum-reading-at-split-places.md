---
title: The datum reading at split places
decls:
  - GlobalTheory.AdForm.DatumRead.reads_datum_eq_thC
  - GlobalTheory.T.datumReading_splitPlaces_eq_classicalTheta
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The datum reading at split places

The last part of this chapter computes the theta kernels of the column chains, which give the class data of [the column condition](/entry/cls-pin-d-of-fam-col-of-true-w/) in the open orbit chapter. The first input is local at a finite set of split places. A theta function on the adelic Weil space is built from a Schwartz-Bruhat function that lives at these places. We read it at the infinite places as a function on a complex vector space, with a Gaussian factor. This section proves that the reading is a classical theta function with characteristics over the period lattice, and that the theta function is holomorphic, that is, a Fock vacuum at every infinite place. The result is used in [the theta kernel at split places](/entry/theta-kernel-eq-jet-th-c/) of the next section, where the jets of the reading give the kernel.

**Setting.** Let $E/F$ be the CM extension of the host datum, with ring of integers $\mathcal{O}_E$, discriminant $d$, adeles $\mathbb{A}_E$ and an ideal $\mathfrak{a}_0$ of $\mathcal{O}_E$. Let $\Sigma$ be the CM type, with embeddings $\tau \colon E \to \mathbb{C}$. Let $\psi$ be an additive character of $\mathbb{A}_F$, let $\theta$ be a family of data at the infinite places, and let $S$ and $T$ be hermitian spaces of ranks $a$ and $b$. Let $\delta \in \mathbb{C}$ and $s_c \in \mathbb{R}$. The *Weil space* $W$ is the space of $b \times a$ matrices over $\mathbb{A}_E$, with the symplectic form $\langle\ ,\ \rangle$ of the pair $(S, T)$ and the Heisenberg translates
$$(h_{w_0} f)(w) = \psi(\langle w, w_0 \rangle)\, f(w + w_0).$$
A *theta function* on $W$ is a continuous and smooth function $f$ with $f(\gamma + w) = \psi(-\langle \gamma, w \rangle) f(w)$ for all rational $\gamma$, fixed by the translates of an open subgroup at the finite places. A function is *holomorphic* if it is a theta function and, at each $\tau \in \Sigma$, a Fock vacuum: the annihilation operators of the standard complex structure at $\tau$ kill it.

We say that $(\theta, S, T, \delta, s_c, \psi)$ is a *standard pair* if $\psi$ is standard of sign $-1$, $\theta$ is an infinite family, $S$ and $T$ have Gram matrix $1$ and admissible signatures, $0 < a < b$ with $a$ and $b$ even, the class condition of the host holds, $\delta \neq 0$, $\tau(\xi_0) = i/\sqrt{d}$ for every $\tau$, and $s_c |\delta|^2 = 2/\sqrt{d}$.

**Definition 2.19.1 (Reading).** Let $V = \prod_{\tau \in \Sigma} M_{b \times a}(\mathbb{C})$ with the hermitian form $H(z, w) = s_c \sum_{\tau, i, j} z_{\tau i j}\, \overline{w_{\tau i j}}$. For $z \in V$ let $x(z) \in W$ be the point with zero finite part and component $-\delta^{-1} z_\tau$ at $\tau$. The *reading* of a function $f$ on $W$ is
$$\xi(f)(z) = e^{\pi H(z, z)/2}\, f(x(z)).$$

The Gaussian factor turns the Fock model at the infinite places into functions on $V$. The Heisenberg group of $(V, H)$ acts by
$$(U_x F)(z) = F(z + x)\, e^{-\pi H(z, x) - \pi H(x, x)/2},$$
and the quadratic phase is $\alpha(x) = \exp(\pi i \tfrac{\sqrt{d}}{2} \operatorname{Re} H(x, x))$.

**Definition 2.19.2 (Period lattice and halves).** Let $N \subset E^a$ and $N' \subset E^b$ be $\mathcal{O}_E$-lattices. Let $M$ be the $\mathcal{O}_E$-span of the maps $r x$ with $r \in \mathfrak{a}_0$ and $x(N) \subset N'$. Let $SS$ be a finite set of places of $E$ and $c > 0$ an integer. Let $e(Q) = 1$ for $Q \in SS$, $e(Q) = -1$ if the conjugate of $Q$ is in $SS$, and $e(Q) = 0$ otherwise. The *half lattices* are
$$M_A = \{ w : w \in c^{-e(Q)} M_Q \text{ for all } Q \}, \qquad M_B = \{ w : w \in c^{e(Q)} M_Q \text{ for all } Q \}.$$
Let $\Lambda$, $A$ and $B$ be the images of $M$, $M_A$ and $M_B$ in $V$ under $x \mapsto (\delta\, \tau(x))_\tau$. We say that the *lattice facts* hold if $\Lambda$ is self dual for $\operatorname{Im} H$ and $\alpha$ is a semicharacter on $\Lambda$: $\alpha = \pm 1$ on $\Lambda$ and $\alpha(x + y) = \alpha(x) \alpha(y)\, e^{\pi i \operatorname{Im} H(x, y)}$.

Let $S_X$ be a set of representatives of $A$ modulo $\Lambda$, let $S_A$ be a set of representatives of $\Lambda \cap A$ modulo $B$, and let $S_B$ be a set of representatives of $B$ modulo $\Lambda$. For a function $\Xi$ on the $E$-linear maps $E^a \to E^b$, let $\Xi_V$ be the function on $V$ that is $\Xi(x)$ at the image of $x$ and $0$ off the image.

**Definition 2.19.3 (Classical theta function).** For $\Xi$ and a function $\vartheta$ on $V$, the *classical theta function* of $\Xi$ over $\vartheta$ is
$$\mathrm{th}_C(\Xi, \vartheta) = \sum_{x \in S_X} \sum_{y \in S_B} \alpha(x)\, \alpha(y)\, \widehat{\Xi}_x(y)\ U_x U_y\, \vartheta,$$
where
$$\widehat{\Xi}_x(y) = \frac{1}{|S_A|} \sum_{t \in S_A} \Xi_V(t - x)\, e^{2\pi i \operatorname{Im} H(t, y)}.$$

So $\widehat{\Xi}_x$ is a finite Fourier transform of $\Xi$ over $\Lambda \cap A$ modulo $B$. When $\vartheta$ is the reading of the vacuum, $U_x U_y \vartheta$ is a theta function with characteristics $x$ and $y$ in the sense of [theta functions with characteristics](/learn/theta-functions-cm/#theta-functions-with-characteristics).

**Theorem 2.19.4 (The reading is a classical theta function).** Let $(\theta, S, T, \delta, s_c, \psi)$ be a standard pair. Let $e$ be the sum of idempotents of the places of $SS$, with $e \bar{e} = 0$. Let $c > 0$ be odd, with $Q_S\, q\, d \notin Q$ for all $Q \in SS$. Assume the lattice facts, and assume that $N$ and $N'$ give self dual lattices of $S$ and $T$. Let $f_0$ be a vacuum for the lattice pair $(N, N')$ with unit scalars. Let $\Phi$ be a Schwartz-Bruhat function on $W$ that is half at $e$ for the lattice $L$ of $(N, N')$: it vanishes off the $e$-part, and for some $k > 0$ it is invariant under $k u$ for half elements $u \in L$ and has $k t \in L$ on its support. Let $f$ be the theta function at $e$ of $\Phi$ with vacuum $f_0$. Let $\Xi$ satisfy:

1. $\Phi(e \gamma) = \Xi(\gamma)$ for every rational matrix $\gamma$;
2. $\Xi(x) \neq 0$ implies that $c x$ maps $N_P$ into $N'_P$ for every $P \in SS$;
3. $\Xi(x + c y) = \Xi(x)$ for every $y$ that maps $N_P$ into $N'_P$ for every $P \in SS$.

Then $f$ is holomorphic, and $\xi(f) = \mathrm{th}_C(\Xi, \xi(f_0))$.

Lean: `GlobalTheory.AdForm.DatumRead.reads_datum_eq_thC` (also `GlobalTheory.T.datumReading_splitPlaces_eq_classicalTheta`, a second name).

*Proof.* We expand $f$ as a finite sum of Heisenberg translates of $f_0$, and then read each translate.

1. *Representatives.* By the lemma on representatives of the period lattice halves, $S_X$, $S_A$ and $S_B$ are finite systems of representatives. Each $x \in S_X$ is the image of some $x' \in M_A$, and each $y \in S_B$ is the image of some $y' \in M_B$. Fix such lifts, and write $\gamma_x$ and $\gamma_y$ for their matrices.
2. *Fourier expansion of $\Phi$.* By the finite Fourier expansion at the half split places, for every $t \in W$,
$$\Phi(t) = \sum_{x \in S_X} \sum_{y \in S_B} \widehat{\Xi}_x(y)\ \psi\big(\langle t + e\gamma_x, \bar{e}\gamma_y \rangle\big)\ \mathbf{1}_{L, e}(t + e\gamma_x),$$
where $\mathbf{1}_{L, e}$ is the indicator of the half elements of $L$.
3. *Translates.* The idempotent satisfies $e^2 = e$. The standard character is $1$ on $\langle c u, \bar{e}\gamma_y \rangle$ for $u \in L$, by the lemma on the half period lattice. The theorem on Fourier sums of theta functions then gives
$$f = \sum_{x \in S_X} \sum_{y \in S_B} \widehat{\Xi}_x(y)\ h_{e\gamma_x} h_{\bar{e}\gamma_y} f_0.$$
4. *Semicharacters.* Let $r(\gamma)$ be the finite rational part of a rational matrix $\gamma$. By the lemma on the conjugate half of the vacuum, $h_{\bar{e}\gamma_y} f_0 = \alpha(y)\, h_{r(\gamma_y)} f_0$. By the lemma on the half component, $h_{e\gamma_x} h_{r(\gamma_y)} f_0 = \alpha(x)\, h_{r(\gamma_x)} h_{r(\gamma_y)} f_0$. So with $C(x, y) = \widehat{\Xi}_x(y)\, \alpha(x)\, \alpha(y)$,
$$f = \sum_{x, y} C(x, y)\ h_{r(\gamma_x)} h_{r(\gamma_y)} f_0.$$
5. *Holomorphy.* The product of two Heisenberg translates is a scalar times the translate by the sum. The sum $r(\gamma_x) + r(\gamma_y)$ has zero infinite part. A finite sum of translates of a theta function by elements with zero infinite part is a theta function, and it is a Fock vacuum at $\tau$ when $f_0$ is one. The vacuum $f_0$ is a theta function and a Fock vacuum at each $\tau$. So $f$ is holomorphic.
6. *Reading.* The reading is linear. By the Gaussian reading of finite rational translates, applied twice, $\xi(h_{r(\gamma_x)} h_{r(\gamma_y)} f_0) = U_x U_y\, \xi(f_0)$, since the image of $\gamma_x$ in $V$ is $x$ and the image of $\gamma_y$ is $y$.
7. *Conclusion.* So $\xi(f) = \sum_{x, y} C(x, y)\, U_x U_y\, \xi(f_0)$. The formula for $\mathrm{th}_C$ as a kernel, with volume $1$, is the same triple sum over $x$, $y$ and $t$. $\square$

The proof does not use hypotheses 2 and 3 on $\Xi$ directly. They enter through the Fourier expansion of step 2, which needs them for $\widehat{\Xi}_x$ to be the coefficient.

**Remark 2.19.5 (Formalization).** The theorem is at [DatumReadingSplitPlacesEqClassicalTheta.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/DatumReadingSplitPlacesEqClassicalTheta.lean#L24). The second name is in [DatumReadingSplitPlacesEqClassicalThetaStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/DatumReadingSplitPlacesEqClassicalThetaStatement.lean#L9); it applies the first by a `first | exact` block under a limit of one million heartbeats. The reading, the standard pair and holomorphy are in [SplitPart.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/SplitPart.lean#L22), and the classical theta function, the half lattices and the lattice facts are in [XiIndCClass.lean](lean:Formalism/LocalToGlobal/KernelLattices/XiIndCClass.lean#L239). The sets of representatives are chosen by `Classical.epsilon`, so the definition of the classical theta function makes sense for all lattices. Step 1 shows that they are real representatives under the hypotheses. The seven lemmas of steps 1 to 6 are restatements in `*Statement.lean` files; we have read their statements, not their proofs. We have not unfolded the vacuum condition beyond its two parts (theta function and Fock vacuum), the place models of the theta function at $e$, or the smoothness condition.
