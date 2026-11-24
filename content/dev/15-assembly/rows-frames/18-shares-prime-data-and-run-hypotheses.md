---
title: Shares, local point data and run hypotheses
decls:
  - GlobalTheory.InputsAtRecord.sharesAt_all
  - GlobalTheory.T.exists_primeData_curve_lifting_heightBounds
  - GlobalTheory.RunPrimeData.exists_primeData_heights
  - GlobalTheory.T.runHypotheses_formsScalars_of_parameterConditions
  - GlobalTheory.RunJoin.hypC_record
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Shares, local point data and run hypotheses

This section proves three of the inputs that [the inputs at a record](/entry/inputs-net-rec-plus/) of section 17 collects: the share conditions of the family, the local point data with the height bound, and the run hypotheses. Each is a step of that proof, in the surjectivity branch of [the unitary hypotheses](/proof/unitary-hypotheses/). Each of the three results splits into the case $j < m$, where the datum is indefinite at the index, and the case $j = m$, where it is definite. The deep work is in the theorems for the two cases, which other chapters prove.

We keep the notation of section 17: the record $T$ with the laws, the index $j$ in range, the algebra $X_j$ of forms over $K$ with the lattices $M_w$, the own prime $p$, the size data $L$, the constants $H$, the weights $\kappa, w_L, w_F$, the integer $T_n$, the parameter conditions and the page conditions. Let $S$ be the scalars of the run at $p$: the scaled theta forms and their normalizing constants. Put $d = \dim Y = |\Psi|\, r(r - 1)/2$.

### The family and the shares

A *family* $G$ for $X_j$ and the weights holds a number $\delta$, forms $\theta'_1, \ldots, \theta'_\delta$ of weight $w_F$, forms of weight $w_L$, a base form, scalars and, when $j < m$, a form of the extra weight. To *refill* $G$ is to replace $\delta$, $\theta'$ and the other fields. The family satisfies the *generator conditions* if, among other things, its forms of weight $w_L$ have no common zero. It satisfies the *eta conditions* if the form of the extra weight is a cusp form with the value and sup bounds of the page.

Let $\mathcal{S}$ be a set of cusp forms of weight $w_F$. The family has *shares in* $\mathcal{S}$ if there are $\delta$ and $\theta'_1, \ldots, \theta'_\delta \in \mathcal{S}$ such that every refill of $G$ with this $\delta$ and $\theta'$ has the following properties:

1. at each prime $\lambda$, a set of vectors made from the family is a basis over the completion at $\lambda$;
2. the rank bound

$$\binom{T_n - 1}{d}\, \delta \leq \operatorname{rk} M_\kappa;$$

3. two more bounds of $\operatorname{rk} M_\kappa$, one in terms of the scalars $S$ and one in terms of the numbers $\rho_P$ of the run;
4. at each prime $\lambda$, the containment of the modules of the family in the module of the run.

**Theorem 7.18.1 (Shares at all indices).** Let $1 \leq j \leq m$. Assume the parameter conditions at $p$ and $j$, the page conditions, the run hypotheses and the lattice condition at $\kappa$. Let $G$ be a family with the generator conditions, and with the eta conditions when $j < m$. Let $\mathcal{S}$ span the cusp forms of weight $w_F$ over $K$. Then $G$ has shares in $\mathcal{S}$.

Lean: `GlobalTheory.InputsAtRecord.sharesAt_all`.

*Proof.* There are two cases.

1. If $j < m$, the datum is indefinite at $j$. The theorem on bases and shares of cusp forms at the indefinite lift index gives the claim from all the hypotheses.
2. If $j = m$, the datum is definite at $j$. The theorem on bases and shares at the definite lift index gives the claim. It uses only the condition that the forms of weight $w_L$ have no common zero. The eta conditions have the premise $j < m$, so they are empty here.

This proves the theorem. $\square$

Since the shares hold for every refill, the four properties do not depend on the fields of $G$ other than $\delta$ and $\theta'$. This lets the proof of section 17 refill the family after it chooses $\delta$ and $\theta'$.

### Local point data

A *local point datum* for $G$ at a prime $\lambda$ is a map $y$ from the points of $G$ over $\lambda$ to the points of $X_j^{+}$, a form $g_0$ of weight $w_F$ and integers $c$. It defines an $\mathcal{O}_\lambda$-module $A_0$. The *local index* $I_\lambda$ is the length of $A_0$ modulo the span of the forms of weight $w_L$ of the family. The datum has the *curve*, *tie* and *lift* conditions if $y$ lies on the curve of the family, the values of $g_0$ match the ties of the family, and the lift of $y$ is defined over $\mathcal{O}_\lambda$.

