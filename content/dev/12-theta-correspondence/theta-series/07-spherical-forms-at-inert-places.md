---
title: Spherical forms at inert places
decls:
  - PositivityTheory.Sph.M2.locMod
  - PositivityTheory.Sph.modSt2
  - PositivityTheory.Sph.sphFun_of_modSt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Spherical forms at inert places

This section proves that at a place where the CM extension does not split, two local [[Weil representations|H3Q2703KKV]] with a common unitary group $U_W$ have spherical linear forms with the same values on the $U_W$ orbits of their vacuum vectors. The key input is an index formula in a Siegel parabolic subgroup: the two indices of its integral points in their conjugates by $p$ differ by a power of $|\det p_{11}|$. We prove it first over a local field and then transfer it to inert places of a number field. The [spherical closure](/entry/close-sph/) of the next section uses the result at the inert places outside the finite set of bad places.

### The local index formula

Let $L$ be a field with a valuation with values in $\mathbb{Z} \cup \{\infty\}$. Write $\operatorname{ord}$ for the valuation, with $\operatorname{ord} 0 = 0$ by convention, and $\mathcal{O}_L$ for the ring of integers.

**Definition 3.7.1 (Unramified involution).** A triple $(\varpi, c, q)$ of $\varpi \in L$, a ring map $c : L \to L$ and $q \in \mathbb{N}$ is an *unramified involution* if $c \circ c = \mathrm{id}$, $c$ preserves the valuation, $c(\varpi) = \varpi$, $\operatorname{ord} \varpi = 1$, there is $x \in \mathcal{O}_L$ with $\operatorname{ord}(c(x) - x) = 0$, $q \ge 2$, and the residue field of $\mathcal{O}_L$ has $q^2$ elements.

This is the situation of an unramified quadratic extension: $c$ is its Galois involution, $\varpi$ is a uniformizer of $L$ and of the fixed field, and $q$ is the size of the residue field of the fixed field.

**Definition 3.7.2 (Siegel parabolic).** Let $m \ge 0$ and let $W_m = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ in $M_{2m}(L)$, in blocks of size $m$. Let $G_W$ be the group of $g \in \mathrm{GL}_{2m}(L)$ that preserve the [[Hermitian form|8NJ7XY6F1S]] given by $W_m$ and $c$. Put $K_W = G_W \cap \mathrm{GL}_{2m}(\mathcal{O}_L)$, let $P_W$ be the group of block upper triangular elements of $G_W$, and put $K_P = P_W \cap K_W$. For $p \in P_W$ write $p_{11}$ for its upper left block.

For subgroups $H$ and $K$ of a group, an index $[K : K \cap H]$ below is a natural number, and it is $0$ when the index is infinite.

**Lemma 3.7.3 (Local modulus).** Let $(\varpi, c, q)$ be an unramified involution of $L$, let $m \ge 0$ and let $p \in P_W$. Then
$$[K_P : K_P \cap p^{-1} K_P\, p] = q^{-2m \operatorname{ord} \det p_{11}}\, [K_P : K_P \cap p K_P\, p^{-1}].$$

Lean: `PositivityTheory.Sph.M2.locMod`

*Proof.* Three facts enter. First, $K_P$ and $p K_P p^{-1}$ are commensurable: both indices $[K_P : K_P \cap p K_P p^{-1}]$ and $[p K_P p^{-1} : K_P \cap p K_P p^{-1}]$ are finite and nonzero. Second, let $z = \operatorname{diag}(\varpi \cdot 1_m, \varpi^{-1} \cdot 1_m) \in P_W$. Conjugation by $z$ fixes the diagonal blocks and multiplies the upper right block by $\varpi^2$, so $z K_P z^{-1} \subset K_P$, with index $q^{2m^2}$. Third, a function $\chi : P_W \to \mathbb{R}$ that is multiplicative, positive, trivial on $K_P$ and has $\chi(z) = 1$ is trivial on $P_W$.

Put $\delta(p) = [K_P : K_P \cap p^{-1} K_P p] / [K_P : K_P \cap p K_P p^{-1}]$. By the first fact $\delta$ is positive. It is $\mu(p K_P p^{-1}) / \mu(K_P)$ for a left invariant measure $\mu$ on the commensurability class of $K_P$, so it is multiplicative. Put $\chi(p) = q^{2m \operatorname{ord} \det p_{11}} \delta(p)$. The map $p \mapsto \det p_{11}$ is multiplicative on block upper triangular matrices, so $\chi$ is multiplicative. On $K_P$ the block $p_{11}$ is invertible over $\mathcal{O}_L$ and $\delta = 1$, so $\chi = 1$. At $z$, the inclusion $z K_P z^{-1} \subset K_P$ gives $K_P \subset z^{-1} K_P z$, so $\delta(z) = q^{-2m^2}$, and $\operatorname{ord} \det z_{11} = m$. So $\chi(z) = 1$, and the third fact gives $\chi = 1$ on $P_W$. This is the claim. $\square$

