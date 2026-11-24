---
title: The Weil representation and quadratic base change
decls:
  - UpperTheory.ConvolutionTheory.R2.weilEx
  - UpperTheory.ConvolutionTheory.R2.fockSt
  - UpperTheory.ConvolutionTheory.R2.ne
  - UpperTheory.ConvolutionTheory.R2.cap
  - keyFock
  - UpperTheory.ConvolutionTheory.R2.I.key
  - UpperTheory.ConvolutionTheory.R2.quadBC2
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Weil representation and quadratic base change

This section proves quadratic base change for $\mathrm{GL}_2$ from a totally real field to a totally imaginary quadratic extension. Let $\pi$ be a regular algebraic cuspidal representation of $\mathrm{GL}_2(\mathbb{A}_F)$. Then either $\pi$ is isomorphic to its twist by the quadratic character of $E/F$, or there is a cuspidal representation of $\mathrm{GL}_2(\mathbb{A}_E)$ that is a base change of $\pi$. The proof is by the theta correspondence. The space of hermitian $2 \times 2$ matrices over $E$ is a quadratic space of dimension four over $F$. The Weil representation of $\mathrm{SL}_2(\mathbb{A}_F)$ on its Schwartz-Bruhat functions commutes with an action of $\mathrm{GL}_2(\mathbb{A}_E)$, and the theta integral lifts forms on $\mathrm{SL}_2$ over $F$ to forms on $\mathrm{GL}_2$ over $E$. Base change is used in the automorphy lifting argument, in Kato's vanishing for two twists, and in the published hypotheses of section 25. See also [base change](/learn/automorphic-forms/#base-change) in the Background.

Let $F$ be a totally real number field, $\mathbb{A} = \mathbb{A}_F$, and $\psi \colon F \backslash \mathbb{A} \to \mathbb{C}^{\times}$ the standard additive character. Let $E/F$ be a totally imaginary extension of degree two.

**Definition 8.23.1 (Datum of a quadratic extension).** A datum for $E/F$ is an element $\delta \in F$ that is negative at each real place, an element $\theta \in E$ with $\theta^{2} = \delta$ such that $1, \theta$ is a basis of $E$ over $F$, and the automorphism $\sigma$ of $E/F$ with $\sigma(\theta) = -\theta$. Write $\bar{z} = \sigma(z)$.

A datum exists, since $E = F(\sqrt{\delta})$ for some totally negative $\delta$. For $v = (v_0, v_1, v_2, v_3) \in \mathbb{A}^{4}$ put

$$X(v) = \begin{pmatrix} v_1 & v_2 + v_3 \theta \\ v_2 - v_3 \theta & v_0 \end{pmatrix}, \qquad q(v) = v_2^{2} - \delta v_3^{2} - v_0 v_1.$$

