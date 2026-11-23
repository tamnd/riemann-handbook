---
title: Constant degeneration data
decls:
  - GlobalTheory.KSFlatPer.isConstAlong_of_heat_flat
  - GlobalTheory.T.degenerationData_constant_of_flat_heatOperators
  - GlobalTheory.KSConst.isConstAlong_of_ks_zero
  - GlobalTheory.T.isConstAlong_of_kodairaSpencer_zero_chart
  - GlobalTheory.ChartConst.isConstAlong_of_ks_mem
  - GlobalTheory.T.degeneration_constant_of_logKodairaSpencer_mem
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Constant degeneration data

This section proves that the degeneration data on a chart are constant along a tangent vector when the Kodaira-Spencer matrix vanishes at the closed point. Here constant means the condition in the definition of a rigid chart in Section 1. We prove it in three steps. First, a basic heat operator with defect $0$ and symbol in the maximal ideal gives the condition. This step puts together the results of Section 22. Second, on a chart ring, a derivation whose Kodaira-Spencer matrix lies in the maximal ideal has such a heat operator. Third, we move the statement from an affine open of a model to a chart at a boundary point. Section 24 applies the third theorem to a rigid chart and gets injectivity of the log Kodaira-Spencer map modulo a maximal ideal. That is item 5 of the lemma in Section 16.

We use the notation of Section 22. Let $k$ be a field of characteristic $0$ and $R = k[[u_1, \dots, u_m, v_1, \dots, v_e]]$ the chart ring. Let $t$ be a semi-abelian datum on $\operatorname{Spec} R$ and $P$ a uniformization of $t$ by degeneration data, with abelian part $A$, line bundle $L$, character lattice $X$, points $c(y)$ and periods $\tau(y, z)$. Let $\gamma_1, \dots, \gamma_m$ be linearly independent forms on $X$ such that $P$ is monomial in the $u_i$ with exponents $\gamma_i$. Suppose that $G$ is abelian exactly over $D(u_1 \cdots u_m)$. For a ring map $\rho : R \to k[\varepsilon]$ we write $\bar\rho$ for the constant map that $\rho$ gives modulo $\varepsilon$. Comparisons for $\rho$, the units $w(s)$ of an isomorphism $w$, and the unit parts $\tau_0$ of $\tau(y, z)$ are as in Section 22.

**Definition 7.23.1 (Constant along a tangent vector).** Let $\rho : R \to k[\varepsilon]$ be a ring map and $a \in k^m$. The pair $(t, P)$ is *constant along $\rho$ with rates $a$* if there are a comparison $(B', \pi_1, \pi_2, c')$ for $\rho$ and an isomorphism $w : \pi_1^* L \to \pi_2^* L$ such that for all $y, z \in X$ and each unit part $\tau_0$ of $\tau(y, z)$
$$\tau_0(\rho) = \frac{w(c'(y + z))\, w(c'(0))}{w(c'(y))\, w(c'(z))} \Bigl(1 + \varepsilon \textstyle\sum_i a_i\, \gamma_i(y, z)\Bigr)\, \tau_0(\bar\rho).$$

This is the precise form of the hypothesis in the definition of a rigid chart in Section 1. The abelian part, with its line bundle and the points $c(y)$, pulls back to the same data along $\rho$ and along $\bar\rho$. The periods agree up to a coboundary of $w \circ c'$ and the factors $1 + \varepsilon \sum_i a_i \gamma_i(y, z)$. These factors come from the log deformations of the torus.

**Theorem 7.23.2 (Constant data from a flat heat operator).** Let the data be as above. Let $H$ be a Raynaud extension of $P$, $v_1, \dots, v_n$ a basis of its tangent vectors at the origin and $\partial_1, \dots, \partial_n$ invariant vector fields for them. Let $D$ be a derivation of $R$ with $D(u_i) = q_i u_i$ for elements $q_i \in R$. Let $h$ be a basic heat operator for $D$ with defect $0$ whose symbol has all entries in $\mathfrak{m}_R$. Let $\rho(r) = r(0) + \varepsilon\, (D r)(0)$. Then there is a rational $c \neq 0$ such that $(t, P)$ is constant along $\rho$ with rates $c\, q_1(0), \dots, c\, q_m(0)$.

