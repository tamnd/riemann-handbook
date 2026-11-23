---
title: Periods over the complex numbers
decls:
  - GlobalTheory.CechPer.span_periods_eq_top_and_finrank
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Periods over the complex numbers

Over $\mathbb{C}$ an abelian variety is a complex torus $\mathbb{C}^g / \Lambda$, and its de Rham classes are measured by their periods along $\Lambda$. This section proves that a map $P$ from $\Lambda$ to de Rham homology whose values are the periods of all primitive classes spans de Rham homology, which has dimension $2g$ (Theorem (Periods span de Rham homology)). It then defines period maps, whose last condition compares the form of a line bundle with its Riemann form. The theorem is used on the way to [EveryCharacter](/step/every-character/), through the span statement of the next section.

Throughout, $A$ is a group scheme over $\mathbb{C}$ and $A(\mathbb{C})$ its group of points, written multiplicatively. We use the notation of the section on the de Rham structure: $H^1_{\mathrm{dR}}(A)$ is the first de Rham cohomology on the infinitesimal site, $H^{\mathrm{pr}}_{\mathrm{dR}}(A)$ its primitive part and $D_{\mathrm{dR}}(A)$ the $\mathbb{C}$-dual of $H^{\mathrm{pr}}_{\mathrm{dR}}(A)$. Write $\check{H}^1_{\mathrm{dR}}(A)$ for the Čech-de Rham cohomology on the affine opens of $A$, as in the section on the Hodge and de Rham structure, with classes given by pairs $(c, \omega)$, and $\gamma : H^1_{\mathrm{dR}}(A) \to \check{H}^1_{\mathrm{dR}}(A)$ for the comparison map. Line bundles are given by Čech data $(U_i, g_{ij})$. For a point $a \in A(\mathbb{C})$ in an open set $U$ and $f \in \mathcal{O}(U)$, $f(a) \in \mathbb{C}$ is the value of $f$ at $a$.

**Definition 1.21.1 (Holomorphic uniformization).** Let $L$ be a line bundle on $A$ and $g \geq 0$. A *holomorphic uniformization* of $(A, L)$ of dimension $g$ consists of a surjective map $e : \mathbb{C}^g \to A(\mathbb{C})$ with $e(z + w) = e(z) e(w)$, a subgroup $\Lambda \subset \mathbb{C}^g$, and functions $\theta_i$ on $e^{-1}(U_i)$, such that:

1. $e(z) = 1$ if and only if $z \in \Lambda$, $\Lambda$ is discrete, and $\Lambda$ spans $\mathbb{C}^g$ over $\mathbb{R}$;
2. for every open set $U$ of $A$ and $f \in \mathcal{O}(U)$, the set $e^{-1}(U)$ is open and $z \mapsto f(e(z))$ is holomorphic on it;
3. each $\theta_i$ is holomorphic and nowhere zero on $e^{-1}(U_i)$, and $\theta_i(z) = g_{ij}(e(z))\, \theta_j(z)$ on $e^{-1}(U_i \cap U_j)$.

The map $e$ identifies $A(\mathbb{C})$ with $\mathbb{C}^g / \Lambda$, and the $\theta_i$ trivialize the pullback of $L$ to $\mathbb{C}^g$.

**Definition 1.21.2 (Periods).** Let $e, \Lambda$ be as above, $x \in \check{H}^1_{\mathrm{dR}}(A)$ and $q : \Lambda \to \mathbb{C}$ a function. Then $q$ is a *period* of $x$ if there are a Čech-de Rham 1-cocycle $(c, \omega)$ that represents $x$ and functions $h_U$ on $e^{-1}(U)$, one for each affine open $U$, such that:

1. $h_U$ is holomorphic on $e^{-1}(U)$, and $dh_U = e^* \omega_U$ there;
2. $h_V(z) = h_U(z) + c_{UV}(e(z))$ for $V \subset U$ and $z \in e^{-1}(V)$;
3. $h_U(z + l) = h_U(z) + q(l)$ for $z \in e^{-1}(U)$ and $l \in \Lambda$.

So $x$ becomes exact on $\mathbb{C}^g$, with primitives $h_U$, and $q(l)$ is the integral of $x$ over the loop that $l$ defines in $\mathbb{C}^g / \Lambda$.

**Theorem 1.21.3 (Periods span de Rham homology).** Let $A$ be an [[abelian scheme|JDDXZ89N33]] over $\mathbb{C}$, $L$ a line bundle on $A$ and $(e, \Lambda, \theta)$ a holomorphic uniformization of $(A, L)$ of dimension $g$. Let $P : \Lambda \to D_{\mathrm{dR}}(A)$ be additive, such that for every $c \in H^{\mathrm{pr}}_{\mathrm{dR}}(A)$ the function $l \mapsto P(l)(c)$ is a period of $\gamma(c)$. Then $P(\Lambda)$ spans $D_{\mathrm{dR}}(A)$ over $\mathbb{C}$, and $\dim_{\mathbb{C}} D_{\mathrm{dR}}(A) = 2g$.

Lean: `GlobalTheory.CechPer.span_periods_eq_top_and_finrank`.

The theorem does not assume that $A$ has relative dimension $g$; the number $g$ comes from the uniformization. Classically, $H^1(\mathbb{C}^g / \Lambda, \mathbb{C}) = \mathrm{Hom}(\Lambda, \mathbb{C})$, which has dimension $2g$, and de Rham homology is dual to it.

We use seven facts. In facts 3 to 7, $A$, $L$ and $(e, \Lambda, \theta)$ are as in the theorem.

