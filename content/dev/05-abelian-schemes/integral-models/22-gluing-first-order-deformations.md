---
title: Gluing first-order deformations
decls:
  - GlobalTheory.T.harrisTaylor_exists_glued_firstOrder_deformation
  - GlobalTheory.HTGlue.exists_glue
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Gluing first-order deformations

This section proves the gluing result that [the universal first-order deformation](/entry/htuniv-main/) uses. Suppose that $d$ maps $f_1, \dots, f_d$ on $H(A_0)$ each come from a deformation of an object $o_0$ over the dual numbers. Then the vector $(f_1, \dots, f_d)$ comes from one deformation over $k[k^d]$. The method is the crystalline description of square-zero lifts: an object over a square-zero thickening is given, up to the data that lift for free, by a direct summand of the crystal of $A_0$ that reduces to the Hodge filtration and respects the action of $O$, the polarization and the Lie condition. We build such a summand over $k[k^d]$ from the summands of the $d$ given deformations.

### Hodge lifts in the crystal

Let $C$ be a local Artinian ring and $\pi : C \to C_0$ a surjection with $(\ker \pi)^2 = 0$. We give $\ker \pi$ the divided powers with $\gamma_n = 0$ for $n \geq 2$. Let $A_0$ be an abelian scheme over $C_0$. We write $\mathbb{D}_C(A_0)$ for the $C$-dual of the primitive classes in the first crystalline cohomology of $A_0$ relative to this thickening. We use the reduction relation between elements of $\mathbb{D}_C(A_0)$ and elements of $H(A_0)$ given by the comparison with de Rham cohomology over $C_0$, and we say that $\delta \in \mathbb{D}_C(A_0)$ *reduces to* $y \in H(A_0)$ when they are related.

**Definition 8.22.1 (Hodge lift).** Let $A$ be an abelian scheme over $C$ with an identification of $A_0$ with $A \times_C C_0$. Pulling back crystalline classes along the map $A_0 \to A$ and dualizing gives a $C$-linear map $\mathbb{D}_C(A_0) \to H(A)$. The *Hodge lift* $L(A) \subseteq \mathbb{D}_C(A_0)$ is the preimage of $\operatorname{Fil}(A)$ under this map.

Lean: `GlobalTheory.DeRham.liftFil`.

For $C = k[V]$ with $V$ a finite-dimensional $k$-space and $C_0 = k$, every primitive de Rham class $\gamma$ of $A_0$ has a constant extension $\tilde\gamma$, and the filtration lifts of [the section on smoothness](/entry/htuniv-main/) are read off from $L(A)$: a linear map $y$ from primitive classes to $V$ is a filtration lift of $x \in H(A_0)$ if and only if some $\delta \in L(A)$ has $\delta(\tilde\gamma) = x(\gamma) + y(\gamma)$ for every $\gamma$. This is the definition of a filtration lift.

### Admissible summands

Fix a datum $D$, a base $b$ over $R$ and an integer $N$ prime to $p$. Let $\beta_C : R \to C$ be a ring map, and let $o_0$ be an object of level $N$ over $\operatorname{Spec}(\pi \beta_C)$, with abelian scheme $A_0$ and action $a \mapsto a_*$ of $O$ on $\mathbb{D}_C(A_0)$. A *polarization pairing over $C$* is a $C$-bilinear form on $\mathbb{D}_C(A_0)$ given by the crystalline Chern class of the bundle of $o_0$, as in the definition of a polarization pairing in [the previous section](/entry/ks-dim-at-point/) with crystalline classes in place of de Rham classes.

**Definition 8.22.2 (Admissible summand).** A $C$-submodule $E \subseteq \mathbb{D}_C(A_0)$ is an *admissible summand* for $o_0$ if the following hold.

1. $E$ is a direct summand: $E \oplus M = \mathbb{D}_C(A_0)$ for some submodule $M$.
2. An element $y \in H(A_0)$ lies in $\operatorname{Fil}(A_0)$ if and only if some $\delta \in E$ reduces to $y$.
3. $E$ is stable under $a_*$ for every $a \in O$.
4. $E$ is isotropic for every polarization pairing over $C$.
5. (Lie condition.) If $\delta \in \mathbb{D}_C(A_0)$ and $\omega_* \delta - \beta_C(\rho) \delta \in E$, then there are $w_1, \dots, w_a \in \mathbb{D}_C(A_0)$ with $c_* w_i - \beta_C(t_i(c)) w_i \in E$ for all $i$ and all $c \in \mathcal{O}_F$, and $\delta - \sum_i w_i \in E$.

We read condition 5 as a crystalline form of the Lie condition of Definition 8.1.3: modulo $E$, the $\rho$-part splits into the eigenparts for the maps $t_1, \dots, t_a$.

### Inputs

We use the following results, in the setting above.

