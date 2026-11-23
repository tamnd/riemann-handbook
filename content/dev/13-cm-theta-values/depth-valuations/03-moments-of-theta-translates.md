---
title: Moments of theta translates at split primes
decls:
  - GlobalTheory.MomOne.Translates.moments_of_translates
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Moments of theta translates at split primes

This section constructs $q$-adic measures whose moments are the jets of the translates of a CM theta function in several variables, at a prime $q$ that splits in $K = \mathbb{Q}(\sqrt{-d})$. The measures live on $\mathbb{Z}_q^r$, and their norms are bounded uniformly in the translation. The input is a theta function $\theta$ in one variable whose $q$-adic expansion in a [multiplicative chart](/entry/exists-multiplicative-chart-at-split-prime/) satisfies three laws. The result is the main step of the [finiteness of moments](/entry/moments-fin/), which adds the norm bound for averaged translates.

### Theta functions in one variable

Fix a prime $d$ with $d \equiv 7 \pmod{16}$, put $w = (1 + i\sqrt d)/2$ and $\mathcal{O}_K = \mathbb{Z} + \mathbb{Z} w$. For $z, x \in \mathbb{C}$ put $h_1(z, x) = \frac{2}{\sqrt d} z \bar x$. For a function $F : \mathbb{C} \to \mathbb{C}$ define the translation operators
$$U_x F(z) = F(z + x)\, e^{-\pi h_1(z, x) - \frac{\pi}{2} h_1(x, x)}, \qquad W_x F = e^{\pi i |x|^2}\, U_x F,$$
and the pairing $\kappa(x, y) = e^{-2\pi i \operatorname{Im} h_1(x, y)}$. These are the Heisenberg operators of the [Fock model](/learn/theta/#the-fock-model) for the Hermitian form $h_1$ ([the Heisenberg group](/learn/groups/#the-heisenberg-and-metaplectic-groups)).

**Definition 4.3.1.** A function $\theta : \mathbb{C} \to \mathbb{C}$ is a *CM theta function for $d$* if $\theta$ is entire, $\theta(0) = 1$, $\theta(-z) = \theta(z)$, $W_x \theta = \theta$ for every $x \in \mathcal{O}_K$, and every zero of $\theta$ lies in $\frac12 + \mathcal{O}_K$.

Let $q$ be a prime, split for $d$ in the sense of the [previous section](/entry/exists-m-chart/). A point $t \in \mathbb{C}$ is *prime to $q$* if $s t \in \mathcal{O}_K$ for some integer $s > 0$ prime to $q$. Fix a field isomorphism $\iota : \mathbb{C} \to \mathbb{C}_q$ and $\omega \in \mathbb{C}_q$. For $G$ holomorphic at $0$ write $\widehat G = \iota(\mathrm{tay}(G))(\omega \log(1 + X)) \in \mathbb{C}_q[[X]]$, as in the previous section. A series is *bounded by $B$* if all its coefficients have absolute value at most $B$.

**Definition 4.3.2.** The pair $(\iota, \omega)$ satisfies the *theta laws* for $\theta$ if the following hold.
1. For every $t$ prime to $q$, the series $\widehat{U_t\theta}$ is bounded by $1$.
2. Let $t, y \in \mathbb{C}$ and $n, s \in \mathbb{N}$ with $s$ prime to $q$ and $st \in \mathcal{O}_K$, and let $y = s v / q^n$ with $v \in \mathcal{O}_K$ and $\|\iota(\bar v)\| \leq q^{-2n}$. Then $\iota(\kappa(1, y))^{q^n} = 1$, and $\widehat{W_y U_t \theta}$ is obtained from $\widehat{U_t\theta}$ by the shift that corresponds to multiplication by $\zeta = \iota(\kappa(1, y))$ in the multiplicative variable $1 + X$.
3. Let $a, m \in \mathbb{N}$, $c_1, \dots, c_m \in \mathbb{C}_q$, $s_1, \dots, s_m$ and $t$ prime to $q$, and $B \in \mathbb{R}$. If $\sum_j c_j (\widehat{U_{s_j}\theta})^a$ is bounded by $B$, then $\sum_j c_j (\widehat{U_t U_{s_j}\theta})^a$ is bounded by $B$.

The shift in clause 2 sends $\sum_m f_m X^m$ to the series with coefficients $\sum_m f_m \binom{m}{n} \zeta^n (\zeta - 1)^{m-n}$. It is $f(X) \mapsto f(\zeta(1 + X) - 1)$. So clause 2 says that translation by a $q$-power torsion point acts on the chart as multiplication by a root of unity in $\hat{\mathbb{G}}_m$.

### Theta functions in several variables

**Definition 4.3.3.** A *setup* of dimension $g$ consists of a prime $d$, a matrix $H \in M_g(\mathbb{C})$ and a subgroup $\Lambda \subseteq \mathbb{C}^g$. Put $h(z, x) = \sum_{i,j} z_i H_{ij} \bar x_j$ and $\beta(z, x) = \frac{\sqrt d}{2} h(z, x)$. The setup is *admissible* if $d \equiv 7 \pmod{16}$, $H$ is positive definite, $\Lambda$ is discrete and spans $\mathbb{C}^g$ over $\mathbb{R}$, $w \Lambda \subseteq \Lambda$, $\beta(\Lambda, \Lambda) \subseteq \mathcal{O}_K$, and $\Lambda$ equals its dual $\{y : \operatorname{Im} h(x, y) \in \mathbb{Z} \text{ for all } x \in \Lambda\}$.

For $x \in \mathbb{C}^g$ and $F : \mathbb{C}^g \to \mathbb{C}$ define $U_x$, $W_x$ and $\kappa$ by the formulas above with $h$ in place of $h_1$, and with the factor $e^{\pi i \operatorname{Re}\beta(x, x)}$ in $W_x$. A smooth function $e$ is a *theta function of the setup* if $W_x e = e$ for all $x \in \Lambda$. A point $t$ is *prime to $q$* if $s t \in \Lambda$ for some integer $s > 0$ prime to $q$. A vector is a *rational direction* if a positive multiple lies in $\Lambda$, and an *algebraic direction* if it is a combination of elements of $\Lambda$ with coefficients in $\overline{\mathbb{Q}}$.

**Definition 4.3.4.** Let $\delta \in \mathbb{C}$. A function $e$ has *algebraic jets for $\delta$* if the $k$-th derivative of $e$ at $0$ in the directions $\delta^{-1} y_1, \dots, \delta^{-1} y_k$ lies in $\overline{\mathbb{Q}}$ for all $k$ and all rational directions $y_j$.

**Definition 4.3.5.** A family $b_1, \dots, b_r \in \Lambda$ is a *basis prime to $q$* if it is $\mathcal{O}_K$-linearly independent, and for each $y \in \Lambda$ some integer $s$ prime to $q$ makes $s y$ an $\mathcal{O}_K$-combination of the $b_i$.

Fix a ring homomorphism $\lambda : \overline{\mathbb{Q}} \to \mathbb{C}_q$, and extend it to $\mathbb{C}$ by $0$ outside $\overline{\mathbb{Q}}$. For $n \geq 0$ and $a \in \mathbb{Z}_q^r$ let $\bar a \in \{0, \dots, q^n - 1\}^r$ be the reduction modulo $q^n$, and put $v_n(a) = \sum_i \bar a_i b_i$. For $\varepsilon \in \mathbb{C}$ and $y \in \{0, \dots, q^n - 1\}^r$ put $\tilde y = \frac{\varepsilon}{q^n} \sum_i y_i b_i$. For $\Omega \in \mathbb{C}_q$ and a direction $u$ put
$$P_u(a) = \Omega^{-1} \sum_{i=1}^r a_i\, \lambda(\beta(u, b_i)).$$

**Definition 4.3.6.** An element $\varepsilon \in \mathcal{O}_K$ is an *idempotent of level $m$* if $\|\lambda(\varepsilon) - 1\| \leq q^{-m}$ and $\|\lambda(\bar\varepsilon)\| \leq q^{-m}$.

**Definition 4.3.7.** A continuous linear form $\mu$ on $C(\mathbb{Z}_q^r, \mathbb{C}_q)$ has the *moment property* for $G$ at the translation $t$ if the following holds. Let $n, m \geq 0$ with $2n \leq m$, let $\varepsilon$ be an idempotent of level $m$ with $\operatorname{Im} h(\varepsilon b_i, t) \in \mathbb{Z}$ for all $i$, let $y \in \{0, \dots, q^n - 1\}^r$, and let $u_1, \dots, u_k$ be algebraic directions. Let $f \in C(\mathbb{Z}_q^r, \mathbb{C}_q)$ with
$$f(a) = \lambda\big(\kappa(v_n(a), \tilde y)\big) \prod_{j=1}^k P_{u_j}(a).$$
Then the $k$-th derivative $J$ of $W_{\tilde y} G$ at $0$ in the directions $\delta^{-1}u_1, \dots, \delta^{-1}u_k$ lies in $\overline{\mathbb{Q}}$, and $\lambda(J) = \mu(f)$.

So $\mu$ is a measure on $\mathbb{Z}_q^r$ whose moments, twisted by characters of $(\mathbb{Z}/q^n)^r$, are the algebraic jets of the torsion translates of $G$.

### The theorem

**Theorem 4.3.8 (moments of theta translates).** Let $d$ be a prime with $d \equiv 7 \pmod{16}$, and let $q$ be a prime split for $d$. Let $\theta$ be a CM theta function for $d$, let $\delta \in \mathbb{C}$ with $\delta \neq 0$, let $\lambda : \overline{\mathbb{Q}} \to \mathbb{C}_q$ be a ring homomorphism, let $\iota : \mathbb{C} \to \mathbb{C}_q$ be a field isomorphism that extends $\lambda$, and let $\Omega \in \mathbb{C}_q$ with $\|\Omega\| = 1$. Assume:
1. for every field isomorphism $\iota' : \mathbb{C} \to \mathbb{C}_q$ there is $\Omega' \in \mathbb{C}_q$ with $\|\Omega'\| = 1$ such that $(\iota', \Omega'/\iota'(\delta))$ satisfies the theta laws for $\theta$;
2. $(\iota, \Omega/\iota(\delta))$ satisfies the theta laws for $\theta$.

