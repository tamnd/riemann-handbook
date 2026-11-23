---
title: The Weil representation of SL2 for an etale Hermitian pair
decls:
  - GlobalTheory.JR.WeilQuad.weilField_main
  - GlobalTheory.T.weilRepresentation_quadraticField_exists
  - GlobalTheory.JR.weilEt_of_weilField
  - GlobalTheory.T.weilRepresentationEtale_of_quadraticField
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Weil representation of SL2 for an etale Hermitian pair

The proof of the fundamental lemma uses the group $\mathrm{SL}_2$ in two ways. In rank one, after a descent to an etale algebra, the partial Fourier transform is the action of the Weyl element in a [Weil representation](/learn/theta/#the-weil-representation). In the induction on the rank, two Weil representations act on the two sides of the matching. This section builds these representations. It first treats the case of a field, by a presentation of $\mathrm{SL}_2$ and a Gauss integral, and then extends the result to every etale algebra. It also shows that the constant in front of the Fourier transform is $1$ when the Hermitian space is the standard one. The results are used in [the rank one transfer](/entry/rank-one/) and in [the induction on the rank](/entry/unit-match-succ/).

Throughout, $(F, E)$ is an unramified quadratic pair and $\psi$ is a standard character of $F$, as in the first section of this chapter.

**Definition 4.2.1 (Etale Hermitian pair).** An etale Hermitian pair over $(F, E)$ is a finite reduced commutative $F$-algebra $K$, with its natural topology as a finite-dimensional $F$-vector space, together with a commutative ring $L$ with an involution $y \mapsto \bar y$, such that $L = K \otimes_F E$ as algebras, the involution fixes $K$, and it acts on $E$ by the conjugation of $E$. The algebra $K$ is also given a Borel measurable structure.

Since $F$ has characteristic $0$, $K$ is a finite product of finite field extensions of $F$ (see [Galois theory](/learn/algebra/#galois-theory)). The basic examples are $K = F$, $L = E$, and $K = F^n$, $L = E^n$. If $K$ is a field, then $L$ is a field when $E$ does not embed in $K$, and $L \cong K \times K$ with the involution that swaps the factors otherwise.

We use the following notation. For a unit $t \in K^\times$, let $|t|_K$ be its modulus: the factor by which multiplication by $t$ scales a Haar measure of $K$. Put $|t|_K = 0$ if $t$ is not a unit. Let $\eta_K(t) = \eta(N_{K/F}(t))$, $\psi_K = \psi \circ \mathrm{Tr}_{K/F}$, and $N = N_{L/K}$.

**Definition 4.2.2 (Self-dual measure).** Let $V$ be a locally compact abelian group with a Borel measure $\mu$ and let $B : V \times V \to \mathbb{C}$. The Fourier transform of $\varphi$ for $B$ is
$$\mathcal{F}_B \varphi(y) = \int_V \varphi(x) B(x, y)\, d\mu(x).$$
The measure $\mu$ is self-dual for $B$ if it is an additive Haar measure and $\mathcal{F}_B \mathcal{F}_B \varphi(y) = \varphi(-y)$ for every test function $\varphi$.

For $x \in K^\times$ we use the kernel $B_x(y', y) = \psi_K\big(x \,\mathrm{Tr}_{L/K}(\bar y' y)\big)$ on $L$. It comes from the Hermitian form $(y', y) \mapsto x \bar y' y$ on the free $L$-module $L$, viewed as a quadratic space over $K$. On $K$ we use the kernel $(y, y') \mapsto \psi_K(y y')$.

**Definition 4.2.3 (Representation on test functions).** Let $G$ be a group and $X$ a topological space. A family of maps $W(g)$, $g \in G$, from functions on $X$ to functions on $X$ is a representation on test functions if: each $W(g)$ maps test functions to test functions; $W(1)\varphi = \varphi$, $W(gh)\varphi = W(g)W(h)\varphi$ and $W(g)(c\varphi + \varphi') = cW(g)\varphi + W(g)\varphi'$ for all test functions $\varphi, \varphi'$ and $c \in \mathbb{C}$.

In $\mathrm{SL}_2(K)$ put
$$n(z) = \begin{pmatrix} 1 & z \\ 0 & 1 \end{pmatrix}, \quad m(s) = \begin{pmatrix} s & 0 \\ 0 & s^{-1} \end{pmatrix}, \quad w = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}.$$

**Definition 4.2.4 (Weil representation).** Let $x \in K$, let $\omega : K \to \mathbb{C}$, let $\mu$ be a measure on $L$ and $\gamma \in \mathbb{C}$. A Weil representation with these data is a representation $W$ of $\mathrm{SL}_2(K)$ on test functions on $L$ such that, for every test function $\varphi$, every $z \in K$, $s \in K^\times$ and $y \in L$:
$$\begin{aligned} W(n(z))\varphi(y) &= \psi_K\big(z x N(y)\big)\, \varphi(y), \\ W(m(s))\varphi(y) &= \omega(s)\, |s|_K\, \varphi(s y), \\ W(w)\varphi(y) &= \gamma\, \mathcal{F}_{B_x}\varphi(y). \end{aligned}$$
The number $\gamma$ is the Weil constant.

These are the formulas of the Weil representation for the quadratic space $(L, x N)$ of dimension $2$ over $K$. The classical constant is an eighth root of unity built from Gauss sums. Here $\omega$ is the quadratic character of the space.

To build $W$ we need a presentation of $\mathrm{SL}_2$ over a field.

**Theorem 4.2.5 (Presentation of $\mathrm{SL}_2$).** Let $K$ be a field and $M$ a monoid. Let $n : K \to M$, $m : K^\times \to M$ and $t \in M$ satisfy, for all $a, b, z \in K$ and $s, s' \in K^\times$ and $u \in K^\times$:
$$\begin{aligned} & n(0) = 1, \quad n(a + b) = n(a)n(b), \quad m(1) = 1, \quad m(ss') = m(s)m(s'), \\ & m(s)n(z) = n(s^2 z)m(s), \quad t^2 = m(-1), \quad t\,m(s) = m(s^{-1})\,t, \\ & t\,n(u)\,t = n(-u^{-1})\,m(-u^{-1})\,t\,n(-u^{-1}). \end{aligned}$$
Then there is a monoid homomorphism $\rho : \mathrm{SL}_2(K) \to M$ with $\rho(n(z)) = n(z)$, $\rho(m(s)) = m(s)$ and $\rho(w) = t$.

Lean: `GlobalTheory.T.exists_hom_specialLinearGroup_of_relations`.

The relations hold for the matrices $n(z)$, $m(s)$ and $w$ themselves. The theorem says that they define $\mathrm{SL}_2(K)$: every family that satisfies them comes from a homomorphism.

**Definition 4.2.6 (Stable Gauss integral).** Let $K$ and $L$ be fields, $x \in K^\times$, $\mu$ a Haar measure on $L$ and $u \in K$. A number $G$ is the stable Gauss integral at $u$ if there is an open compact subgroup $\Lambda_0 \subset L$ such that
$$\int_\Lambda \psi_K\big(u x N(y)\big)\, d\mu(y) = G$$
for every open compact subgroup $\Lambda \supseteq \Lambda_0$.

**Theorem 4.2.7 (Weil representation for a field).** Let $(K, L)$ be an etale Hermitian pair over $(F, E)$ with $K$ and $L$ fields. Let $\psi$ be standard, $x \in K^\times$, and $\mu$ a measure on $L$ that is self-dual for $B_x$. Let $\omega : K \to \mathbb{C}$ satisfy, for every $s \in K^\times$: $\omega(s) = 1$ if $s$ is a norm from $L$, and $\omega(s) = -1$ if it is not. Then there exist $\gamma$ and a Weil representation $W$ with the data $x, \omega, \mu, \gamma$.

Lean: `GlobalTheory.JR.WeilQuad.weilField_main` (also `GlobalTheory.T.weilRepresentation_quadraticField_exists`, a second name).

*Proof.* Let $S$ be the complex vector space of test functions on $L$. Define operators on $S$ by $n(z)\varphi(y) = \psi_K(z x N(y))\varphi(y)$, $m(s)\varphi(y) = \omega(s)|s|_K\varphi(sy)$ and $\mathcal{F} = \mathcal{F}_{B_x}$. These preserve $S$. Since $L/K$ is a quadratic extension, $\omega$ is the quadratic character of $K^\times$ with kernel the norms. So $\omega$ is multiplicative. Also $\omega(-1) = 1$: the extension $L/K$ is unramified, so every unit of $K$ is a norm.

The stable Gauss integral $G_1$ at $u = 1$ exists, and $G_1^2 = 1$. More generally the stable Gauss integral $G_u$ at a unit $u$ exists and equals $G_1\, \omega(u)\, |u|_K^{-1}$. Put $t = G_1^{-1}\mathcal{F}$. We check the relations of the presentation on $S$.

1. The relations for $n$ and $m$ are direct: $\psi_K$ is additive, $\omega$ and $|\cdot|_K$ are multiplicative, and $N(sy) = s^2 N(y)$ gives $m(s)n(z) = n(s^2 z)m(s)$.
2. Self-duality gives $\mathcal{F}^2\varphi(y) = \varphi(-y)$. Since $G_1^{-2} = 1$, $\omega(-1) = 1$ and $|-1|_K = 1$, this is $t^2 = m(-1)$.
3. A change of variables gives $\mathcal{F}(\varphi(s\,\cdot))(y) = |s|_K^{-2}\,\mathcal{F}\varphi(s^{-1}y)$, since $\bar s = s$ and $|s|_L = |s|_K^2$. With $\omega(s^{-1}) = \omega(s)$ this gives $t\,m(s) = m(s^{-1})\,t$.
4. For a unit $u$ and a test function $\varphi$, completing the square in the Fourier integral gives
$$\mathcal{F}\, n(u)\, \mathcal{F}\varphi(z) = G_u\, \psi_K\big(-u^{-1} x N(z)\big)\, \mathcal{F}\big(n(-u^{-1})\varphi\big)(-u^{-1} z).$$
With $G_u = G_1\omega(u)|u|_K^{-1}$ this is the last relation.

The presentation gives a homomorphism $\rho$ from $\mathrm{SL}_2(K)$ to the endomorphisms of $S$. Put $W(g)\varphi = \rho(g)\varphi$ for test functions $\varphi$, and $W(g)\varphi = 0$ otherwise. Then $W$ is a representation on test functions with the formulas of a Weil representation, and $\gamma = G_1^{-1}$. $\square$

Since $G_1^2 = 1$, the constant is $\gamma = \pm 1$.

**Theorem 4.2.8 (Weil representation for an etale pair).** Assume the conclusion of the [Theorem 4.2.7](/entry/weil-field-main/) for fields, for every unramified quadratic pair and every $\omega$ as there. Then for every unramified quadratic pair $(F, E)$, every etale Hermitian pair $(K, L)$ over it, every standard $\psi$, every $x \in K^\times$ and every measure $\mu$ on $L$ that is self-dual for $B_x$, there exist $\gamma$ and a Weil representation with the data $x, \eta_K, \mu, \gamma$.

Lean: `GlobalTheory.JR.weilEt_of_weilField` (also `GlobalTheory.T.weilRepresentationEtale_of_quadraticField`, a second name).

*Proof.* Say that $(K, L)$ is good if the conclusion holds for it, for all $\psi$, $x$ and $\mu$. We prove that every pair is good by strong induction on $\dim_F K$.

1. If $K = 0$, there is only one function on $L = 0$, and the trivial representation works.
2. If $K$ and $L$ are fields, apply the hypothesis with $\omega = \eta_K$. This is allowed: $\eta_K(s) = 1$ when $s$ is a norm from $L$, and $\eta_K(s) = -1$ when it is not. Indeed $L$ is a field, so $E$ does not embed in $K$, the residue degree $f$ of $K/F$ is odd, and $\eta_K(s) = (-1)^{f v_K(s)} = (-1)^{v_K(s)}$, which is $1$ exactly on the norms of the unramified extension $L/K$.
3. If $K$ is a field and $L$ is not, then $L \cong K \times K$ with the involution that swaps the factors. Here there is an explicit Weil representation with $\gamma = 1$.
4. If $K$ is not a field and not $0$, it is a product. Then $(K, L)$ splits as a product of two etale Hermitian pairs $(K_1, L_1)$ and $(K_2, L_2)$ of smaller dimension. These are good by induction, and a pair that splits into two good pairs is good. $\square$

The Weil constant is often $1$. We need this in one case.

**Theorem 4.2.9 (Weil constant of the standard form).** Let $(K, L)$ be an etale Hermitian pair over $(F, E)$, $\psi$ standard, $x \in K^\times$, $\mu$ self-dual for $B_x$, and $\omega$ any function on $K$. Let $W$ be a Weil representation with the data $x, \omega, \mu, \gamma$. Assume there are $r \ge 0$ and an $E$-linear isomorphism $j : L \to E^r$ with
$$\overline{j(y)}^{\,t}\, j(y') = \mathrm{Tr}_{L/E}(x\, \bar y\, y') \quad \text{for all } y, y' \in L.$$
Then $\gamma = 1$.

Lean: `GlobalTheory.JR.gammaOne_holds` (also `GlobalTheory.T.weilConstantStandardHermitian_eq_one`, a second name).

*Proof.* The map $j$ says that the Hermitian space $(L, \mathrm{Tr}_{L/E}(x \bar y y'))$ is the standard one. Let $\Lambda = j^{-1}(\mathcal{O}_E^r)$ and $\varphi_0 = 1_\Lambda$. Then $\Lambda$ is open and compact, and $\varphi_0$ is a test function. On $\Lambda$ we have $\psi_K(x N(y)) = 1$, and the [lattice](/learn/hermitian-lattices/#lattices-in-quadratic-and-hermitian-spaces) $\Lambda$ is self-dual for $B_x$, so $\mathcal{F}_{B_x}\varphi_0 = \mu(\Lambda)\varphi_0$. Self-duality of $\mu$ at $y = 0$ gives $\mu(\Lambda)^2 = 1$, so $\mu(\Lambda) = 1$. Hence $W(w)\varphi_0 = \gamma\varphi_0$ and $W(n(1))\varphi_0 = \varphi_0$. In $\mathrm{SL}_2(K)$ we have $w^4 = 1$ and $(w\,n(1))^3 = 1$. Apply $W$ to $\varphi_0$ and evaluate at $0$, where $\varphi_0(0) = 1$: this gives $\gamma^4 = 1$ and $\gamma^3 = 1$. So $\gamma = \gamma^4/\gamma^3 = 1$. $\square$

**Remark 4.2.10 (Formalization).** A representation on test functions satisfies its rules only on test functions, and the construction sets $W(g)\varphi = 0$ for every other $\varphi$ ([WeilRepresentationQuadraticFieldExists.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/WeilRepresentationQuadraticFieldExists.lean#L240)). The theorem on the Weil constant holds for every function $\omega$, since its proof uses only $n(1)$ and $w$ (IsTestRep.lean:160). The statement for a field allows any value $\omega(0)$; only the values on units enter the formulas.
