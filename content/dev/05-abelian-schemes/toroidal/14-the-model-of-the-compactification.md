---
title: The model of the compactification
decls:
  - GlobalTheory.T.unitary_compactification_isModel_of_charts
  - GlobalTheory.UChart.exists_model_of_charts
  - GlobalTheory.T.exists_triple_on_descended_group
  - GlobalTheory.DescTriple.exists_triple_of_group_sepB
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The model of the compactification

This section makes the blowup $S$ of Section 2 into a model $Y$ of $X_F$ over $\mathrm{id}_F$. The main step puts a semi-abelian datum on $S$ that extends the universal object on $X_F$. The group scheme comes from a descent lemma along tautological charts, and the result here adds the action of $\mathcal{O}_E$, the cubical line bundle and the two conditions on the polarization. The model also receives a map of semi-abelian data from each tautological chart. [The theorem on rigid charts from a separating blowup](/entry/rigid-boundary-charts-for-fan-of-unitary-separation/) of Section 12 uses this model, and so does the next section. We use the notation of Sections 1, 2 and 12. In particular, $(Z, i, \mathcal{O}_Z(1), N, d, J, \pi : S \to Z, j, B)$ are separating blowup data with $j$ separating for $\varphi$, and $z_S : Z \to \operatorname{Spec} F$ is the structure map of $Z$. For a chart ring $R$ we write $j_R : \operatorname{Spec} \operatorname{Frac} R \to \operatorname{Spec} R$ for the generic point.

**Theorem 7.14.1 (Model of the compactification).** Let $E$, $H$ and $D$ be as in Section 1 with $p + q \ge 1$, and let $\varphi$ be a polarized fan with no self-intersections in rank at most $\min(p, q)$. Let $(Z, i, \mathcal{O}_Z(1), N, d, J, \pi : S \to Z, j, B)$ be separating blowup data with $j$ separating for $\varphi$, and suppose that each $x \in S$ with $x \notin j(X_F)$ has a prechart. Then there are a model $Y$ of $X_F$ over $\mathrm{id}_F$ and an isomorphism $\varepsilon : Y \to S$ such that:

1. $\varepsilon \circ j_Y = j$, and the structure map of $Y$ is $z_S \circ \pi \circ \varepsilon$;
2. for each tautological chart $C_1 = (t_1, P_1, y_1, s^1, \delta^1)$ over a chart ring $R$ and each $\xi : \operatorname{Spec} R \to S$ with $j \circ y_1 = \xi \circ j_R$, there is a map of semi-abelian data from $t_1$ to the datum of $Y$ over $\varepsilon^{-1} \circ \xi$.

Lean: `GlobalTheory.UChart.exists_model_of_charts` (also `GlobalTheory.T.unitary_compactification_isModel_of_charts`, a second name).

*Proof.* There are four steps.

1. The universal object of $X$ pulls back along the projection $X_F \to X$ to an object over $X_F$. Let $t_F$ be its semi-abelian datum. It comes with a map of semi-abelian data from $t_F$ to the universal datum over the projection.
2. A lemma on semi-abelian descent along toric charts applies to the data, the separation of $j$, the precharts and $t_F$. It gives a commutative semi-abelian group scheme $G$ over $S$ and a map $e$ from the group of $t_F$ to $G$, such that the group of $t_F$ is the pullback of $G$ along $j$ through $e$, and $\operatorname{ab}(G) = j(X_F)$. It also gives the hypothesis on charts in the next theorem.
3. [The theorem on the datum of a descended group](/entry/exists-triple-of-group-sep-b/) below gives a semi-abelian datum $t$ on $S$ with group $G$, a map of semi-abelian data from $t_F$ to $t$ over $j$, and for each tautological chart $C_1$ and $\xi$ as in item 2 a map of semi-abelian data from $t_1$ to $t$ over $\xi$.
4. We define $Y$. Its scheme is $S$, with structure map $z_S \circ \pi$. By item 5 of the separating blowup data, $S$ is normal and projective over $F$, and $S$ is flat over $F$ because $F$ is a field. The projection $g : S \times_F F \to S$ along $\mathrm{id}_F$ is an isomorphism. Put $j_Y = g^{-1} \circ j$. It is an open immersion over $F$, because $\pi \circ j = i$ and $i$ lies over $F$ by item 1. Its image is dense, because $g^{-1}$ is a homeomorphism and $j$ has dense image. The datum of $Y$ is $t$, with the maps of steps 1 and 3. The abelian locus of $t$ is $\operatorname{ab}(G) = j(X_F)$, so its preimage under $g$ is the image of $j_Y$.

Let $\varepsilon$ be the identity of $S$. Then $\varepsilon \circ j_Y = g \circ g^{-1} \circ j = j$ and the structure map of $Y$ is $z_S \circ \pi \circ \varepsilon$. Item 2 is the last part of step 3. $\square$

The theorem uses only five parts of the separating blowup data directly: $i$ lies over $F$, $\pi$ is a normalized blowup, $S$ is projective, $j$ has dense image, and $\pi \circ j = i$. All the data, the separation and the precharts go to the lemmas of steps 2 and 3.

