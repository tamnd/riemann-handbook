---
title: Reductions of the open conditions
decls:
  - Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_open_positive
  - Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_open_dimensions
  - Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_open_base_dims
  - Formalism.MainNotions.G.SymmetricFormBlocks.theorem_A_closed_of_eight_open_bounds
  - Formalism.MainNotions.G.SymmetricFormBlocks.theorem_A_closed_of_nine_open_bounds
  - Formalism.MainNotions.G.SymmetricFormBlocks.integrality_from_metric_of_orthogonality_window
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Reductions of the open conditions

Section 6 reduced the closed form of Theorem A to four conditions on the blocks of an instance: base dimension, level part, sum over the window, and directions. This section removes them one at a time. Each step replaces a condition by a weaker or more local one, or proves it outright, and each step gives a theorem of the same shape: if the remaining conditions hold for large constants, for all $C_M \geq 1$ and all admitted instances satisfying the window hypotheses, then the closed form holds for large constants. At the end two conditions on the level lattices remain, an orthogonal family condition and a window condition, together with a base change property of highest weight lattices. Section 8 treats them.

We keep the notation of Section 6. Write $\Lambda_\ell$ for the level lattice of a block $G(a_{\mathrm{top}}, a_+, b)$ at the level $\ell = (j, j_+)$. It does not depend on $a_+$; only its pairing does. Write $\beta^{a_+}_\ell$ for the pairing of the block with this $a_+$, and $\beta^{\Phi}_\ell$ for the pairing at $a_+ = 0$ built with the tie operators, which is the pairing of the level part and sum over the window conditions. Let $D_1 = D_1(C_M)$ and let $\mathcal{S}$ be the standard lattice of the block.

**Definition 7.7.1 (Conditions on the level lattices).** Let $X$ be an instance and $C_M \geq 1$. At each class $\delta$, box point $a_{\mathrm{top}} \in \operatorname{box}(\delta)$ and index $(b, \ell) \in I(\delta, a_{\mathrm{top}})$, consider:

1. (Orthogonal family.) There are $n_1 \geq 0$ and $e_1, \dots, e_{n_1} \in \Lambda_\ell$, linearly independent over $\mathbb{Z}_p$, with $\beta^{\Phi}_\ell(e_a, e_b) = 0$ for $a \neq b$, $\beta^{\Phi}_\ell(e_a, e_a) \neq 0$ and $v_p(\beta^{\Phi}_\ell(e_a, e_a)) \leq \lfloor D_1 \rfloor$, and $n_1 \leq \operatorname{rk} \Lambda_\ell \leq n_1 + \operatorname{bad}(\beta^{\Phi}_\ell, \Lambda_\ell, \lfloor D_1 \rfloor)$.
2. (Window.) For every family $e_1, \dots, e_{n_1}$ with the properties in 1 except the rank bounds,
$$\sum_{a_+ \in A} \operatorname{bad}\bigl(\beta^{a_+}_\ell, \textstyle\sum_a \mathbb{Z}_p e_a, \lfloor Y D_1 \rfloor\bigr) \leq |A| \cdot \frac{5}{Y}\, n_1.$$

For every block $G = G(a_{\mathrm{top}}, a_+, b)$ and level $\ell$ of $G$, consider:

3. (Level dimension.) $r_L(a_{\mathrm{top}}, b, \ell) \leq \dim_{\mathbb{Q}_p} \operatorname{span}_{\mathbb{Q}_p} \Gamma_\ell(G)$, where $\Gamma_\ell(G)$ is the set of generators of $\mathcal{S}$ at level $\ell$.
4. (Spans of the standard lattice.) $\sum_\ell r_L(a_{\mathrm{top}}, b, \ell) \leq \dim_{\mathbb{Q}_p} \operatorname{span}_{\mathbb{Q}_p} \mathcal{S}$.
5. (Levels after base change.) $\dim_K \operatorname{span}_K \Gamma^O_\ell(G) \leq \operatorname{rk} \Lambda_\ell$, where $O$ is the discrete valuation ring of the instance, $K$ its fraction field, and $\Gamma^O_\ell(G)$ the generators at level $\ell$ of the block over $O$.

The window condition is the one with content: it says that the pairings $\beta^{a_+}_\ell$ for varying $a_+$ are, on average over the window, almost unimodular on an orthogonal family. The other conditions are about ranks and dimensions.