1. (Lattices.) A discrete subgroup of $\mathbb{C}^g$ that spans $\mathbb{C}^g$ over $\mathbb{R}$ has a $\mathbb{Z}$-basis with $2g$ elements.
2. (Linear algebra.) Let $W$ be a $\mathbb{C}$-vector space, $\Lambda$ a free abelian group with a basis of $n$ elements and $P : \Lambda \to W^*$ additive. Suppose that $w = 0$ whenever $P(l)(w) = 0$ for all $l$, and that every additive $p : \Lambda \to \mathbb{C}$ is $l \mapsto P(l)(w)$ for some $w \in W$. Then $P(\Lambda)$ spans $W^*$ and $\dim W^* = n$.
3. (Comparison.) The map $\gamma$ is bijective.
4. (Zero periods.) If $0$ is a period of $x$, then $x = 0$.
5. (Existence.) Every additive $p : \Lambda \to \mathbb{C}$ is a period of some $x \in \check{H}^1_{\mathrm{dR}}(A)$.
6. (Primitivity.) If $\gamma(c)$ has an additive period, then $c$ is primitive.
7. (Uniqueness.) Two periods of the same class are equal.

In fact 2, the map $w \mapsto (l \mapsto P(l)(w))$ is a bijection from $W$ onto $\mathrm{Hom}(\Lambda, \mathbb{C}) \cong \mathbb{C}^n$, under which the $P(l)$ for $l$ in a basis become the coordinate functions. Facts 4, 5 and 7 together are the de Rham theorem in degree one on the torus $\mathbb{C}^g / \Lambda$.

*Proof.* By fact 1, $\Lambda$ has a $\mathbb{Z}$-basis of $2g$ elements. We apply fact 2 with $W = H^{\mathrm{pr}}_{\mathrm{dR}}(A)$, so that $W^* = D_{\mathrm{dR}}(A)$, and $n = 2g$.

Let $w \in W$ with $P(l)(w) = 0$ for all $l$. By hypothesis the zero function is a period of $\gamma(w)$, so $\gamma(w) = 0$ by fact 4, and $w = 0$ by fact 3.

Let $p : \Lambda \to \mathbb{C}$ be additive. Fact 5 gives $x$ with period $p$, and fact 3 gives $c \in H^1_{\mathrm{dR}}(A)$ with $\gamma(c) = x$. By fact 6, $c$ is primitive. By hypothesis, $l \mapsto P(l)(c)$ is also a period of $\gamma(c)$, so it equals $p$ by fact 7.

Fact 2 now gives both conclusions. $\square$

**Definition 1.21.4 (Period map).** Let $\varepsilon = \pm 1$, $A$ an abelian scheme over $\mathbb{C}$, $u = (e, \Lambda, \theta)$ a holomorphic uniformization of $(A, L)$ and $P : \Lambda \to D_{\mathrm{dR}}(A)$ additive. Then $P$ is a *period map of sign $\varepsilon$* if:

1. $P(\Lambda)$ spans $D_{\mathrm{dR}}(A)$ and $\dim D_{\mathrm{dR}}(A) = 2g$;
2. each $P(x)$ is the Lie image of a tangent vector $v$ such that the $\varepsilon$ part of $v^* f$ is $d(f \circ e)_0(x)$ for every regular function $f$ on an open set that contains the image of $v$, that is, of the derivative of $e$ at $0$ in the direction $x$;
3. if $\alpha$ is an endomorphism of $A$ as a group and $M$ is $\mathbb{C}$-linear with $e(Mw) = \alpha(e(w))$, then $\alpha_* P(x) = P(Mx)$;
4. for every Appell-Humbert datum $(H, \chi)$ of $u$ and every form $\psi$ of $L$, $\psi(P(x), P(x')) = \varepsilon \cdot 2\pi i \cdot \mathrm{Im}(x^{\mathsf{T}} H \bar{x}')$.

Here an *Appell-Humbert datum* is a positive definite hermitian matrix $H$ and $\chi : \Lambda \to \mathbb{C}$ with $|\chi| = 1$ such that $\theta_i(z) = \chi(l) \exp(\pi z^{\mathsf{T}} H \bar{l} + \frac{\pi}{2} l^{\mathsf{T}} H \bar{l})\, \theta_i(z + l)$. Condition 4 says that the form of $L$ is $\varepsilon \cdot 2\pi i$ times the Riemann form $\mathrm{Im}\, H$ of $L$.

**Remark 1.21.5 (Formalization).** A holomorphic uniformization is `HolUnif` ([IsLieBasis.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/IsLieBasis.lean#L69)), periods are `GlobalTheory.CechPer.IsPer` ([IsRatioCover.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsRatioCover.lean#L41)), and $\gamma$ is `cmp1`. Values of regular functions are taken with `valAt'`, which is $0$ at points outside the open set, and $e^* \omega_U$ is `evForm`, a chosen evaluation of Kähler forms that is $0$ if none exists; the definitions use both only on $e^{-1}(U)$. Facts 1 to 7 of the theorem are `GlobalTheory.exists_basis_of_discrete_of_span_eq_top_complex_pi`, `GlobalTheory.T.latticeEvaluation_span_dual_finrank`, `GlobalTheory.T.bijective_cmp1_of_isAbelianScheme_over_complex`, `GlobalTheory.T.cechDeRham_class_eq_zero_of_periods_zero`, `GlobalTheory.T.surjective_periodMap_abelianVariety_lattice`, `GlobalTheory.T.mem_primitiveDeRhamCohomology_of_additive_periods` and `GlobalTheory.T.isPer_unique'`; they are cited by their statements. The span statement of the section on periods in families assumes relative dimension $g$, which this theorem does not use. The definition of a period map is used only in that section; it is stated here because condition 4 gives the comparison with the Riemann form that the section on the de Rham structure refers to.