The matrix $X(v)$ is hermitian, and $q(v) = -\det X(v)$. The group $\mathrm{GL}_2(\mathbb{A}_E)$ acts on $\mathbb{A}^{4}$ by $h \cdot X = h X \bar{h}^{t}$, and this action multiplies $q$ by $\nu(h) = N_{E/F}(\det h)$. Let $B(v, v') = 2(v_2 v'_2 - \delta v_3 v'_3) - v_1 v'_0 - v_0 v'_1$, the bilinear form of $q$.

**Definition 8.23.2 (Weil representation).** Let $\mathcal{S}$ be the Schwartz-Bruhat space of $\mathbb{A}^{4}$. A Weil representation for the datum is a Hecke character $\eta$ of $F$ that is the quadratic character of $E/F$, with $\eta^{2} = 1$ and $\eta \circ N_{E/F} = 1$, together with two homomorphisms $\omega \colon \mathrm{SL}_2(\mathbb{A}) \to \mathrm{End}(\mathcal{S})$ and $L \colon \mathrm{GL}_2(\mathbb{A}_E) \to \mathrm{End}(\mathcal{S})$ with the following properties.

1. $\omega(n(b)) \varphi(v) = \psi(b\, q(v)) \varphi(v)$ for $n(b) = \begin{pmatrix} 1 & b \\ 0 & 1 \end{pmatrix}$.
2. $\omega(m(a)) \varphi(v) = \eta(a) |a|^{2} \varphi(a v)$ for $m(a) = \mathrm{diag}(a, a^{-1})$.
3. $\omega(w) \varphi$ is the Fourier transform $\int \varphi(y) \psi(B(y, v))\, dy$, where $w = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$.
4. $L(h) \varphi(v) = |\nu(h)|^{-1} \varphi(h^{-1} \cdot v)$.
5. $L(h) \omega(g) = \omega(c_{\nu(h)}(g)) L(h)$, where $c_t$ multiplies the upper right entry of $g$ by $t^{-1}$ and the lower left entry by $t$.
6. The theta distribution $\Theta(\varphi) = \sum_{\xi \in F^{4}} \varphi(\xi)$ is invariant under $\omega(\gamma)$ for $\gamma \in \mathrm{SL}_2(F)$ and under $L(\gamma)$ for $\gamma \in \mathrm{GL}_2(E)$.
7. Each $\varphi$ is fixed by $\omega(g)$ for $g$ near $1$ with trivial archimedean part, and at almost all places by the integral points; and $(g, v) \mapsto \omega(g) \varphi(v)$ is continuous.

Properties 1 to 3 are Weil's formulas for the generators of $\mathrm{SL}_2$. Property 5 says that $L$ and $\omega$ commute up to the similitude factor.

**Theorem 8.23.3 (Existence of the Weil representation).** For each datum of $E/F$ there is a Weil representation.

Lean: `UpperTheory.ConvolutionTheory.R2.weilEx`.

*Proof.* The element $\delta$ is not zero, since it is negative at a real place. Take for $\eta$ the quadratic character of $E/F$; it satisfies $\eta^{2} = 1$ and $\eta \circ N_{E/F} = 1$. Define operators on $\mathcal{S}$ by the formulas 1, 2 and 3. They satisfy the relations of a presentation of $\mathrm{SL}_2(\mathbb{A})$ by the elements $n(b)$, $m(a)$ and $w$. The relation that involves $w^{2}$ and the Weil index of $q$ is the place where $\eta$ enters: the Weil index of $q$ at $a$ is $\eta(a)$. So the operators extend to a homomorphism $\omega$. The operators $L(h)$ are defined by formula 4. The commutation 5 is checked on the generators. The invariance of $\Theta$ under $\mathrm{SL}_2(F)$ is the Poisson summation formula for $w$ and is clear for $n(b)$ and $m(a)$. The invariance under $\mathrm{GL}_2(E)$ holds because $\gamma \cdot$ permutes the lattice $F^{4}$ and $|\nu(\gamma)| = 1$ by the product formula. $\square$

**Definition 8.23.4 (Fock space).** Let $\mathcal{F} \subset \mathcal{S}$ be the space spanned by the functions

$$\varphi(v) = p(v_\infty)\, e^{-\pi\, Q(v_\infty)}\, \varphi_f(v_f),$$

where $p$ is a polynomial in the real coordinates of $v_\infty$, $\varphi_f$ is a Schwartz-Bruhat function on the finite adeles, and $Q(v) = \mathrm{tr}\bigl(v_0^{2} + v_1^{2} + 2(v_2^{2} - \delta v_3^{2})\bigr)$, a positive definite form at each real place.

These are the right test functions for the theta lift: they are finite under the maximal compact subgroups at infinity, and their lifts are smooth automorphic forms.

**Theorem 8.23.5 (Stability of the Fock space).** Let $W$ be a Weil representation. Then the following hold.

1. $L(k) \mathcal{F} \subset \mathcal{F}$ for each $k \in \mathrm{GL}_2(\mathbb{A}_{E, f})$.
2. For each $\varphi \in \mathcal{F}$ there is a finite-dimensional subspace $U \subset \mathcal{F}$ that contains $L(k) \varphi$ for each $k$ in the unitary group at the archimedean places of $E$.
3. For each $\varphi \in \mathcal{F}$ and each compact set $C$ of elements of $\mathrm{SL}_2(\mathbb{A})$ that are orthogonal at infinity, there is a finite-dimensional $U \subset \mathcal{F}$ that contains $\omega(k) \varphi$ for each $k \in C$.

Lean: `UpperTheory.ConvolutionTheory.R2.fockSt`.

*Proof.* The space $\mathcal{F}$ has a description by creation operators. There are a space of vacuum vectors (the Gaussian times a function on the finite adeles fixed by an open subgroup) and operators $x_{w,i}$, $d_{w,i}$ (multiplication by a coordinate and differentiation in a coordinate at a real place $w$). A finite set of Fock vectors lies in the space spanned by finitely many products of these operators applied to the vacuum vectors fixed by an open subgroup $\Lambda$, and this span is finite-dimensional for a bounded degree. An operator $T$ maps $\mathcal{F}$ into itself if it maps vacuum vectors to vacuum vectors and if $T x_{w,i}$ lies in the span of the $x_{w',j} T$ and $d_{w',j} T$. The operators $L(k)$ for finite $k$, $L(k)$ for unitary $k$ at infinity and $\omega(k)$ for $k$ orthogonal at infinity have these two properties, since they preserve the Gaussian and act linearly on the coordinates. For 3, the orbit of $\varphi$ under $C$ lies in the span of finitely many such vectors. $\square$

Let $\mathcal{M}$ be a Haar measure on $\mathrm{SL}_2(\mathbb{A})$ with a fundamental domain $D$ for $\mathrm{SL}_2(F)$, and with the Iwasawa decomposition of the measure. For a cusp form $f$ of $\pi$, $\varphi \in \mathcal{F}$ and $h \in \mathrm{GL}_2(\mathbb{A}_E)$, the theta lift is

$$\theta(f, \varphi)(h) = \int_{D} f\bigl(g\, d(\nu(h))\bigr)\, \Theta\bigl(\omega(g) L(h) \varphi\bigr)\, dg,$$

where $d(t) = \mathrm{diag}(1, t)$. Let $V(\pi)$ be the span of the lifts $\theta(f, \varphi)$ over $f \in \pi$ and $\varphi \in \mathcal{F}$. For a function $\Phi$ on $\mathrm{GL}_2(\mathbb{A}_E)$, its Whittaker function is

$$W_E(\Phi)(h) = \int_{(F \backslash \mathbb{A})^{2}} \Phi\bigl(n(u_0 + u_1 \theta) h\bigr)\, \psi(2 u_0)\, du,$$

the Whittaker function for the character $z \mapsto \psi(\mathrm{tr}_{E/F} z)$. On the side of $F$, let $W_1(f, \varphi, h)$ be the integral over $N(\mathbb{A}) \backslash \mathrm{SL}_2(\mathbb{A})$ of the Whittaker function of $f$ at $g\, d(\nu(h))$ times the partial Fourier transform of $\omega(g) L(h) \varphi$ at the point $(0, 1, 1, 0)$. The Whittaker expansion of the lift says $W_E(\theta(f, \varphi)) = W_1(f, \varphi, \cdot)$.

**Theorem 8.23.6 (Nonvanishing of the lift).** There are $f \in \pi$, $\varphi \in \mathcal{F}$ and $h$ with $W_1(f, \varphi, h) \ne 0$.

Lean: `UpperTheory.ConvolutionTheory.R2.ne`.

*Proof.* We take $h = 1$. There are $f \in \pi$, a idele $a$ and $k$ in the maximal compact subgroup with the Whittaker function of $f$ at $m(a) k$ not zero, since $\pi$ is cuspidal and so generic. There is $\varphi \in \mathcal{F}$ whose partial Fourier transform at the point $(0, 1, 1, 0)$, moved by $m(a) k$, is not zero. If $W_1(f, \varphi', 1) = 0$ for all $\varphi' \in \mathcal{F}$, then the integrand vanishes at $m(a) k$, because the integral of a Fock vector against the Whittaker function determines the product of the two values. This contradicts the choice of $f$ and $\varphi$. $\square$

Let $\pi$ have infinitesimal character given by a multiset $m$ at a real place of $F$. The Capelli element at a complex place $\tau$ of $E$ is the quantum determinant $\mathrm{cap}_\tau(u)$ of the matrix of Lie algebra operators $E_{ij}$ at $\tau$, a polynomial in $u$ with values in the centre of the enveloping algebra. A form has infinitesimal character $m$ at $\tau$ when $\mathrm{cap}_\tau(u)$ acts on it by $\prod_{z \in m} (u + z)$.

**Theorem 8.23.7 (Infinitesimal character of the lift).** Let $\tau$ be a complex place of $E$ above the place $v$ of $F$, and suppose that $\pi$ has infinitesimal character $m$ at $v$. Then for each $u \in \mathbb{C}$ and $\Phi \in V(\pi)$,

$$\mathrm{cap}_\tau(u)\, \Phi = \prod_{z \in m} (u + z)\, \Phi.$$

Lean: `UpperTheory.ConvolutionTheory.R2.cap`.

*Proof.* The Lie algebra of $\mathrm{GL}_2$ at $\tau$ acts on the lift through its action on $\varphi$ by $L$. On the Fock space, this action is the action of the Lie algebra of $\mathrm{SL}_2$ at $v$ through $\omega$, moved by the commutation of the dual pair. So the Capelli element on the side of $E$ becomes a central element on the side of $F$, and it acts on $f$ by its infinitesimal character. $\square$

Now let $v$ be a place of $F$ that splits in $E$, and $\theta_v \in F_v$ with $\theta_v^{2} = \delta$. Then $E \otimes F_v \cong F_v \times F_v$, and the idempotent $e = \tfrac12 + \tfrac{1}{2 \theta_v} \theta$ gives an embedding $J \colon \mathrm{GL}_2(F_v) \to \mathrm{GL}_2(\mathbb{A}_E)$, $J(x) = 1 + e(x - 1)$, at one of the two places above $v$. A matrix coefficient of the local component $\pi_v$ is a function $x \mapsto \lambda(\pi_v(x) u)$ for $u$ in the space of $\pi_v$ and a linear form $\lambda$.

**Lemma 8.23.8 (Matrix coefficients of the lift, Fock form).** Let $f \in \pi$, $\varphi \in \mathcal{F}$, and $h' \in \mathrm{GL}_2(\mathbb{A}_E)$ commuting with the lower unipotent elements at $v$ in the image of $J$. Then $x \mapsto W_1(f, \varphi, h' J(x))$ is in the span of the matrix coefficients of $\pi_v$.

Lean: `keyFock`.

*Proof.* The function $\varphi \mapsto W_1(f, \varphi, h)$ is linear on $\mathcal{F}$ for each $h$, since the theta integral is bilinear. So the set of $\varphi$ with the property is a subspace. At $v$, the Fock space is in the span of pure tensors $u \otimes \varphi_a$, where $\varphi_a$ is built from a Schwartz function $a$ on $M_2(F_v)$ and $\omega(j(g))$ acts on $\varphi_a$ by right translation of $a$ by $g \in \mathrm{SL}_2(F_v)$. For a pure tensor, $W_1(f, u \otimes \varphi_a, h' J(x))$ is an integral over $\mathrm{GL}_2(F_v)$ of a translate of the local Whittaker function of $f$ against $a$, so it is a matrix coefficient of $\pi_v$. $\square$

**Theorem 8.23.9 (Matrix coefficients of the lift).** Let $v$, $\theta_v$ and $J$ be as above, $\Phi \in V(\pi)$ and $h \in \mathrm{GL}_2(\mathbb{A}_E)$. Then the function $x \mapsto W_E(\Phi)(h J(x))$ on $\mathrm{GL}_2(F_v)$ is in the span of the matrix coefficients of $\pi_v$.

Lean: `UpperTheory.ConvolutionTheory.R2.I.key`.

*Proof.* Both sides are linear in $\Phi$, since $W_E$ is linear on continuous functions. So it suffices to take $\Phi = \theta(f, \varphi)$. Write $h = h' k$ with $k$ finite, $k$ commuting with $J(x)$, and $h'$ commuting with the lower unipotent elements at $v$. Since $\pi$ is smooth, $f$ translated by the image of $k$ is a form $f' \in \pi$, and $L(k) \varphi$ is in $\mathcal{F}$ by the [Theorem 8.23.5](/entry/fock-st/) on stability. By the Whittaker expansion and the equivariance of the lift under $k$,

$$W_E(\theta(f, \varphi))(h' k J(x)) = W_1\bigl(f', L(k) \varphi, h' J(x)\bigr).$$

The [Lemma 8.23.8](/entry/key-fock/) applies to the right side. $\square$

**Definition 8.23.10 (Base change).** Let $\pi$ be cuspidal on $\mathrm{GL}_2(\mathbb{A}_F)$ and $P$ cuspidal on $\mathrm{GL}_2(\mathbb{A}_E)$. Then $P$ is a base change of $\pi$ if three things hold: for each complex place $\tau$ of $E$, $P$ has at $\tau$ the infinitesimal character of $\pi$ at the place below; for each finite $v$ and $w$ with an isomorphism $F_v \cong E_w$ over $F$, $P_w \cong \pi_v$ through the isomorphism; for almost all $w$ above $v$ with $N w = (N v)^{f}$, the Satake parameters of $P_w$ are the $f$-th powers of those of $\pi_v$.

**Theorem 8.23.11 (Quadratic base change for $\mathrm{GL}_2$).** Let $F$ be totally real, $E/F$ totally imaginary of degree two, and $\pi$ a regular algebraic cuspidal representation of $\mathrm{GL}_2(\mathbb{A}_F)$. Then either $\pi \cong \pi \otimes \eta$ for a Hecke character $\eta$ that is the quadratic character of $E/F$ at almost all places, or there is a cuspidal $P$ on $\mathrm{GL}_2(\mathbb{A}_E)$ that is a base change of $\pi$.

Lean: `UpperTheory.ConvolutionTheory.R2.quadBC2`.

*Proof.* Choose a datum, a Weil representation and a measure. Consider the terms of the theta lift that come from the trivial orbit, that is, the integrals of $f(g\, d(\nu(h)))$ against the partial theta series of $\omega(g) L(h) \varphi$ with its first two coordinates zero.

If these terms do not all vanish, then $\pi \cong \pi \otimes \eta$ for the character $\eta$ of the Weil representation (the dihedral case).

Suppose that they all vanish. Then the lifts are cuspidal. The space $V(\pi)$ is not zero: by the [Theorem 8.23.6](/entry/ne/) on nonvanishing there are $f$, $\varphi$ and $h$ with $W_1(f, \varphi, h) \ne 0$; the lift $\theta(f, \varphi)$ is a smooth form, and by the Whittaker expansion its Whittaker function at $h$ is $W_1(f, \varphi, h) \ne 0$. Since $\pi$ is regular algebraic and $V(\pi) \ne 0$, $V(\pi)$ contains a cuspidal representation $P$. The infinitesimal characters agree by the [Theorem 8.23.7](/entry/cap/) on the Capelli element. The local components agree at split places by the [Theorem 8.23.9](/entry/key/) on matrix coefficients. The Satake parameters agree at almost all places by the unramified computation. So $P$ is a base change of $\pi$. $\square$

**Remark 8.23.12 (Formalization).** The Lemma is a private theorem `keyFock` in the root namespace ([KeyFock.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/RealGroupAnalysis/SpecialLinearCosets/KeyFock.lean#L19)). The Weil representation is the structure `Weil` ([ThetaLiftTrivialOrbitTermsVanish.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/RealGroupAnalysis/ThetaLiftTrivialOrbitTermsVanish.lean#L171)), and the targets of the four theorems are `WeilEx`, `FockSt`, `Ne` and `Cap` ([Smooth.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/RealGroupAnalysis/Smooth.lean#L46)). The files `Smooth.lean` and `ThetaLiftTrivialOrbitTermsVanish.lean` exist both in `RealGroupAnalysis` and in `RealGroupAnalysis/WeilRepresentation`, with different contents. In base change, the agreement of local components is asked only at pairs $v$, $w$ with $F_v \cong E_w$, that is, at split places, and $\eta$ is asked to be the quadratic character only at almost all places. Our proofs of the existence theorem, the nonvanishing and the Capelli statement name the steps that the formal proofs call; we have not unfolded those steps, nor the proofs of the dihedral case, the irreducibility, the unramified comparison, the cuspidality and the Whittaker expansion.