Let $g \geq 1$, let $(d, H, \Lambda)$ be an admissible setup, let $b_1, \dots, b_r$ be a basis prime to $q$, and let $e$ be a theta function of the setup with algebraic jets for $\delta$. Then there is a real number $N$ with the following property. For every $t$ prime to $q$ there is a continuous linear form $\mu$ on $C(\mathbb{Z}_q^r, \mathbb{C}_q)$ with $\|\mu\| = N$ that has the moment property for $U_t e$ at the translation $t$.

Lean: `GlobalTheory.MomOne.Translates.moments_of_translates`.

*Proof.* Step 1 (arithmetic at $q$). Since $q$ splits, $q\mathcal{O}_K = \mathfrak{q}\bar{\mathfrak{q}}$ with $\mathfrak{q} \neq \bar{\mathfrak{q}}$, and $\mathcal{O}_K \otimes \mathbb{Z}_q \cong \mathbb{Z}_q \times \mathbb{Z}_q$. This gives the idempotents of every level, and it identifies the completion of $\mathcal{O}_K$ at $\mathfrak{q}$ with $\mathbb{Z}_q$.

Step 2 (an orthogonal frame). Since $\Lambda$ is self-dual, there are $x_1, \dots, x_g \in \Lambda$ and integers $a_i > 0$ prime to $q$ with $\beta(x_i, x_j) = a_i$ for $i = j$ and $0$ otherwise.

