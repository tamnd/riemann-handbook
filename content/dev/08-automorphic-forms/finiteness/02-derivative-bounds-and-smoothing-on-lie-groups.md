---
title: Derivative bounds and smoothing on Lie groups
decls:
  - GlobalTheory.derivWord_le_integral_of_aeval_casimir_eq_zero
  - GlobalTheory.T.exists_compact_derivWord_bound_of_aeval_casimir
  - GlobalTheory.HCA.solG_smFn
  - GlobalTheory.T.laplacePolynomialKernel_derivativeWords_family
  - GlobalTheory.HCA.exists_alpha_convolution
  - GlobalTheory.T.exists_smooth_convolution_eq_derivative
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Derivative bounds and smoothing on Lie groups

Let $G$ be a real Lie group and $\Delta$ a Laplace operator on $G$. A smooth function $f$ that is killed by a monic polynomial in $\Delta$ behaves like a solution of an elliptic equation: each of its derivatives at a point is bounded by the integral of $|f|$ over a fixed compact set. This section proves that bound, and then a theorem of Harish-Chandra: for each differential operator $D$ there is one smooth function $\alpha$ with compact support such that $f * \alpha = D f$ for all such $f$. With $D = 1$ this says that $f$ reproduces itself under convolution with $\alpha$. This is the form in which the finiteness theorem for automorphic forms on $\mathrm{GL}_a$ uses the condition on the center of the enveloping algebra, through [the finiteness of forms of one type](/entry/finite-dimensional-single/).

### The setting

Let $\mathcal{A}$ be a finite-dimensional real Banach algebra, $G$ a subgroup of the unit group $\mathcal{A}^\times$, and $\mathfrak{g} \subseteq \mathcal{A}$ a real subspace. We assume that $\exp X \in G$ for each $X \in \mathfrak{g}$, and that there is an open neighbourhood $U$ of $0$ in $\mathcal{A}$, on which $\exp$ is a local homeomorphism, with $X \in \mathfrak{g}$ whenever $X \in U$ and $\exp X \in G$. Then the maps $X \mapsto g \exp X$ for $X$ near $0$ in $\mathfrak{g}$ are charts of a Lie group structure on $G$ with Lie algebra $\mathfrak{g}$. For example, $\mathcal{A} = M_n(\mathbb{C})$, $G = \mathrm{GL}_n(\mathbb{C})$ and $\mathfrak{g} = M_n(\mathbb{C})$ as a real space; or $G = \mathrm{U}(p,q)$ and $\mathfrak{g} = \mathfrak{u}(p,q)$. A function $f : G \to \mathbb{C}$ is *smooth* if it is smooth for this structure.

**Definition 1.2.1 (Right derivatives and the Laplace operator).** For $X \in \mathfrak{g}$ and a smooth $f$, the *right derivative* is
$$R(X) f(g) = \frac{d}{dt} f(g \exp tX) \Big|_{t = 0}.$$
For a word $w = (X_1, \dots, X_k)$ in $\mathfrak{g}$ put $R(w) = R(X_1) \cdots R(X_k)$, with $R(\varnothing) = 1$. Let $b_1, \dots, b_d$ be a basis of $\mathfrak{g}$. The *Laplace operator* of the basis is $\Delta = \sum_{i=1}^d R(b_i)^2$. For a monic polynomial $P \in \mathbb{C}[T]$, let $S_P$ be the space of smooth $f : G \to \mathbb{C}$ with $P(\Delta) f = 0$.

The operators $R(X)$ commute with left translations $f \mapsto f(x\,\cdot)$, so $S_P$ is stable under left translation. The operator $\Delta$ is elliptic of order $2$, and $P(\Delta)$ is elliptic of order $2 \deg P$. For $G = \mathbb{R}^d$ with the standard basis, $\Delta$ is the usual Laplacian and $S_{T}$ is the space of harmonic functions. For a finite-dimensional space of smooth functions that $\Delta$ preserves, the minimal polynomial of $\Delta$ on it is a monic $P$ with the space inside $S_P$. This is how $S_P$ arises for automorphic forms: a form that is finite under the center of the enveloping algebra lies in some $S_P$.

For $t \in \mathbb{R}^d$ put $e(t) = \exp(t_1 b_1) \cdots \exp(t_d b_d)$. Near $t = 0$ this is a chart of $G$ at $1$.

### The derivative bound

**Theorem 1.2.2 (Derivatives of solutions of $P(\Delta) f = 0$).** Let $P$ be monic and $\mu$ a Haar measure on $G$. There is a compact set $K \subseteq G$ with the following property. For each word $w$ in $\mathfrak{g}$ there is $C$ such that
$$|R(w) f(1)| \le C \int_K |f|\, d\mu$$
for every $f \in S_P$.

Lean: `GlobalTheory.derivWord_le_integral_of_aeval_casimir_eq_zero` (also `GlobalTheory.T.exists_compact_derivWord_bound_of_aeval_casimir`, a second name).

*Proof.* We use four facts.

