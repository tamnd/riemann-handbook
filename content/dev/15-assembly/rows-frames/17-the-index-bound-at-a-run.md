---
title: The index bound at a run
decls:
  - GlobalTheory.FinalJoin.exists_top_of_core
  - GlobalTheory.FinalJoin.runHolds_of_parOK
  - GlobalTheory.FinalJoin.inputs4_of_net
  - GlobalTheory.T.exists_indexBoundHypothesesWithNet_allValuedPoints
  - GlobalTheory.InputsAtRecord.inputsNet_recPlus
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The index bound at a run

This section proves the index bound at every run of a record whose size parameter is large. It is the largest step below [the surjectivity from the hypotheses](/entry/onto-x-of-hypotheses-alt-alt/), in the surjectivity branch of [the unitary hypotheses](/proof/unitary-hypotheses/). The bound compares the lattice of integral cusp forms with the span of theta products, prime by prime. Its inputs are collected at one run, and the next section proves the three largest of them. We begin with the completion of a pinned core to a full record, which [the pinned runs](/entry/exists-run-pins/) of part 1 use.

### Completing a core

Let $D$ be a datum with rank $m$. A *core* $C$ of $D$ holds a parameter datum $Q$ with, for each index $j$, a weight datum $D_w(j)$ of signature $(p_j, q_j)$, an algebra $X_o(j)$ of forms over a coefficient field $c$, and unitary data $U(j, \sigma)$ for the good embeddings $\sigma$. A *record* $T$ of $D$ extends a core by the spaces of cusp forms at each index and weight. The core *satisfies the laws* if the pins of $Q$ hold and the unitary data are unfolded at each good embedding. The datum is *$\Psi$-admissible* if every pinned parameter datum has its coefficient field in the CM type at each index in range.

For an index $j$ in range, a connection $\nabla$ on $X_o(j)$ and weights $a$ with a positive last entry, the theta generators of weight $a$ and degree $n$ are a set of forms built from $\nabla$ and harmonic polynomials. The core has *theta in the cusp* at $j$ if these generators lie in the cusp forms of weight $a$. It has *nonzero theta* at $j$ if, for $0 < n$, $p_j + q_j \leq n$ and $\sum a + 2$ at most the level bound, a nonzero harmonic polynomial of weight $a$ gives a nonzero theta generator.

**Lemma 7.17.1 (Completion of a core).** Let $C$ be a core of $D$ that satisfies the laws, with $1 \leq p_j + q_j$ for each $j$, and let $D$ be $\Psi$-admissible. Then there is a record $T$ of $D$ that satisfies the laws of records and whose core is $C$.

Lean: `GlobalTheory.FinalJoin.exists_top_of_core`.

*Proof.* The completion theorem for cores builds $T$ from $C$, given that the value of a harmonic germ does not depend on the chart, that $1 \leq p_j + q_j$, that the coefficient field lies in the CM type at the pins, and that at each $j$ in range the core has theta in the cusp and nonzero theta.

1. Theta in the cusp holds at $j$. The rank $r$ of $D$ satisfies $1 \leq r$, since $m \geq 2$. The unitary data are unfolded at each good embedding, so the dictionary theorem for theta in the cusp applies.
2. Nonzero theta holds at $j$, by the theorem on nonzero theta for cores with the laws.

This gives $T$. $\square$

The completion theorem asks for nonzero theta only at the indices $j < m$. The proof gives it at all $j$ in range.

### The index bound

Fix a record $T$ that satisfies the laws. For each index $1 \leq j \leq m$ it gives an algebra of forms $X_j$ over a number field $K$, which contains the cusp forms of each weight $w$. Over each prime $\lambda$ of $\mathcal{O}_K$ there is a set of points $y$, each with a valuation $v_y$ on forms. The lattice $M_w$ is the set of cusp forms of weight $w$ with $v_y \geq 0$ at all points. Put $\ell(\lambda) = \log N\lambda / [K : \mathbb{Q}]$.

Let $w_L$ and $w_F$ be weights and $T_n$ an integer, and let $\Theta \subseteq X_j$ be the submodule spanned by the products of $T_n$ scaled theta forms of weight $w_L$ with short theta forms of weight $w_F$. The *index bound* at weight $\kappa$ with weights $\nu(\lambda)$ and total $\beta$ says that there are $r(\lambda) \geq 0$ with $\sum_\lambda r(\lambda) \ell(\lambda) \leq \beta$, such that for each $\lambda$, each integer $e \geq T_n \nu(\lambda)$ and each $K_\lambda$-subspace $V'$ of the span of $M_\kappa$,

