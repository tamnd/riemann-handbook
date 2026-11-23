---
title: The geometric lemma filtration
decls:
  - GlobalTheory.CompanionTheory.GeoAssembly.jacquetOfInducedFiltration
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The geometric lemma filtration

The geometric lemma of Bernstein and Zelevinsky computes the Jacquet module of a parabolically induced representation. For $\mathrm{GL}_n$ over a $p$-adic field it says that the Jacquet module for one block parabolic of a representation induced from another block parabolic has a filtration, and that the layers are indexed by matrices of natural numbers with fixed row and column sums. Each layer is a product of Jacquet modules of the inducing data, induced again. This section states the lemma in that form and assembles it from the double coset decomposition of $\mathrm{GL}_n$ and from the lemma for one pair of standard parabolics. The lemma is the tool that computes the exponents of products, as in Section 15, and the Jacquet modules behind the Grothendieck ring of Section 21, which the step [EveryCharacter](/step/every-character/) uses. For background see [parabolic induction and the Jacquet module](/learn/representations/#parabolic-induction-and-the-jacquet-module).

### Setting

Let $k$ be a nonarchimedean local field. All representations are on complex vector spaces. A representation of a topological group is *smooth* if the stabilizer of each vector is open. For a natural number $r$ put $[r] = \{0, 1, \dots, r-1\}$.

A *composition* of a finite set $n$ consists of a finite totally ordered set $I$, a family of finite sets $(m_i)_{i \in I}$ and a bijection $e : \bigsqcup_{i \in I} m_i \to n$. Its *Levi subgroup* is $M_m = \prod_{i \in I} \mathrm{GL}(m_i)(k)$, and $e$ embeds $M_m$ in $\mathrm{GL}(n)(k)$ as a block diagonal subgroup. The blocks are ordered by the order of $I$. Let $P_e$ be the block upper triangular subgroup of $\mathrm{GL}(n)(k)$ for this order of blocks, with unipotent radical $U_e$ and modulus character $\delta_e$.

For a smooth representation $\rho$ of $M_m$, let $i_e(\rho)$ be the normalized parabolic induction: the smooth induction from $P_e$ to $\mathrm{GL}(n)(k)$ of $\rho\,\delta_e^{1/2}$, inflated through $P_e \to M_m$. For a representation $\pi$ of $\mathrm{GL}(n)(k)$ on $V$, let $r_e(\pi)$ be the normalized Jacquet module: the representation of $M_m$ on $V/V(U_e)$ given by $g \mapsto \delta_e(g)^{-1/2}\pi(g)$, where $V(U_e)$ is the span of the vectors $\pi(u)v - v$ for $u \in U_e$. These are the functors $i_{G,M}$ and $r_{M,G}$ of Bernstein and Zelevinsky (1977), Section 1.8.

The same definitions apply one level down. Let $c = (c_{ij})_{i \in I, j \in J}$ be finite sets and let $f_i : \bigsqcup_{j \in J} c_{ij} \to m_i$ be bijections, with $J$ totally ordered. Then each $f_i$ is a composition of $m_i$, and we write $r_f(\rho)$ for the representation of $\prod_{i}\prod_{j}\mathrm{GL}(c_{ij})(k)$ obtained from the normalized Jacquet modules for the $f_i$, factor by factor. In the same way, bijections $g_j : \bigsqcup_{i \in I} c_{ij} \to m'_j$ give a normalized induction $i_g$ from $\prod_j \prod_i \mathrm{GL}(c_{ij})(k)$ to $M_{m'} = \prod_j \mathrm{GL}(m'_j)(k)$.

**Definition 1.16.1 (Size matrix).** Let $(I, m)$ and $(J, m')$ be compositions of the same set. A *size matrix* is a function $b : I \times J \to \mathbb{N}$ with $\sum_{j} b_{ij} = |m_i|$ for every $i$ and $\sum_i b_{ij} = |m'_j|$ for every $j$. Let $\mathcal{S}(m, m')$ be the set of size matrices.

**Definition 1.16.2 (Cell functor).** Let $c$, $f$ and $g$ be as above. Let $s$ be the isomorphism $\prod_j \prod_i \mathrm{GL}(c_{ij})(k) \to \prod_i \prod_j \mathrm{GL}(c_{ij})(k)$ that changes the order of the two products. For a representation $\rho$ of $M_m$ put
$$F_{f,g}(\rho) = i_g\bigl(r_f(\rho) \circ s\bigr),$$
a representation of $M_{m'}$.

In the language of Zelevinsky (1980), Section 1.6, the layer $F_{f,g}(\rho)$ for $\rho = \rho_1 \otimes \dots \otimes \rho_a$ is the product over $j$ of the products over $i$ of the pieces of $r(\rho_i)$ of sizes $b_{ij}$.

### Inputs

Fix $N$. For $\beta : [N] \to \mathbb{N}$ let $P_\beta$ be the subgroup of $\mathrm{GL}_N(k)$ of matrices $g$ with $g_{xy} = 0$ whenever $\beta(x) > \beta(y)$, and let $L_\beta$ be its subgroup of matrices with $g_{xy} = 0$ whenever $\beta(x) \neq \beta(y)$. Write $i_\beta$ and $r_\beta$ for normalized induction from $P_\beta$ and the normalized Jacquet module for $P_\beta$. For a bijection $e : \bigsqcup_i m_i \to [N]$ and $x \in [N]$, let $\mathrm{blk}_e(x) \in I$ be the block that contains $x$. For a permutation $w$ of $[N]$ let $\mathrm{sz}(w)$ be the function on $I \times J$ given by
$$\mathrm{sz}(w)_{ij} = \#\{x \in [N] : \mathrm{blk}_e(x) = i,\ \mathrm{blk}_{e'}(w^{-1}x) = j\},$$
and let $p(w) \in \mathrm{GL}_N(k)$ be its permutation matrix.

**Theorem 1.16.3 (Inputs on block parabolics).** Let $e : \bigsqcup_{i \in I} m_i \to [N]$ and $e' : \bigsqcup_{j \in J} m'_j \to [N]$ be compositions.

1. There is $\beta : [N] \to \mathbb{N}$ with $\beta(x) < \beta(y)$ if and only if $\mathrm{blk}_e(x) < \mathrm{blk}_e(y)$.
2. For such $\beta$ there is an isomorphism of groups $\varphi : M_m \to L_\beta$ that is a homeomorphism and agrees with the block embedding given by $e$.
3. For every permutation $w$ of $[N]$, $\mathrm{sz}(w)$ is a size matrix.
4. Let $\beta$ and $\gamma$ be as in item 1 for $e$ and $e'$. For permutations $w$ and $w'$ of $[N]$, $p(w') \in P_\beta\,p(w)\,P_\gamma$ if and only if $\mathrm{sz}(w) = \mathrm{sz}(w')$.
5. For every size matrix $b$ there is a permutation $w$ with $\mathrm{sz}(w) = b$.
6. (Geometric lemma.) For $\beta, \gamma : [N] \to \mathbb{N}$ there are $K$ and permutations $w_0, \dots, w_{K-1}$ such that every $g \in \mathrm{GL}_N(k)$ lies in $P_\beta\,p(w_t)\,P_\gamma$ for exactly one $t$. For each smooth $\sigma$ of $L_\beta$ there are $L_\gamma$-stable subspaces $0 = V_0 \subseteq V_1 \subseteq \dots \subseteq V_K = r_\gamma(i_\beta \sigma)$ and surjective maps from $V_{t+1}$ onto $G_{w_t}(\sigma)$ with kernel $V_t$. Here $G_w(\sigma)$ is the normalized induction to $L_\gamma$ from $L_\gamma \cap p(w)^{-1} P_\beta\, p(w)$ of the conjugate by $p(w)$ of the Jacquet module of $\sigma$ for $L_\beta \cap p(w) P_\gamma\, p(w)^{-1}$.
7. With $\varphi$ and $\varphi'$ as in item 2 for $(e, \beta)$ and $(e', \gamma)$, for every representation $\rho$ of $M_m$ and every $w$ there are bijections $f$ and $g$ with $c_{ij} = [\mathrm{sz}(w)_{ij}]$ such that $G_w(\rho \circ \varphi^{-1}) \circ \varphi' \cong F_{f,g}(\rho)$.
8. If $c$ and $c'$ have $|c_{ij}| = |c'_{ij}|$ for all $i, j$, then $F_{f,g}(\rho) \cong F_{f',g'}(\rho)$ for all bijections $f, g$ for $c$ and $f', g'$ for $c'$.
9. (Transport.) For a bijection $\iota : n \to [N]$, $r_{e'}(i_e \rho) \cong r_{\iota e'}(i_{\iota e}\rho)$. With $\varphi, \varphi'$ as in item 7, $i_e \rho \cong i_\beta(\rho \circ \varphi^{-1})$ and $r_{e'}\pi \cong r_\gamma(\pi) \circ \varphi'$. The functor $r_\gamma$ carries isomorphic representations to isomorphic ones. If $\psi$ is a continuous homomorphism and $\rho$ is smooth, then $\rho \circ \psi$ is smooth. A filtration with known layers carries over along an isomorphism $\rho \cong \rho' \circ \psi$.

Lean: `GlobalTheory.T.exists_strict_block_order` (also `GlobalTheory.T.levi_block_homeomorph`, `GlobalTheory.T.permutation_block_counts`, `GlobalTheory.T.double_coset_block_matrix`, `GlobalTheory.T.exists_perm_block_matrix`, `GlobalTheory.T.bernstein_zelevinsky_geometric_lemma`, `GlobalTheory.T.levi_intersection_conjugate`, `GlobalTheory.T.cell_levi_tensor_decomposition`, `GlobalTheory.T.induction_reindex_equiv`, `GlobalTheory.T.parabolicInd_equiv_levi_transport`, `GlobalTheory.T.jac_equiv_jacquetRep_comp_levi_equiv`, `GlobalTheory.T.jacquet_module_equiv`, `GlobalTheory.T.isSmooth_comp_continuous`, `GlobalTheory.T.filtration_transport_equiv`).

Item 6 is the geometric lemma of Bernstein and Zelevinsky (1977), Section 2.12 and Theorem 5.2, for one pair of standard parabolics. The double coset description in items 4 and 5 is in Zelevinsky (1980), Section 1.6, and Bernstein and Zelevinsky (1977), Section 2.11. Items 7 and 8 are the computation in Zelevinsky (1980), Section 1.6, of the layers in terms of the blocks.

### The filtration

**Theorem 1.16.4 (Geometric lemma filtration).** Let $I$ and $J$ be finite totally ordered sets, $n$ a finite set, and $e : \bigsqcup_{i \in I} m_i \to n$ and $e' : \bigsqcup_{j \in J} m'_j \to n$ compositions. There are $N \geq 0$ and a bijection $b : [N] \to \mathcal{S}(m, m')$ with the following property. For every smooth representation $\rho$ of $M_m$ there are subrepresentations
$$0 = S_0 \subseteq S_1 \subseteq \dots \subseteq S_N = r_{e'}(i_e \rho)$$
such that, for every $t \in [N]$ and all bijections $f_i : \bigsqcup_j [b(t)_{ij}] \to m_i$ and $g_j : \bigsqcup_i [b(t)_{ij}] \to m'_j$,
$$S_{t+1}/S_t \cong F_{f,g}(\rho).$$

Lean: `GlobalTheory.CompanionTheory.GeoAssembly.jacquetOfInducedFiltration`.

The number $N$ and the bijection $b$ do not depend on $\rho$. Each size matrix gives exactly one layer.

*Proof.* Put $N_0 = |n|$ and choose a bijection $\iota : n \to [N_0]$. By the first transport fact of item 9 we may replace $e$ and $e'$ by $\iota e$ and $\iota e'$, so we take $n = [N_0]$. By item 1 choose $\beta$ for $e$ and $\gamma$ for $e'$. By item 2 choose $\varphi : M_m \to L_\beta$ and $\varphi' : M_{m'} \to L_\gamma$.

Step 1: the index set. Apply item 6 to $\beta$ and $\gamma$. This gives $K$ and permutations $w_0, \dots, w_{K-1}$. Define $b(t) = \mathrm{sz}(w_t)$, a size matrix by item 3. We show that $b$ is a bijection from $[K]$ onto $\mathcal{S}(m, m')$, and we take $N = K$. Suppose $b(s) = b(t)$. By item 4, $p(w_t) \in P_\beta\, p(w_s)\, P_\gamma$. Also $p(w_t) \in P_\beta\, p(w_t)\, P_\gamma$. By the uniqueness in item 6, $s = t$. Let $c$ be a size matrix. By item 5 there is $w$ with $\mathrm{sz}(w) = c$. By item 6, $p(w) \in P_\beta\, p(w_t)\, P_\gamma$ for some $t$, and by item 4, $\mathrm{sz}(w_t) = \mathrm{sz}(w) = c$. So $b(t) = c$.

Step 2: the filtration. Let $\rho$ be smooth. Since $\varphi^{-1}$ is continuous, $\sigma = \rho \circ \varphi^{-1}$ is a smooth representation of $L_\beta$ by item 9. Item 6 gives the subspaces $V_t$ of $r_\gamma(i_\beta \sigma)$ and the surjections onto $G_{w_t}(\sigma)$. By item 9,
$$r_{e'}(i_e \rho) \cong r_\gamma(i_e \rho) \circ \varphi' \cong r_\gamma(i_\beta \sigma) \circ \varphi',$$
where the second isomorphism uses $i_e\rho \cong i_\beta \sigma$ and the fact that $r_\gamma$ respects isomorphisms. The transport fact of item 9, applied to this isomorphism, gives subrepresentations $S_0 \subseteq \dots \subseteq S_K$ of $r_{e'}(i_e\rho)$ with $S_0 = 0$, $S_K = r_{e'}(i_e\rho)$ and
$$S_{t+1}/S_t \cong G_{w_t}(\sigma) \circ \varphi'.$$

Step 3: the layers. Fix $t$ and bijections $f$, $g$ for the sets $[b(t)_{ij}]$. By item 7 there are bijections $f^0$, $g^0$ for the same sets with $G_{w_t}(\sigma) \circ \varphi' \cong F_{f^0, g^0}(\rho)$. By item 8, $F_{f^0,g^0}(\rho) \cong F_{f,g}(\rho)$. So $S_{t+1}/S_t \cong F_{f,g}(\rho)$. $\square$

The theorem fixes no order on the size matrices. In Bernstein and Zelevinsky (1977), Section 2.12, the layers follow an order of the double cosets that is compatible with their closure relation. That order is needed when one compares the bottom or top layer with a submodule or a quotient. Here $b$ is the order in which item 6 lists the double cosets. A later argument that needs a specific layer at the bottom must therefore get that fact from item 6 directly.

**Remark 1.16.5 (Formalization).** The theorem is in [JacquetOfInducedFiltration.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/JacquetOfInducedFiltration.lean#L39). The property it proves is `GlobalTheory.SmGL.JacquetOfInducedFiltration`, defined with `SizeMatrix`, `cellFunctor`, `relJac`, `relInd` and `swapBlocks` in [ExistsCellOfIsSubquotient.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/ExistsCellOfIsSubquotient.lean#L149), a file far from the block decomposition folder. The functors `jac` and `relJac` carry the factor $\delta^{-1/2}$ and `relInd` carries $\delta^{1/2}$, so the Jacquet modules and inductions are normalized as above. The module sets `maxSynthPendingDepth 1` at L21 and `maxHeartbeats 1000000` for the theorem, and it defines the helper `equivComp`, which restricts an isomorphism along a homomorphism. The geometric lemma of item 6 is `bernstein_zelevinsky_geometric_lemma`; its subgroups are `blockUpper`, `levi` and `cellLeviSub`, and its inducing datum is `normInducing`. We read the statements of the inputs, not their proofs, and we did not unfold `cellLeviSub` and `normInducing`. The input `cell_levi_tensor_decomposition` says only that the cell functor does not depend on the choice of the bijections; its name speaks of a tensor decomposition. Item 9 joins two different notions of smoothness: `isSmooth_comp_continuous` takes `GlobalTheory.PRep.IsSmooth` and returns `GroundTheory.Automorphic.IsSmooth`, which is the form that item 6 requires. The theorem needs no admissibility or finite length.
