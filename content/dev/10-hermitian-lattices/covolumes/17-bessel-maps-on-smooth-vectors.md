---
title: Bessel maps on smooth vectors
decls:
  - GlobalTheory.T.exists_continuous_besselMap_smoothVectors
  - GlobalTheory.SgInf.exists_besselExt
  - GlobalTheory.T.exists_besselMap_rankOne_factorisation_translateSpan
  - GlobalTheory.SgInf.exists_isEll_DD
  - GlobalTheory.Amp.SchurNorm.exists_isEll_smul
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Bessel maps on smooth vectors

The archimedean amplitude of a term is an integral of a rank one operator built from two Bessel functions of a discrete series representation. To bound it we need a Bessel functional of rank one: a single map $\ell$ from smooth vectors to the finite-dimensional space $W_p$ such that the Bessel form $\beta(u, u')$ is the rank one operator $\ell(u) \otimes \ell(u')^*$. This section constructs $\ell$. First every Bessel form, evaluated at a fixed second vector, is the restriction of a continuous Bessel map on smooth vectors. Then multiplicity one and a positivity argument give the rank one factorization. Finally a given Bessel map is identified with a multiple of $\ell$, with the size of the multiple fixed by its $L^2$ norm. These results feed the [Hilbert-Schmidt bounds](/entry/lintegral-hs-norm-sq-amp-j-le/) of the next section, which are used in the step [HypsAlt is nonempty from the closed bound](/step/nonempty-hyps/).

### The archimedean setting

Let $k, r \ge 0$, $n = 2r + k + 1$, and let $G = U(H_{k,r}) \subseteq M_n(\mathbb{C})$ be the unitary group of the model Hermitian form, with the real unipotent radical $N = N_{k,r}$ of [Section 2.16.3](/entry/covolume-n/). Write $\|g\|$ for the operator norm of a matrix $g$ on $\mathbb{C}^n$.

**Definition 2.17.1 (Standard representation data).** Let $\sigma$ be a map from $G$ to the bounded operators on a complex Hilbert space $H$, let $w \in H$, $a \in \mathbb{R}$, $\mu_G$ a measure and $d \in \mathbb{R}$. For $u, v \in H$ write $c_{u,v}(g) = \langle v, \sigma(g) u \rangle$ for the matrix coefficient, and let $D(w)$ be the span of the translates $\sigma(g) w$, $g \in G$. The tuple $(\sigma, w, a, \mu_G, d)$ is *standard* if:

1. $k \ge 1$, $\sigma$ is an irreducible unitary representation of $G$, and $\|w\| = 1$;
2. $\mu_G$ is a Haar measure on $G$;
3. Schur orthogonality holds with formal degree $d > 0$: for all $v, w_1, v', w'_1 \in H$,
$$\int_G c_{v,w_1}(g)\, \overline{c_{v',w'_1}(g)}\, d\mu_G(g) = \frac{\langle v', v\rangle \langle w_1, w'_1 \rangle}{d};$$
4. $a \ge 2 n^5$, and for $u, v \in D(w)$ there is $C$ with $|c_{u,v}(g)| \le C \|g\|^{-a}$ on $G$.

It is *standard and smooth* if also $w$ is a smooth vector: $g \mapsto \sigma(g) w$ is the restriction of a smooth map on $M_n(\mathbb{C})$.

Condition (3) says that $\sigma$ is square integrable with formal degree $d$; condition (4) is a strong decay of the matrix coefficients of $D(w)$, as for a discrete series representation with large parameter.

**Definition 2.17.2 (Side data and the Bessel form).** Let $z \in \mathbb{C}^n$ be a vector of the reduced space with positive norm $T(z) > 0$. Let $U_z \subseteq G$ be its stabilizer group and $S_z = U_z N$ the Bessel subgroup. Side data $(z, \pi, \mu_S)$ consist of a unitary representation $\pi$ of $U_z$ on a finite-dimensional inner product space $W_p$ and a Haar measure $\mu_S$ on $S_z$; they are *irreducible* if $\pi$ is irreducible and $W_p \ne 0$. For $c \in \mathbb{C}^r$ let $\psi = \psi_{z,c}$ be the generic character of $N$,
$$\psi(g) = \exp\Big(i\, \operatorname{Re} \sum_{a < r} c_a\, \ell_a(z, g)\Big),$$
and for $s = h m$ with $h \in U_z$ the middle block of $s$ and $m \in N$ put $\Pi(s) = \psi(m)\, \pi(h)$. The *Bessel form* is
$$\beta(u, u') = \int_{S_z} c_{u,u'}(s)\, \Pi(s^{-1})\, d\mu_S(s) \in \operatorname{End}(W_p).$$

