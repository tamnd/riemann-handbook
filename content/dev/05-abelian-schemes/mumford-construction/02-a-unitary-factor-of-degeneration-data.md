---
title: A unitary factor of degeneration data
decls:
  - GlobalTheory.Mum.exists_pelOK_factor
  - GlobalTheory.T.exists_unitaryPELType_factor_degData
  - GlobalTheory.Mum.tens_pelOK
  - GlobalTheory.T.tensorDegData_unitary_type
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A unitary factor of degeneration data

This section proves the first step of [Mumford's construction](/entry/has-of-base/): every set of degeneration data with a non-zero character lattice is a direct factor of a set of degeneration data of unitary PEL type. The larger data are a tensor product of the given data with a unimodular lattice over the integers of a CM field, and the factor is cut out by an idempotent. Data of unitary PEL type carry an action of $\mathcal{O}_E$ and a full level structure on their torsion, and for such data the later sections construct a labelled cover. The section uses [Hermitian and skew-Hermitian forms](/learn/algebra/#hermitian-and-skew-hermitian-forms), [lattices in quadratic and Hermitian spaces](/learn/hermitian-lattices/#lattices-in-quadratic-and-hermitian-spaces) and [polarizations](/learn/abelian-varieties/#polarizations-and-zarhins-trick) from Volume 1.

Throughout, $R$ is a base in the sense of [the first section](/entry/has-of-base/), and degeneration data are taken with respect to the maximal ideal of $R$. For degeneration data $D$ we write $B$, $L$, $\mathsf{X}$, $c$, $\psi$ and $\tau$ as there, and $g_B$ for the relative dimension of $B$.

### Host data and unitary data

**Definition 4.2.1 (Host data).** Let $E$ be a CM field with ring of integers $\mathcal{O}_E$ and complex conjugation $a \mapsto \bar a$. *Host data* for $E$ consist of a prime $d$ with $d \equiv 7 \pmod{16}$, elements $s, w_0 \in \mathcal{O}_E$ with $s^2 = -d$ and $2 w_0 = 1 + s$, and a complex number $s_0$ with $s_0^2 = -d$. We require that $\mathcal{O}_E$ is unramified over the ring of integers of the maximal real subfield of $E$.

Lean: `ReciprocityTheory.ChartRestriction.G.Geo.Tor.Host`.

The ring $\mathcal{O}_E$ with $a \mapsto \bar a$ is a ring with involution. Since $d \equiv 3 \pmod 4$, the element $(1 + s)/2$ is integral, so $w_0$ exists as soon as $s$ does. An example is $E = \mathbb{Q}(\zeta_{21})$ with $d = 7$: it contains $\sqrt{-7}$, and it is unramified over its maximal real subfield.

**Definition 4.2.2 (Unitary datum).** Let $H$ be host data for $E$. A *unitary datum* for $H$ consists of a finite projective $\mathcal{O}_E$-module $\Lambda$; an alternating $\mathbb{Z}$-bilinear form $\langle\ ,\ \rangle$ on $\Lambda$ that is unimodular and satisfies $\langle a x, y\rangle = \langle x, \bar a y\rangle$; and integers $p, q \geq 0$ with $p + q = \operatorname{rank}_{\mathcal{O}_E} \Lambda$. We require a complex structure $J$ on $\Lambda \otimes \mathbb{R}$ that preserves the form, with $\langle J x, x\rangle > 0$ for $x \neq 0$, which commutes with $\mathcal{O}_E$ and on which $\mathcal{O}_E$ acts with signature $(p, q)$ at the embeddings $\tau$ with $\tau(s) = s_0$.

Lean: `ReciprocityTheory.ChartRestriction.G.Geo.Tor.Datum`.

Let $\mathcal{O}$ be a ring with involution $a \mapsto a^*$. An *action* of $\mathcal{O}$ on degeneration data $D$ is an action $a \mapsto [a]$ of $\mathcal{O}$ on $B$ by endomorphisms together with an $\mathcal{O}$-module structure on $\mathsf{X}$, such that $c(a y) = [a] \circ c(y)$ and such that $\tau$ is balanced: $\tau(a y, z)$ and $\tau(y, a^* z)$ correspond under $[a]$ and $[a^*]$.

**Definition 4.2.3 (Unitary PEL type).** Let $H$ be host data for $E$, let $\Lambda$ be a unitary datum for $H$, and let $D$ be degeneration data over $R$ with an action of $\mathcal{O}_E$. We say that $(\Lambda, D)$ is of *unitary PEL type* if the following hold.

1. $p = q$ and $p \geq 1$.
2. Twist condition. There is a rigidified generator of the line bundle with fibre $L_{x + [w_0] x} \otimes L_x^{-2} \otimes L_{[w_0]x}^{-1} \otimes L_0^{2}$ on $B$, under which $\tau(y, w_0 y)$ corresponds to $\psi(y)$ for every $y \in \mathsf{X}$. So $L$ is the restriction of $\Lambda(L)$ along $x \mapsto (x, [w_0]x)$, in a way that matches the periods.
3. Signature. For every algebraically closed field $F$ over $K$ and every ring map $\tau : \mathcal{O}_E \to F$, the multiplicity of $\tau$ in the Lie algebra of $B_F$ is a number $n$ with $n + \operatorname{rank}_{\mathcal{O}_E} \mathsf{X} = p$.
4. Level structure. For every such $F$ and every compatible system $(\zeta_n)$ of primitive roots of unity in $F$, there are maps $\Lambda \to Q_n(D)(F)$ to the torsion classes of level $n$, for all $n \geq 1$. They are additive and $\mathcal{O}_E$-linear, induce bijections $\Lambda / n\Lambda \cong Q_n(D)(F)$, are compatible as $n$ varies, and carry $\zeta_n^{\langle a, b\rangle}$ to the Weil pairing of the images of $a$ and $b$.

Lean: `GlobalTheory.Mum.PelOK`.

Conditions 1 and 3 say that the Lie algebra of the semi-abelian scheme that the data should give has signature $(p, p)$ at each embedding. Condition 4 is a full level structure on the torsion of the data.

### Tensor products and factors

**Definition 4.2.4 (Tensor product with a matrix).** Let $D$ and $D'$ be degeneration data over $R$, let $r \geq 0$ and let $W \in M_r(\mathbb{Z})$. A *tensor structure* of $D'$ over $D$ with matrix $W$ consists of homomorphisms $p_1, \dots, p_r : B' \to B$ that make $B'$ the product $B^r$; an isomorphism $\mathsf{X}' \cong \mathsf{X}^r$, $z \mapsto (z_1, \dots, z_r)$, with $p_i \circ c'(z) = c(z_i)$; and a generating isomorphism
$$L' \cong \bigotimes_{i, j} (p_i, p_j)^* \Lambda(L)^{W_{ij}},$$
under which
$$\psi'(z) = \prod_{i, j} \tau(z_i, z_j)^{W_{ij}}.$$
Let $\rho : \mathcal{O} \to M_r(\mathbb{Z})$ be a ring map and $o$ an action of $\mathcal{O}$ on $D'$. The tensor structure is *$\mathcal{O}$-linear for $\rho$* if $(a z)_i = \sum_j \rho(a)_{ij} z_j$ and $p_i \circ [a] = \sum_j \rho(a)_{ij}\, p_j$.

Lean: `GlobalTheory.Mum.Tens` (also `GlobalTheory.Mum.Tens.IsAct`, the linearity).

If $W + W^{T}$ is the identity, the tensor product is $D^r$ with the product line bundle.

**Definition 4.2.5 (Factor).** Let $D$ and $D'$ be degeneration data over $R$. A *factor* of $D'$ onto $D$ consists of a ring $\mathcal{O}$ with involution acting on $D'$; an idempotent $e \in \mathcal{O}$ and an element $f \in \mathcal{O}$; homomorphisms $i : B \to B'$ and $\pi : B' \to B$ with $\pi \circ i = 1$ and $i \circ \pi = [e]$; homomorphisms $\xi : \mathsf{X} \to \mathsf{X}'$ and $\eta : \mathsf{X}' \to \mathsf{X}$ with $\eta \circ \xi = 1$ and $\xi \circ \eta = e$; such that $c'(\xi y) = i \circ c(y)$. We require that $y \mapsto e^* f \xi(y)$ is injective with image $e^* \mathsf{X}'$, a generating isomorphism of $\Lambda(L)$ with the pullback of $\Lambda(L')$ along $(x, y) \mapsto (i(x), [f]\, i(y))$, and that under it $\tau(a, b)$ corresponds to $\tau'(\xi a, f \xi b)$. The factor is *algebraic* if $e^* e = b\, e^* f e$ for an integer $b > 0$, $e^* f e = e^* f^* e$, and $e = h\, e^* f e$ for some $h \in \mathcal{O}$.