For a cusp form $\theta$ let $\mathrm{mls}(\theta)$ be the mean over the embeddings of $K$ of the log sup norm of its conjugates. Let $G_c$, $P_H$ and $P_{rw}$ be the growth constant, the height constant and the row constant of the size data, and let $|w_L|$ be the size of the weight $w_L$.

**Theorem 7.18.2 (Local point data with height bounds).** Assume that the function fields are algebraically closed, the page conditions, the run hypotheses, a constant $C_L > 0$ with the lower bound for the log sup norms at all weights, and the combined bound. Let $G$ be a family with the generator conditions, the eta conditions when $j < m$, the tie of its forms $\theta'$ with the scalars, the basis property at each prime, and $\log \delta \leq 1041\, z^3$ for $z = z_{\mathrm{base}}(L)$. Then there are local point data at all primes $\lambda$ for $G$ moved to $X_j^{+}$, with the curve, tie and lift conditions, such that each $I_\lambda$ is finite, the sum $\sum_\lambda I_\lambda \ell(\lambda)$ converges, and

$$\begin{aligned} 2 \sum_\lambda I_\lambda\, \ell(\lambda) \leq{} & \delta \log \delta + 2 \sum_{i = 1}^{\delta} \mathrm{mls}(\theta'_i) + \tfrac{8}{3}\, d (d + 4)\, \delta\, P_{rw}\, |w_L| \\ & + 2 (d + 4)(d + 1)\, \delta\, (2 G_c + 6 P_H)\, |w_L|. \end{aligned}$$

When $j < m$, a second bound of the same kind holds for the net of the run.

Lean: `GlobalTheory.T.exists_primeData_curve_lifting_heightBounds` (also `GlobalTheory.RunPrimeData.exists_primeData_heights`).

*Proof.* We take the steps in order.

1. The page hypotheses at the cusp give the form $g_0$ of weight $w_F$.
2. The existence theorem for the real points of the local data gives the map $y$ at each $\lambda$, with the curve, tie and lift conditions.
3. If $\delta = 0$, the family has no points. Then each $I_\lambda$ is $0$, and both sides of the bound are $0$.
4. If $\delta > 0$ and $j < m$, the height inequalities at the indefinite lift index give the two bounds.
5. If $\delta > 0$ and $j = m$, the height inequality at the definite lift index gives the bound. The net bound is empty, since its premise is $j < m$.

This proves the theorem. $\square$

In section 17 the theorem is applied with the forms $\theta'$ of the shares, and the bound $\log \delta \leq 1041\, z^3$ comes from the rank bound of the shares and the page.

### The run hypotheses

Let $s_W(w_L)$ be the normalizing scalar of the scaled theta forms of weight $w_L$. The *run hypotheses* at the record are the hypotheses on the page of the run with the constant $C_R = 7$, the exponent $0$, the scalars $S$ and the weights $\nu$ of the record at $w_L$. The *theta integrality* at a weight $w$ says that the scaled theta lattice of weight $w$ lies in the lattice of forms with bounded sup norm. The *page support* condition at $w_L$ holds if the page has its support conditions and $s_W(w_L)$ has a nonzero image at each embedding $\sigma$.

**Theorem 7.18.3 (Run hypotheses from the parameter conditions).** Let the map of tuples be injective, and let the parameter conditions hold at $p$ and $j$ and the page conditions hold. Then:

1. the run hypotheses hold;
2. the lattice condition holds at $\kappa$: the cusp forms of weight $\kappa$ with integral values form a lattice;
3. theta integrality holds at every weight $w$;
4. the page support condition holds at $w_L$;
5. there is a finite set $\mathcal{S}$ of cusp forms of weight $w_F$ that spans them over $K$, such that every family $G$ with all $\theta'_i \in \mathcal{S}$ has its forms $\theta'$ tied with the scalars $S$ and the growth constant $G_c$.

Lean: `GlobalTheory.T.runHypotheses_formsScalars_of_parameterConditions` (also `GlobalTheory.RunJoin.hypC_record`).

*Proof.* We take the steps in order.

1. The page conditions give the page hypotheses, among them the size facts $n(w_L) = n_W$ with $f r (r + 1) \leq n_W$ and the facts that $w_L$ and $w_F$ are admissible. The page rows give $\log(1 + |\kappa|) \leq 2 L$, and the weights of the page lie below $\kappa$: $|w_L| \leq |\kappa|$. Since $3 \leq |w_L|$, we get $\log |w_L| \leq \log(1 + |\kappa|) \leq 2L$.
2. From $r \geq 1$ we get $2 f r \leq f r (r + 1) \leq n(w_L)$. The depth sum for the record then gives the first part of the run hypotheses at $w_L$.
3. The shared laws give a prime $q$ that is the own prime of the run, with all twisted places at $q$. The parameter conditions put $p$ at the twisted places of index $j$. So $p = q$, and $p$ is the own prime.
4. The scaled run lattices lie in the sup lattices at $p$. The scaled theta lattice lies in the sup lattice at every weight. This is claim 3.
5. The theorem on the hypotheses of the theta index bound at an instance takes the value of a harmonic germ that does not depend on the chart, the theta values of the core, the shared laws, the page and the facts of steps 3 and 4. It gives the run hypotheses, which is claim 1, and a finite spanning set $\mathcal{S}$ with the tie, which is claim 5.
6. The short theta series span the cusp forms of weight $\kappa$, since the last entry of $\kappa$ is positive. With the scalar part of the run hypotheses, the module of weight $\kappa$ is a lattice. This is claim 2.
7. The page gives the support conditions. The scalar $s_W(w_L)$ is the scalar $s(w_L)$ of the theta lattice, and $s(w_L)$ is nonzero at each embedding. This is claim 4.

This proves the theorem. $\square$

The own prime is the only prime at which the parameter conditions can hold, by step 3. The constant $C_R = 7$ and the exponent $0$ are fixed by the theorem, and the lemma of section 17 asks for $C_{R,c} = 7$.

**Remark 7.18.4 (Formalization).** The theorem `sharesAt_all` is at line 66 of [ExistsIndexBoundHypothesesWithNetAllValuedPoints.lean](lean:Development/AbelianVarietyTheory/Proofs/HeightProofs/ExistsIndexBoundHypothesesWithNetAllValuedPoints.lean#L66). For $j = m$ it passes only the part `NoCommonZero` of `GenOK` to the definite lemma. The predicates `SharesAt` and `ParOK` are at lines 79 and 24 of [GrowthConstantBoundGcR.lean](lean:Development/AbelianVarietyTheory/Definitions/HeightFunctions/GrowthConstantBoundGcR.lean#L79); `SharesAt` quantifies over the eight other fields of `FamilyHypotheses.refill`. The statement `T.exists_primeData_curve_lifting_heightBounds` is a `first | exact` wrapper at line 22 of its Statement file, which imports about twenty modules but uses one theorem. The proof `exists_primeData_heights` at line 14 of [ExistsPrimeDataCurveLiftingHeightBounds.lean](lean:Development/AbelianVarietyTheory/Proofs/HeightProofs/ExistsPrimeDataCurveLiftingHeightBounds.lean#L14) is one application of `exists_primeData_heights_of`, at line 96 of [AuxiliaryCuspFormConstantMonotone.lean](lean:Development/AbelianVarietyTheory/Proofs/HeightProofs/AuxiliaryCuspFormConstantMonotone.lean#L96), with the case $\delta = 0$ done by `NoPoint.heights_no_point`. The local data are the structure `LocalPointData` and the bound is `Heights`, at line 313 of [PublishedIntClosHolds.lean](lean:Formalism/SharpRestriction/GenusPolyhedralBounds/RelativeIndexClassSets/PublishedIntClosHolds.lean#L313). The proof `hypC_record` is at line 49 of [RunHypothesesFormsScalarsOfParameterConditions.lean](lean:Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/RunHypothesesFormsScalarsOfParameterConditions.lean#L49), under `maxHeartbeats 4000000` and `synthInstance.maxHeartbeats 400000`. It reads the page hypotheses by the pattern `⟨-, -, -, -, -, -, -, -, -, -, -, -, hnW, -, hIsL, hIsF, -⟩`, so it uses three of seventeen fields. The bound $\log |w_L| \leq 2L$ of step 1 is `log_DF_le_of_rows` at line 36. Of the conclusion of the instance theorem it keeps the first part at $w_L$ and the pattern `⟨-, Sh, hspan, -, -, hTied⟩`.