Step 3 (theta in the frame). There are $m$, algebraic numbers $r_1, \dots, r_m$ and points $t_{ji}$ prime to $q$ with
$$e\Big(\sum_i z_i x_i\Big) = \sum_{j=1}^m r_j \prod_{i=1}^g \big(U_{t_{ji}}\theta(z_i)\big)^{a_i}$$
for all $z \in \mathbb{C}^g$. The product of translates of $\theta$ is a theta function of the setup. The space of theta functions of the setup is one-dimensional, so $e$ is a constant multiple of it. The constant is algebraic, because both sides have algebraic jets and $e \neq 0$. The jets of the products of translates are algebraic by hypothesis 1: an algebraic number is one whose images under all field isomorphisms $\iota'$ are bounded in a uniform way, and the theta laws for every $\iota'$ give such bounds.

Step 4 (operators in coordinates). The operators $U_x$, $W_x$ and the pairing $\kappa$ of the setup, written in the frame coordinates, are products of the one-variable operators in each coordinate, with the forms $a_i h_1$.

Step 5 (a frame change over $\mathbb{Z}_q$). The frame $x_i$ and the basis $b_i$ generate the same lattice after tensoring with $\mathbb{Z}_q$. So there is an invertible $\mathbb{Z}_q$-linear change of variables $T$ from the coordinates of $b$ to those of $x$.

Step 6 (product measures). In one variable, the theta laws turn $\widehat{U_t\theta}$ into a bounded series in $X$, which is the Amice transform of a measure on $\mathbb{Z}_q$ with norm at most $1$. Clause 2 says that twisting by a character of $\mathbb{Z}/q^n$ corresponds to translation by a torsion point. Products and powers of such measures, and the finite sum of Step 3 with coefficients $\lambda(r_j)$, give a measure for $e$ in the frame coordinates. Clause 3 bounds the norm of the measure for the translate $U_t e$ by a constant $N$ that does not depend on $t$.

Step 7 (the cocycle). Translations compose up to a factor: $U_x U_y = c(x, y) U_{x+y}$ with an explicit root of unity $c(x, y)$. With $s = (s_0 \prod_i a_i)^{\varphi(q^n)} \equiv 1 \pmod{q^n}$, the operator $W_{\tilde y}$ agrees with the operator of a lift of $\tilde y$ that is compatible with the frame. The pairings $\kappa(v_n(a), \tilde y)$ are computed in the frame by the torsion pairing.

Step 8 (conclusion). The measure of Step 6, pulled back along the change of variables $T$ of Step 5, is the form $\mu$. It has the same norm $N$, because $T$ is an isometry of $\mathbb{Z}_q^r$. Steps 4 and 7 show that it has the moment property for $U_t e$. $\square$

**Remark 4.3.9 (Formalization).** The statement asks for $\|\mu\| = N$, not $\|\mu\| \leq N$. All hypotheses of the theorem are used. Each step is a lemma of its own, in the modules imported by [CmLatticeTranslationOperatorEqPhaseMulNegComp.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/CmLatticeTranslationOperatorEqPhaseMulNegComp.lean#L288).