$$\operatorname{length}_{\mathcal{O}_\lambda} \bigl( (M_\kappa)_\lambda \cap V' \big/ \Theta_\lambda \cap V' \bigr) \leq e \dim V' + r(\lambda) < \infty.$$

The *parameter conditions* at the own prime $p$ and index $j$ hold if the record satisfies the shared laws, has an orientation, has algebraically closed function fields, and $p$ is the own prime of every twisted place of the run. The *page conditions* are the page hypotheses at the size data $L$, with the constants $H$, the weights $\kappa, w_L, w_F$ and the integers. A *second norm* is a family of norms $N$ on the cusp forms, one for each weight and each complex embedding $\sigma$ of $K$, with $N(aF) = |\sigma(a)| N(F)$ and $N \leq \|\cdot\|_{\sup}$.

Let $X_j^{+}$ be $X_j$ with all valued points added: over each prime $\lambda$, all the valuations of the valuation set under the trivial class condition.

### The inputs at a record

The *inputs with a net* for an algebra are four groups of facts.

1. The base facts: the run hypotheses, the lattice condition, a lower bound for the log sup norms of integral forms with constant $C_L$, the page lattice bound when $j < m$, and the deep submodule bound.
2. A net: a finite set of forms at a complex embedding $\sigma_0$ of $K$, with four conditions and $\log \#\mathrm{net} \leq P_d$.
3. A family of forms $\theta'_1, \ldots, \theta'_\delta$ of weight $w_F$ and forms of weight $w_L$, with a number $\delta$ and twelve conditions, among them the shares of section 18.
4. The combined bound, and at each $\lambda$ a local point datum with the curve, tie and lift conditions and the height bound.

The family uses the constants $G_c$, $P_H$, $P_{rw}$, $P_{\mathrm{et}}$ and $P_d$ of the size data.

**Theorem 7.17.2 (Inputs at a record).** There are $C_L \in \mathbb{R}$ and functions $C_q, Z_0 : \mathbb{R}^2 \to \mathbb{R}$ with the following property. Let the parameter conditions hold at $p$ and $j$, let the page conditions hold for $X_j$, and let $Z_0(C_A, C_K) \leq z_{\mathrm{base}}(L)$ for the constants $C_A$ and $C_K$ of $H$. Then the inputs with a net hold for $X_j^{+}$, with the constants of $C_L$ and $C_q(C_A, C_K)$, and the page support condition holds.

Lean: `GlobalTheory.T.exists_indexBoundHypothesesWithNet_allValuedPoints` (also `GlobalTheory.InputsAtRecord.inputsNet_recPlus`).

*Proof.* We take the steps in order.

1. The absolute lower bound for the log sup norms of integral forms gives $C_L$ and the lower bound. The recursive page lattice bound gives $C_q$ and the page lattice bound. The polynomial domination of the page gives $Z_0$ and the conditions on the page.
2. [The run hypotheses from the parameter conditions](/entry/run-hypotheses-forms-scalars-of-parameter-conditions/) give the run hypotheses, the lattice condition, the page support condition and a finite spanning set of cusp forms of weight $w_F$.
3. The theorem on admissible generators of the theta lattice gives a first family of forms. When $j < m$ it also uses the auxiliary form of scalar weight.
4. [The shares at all indices](/entry/shares-at-all/) give the new $\delta$ and $\theta'$ from the spanning set, and five share conditions. Put them into the family.
5. The combined bound for the run scalars, with the inclusion of Hodge and Tate charts, gives the combined bound. The net at the run gives the net and the deep submodule bound.
6. [The local point data with height bounds](/entry/exists-prime-data-curve-lifting-height-bounds/) give the local point data and the height bound.
7. The regularity of the extended points moves the combined bound to $X_j^{+}$. The base facts and the family conditions do not depend on the extra points.

The rest is bookkeeping. $\square$

### From the net to the bound

**Lemma 7.17.3 (Refined inputs from a net).** Let the inputs with a net hold for $X_j$, with the constants of $C_L$. Assume the ties $C_1 = C_c = C_2$ and $A_1 = A_c = A_2$ of the constants, $C_{R,c} = 7$ and $A_2 \geq 12$, and the page and page support conditions. Then there is a second norm $n$ such that, for $X_j$ and the scalars renormed by $n$, the refined inputs hold, and the index bound holds at $\kappa$ with

$$\beta = \operatorname{rk}(M_\kappa) \cdot f \cdot m \cdot b \cdot d_{e2}.$$

Lean: `GlobalTheory.FinalJoin.inputs4_of_net`.

*Proof.* We take the steps in order.

