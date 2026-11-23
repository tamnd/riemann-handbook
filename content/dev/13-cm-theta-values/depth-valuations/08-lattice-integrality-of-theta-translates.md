---
title: Lattice integrality of theta translates
decls:
  - GlobalTheory.MomN.exists_per
  - GlobalTheory.MomN.translates_latInt
  - GlobalTheory.T.cmTheta_baseVector_translates_integral
  - GlobalTheory.MomN.latInt_U_thZero
  - GlobalTheory.T.cm_base_theta_tensor_power_translates_integral
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Lattice integrality of theta translates

This section proves that the translates of the base theta function $\theta_M$ on $\mathbb{C}^{\mathcal{T}}$ and of its tensor powers $\Theta_{N, N'}$, by points of finite order prime to a split prime $q$, have integral $q$-adic jets in the directions of their lattice. The tensor power is a product of copies of $\theta_M$, and the fourth power of $\theta_M$ is a combination of products of translates of a theta function of one variable. The input is a period datum at $q$, whose existence we prove first. The next section extends the result to normalized theta vectors, the integrality step in the [finiteness of moments](/entry/moments-fin/).

### Lattice integrality

Let $q$ be a prime, let $\iota : \mathbb{C} \to \mathbb{C}_q$ be a field isomorphism and let $\omega \in \mathbb{C}_q$. Let $V$ be a finite-dimensional complex vector space, $\Lambda \subseteq V$ a subgroup and $G : V \to \mathbb{C}$ a smooth function. For a finite set $\kappa$ we view $\mathbb{Z}_q \subseteq \mathbb{C}_q$, and we write $\|\mu\|$ for the norm of a continuous linear form $\mu$ on $C(\mathbb{Z}_q^\kappa, \mathbb{C}_q)$.

**Definition 4.8.1.** Let $u : \kappa \to V$ be a finite family of vectors. A continuous linear form $\mu$ on $C(\mathbb{Z}_q^\kappa, \mathbb{C}_q)$ is a *moment measure* for $G$ in the directions $u$ if for every $k \geq 0$, every map $j : \{1, \dots, k\} \to \kappa$ and the function $f(a) = \prod_{l=1}^k a_{j(l)}$ we have
$$\iota\big(D^k G(0)(u_{j(1)}, \dots, u_{j(k)})\big) = \mu(f).$$
The function $G$ is *lattice integral* for $(\iota, \omega, \Lambda)$ if for every finite set $\kappa$ and every family $v : \kappa \to \Lambda$ there is a moment measure $\mu$ for $G$ in the directions $\iota^{-1}(\omega) v$ with $\|\mu\| \leq 1$.

The scalar $\iota^{-1}(\omega)$ plays the part of the period of a [multiplicative chart](/entry/exists-multiplicative-chart-at-split-prime/). A measure on $\mathbb{Z}_q$ of norm at most $1$ is the same as a series $\sum_m \mu\big(\binom{a}{m}\big) T^m$ in $\mathcal{O}_{\mathbb{C}_q}[[T]]$ (Mahler's theorem), and its moment series $\sum_k \mu(a^k) Y^k / k!$ becomes this series under $Y = \log(1 + T)$. So lattice integrality says that the series $\widehat{G}$ of [the theta laws](/entry/moments-of-translates/), taken along any finite family of lattice directions, has integral coefficients in the multiplicative variables.

We use three properties of lattice integrality.

1. Products. If $G_1, \dots, G_s$ are smooth and lattice integral for $(\iota, \omega, \Lambda)$, so is $G_1 \cdots G_s$. For two factors, let $\mu$ be the image of $\mu_1 \otimes \mu_2$ under addition $\mathbb{Z}_q^\kappa \times \mathbb{Z}_q^\kappa \to \mathbb{Z}_q^\kappa$. Expanding $\prod_l (a_{j(l)} + b_{j(l)})$ gives the Leibniz rule for $D^k(G_1 G_2)(0)$, so $\mu$ is a moment measure for $G_1 G_2$, and $\|\mu\| \leq \|\mu_1\| \|\mu_2\| \leq 1$. The empty product $1$ has the Dirac measure at $0$.
2. Sums. If $G = \sum_{x \in S} r_x G_x$ is a finite sum with each $G_x$ lattice integral and $\|\iota(r_x)\| \leq 1$, then $\mu = \sum_x \iota(r_x) \mu_x$ is a moment measure for $G$, and $\|\mu\| \leq 1$ by the ultrametric inequality.
3. Pullback. Let $A : V' \to V$ be complex linear and $\Lambda' \subseteq V'$ a subgroup such that for each $y \in \Lambda'$ some integer $s$ prime to $q$ has $s A(y) \in \Lambda$. If $G$ is lattice integral for $\Lambda$, then $G \circ A$ is lattice integral for $\Lambda'$. Indeed, given $v' : \kappa \to \Lambda'$, choose $s_k$ prime to $q$ with $v_k = s_k A(v'_k) \in \Lambda$, and a measure $\mu$ for $G$ in the directions $\iota^{-1}(\omega) v$. The jets of $G \circ A$ in the directions $\iota^{-1}(\omega) v'$ are those of $G$ divided by $\prod_l s_{j(l)}$. The image of $\mu$ under $a \mapsto (a_k / s_k)_k$, a homeomorphism of $\mathbb{Z}_q^\kappa$ since each $s_k$ is a unit of $\mathbb{Z}_q$, is a moment measure for $G \circ A$ of the same norm.

### Period data

Let $d$ be a prime with $d \equiv 7 \pmod{16}$, $K = \mathbb{Q}(\sqrt{-d})$, and let $\Delta(\mathcal{O}_K) = g_2^3 - 27 g_3^2$ be the discriminant of the lattice $\mathcal{O}_K \subseteq \mathbb{C}$. We use [CM theta functions for $d$, the theta laws](/entry/moments-of-translates/), models at $q$ and multiplicative charts as in the earlier sections.

**Definition 4.8.2.** Let $q$ be a prime and $\iota : \mathbb{C} \to \mathbb{C}_q$ a field isomorphism. A *period datum* for $\iota$ is a triple $(\delta_0, \theta, \Omega)$ with $\delta_0 \in \mathbb{C}$, $\theta : \mathbb{C} \to \mathbb{C}$ and $\Omega \in \mathbb{C}_q$ such that:
1. $\theta$ is a CM theta function for $d$;
2. $\delta_0^{12} = \Delta(\mathcal{O}_K)$ and $\delta_0 \neq 0$;
3. for every field isomorphism $\iota' : \mathbb{C} \to \mathbb{C}_q$ there is $\Omega' \in \mathbb{C}_q$ with $\|\Omega'\| = 1$ such that $(\iota', \Omega'/\iota'(\delta_0))$ satisfies the theta laws for $\theta$;
4. $\|\Omega\| = 1$ and $(\iota, \Omega/\iota(\delta_0))$ satisfies the theta laws for $\theta$;
5. there is a model $(\iota, L, c, W)$ at $q$ with $L = \mathcal{O}_K$ for which $\Omega / \iota(\delta_0)$ gives a multiplicative chart.

