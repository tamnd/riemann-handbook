---
title: Lattice counts and matching
decls:
  - GlobalTheory.CountId.countIdentity_of_unitMatch
  - GlobalTheory.T.relativeFundamentalLemmaCountIdentity_of_unitMatch
  - GlobalTheory.UnitLemma.unitaryLimit
  - GlobalTheory.T.unitary_lattice_count_ratio_tendsto
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Lattice counts and matching

The fundamental lemma compares orbital integrals of unit functions. When the element is regular semisimple, both orbital integrals are counts of lattices in a finite algebra with an involution. This section sets up these counts, and proves two facts about them. The first is a count identity: a weighted count of lattices on the linear side equals a count of self-dual lattices on the unitary side. It is the [fundamental lemma](/entry/unit-match-all/) in the language of lattices. The second is a limit formula: the unitary count, divided by the size of a box in a torus, tends to the number of orbits of self-dual lattices. The [next section](/entry/linear-descent/) uses both facts to prove the unit lemma. For Hermitian lattices and their local classification, see [lattices in Hermitian spaces](/learn/hermitian-lattices/#lattices-in-quadratic-and-hermitian-spaces) and [local classification](/learn/hermitian-lattices/#local-classification).

**Definition 4.6.1 (Unramified quadratic data).** An *unramified quadratic datum* $K$ consists of:

1. a complete discrete valuation ring $\mathcal{O}$ whose residue field is finite with $q^2$ elements, and whose fraction field $E$ has characteristic $0$;
2. a ring automorphism $c$ of $E$ with $c \circ c = \mathrm{id}$ and $c(\mathcal{O}) \subseteq \mathcal{O}$;
3. elements $x, y \in \mathcal{O}$ with $c(x) = y$ and $x - y \notin \mathfrak{m}$, where $\mathfrak{m}$ is the maximal ideal.

For $x \in E$ let $\mathrm{val}(x)$ be its valuation, with $\mathrm{val}(0) = 0$, and let $\eta(x) = (-1)^{\mathrm{val}(x)}$. The datum is *odd* if $2$ is a unit in $\mathcal{O}$. An element $a \in \mathcal{O}$ is *small* if $a \neq 0$, $a \in \mathfrak{m}$ and $c(a) = a$.

Condition 3 says that $c$ is not the identity on the residue field. So the fixed field $F$ of $c$ has residue field with $q$ elements, and $E/F$ is an [unramified quadratic extension](/learn/number-fields/#places-and-completions).

**Definition 4.6.2 (Algebra with involution).** An *algebra with involution* over $K$ is a commutative $E$-algebra $A$ of finite dimension $n$, also an $\mathcal{O}$-algebra compatibly, with a ring automorphism $\sigma$ of $A$ such that $\sigma \circ \sigma = \mathrm{id}$ and $\sigma(e y) = c(e)\sigma(y)$ for $e \in E$, and with an element $g \in A$. Let $P$ be the characteristic polynomial of multiplication by $g$. The product of two such algebras is $A_1 \times A_2$ with $\sigma_1 \times \sigma_2$ and $(g_1, g_2)$.

Fix an algebra with involution. For $x \in A$ define the form $h_x(y, z) = \mathrm{Tr}_{A/E}(x y \sigma(z))$. When $\sigma(x) = x$, this is a [Hermitian form](/learn/algebra/#hermitian-and-skew-hermitian-forms) on $A$ relative to $c$. A *lattice* is a finitely generated $\mathcal{O}$-submodule of $A$ that spans $A$ over $E$.

**Definition 4.6.3 (Lattice counts).** Let $x, w, u \in A$.

1. $X(x)$ is the set of lattices $L$ with $gL \subseteq L$ that are self-dual for $h_x$: $y \in L$ if and only if $h_x(y, z) \in \mathcal{O}$ for all $z \in L$.
2. $T = \{t \in A^\times : t\sigma(t) = 1\}$, and $T_0 = T \cap \mathcal{O}_A^\times$, where $\mathcal{O}_A^\times$ is the group of units $t$ such that $t$ and $t^{-1}$ are integral over $\mathcal{O}$.
3. $N(x) = \sum_{L} [\mathrm{Stab}_T(L) : \mathrm{Stab}_T(L) \cap T_0]$, the sum over a set of representatives $L$ of the $T$-orbits on $X(x)$. Here the index is the relative index of $T_0$ in the stabilizer.
4. $U(x, w)$ is the number of $L \in X(x)$ with $w \in L$.
5. $\mathrm{Lin}$ is the set of lattices $M$ with $gM \subseteq M$ and $\sigma M \subseteq M$. For $M \in \mathrm{Lin}$ with an $\mathcal{O}$-basis $m_1, \dots, m_n$, put $\epsilon(M) = \eta\big(\det(\mathrm{Tr}_{A/E}(g^k m_l))_{0 \le k < n,\, 1 \le l \le n}\big)$.
6. $G(u) = \sum \epsilon(M)$, the sum over $M \in \mathrm{Lin}$ with $u \in M$ and $\mathrm{Tr}_{A/E}(M) \subseteq \mathcal{O}$.
7. $\rho(w)$ is the number of classes $tT_0 \in T/T_0$ such that $t^{-1}w$ is integral over $\mathcal{O}$.

A sum or count over an infinite set is $0$ by convention. The sign $\epsilon(M)$ does not depend on the basis: a change of basis multiplies the determinant by a unit of $\mathcal{O}$.

The algebra is *Lie regular* if $\sigma(g) = g$ and $P$ is separable. An element $x$ is *positive* if $x$ is a unit and $\sigma(x) = x$.

The count $G$ is the linear orbital integral and $U$ is the unitary orbital integral. To see this, let $A$ be Lie regular. The powers $1, g, \dots, g^{n-1}$ form an $E$-basis of $A$ that is fixed by $\sigma$. So the $\sigma$-fixed part $A^\sigma$ is an $F$-form of $A$, and the $\sigma$-stable lattices are the $\mathcal{O}$-spans of the $\mathcal{O}_F$-lattices in $A^\sigma$. These are the points of $\mathrm{GL}_n(F)/\mathrm{GL}_n(\mathcal{O}_F)$. On the unitary side, a self-dual lattice has an orthonormal basis for $h_x$, so self-dual lattices are the points of $U_n(F)/U_n(\mathcal{O}_F)$.

**Theorem 4.6.4 (Count identity).** Assume that the fundamental lemma holds in every rank. Let $K$ be an unramified quadratic datum and $A$ a Lie regular algebra with involution. Let $x$ be positive and let $w$ be a unit. Then
$$G(x\, w\, \sigma(w)) = U(x, w).$$

Lean: `GlobalTheory.CountId.countIdentity_of_unitMatch` (also `GlobalTheory.T.relativeFundamentalLemmaCountIdentity_of_unitMatch`, a second name).

*Proof.* Step 1: the local fields. The datum $K$ comes from an unramified quadratic pair $(F, E)$ in the sense of [the first section](/entry/unit-match-at-of-one-le-norm/). The conjugation of $E$ is $c$, and $|y| \le 1$ exactly when $y \in \mathcal{O}$. Choose measures in rank $n$; they exist.

Step 2: the linear point. Let $e_i = g^i$ for $0 \le i < n$; this is a basis fixed by $\sigma$. Put $u = x w \sigma(w)$. Then $\sigma(u) = u$ and $u$ is a unit. Let $Y = (S, b, \kappa, 0) \in \mathfrak{g}_n(F)$, where $S$ is the matrix of multiplication by $g$ in the basis $e$, $b$ is the coordinate vector of $u$, and $\kappa_i = \mathrm{Tr}_{A/E}(e_i)$. All entries are fixed by $c$, so they lie in $F$. Let $a$ be the invariants of $Y$. Then the moments of $a$ are $\kappa S^k b = \mathrm{Tr}_{A/E}(g^k u)$.

Step 3: regularity. The Hankel matrix of $a$ is $(\mathrm{Tr}_{A/E}(g^{k+l}u))_{k,l}$. Its determinant is not $0$, since $P$ is separable and $u$ is a unit: the trace form of a separable algebra is nondegenerate. So $\Delta(a) \neq 0$.

Step 4: the linear orbital integral. The orbit of $\mathrm{sec}(a)$ contains $Y$. A coset $h\,\mathrm{GL}_n(\mathcal{O}_F)$ gives the lattice $M = h \cdot \mathcal{O}^n$ in the coordinates $e$, and the integrand $1_{\mathfrak{g}_n}(h^{-1} \cdot Y)$ is $1$ exactly when $gM \subseteq M$, $u \in M$ and $\mathrm{Tr}(M) \subseteq \mathcal{O}$. A computation with the bordered matrix shows that the transfer factor at $h^{-1} \cdot Y$ is the sign $\epsilon(M)$. So $O(1_{\mathfrak{g}_n}, \mathrm{sec}(a)) = G(u)$.

Step 5: the unitary side. Suppose $X \in \mathfrak{h}_n$ has invariants $a$. The invariants of $X$ and of the triple formed by multiplication by $g$, the vector $w$ and the functional $y \mapsto h_x(y, w)$ agree, since $h_x(g^k w, w) = \mathrm{Tr}_{A/E}(g^k u)$. Two elements of $\mathfrak{g}_n(E)$ with the same invariants $a$ and $\Delta(a) \neq 0$ are conjugate under $\mathrm{GL}_n(E)$, by the normal form lemma behind [the first section](/entry/unit-match-at-of-one-le-norm/). The conjugating element turns the basis $e$ into a basis of $A$ in which the triple is $X$. Since $X$ is Hermitian and $w$ generates $A$ as an $E[g]$-module, this basis is orthonormal for $h_x$. Then a coset $\gamma U_n(\mathcal{O}_F)$ gives the self-dual lattice spanned by $\gamma$ applied to this basis, and the integrand $1_{\mathfrak{h}_n}(\gamma^{-1}X)$ is $1$ exactly when the lattice is $g$-stable and contains $w$. So $O(1_{\mathfrak{h}_n}, X) = U(x, w)$, and the first clause of matching gives the identity.

Step 6: the vanishing case. Suppose no $X \in \mathfrak{h}_n$ has invariants $a$. The second clause of matching gives $G(u) = 0$. Assume $U(x, w) \neq 0$. Then there is $L \in X(x)$ with $w \in L$. A self-dual lattice has a basis $b_1, \dots, b_n$ with $h_x(b_i, b_j) = \delta_{ij}$. In this basis, the matrix of $g$ is Hermitian, since $h_x(gy, z) = h_x(y, gz)$. Let $X$ be this matrix, with the coordinate vector of $w$ and $d = 0$. Its invariants are $a$, by the computation of Step 5. This is a contradiction. So $U(x, w) = 0$. $\square$

**Lemma 4.6.5 (Facts on the torus).** Let $A$ be Lie regular, let $a$ be small and let $x$ be positive.

1. The set of $T$-orbits on $X(x)$ is finite. For each $L \in X(x)$, $\mathrm{Stab}_T(L) \subseteq \mathcal{O}_A^\times$, and the relative index in item 3 of the definition is not $0$.
2. There are $r \ge 0$, a surjective homomorphism $\phi : T \to \mathbb{Z}^r$ with kernel $T_0$, and integers $d_1, \dots, d_r > 0$, such that $t^{-1}a^k$ is integral if and only if $|\phi(t)_i| \le k d_i$ for all $i$. In particular $\rho(a^k) = \prod_i (2kd_i + 1)$.
3. For each lattice $L$ there is $m$ such that, for $k \ge m$, $a^k y \in L$ for every integral $y$, and $a^k L$ consists of integral elements.
4. If $L \in X(x)$ and $m$ is as in item 3, then for $k \ge m$ the number $n_k(L)$ of lattices $tL$ with $t \in T$ and $a^k \in tL$ satisfies
$$\iota(L)\rho(a^{k-m}) \le n_k(L) \le \iota(L)\rho(a^{k+m}),$$
where $\iota(L)$ is the relative index of $T_0$ in $\mathrm{Stab}_T(L)$.

Lean: `GlobalTheory.T.selfDual_stable_lattice_unit_orbits_finite`, `GlobalTheory.T.torus_mod_integralUnits_structure_and_integrality`, `GlobalTheory.T.finiteAlgebraInvolution_rho_pow_eq_card_box`, `GlobalTheory.T.fullLattice_sandwich_between_integral_elements`, `GlobalTheory.T.torus_orbit_lattice_count_bounded_by_rho`.

The proofs are not reproduced here. Item 2 says that $T/T_0$ is a free abelian group of finite rank, and that $\rho(a^k)$ counts the points of a box in it.

**Theorem 4.6.6 (Unitary limit).** Let $K$ be an unramified quadratic datum, let $A$ be a Lie regular algebra with involution, let $a$ be small and let $x$ be positive. Then
$$\lim_{k \to \infty} \frac{U(x, a^k)}{\rho(a^k)} = N(x).$$

Lean: `GlobalTheory.UnitLemma.unitaryLimit` (also `GlobalTheory.T.unitary_lattice_count_ratio_tendsto`, a second name).

*Proof.* By item 1 of the Lemma, choose representatives $L_1, \dots, L_s$ of the $T$-orbits on $X(x)$. By item 3, choose $m_j$ for $L_j$, and let $m$ be the largest $m_j$. For $k \ge m$, each lattice in $X(x)$ that contains $a^k$ lies in exactly one orbit, so $U(x, a^k) = \sum_j n_k(L_j)$. By item 4 and $N(x) = \sum_j \iota(L_j)$,
$$N(x)\rho(a^{k-m}) \le U(x, a^k) \le N(x)\rho(a^{k+m}).$$
By item 2, $\rho(a^j) > 0$ for all $j$, and
$$\frac{\rho(a^{k+m})}{\rho(a^k)} = \prod_i \frac{2(k+m)d_i + 1}{2kd_i + 1} \to 1$$
as $k \to \infty$. The same holds for $\rho(a^{k-m})/\rho(a^k)$. Divide the inequality by $\rho(a^k)$; both bounds tend to $N(x)$. $\square$

**Remark 4.6.7 (Formalization).** The data $K$ and $A$ are structures in the code, with the field $F$ left implicit; the proof of the count identity builds $F$ and the normed fields from $K$. Counts are taken with `Nat.card` and sums with `finsum`, so both are $0$ on infinite sets ([UnitLemmaGroup.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/UnitLemmaGroup.lean#L43), [LinearDescent.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/LinearDescent.lean#L14)). The theorems above prove finiteness where it matters, but the definitions alone do not. The sign $\epsilon(M)$ is defined with a basis chosen by `Classical.epsilon` ([LinearDescent.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/LinearDescent.lean#L21)), so independence of the basis is a lemma, not part of the definition. Also $\mathrm{val}(0) = 0$, so $\eta(0) = 1$, as in the first section. The count identity uses all ranks of the fundamental lemma, but only rank $n = \dim_E A$ for a given $A$. The lemmas on the torus are proved in files that this chapter does not cover.