### The global index formula

Let $F$ and $E$ be number fields with an involution $\sigma$ of $E$ over $F$, a base datum $B$ that is good for $\sigma$, and a skew-Hermitian space $W$ of dimension $d$ over $E$ with the [[unitary group|0R9R0Y1HDK]] $U_W$ over the adeles, as in the [theta matching chapter](/proof/theta-matching/). Let $v$ be a finite place of $F$ that is inert in $E$, and let $w$ be the place of $E$ above it. Let $C$ be a $d \times m$ matrix with adelic entries whose columns span a Lagrangian at $v$, and which is adapted at $v$. Let $P_v(C)$ be the group of $p \in U_W(F_v)$ with $p C = C t$ and $p^{-1} C = C t'$ for some matrices $t, t'$. Let $K_v$ be the integral subgroup of $U_W(F_v)$. Write $|u|_v$ for the modulus of $u \in F_v^\times$ for the [[Haar measure|CE0V9686M8]] of $F_v$.

**Theorem 3.7.4 (Global modulus at inert places).** Let $v$, $C$ be as above, let $p \in P_v(C)$ with $p C = C t$, and let $u = N_{E_w/F_v}(\det t_w)$. Then, with $K = P_v(C) \cap K_v$,
$$[K : K \cap p^{-1} K p] = |u|_v^m\, [K : K \cap p K p^{-1}].$$

Lean: `PositivityTheory.Sph.modSt2`

*Proof.* A basis of $W$ at $v$ adapted to the Lagrangian identifies $U_W(F_v)$ with the group $G_W$ for $E_w$ with its conjugation $c$. This identification is a group isomorphism. It carries $K_v$ onto the integral points, $P_v(C)$ onto $P_W$, and an element $p$ with $p C = C t$ to a matrix with $\det p_{11} = (\det t)_w$. So the two indices of the claim are those of the [local lemma](/entry/loc-mod/) for the image of $p$. Since $E_w / F_v$ is unramified with residue field of size $q^2$, we have $|N_{E_w/F_v}(x)|_v = q^{-2 \operatorname{ord}_w x}$, and so $q^{-2m \operatorname{ord} \det p_{11}} = |u|_v^m$. $\square$

### Spherical forms

Fix a triple as in the [theta matching chapter](/proof/theta-matching/): a geometric datum with Hermitian spaces $V$ and $V'$ of dimensions $a$ and $a'$ and the space $W$, Hecke characters $\alpha, \beta$ with a finite set $T$ of places, and Weil representations $\omega$ of $U_V \times U_W$ and $\omega'$ of $U_{V'} \times U_W$. A local representation $\omega_v$ of $\omega$ at $v$ acts on a local Schwartz space with a vacuum vector $\phi^0$. A linear form $l$ on this space is *spherical* if it vanishes on the augmentation subspace of $\omega$ at $v$, satisfies $l(\omega_v(1, k)\phi) = l(\phi)$ for $k \in K_v$ and all Schwartz functions $\phi$, and has $l(\phi^0) = 1$.

**Lemma 3.7.5 (Averages over a compact subgroup).** Let $U$ be a group with subgroups $K, P \subset U$ such that $U = P K$, every $h \in U$ has $h^{-1} \in K h K$, and $[K : K \cap h K h^{-1}]$ is finite for $h \in U$. Let $f, f' : U \to \mathbb{C}$ with $f(1) = f'(1) = 1$, $f(p g k) = f(p) f(g)$ and $f'(p g k) = f'(p) f'(g)$ for $p \in P$, $g \in U$, $k \in K$, and
$$f(p) f'(p)\, [K_P : K_P \cap p K_P p^{-1}] = [K_P : K_P \cap p^{-1} K_P p], \qquad K_P = P \cap K.$$
Then for each $h \in U$ the averages of $k \mapsto f(k h)$ and $k \mapsto f'(k h)$ over $K / (K \cap h K h^{-1})$ are equal.