So $\Omega/\iota(\delta_0)$ is a $q$-adic period of the CM curve, normalized by a twelfth root of its discriminant. Conditions 3 and 4 are the hypotheses of the [theorem on moments of theta translates](/entry/moments-of-translates/).

**Theorem 4.8.3 (existence of period data).** Let $d$ be a prime with $d \equiv 7 \pmod{16}$, let $q$ be a prime split for $d$, and let $\iota : \mathbb{C} \to \mathbb{C}_q$ be a field isomorphism. Then there is a period datum for $\iota$.

Lean: `GlobalTheory.MomN.exists_per`.

*Proof.* Since $\mathbb{C}$ is algebraically closed, $\Delta(\mathcal{O}_K)$ has a twelfth root $\delta_0$. The lattice $\mathcal{O}_K$ has a CM theta function $\theta$ for $d$, an even theta function for this lattice. The discriminant of a lattice is not $0$, so $\delta_0 \neq 0$.

Now let $\iota'$ be any field isomorphism. There is a good model $(\iota', \mathcal{O}_K, c, W)$ at $q$ whose Weierstrass coefficients are algebraic. The [multiplicative chart theorem](/entry/exists-multiplicative-chart-at-split-prime/) gives $\omega_0$ with a multiplicative chart, and a normalization replaces it by $\omega = \omega_0 a$ with $a \in \mathbb{Z}_q$. Put $\Omega' = \omega \iota'(\delta_0)$. Two facts on the good model give $\|\iota'(\delta_0)\| \|\omega\| = 1$: one computes $\|\iota'(\delta_0)\|$ from $\delta_0^{12} = \Delta(\mathcal{O}_K)$, the other computes the norm of the normalized period $\omega$. So $\|\Omega'\| = 1$, and $\Omega'/\iota'(\delta_0) = \omega$ gives a multiplicative chart. Law 3 for $(\iota', \omega)$ is a bound for translates of power combinations in the chart, law 1 is law 3 for the single term $\theta$, whose chart series is integral, and law 2 is the shift formula for $W_y$ at $q$-power torsion points. Applied to $\iota' = \iota$ this gives conditions 4 and 5, and applied to all $\iota'$ it gives condition 3. $\square$

### The base theta function and its translates