**Definition 2.17.3 (Smooth Bessel map, multiplicity one).** A *smooth Bessel map* is a map $B \colon H \to W_p$ that is additive and linear on smooth vectors, satisfies
$$B(\sigma(h m) v) = \psi(m)\, \pi(h)\, B(v) \qquad (h \in U_z,\ m \in N,\ v \text{ smooth}),$$
and is bounded by a finite sum of norms of derivatives $\|d\sigma(X_1 \cdots X_j) v\|$ along the Lie algebra. The data have *multiplicity one* if for any two smooth Bessel maps $B$, $B'$ there is $\lambda \in \mathbb{C}$ with $B = \lambda B'$ or $B' = \lambda B$ on smooth vectors.

**Definition 2.17.4 (Rank one Bessel functional).** A map $\ell \colon H \to W_p$ is a *rank one Bessel functional* on $D(w)$ if $\ell$ is a smooth Bessel map, $\ell(u) \ne 0$ for some $u \in D(w)$, and for all $u, u' \in D(w)$,
$$\beta(u, u') = \ell(u) \otimes \ell(u')^*, \qquad \text{that is,} \quad \beta(u, u')\xi = \langle \ell(u'), \xi\rangle\, \ell(u).$$

We also use two measures. A measure $\nu$ on $G$ is a *quotient measure* for $(\mu_G, \mu_S)$ if $\int_G f\, d\mu_G = \int \int_{S_z} f(s x)\, d\mu_S(s)\, d\nu(x)$ for every measurable $f \ge 0$. The Bessel model is *nonvanishing* if there is a measurable $W \colon G \to W_p$ with $W(h m g) = \psi(m) \pi(h) W(g)$, with finite and nonzero $L^2$ norm for $\nu$, and fixed by right convolution with the normalized matrix coefficient of $w$.

**Theorem 2.17.5 (Bessel maps through the Bessel form).** Let $(\sigma, w, a, \mu_G, d)$ be standard, let $(z, \pi, \mu_S)$ be side data, let $c \in \mathbb{C}^r$, and let $w$ be smooth. For every $v \in D(w)$ and $\xi \in W_p$ there is a smooth Bessel map $\ell$ with
$$\ell(u) = \beta(u, v)\, \xi \qquad \text{for all } u \in D(w).$$

Lean: `GlobalTheory.SgInf.exists_besselExt` (also `GlobalTheory.T.exists_continuous_besselMap_smoothVectors`, a second name).

*Proof.* The function $A_u(x) = \beta(\sigma(x) u, v)\xi$ on $G$ is defined for $u \in D(w)$. The map $u \mapsto A_u$ extends to a bounded linear map $T$ from $H$ to functions on $G$ that is equivariant for right translation by $G$ and for left translation by $S_z$ through $\Pi$; this uses the decay of the matrix coefficients and Schur orthogonality. The smooth vectors are dense and invariant. For a smooth vector $u$, the function $T u$ agrees almost everywhere with a continuous function $F_u$, and $\|F_u(1)\|$ is bounded by a finite sum of norms of derivatives of $u$; this is a Sobolev bound on $G$. Put $\ell(u) = F_u(1)$ for smooth $u$, and $\ell(u) = 0$ otherwise. Two continuous functions that agree almost everywhere for a Haar measure agree on $G$. This gives additivity and linearity of $\ell$ on smooth vectors, and, with the equivariance of $T$ and the unimodularity of $G$, the Bessel equivariance $\ell(\sigma(hm)u) = \psi(m)\pi(h)\ell(u)$. For $u \in D(w)$ the function $A_u$ is continuous, so $F_u = A_u$ and $\ell(u) = A_u(1) = \beta(u, v)\xi$. $\square$

**Theorem 2.17.6 (Rank one factorization of the Bessel form).** Let $(\sigma, w, a, \mu_G, d)$ be standard with $w$ smooth, let $(z, \pi, \mu_S)$ be side data with multiplicity one, let $c \in \mathbb{C}^r$, let $\nu$ be a quotient measure, and let the Bessel model be nonvanishing. Then a rank one Bessel functional on $D(w)$ exists.

Lean: `GlobalTheory.SgInf.exists_isEll_DD` (also `GlobalTheory.T.exists_besselMap_rankOne_factorisation_translateSpan`, a second name).