1. (Interior estimate.) There is a compact $K_c \subseteq G$ such that for each word $w$ there is $C_w \ge 0$ with $|R(w) f(g)| \le C_w M$ whenever $f \in S_P$, $g \in G$ and $|f(gy)| \le M$ for all $y \in K_c$. This is the interior estimate for the elliptic operator $P(\Delta)$, made uniform in $g$ by left translation.
2. (Comparison with Haar measure.) There is $\rho > 0$ such that for each compact $K_1$ there are $C_0 \ge 0$ and a compact $K_2$ with $\int_{|t| \le \rho} |\varphi(e(t) y)|\, dt \le C_0 \int_{K_2} |\varphi|\, d\mu$ for every continuous $\varphi$ and every $y \in K_1$. This holds because $t \mapsto e(t) y$ has a smooth Jacobian with respect to $\mu$ on the ball, uniformly in $y \in K_1$.
3. (A Sobolev representation.) For each $\varepsilon > 0$ there are words $w_1, \dots, w_N$ and continuous functions $\kappa_1, \dots, \kappa_N$ on $\mathbb{R}^d$ with support in the ball of radius $\varepsilon$, such that every smooth $f$ satisfies $f(g) = \sum_i \int \kappa_i(t)\, R(w_i) f(g\, e(t))\, dt$ for all $g$.
4. (Left smoothing.) For a continuous $\kappa$ with compact support and a smooth $f$, the function $v(y) = \int \kappa(t) f(e(t) y)\, dt$ is smooth, and $T v(y) = \int \kappa(t)\, (Tf)(e(t) y)\, dt$ for every $T$ in the algebra generated by the $R(X)$.

Take $K_c$ from 1 and $\rho$ from 2, and apply 2 to $K_1 = K_c$; this gives $C_0$ and $K = K_2$. Apply 3 with $\varepsilon = \rho$. Let $S_i$ be a bound for $|\kappa_i|$. Fix $w$ and $f \in S_P$. By 3 applied to the smooth function $R(w) f$ at $g = 1$,
$$R(w) f(1) = \sum_{i=1}^N \int \kappa_i(t)\, R(w_i) R(w) f(e(t))\, dt.$$
Let $v_i$ be the left smoothing of $f$ by $\kappa_i$, as in 4. Since $P(\Delta)$ lies in the algebra generated by the $R(X)$, 4 gives $P(\Delta) v_i = 0$, so $v_i \in S_P$. Also by 4 with $T = R(w_i) R(w)$ at $y = 1$, the $i$-th term is $R(w_i w) v_i(1)$. For $y \in K_c$,
$$|v_i(y)| \le S_i \int_{|t| \le \rho} |f(e(t) y)|\, dt \le S_i C_0 \int_K |f|\, d\mu,$$
by 2. So 1 with $g = 1$ and the word $w_i w$ gives $|R(w_i w) v_i(1)| \le C_{w_i w} S_i C_0 \int_K |f|\, d\mu$. Sum over $i$ and put $C = \sum_i C_{w_i w} S_i C_0$. $\square$

The constant $C$ depends on $w$, but the compact set $K$ does not. This is what the next step needs.

### Smooth families of functionals

**Definition 1.2.3 (Smooth family of functionals).** Let $S$ be a space of continuous functions on $G$, stable under left translation, and $K \subseteq G$ compact. A *smooth family* on $S$ with support $K$ is a family of maps $\Lambda_l : S \to \mathbb{C}$, indexed by the finite words $l$ in $\{1, \dots, d\}$, such that

1. each $\Lambda_l$ is linear;
2. for each $l$ there is $C$ with $|\Lambda_l f| \le C \int_K |f|\, d\mu$ for all $f \in S$;
3. for each $l$, each $i$ and each $f \in S$, the function $t \mapsto \Lambda_l\big(f(\exp(t b_i)\, \cdot)\big)$ has derivative $\Lambda_{(i, l)} f$ at $t = 0$.

Condition 3 says that $\Lambda_{(i,l)}$ is the derivative of $\Lambda_l$ along the left action of $\exp(t b_i)$. The model is $\Lambda_l f = \int f \alpha_l\, d\mu$ with $\alpha_l$ smooth with support in $K$; the next lemma is the converse for $\Lambda_\varnothing$.

**Lemma 1.2.4 (Smooth functionals are integrals).** Let $\mu$ be a Haar measure, $S$ a space of continuous functions stable under left translation, $K$ compact, and $(\Lambda_l)$ a smooth family on $S$ with support $K$. Then there is a smooth $\alpha$ with compact support such that $\int f \alpha\, d\mu = \Lambda_\varnothing f$ for all $f \in S$.

Lean: `GlobalTheory.T.first_functional_integral_smooth_compact` (also `GlobalTheory.HCA.smFn_nil_eq_integral_smooth`, a second name).

