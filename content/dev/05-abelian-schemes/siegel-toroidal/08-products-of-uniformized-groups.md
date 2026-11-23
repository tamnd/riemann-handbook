---
title: Products of uniformized groups
decls:
  - GlobalTheory.T.product_uniformised_groups_sum_data
  - GlobalTheory.MumProd.prod_main
  - GlobalTheory.T.product_uniformised_groups_uniformised_by_sum
  - GlobalTheory.MumProdUnifSum.main
  - GlobalTheory.T.uniformisation_product_of_uniformisedGroups
  - GlobalTheory.ProdUnifExists.main
  - GlobalTheory.ProdUnifExists.exists_unif
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Products of uniformized groups

This section proves that the product of two uniformized semi-abelian groups is uniformized by the sum of their degeneration data, and that the inclusions and projections of the factors are linear and adjoint in pairs. It is the lemma on products in the proof of the [theorem on adjoint pairs](/entry/exists-lin-hom/): there a pair of maps between two uniformized groups becomes an endomorphism of their product, which the case of one group handles.

We keep the notation of the previous section. $R$ is a local domain, degeneration data are taken with respect to an ideal $I$ of $R$ (in most statements $I = \mathfrak{m}_R$), and $K = K_R$. For group schemes $G_1, G_2$ over $R$ we write $G_1 \times_R G_2$ for their product, with projections $\mathrm{fst}, \mathrm{snd}$, and $(1, 0) : G_1 \to G_1 \times_R G_2$, $(0, 1) : G_2 \to G_1 \times_R G_2$ for the two inclusions. For line bundles $L_1, L_2$ on $B_1, B_2$ and maps $a_k : B \to B_k$, the *external tensor product* of $L_1, L_2$ along $a_1, a_2$ is $a_1^* L_1 \otimes a_2^* L_2$ on $B$.

**Definition 9.8.1 (Sum data).** Let $A, A_1, A_2$ be polarized abelian schemes over a scheme $S$, with bundles $L, L_1, L_2$. Then $A$ is the *sum* of $A_1, A_2$ along homomorphisms $a_k : A \to A_k$ if $(a_1, a_2) : A \to A_1 \times A_2$ is an isomorphism and there is a generating isomorphism of $L$ with the external tensor product of $L_1, L_2$ along $a_1, a_2$.

Let $D, D_1, D_2$ be degeneration data over $R$, with abelian parts $B, B_1, B_2$, lattices $Y, Y_1, Y_2$, maps $c, c_1, c_2$ and trivializations $\psi, \psi_1, \psi_2$. Then $D$ is the *sum* of $D_1, D_2$ along homomorphisms $p_k : B \to B_k$ and additive maps $q_k : Y \to Y_k$ if:

1. $(p_1, p_2) : B \to B_1 \times B_2$ is an isomorphism and $(q_1, q_2) : Y \to Y_1 \times Y_2$ is bijective;
2. $c(y) \circ p_k = c_k(q_k(y))$ for $k = 1, 2$ and all $y \in Y$;
3. there is a generating isomorphism $w$ of $L_D$ with the external tensor product of $L_{D_1}, L_{D_2}$ along $p_1, p_2$ that maps the rigidification of $L_D$ to the product of the rigidifications of $L_{D_1}, L_{D_2}$, and for each $y$ maps $\psi(y)$ to the product of $\psi_1(q_1 y)$ and $\psi_2(q_2 y)$.

Lean: `GlobalTheory.MumProd.IsSumPolAV` (also `GlobalTheory.MumProd.IsSumDeg`).

**Definition 9.8.2 (Product uniformization).** Let $U_1, U_2$ be uniformizations of $G_1, G_2$ by $D_1, A_1$ and $D_2, A_2$, and let $U$ be a uniformization of $G_1 \times_R G_2$ by $D, A$, all without the expansion property. Let $p_k, q_k$ be as above and $a_k : A \to A_k$. Then $U$ is the *product* of $U_1$ and $U_2$ if:

1. the generic fibre isomorphism of $U$ followed by $a_1$ equals $\mathrm{fst}$ followed by the generic fibre isomorphism of $U_1$, and the same holds for $a_2$ and $\mathrm{snd}$;
2. there is a generating isomorphism of $L_U$ with the external tensor product of $L_{U_1}, L_{U_2}$ along $\mathrm{fst}, \mathrm{snd}$;
3. for each $e \ge 0$, $p_1 \circ q_e = q_{1,e} \circ \mathrm{fst}$ and $p_2 \circ q_e = q_{2,e} \circ \mathrm{snd}$;
4. for each $e \ge 0$ and each map $h : Y_1 \to Y$ with $q_1 h = 1$ and $q_2 h = 0$, there is a map of tori $t$ given by $h$ on characters with $\mathrm{fst} \circ i_e = i_{1,e} \circ t$; and the same for $h : Y_2 \to Y$ with $q_1 h = 0$, $q_2 h = 1$ and $\mathrm{snd}$.