*Proof.* First, $\beta$ is not zero on $D(w)$. If it were, the Bessel functional formula for the standard side would write each value $W(y)$ of the nonvanishing function as an integral of values of $\beta$ on $D(w)$, so $W$ would vanish on $G$ and its $L^2$ norm would be $0$. Choose $u_1, v_1 \in D(w)$ and $\xi_1$ with $\beta(u_1, v_1)\xi_1 \ne 0$, and let $\ell_0$ be the smooth Bessel map of the [Theorem 2.17.5](/entry/exists-bessel-ext/) for $(v_1, \xi_1)$. For any $v \in D(w)$ and $\xi$, the Theorem gives a smooth Bessel map $\ell$ with $\ell(u) = \beta(u, v)\xi$ on $D(w)$. By multiplicity one, $\ell$ and $\ell_0$ are proportional; the case $\ell_0 = 0 \cdot \ell$ is excluded since $\ell_0(u_1) \ne 0$. So $\beta(u, v)\xi = b(v, \xi)\, \ell_0(u)$ for a scalar $b(v, \xi)$. The kernel $\beta$ is Hermitian, $\beta(u, v)^* = \beta(v, u)$, and positive, $\langle \xi, \beta(v, v)\xi\rangle \ge 0$; the second fact is a norm identity for Bessel coefficients on the quotient. A Hermitian positive operator kernel whose columns lie on the line of $\ell_0$ is of the form $\ell \otimes \ell^*$ with $\ell = t \ell_0$ for some $t \in \mathbb{C}$. Then $\ell$ is a smooth Bessel map, and it is not zero on $D(w)$. $\square$

**Proposition 2.17.7 (A Bessel map is a multiple of the rank one functional).** Let $v_0 \in H$ be nonzero and $w = v_0 / \|v_0\|$. Assume that $(\sigma, w, a, \mu_G, d)$ is standard and smooth, that $(z, \pi, \mu_S)$ are irreducible side data with multiplicity one, and that $\nu_S$ is a quotient measure. Let $B$ be a smooth Bessel map, let $c_0 > 0$, and assume
$$\int \|B(\sigma(g) v_0)\|^2\, d\nu_S(g) = c_0 \dim W_p,$$
and that for every smooth $v$ the $L^2$ norm of $g \mapsto B(\sigma(g)v)$ times $\|v_0\|^2$ equals the $L^2$ norm of $g \mapsto B(\sigma(g)v_0)$ times $\|v\|^2$. Then there are a rank one Bessel functional $\ell$ on $D(w)$ and $t \in \mathbb{C}$ with
$$|t|^2 = c_0\, d \dim W_p, \qquad B(\sigma(g) v_0) = t\, \ell(\sigma(g) w) \quad (g \in G).$$

Lean: `GlobalTheory.Amp.SchurNorm.exists_isEll_smul`.

*Proof.* The smooth vectors are dense and invariant, and since $B \ne 0$ the Bessel model is nonvanishing: the function $g \mapsto B(\sigma(g) v_0)$ is a nonzero square integrable fixed vector. So the [Theorem 2.17.6](/entry/exists-is-ell-dd/) gives a rank one functional $\ell$ on $D(w)$. By multiplicity one, $B = \lambda \ell$ or $\ell = \lambda B$ on smooth vectors; as $\ell \ne 0$ on $D(w)$ and $B \ne 0$, in both cases $B = t' \ell$ for some $t' \in \mathbb{C}$. Put $t = t' \|v_0\|$; then $B(\sigma(g) v_0) = t\, \ell(\sigma(g) w)$ by linearity. To compute $|t|$, use the projector property of the Bessel model on a line: the $L^2$ norm of $g \mapsto \ell(\sigma(g) w)$ for $\nu_S$ is $\|w\|^2 \dim W_p / d = \dim W_p / d$, because the Bessel form of $\ell$ is $\ell \otimes \ell^*$ and Schur orthogonality has formal degree $d$. So
$$c_0 \dim W_p = |t|^2\, \frac{\dim W_p}{d},$$
and $|t|^2 = c_0\, d \dim W_p$. $\square$

**Remark 2.17.8 (Formalization).** The rank one condition is `IsEll`, the Bessel form is `be` and multiplicity one is `MultOne` ([MatrixOfBesselTwoSidedAction.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/MatrixOfBesselTwoSidedAction.lean#L106)). The continuity bound of a smooth Bessel map is `IsCWCont`, and the nonvanishing condition `NonVan` uses the convolution `rconv` with `eFun`; neither is unfolded here. In the first Theorem, the map $\ell$ is set to $0$ off the smooth vectors, so it is a Bessel map only on smooth vectors, as the definition asks. The hypothesis on the $L^2$ norms of all smooth $v$ in the Proposition is the proportionality that the projector argument needs.