1. The net gives a second norm $n$. For the renormed algebra, the net condition is replaced by three facts: the sup norm squared is at most $e^{P(1 + \log |\kappa|)}$ times the $L^2$ norm squared at weight $\kappa$, a hermitian deep bound, and $\log \dim_K$ of the cusp forms of weight $\kappa$ is at most $P_d$.
2. The net bound in degree two changes the constants. The pair $(C_G, A_G)$ of the sup bound goes from $(1041, 3)$ to $(1041 z, 2)$, where $z = z_{\mathrm{base}}$.
3. The ties and $A_G = 2$ give the tie of the constants. The chosen family of the intrinsic hypotheses, with the page and page support conditions, gives the refined inputs.
4. The index bound from refined inputs gives the conclusion.

The rest is bookkeeping. $\square$

**Theorem 7.17.4 (Index bound at a run).** There is $x_0 : \mathbb{R}^2 \to \mathbb{R}$ with the following property. Let the map of tuples be injective, let the parameter conditions hold at $p$ and at every $j \in [1, m]$, and fix $j$, the size data $L$, the constants $H$, the weights and the integers. If the page run conditions hold and $x_0(C_A, C_K) \leq x(L)$, then:

1. for some second norm $n$ and constants, the refined inputs and the index bound hold for $X_j^{+}$ renormed by $n$;
2. the run hypotheses hold for $X_j$;
3. the index bound holds for $X_j$ with $\beta = \operatorname{rk}(M_\kappa) \cdot f \cdot m \cdot b \cdot d_{e2}$.

Lean: `GlobalTheory.FinalJoin.runHolds_of_parOK`.

*Proof.* We take the steps in order.

1. [The inputs at a record](/entry/exists-index-bound-hypotheses-with-net-all-valued-points/) give $C_L$, $C_q$ and $Z_0$.
2. The numerical run conditions beyond a threshold turn $Z_0$ into $x_0$: the page run conditions and $x_0 \leq x(L)$ give the page conditions and $Z_0 \leq z_{\mathrm{base}}(L)$. So the inputs with a net hold for $X_j^{+}$.
3. [The refined inputs from a net](/entry/inputs4-of-net/) give $n$, the refined inputs and the index bound for $X_j^{+}$. This is claim 1.
4. The run hypotheses and the index bound do not see the extra points or the second norm. So they hold for $X_j$. This gives claims 2 and 3.

This proves the theorem. $\square$

The parameter conditions force $p$ to be the own prime of every twisted place of the run. So for $m \geq 1$ they hold for at most one prime $p$ per record. The user of the theorem keeps only claims 2 and 3.

**Remark 7.17.5 (Formalization).** The completion `exists_top_of_core` is in [ExistsTopOfCore.lean](lean:Development/AbelianVarietyTheory/Proofs/HeightProofs/ExistsTopOfCore.lean#L26), with `thInCusp_of_laws` above it; it gives the nonzero theta part as `fun _ => ...`, so the premise $j < m$ is not used. The predicates `ThInCusp` and `ThNe0` are at lines 23 and 30 of [ThProps.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/ThProps.lean#L23), and `OKPsi` is at line 7 of [RecCond.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/RecCond.lean#L7). The index bound `runHolds_of_parOK` is at line 58 and `inputs4_of_net` at line 33 of [ExistsThresholdRunHolds.lean](lean:Development/AbelianVarietyTheory/Proofs/HeightProofs/ExistsThresholdRunHolds.lean#L58). The lemmas `concl_xplus`, `indexBoundConclusion_secondNorm_iff` and `scalOfP_base` are `rfl` or `Iff.rfl`, which is step 4. The tie `TieC` asks for $A_G \leq 2$ while the constants `kR` have $A_G = 3$, which is why step 2 of the lemma is needed, and `concl_of_inputs4` drops the last part of `Inputs4`. The statement `T.exists_indexBoundHypothesesWithNet_allValuedPoints` is a `first | exact` wrapper at line 8 of its Statement file. The proof `inputsNet_recPlus` is at line 79 of [ExistsIndexBoundHypothesesWithNetAllValuedPoints.lean](lean:Development/AbelianVarietyTheory/Proofs/HeightProofs/ExistsIndexBoundHypothesesWithNetAllValuedPoints.lean#L79); there `baseIn_xplus` and `famIn_xplus` at line 29 have the proof `h`. The parts of the inputs, `InputsNet`, `InputsR` and `Inputs4`, are in [ConclOfInputs4.lean](lean:Development/AbelianVarietyTheory/Definitions/HeightFunctions/ConclOfInputs4.lean#L51).