**Theorem 7.14.2 (Datum of a descended group).** Let $E$, $H$, $D$, $\varphi$ and the separating blowup data be as in the previous theorem, and suppose that each $x \in S$ with $x \notin j(X_F)$ has a prechart. Let $t_F$ be a semi-abelian datum on $X_F$ with a map to the universal datum over the projection $X_F \to X$. Let $G$ be a commutative semi-abelian group scheme over $S$ and $e$ a map from the group $G_F$ of $t_F$ to $G$ such that $G_F$ is the pullback of $G$ along $j$ through $e$. Suppose the following for each tautological chart $C_1$ over a chart ring $R$ and each $\xi : \operatorname{Spec} R \to S$ with $j \circ y_1 = \xi \circ j_R$. For each semi-abelian datum $t_K$ on $\operatorname{Spec} \operatorname{Frac} R$ with maps $a : t_K \to t_1$ over $j_R$ and $b : t_K \to t_F$ over $y_1$, there is a map $\pi_C$ from the group of $t_1$ to $G$ such that the group of $t_1$ is the pullback of $G$ along $\xi$ through $\pi_C$ and $\pi_C \circ a = e \circ b$ on groups. Then there is a semi-abelian datum $t$ on $S$ with group $G$ such that:

1. there is a map of semi-abelian data from $t_F$ to $t$ over $j$;
2. for each $C_1$ and $\xi$ as above, there is a map of semi-abelian data from $t_1$ to $t$ over $\xi$.

Lean: `GlobalTheory.DescTriple.exists_triple_of_group_sepB` (also `GlobalTheory.T.exists_triple_on_descended_group`, a second name).

*Proof.* We extend each part of the datum $t_F$ from $X_F$ to $S$.

1. A lemma on ring actions gives an action of $\mathcal{O}_E$ on $G$ that is compatible with the action on $G_F$ through $e$.
2. A lemma on cubical bundles gives a rigidified line bundle $L$ on $G$ with a cubical structure, such that $L$ is symmetric, and a map from the line bundle of $t_F$ to $L$ over $e$ that respects the rigidification and the cubical structures.
3. Two lemmas extend the conditions of a semi-abelian datum on the polarization from $t_F$ to $L$: the compatibility of $L$ with the action through $a \mapsto \bar a$, and the isomorphism of $L$ with the cube combination of $1$ and $w_0$.
4. Let $t$ consist of $G$, the action of step 1 and the line bundle of step 2, with the conditions of step 3. The maps $e$ and the map of line bundles of step 2 form a map of semi-abelian data from $t_F$ to $t$ over $j$. This gives item 1.
5. Let $C_1$ and $\xi$ be as in item 2. The family $C_1$ has a datum $t_K$ on $\operatorname{Spec} \operatorname{Frac} R$ with a map $a : t_K \to t_1$ over $j_R$ and a map to the universal datum over the composite of $y_1$ and the projection. Maps of semi-abelian data are cartesian, so a cancellation lemma factors this map through the map of $t_F$ to the universal datum. This gives $b : t_K \to t_F$ over $y_1$. The hypothesis now gives $\pi_C$.
6. A lemma on actions on charts shows that $\pi_C$ respects the actions of $\mathcal{O}_E$, and a lemma on cubical extensions gives a map from the line bundle of $t_1$ to $L$ over $\pi_C$ that respects the cubical structures. So $\pi_C$ is part of a map of semi-abelian data from $t_1$ to $t$ over $\xi$. This gives item 2. $\square$

The proof does not use that $j$ is separating.

**Remark 7.14.3 (Formalization).** The proofs are in [UnitaryCompactificationIsModelOfCharts.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UnitaryCompactificationIsModelOfCharts.lean#L16) and [ExistsTripleOnDescendedGroup.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsTripleOnDescendedGroup.lean#L19). The `T.*` names are wrappers, at line 10 of the matching `Statement` files, that close their goal with `first | exact @X | exact X | (intros; apply X <;> assumption)`. In `exists_model_of_charts` the pattern at line 22 keeps only `hiz`, `hNB`, `hproj`, `hjd` and `hji` of `UPoinOnX`, the hypotheses $p + q \ge 1$, `IsPolFan` and `NoSelfInt` are only passed on (lines 20 and 21), flatness is found by `inferInstance`, and $\varepsilon$ is `Iso.refl S` (line 67). The scheme of $Y$ is $S$ itself, so the isomorphism $\varepsilon$ adds nothing; the base change $S \times_F F$ appears only in the field `jQ`. In `exists_triple_of_group_sepB` the hypothesis `SepB` is the unused variable `_hSep` (line 20), and the equality of abelian loci is `rfl`, since the group of $t$ is $G$. The datum $t_K$ of step 5 is the field `gen` of the family (line 31), and the factorization is `sabCancel pullCubCancel` (line 32). The proofs apply `LevelQuotRep.obj_pull_same`, `T.exists_semiAbelian_descent_of_toricCharts_corrected_sep`, `T.exists_ringAction_extend_descended_semiAbelian`, `T.exists_rigidified_symmetric_cubicalBundle_extension`, `T.hermitianAdjointnessIso_extends_descendedGroup`, `T.principalPolarisationIso_extends_descendedGroup`, `T.chart_ringAction_compatible_extended` and `T.rigidCubicalExtension_pullback_of_toricChart`. They have no entries in this chapter, and we use only their statements. We have not unfolded `IsGrpPullback`, `IsSemiAbelian` or `SABMap` beyond Section 1.