Lean: `GlobalTheory.KSFlatPer.isConstAlong_of_heat_flat` (also `GlobalTheory.T.degenerationData_constant_of_flat_heatOperators`, a second name).

*Proof.* We construct the parts of the definition in turn.

1. A lemma on the abelian part uses the heat operator $h$ and the fact that its symbol is in $\mathfrak{m}_R$. It gives a group scheme $B'$ over $k[\varepsilon]$ and maps $\pi_1, \pi_2 : B' \to A$ that satisfy conditions 1 and 2 of a comparison. So $B'$ is the pullback of $A$ along $\operatorname{Spec} \rho$ by $\pi_1$ and along $\operatorname{Spec} \bar\rho$ by $\pi_2$, and the two maps agree on the closed fibre.
2. A lemma on the points $c(y)$ uses the same data and $(B', \pi_1, \pi_2)$. For each $y \in X$ it gives a section $c'(y)$ of $B'$ over $k[\varepsilon]$ with $\pi_1 c'(y) = c(y) \circ \operatorname{Spec} \rho$ and $\pi_2 c'(y) = c(y) \circ \operatorname{Spec} \bar\rho$. We choose one such section for each $y$. Then $(B', \pi_1, \pi_2, c')$ is a comparison for $\rho$.
3. The theorem on periods along a tangent vector in Section 22 applies to this comparison. It gives a rational $c \neq 0$ and an isomorphism $w$ with the identity of the definition for $a_i = c\, q_i(0)$.

The comparison and $w$ are the data that the definition asks for. $\square$

The proof in Section 22 takes $c = -1$. So the rates are $-q_i(0)$, the opposite of the first-order change of the boundary parameters along $D$.

**Theorem 7.23.3 (Constant data from a vanishing Kodaira-Spencer matrix).** Let the data be as above. Let $v_1, \dots, v_n$ be tangent vectors of $G$ along $\operatorname{Spec} R$ such that each tangent vector is a unique $R$-linear combination of them. Let $D$ be a derivation of $R$ with $D(u_i) = q_i u_i$ for elements $q_i \in R$. Let $\Theta$ be a Kodaira-Spencer matrix of $D$ along $D(u_1 \cdots u_m)$ on the affine scheme $\operatorname{Spec} R$, in the sense of Section 16, and suppose that all entries of $\Theta$ lie in $\mathfrak{m}_R$. Let $\rho(r) = r(0) + \varepsilon\, (D r)(0)$. Then there is a rational $c \neq 0$ such that $(t, P)$ is constant along $\rho$ with rates $c\, q_1(0), \dots, c\, q_m(0)$.

Lean: `GlobalTheory.KSConst.isConstAlong_of_ks_zero` (also `GlobalTheory.T.isConstAlong_of_kodairaSpencer_zero_chart`, a second name).

*Proof.* We build a heat operator for $D$ and apply the previous theorem.

1. The chart ring is Noetherian and complete for its maximal ideal. So the data of Section 17 apply to $R$.
2. The degeneration data $P$ have a Raynaud extension $H$. A lemma on Raynaud extensions gives a basis $v'_1, \dots, v'_{n'}$ of the tangent vectors of $H$ at the origin with invariant vector fields $\partial_1, \dots, \partial_{n'}$.
3. Each $u_i$ is nonzero, since its coefficient at the monomial $u_i$ is $1$.
4. We have $D(u_i) = q_i u_i \in (u_i)$. So [the theorem on torus invariant heat operators that commute with the periods](/entry/exists-torus-invariant-heat-operator-commuting-periods/) gives a basic heat operator $h$ for $D$ with defect $0$.
5. A lemma on symbols gives that the symbol of $h$ has all entries in $\mathfrak{m}_R$. Its proof is as follows. By [the theorem that the symbol is the Kodaira-Spencer matrix](/entry/is-ks-of-heat/) of Section 20, the symbol of $h$ is a Kodaira-Spencer matrix of $D$ for the tangent vectors that $v'$ gives on $G$. Over the abelian locus of the chart, two Kodaira-Spencer matrices of $D$ for two bases differ by the change of basis. So the symbol is obtained from $\Theta$ by a change of basis over $R$, and its entries lie in $\mathfrak{m}_R$ with those of $\Theta$.
6. The previous theorem, applied to $H$, $v'$, $\partial$, $D$ and $h$, gives the claim. $\square$

So on a chart, a derivation whose Kodaira-Spencer matrix vanishes at the closed point gives a tangent vector $\rho$ along which the data are constant. The rates are fixed by the values $q_i(0)$, that is, by the action of $D$ on the boundary parameters at the closed point.

The last theorem moves this statement from a model to a chart. We use the notation of Section 16. Let $E$, $H$ and $D$ be as in Section 1, and let $Y$ be a model of $X_F$ over $\mathrm{id}_F$ with semi-abelian datum $t_Y$ and group $G_Y \to Y$. Let $U$ be an affine open of $Y$ and $v_1, \dots, v_n$ a basis of the tangent vectors of $G_Y$ along $U$. Let $\mathfrak{m}$ be a maximal ideal of $\Gamma(U)$ and $x$ a point of $U$ off $j(X_F)$ at which each element of $\mathfrak{m}$ vanishes.

**Theorem 7.23.4 (Constant data at a boundary point).** Let the data be as above. Let $D$ be a log derivation of $\Gamma(U)$ and $\Theta$ a Kodaira-Spencer matrix of $D$ along $j(X_F)$ with all entries in $\mathfrak{m}$. Let $k$ be a field, $R = k[[u_1, \dots, u_m, v_1, \dots, v_e]]$ and $\xi : \operatorname{Spec} R \to Y_F$ a map that sends the closed point to a point $x'$ over $x$. Let $t$, $P$ and $\gamma_1, \dots, \gamma_m$ be data on $\operatorname{Spec} R$ that satisfy conditions 1 to 3 of a fan chart in Section 1, where $t$ has a map to the pullback of $t_Y$ and the $\gamma_i$ are part of a basis of the forms. Suppose that $\xi$ maps $\operatorname{Spec} R$ into $U$. Let $D_R$ be a derivation of $R$ with $D_R(\xi^* r) = \xi^*(D r)$ for $r \in \Gamma(U)$ and $D_R(u_i) = a_i u_i$ for elements $a_i \in R$. Let $\rho(r) = r(0) + \varepsilon\, (D_R r)(0)$. Then there is a rational $c_0 \neq 0$ such that $(t, P)$ is constant along $\rho$ with rates $c_0\, a_1(0), \dots, c_0\, a_m(0)$.

Lean: `GlobalTheory.ChartConst.isConstAlong_of_ks_mem` (also `GlobalTheory.T.degeneration_constant_of_logKodairaSpencer_mem`, a second name).

*Proof.* We check the hypotheses of the previous theorem for $t$, $P$, $D_R$ and the pullback of $\Theta$.

1. A lemma on charts gives that $k$ has characteristic $0$. Its only input is the map $\xi$ to $Y_F$, and $F$ has characteristic $0$.
2. A lemma on charts gives a ring map $\chi : \Gamma(U) \to R$ such that $\xi$, followed by $Y_F \to Y$, is $\operatorname{Spec} \chi$ followed by the inclusion $U \subseteq Y$.
3. A lemma on pullbacks of bases gives tangent vectors $v^R_1, \dots, v^R_n$ of $G$ along $\operatorname{Spec} R$. Each tangent vector is a unique $R$-linear combination of them, and they are the images of the $\chi(v_a)$ under the map of semi-abelian data.
4. A lemma on the abelian locus gives that $G$ is abelian exactly over $D(u_1 \cdots u_m)$. This uses condition 2 of a fan chart. In particular $\operatorname{Spec} \chi$ maps $D(u_1 \cdots u_m)$ into $j(X_F)$.
5. Since the $\gamma_i$ are part of a basis, they are linearly independent.
6. A lemma on Kodaira-Spencer matrices gives that the pullback is compatible with maps of semi-abelian data. So the matrix $\chi(\Theta)$ is a Kodaira-Spencer matrix of $D_R$ along $D(u_1 \cdots u_m)$ for the vectors $v^R$.
7. Let $a, b$ be indices. The element $\Theta_{ab}$ lies in $\mathfrak{m}$, so it vanishes at $x$. The closed point of $\operatorname{Spec} R$ maps to $x$. So $\chi(\Theta_{ab})$ lies in $\mathfrak{m}_R$.
8. The previous theorem, applied to $D_R$ with $q_i = a_i$ and the matrix $\chi(\Theta)$, gives the claim. $\square$

The other steps are bookkeeping. They move $D_R$ to the global sections of $\operatorname{Spec} R$ and cancel the isomorphism $\Gamma(\operatorname{Spec} R) \cong R$.

**Remark 7.23.5 (Formalization).** The proofs are in [DegenerationDataConstantOfFlatHeatOperators.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/DegenerationDataConstantOfFlatHeatOperators.lean#L20), [IsConstAlongOfKodairaSpencerZeroChart.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsConstAlongOfKodairaSpencerZeroChart.lean#L26) and [DegenerationConstantOfLogKodairaSpencerMem.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/DegenerationConstantOfLogKodairaSpencerMem.lean#L62). The `T.*` names are wrappers, at line 16, line 16 and line 20 of the matching `Statement` files, that close their goal with `first | exact @X | exact X | (intros; apply X <;> assumption)`. The definition above is `GlobalTheory.RigChart.IsConstAlong` in [RigidForFan.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/RigidForFan.lean#L33). It also asks that $w$ is a generator. A second definition with the same short name, `GlobalTheory.LogKSChart.IsConstAlong`, is in [HasRigidChart.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/HasRigidChart.lean#L32). It has an extra additive map $X \to k$ and an extra unit of $k[\varepsilon]$. The three theorems here use only the first one. In the first proof, steps 1 and 2 are `T.abelian_part_constant_heat_operator_symbol_in_maximal_ideal` and `T.heatOperators_symbol_zero_torsion_points_horizontal` (lines 22 and 23), and step 3 is `T.unitPart_periods_constant_along_tangent` (line 24). In the second proof, step 1 is `MumfordChart.admissibleBase_chartRing` (line 28). The Raynaud extension of step 2 comes from an instance `Nonempty (Ray _)` (line 32). That instance, in [IsLinearHomPull.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/IsLinearHomPull.lean#L40), is proved from `GlobalTheory.allSixLaws`. Lines 37 to 40 of the second file rebuild $D$ as a derivation over $\mathbb{Z}$ from its four laws before they call the theorem of step 4. Step 5 is `T.heat_symbol_mem_maximalIdeal_of_kodairaSpencer_zero` (line 51); we read its proof only to the names `KSFrameChange.isKS_frame_change`, `KSZeroMod.exists_basis_isKS_symbol` and `T.kodairaSpencer_matrix_unique_over_chart_abelian_locus`. In the third proof, the steps are `LocReg.charZero_of_chart`, `LocReg.comp_genι_eq_spMap_chartHom`, `LocReg.BasisPull.exists_basis_pull`, `ChartAbLocus.mem_abLocus_iff`, `IsPartOfBasis.linearIndependent`, `T.cechKodairaSpencer_pullback_semiAbelianMap` and the helper `valR_mem_maximalIdeal` (line 46). The helper `exists_derivation_top` (line 32) does the bookkeeping. The lemmas without links have no entries in this chapter, and we use only their statements. The statement of the third theorem has more hypotheses than the proof uses. The `intro` at line 63 names $p + q \ge 1$, smoothness, the normal crossings condition, the action matrices $A(a)$ and their property, the maximality of $\mathfrak{m}$, the fact that $x$ is off $j(X_F)$, the étale completion condition and the condition on the boundary ideal, and the proof never uses them. So the third theorem holds for any map $\xi$ with conditions 2 and 3.