*Proof.* First, there are smooth families $\Lambda'^{(1)}, \dots, \Lambda'^{(N)}$ on $S$ with support $K$ and continuous $\kappa_m$ on $\mathbb{R}^d$ with small support such that
$$\Lambda_\varnothing f = \sum_{m=1}^N \int \kappa_m(t)\, \Lambda'^{(m)}_\varnothing\big(f(e(t)\, \cdot)\big)\, dt$$
for $f \in S$; this is a decomposition of Dixmier-Malliavin type, and it uses condition 3. Each $\Lambda'^{(m)}_\varnothing$ is bounded by a multiple of the $L^1(K)$ norm, so by the Hahn-Banach and Riesz theorems there is a bounded measurable $a_m$ with support in $K$ and $\Lambda'^{(m)}_\varnothing f = \int f a_m\, d\mu$. The measure $\kappa_m(t)\,dt$, carried to $G$ by $t \mapsto e(t)$, has a smooth density $\kappa'_m$ with compact support. Then $\alpha = \sum_m \kappa'_m * a_m$, with $(\kappa' * a)(z) = \int \kappa'(x) a(x^{-1} z)\, d\mu(x)$, is smooth with compact support, and Fubini gives $\int f \alpha\, d\mu = \sum_m \int \kappa'_m(x) \Lambda'^{(m)}_\varnothing(f(x\,\cdot))\, d\mu(x) = \Lambda_\varnothing f$. $\square$

**Proposition 1.2.5 (The derivatives at $1$ form a smooth family).** Let $P$ be monic and $\mu$ a Haar measure. Then every $f \in S_P$ is continuous, $S_P$ is stable under left translation, and there is a compact $K$ such that for each word $w_0$ in $\mathfrak{g}$ the family
$$\Lambda_l f = R(b_{l_1}) \cdots R(b_{l_k}) R(w_0) f(1), \qquad l = (l_1, \dots, l_k),$$
is a smooth family on $S_P$ with support $K$.

Lean: `GlobalTheory.HCA.solG_smFn` (also `GlobalTheory.T.laplacePolynomialKernel_derivativeWords_family`, a second name).

*Proof.* Smooth functions are continuous. Left translation by $g$ commutes with each $R(X)$, hence with $P(\Delta)$, so it maps $S_P$ to $S_P$. Take $K$ from [the derivative bound](/entry/deriv-word-le-integral-of-aeval-casimir-eq-zero/). Each $\Lambda_l$ is linear, since the $R(X)$ are linear. Condition 2 is the derivative bound for the word $(b_{l_1}, \dots, b_{l_k}) w_0$. For condition 3, left translation commutes with $R(w)$, so $\Lambda_l(f(\exp(t b_i)\,\cdot)) = R(b_l) R(w_0) f(\exp(t b_i))$, and its derivative at $t = 0$ is $R(b_i) R(b_l) R(w_0) f(1) = \Lambda_{(i,l)} f$. $\square$

### The reproducing function

**Theorem 1.2.6 (Harish-Chandra's convolution theorem).** Let $P$ be monic, $\mu$ a Haar measure on $G$, and $w$ a word in $\mathfrak{g}$. There is a smooth function $\alpha$ on $G$ with compact support such that
$$\int_G f(g y)\, \alpha(y)\, d\mu(y) = R(w) f(g)$$
for every $f \in S_P$ and every $g \in G$.

Lean: `GlobalTheory.HCA.exists_alpha_convolution` (also `GlobalTheory.T.exists_smooth_convolution_eq_derivative`, a second name).

*Proof.* By [the proposition](/entry/sol-g-sm-fn/) with $w_0 = w$, the family $\Lambda_l f = R(b_l) R(w) f(1)$ is smooth on $S_P$, which consists of continuous functions and is stable under left translation. The lemma above on smooth functionals gives a smooth $\alpha$ with compact support and $\int f \alpha\, d\mu = \Lambda_\varnothing f = R(w) f(1)$ for $f \in S_P$. Apply this to $f(g\,\cdot) \in S_P$: since left translation commutes with $R(w)$, the right side is $R(w) f(g)$. $\square$

With $w = \varnothing$ the theorem says that each $f \in S_P$ is reproduced by integration against one fixed $\alpha$. For automorphic forms on $\mathrm{GL}_a$ over a totally complex field, this is applied to the archimedean group $\mathrm{GL}_a(E \otimes \mathbb{R})$ in the next section, where it makes a space of forms equicontinuous.

**Remark 1.2.7 (Formalization).** The group is a subgroup of the units of a finite-dimensional real Banach algebra, and the Lie algebra is a subspace that $\exp$ maps into the group, with a local converse. The words are lists, and $R(w)$ is a right fold of the right derivatives. The four facts in the proof of the derivative bound are the statements of `GlobalTheory.T.exists_interior_estimate_deriv_word_polyLaplacian`, `GlobalTheory.T.exists_setIntegral_norm_prodExp_mul_le_haar`, `GlobalTheory.T.exists_sobolev_representation_prodExp'` and `GlobalTheory.T.leftSmoothing_prodExp_smooth_commute`; we read these statements, not their proofs, and the reasons given for facts 1 and 2 are the classical ones. In the lemma on smooth functionals we read the outline of the proof; its inputs (the decomposition, the density in $L^1(K)$, the smooth density of $\kappa_m$) are statements whose proofs we did not open. All the second names are proved by `first | exact @...` with the first name.