**Definition 7.7.2 (Base change of highest weight lattices).** The *base change property* says: for every domain $O$, every ring map $\iota$ from $\mathbb{Q}_p$ to the fraction field $K$ of $O$, every word $L$ of letters, and all thresholds $J, M$, every integral highest weight polynomial over $O$ for $(L, J, M)$ lies in the $K$-span of the image under $\iota$ of the integral highest weight lattice $Y_{\mathbb{Z}}(L, J, M)$ over $\mathbb{Z}_p$.

**Proposition 7.7.3 (Without the level part).** If the base dimension, sum over the window and directions conditions hold for large constants, for all $C_M \geq 1$ and all admitted instances satisfying the window hypotheses, then the closed form holds for large constants.

Lean: `Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_open_positive`.

*Proof.* The level part condition holds for every instance and every $C_M$. It compares the bad count of $\beta^{\Phi}_\ell$ on $\Lambda_\ell$ with $d_r(B - j_+)$ times the bad count of the highest weight lattice: by the [Fock block decomposition](/entry/fock-block-decomposition/), the level lattice behaves like $d_r(B - j_+)$ copies of the integral highest weight lattice of the level, so the good count of $\beta^{\Phi}_\ell$ on $\Lambda_\ell$ is at least $d_r(B - j_+)$ times the good count of the tie pairing on that lattice. Add the level part condition to the hypotheses and apply the [Theorem (Closed form from four conditions)](/entry/closed-of-open-directions/). $\square$

**Proposition 7.7.4 (Directions from spans).** If the base dimension, sum over the window and span conditions (4) hold for large constants, for all $C_M \geq 1$ and all admitted instances satisfying the window hypotheses, then the closed form holds for large constants.

Lean: `Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_open_dimensions`.

*Proof.* For every block, $\dim_{\mathbb{Q}_p} \operatorname{span} \mathcal{S}$ is at most the rank of the block lattice: the block lattice over $O$ is spanned by the images of the generators of $\mathcal{S}$, and the images of $\mathbb{Q}_p$-independent generators stay independent over $K$. So condition 4 implies the directions condition, and the [Proposition (Without the level part)](/entry/closed-of-open-positive/) applies. $\square$

**Proposition 7.7.5 (The window replaces the sum).** If the base dimension, orthogonal family, window and span conditions hold for large constants, for all $C_M \geq 1$ and all admitted instances satisfying the window hypotheses, then the closed form holds for large constants.

Lean: `Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_open_base_dims`.

