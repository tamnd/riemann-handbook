---
title: Rigid charts from a separating blowup
decls:
  - GlobalTheory.T.exists_pointRigid_tautological_chart_unitary_boundary
  - GlobalTheory.UCanon.exists_tautB_chart_at
  - GlobalTheory.T.exists_tripleChart_unitary_boundary_pointRigid
  - GlobalTheory.UCanon.uPre_of_boundary_pointRigid
  - GlobalTheory.T.exists_tripleChart_unitary_boundary_point
  - GlobalTheory.UChart.uPre_of_boundary
  - GlobalTheory.T.rigidBoundaryChartsForFan_of_unitarySeparation
  - GlobalTheory.UChartJoin.rigidForFan_of_uStB
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Rigid charts from a separating blowup

This section proves [the theorem on rigid charts for a fan](/entry/rigid-for-fan-holds/) of Section 1 from [the separating normalized blowup](/entry/u-poin-st-x-sep/) of Section 2. Let $S$ be the blowup. At each point $x$ of $S$ outside $j(X_F)$ we first find a degenerating monomial family that specializes to $x$. Section 11 puts this family through a tautological chart $\xi : \operatorname{Spec} R \to S$ with $\xi$ of the closed point equal to $x$. Two lemmas then show that $\xi$ is an étale completion at $x$ and give the equations of the boundary and of $B$ in the chart. We call these data a *prechart* at $x$. Later results identify $S$ with a model $Y$ of $X_F$, show that $S$ is smooth with a strict normal crossings boundary, and turn each prechart into a fan chart and a rigid chart on $Y$. The last step checks the five conditions of Section 1. We use the notation of Sections 1, 2 and 11. In particular, $(Z, i, \mathcal{O}_Z(1), N, d, J, \pi : S \to Z, j, B)$ are separating blowup data with $j$ separating for $\varphi$, and $R = k[[u_1, \dots, u_m, v_1, \dots, v_e]]$ is a chart ring.

**Definition 7.12.1 (Prechart at a boundary point).** Let $x \in S$ with $x \notin j(X_F)$. A *prechart* at $x$ consists of a field $k$, integers $m, e \ge 0$, a tautological chart $C_1 = (t_1, P_1, y_1, s^1, \delta^1)$ over $R$, a map $\xi : \operatorname{Spec} R \to S$ and integers $a_1, \dots, a_m \ge 0$ such that:

