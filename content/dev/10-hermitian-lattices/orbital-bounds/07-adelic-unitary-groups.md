---
title: Indices, classes and counts in adelic unitary groups
decls:
  - PI.adelic_index_eq
  - adelic_class_set_finite
  - unitary_class_mass_hermitian
  - lattice_count_all
  - sc_reference_exists
  - sc_xu_exists
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Indices, classes and counts in adelic unitary groups

This section proves six facts about the unitary group of a Hermitian space over the adeles of a CM field. The first is a symmetry of indices: conjugation by $x$ and by $x^{-1}$ cut the stabilizer of the lattice to subgroups of the same index. The second is the finiteness of the double coset space of rational points and an open subgroup. The third identifies the sum of inverse stabilizer orders over the double cosets with the mass of the genus. The fourth counts rational points in a box of bounded Cartan distance. The last two build a reference frame of the lattice at the primes of a level and move a vector onto it. The results are used in the step on [theta local matching](/step/theta-local-matching/), in the step on [every character of a row](/step/every-character-of-row/), in the theorems on the class mass of a genus, on the lattice count, and on the existence of a reference frame and of an approximating element. For the background see [adeles and ideles](/learn/number-fields/#adeles-and-ideles) and [adelic points and compact open subgroups](/learn/groups/#adelic-points-and-compact-open-subgroups).

### The setting

Let $E/F$ be a CM extension of number fields with complex conjugation $a \mapsto \bar a$, let $n \geq 1$, and let $J$ be an $n \times n$ Hermitian matrix over $E$ with $\det J \neq 0$. Put $h(x, y) = \bar x^{\mathsf T} J y$ on $E^n$. Let $L \subseteq E^n$ be an $\mathcal{O}_E$-lattice that is self-dual for $h$, and let $L_f$ be its closure in $E^n \otimes_F \mathbb{A}_{F,f}$. Let $G_f = U_J(\mathbb{A}_{F,f})$. For each infinite place $v$ of $F$ there are a sign vector $\varepsilon_v$, an embedding $\varphi_v$ of $E$ into $\mathbb{C}$ above $v$, and a matrix $P_v$ with $P_v^* J^{\varphi_v} P_v = J_{\varepsilon_v}$, where $J_{\varepsilon_v}$ is the diagonal matrix of the signs. Put $G_\infty = \prod_v U(J_{\varepsilon_v})$ and $G_{\mathbb{A}} = G_\infty \times G_f$. The rational points $U_J(E)$ embed diagonally in $G_{\mathbb{A}}$ through the $P_v$, and in $G_f$. Let $d = [F : \mathbb{Q}]$.

Let $K \subseteq G_f$ be the stabilizer of $L_f$. The topology on $G_f$ has as a basis the sets $K(g) = \{ x : x L_f = L_f,\ (x - 1) L_f \subseteq g L_f \}$ for integers $g \geq 1$, and their translates. For subgroups $A$ and $B$ we write $[B : A \cap B]$ for the index, read as $0$ when it is infinite.

### Indices and classes

**Theorem 4.7.1 (Index symmetry).** For every setting and every $x \in G_f$,
$$[K : x K x^{-1} \cap K] = [K : x^{-1} K x \cap K].$$

Lean: `PI.adelic_index_eq`.

*Proof.* This is a reduction of the equality to the integrality of a trace, applied to the proved integrality statement. We did not unfold either. $\square$

For a unimodular locally compact group with $K$ compact open, both sides are finite and the equality follows from the invariance of Haar measure.

**Theorem 4.7.2 (Finitely many classes).** For every setting and every open subgroup $U \subseteq G_f$ there is a finite set $S \subseteq G_f$ such that every $x \in G_f$ is a product
$$x = \gamma\, s\, u, \qquad \gamma \in U_J(E),\ s \in S,\ u \in U.$$

Lean: `adelic_class_set_finite`.

*Proof.* This is a reduction of the finiteness to a statement on successive minima at the real places, applied to that statement, which is proved. We did not unfold either. $\square$

So the double coset space $U_J(E) \backslash G_f / U$ is finite. This is the finiteness of class numbers for the unitary group, as in Borel's paper on the finiteness of class numbers.

### The class mass

Here the setting is more general. Let $F$ and $E$ be number fields with $E$ an $F$-algebra and with an involution $a \mapsto \bar a$, given as an $F$-algebra map $\sigma$ with $\sigma(a) = \bar a$. Assume that $\sigma \theta \neq \theta$ for some $\theta$, and that $\tau(\bar a) = \overline{\tau(a)}$ for every embedding $\tau : E \to \mathbb{C}$. Let $V$ be a finite-dimensional $E$-space with a nondegenerate Hermitian form $h$, let $b$ be a basis of $V$ with $M$ elements, and let $L_0 \subseteq V$ be an $\mathcal{O}_E$-lattice. Let $\Gamma = U(E)$ be the unitary group of the Gram matrix of $h$ in $b$, and let $K_0 \subseteq U(\mathbb{A}_{F,f})$ be the stabilizer of the coordinates of $L_0$. For $g \in U(\mathbb{A}_{F,f})$ put
$$\Gamma_g = \{ \gamma \in \Gamma : g^{-1} \gamma g \in K_0 \}.$$
The *mass* of $L_0$ is $\sum_M 1/\#\operatorname{Aut}(M)$, over a set of representatives of the classes in the genus of $L_0$, when there is a finite such set, and $0$ otherwise.

**Theorem 4.7.3 (Class mass).** Assume that the Gram matrix of $h$ in $b$ has signature $(M, 0)$ at every embedding $\tau$. Let $g_1, \dots, g_N \in U(\mathbb{A}_{F,f})$ be such that every $x$ is a product $\gamma g_i k$ with $\gamma \in \Gamma$ and $k \in K_0$, and the index $i$ is unique. Then
$$\sum_{i=1}^{N} \frac{1}{\# \Gamma_{g_i}} = \operatorname{mass}(L_0).$$

Lean: `unitary_class_mass_hermitian`.

*Proof.* This is the unitary class mass theorem, which has the same hypotheses and the same conclusion. We did not unfold its proof. $\square$

The theorem is used in the theorem on the class mass of a genus. The signature condition makes $h$ definite at each infinite place, so each $\Gamma_{g_i}$ is finite. The $g_i$ represent the double cosets $\Gamma \backslash U(\mathbb{A}_{F,f}) / K_0$, and each double coset is a class in the genus, with automorphism group $\Gamma_{g_i}$.

### Counting rational points

Let $x \in G_{\mathbb{A}}$. Its lattice is the set $L(x)$ of $u \in E^n$ with $x_f^{-1} u \in L_f$. At an infinite place $v$, the coordinates of $u$ are $(x_v)^{-1} P_v^{-1} \varphi_v(u)$. A *sublattice* of $x$ is a family $b_1, \dots, b_j$ of linearly independent vectors, with $j \geq 1$, together with an $\mathcal{O}_E$-module $B \subseteq L(x)$ that contains the $b_i$ and lies in their $E$-span. Its height is
$$\operatorname{ht}(B) = \frac{\prod_v \det G_v(b)}{[B : \mathcal{O}_E b_1 + \dots + \mathcal{O}_E b_j]},$$
where $G_v(b)$ is the Gram matrix of the coordinates of the $b_i$ at $v$. Its size is $\operatorname{ht}(B)^{1/(2dj)}$. Put
$$\tau_1(x) = \min\Big( \tfrac{1}{2},\ \inf_B \operatorname{ht}(B)^{1/(2dj)} \Big).$$
For $g \in U(J_{\varepsilon})$ let $\operatorname{dist}(g)$ be the infimum of $\|X\|$ over all ways to write $g = k \exp(X)$ with $k$ in the maximal compact subgroup and $X$ in the complement $\mathfrak{p}$ of its Lie algebra, with the Hilbert-Schmidt norm.

**Theorem 4.7.4 (Lattice count).** For every setting, let $x, y \in G_{\mathbb{A}}$ with $\tau_1(x) > 0$ and $\tau_1(y) > 0$, and let $r_v \geq 0$ for each infinite place $v$. Let $S$ be a finite set of rational points $\gamma$ such that $(x^{-1} \gamma y)_f \in K$ and $\operatorname{dist}\big((x^{-1} \gamma y)_v\big) \leq r_v$ for every $v$. Then
$$\# S \leq \left( \frac{3 \sqrt{n}}{\tau_1(x)\, \tau_1(y)} \right)^{2 n^2 d} \exp\Big( 2 n^2 \sum_v r_v \Big).$$

Lean: `lattice_count_all`.

*Proof.* This is a reduction lemma applied to two proved inputs: a formula for the index of a lattice by a determinant, and a lemma on the index of a lattice in its saturation. We did not unfold the count. $\square$

The count is used in the lattice count of the closed volume statements. Since the bound does not depend on $S$, the set of all such $\gamma$ is finite and has at most this many elements. The quantity $\tau_1(x)$ measures how short the shortest sublattice of $x$ is; when $x$ goes to a cusp it tends to $0$ and the bound grows.

### A reference frame and an approximating element

Fix an integer $g \geq 1$. A vector $w$ of $E^n \otimes \mathbb{A}_{F,f}$ lies *in $mL$ at $g$* if $c\, w \in m L_f$ for some integer $c$ prime to $g$. An element $c$ of $E \otimes \mathbb{A}_{F,f}$ is *$0$ modulo $g$* if $c = g t$ for an integral element $t$. Let $r, k \geq 0$ with $n = 2r + k + 1$, and let $e_1, \dots, e_r$ and $f_1, \dots, f_r$ in $E^n$ satisfy
$$h(e_a, e_b) = 0, \qquad h(f_a, f_b) = 0, \qquad h(e_a, f_b) = \delta_{ab},$$
with all $e_a$ and $f_a$ in $L$ at $g$.

**Definition 4.7.5 (Reference frame).** A *reference frame* for $(g, e, f)$ consists of vectors $e^0_a, f^0_a, z^0, w_i, w^*_i$ in $L_f$, for $a \leq r$ and $i \leq k$, and an integral idempotent $\epsilon$ of $E \otimes \mathbb{A}_{F,f}$, with these properties.

1. $e^0_a - e_a$ and $f^0_a - f_a$ lie in $gL$ at $g$.
2. Modulo $g$, the Gram matrix of the $e^0_a$ and $f^0_a$ is the hyperbolic one, $h(z^0, z^0) \equiv -1$, and $z^0$ is orthogonal to all $e^0_a$ and $f^0_a$.
3. Modulo $g$, the $w_i$ and $w^*_i$ are orthogonal to $z^0$ and to all $e^0_a$ and $f^0_a$.
4. $\epsilon \bar\epsilon = 0$, $(1 - \epsilon - \bar\epsilon) L_f \subseteq g L_f$, $w_i = \epsilon w_i$, $w^*_i = \bar\epsilon w^*_i$, and $h(w^*_i, w_j) \equiv \delta_{ij}\, \epsilon$ modulo $g$.
5. Every vector of $L_f$ is the sum of an integral combination of the frame vectors and an element of $g L_f$.

**Theorem 4.7.6 (Reference frame).** Assume that every prime of $F$ that divides $g$ splits in $E$. Then a reference frame for $(g, e, f)$ exists.

Lean: `sc_reference_exists`.

*Proof.* This is a reduction lemma applied to a lemma that builds a Witt frame. The Witt frame lemma is derived from two proved inputs: the local rings at the primes of $g$ are principal, and a Weil basis exists. $\square$

**Theorem 4.7.7 (Approximating element).** Assume that every prime of $F$ that divides $g$ splits in $E$, and fix a reference frame for $(g, e, f)$. Let $z \in E^n$ be orthogonal to all $e_a$ and $f_a$, with $h(z, z) = -t$ for an integer $t \equiv 1 \pmod g$, and with $z$ in $L$ at $g$. Then there is $x \in K$ with the following properties.

1. $x e_a = e_a$ and $x f_a = f_a$ for all $a$.
2. $x^{-1} z - z^0$ lies in $gL$ at $g$.
3. For every integer $m$ prime to $g$ and every $y \in L_f$, $(x - 1) y$ lies in $mL$ at $m$.

Lean: `sc_xu_exists`.

*Proof.* This is a reduction lemma applied to three proved inputs: a projection lemma at the split primes, a lemma that the local data satisfy the linear hypotheses of the construction, and a compatibility of the split unitary projection. We did not unfold the construction. $\square$

The two theorems are used to build a reference frame and an approximating element for the closed volume statements. At a split prime $E \otimes F_v = F_v \times F_v$, and the idempotent $\epsilon$ is one of the two factors. Then $L_f$ at $v$ is a pair of dual lattices, and the $w_i$ and $w^*_i$ are dual bases of the two factors.

**Remark 4.7.8 (Formalization).** The class mass theorem only renames the unitary class mass theorem that it calls; its statement is the same, see [UnitaryClassMassHermitian.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/UnitaryClassMassHermitian.lean#L4). It does not ask that $F$ be the fixed field of $\sigma$, only that $\sigma$ fix $F$. The indices in the index symmetry are relative indices of subgroups, which are $0$ when infinite; see [AdIndexEq.lean](lean:Formalism/PeriodIntegrals/AdIndexEq.lean#L12). The set $S$ of the lattice count is a finite set of rational points, and the count is stated for each such set; see [LatCountG.lean](lean:Formalism/PeriodIntegrals/LatCountG.lean#L51). The setting is in [GlobAut.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/GlobAut.lean#L32), the reference frame in [ScRefExists.lean](lean:Formalism/PeriodIntegrals/ScRefExists.lean#L39), and the approximating element in [ScXuExists.lean](lean:Formalism/PeriodIntegrals/ScXuExists.lean#L16). The inputs of the six proofs were not unfolded beyond their statements. The theorems are in [AdIndexEq.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/AdIndexEq.lean#L8), [AdelClassFin.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/AdelClassFin.lean#L5), [LatCountG.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/LatCountG.lean#L7), [ScRefExists.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/ScRefExists.lean#L8) and [ScXuExists.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/ScXuExists.lean#L8).
