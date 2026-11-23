---
title: Level splitting of the flag parabolic
decls:
  - PI.LevelKSplit.W.SemiT.homeoNH
  - PI.LevelKSplit.W.SemiT.semi_gen
  - PI.LevelKSplit.W.SemiT.semidirect_topological_all
  - PI.LevelKSplit.W.NCH.heisenberg_parabolic
  - PI.LevelKSplit.W.NCH.heisenberg_parabolic_all
  - PI.LevelKSplit.W.Top6.levelSplitting_of_heisenberg_levi
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Level splitting of the flag parabolic

This section studies a unipotent subgroup $S$ of a unitary group over the finite adeles that fixes a flag $e_1, \dots, e_r, z$. We prove that $S$ is a topological semidirect product $N \rtimes H$, where $N$ is unipotent and $H$ is the unitary group of a complement. We prove that the part of $N$ that fixes $e_1, \dots, e_r$ is a Heisenberg group. From these facts and one assumption on a Levi part, we deduce that the volume of the level subgroup of $S$ is the product of the volumes of its parts in $N$ and $H$. This *level splitting* is the result [Theorem 4.6.1](/entry/level-s-all-split/), which serves the volume computations of the mass formula. For the group theory see [unitary groups](/learn/groups/#unitary-groups), [parabolic subgroups](/learn/groups/#parabolic-subgroups) and [the Heisenberg group](/learn/groups/#the-heisenberg-and-metaplectic-groups).

### The groups

In this section $F$ is a number field and $E$ is a field with an $F$-algebra structure and an $F$-automorphism $\sigma$. The pair is a *CM extension* if $F$ is totally real, $E$ is a totally complex number field, $[E : F] = 2$, and $\tau(\sigma x) = \overline{\tau(x)}$ for every embedding $\tau \colon E \to \mathbb{C}$. Then $\sigma^2 = 1$. A matrix $J \in M_M(E)$ is *Hermitian nondegenerate* if $\sigma(J_{ji}) = J_{ij}$ for all $i, j$ and $\det J \neq 0$. It defines the form
$$h(x, y) = \sum_{i, j} \sigma(x_i)\, J_{ij}\, y_j, \qquad x, y \in E^M,$$
which is $\sigma$-linear in $x$ and linear in $y$. For a commutative $F$-algebra $R$, $\sigma$ and $h$ extend to $R \otimes_F E$ and $(R \otimes_F E)^M$, and the *unitary group* is
$$U_J(R) = \{ g \in GL_M(R \otimes_F E) : \sigma(g)^{\mathsf T} J g = J \}.$$
We use $R$ equal to the ring $\mathbb{A}_f$ of finite adeles of $F$, with its topology.

**Definition 6.8.1 (Standard frame).** Let $r \geq 0$ and $T \in F$. A *standard frame* of rank $r$ and norm $T$ is a tuple of vectors $e_1, \dots, e_r, f_1, \dots, f_r, z \in E^M$ with
$$h(e_a, e_b) = h(f_a, f_b) = 0, \quad h(e_a, f_b) = \delta_{ab}, \quad h(e_a, z) = h(f_a, z) = 0, \quad h(z, z) = -T, \quad T \neq 0.$$

Let $X = \operatorname{span}(e_a)$, $Y = \operatorname{span}(f_a)$, $U = X \oplus Y \oplus \operatorname{span}(z)$ and $W = U^{\perp}$. Since $h$ is nondegenerate on $U$, $E^M = U \oplus W$. Let $p_U$ be the projection onto $U$ along $W$, given by $p_U(v) = \sum_a h(f_a, v) e_a + \sum_a h(e_a, v) f_a - T^{-1} h(z, v) z$, and let $p_W = 1 - p_U$. Let $W' = (X \oplus Y)^{\perp} = \operatorname{span}(z) \oplus W$. All these extend to $R \otimes_F E$.

**Definition 6.8.2 (Flag subgroups).** Fix a standard frame and a commutative $F$-algebra $R$.

1. $S(R)$ is the group of $g \in U_J(R)$ with $g e_b - e_b \in \operatorname{span}(e_a : a < b)$ for each $b$ and $g z - z \in X$.
2. $H(R)$ is the group of $g \in U_J(R)$ that fix each $e_a$, each $f_a$ and $z$.
3. $N(R)$ is the group of $g \in U_J(R)$ with $g e_b - e_b \in \operatorname{span}(e_a : a < b)$ for each $b$ and $g v - v \in X$ for each $v \in X^{\perp}$.
4. $N_0(R) = \{ g \in N(R) : g e_a = e_a \text{ for all } a \}$ and $Z(R) = \{ g \in N(R) : g v = v \text{ for all } v \in X^{\perp} \}$.

Since $z \in X^{\perp}$, $N \subseteq S$, and clearly $H \subseteq S$. The group $H$ is the unitary group of $W$, extended by the identity on $U$. The group $N$ acts trivially on $X^{\perp}/X$, so it lies in the unipotent radical of the parabolic subgroup that stabilizes $X$.

**Definition 6.8.3 (Level subgroups).** For a set $\Lambda \subseteq E^M$ and a finite place $v$ of $F$, let $\Lambda_v$ be the $\mathcal{O}_v$-span of $\Lambda$ in $(F_v \otimes_F E)^M$. Let $K(\Lambda)$ be the set of $g \in U_J(\mathbb{A}_f)$ such that $g_v \Lambda_v = \Lambda_v$ at every finite place $v$. Let $K_S(\Lambda) = S \cap K(\Lambda)$, $K_N(\Lambda) = N \cap K(\Lambda)$ and $K_H(\Lambda) = H \cap K(\Lambda)$.

Three sets $\Lambda_X, \Lambda_W, \Lambda_Y$ are *adapted* to the frame if $\Lambda_X \subseteq X$, $\Lambda_Y \subseteq Y$, and each vector of $\Lambda_W$ is orthogonal to all $e_a$ and $f_a$.

### The semidirect product

**Theorem 6.8.4 (Semidirect decomposition).** Let $E/F$ be a finite extension with $\sigma^2 = 1$, $J$ Hermitian nondegenerate, and a standard frame. Let $R$ be a commutative $F$-algebra with a topology that makes it a topological ring. Then $H(R)$ normalizes $N(R)$, and the map $(n, h) \mapsto n h$ is a homeomorphism $N(R) \times H(R) \to S(R)$.

Lean: `PI.LevelKSplit.W.SemiT.semi_gen` (also `PI.LevelKSplit.W.SemiT.homeoNH`, the homeomorphism).

*Proof.* For $g \in S(R)$ let $\pi(g) = p_U + p_W\, g\, p_W$. We show that $\pi(g) \in H(R)$. The element $g$ is unitary and maps $X$ to $X$, so it maps $X^{\perp} = X \oplus \operatorname{span}(z) \oplus W$ to itself. For $w \in W$, $g w \in X^{\perp}$ and $h(z, g w) = h(g z, g w) - h(g z - z, g w) = h(z, w) - 0 = 0$, since $g z - z \in X$. So $g w \in X \oplus W$, and $p_W g$ on $W$ is the map induced by $g$ on $(X \oplus W)/X \cong W$. This map is unitary for $h$ on $W$, so $\pi(g)$ is unitary. It fixes $U$ pointwise, so $\pi(g) \in H(R)$. The same computation shows that $\pi$ is multiplicative on $S(R)$, that $\pi(n) = 1$ for $n \in N(R)$ and that $\pi(h) = h$ for $h \in H(R)$. Then $g\pi(g)^{-1}$ acts on $X^{\perp}/X$ as the identity, and it moves the vectors $e_b$ as $g$ does, so $g \pi(g)^{-1} \in N(R)$. Hence $g \mapsto (g \pi(g)^{-1}, \pi(g))$ is inverse to $(n, h) \mapsto n h$: indeed $\pi(nh) = \pi(n)\pi(h) = h$. The matrix entries of $\pi(g)$ are polynomials in those of $g$, so $\pi$ is continuous, and inversion is continuous on $U_J(R)$. So both maps are continuous. For $h \in H(R)$ and $n \in N(R)$, $h n h^{-1}$ fixes the flag of the $e_a$ as $n$ does, and $h$ maps $X^{\perp}$ to $X^{\perp}$ and fixes $X$, so $h n h^{-1} \in N(R)$. $\square$

**Corollary 6.8.5 (Semidirect decomposition over the adeles).** Let $E/F$ be a CM extension, $J$ Hermitian nondegenerate and $P$ a standard frame. Then $S(\mathbb{A}_f) = N(\mathbb{A}_f) \rtimes H(\mathbb{A}_f)$ as topological groups.

Lean: `PI.LevelKSplit.W.SemiT.semidirect_topological_all`.

*Proof.* This is the theorem for $R = \mathbb{A}_f$. The extension $E/F$ is finite because $E$ is finite over $\mathbb{Q}$. $\square$

### The Heisenberg structure

For $n \in N_0(R)$ and $1 \leq a \leq r$ let $y(n)_a = p_{W'}(n f_a)$, where $p_{W'}(x) = x - \sum_b h(f_b, x) e_b - \sum_b h(e_b, x) f_b$ is the projection onto $W'$. For $y = (y_1, \dots, y_r) \in W'^r$ let $s(y)$ be the linear map
$$s(y) v = v + \sum_a h(e_a, v)\Bigl(y_a - \tfrac12 \sum_b h(y_b, y_a)\, e_b\Bigr) - \sum_b h(y_b, v)\, e_b.$$
It fixes $X^{\perp} \cap Y^{\perp}$ up to $X$, and it maps $f_a$ to $f_a + y_a - \frac12 \sum_b h(y_b, y_a) e_b$. The term $-\frac12 h(y_b, y_a)$ makes $s(y)$ unitary.

**Theorem 6.8.6 (Heisenberg structure).** Let $E/F$ be a finite extension of a number field with $\sigma^2 = 1$, $J$ Hermitian nondegenerate and a standard frame. Over $R = \mathbb{A}_f$, there is a continuous map $s \colon W'^r \to U_J(R)$, with $y \colon U_J(R) \to (R \otimes_F E)^{M r}$ also continuous, such that:

1. $s(y) \in N_0$ for every $y$;
2. for every $n \in N_0$, $y(n) \in W'^r$ and $s(y(n))^{-1} n \in Z$;
3. $y(s(y)\, \zeta) = y$ for all $y$ and $\zeta \in Z$;
4. $Z \subseteq N_0$, and each element of $Z$ commutes with each element of $N_0$;
5. $s(y) s(y') s(y + y')^{-1} \in Z$ for all $y, y'$;
6. $N$ normalizes $Z$;
7. for $h \in H$ and $y \in W'^r$, $h s(y) h^{-1} = s(h y)$, where $h y = (h y_1, \dots, h y_r)$;
8. each element of $H$ commutes with each element of $Z$.

Lean: `PI.LevelKSplit.W.NCH.heisenberg_parabolic` (also `PI.LevelKSplit.W.NCH.heisenberg_parabolic_all`, the same for all CM extensions).

So $N_0$ is a central extension of the additive group $W'^r$ by $Z$, with section $s$, and $H$ acts on it through its linear action on $W'^r$. This is a Heisenberg group in the sense of [the Heisenberg group](/learn/groups/#the-heisenberg-and-metaplectic-groups).

*Proof.* Take $s$ as defined above, with $\frac12 \in F$. Unitarity of $s(y)$ is a computation with $h(e_a, e_b) = 0$, $h(e_a, f_b) = \delta_{ab}$ and $y_a \perp e_b, f_b$: the cross terms cancel because of the factor $\frac12$ and the Hermitian symmetry $h(y_b, y_a) = \sigma(h(y_a, y_b))$. Since $h(e_a, e_b) = 0$, $s(y)$ fixes each $e_b$; for $v \in X^{\perp}$, $s(y) v - v = -\sum_b h(y_b, v) e_b \in X$. So $s(y) \in N_0$, and $p_{W'}(s(y) f_a) = y_a$, which gives (3) for $\zeta = 1$. An element $\zeta \in Z$ fixes $X^{\perp}$ and $X$; unitarity forces $\zeta f_a - f_a \in X$, so $y(g\zeta) = y(g)$ for $g \in N_0$, which gives (3). For (2), let $n \in N_0$ and $g = s(y(n))^{-1} n \in N_0$. Since $n$ is unitary and fixes $X$, $h(e_a, n f_b) = \delta_{ab}$ and $n f_b \perp n f_a$, so $n f_b - f_b$ lies in $X \oplus W'$ with $W'$-part $y(n)_b$; the formula for $s$ then gives $g f_b = f_b + x_b$ with $x_b \in X$. For $v \in X^{\perp}$ write $g v - v = \sum_b c_b e_b$. Then $c_b = h(f_b, g v) - h(f_b, v) = h(g f_b - x_b, g v) - h(f_b, v) = -h(x_b, g v) = 0$, since $g v \in X^{\perp}$. So $g$ fixes $X^{\perp}$ and lies in $Z$. The commutator relations (4) to (6) and (8) follow because elements of $Z$ act as $v \mapsto v + \sum_a h(e_a, v) x_a$ with $x_a \in X$, and the elements of $N_0$ and $H$ fix $X$ pointwise and preserve $X^{\perp}$. In (5) the product $s(y) s(y') s(y+y')^{-1}$ fixes $X^{\perp}$ since the linear terms in $y$ add. For (7), $h$ fixes the $e_a$ and $f_a$ and preserves $h$, so conjugating the formula for $s(y)$ by $h$ replaces $y_a$ by $h y_a$. Continuity holds because $s(y)$ and $y(g)$ are polynomial in the coordinates. The second form follows because a CM extension has $[E : F] = 2$, so it is finite. $\square$

### The level splitting

The level splitting needs one more input, on a Levi part of $N$.

**Definition 6.8.7 (Levi hypothesis).** Let $E/F$, $J$ and a standard frame be given. The *Levi hypothesis* says that there are a closed subgroup $A \subseteq N(\mathbb{A}_f)$ and a continuous map $\ell \colon U_J(\mathbb{A}_f) \to U_J(\mathbb{A}_f)$ such that $\ell(n) \in A$ and $\ell(n)^{-1} n \in N_0$ for $n \in N$, $A \cap N_0 = \{1\}$, $N$ normalizes $N_0$, and each element of $H$ commutes with each element of $A$.

The group $A$ plays the role of the unipotent upper triangular matrices in $GL(X)$, which act on $X$ and on $Y$ by the dual action and trivially on $W'$.

**Theorem 6.8.8 (Level splitting).** Assume the Levi hypothesis for every CM extension, every Hermitian nondegenerate $J$ and every standard frame. Let $E/F$ be a CM extension, $J$ Hermitian nondegenerate, $P$ a standard frame, and $\Lambda_X, \Lambda_W, \Lambda_Y$ adapted to $P$, with $\Lambda = \Lambda_X \cup \Lambda_W \cup \Lambda_Y$. Let $\mu_N$ and $\mu_H$ be Haar measures on $N(\mathbb{A}_f)$ and $H(\mathbb{A}_f)$. Then there is a Haar measure $\mu_S$ on $S(\mathbb{A}_f)$ with
$$\int_S f\, d\mu_S = \int_N \int_H f(n h)\, d\mu_H(h)\, d\mu_N(n)$$
for each measurable $f \geq 0$, and for every such $\mu_S$,
$$\mu_S(K_S(\Lambda)) = \mu_N(K_N(\Lambda))\, \mu_H(K_H(\Lambda)).$$

Lean: `PI.LevelKSplit.W.Top6.levelSplitting_of_heisenberg_levi`.

*Proof.* First, $N$ has coordinates. By the Heisenberg structure and the Levi hypothesis, each $n \in N$ is $\ell(n) \cdot s(y) \cdot \zeta$ with unique $\ell(n) \in A$, $y \in W'^r$ and $\zeta \in Z$, and this gives a homeomorphism $A \times W'^r \times Z \to N$. Left translation by a fixed element is affine in these coordinates, and conjugation by $h \in H$ changes only the coordinate $y$, by the linear map $y \mapsto h y$ of (7) and (8). A unitary element preserves every additive Haar measure on $(\mathbb{A}_f \otimes_F E)^M$, so the linear map $y \mapsto h y$ preserves Haar measure on $W'^r$. Hence conjugation by $H$ preserves $\mu_N$. With the [semidirect decomposition over the adeles](/entry/semidirect-topological-all/), the product measure pushed forward by $(n, h) \mapsto n h$ is then a left Haar measure on $S$; this is the existence of $\mu_S$ with the product formula. Next, if $n \in N$, $h \in H$ and $n h \in K(\Lambda)$, then $h \in K(\Lambda)$. Indeed, $h$ fixes $\Lambda_X$ and $\Lambda_Y$ pointwise. For $w \in \Lambda_W$, $h w \in W'$, and $(n h) w - h w \in X$ because $h w \in X^{\perp}$ and $n \in N$. The sum $X \oplus W' \oplus Y$ is direct, and $\Lambda_v$ is the sum of the $\mathcal{O}_v$-spans of $\Lambda_X$, $\Lambda_W$, $\Lambda_Y$, which lie in $X$, $W'$, $Y$. So the $W'$-component of an element of $\Lambda_v$ lies in $\Lambda_v$. The $W'$-component of $(n h) w \in \Lambda_v$ is $h w$, so $h w \in \Lambda_v$. The same argument for $h^{-1}$ and $(n h)^{-1} = h^{-1} n^{-1}$ gives $h_v \Lambda_v = \Lambda_v$. Then also $n = (n h) h^{-1} \in K(\Lambda)$. So the indicator of $K(\Lambda)$ satisfies $1_K(n h) = 1_K(n) 1_K(h)$, and the product formula with $f = 1_{K(\Lambda)}$, which is measurable, gives the result. $\square$

**Remark 6.8.9 (Formalization).** The theorem takes two inputs, the Heisenberg structure for all CM extensions and the Levi hypothesis, but the first is proved above as `heisenberg_parabolic_all` ([HeisenbergParabolicAll.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/LevelSplitting/HeisenbergParabolicAll.lean#L41)); only the Levi hypothesis is a real input, and it is proved elsewhere as `levi_part_all`. The proof of the level splitting ([LevelSAllOfHL.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/LevelSplitting/LevelSAllOfHL.lean#L9)) passes the inputs to `levelSAll_of_semiNHS_heis_lev` with the proved results `modulus_all_extensions` (unitary maps preserve additive Haar measure) and `normal_conjugation_all`; we read the statements of these and the chain `levelSAll_of_parts`, `levelS_of`, not every proof. In the semidirect decomposition we read the statements of `piG_mem_H`, `mul_inv_piG_mem_N`, `piG_mul` and `norm_N`, and in the Heisenberg structure the statements of the lemmas on `sHG`; the arguments given above for them are ours. The level sets $\Lambda_X, \Lambda_W, \Lambda_Y$ are arbitrary sets of vectors, not lattices. The level splitting statement repeats the hypothesis that $J$ is Hermitian nondegenerate, which is already part of the quantifier over CM extensions, and it does not ask for $\sigma^2 = 1$, which follows from the CM condition. The map $y$ is defined on all of $U_J(\mathbb{A}_f)$, and its values lie in $W'^r$ only on $N_0$.