1. $j \circ y_1 = \xi$ on $\operatorname{Spec} \operatorname{Frac} R$, and $\xi$ sends the closed point to $x$;
2. the stalk map $\mathcal{O}_{S, x} \to R$ of $\xi$ is an *étale completion*: it is flat, the maximal ideal of $\mathcal{O}_{S, x}$ generates the maximal ideal of $R$, and the map of residue fields is finite;
3. the ideal of $S \setminus j(X_F)$ pulls back along $\xi$ to $(u_1 \cdots u_m)$, and a point $\mathfrak{p}$ of $\operatorname{Spec} R$ maps into $j(X_F)$ if and only if $u_1 \cdots u_m \notin \mathfrak{p}$;
4. $a_i = d\, \varphi(M' \delta^1_i)$ for each $i$, and the ideal of $B$ pulls back along $\xi$ to $(\prod_i u_i^{a_i})$.

Lean: `GlobalTheory.UChart.UPre` (also `GlobalTheory.Toroidal.IsEtaleCompletion`).

Items 2 to 4 are conditions 1, 2 and 5 of a fan chart in Section 1, stated on $S$ in place of $Y_F$. Item 3 uses $s^1_i = u_i$, which is part of the definition of a tautological chart.

**Theorem 7.12.2 (Tautological chart at a boundary point).** Let $E$, $H$ and $D$ be as in Section 1 with $p + q \ge 1$, and let $\varphi$ be a polarized fan with no self-intersections in rank at most $\min(p, q)$. Let $(Z, i, \mathcal{O}_Z(1), N, d, J, \pi : S \to Z, j, B)$ be separating blowup data with $j$ separating for $\varphi$, and let $x \in S$ with $x \notin j(X_F)$. Then there are a field $k$, integers $m, e$, a tautological chart $C_1$ with rigid coordinates over $R = k[[u_1, \dots, u_m, v_1, \dots, v_e]]$ and a map $\xi : \operatorname{Spec} R \to S$ such that $j \circ y_1 = \xi$ on $\operatorname{Spec} \operatorname{Frac} R$ and $\xi$ sends the closed point to $x$.

Lean: `GlobalTheory.UCanon.exists_tautB_chart_at` (also `GlobalTheory.T.exists_pointRigid_tautological_chart_unitary_boundary`, a second name).

*Proof.* There are three steps.

1. A lemma on degenerating monomial families at boundary points gives a local domain $V$ that is a Mumford base, with algebraically closed residue field, a monomial family $(t, P, y, s, \delta)$ over $V$ with $X_P \ne 0$, and a map $\xi_V : \operatorname{Spec} V \to S$. This map satisfies $j \circ y = \xi_V$ on $\operatorname{Spec} \operatorname{Frac} V$ and sends the closed point of $V$ to $x$.
2. [The theorem on tautological charts through a family](/entry/exists-tautological-chart-versality/) of Section 11 applies to this family and $\xi_V$. It gives $k$, $m$, $e$, a tautological chart $C_1$ with rigid coordinates over $R$, a map $\xi : \operatorname{Spec} R \to S$ with $j \circ y_1 = \xi$ on $\operatorname{Spec} \operatorname{Frac} R$, and a local map $\theta : R \to V$ with $\xi \circ \operatorname{Spec} \theta = \xi_V$.
3. Since $\theta$ is local, $\operatorname{Spec} \theta$ sends the closed point of $V$ to the closed point of $R$. So $\xi$ sends the closed point of $R$ to $\xi_V$ of the closed point of $V$, which is $x$.

This gives $k$, $m$, $e$, $C_1$ and $\xi$. $\square$

**Theorem 7.12.3 (Prechart at a boundary point).** Let the data be as in the previous theorem. Then each $x \in S$ with $x \notin j(X_F)$ has a prechart.

Lean: `GlobalTheory.UCanon.uPre_of_boundary_pointRigid` (also `GlobalTheory.T.exists_tripleChart_unitary_boundary_pointRigid`, `GlobalTheory.UChart.uPre_of_boundary` and `GlobalTheory.T.exists_tripleChart_unitary_boundary_point`, second names).

*Proof.* The previous theorem gives $k$, $m$, $e$, a tautological chart $C_1$ with rigid coordinates and $\xi$ with item 1. A lemma on tautological charts with rigid coordinates in separating blowup data shows that the stalk map of $\xi$ at the closed point is an étale completion. This gives item 2. A lemma on the boundary equations of such charts gives item 3. The same lemma gives integers $a_i$ with $a_i = d\, \varphi(M' \delta^1_i)$ and with the ideal of $B$ equal to $(\prod_i u_i^{a_i})$ after pullback along $\xi$. This gives item 4. A tautological chart with rigid coordinates is a tautological chart, so $C_1$, $\xi$ and the $a_i$ form a prechart at $x$. $\square$

**Theorem 7.12.4 (Rigid charts from a separating blowup).** Suppose that the conclusion of [the theorem on the separating normalized blowup](/entry/u-poin-st-x-sep/) of Section 2 holds. That is, for all $E$, $H$, $D$ with $p + q \ge 1$, each polarized fan $\varphi$ with no self-intersections in rank at most $\min(p, q)$, and each $l$, $X$ and $F$, there are separating blowup data with $j$ separating for $\varphi$. Then the conclusion of [the theorem on rigid charts for a fan](/entry/rigid-for-fan-holds/) of Section 1 holds.

Lean: `GlobalTheory.UChartJoin.rigidForFan_of_uStB` (also `GlobalTheory.T.rigidBoundaryChartsForFan_of_unitarySeparation`, a second name).

*Proof.* Fix $E$, $H$, $D$, $\varphi$, $l$, $X$ and $F$, and take separating blowup data $(Z, i, \mathcal{O}_Z(1), N, d, J, \pi : S \to Z, j, B)$ with $j$ separating for $\varphi$. We use these parts of the data: $\mathcal{O}_Z(1)$ is a line bundle; $N \ge 1$ and item 2 of the data; $d \ge 1$ and the support of $J$ does not meet $i(X_F)$; $j$ is an open immersion with $\pi \circ j = i$; the ideal of $B$ is $\pi^{-1} J \cdot \mathcal{O}_S$; and $k_0$ with $\pi^* \mathcal{O}_Z(k) \otimes \mathcal{O}(-B)$ ample for each $k \ge k_0$.

1. *Precharts.* The previous theorem gives a prechart at each point of $S \setminus j(X_F)$.
2. *The model.* [The theorem on the model of a compactification with charts](/entry/unitary-compactification-is-model-of-charts/) gives a model $Y$ of $X_F$ over $\mathrm{id}_F$ and an isomorphism $\varepsilon : Y \to S$ with $\varepsilon \circ j_Y = j$. The structure map of $Y$ is the composite $Y \to S \to Z \to \operatorname{Spec} F$. For each tautological chart $C_1$ and each $\xi$ with $j \circ y_1 = \xi$ on $\operatorname{Spec} \operatorname{Frac} R$, the datum $t_1$ maps to the pullback of the datum of $Y$ along $\varepsilon^{-1} \circ \xi$.
3. *Smoothness.* [The theorem on smoothness and normal crossings](/entry/toroidal-compactification-smooth-snc-boundary/) shows that $S$ is smooth over $F$ of relative dimension $n_D$ and that $S \setminus j(X_F)$ is a strict normal crossings divisor.
4. *Charts.* A lemma on charts from precharts uses the precharts of step 1 and the maps of step 2. It gives at each point of $\partial Y_F$ a fan chart for $\varphi$, $\varepsilon^* B$ and $d$, and a rigid chart.

Put $B_Y = \varepsilon^* B$, keep $d$, and put $k = N k'$ with $k' = \max(k_0, 1)$. We check the conditions of Section 1.

- *Integers.* $d \ge 1$ is given, and $k \ge 1$ since $N \ge 1$ and $k' \ge 1$.
- *Condition 1.* The base change $Y_F \to Y$ along $\mathrm{id}_F$ is an isomorphism, so $Y_F \to S$ is an isomorphism. An isomorphism is smooth of relative dimension $0$. The structure map of $Y_F$ is $Y_F \to S$ followed by $S \to Z \to \operatorname{Spec} F$, so it is smooth of relative dimension $0 + n_D = n_D$. A point $w$ of $Y_F$ lies in the image of $X_F$ if and only if its image in $S$ lies in $j(X_F)$, because $\varepsilon \circ j_Y = j$ and $Y_F \to S$ is injective. So the isomorphism $Y_F \to S$ sends $\partial Y_F$ onto $S \setminus j(X_F)$. An isomorphism keeps the strict normal crossings property, so $\partial Y_F$ is a strict normal crossings divisor.
- *Condition 2.* Let $y$ be in the support of $B_Y$ and in $\operatorname{ab}(G)$. The abelian locus of a model is the image of $X_F$, so $y = j_Y(z)$ for some $z \in X_F$. The support of $B_Y$ is the inverse image of the support of $J$ under $\pi \circ \varepsilon$. So $\pi(\varepsilon(j_Y(z))) = i(z)$ is in the support of $J$. This is false, because the support of $J$ does not meet $i(X_F)$.
- *Conditions 3 and 5.* These are step 4.
- *Condition 4.* Suppose that $\omega_Y$ is a line bundle. Put $A = \pi^* \mathcal{O}_Z(k') \otimes \mathcal{O}(-B)$. Since $k' \ge k_0$, $A$ is ample on $S$, so $\varepsilon^* A$ is ample on $Y$. The map $\pi \circ \varepsilon$ extends $i$, so item 2 of the data gives $(\pi \circ \varepsilon)^* \mathcal{O}_Z(1) \cong \omega_Y^{\otimes N}$. Also $\varepsilon^* \mathcal{O}(B) \cong \mathcal{O}(B_Y)$. In the Picard group of $Y$ this gives
$$[\omega_Y^{\otimes N k'}(-B_Y)] = k' N [\omega_Y] - [\mathcal{O}(B_Y)] = k' [(\pi \circ \varepsilon)^* \mathcal{O}_Z(1)] - \varepsilon^* [\mathcal{O}(B)] = [\varepsilon^* A].$$
Two line bundles with the same class are isomorphic, and a line bundle isomorphic to an ample one is ample. So $\omega_Y^{k}(-B_Y)$ is ample.

This gives $Y$, $B_Y$, $d$ and $k$ with the five conditions. $\square$

With [the theorem on the separating normalized blowup](/entry/u-poin-st-x-sep/), this theorem gives the theorem on rigid charts for a fan, as in its proof in Section 1. The separating property of $j$ is a hypothesis of each lemma of this section, and of the later results in steps 2 and 3. In the chain of [toroidal compactifications](/learn/abelian-varieties/#toroidal-and-minimal-compactifications), the scheme $S$ plays the role of the toroidal compactification for $\varphi$, and $B$ is the boundary divisor of $d\varphi$ that makes $\omega^{k}(-B)$ ample.

**Remark 7.12.5 (Formalization).** The proofs are in [ExistsPointRigidTautologicalChartUnitaryBoundary.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsPointRigidTautologicalChartUnitaryBoundary.lean#L13), [ExistsTripleChartUnitaryBoundaryPointRigid.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsTripleChartUnitaryBoundaryPointRigid.lean#L14), [ExistsTripleChartUnitaryBoundaryPoint.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsTripleChartUnitaryBoundaryPoint.lean#L12) and [RigidBoundaryChartsForFanOfUnitarySeparation.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/RigidBoundaryChartsForFanOfUnitarySeparation.lean#L21). The `T.*` names are wrappers that close their goal with `first | exact @X | exact X | (intros; apply X <;> assumption)`. `UPre` is in [ExistsMonoFamNontrivial.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ExistsMonoFamNontrivial.lean#L156). `IsEtaleCompletion` is in [IsProperToroidalModelStructureMap.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsProperToroidalModelStructureMap.lean#L347). The name says "étale completion", but the definition asks only for item 2: flatness, the maximal ideal condition and a finite residue map. It does not ask that $R$ is a completion of an étale neighbourhood. `SepB` and `UStB` are in [FromBaseAlt.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/FromBaseAlt.lean#L45), at lines 45 and 57. `UChart.uPre_of_boundary` is the term `T.exists_tripleChart_unitary_boundary_pointRigid`, so the "point" and "pointRigid" names have the same statement. In `uPre_of_boundary_pointRigid` the proof packs `hT.1` (line 26), so it drops `HasRigidCoords` and keeps only `IsTaut`. In `exists_tautB_chart_at` the map $\theta$ is used only for the closed point and is dropped at line 19. The hypotheses $p + q \ge 1$, `IsPolFan` and `NoSelfInt` are only passed to other lemmas in all four proofs. In `rigidForFan_of_uStB` the pattern at line 24 keeps only six parts of `UPoinOnX` and drops normality, projectivity, the extension property, density and the order conditions. The full `UPoinOnX` and `SepB` are passed to the lemmas of steps 1 to 3. The divisor is `BD.pull ε.hom` on `Y.X` (line 31), while conditions 1, 3 and 5 are on `gen Y`, the base change along $\mathrm{id}_F$, through `genι Y`. Condition 2 uses `Y.ab_gen`, which says that the abelian locus is the image of $X_F$. Ampleness of $\varepsilon^* A$ comes from `pull_of_isAffineHom` (line 72). There are two definitions `RigidForFan`: `GlobalTheory.RigChart.RigidForFan` in [RigidForFan.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/RigidForFan.lean#L70), which this proof gives, and `GlobalTheory.LogKSChart.RigidForFan` in [HasRigidChart.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/HasRigidChart.lean#L67). Their texts are the same, but each uses the `HasRigidChart` and `IsRigid` of its own namespace. The proofs apply `T.exists_degenerating_monomialFamily_algClosed_residue`, `T.tautologicalChart_isEtaleCompletion_localRing`, `T.tautologicalChart_boundary_equations`, `UChartOf.charts_of_upre` (in [ChartsOfUpre.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ChartsOfUpre.lean#L57)), `SncIso.snc_vanishingIdeal_of_isIso` and `smoothOfRelativeDimension_comp`. These have no entries in this chapter, and we use only their statements. We have not unfolded `idlAlong`, `SABMap`, `Snc`, `polOf` or `CechPic`.