*Proof.* We derive the sum over the window condition. Since $Y > 0$, the factor $5/Y$ is nonnegative. Fix $\delta, a_{\mathrm{top}}, (b, \ell)$ and take the family $e_1, \dots, e_{n_1}$ of the orthogonal family condition. Let $L' = \sum_a \mathbb{Z}_p e_a \subseteq \Lambda_\ell$, of rank $n_1$. For any pairing and depth, a sublattice of rank $n_1$ has bad count at least the bad count of the lattice minus $\operatorname{rk} \Lambda_\ell - n_1$, because good pairs in $L'$ are good pairs in $\Lambda_\ell$. So for every $a_+ \in A$,
$$\operatorname{bad}(\beta^{a_+}_\ell, \Lambda_\ell, \lfloor Y D_1 \rfloor) \leq (\operatorname{rk} \Lambda_\ell - n_1) + \operatorname{bad}(\beta^{a_+}_\ell, L', \lfloor Y D_1 \rfloor).$$
Sum over $a_+ \in A$. The first terms give $|A| (\operatorname{rk} \Lambda_\ell - n_1) \leq |A| \operatorname{bad}(\beta^{\Phi}_\ell, \Lambda_\ell, \lfloor D_1 \rfloor)$ by the rank bound in the orthogonal family condition. The second terms give at most $|A| \cdot \frac{5}{Y} n_1 \leq |A| \cdot \frac{5}{Y} \operatorname{rk} \Lambda_\ell$ by the window condition. This is the sum over the window condition. Apply the [Proposition (Directions from spans)](/entry/closed-of-open-dimensions/). $\square$

**Proposition 7.7.6 (Base dimension from the levels).** If the conditions 1, 2, 4 and 5 hold for large constants, for all $C_M \geq 1$ and all admitted instances satisfying the window hypotheses, then the closed form holds for large constants.

Lean: `Formalism.MainNotions.G.SymmetricFormBlocks.theorem_A_closed_of_eight_open_bounds`.

*Proof.* The rank of the block lattice over $O$ equals the sum over the levels $\ell$ of $\dim_K \operatorname{span}_K \Gamma^O_\ell(G)$. This uses the valuation properties of the instance: the block lattice is the direct sum of its level pieces, and each level piece is free with rank the dimension of its span. Condition 5 bounds each term by $\operatorname{rk} \Lambda_\ell$, which is the base dimension condition. Apply the [Proposition (The window replaces the sum)](/entry/closed-of-open-base-dims/). $\square$

**Proposition 7.7.7 (Spans from the levels).** If the conditions 1, 2, 3 and 5 hold for large constants, for all $C_M \geq 1$ and all admitted instances satisfying the window hypotheses, then the closed form holds for large constants.

Lean: `Formalism.MainNotions.G.SymmetricFormBlocks.theorem_A_closed_of_nine_open_bounds`.

*Proof.* For every block, $\sum_\ell \dim \operatorname{span}_{\mathbb{Q}_p} \Gamma_\ell(G) \leq \dim \operatorname{span}_{\mathbb{Q}_p} \mathcal{S}$: the generators at different levels have different multidegrees in the letters, so the spans at distinct levels are independent, and their sum lies in the span of $\mathcal{S}$. Summing condition 3 over the levels gives condition 4. Apply the [Proposition (Base dimension from the levels)](/entry/theorem-a-closed-of-eight-open-bounds/). $\square$

**Proposition 7.7.8 (Levels from base change).** Assume the base change property. If the orthogonal family, window and level dimension conditions hold for large constants, for all $C_M \geq 1$ and all admitted instances satisfying the window hypotheses, then the closed form holds for large constants.

Lean: `Formalism.MainNotions.G.SymmetricFormBlocks.integrality_from_metric_of_orthogonality_window`.

*Proof.* We prove condition 5 for every instance. The generators $\Gamma^O_\ell(G)$ of the block over $O$ are products of integral highest weight polynomials over $O$ and monomials. By the base change property each such highest weight polynomial lies in the $K$-span of the image of $Y_{\mathbb{Z}}$, so $\operatorname{span}_K \Gamma^O_\ell(G)$ is contained in the $K$-span of the image of $\Lambda_\ell$. The latter has dimension at most $\operatorname{rk} \Lambda_\ell$. Apply the [Proposition (Spans from the levels)](/entry/theorem-a-closed-of-nine-open-bounds/). $\square$

The six propositions remove the four conditions of Section 6 and leave the orthogonal family, window and level dimension conditions and the base change property. The orthogonal family condition is the Theorem (Orthogonal family) of Section 1 applied to $\Lambda_\ell$, once $\beta^{\Phi}_\ell$ is known to be symmetric on $\Lambda_\ell$ and $p \neq 2$.

**Remark 7.7.9 (Formalization).** The six theorems are one-line compositions: each applies one implication between condition bundles (`positive_of_dimension_change`, `restricted_bounds_weaken_from_seven_to_six` and so on) under the monotonicity lemma `thr_mono` for large constants, then calls the next theorem. The names do not describe the steps well. `closed_of_open_positive` ([DirectionsOfPositivePart.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/DirectionsOfPositivePart.lean#L23)) supplies the level part condition `RestPlusA` through `directions_of_positive_part`, and `closed_of_open_dimensions` ([PositiveOfDimensionChange.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/PositiveOfDimensionChange.lean#L23)) supplies directions through `positive_of_dimension_change`. The level part condition is proved by `plusACondition` through `plusAWICondition`, which we did not open; the proof above states the comparison it proves (`RestPlusAW`) and its source in the block decomposition as we understand it. The dimension facts used in the proofs are `restDimBC_proved`, `finrank_blockLat` with `valuation_properties_hold`, `restSumSpan_proved` and `restBClvl_of`; we give the arguments in outline. The equality between $\Lambda_\ell$ at $a_+$ and at $0$ is definitional: `restPlusB_of` uses a sublattice of the lattice at $a_+ = 0$ as a sublattice of the lattice at $a_+$.