We fix the data of the twisting chapters of this volume. A datum $D$ has the host field $K$ and a CM field $E$, with a finite set $\mathcal{T}$ of embeddings. A *curve ideal* is a nonzero ideal $\mathfrak{c}$ of $\mathcal{O}_K$ whose norm is prime to $2d$. Let $\delta \in \mathbb{C}$ with $\delta^{12} = \Delta(\varphi_0(\mathfrak{c}))$, the discriminant of the lattice $\varphi_0(\mathfrak{c}) \subseteq \mathbb{C}$. A *base* $B$ for $(D, \mathfrak{c}, \delta)$ contains the following objects.
- The lattice $\Lambda = \delta \varphi_0(\mathfrak{c})$ in $\mathbb{C}$ and a theta function $\theta_0$ of one variable for $\Lambda$.
- The lattice $\Lambda_M \subseteq \mathbb{C}^{\mathcal{T}}$ generated by the vectors $(w \tau(a))_{\tau \in \mathcal{T}}$ with $w \in \Lambda$ and $a$ in a fixed fractional ideal $\mathfrak{b}^{-1}$ of $E$.
- The Hermitian form $H_1 = \operatorname{area}(\Lambda)^{-1} \mathrm{Id}$ on $\mathbb{C}^{\mathcal{T}}$ and the translation operators $U_t$ of $H_1$, as in [the earlier section](/entry/moments-of-translates/).
- A *base theta function* $\theta_M$: a theta function for $(H_1, \Lambda_M)$ with the quadratic semicharacter of the base, whose fourth tensor power $\theta_M(z_1)\theta_M(z_2)\theta_M(z_3)\theta_M(z_4)$ is a nonzero multiple of a standard kernel moved by a fixed isometry.

A point $t$ is *of order prime to $q$* for a lattice $\Lambda'$ if $n t \in \Lambda'$ for some integer $n > 0$ prime to $q$.

**Theorem 4.8.4 (translates of the base theta function).** Let $\mathfrak{c}$ be a curve ideal, $\delta^{12} = \Delta(\varphi_0(\mathfrak{c}))$, and $B$ a base. Let $q \neq 2$ be a prime with $\left(\frac{-d}{q}\right) = 1$ and with $N(\mathfrak{c})$ prime to $q$. Let $\iota : \mathbb{C} \to \mathbb{C}_q$ be a field isomorphism and $(\delta_0, \theta, \Omega)$ a period datum for $\iota$. Let $t \in \mathbb{C}^{\mathcal{T}}$ and let $n$ be an integer prime to $q$ with $n t \in \Lambda_M$. Then $U_t \theta_M$ is lattice integral for $(\iota, \Omega/\iota(\delta_0), \Lambda_M)$.

Lean: `GlobalTheory.MomN.translates_latInt` (also `GlobalTheory.T.cmTheta_baseVector_translates_integral`, a second name).

*Proof.* Step 1 (the isometry). Put $W = \mathbb{C}^{\{1,2,3,4\} \times \mathcal{T}}$. Since $q$ splits and is odd, there are a linear isometry $g$ of $W$ and a constant $e$ with $\|\iota(e)\| = 1$ with the following properties: $g$ carries $\Lambda_M^4$ onto a lattice $g(\Lambda_M^4)$ whose index $m$ in the standard lattice $\Lambda^{\{1,2,3,4\} \times \mathcal{T}}$ is prime to $q$, and the fourth tensor power of $\theta_M$ is $e$ times the standard kernel moved by $g$.

Step 2 (the shape of the fourth power). Let $S \subseteq g(\Lambda_M^4)$ be a finite set of coset representatives given by the index condition, and let $v = g(t, t, t, t)$. The quadratic semicharacter identity gives, for $y \in W$,
$$\big(U_t \theta_M\big)^{\otimes 4}(g^{-1} y) = \sum_{x \in S} r(x) \prod_{w} \big(U_{v_w + x_w} \theta_0\big)(y_w),$$
with $r(x) = e\, m^{-1/2}\, \alpha(x)\, e^{-\pi i E(v, x)}$, where $\alpha(x) = \pm 1$ is the semicharacter and $E$ is the alternating form of the standard Hermitian form.

Step 3 (the coefficients). We have $\|\iota(r(x))\| \leq 1$: $\|\iota(e)\| = 1$, $\|\iota(\sqrt m)\| = 1$ because $m$ is prime to $q$, $\alpha(x) = \pm 1$, and $e^{-\pi i E(v, x)}$ is a root of unity of order dividing $2n$, because $n v \in g(\Lambda_M^4)$ and the lattice is self-dual.