Lean: `GlobalTheory.MumProd.IsProdUnif`.

Clauses 3 and 4 say that $\mathrm{fst}$ is linear over $(p_1, h)$ for each section $h$ of $q_1$ that $q_2$ kills, and in the same way for $\mathrm{snd}$.

**Theorem 9.8.3 (Product uniformizations exist).** Let $I$ be an ideal of $R$ such that $R$ is an admissible base at $I$. Let $D$ be the sum of $D_1, D_2$ along $p_k, q_k$ and $A$ the sum of $A_1, A_2$ along $a_k$. Let $U_1, U_2$ be uniformizations of $G_1, G_2$ by $D_1, A_1$ and $D_2, A_2$. Then there is a uniformization $U$ of $G_1 \times_R G_2$ by $D$ and $A$ that is the product of $U_1$ and $U_2$.

Lean: `GlobalTheory.ProdUnifExists.exists_unif` (also `GlobalTheory.ProdUnifExists.main`, the case $I = \mathfrak{m}_R$ over a base $R$, and `GlobalTheory.T.uniformisation_product_of_uniformisedGroups`, a wrapper of `main`).

*Proof.* Step 1 (the data without expansion). A lemma on sum data gives the box structure of the bundles of $D$. The generic fibre of $G_1 \times_R G_2$ is the product of the generic fibres, and $A$ is the sum of $A_1, A_2$, so a lemma on generic fibres gives the generic fibre isomorphism with clause 1. A lemma on external tensor products gives a rigidified cubical symmetric bundle on $G_1 \times_R G_2$ with clause 2. For each $e$, a lemma on thickenings gives the exact sequence of $G_1 \times_R G_2$ over $R/I^{e+1}$ from the sequences of $U_1$ and $U_2$, with the torus of $Y \cong Y_1 \times Y_2$; this gives clauses 3 and 4. A lemma on cubical structures shows that the isomorphism of thickenings keeps the cubical structure. This is a uniformization $U$ without the expansion property, and it is the product of $U_1$ and $U_2$.

Step 2 (dimensions). Fix $k \ge 1$. The abelian scheme laws hold for $A, A_1, A_2$. A lemma on dimensions of theta families applies to $D_1$, $D_2$ and $D$, and the ranks and the dimensions add: $\operatorname{rank} Y = \operatorname{rank} Y_1 + \operatorname{rank} Y_2$, and the same for the dimensions of $B$ and $A$. Since $U_1$ and $U_2$ have the expansion property for $k$, the space of theta families of $D_i$ of degree $k$ has dimension $k^{g_i}$, where $g_i$ is the dimension of $A_i$.

Step 3 (a basis). Choose bases $b_1, b_2$ of the theta families of $D_1, D_2$ of degree $k$, and let $\sigma_1, \sigma_2$ be the sections of $L_{U_1}^{k}, L_{U_2}^{k}$ that they expand to. A lemma gives the box families $b_1 \boxtimes b_2$ of $D$, indexed by pairs, and their box sections $\sigma_1 \boxtimes \sigma_2$ of $L_U^{k}$. A lemma on product degenerations shows that the box families are linearly independent. There are $k^{g_1} k^{g_2} = k^{g}$ of them, which is the dimension of the theta families of $D$, so they are a basis.

Step 4 (expansion). Each box section expands to its box family: the expansion modulo $I^{e+1}$ of a box product is the box product of the expansions. A lemma on bases then shows that $U$ has the expansion property for $k$: a bijection on a basis that is compatible with the linear structure extends to the whole space. As $k$ is arbitrary, $U$ is a uniformization. $\square$

**Theorem 9.8.4 (Uniformization by sum data).** Let $R$ be a local domain that is an admissible base of characteristic $0$. Let $D, A$ be the sums of $D_1, D_2$ and $A_1, A_2$ along $p_k, q_k$ and $a_k$, and let $U_1, U_2$ be uniformizations of $G_1, G_2$ by $D_1, A_1$ and $D_2, A_2$. Then there is a uniformization $U$ of $G_1 \times_R G_2$ by $D$ and $A$ such that:

1. $((1, 0), \mathrm{fst})$ is adjoint for $(L_{U_1}, L_U)$ and $((0, 1), \mathrm{snd})$ is adjoint for $(L_{U_2}, L_U)$;
2. for all homomorphisms $i_k : B_k \to B$ and additive maps $j_k : Y_k \to Y$ with $p_k i_k = 1$, $p_l i_k = 0$, $q_k j_k = 1$ and $q_l j_k = 0$ for $l \ne k$, the map $(1, 0)$ is linear over $(i_1, q_1)$, $\mathrm{fst}$ is linear over $(p_1, j_1)$, $(0, 1)$ is linear over $(i_2, q_2)$ and $\mathrm{snd}$ is linear over $(p_2, j_2)$.

