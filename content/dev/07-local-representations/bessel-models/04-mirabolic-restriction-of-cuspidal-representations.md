---
title: Mirabolic restriction of cuspidal representations
decls:
  - CompanionTheory.Mirab.cuspidalMirabolic
  - CompanionTheory.Mirab.Restr.cuspidalRestrictsToInduced
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Mirabolic restriction of cuspidal representations

This section treats the finite field analogue of a Bessel model of the simplest kind: the Whittaker model of a cuspidal representation of $\mathrm{GL}_{n+1}(\mathbb{F}_q)$. We prove that the restriction of an irreducible cuspidal representation to the mirabolic subgroup is the representation induced from a generic character of the unipotent upper triangular group. Together with the existence of cuspidal representations, this is the statement of [Theorem 1.6.4 of Volume 8](/entry/cuspidal-mirabolic-holds/), one of the published inputs of the proof. The theory over finite fields is the model for the local theory over $p$-adic fields; see [cuspidal representations and segments](/learn/representations/#cuspidal-representations-and-segments) and [generic representations and local factors](/learn/representations/#generic-representations-and-local-factors).

### Cuspidal representations

Let $k$ be a finite field with $q$ elements and $N \geq 1$. All representations are on complex vector spaces.

**Definition 6.4.1 (Block unipotent radical).** Let $b : \{0, \dots, N-1\} \to \mathbb{N}$ be monotone. The *unipotent radical* $U_b$ is the group of $u \in \mathrm{GL}_N(k)$ with $(u - 1)_{ij} = 0$ whenever $b_j \leq b_i$.

If $b$ takes the values $0, \dots, s$ on consecutive blocks of sizes $N_0, \dots, N_s$, then $U_b$ is the unipotent radical of the standard parabolic subgroup with Levi $\mathrm{GL}_{N_0} \times \dots \times \mathrm{GL}_{N_s}$ ([parabolic subgroups](/learn/groups/#parabolic-subgroups)). The radical is proper exactly when $b$ is not constant.

**Definition 6.4.2 (Cuspidal representation).** A representation $\rho$ of $\mathrm{GL}_N(k)$ on $V$ is *cuspidal* if, for each monotone nonconstant $b$, the only vector of $V$ fixed by $U_b$ is $0$.

So $\rho$ has no nonzero vectors invariant under the unipotent radical of any proper parabolic subgroup. Equivalently, the Jacquet modules of $\rho$ for all proper parabolic subgroups vanish, so $\rho$ is not a constituent of a parabolically induced representation. It is enough to check the maximal parabolic subgroups, that is the functions $b$ with two values.

**Example 6.4.3.** Let $k = \mathbb{F}_2$. The group $\mathrm{GL}_2(\mathbb{F}_2)$ permutes the four vectors of $\mathbb{F}_2^2$, and the sign of this permutation is a character $\chi$. The transvection $t = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ swaps $(0,1)$ and $(1,1)$ and fixes the other two vectors, so $\chi(t) = -1$. The only proper unipotent radical is $\{1, t\}$, and a vector fixed by $t$ satisfies $v = -v$. So $\chi$ is an irreducible cuspidal representation of dimension $1 = q - 1$.

### The mirabolic subgroup and the generic character

Let $n \geq 0$ and $N = n + 1$.

**Definition 6.4.4 (Mirabolic subgroup).** The *mirabolic subgroup* $P_{n+1} \subset \mathrm{GL}_{n+1}(k)$ is the group of matrices whose last row is $(0, \dots, 0, 1)$. Let $U_{n+1} \subset P_{n+1}$ be the group of upper triangular unipotent matrices.

**Definition 6.4.5 (Generic character).** Let $\psi_0 : k \to \mathbb{C}^\times$ be a nontrivial additive character. The *generic character* of $U_{n+1}$ is
$$\psi(u) = \psi_0\Big( \sum_{i=0}^{n-1} u_{i, i+1} \Big),$$
the character of the sum of the entries just above the diagonal.

The map $u \mapsto \sum_i u_{i,i+1}$ is a homomorphism from $U_{n+1}$ to $k$, so $\psi$ is a character. Its restriction to each simple root group is nontrivial.

**Definition 6.4.6 (Mirabolic induced representation).** Let $I(\psi)$ be the space of functions $f : P_{n+1} \to \mathbb{C}$ with $f(u x) = \psi(u) f(x)$ for $u \in U_{n+1}$ and $x \in P_{n+1}$. The group $P_{n+1}$ acts on $I(\psi)$ by right translation: $(h \cdot f)(x) = f(x h)$.

This is $\mathrm{Ind}_{U_{n+1}}^{P_{n+1}} \psi$. Its dimension is the index $[P_{n+1} : U_{n+1}]$. Since $P_{n+1} \cong \mathrm{GL}_n(k) \ltimes k^n$, we have $|P_{n+1}| = q^n |\mathrm{GL}_n(k)| = q^{n(n+1)/2} \prod_{i=1}^{n} (q^i - 1)$, and $|U_{n+1}| = q^{n(n+1)/2}$. So $\dim I(\psi) = \prod_{i=1}^{n} (q^i - 1)$.

**Lemma 6.4.7 (Irreducibility of the mirabolic induced representation).** The representation $I(\psi)$ of $P_{n+1}$ is irreducible, and $\dim I(\psi) = \prod_{i=1}^{n} (q^i - 1)$.

*Proof.* The dimension was computed above. We use one fact of Mackey type, which holds because $\psi_0$ is nontrivial: for each $h \in P_{n+1}$ outside $U_{n+1}$ there is $u \in U_{n+1}$ with $c = h^{-1} u h \in U_{n+1}$ and $\psi(c) \neq \psi(u)$. Let $f \in I(\psi)$ satisfy also $f(x u) = f(x) \psi(u)$ for $u \in U_{n+1}$. For $h \notin U_{n+1}$ and $u, c$ as above, $f(u h) = f(h c)$ gives $\psi(u) f(h) = f(h) \psi(c)$, so $f(h) = 0$. Hence $f = f(1)\,\delta$, where $\delta$ is supported on $U_{n+1}$ with $\delta(u) = \psi(u)$. Now let $W \neq 0$ be a subrepresentation and $f \in W$ nonzero. After a right translation we may assume $f(1) \neq 0$. The average $\sum_{u \in U_{n+1}} \overline{\psi(u)}\, (u \cdot f)$ lies in $W$, has the right transformation law under $U_{n+1}$ on both sides, and takes the value $|U_{n+1}| f(1) \neq 0$ at $1$. So $\delta \in W$. The right translates $h \cdot \delta$ are supported on the cosets $U_{n+1} h^{-1}$, so they span $I(\psi)$. Hence $W = I(\psi)$. $\square$

### The restriction theorem

**Theorem 6.4.8 (Gelfand).** Let $\rho$ be an irreducible cuspidal representation of $\mathrm{GL}_{n+1}(k)$. Then the restriction of $\rho$ to $P_{n+1}$ is isomorphic to $\mathrm{Ind}_{U_{n+1}}^{P_{n+1}} \psi$. In particular $\dim \rho = \prod_{i=1}^{n} (q^i - 1)$, and $\rho$ has a Whittaker functional, unique up to a scalar.

**Theorem 6.4.9 (Mirabolic restriction).** Let $k$ be a finite field, $n \geq 0$, and $\psi_0$ a nontrivial additive character of $k$. Let $\rho$ be an irreducible cuspidal representation of $\mathrm{GL}_{n+1}(k)$ on a finite-dimensional space $V$. Then the restriction of $\rho$ to $P_{n+1}$ is isomorphic to $I(\psi)$.

Lean: `CompanionTheory.Mirab.Restr.cuspidalRestrictsToInduced`.

*Proof.* A *Whittaker functional* is a linear form $L$ on $V$ with $L(\rho(u) x) = \psi(u) L(x)$ for $u \in U_{n+1}$. Let $V_\psi = \{ x : \rho(u) x = \psi(u) x \text{ for all } u \}$ be the $\psi$-eigenspace, and $e = \sum_{u} \overline{\psi(u)} \rho(u)$ the averaging operator. Then $e$ maps $V$ onto $V_\psi$, and $l \circ e$ is a Whittaker functional for each linear form $l$.

We use two results that are proved elsewhere in the development. The first is a dimension formula for cuspidal representations: $\dim V = \prod_{i=1}^{n} (q^i - 1) \cdot \dim V_\psi$. It comes from the filtration of the restriction to $P_{n+1}$ by derivatives, in which cuspidality kills every term except the top one. The second is the multiplicity one theorem of Gelfand and Graev: two Whittaker functionals on an irreducible $V$, the first nonzero, are proportional.

Since $V \neq 0$, the dimension formula gives $V_\psi \neq 0$. Take $x \in V_\psi$ nonzero and a form $l$ with $l(x) \neq 0$. Then $L = l \circ e$ satisfies $L(x) = |U_{n+1}| \, l(x) \neq 0$, so $L$ is a nonzero Whittaker functional. The map $y \mapsto L(y)$ on $V_\psi$ is injective: if $L(y) = 0$ for $y \in V_\psi$, then for each $l'$ the functional $l' \circ e$ is a multiple of $L$ by Gelfand-Graev, so $|U_{n+1}| \, l'(y) = l'(e y) = 0$, and $y = 0$. Hence $\dim V_\psi = 1$ and $\dim V = \prod_{i=1}^{n} (q^i - 1)$.

Define $T : V \to I(\psi)$ by $T(x)(p) = L(\rho(p) x)$. For $u \in U_{n+1}$ we get $T(x)(u p) = L(\rho(u) \rho(p) x) = \psi(u) T(x)(p)$, so $T(x) \in I(\psi)$. The map $T$ intertwines $\rho|_{P_{n+1}}$ with right translation. Its image is a subrepresentation of $I(\psi)$, and it is nonzero since $T(x)(1) = L(x)$ and $L \neq 0$. By the lemma, $I(\psi)$ is irreducible, so $T$ is onto. The two spaces have the same dimension $\prod_{i=1}^{n} (q^i - 1)$, so $T$ is an isomorphism. $\square$

**Theorem 6.4.10 (Cuspidal representations and the mirabolic subgroup).** For each finite field $k$ and each $n \geq 0$:

1. there is an irreducible cuspidal representation of $\mathrm{GL}_{n+1}(k)$ on a finite-dimensional space;
2. the conclusion of the mirabolic restriction theorem holds for every nontrivial $\psi_0$ and every irreducible cuspidal representation of $\mathrm{GL}_{n+1}(k)$.

Lean: `CompanionTheory.Mirab.cuspidalMirabolic`.

*Proof.* Part 1 is the existence of cuspidal representations, proved elsewhere in the development. Classically, the cuspidal representations of $\mathrm{GL}_{n+1}(k)$ are attached to the regular characters of $\mathbb{F}_{q^{n+1}}^\times$ (Digne and Michel, *Representations of Finite Groups of Lie Type*, Chapters 11 to 15). Part 2 is the theorem above. $\square$

**Remark 6.4.11.** For $n = 0$ every representation of $\mathrm{GL}_1(k) = k^\times$ is cuspidal, since there is no nonconstant monotone $b$ on one index, and $P_1$ and $U_1$ are trivial. The theorem is the statement of [Theorem 1.6.4 of Volume 8](/entry/cuspidal-mirabolic-holds/), which enters the proof as a published input.

**Remark 6.4.12 (Formalization).** The lemma on the irreducibility of $I(\psi)$ and its dimension are proved in `IndIrr.lean` (line 122) and `IndDim.lean` (lines 92 to 99). `IndFacts.lean` (lines 15 to 25) repeats them as wrappers. The whole folder of these proofs is duplicated under `Development/WeilBound/CoreStatements/RegularisedThetaMirabolic/CuspidalMirabolic/`. The dimension formula with $\dim V_\psi$ and the Gelfand-Graev multiplicity one theorem are used as proved inputs; we have not unfolded their proofs, and the description of the first through derivatives is the classical argument, not a reading of the code.
