---
title: Isotropic means of theta functions
decls:
  - GlobalTheory.T.isotropicIntegrals_determine_thetaMean_products
  - GlobalTheory.IsoMean.meanX_prod_zero_eq
  - GlobalTheory.IsoMean.meanX_prod_zero
  - GlobalTheory.T.isotropicMean_changes_by_scalar_of_trivial_action
  - GlobalTheory.IsoMean.mean_scalar
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Isotropic means of theta functions

A theta function on an adelic symplectic space can be averaged over an isotropic subspace. This section proves that such an average changes only by a scalar of absolute value $1$ when one applies the Weil representation of a pair $(g, h)$ that fixes the isotropic subspace and acts trivially modulo it on its orthogonal. The result is used in the step [EveryCharacter from the literature](/step/every-character-of-literature/), where the mean over an isotropic subspace is the constant term of a theta function along a unipotent radical. The main tool is that the products of two means are determined by the integrals of matrix coefficients over the isotropic subspace.

We fix the notation for the whole chapter. Let $F$ be a totally real number field, $E/F$ a CM extension with conjugation $a \mapsto \bar a$, and $\mathbb{A}_F$, $\mathbb{A}_E = \mathbb{A}_F \otimes_F E$ their adele rings. A *Hermitian space* $V$ of rank $n_V$ is $E^{n_V}$ with an invertible Hermitian Gram matrix $J_V$. Its adelic [unitary group](/learn/groups/#unitary-groups) is $G_V = U(V)(\mathbb{A}_F)$, with the subgroup $G_V(F)$ of rational points.

**Definition 8.1.1 (The symplectic space of a pair).** Let $V$ and $W$ be Hermitian spaces. Put $\mathbb{W} = \mathbb{W}_{V,W} = M_{n_W \times n_V}(\mathbb{A}_E)$, with the Hermitian form $h(x, y) = \operatorname{tr}(J_V^{-1} y^* J_W x)$ and the symplectic form
$$\langle x, y \rangle = \operatorname{tr}_{\mathbb{A}_E/\mathbb{A}_F}\bigl(\xi_0\, h(x, y)\bigr),$$
for a fixed $\xi_0 \in E$. The group $G_V \times G_W$ acts by $(g, h) \cdot x = h x g^{-1}$, and $\mathbb{W}(E) = M_{n_W \times n_V}(E)$ is the lattice of rational points.

This is the space $W \otimes V$ of the [reductive dual pair](/learn/theta/#reductive-dual-pairs) $(U(V), U(W))$, written in coordinates.

**Definition 8.1.2 (Heisenberg operators and theta functions).** Let $\psi$ be a character of $\mathbb{A}_F$. For $w_0 \in \mathbb{W}$ and a function $f$ on $\mathbb{W}$ put
$$\rho(w_0) f(w) = \psi\bigl(\tfrac12 \langle w, w_0 \rangle\bigr)\, f(w + w_0).$$
A *theta function* is a continuous function $f : \mathbb{W} \to \mathbb{C}$ with:

1. $f(\gamma + w) = \psi(-\tfrac12 \langle \gamma, w \rangle) f(w)$ for $\gamma \in \mathbb{W}(E)$;
2. $\rho(u) f = f$ for all $u$ in an open subgroup of $\mathbb{W}$ with zero archimedean component;
3. $t \mapsto f(w + L(t))$ is smooth for each continuous additive map $L : \mathbb{R}^k \to \mathbb{W}$ with values in the archimedean part.

The theta functions are the functions $\Theta(\varphi)$ of the [Schrödinger model](/learn/theta/#the-schrödinger-model) written on $\mathbb{W}$ itself: the first condition is the quasi-periodicity of a theta series, and the second says that $\varphi$ is fixed by a compact open subgroup at the finite places.

**Definition 8.1.3 (Weil datum).** A character $\psi$ of $\mathbb{A}_F / F$ is *standard* if $\psi_\infty(x) = \exp(-2\pi i \operatorname{tr} x)$. A *Weil datum* for $(V, W)$ is a standard $\psi$, two Hecke characters $\chi_V, \chi_W$ of $\mathbb{A}_E^\times / E^\times$ with $\chi_V|_{\mathbb{A}_F^\times} = \eta^{n_V}$ and $\chi_W|_{\mathbb{A}_F^\times} = \eta^{n_W}$ for the quadratic character $\eta$ of $E/F$, and a homomorphism $\omega : G_V \times G_W \to \operatorname{End}(\mathbb{C}^{\mathbb{W}})$ such that, for every theta function $f$:

1. $\omega(g, h) f$ is a theta function;
2. $\omega(g, h)\, \rho(w_0) f = \rho((g, h) \cdot w_0)\, \omega(g, h) f$;
3. $\omega(\gamma, \gamma') f(0) = f(0)$ for $\gamma \in G_V(F)$, $\gamma' \in G_W(F)$;
4. $(g, h) \mapsto \omega(g, h) f(w)$ is continuous;
5. $\int_{\mathcal{F}} |\omega(g, h) f|^2 = \int_{\mathcal{F}} |f|^2$ for each fundamental domain $\mathcal{F}$ of $\mathbb{W}(E)$ in $\mathbb{W}$;
6. at each split place, $\omega(g, h)$ acts on functionals invariant under the Heisenberg group at that place by $r \cdot \chi_W(\det g)^{-1} \chi_V(\det h)$, with $r > 0$.

This is the global [Weil representation](/learn/theta/#the-weil-representation) with the [splitting characters](/learn/theta/#splitting-characters) $(\chi_V, \chi_W)$, given by its properties. Condition 2 is the Stone-von Neumann covariance, condition 3 says that $f \mapsto f(0)$ is the automorphic functional, and condition 6 fixes the character at the split places.

Now fix $a, b \ge 0$, a matrix $P \in M_{n_W \times a}(E)$ of rank $a$ and a matrix $Q \in M_{b \times n_V}(E)$ of rank $b$. Put
$$\iota : M_{a \times b}(\mathbb{A}_E) \to \mathbb{W}, \qquad \iota(y) = P y Q,$$
and $Y = \iota(M_{a \times b}(\mathbb{A}_E))$. We assume that $Y$ is isotropic: $\langle \iota(y), \iota(y') \rangle = 0$ for all $y, y'$. Let $Y^\perp$ be the set of $x \in \mathbb{W}$ with $\langle x, Y \rangle = 0$. Let $\mu$ be a Haar measure on $M_{a \times b}(\mathbb{A}_E)$ and $\mathcal{Y}$ a fundamental domain for $M_{a \times b}(E)$ with $\mu(\mathcal{Y}) = 1$.

**Definition 8.1.4 (Isotropic mean).** The *isotropic mean* of a function $f$ on $\mathbb{W}$ is
$$m_f(x) = \int_{\mathcal{Y}} f(\iota(y) + x)\, d\mu(y), \qquad x \in \mathbb{W}.$$

For $x \in Y^\perp$ the phase of $\rho(x)$ is trivial on $Y$, so $\int_{\mathcal{Y}} \rho(x) f(\iota(y))\, d\mu(y) = m_f(x)$. When $Y$ is the unipotent radical of a parabolic subgroup in a mixed model, $m_f(0)$ is the constant term of the theta function along that radical.

**Theorem 8.1.5 (Isotropic integrals determine products of means).** Let $\psi$ be standard and let $F_1, F_1', F_2, F_2'$ be theta functions. Assume that for every Haar measure $\nu$ on $\mathbb{W}$, every fundamental domain $\mathcal{F}$ of $\mathbb{W}(E)$ and every $w \in Y^\perp$,
$$\begin{aligned} &\int \int_{\mathcal{F}} \rho(w + \iota(y)) F_1(u)\, \overline{F_1'(u)}\, d\nu(u)\, d\mu(y) \\ &\quad = \int \int_{\mathcal{F}} \rho(w + \iota(y)) F_2(u)\, \overline{F_2'(u)}\, d\nu(u)\, d\mu(y), \end{aligned}$$
where $y$ runs over all of $M_{a \times b}(\mathbb{A}_E)$. Then
$$m_{F_1}(0)\, \overline{m_{F_1'}(0)} = m_{F_2}(0)\, \overline{m_{F_2'}(0)}.$$

Lean: `GlobalTheory.T.isotropicIntegrals_determine_thetaMean_products` (also `GlobalTheory.IsoMean.meanX_prod_zero_eq`, the proof).

*Proof.* First choose a rational complement. There are $k \ge 0$ and $B_1, \dots, B_k \in \mathbb{W}(E)$ such that $\beta(z) = \sum_i z_i B_i$, for $z \in \mathbb{A}_E^k$, has these properties: $\beta(z) \perp Y$; every $x \in Y^\perp$ is $\beta(z) + \iota(y)$ for some $z, y$; the sum is direct; $\beta(z) + \iota(y)$ is rational only if $z$ and $y$ are; and $\psi(\langle \beta(z), \beta(c) \rangle) = 1$ for all $c \in E^k$ if and only if $z \in E^k$. So $\beta(\mathbb{A}_E^k)$ is a self-dual complement of $Y$ in $Y^\perp$ modulo $Y$. Let $\eta$ be a Haar measure on $\mathbb{A}_E^k$ and $\mathcal{Z}$ a fundamental domain for $E^k$.

Second, the integral of a matrix coefficient over $Y$ is an integral of means. There is $\kappa \neq 0$, independent of the theta functions, with
$$\int \int_{\mathcal{F}} \rho(\iota(y)) G\, \overline{G'}\, d\nu\, d\mu = \kappa \int_{\mathcal{Z}} m_G(\beta(z))\, \overline{m_{G'}(\beta(z))}\, d\eta(z)$$
for all theta functions $G, G'$. Now take $w = \beta(c)$ with $c \in E^k$. Since $\langle \beta(c), \iota(y) \rangle = 0$, the Heisenberg operators compose without a phase: $\rho(\beta(c) + \iota(y)) = \rho(\iota(y)) \rho(\beta(c))$. For a rational $\beta(c)$ the mean of $\rho(\beta(c)) G$ is $m_{\rho(\beta(c)) G}(x) = \psi(\langle x, \beta(c) \rangle) m_G(x)$ on $Y^\perp$. So the hypothesis becomes
$$\int_{\mathcal{Z}} \psi(\langle \beta(z), \beta(c) \rangle)\, \Phi(z)\, d\eta(z) = 0, \qquad c \in E^k,$$
with $\Phi(z) = m_{F_1}(\beta z) \overline{m_{F_1'}(\beta z)} - m_{F_2}(\beta z) \overline{m_{F_2'}(\beta z)}$, after we divide by $\kappa$.

Third, $\Phi$ is continuous and periodic under $E^k$, because the product $m_G \overline{m_{G'}}$ is invariant under rational translations in $\beta(E^k)$ (the two phases cancel). The quotient $\mathbb{A}_E^k / E^k$ is compact. The functions $z \mapsto \psi(\langle \beta(z), \beta(c) \rangle)$, $c \in E^k$, are continuous unitary characters of this quotient, they multiply as characters in $c$, and they separate points by the self-duality above. A continuous periodic function whose integrals against a separating group of characters all vanish is zero. So $\Phi = 0$, and $\Phi(0) = 0$ is the claim. $\square$

**Theorem 8.1.6 (Products of means under a pair that fixes the isotropic subspace).** Let $(\psi, \chi_V, \chi_W, \omega)$ be a Weil datum and $(g, h) \in G_V \times G_W$. Assume that $(g, h)$ fixes $Y$ pointwise and that $(g, h) \cdot x - x \in Y$ for every $x \in Y^\perp$. Then for all theta functions $f, f'$,
$$m_{\omega(g,h) f}(0)\, \overline{m_{\omega(g,h) f'}(0)} = m_f(0)\, \overline{m_{f'}(0)}.$$

Lean: `GlobalTheory.IsoMean.meanX_prod_zero`.

*Proof.* Apply the [Theorem 8.1.5](/entry/isotropic-integrals-determine-theta-mean-products/) to $F_1 = \omega(g,h) f$, $F_1' = \omega(g,h) f'$, $F_2 = f$, $F_2' = f'$; these are theta functions by condition 1 of a Weil datum. Its hypothesis is the invariance of the double integral
$$\int \int_{\mathcal{F}} \rho(w + \iota(y)) f\, \overline{f'}\, d\nu\, d\mu$$
under $(f, f') \mapsto (\omega(g,h) f, \omega(g,h) f')$ for $w \in Y^\perp$. By covariance, $\omega(g,h)$ moves $\rho(w + \iota(y))$ to $\rho((g,h)(w + \iota(y)))$, and $(g,h)(w + \iota(y)) = w + \iota(y + y_0)$ for some $y_0$; the translation $y \mapsto y + y_0$ preserves the Haar measure on the whole space, and the unitarity of $\omega$ on fundamental domains removes $\omega(g,h)$. $\square$

The following elementary fact turns equal products into a scalar.

**Lemma 8.1.7 (Scalars from products).** Let $X$ be a set and $\phi, \phi' : X \to \mathbb{C}$ with $\phi'(y) \overline{\phi'(x)} = \phi(y) \overline{\phi(x)}$ for all $x, y$. Then $\phi' = c \phi$ for some $c$ with $|c| = 1$.

*Proof.* Taking $x = y$ gives $|\phi'| = |\phi|$. If $\phi = 0$, take $c = 1$. Otherwise pick $x_0$ with $\phi(x_0) \neq 0$ and put $c = \phi'(x_0)/\phi(x_0)$; then $|c| = 1$, and the identity at $x = x_0$ gives $\phi'(y) = \phi(y)\, \overline{\phi(x_0)} / \overline{\phi'(x_0)} = c\, \phi(y)$. $\square$

**Theorem 8.1.8 (The isotropic mean changes by a scalar).** Under the hypotheses of the [Theorem 8.1.6](/entry/mean-x-prod-zero/), there is $c \in \mathbb{C}$ with $|c| = 1$ such that for every theta function $f$ and every $x \in Y^\perp$,
$$\int_{\mathcal{Y}} \rho(x)\bigl(\omega(g,h) f\bigr)(\iota(y))\, d\mu(y) = c \int_{\mathcal{Y}} \rho(x) f(\iota(y))\, d\mu(y).$$

Lean: `GlobalTheory.T.isotropicMean_changes_by_scalar_of_trivial_action` (also `GlobalTheory.IsoMean.mean_scalar`, the proof).

*Proof.* Both sides are isotropic means: for $x \in Y^\perp$ the left side is $m_{\omega(g,h) f}(x)$ and the integral on the right is $m_f(x)$. Two identities move $x$ into the function. First, $m_{\rho(x) F}(0) = m_F(x)$ for $x \in Y^\perp$. Second, by covariance $\omega(g,h) \rho(x) f = \rho(x + \iota(y_0)) \omega(g,h) f$ for some $y_0$, and $m_F$ is invariant under $x \mapsto x + \iota(y_0)$ because the mean is over a fundamental domain of $Y$ with respect to a Haar measure. So $m_{\omega(g,h) \rho(x) f}(0) = m_{\omega(g,h) f}(x)$.

Let $X$ be the set of pairs $(f, x)$ with $f$ a theta function and $x \in Y^\perp$, and put $\phi(f, x) = m_f(x)$ and $\phi'(f, x) = m_{\omega(g,h) f}(x)$. The functions $\rho(x) f$ are theta functions. The [Theorem 8.1.6](/entry/mean-x-prod-zero/) for $\rho(x') f'$ and $\rho(x) f$, rewritten with the two identities, gives $\phi'(f', x') \overline{\phi'(f, x)} = \phi(f', x') \overline{\phi(f, x)}$. The Lemma gives $\phi' = c \phi$ with $|c| = 1$, which is the claim. $\square$

**Remark 8.1.9 (Formalization).** The statement of the last theorem writes the embedding $\iota(y) = P y Q$ out in each place where it occurs; the proof restates the hypotheses in terms of $\iota$. The hypothesis of the first theorem is required for every Haar measure $\nu$ and every fundamental domain $\mathcal{F}$, and the outer integral is over the whole of $M_{a \times b}(\mathbb{A}_E)$, not over $\mathcal{Y}$. The splitting characters $\chi_V, \chi_W$ enter only through the Weil datum. We use the statements of the rational complement, the integral identity with the constant $\kappa$ and the invariance of the double integrals, which are lemmas of the same development; we have not opened their proofs.
