---
title: Torsion of tensor data
decls:
  - GlobalTheory.Mum.TensTor.tate_tens
  - GlobalTheory.T.tensorDegenerationData_torsion_isometry_onto
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Torsion of tensor data

This section proves that a full level structure passes from degeneration data $D$ to a tensor product $D'$ of $D$ with a unimodular matrix. Symplectic bases of the torsion classes of $D$ at all levels, one copy for each of the $r$ factors, give a full level structure on $D'$ of the type of a unitary datum. The result supplies the level structure, condition 4 of unitary PEL type, in [the theorem on the unitary type of a tensor product](/entry/tens-pel-ok/). For level structures on abelian varieties see [Siegel moduli schemes and level structures](/learn/abelian-varieties/#siegel-moduli-schemes-and-level-structures) in Volume 1.

Throughout, $R$ is a base with fraction field $K$, and $D = (B, L, \mathsf{X}, c, \psi, \tau)$ are degeneration data over $R$. We write $\widetilde G$ for the Raynaud extension of $D$ and $F$ for an algebraically closed field that contains $K$.

### Torsion classes

A point of $\widetilde G$ with values in $F$ is a pair $g = (b, s)$: a point $b \in B(F)$ and, for each $\chi \in \mathsf{X}$, a generator $s_\chi$ of the fibre of $\Lambda(L)^{-1}$ at $(c(\chi), b)$, where $\Lambda(L)$ is the line bundle with fibre $L_{x + y} \otimes L_x^{-1} \otimes L_y^{-1} \otimes L_0$ at $(x, y)$. We require $s_0 = 1$ and $s_{\chi + \chi'} = s_\chi s_{\chi'}$ through the cubical structure of $L$. Points add by adding the points $b$ and multiplying the generators through the cubical structure. The periods give a homomorphism $\iota : \mathsf{X} \to \widetilde G(F)$, with $\iota(y) = (c(y), \tau(y, \cdot))$.

**Definition 4.8.1 (Torsion class).** Let $k \geq 1$. A *torsion point of level $k$* of $D$ over $F$ is a pair $p = (y, g)$ with $y \in \mathsf{X}$ and $g \in \widetilde G(F)$ such that $k g = \iota(y)$. Two such points are *equivalent* if there is $z \in \mathsf{X}$ with
$$p' = (y + k z,\ g + \iota(z)).$$
A *torsion class of level $k$* is an equivalence class. We write $Q_k(D)(F)$ for the set of classes.

Lean: `ReciprocityTheory.ChartRestriction.G.Out.QkPt` (also `ReciprocityTheory.ChartRestriction.G.Out.QkPt.Equiv`, the equivalence).

The set $Q_k(D)(F)$ is the group of points of order dividing $k$ of the quotient $\widetilde G(F) / \iota(\mathsf{X})$: the class of $(y, g)$ is the image of $g$. Classes add by $(y, g) + (y', g') = (y + y', g + g')$. If $\mathcal{O}$ acts on $D$, then $a \in \mathcal{O}$ acts by $a (y, g) = (a y, a g)$. When $D$ comes from an abelian variety $A$ over $K$, the group $Q_k(D)(F)$ is the group $A[k](F)$ in the classical picture of Mumford.

The *Weil pairing* of level $k$ is defined with theta families of level $k$. A torsion point $p = (y, g)$, with a generator of $L_0^{k} \otimes L_b^{-k}$, acts on such families by a translation by $b$ and a shift of the index by $y$. For two torsion points $p, q$ and a root of unity $\zeta$ in $F$, we say that *the Weil pairing of $p$ and $q$ is $\zeta$* if, for all choices of generators and all families, the result of letting $p$ act and then $q$ is $\zeta$ times the result of letting $q$ act and then $p$.

### Full level structures

Let $E$ be a CM field with host data $H$ and let $\Lambda$ be a unitary datum for $H$ with form $\langle\ ,\ \rangle$, as in [the section on unitary factors](/entry/tens-pel-ok/).

**Definition 4.8.2 (Full level structure).** Let $D$ carry an $\mathcal{O}_E$-module structure on $\mathsf{X}$ and an action $o$ of $\mathcal{O}_E$. A *full level structure of type $\Lambda$* on $(D, o)$ over $F$ consists of elements $\zeta_n \in F^\times$ for $n \geq 1$ and maps $\mathrm{ev}_n : \Lambda \to Q_n(D)(F)$ such that, for all $n, m \geq 1$:

1. $\zeta_n$ is a primitive $n$-th root of unity and $\zeta_{nm}^m = \zeta_n$;
2. $\mathrm{ev}_n$ is additive and $\mathcal{O}_E$-linear;
3. $\mathrm{ev}_n(a) = \mathrm{ev}_n(b)$ if and only if $a - b \in n \Lambda$, and $\mathrm{ev}_n$ is onto;
4. for each $a \in \Lambda$, $m$ times a point of the class $\mathrm{ev}_{nm}(a)$ is a point of the class $\mathrm{ev}_n(a)$;
5. the Weil pairing of $\mathrm{ev}_n(a)$ and $\mathrm{ev}_n(b)$ is $\zeta_n^{\langle a, b\rangle}$.

Lean: `ReciprocityTheory.ChartRestriction.G.Geo.Tor.TateIsoQ`.

So a full level structure is a compatible system of isomorphisms $\Lambda / n \Lambda \cong Q_n(D)(F)$ that carry the form $\langle\ ,\ \rangle$ to the Weil pairing. In condition 4 the multiple keeps the lattice part $y$ and multiplies the point $g$ by $m$.

### The theorem

**Theorem 4.8.3 (Torsion of tensor data).** Let $E$ be a CM field with host data $H$, let $D$ and $D'$ be degeneration data over $R$, let $r \geq 0$ and $W \in M_r(\mathbb{Z})$, and put $S = W + W^{T}$. Assume that $S$ is positive definite and $\det S = \pm 1$. Let a tensor structure of $D'$ over $D$ with matrix $W$ be given, and a ring map $\rho : \mathcal{O}_E \to M_r(\mathbb{Z})$ with $\rho(a)^T S = S \rho(\bar a)$ for all $a$ and $W = S \rho(w_0)$. Let $\mathsf{X}'$ carry an $\mathcal{O}_E$-module structure and $D'$ an action $o$ of $\mathcal{O}_E$, such that the tensor structure is $\mathcal{O}_E$-linear for $\rho$ and the twist condition holds. Let $\Lambda$ be a unitary datum for $H$, let $g \geq 0$ and let $e : \Lambda \to (\mathbb{Z}^g \times \mathbb{Z}^g)^r$ be an additive isomorphism, with $g = g_B + \operatorname{rank} \mathsf{X}$, such that $e(a x)_i = \sum_j \rho(a)_{ij} e(x)_j$ and
$$\langle x, y \rangle = \sum_{i, j} S_{ij} \bigl( e(x)_i' \cdot e(y)_j'' - e(x)_i'' \cdot e(y)_j' \bigr),$$
where $e(x)_i = (e(x)_i', e(x)_i'')$. Let $(\zeta_n)_{n \geq 1}$ be primitive roots of unity in $F$ with $\zeta_{nm}^m = \zeta_n$, and let $\mathrm{ev}_n : \mathbb{Z}^g \times \mathbb{Z}^g \to Q_n(D)(F)$ be maps that satisfy conditions 2 to 4 of a full level structure (without the $\mathcal{O}_E$-linearity), and condition 5 for the standard symplectic form $u' \cdot v'' - u'' \cdot v'$. Then $(D', o)$ has a full level structure of type $\Lambda$ over $F$ whose roots of unity are the $\zeta_n$.

Lean: `GlobalTheory.Mum.TensTor.tate_tens` (also `GlobalTheory.T.tensorDegenerationData_torsion_isometry_onto`, a second name).

*Proof.* We describe torsion classes of $D'$ through their components. Let $p'$ be a torsion point of level $n$ of $D'$ and $(p_1, \dots, p_r)$ torsion points of level $n$ of $D$. We say that $p'$ *corresponds* to $(p_i)$ if the tensor structure carries $p'$ to $(p_i)$: the lattice part of $p'$ goes to the lattice parts of the $p_i$ under $\mathsf{X}' \cong \mathsf{X}^r$, and the point of $\widetilde G'$ goes to the points of $\widetilde G$ under the projections $B' \to B$ and the isomorphism of line bundles. This is read in numerical models of $D$ and $D'$ over $F$, which exist since $F$ is algebraically closed. We use six facts about this relation, all proved from the tensor structure:

(a) every tuple $(p_i)$ has a corresponding $p'$;

(b) if $p'$ corresponds to $(p_i)$, $q'$ to $(q_i)$ and $s'$ to $(p_i + q_i)$, then $s'$ is equivalent to $p' + q'$;

(c) if $\det S = \pm 1$, then $p'$ and $q'$ are equivalent if and only if $p_i$ and $q_i$ are equivalent for every $i$;

(d) if $\det S = \pm 1$, every $p'$ corresponds to some tuple;

(e) the relation is compatible with multiplication by $m$ from level $nm$ to level $n$;

(f) if the Weil pairing of $p_i$ and $q_j$ is $z_{ij}$ for all $i, j$, then the Weil pairing of $p'$ and $q'$ is $\prod_{i, j} z_{ij}^{S_{ij}}$.

There is also a linearity fact: (g) if $p'$ corresponds to $(\mathrm{ev}_n(a_j))_j$ and $q'$ corresponds to $(\mathrm{ev}_n(\sum_j \rho(x)_{ij} a_j))_i$, then $q'$ is equivalent to $x p'$. This uses the relation $\rho(a)^T S = S \rho(\bar a)$, the $\mathcal{O}_E$-linearity of the tensor structure, and conditions 2 and 3 for the maps $\mathrm{ev}_n$.

Now define $\mathrm{ev}'_n(a)$, for $a \in \Lambda$, as a torsion point of $D'$ that corresponds to the tuple $(\mathrm{ev}_n(e(a)_j))_j$; it exists by (a). We check the conditions.

Additivity follows from (b), since $e$ is additive and each $\mathrm{ev}_n$ is additive. Linearity follows from (g), since $e(x a)_i = \sum_j \rho(x)_{ij} e(a)_j$. For the kernel, (c) says that $\mathrm{ev}'_n(a)$ and $\mathrm{ev}'_n(b)$ are equivalent if and only if $e(a)_i \equiv e(b)_i \pmod n$ for all $i$; as $e$ is an isomorphism this means $a - b \in n \Lambda$. For surjectivity, let $p'$ be a class; by (d) it corresponds to a tuple $(p_i)$, each $p_i$ is $\mathrm{ev}_n(c_i)$ up to equivalence, and with $a = e^{-1}(c)$ fact (c) shows that $\mathrm{ev}'_n(a)$ is equivalent to $p'$. Condition 4 is (e) applied componentwise.

For the pairing, the Weil pairing of $\mathrm{ev}_n(e(a)_i)$ and $\mathrm{ev}_n(e(b)_j)$ is $\zeta_n^{e(a)_i' \cdot e(b)_j'' - e(a)_i'' \cdot e(b)_j'}$. By (f) the Weil pairing of $\mathrm{ev}'_n(a)$ and $\mathrm{ev}'_n(b)$ is
$$\begin{aligned} \prod_{i, j} \bigl( \zeta_n^{e(a)_i' \cdot e(b)_j'' - e(a)_i'' \cdot e(b)_j'} \bigr)^{S_{ij}} &= \zeta_n^{\sum_{i, j} S_{ij} ( e(a)_i' \cdot e(b)_j'' - e(a)_i'' \cdot e(b)_j' )} \\ &= \zeta_n^{\langle a, b\rangle}, \end{aligned}$$
by the rule $\zeta^{\sum_k m_k} = \prod_k \zeta^{m_k}$ and the formula for the form. The roots of unity of the structure are the $\zeta_n$ by construction. $\square$

The hypotheses that $S$ is positive definite, that $W = S \rho(w_0)$, the twist condition and the value of $g$ are not used in the proof. They are the hypotheses of the theorem on the unitary type of a tensor product, where the result is applied.

**Remark 4.8.4 (Formalization).** The second name is a wrapper, proved by a `first | exact` tactic. The proof ([TensorDegenerationDataTorsionIsometryOnto.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TensorDegenerationDataTorsionIsometryOnto.lean#L32)) takes the numerical models from `GlobalTheory.T.exists_degenerationValues_algClosed_field`; fact (a) is `GlobalTheory.T.exists_tensor_torsion_point_of_component_tuple`, (b) is `GlobalTheory.T.tensor_torsion_add_componentwise`, (c) is `GlobalTheory.T.tensor_torsion_point_equiv_iff_components_equiv`, (d) is `GlobalTheory.T.exists_component_tuple_tensor_torsion_unimodular`, (e) is `GlobalTheory.T.tensor_torsion_tower_nsmul_componentwise`, (f) is `GlobalTheory.T.weil_pairing_tensor_torsion_eq_prod_components` and (g) is `GlobalTheory.T.tensorQuotientTorsion_orderAction_matrix`. The power rule is the helper `GlobalTheory.Mum.TensTor.zpow_sum_tens`. The correspondence is `GlobalTheory.Mum.TensTor.PtRel`, defined through the numerical models; we did not unfold it further. The positive definiteness, the relation $W = S\rho(w_0)$, the twist condition `TraceFormTwistIso` and the equation for $g$ are bound to `_` at line 33 and never used. The Weil pairing is the relation `WeilQkIs`, a statement for all choices of families and generators; we did not check that such choices exist, so for given points the relation may hold for more than one $\zeta$.