Lean: `GlobalTheory.Mum.Factor` (also `GlobalTheory.Mum.Factor.Alg`, the algebraic condition).

The ring of a factor acts on $D'$, and the idempotent $e$ cuts $D$ out of $D'$: the abelian part $B$ is the image of $[e]$, and the lattice $\mathsf{X}$ is a direct summand of $\mathsf{X}'$. The pairing on $D$ is the pairing of $D'$ twisted by $f$. The algebraic condition makes $e^* f e$ a positive and symmetric element which generates $e$, as a polarisation does for a Rosati involution.

### The theorems

**Theorem 4.2.6 (Unitary type of a tensor product).** Let $E$ be a CM field with host data $H$, and let $D$ and $D'$ be degeneration data over $R$ with $\mathsf{X} \neq 0$. Let $r \geq 1$ and $W \in M_r(\mathbb{Z})$ be such that $S = W + W^{T}$ is positive definite with $\det S = \pm 1$. Suppose given a tensor structure of $D'$ over $D$ with matrix $W$, and a ring map $\rho : \mathcal{O}_E \to M_r(\mathbb{Z})$ with
$$\rho(a)^{T} S = S \rho(\bar a) \quad (a \in \mathcal{O}_E), \qquad W = S \rho(w_0).$$
Suppose given an $\mathcal{O}_E$-module structure on $\mathsf{X}'$ and an action of $\mathcal{O}_E$ on $D'$ for which the tensor structure is $\mathcal{O}_E$-linear for $\rho$ and which satisfies the twist condition. Then there is a unitary datum $\Lambda$ for $H$ such that $(\Lambda, D')$ is of unitary PEL type.

Lean: `GlobalTheory.Mum.tens_pelOK` (also `GlobalTheory.T.tensorDegData_unitary_type`, a second name).

*Proof.* The ring map $\rho$ makes $\mathbb{Z}^r$ a module over $\mathcal{O}_E$, which is torsion free; so $r = s\,[E : \mathbb{Q}]$ for an integer $s$, and $s \geq 1$ since $r \geq 1$. Put $g = g_B + \operatorname{rank}_{\mathbb{Z}} \mathsf{X}$. Let $\Lambda = (\mathbb{Z}^g \times \mathbb{Z}^g)^r$, with $\mathcal{O}_E$ acting by $\rho$ on the outer factor and with the form
$$\langle x, y\rangle = \sum_{i, j} S_{ij} \bigl( x_i' \cdot y_j'' - x_i'' \cdot y_j' \bigr), \qquad x_i = (x_i', x_i'').$$
The relation $\rho(a)^T S = S \rho(\bar a)$ makes $\langle\ ,\ \rangle$ Hermitian for $\mathcal{O}_E$, and $\det S = \pm 1$ makes it unimodular. Since $S$ is positive definite and $W = S \rho(w_0)$, this lattice is a unitary datum with $p = q = s g$. So $p \geq 1$, as $\mathsf{X} \neq 0$.

For the signature, the tensor structure identifies $B'$ with $B^r$ and $\mathsf{X}'$ with $\mathsf{X}^r$, with $\mathcal{O}_E$ acting through $\rho$. So $\operatorname{rank}_{\mathcal{O}_E} \mathsf{X}' = s \operatorname{rank}_{\mathbb{Z}} \mathsf{X}$, and each $\tau : \mathcal{O}_E \to F$ occurs in the Lie algebra of $B'_F$ with multiplicity $s g_B$. The sum is $s g = p$. The twist condition is a hypothesis.

For the level structure, let $F$ be algebraically closed over $K$ and $(\zeta_n)$ a compatible system of primitive roots of unity. The torsion classes of $D$ over $F$ have compatible symplectic bases: there are maps $(\mathbb{Z}^g \times \mathbb{Z}^g) \to Q_n(D)(F)$ which are additive, induce bijections modulo $n$, are compatible in $n$, and carry the standard symplectic form to the Weil pairing through $\zeta_n$. Through the isomorphism $\Lambda \cong (\mathbb{Z}^g \times \mathbb{Z}^g)^r$ and the tensor structure, [the result on torsion of tensor data](/entry/tensor-degeneration-data-torsion-isometry-onto/) turns these maps into maps $\Lambda \to Q_n(D')(F)$ with all the properties of condition 4, where the Weil pairing on $D'$ is matched with $\zeta_n^{\langle a, b\rangle}$ for the form $\langle\ ,\ \rangle$ built from $S$. $\square$

**Theorem 4.2.7 (Unitary factor).** Let $R$ be a base and $D$ degeneration data over $R$ with $\mathsf{X} \neq 0$. Then there are a CM field $E$ with host data $H$, a unitary datum $\Lambda$ for $H$, degeneration data $D'$ over $R$ with an $\mathcal{O}_E$-module structure on $\mathsf{X}'$ and an action of $\mathcal{O}_E$ on $D'$, such that $(\Lambda, D')$ is of unitary PEL type and there is an algebraic factor of $D'$ onto $D$.

Lean: `GlobalTheory.Mum.exists_pelOK_factor` (also `GlobalTheory.T.exists_unitaryPELType_factor_degData`, a second name).

*Proof.* We take $E = \mathbb{Q}(\zeta_{21})$ with its host data for $d = 7$; the field does not depend on $D$. Next we choose a lattice. From a positive definite Gram matrix of the trace form of $E$ one gets $r \geq 1$, a matrix $W \in M_r(\mathbb{Z})$ and $\rho : \mathcal{O}_E \to M_r(\mathbb{Z})$ such that $S = W + W^T$ is positive definite with $\det S = \pm 1$, $\rho(a)^T S = S \rho(\bar a)$, and $W = S \rho(w_0)$.

Since $S$ is positive definite and unimodular, there are degeneration data $D'$ over $R$ with a tensor structure over $D$ with matrix $W$. For any such tensor structure, the relations between $\rho$, $S$ and $W$ give an $\mathcal{O}_E$-module structure on $\mathsf{X}'$ and an action of $\mathcal{O}_E$ on $D'$, for which the tensor structure is $\mathcal{O}_E$-linear for $\rho$ and which satisfy the twist condition. By [the theorem on the unitary type of a tensor product](/entry/tens-pel-ok/), there is a unitary datum $\Lambda$ with $(\Lambda, D')$ of unitary PEL type. Finally, a tensor structure with $r \geq 1$ and with $S$ positive definite and unimodular gives an algebraic factor of $D'$ onto $D$. $\square$

**Remark 4.2.8 (Formalization).** Both second names are wrappers, proved by a `first | exact` tactic. The proof of the unitary factor theorem ([ExistsUnitaryPELTypeFactorDegData.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsUnitaryPELTypeFactorDegData.lean#L1)) composes `GlobalTheory.Mum.exists_host`, `GlobalTheory.Mum.unimodLattice`, `GlobalTheory.T.exists_tensorDegenerationData_of_unimodular_posDef`, `GlobalTheory.T.exists_ringOfIntegers_module_on_tensor_data`, the theorem on the unitary type, and `GlobalTheory.T.exists_algebraic_factor_of_unimodular_tensor`. The last three of these need only an admissible base. The host data are fixed: `GlobalTheory.HostModel.host` on $\mathbb{Q}(\zeta_{21})$. In the proof of the unitary type, the divisibility $r = s[E : \mathbb{Q}]$ is `GlobalTheory.T.finrank_dvd_of_ringOfIntegers_to_int_matrix`, the standard lattice is `GlobalTheory.T.exists_unitary_datum_standardLattice_tensor_unimodular`, the signature count is `GlobalTheory.T.lieMultiplicity_and_rank_tensorData_lattice`, the symplectic bases are `GlobalTheory.T.exists_compatible_symplectic_bases_levelPoints`, and the transfer of the level structure is [the result on torsion of tensor data](/entry/tensor-degeneration-data-torsion-isometry-onto/). The existence of the tensor data, of the action and of the algebraic factor are separate statements in the Lean code, and the text above gives only their statements. The action exists for every tensor structure with these relations, not only for a chosen one.