Lean: `GlobalTheory.MumProdUnifSum.main` (also `GlobalTheory.T.product_uniformised_groups_uniformised_by_sum`, a wrapper).

*Proof.* The theorem above gives a uniformization $U$ that is the product of $U_1$ and $U_2$. Clause 2 of the product makes $L_U$ an external tensor product, and a lemma on products of bundles gives the two adjoint pairs of clause 1. For clause 2, $\mathrm{fst}$ is linear over $(p_1, j_1)$ and $\mathrm{snd}$ over $(p_2, j_2)$ by clauses 3 and 4 of the product. A lemma on inclusions shows that $(1, 0)$ is linear over $(i_1, q_1)$: it uses $p_1 i_1 = 1$ and $p_2 i_1 = 0$ on the abelian parts and $q_1$ on the torus. The same lemma gives $(0, 1)$ over $(i_2, q_2)$. $\square$

**Theorem 9.8.5 (Product of uniformized groups).** Let $R$ be a local domain that is an admissible base of characteristic $0$. Let $U_1, U_2$ be uniformizations of semi-abelian groups $G_1, G_2$ by $D_1, A_1$ and $D_2, A_2$. Then there are degeneration data $D$, a polarized abelian scheme $A$, a uniformization $U$ of $G_1 \times_R G_2$ by $D$ and $A$, homomorphisms $i_k : B_k \to B_D$, $p_k : B_D \to B_k$ and additive maps $j_k : Y_k \to Y_D$, $q_k : Y_D \to Y_k$ for $k = 1, 2$, such that:

1. $G_1 \times_R G_2$ is semi-abelian, $p_k \circ i_k = 1$ and $q_k \circ j_k = 1$;
2. $(i_k, p_k, j_k, q_k)$ is an adjoint pair from $D_k$ to $D$ for $k = 1, 2$;
3. $(1, 0)$ is linear over $(i_1, q_1)$, $\mathrm{fst}$ over $(p_1, j_1)$, $(0, 1)$ over $(i_2, q_2)$ and $\mathrm{snd}$ over $(p_2, j_2)$;
4. $((1, 0), \mathrm{fst})$ is adjoint for $(L_{U_1}, L_U)$ and $((0, 1), \mathrm{snd})$ is adjoint for $(L_{U_2}, L_U)$.

Lean: `GlobalTheory.MumProd.prod_main` (also `GlobalTheory.T.product_uniformised_groups_sum_data`, a wrapper).

*Proof.* A lemma on product degeneration data gives $D$ with $p_k, q_k$ such that $D$ is the sum of $D_1, D_2$, and a lemma on products of abelian schemes gives $A$ with $a_k$ such that $A$ is the sum of $A_1, A_2$. The theorem above gives $U$ with clause 4 and with the linearity statement for every choice of sections. Let $e = (q_1, q_2) : Y_D \to Y_1 \times Y_2$, which is bijective. Put
$$i_1 = (p_1, p_2)^{-1} \circ (1, 0), \quad i_2 = (p_1, p_2)^{-1} \circ (0, 1), \quad j_1 = e^{-1} \circ \mathrm{inl}, \quad j_2 = e^{-1} \circ \mathrm{inr}.$$
Then $p_k i_k = 1$, $p_l i_k = 0$, $q_k j_k = 1$ and $q_l j_k = 0$ for $l \ne k$, so the theorem gives clause 3, and clause 1 holds except for the first claim. A lemma on products of semi-abelian groups shows that $G_1 \times_R G_2$ is semi-abelian. Two lemmas on product data show that $(i_1, p_1, j_1, q_1)$ and $(i_2, p_2, j_2, q_2)$ are adjoint pairs, using the generating isomorphism of the sum. $\square$

**Remark 9.8.6 (Formalization).** The theorem `ProdUnifExists.main` takes a base $R$ but uses only the first half of the hypothesis, that $R$ is an admissible base; characteristic $0$ is not used ([UniformisationProductOfUniformisedGroups.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UniformisationProductOfUniformisedGroups.lean#L347)). In `prod_main` the hypotheses that $G_1, G_2$ are semi-abelian are used only for the claim that $G_1 \times_R G_2$ is semi-abelian ([ProductUniformisedGroupsSumData.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ProductUniformisedGroupsSumData.lean#L20)). The linearity of the projections is the pair of lemmas `IsProdUnif.linHom_fst` and `linHom_snd`, which unfold the product clauses ([IsProdUnif.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsProdUnif.lean#L37)). The maps written $(1, 0)$ and $(0, 1)$ are `lift (𝟙 G₁) 1` and `lift 1 (𝟙 G₂)`, where `1` is the constant map to the unit. The lemmas on sum data, generic fibres, external tensor products, thickenings, dimensions, box families and bases have no entries in this chapter; we use only their statements. The box condition $\mathrm{MapsAt}_2$ in the sum of degeneration data is given here only in words.