Step 4 (the factors). For $x \in S$ we have $n(v + x) \in g(\Lambda_M^4)$, so the point $v_w + x_w$ satisfies $n m (v_w + x_w) \in \Lambda$, and $nm$ is prime to $q$. The one-variable theorem for $\theta_0$, which uses the period datum, shows that $U_{v_w + x_w} \theta_0$ is lattice integral for $\Lambda$. The projection $y \mapsto y_w$ carries the standard lattice into $\Lambda$, so the pullback property shows that $y \mapsto U_{v_w + x_w}\theta_0(y_w)$ is lattice integral for the standard lattice. By the product and sum properties and Step 3, the sum $G$ of Step 2 is lattice integral.

Step 5 (back to $\Lambda_M$). For $z \in \Lambda_M^4$ we have $m\, g(z)$ in the standard lattice, and $m$ is prime to $q$. The pullback property along $g$ shows that $(U_t \theta_M)^{\otimes 4} = G \circ g$ is lattice integral for $\Lambda_M^4$. Finally, lattice integrality of the fourth tensor power of a smooth function for $\Lambda_M^4$ implies lattice integrality of the function for $\Lambda_M$. $\square$

### Tensor powers

For $N, N' \geq 0$ let $V_{N, N'} = \mathbb{C}^{\mathcal{T} \times N' \times N}$, with points $z = (z_{\tau i j})$. The *tensor power* of the base theta function is
$$\Theta_{N, N'}(z) = \prod_{i < N'} \prod_{j < N} \theta_M\big((z_{\tau i j})_{\tau}\big).$$
For $O_E$-lattices $L \subseteq E^N$ and $L' \subseteq E^{N'}$ let $\Lambda_{L, L'} \subseteq V_{N, N'}$ be the lattice of the base attached to $(L, L')$, and let $U_s$ be the translation operators on $V_{N, N'}$ of the Hermitian form of the base. For the standard lattices $L = \mathcal{O}_E^N$ and $L' = \mathcal{O}_E^{N'}$, $\Lambda_{L, L'}$ is the set of $z$ whose columns $(z_{\tau i j})_\tau$ all lie in $\Lambda_M$.

**Theorem 4.8.5 (translates of tensor powers).** Under the hypotheses of the previous theorem on $\mathfrak{c}$, $\delta$, $B$, $q$, $\iota$ and the period datum, let $N, N' \geq 0$ and let $s \in V_{N, N'}$ be of order prime to $q$ for the standard lattice $\Lambda_{\mathrm{std}} = \Lambda_{\mathcal{O}_E^N, \mathcal{O}_E^{N'}}$. Then $U_s \Theta_{N, N'}$ is lattice integral for $(\iota, \Omega/\iota(\delta_0), \Lambda_{\mathrm{std}})$.

Lean: `GlobalTheory.MomN.latInt_U_thZero` (also `GlobalTheory.T.cm_base_theta_tensor_power_translates_integral`, a second name).

*Proof.* The Hermitian form of the base on $V_{N, N'}$ is the orthogonal sum of copies of $H_1$, one for each pair $(i, j)$, since the areas of the two lattices agree. So the translation operator splits as a product, and
$$U_s \Theta_{N, N'}(z) = \prod_{i, j} \big(U_{s_{\cdot i j}} \theta_M\big)\big((z_{\tau i j})_\tau\big).$$
Let $n > 0$ be prime to $q$ with $n s \in \Lambda_{\mathrm{std}}$. Then $n s_{\cdot i j} \in \Lambda_M$, so by the previous theorem each $U_{s_{\cdot ij}} \theta_M$ is lattice integral for $\Lambda_M$. The map $z \mapsto (z_{\tau i j})_\tau$ carries $\Lambda_{\mathrm{std}}$ into $\Lambda_M$, so the pullback property (with $s = 1$) makes each factor lattice integral for $\Lambda_{\mathrm{std}}$. The product property, applied twice, finishes the proof. $\square$

**Remark 4.8.6 (Formalization).** We did not open the proof of the lemma on fourth tensor powers ([LatticeJetsAreBoundedMomentsOfTensorFourthPowerStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/LatticeJetsAreBoundedMomentsOfTensorFourthPowerStatement.lean#L4)). We did not unfold the construction of the base lattices beyond what is stated. In the first theorem the function $\theta$ and the root $\delta_0$ of the period datum enter only through $\Omega / \iota(\delta_0)$ and the one-variable lemma ([CmThetaBaseVectorTranslatesIntegral.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/CmThetaBaseVectorTranslatesIntegral.lean#L51)). The base theta function is chosen by the axiom of choice. In the existence of period data, $\delta_0 \neq 0$ is taken from a lemma on unit periods instead of from $\Delta(\mathcal{O}_K) \neq 0$, and the model given for $\iota' \neq \iota$ is dropped ([LawsAndChart.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/LawsAndChart.lean#L43)). The two results with the prefix `GlobalTheory.T.` are second names, proved by `first | exact @…` under `maxHeartbeats 1000000`.