1. (Hodge lifts are admissible.) Let $o$ be an object over $\operatorname{Spec} \beta_C$ and $o_0 \to o$ a map of objects over $\operatorname{Spec} \pi$, with abelian scheme $A$. Then $L(A)$ satisfies conditions 1 to 5.
2. (Lifting the abelian scheme and the action.) If $E$ satisfies conditions 1, 2 and 3, then there are an abelian scheme $A$ over $C$ with an identification of $A_0$ with $A \times_C C_0$ and an action of $O$ on $A$ that restricts to the action on $A_0$, such that $L(A) = E$.
3. (Lifting the polarization.) If $E$ also satisfies condition 4, then the bundle $P_0$ of $o_0$ lifts to a line bundle $P$ on $A \times_C A$ that is trivial on $0 \times A$ and $A \times 0$, symmetric, with $\Delta^* P$ relatively ample, with kernel killed by an integer prime to $p$, and with the Rosati condition, and the pullback of $P$ to $A_0 \times A_0$ is $P_0$ up to isomorphism.
4. (Lifting the level structure.) As $N$ is prime to $p$, the level structure of $o_0$ lifts to a level structure of $A$ of level $N$, compatible with the map $A_0 \to A$.
5. (Lifting the Lie condition.) If $E$ satisfies condition 5, then $A$ satisfies the Lie condition of Definition 8.1.3. The multiplicity part of that condition holds for every square-zero lift of the action.

For $C = k[V]$ we also use these results about gluing. Let $f_1, \dots, f_d : H(A_0) \to H(A_0)$ be linear and $V = k^d$.

**Definition 8.22.3 (Glued filtration).** The *glued filtration* $E_f \subseteq \mathbb{D}_{k[k^d]}(A_0)$ is the set of $\delta$ for which there are $x \in \operatorname{Fil}(A_0)$ and $z_1, \dots, z_d \in \operatorname{Fil}(A_0)$ with
$$\delta(\tilde\gamma) = x(\gamma) + \big((f_1 x + z_1)(\gamma), \dots, (f_d x + z_d)(\gamma)\big)$$
for every primitive de Rham class $\gamma$ of $A_0$.

Lean: `GlobalTheory.HTGlue.glueFil`.

So $E_f$ is the graph of $(f_1, \dots, f_d)$ on $\operatorname{Fil}(A_0)$, enlarged by $\operatorname{Fil}(A_0) \otimes k^d$.

6. (Glued filtration, conditions 1 and 2.) For every $f$, $E_f$ satisfies conditions 1 and 2 over $C = k[k^d]$.
7. (Glued filtration, conditions 3, 4 and 5.) Let $E'_1, \dots, E'_d \subseteq \mathbb{D}_{k[\varepsilon]}(A_0)$ satisfy conditions 1, 2 and 3 over $k[\varepsilon]$, and suppose that for every $j$ and every $x \in \operatorname{Fil}(A_0)$ some $\delta \in E'_j$ has $\delta(\tilde\gamma) = x(\gamma) + (f_j x)(\gamma) \varepsilon$ for all $\gamma$. Then $E_f$ satisfies condition 3. If every $E'_j$ satisfies condition 4, so does $E_f$. If $d > 0$ and every $E'_j$ satisfies condition 5, so does $E_f$.
8. (Filtration lifts from the glued filtration.) Let $A$ be an abelian scheme over $k[k^d]$ with an identification of $A_0$ with its special fibre, and suppose $L(A) = E_f$. Then $(f_1 x, \dots, f_d x)$ is a filtration lift of $x$ for $A$, for every $x \in \operatorname{Fil}(A_0)$.
9. (The case $d = 0$.) Let $k$ be algebraically closed, $N \geq 3$, and $\varphi$ a polarization pairing of $o_0$. If $f_1, \dots, f_d$ are Kodaira-Spencer maps for $(\sigma_0, \varphi, \operatorname{Fil}(A_0), Z(o_0, \beta))$, then there is a deformation of $o_0$ to $k[k^d]$ for which $(f_1 x, \dots, f_d x)$ is a filtration lift of $x$, for every $x \in \operatorname{Fil}(A_0)$. We use it only for $d = 0$.

Results 2 to 5 are the shape of Grothendieck-Messing theory: lifts of an abelian scheme along a nilpotent thickening with divided powers correspond to lifts of the Hodge filtration (W. Messing, Lecture Notes in Math. 264, 1972). We have not compared the statements here with that source.

### Objects from admissible summands

**Lemma 8.22.4 (Objects from admissible summands).** Let $C$ be a local Artinian ring, $\pi : C \to C_0$ surjective with $(\ker \pi)^2 = 0$, $\beta_C : R \to C$, and $N$ prime to $p$. Let $o_0$ be an object of level $N$ over $\operatorname{Spec}(\pi \beta_C)$, and $E \subseteq \mathbb{D}_C(A_0)$ an admissible summand. Then there are an object $o$ of level $N$ over $\operatorname{Spec} \beta_C$ and a map of objects $o_0 \to o$ over $\operatorname{Spec} \pi$ whose abelian scheme $A$ has $L(A) = E$.