*Proof.* By $U = P K$ and the right $K$ invariance, the average of $f$ at $h$ is a sum of $f(p)$ over the cosets $p K_P$ with $p \in P \cap K h K$. The orbit of $K_P$ through the coset of $p^{-1}$ has $[K_P : K_P \cap p K_P p^{-1}]$ elements, and $K h K = K h^{-1} K$ makes $p \mapsto p^{-1}$ preserve the set of cosets. Regroup the sum for $f'$ by these orbits and use the relation. $\square$

**Theorem 3.7.6 (Spherical forms agree).** Assume that the global index formula holds for all data. Let $v$ be a finite place of $F$ such that there is no $F$-algebra map $E \to F_v$. Let $\omega_v$ and $\omega'_v$ be local representations of $\omega$ and $\omega'$ at $v$ whose vacuum vectors are fixed by $\omega_v(1, k)$ and $\omega'_v(1, k)$ for all $k \in K_v$. Then there are spherical forms $l$ for $\omega_v$ and $l'$ for $\omega'_v$ with
$$l(\omega_v(1, h)\phi^0) = l'(\omega'_v(1, h)\phi'^0) \quad \text{for all } h \in U_W(F_v).$$

Lean: `PositivityTheory.Sph.sphFun_of_modSt`

*Proof.* The place $v$ is inert in $E$ and $v \notin T$. Since $d$ is even (this is part of the data of a triple), there is a Lagrangian $C$ at $v$, adapted at $v$, with $U_W(F_v) = P_v(C) K_v$ and $a + a' = 2m$. We use the following facts on the local Weil representations. There are linear forms $l_0$ and $l'_0$, nonzero at the vacuum vectors, that are eigenforms of $P_v(C)$. For $p \in P_v(C)$ with $p C = C t$, the determinant $\det t_w$ is a unit of $E_w$; take a unit idele $z$ with component $\det t_w$ at $w$ that is trivial at the finite places other than $v$, and put $u = N(\det t_w)$. Then
$$l_0(\omega_v(1, p)\phi) = \beta(z) |u|_v^{a/2} l_0(\phi), \qquad l'_0(\omega'_v(1, p)\phi) = \alpha(z) |u|_v^{a'/2} l'_0(\phi),$$
and $\alpha(z) \beta(z) = 1$. The Cartan symmetry $h^{-1} \in K_v h K_v$ holds, and the indices $[K_v : K_v \cap h K_v h^{-1}]$ are finite.

Average $l_0$ over $K_v$ to get a spherical form $l$. Then $l(\omega_v(1, h)\phi^0)$ is the average over $K_v / (K_v \cap h K_v h^{-1})$ of $f(k h)$, with $f(g) = l_0(\omega_v(1, g)\phi^0) / l_0(\phi^0)$. Do the same for $l'$ and $f'$. By the eigenvalues above and the [global index formula](/entry/mod-st2/),
$$f(p) f'(p)\, [K : K \cap p K p^{-1}] = |u|_v^{(a + a')/2} [K : K \cap p K p^{-1}] = [K : K \cap p^{-1} K p].$$
The lemma on averages above, with $U = U_W(F_v)$, $K = K_v$ and $P = P_v(C)$ then gives the claim. $\square$

**Remark 3.7.7 (Formalization).** The lemma is [LocMod.lean](lean:Development/WeilBound/ThetaLifts/SphericalLattices/LocMod.lean#L8), proved as `locMod_of locComm zCount gen` from the three facts of its proof. The global formula is [ModSt2.lean](lean:Development/WeilBound/ThetaLifts/SphericalLattices/ModSt2.lean#L7), `modSt_of chart locMod`, where `chart` is the identification. The spherical forms are [FunTop.lean](lean:Development/WeilBound/ThetaLifts/SphericalLattices/FunTop.lean#L13), `sphFun_of` applied to the hypothesis `ModSt` and to nine statements proved in the same folder: `countSt` (the lemma on averages), `avgSt`, `pInvSt`, `unitLiftSt`, `charSt`, `evInvSt`, `siegSt`, `cartanSt2` and `finSt`. The isometry predicate of $G_W$, the predicates "Lagrangian at $v$" and "adapted at $v$", the eigenform predicate of $l_0$ and the skew-Hermitian predicate on $W$ (with two integers $r, s$) are not unfolded here. The indices are natural numbers, so an infinite index counts as $0$. The hypothesis of the spherical forms is a place with no $F$-algebra map $E \to F_v$, not "inert": the proof derives that $v$ is inert. The user [`theoremK_head2`](/entry/theorem-k-head2/) fills the hypothesis `ModSt` with `modSt2`, so the theorem holds without hypothesis. FunSieg.lean declares `siegSt` twice, at L30 in a sub-namespace and at L64 as an alias.