Lean: `GlobalTheory.HTGlue.exists_obj_of_summand`.

*Proof.* Result 2 gives $A$ with its $O$-action and $L(A) = E$. Result 3 gives the bundle $P$ with all its conditions. Result 4 gives the level structure. Result 5 gives the Lie condition. These data form an object $o$ over $\operatorname{Spec} \beta_C$. The identification of $A_0$ with $A \times_C C_0$, the compatibility of the actions, the isomorphism of bundles and the compatibility of the level structures form a map of objects $o_0 \to o$ over $\operatorname{Spec} \pi$. $\square$

### The gluing theorem

**Theorem 8.22.5 (Gluing of first-order deformations).** Let $N \geq 3$ be prime to $p$, $k$ an algebraically closed field, and $o_0$ an object of level $N$ over $t : \operatorname{Spec} k \to \operatorname{Spec} R$. Let $d \geq 0$ and $f_1, \dots, f_d : H(A_0) \to H(A_0)$ be linear. Suppose that for each $j$ there is a deformation of $o_0$ to $k[\varepsilon]$ for which $f_j x$ is a filtration lift of $x$, for every $x \in \operatorname{Fil}(A_0)$. Then there is a deformation of $o_0$ to $k[k^d]$ for which $(f_1 x, \dots, f_d x)$ is a filtration lift of $x$, for every $x \in \operatorname{Fil}(A_0)$.

Lean: `GlobalTheory.HTGlue.exists_glue` (also `GlobalTheory.T.harrisTaylor_exists_glued_firstOrder_deformation`, a second name).

*Proof.* Write $t = \operatorname{Spec} \beta$ with $\beta : R \to k$.

The case $d = 0$. By result 1 of [the section on Kodaira-Spencer directions](/entry/htcount-count/), $o_0$ has a polarization pairing $\varphi$. With $d = 0$ the list of Kodaira-Spencer maps is empty, and result 9 gives the deformation.

The case $d > 0$. The ring $k[k^d]$ is local and Artinian, as it is a finite-dimensional local $k$-algebra; so is $k[\varepsilon]$. Let $\pi : k[k^d] \to k$ be the projection and $\beta_C = \iota \beta : R \to k[k^d]$. Then $\pi \beta_C = \beta$, so $o_0$ is an object over $\operatorname{Spec}(\pi \beta_C)$.

For each $j$ choose a deformation $o'_j$ of $o_0$ to $k[\varepsilon]$ as in the hypothesis, with abelian scheme $A'_j$, and put $E'_j = L(A'_j)$. By result 1, $E'_j$ satisfies conditions 1 to 5 over $k[\varepsilon]$. For $x \in \operatorname{Fil}(A_0)$, the vector $f_j x$ is a filtration lift of $x$ for $A'_j$, so by the definition of a filtration lift some $\delta \in E'_j$ has $\delta(\tilde\gamma) = x(\gamma) + (f_j x)(\gamma) \varepsilon$ for all $\gamma$.

So the hypotheses of result 7 hold. With result 6, the glued filtration $E_f$ satisfies conditions 1 to 5 over $k[k^d]$; for condition 5 we use $d > 0$. So $E_f$ is an admissible summand. The lemma on objects from admissible summands gives an object $o$ over $\operatorname{Spec} \beta_C = t \circ \operatorname{Spec} \iota$ and a map of objects $o_0 \to o$ over $\operatorname{Spec} \pi$ with $L(A) = E_f$. This is a deformation of $o_0$ to $k[k^d]$. By result 8, $(f_1 x, \dots, f_d x)$ is a filtration lift of $x$ for it, for every $x \in \operatorname{Fil}(A_0)$. $\square$

**Remark 8.22.6 (Formalization).** The theorem is in [HarrisTaylorExistsGluedFirstOrderDeformation.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HarrisTaylorExistsGluedFirstOrderDeformation.lean#L93), under a raised heartbeat limit, and the lemma at [line 32](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HarrisTaylorExistsGluedFirstOrderDeformation.lean#L32). The second name is a wrapper whose list of alternatives also tries two unrelated results of the same file: [HarrisTaylorExistsGluedFirstOrderDeformationStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HarrisTaylorExistsGluedFirstOrderDeformationStatement.lean#L10). The case $d = 0$ is treated apart ([lines 95 to 100](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HarrisTaylorExistsGluedFirstOrderDeformation.lean#L95)); there the deformations in the hypothesis are not used, and result 9 asks for Kodaira-Spencer maps, so for $d > 0$ it could not replace the gluing. The lemma needs $N$ prime to $p$ but not $N \geq 3$. The name "admissible summand" is ours; its five conditions are hypotheses of the lemma. We have not unfolded the crystal, the reduction relation or the crystalline Chern class, and their descriptions in words are ours. Result 8 is proved in the same file, and result 6 consists of two results that need no hypothesis on $f$. We read the statements of results 1 to 9, not their proofs.
