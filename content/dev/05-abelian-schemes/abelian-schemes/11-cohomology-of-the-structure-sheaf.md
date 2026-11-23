---
title: Cohomology of the structure sheaf
decls:
  - GlobalTheory.T.abelianScheme_structureSheafCohomology_noetherian
  - GlobalTheory.AbCohRing.oStr_noetherian
  - GlobalTheory.UnobTop.abelianUnobstructed
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Cohomology of the structure sheaf

Let $A$ be an [[abelian scheme|JDDXZ89N33]] over a ring $R$, [[smooth|EXKGG9X6J0]] of relative dimension $g$. Over a field, $H^1(A, \mathcal{O})$ has dimension $g$ and $H^2(A, \mathcal{O})$ is its second exterior power, with the cup product as the map. This section proves the same over a noetherian ring, together with base change (Theorem (Structure cohomology)). It then states the result that the next two sections use: an abelian scheme lifts over a square zero thickening of the base (Theorem (Unobstructedness)). The proof of the first theorem reduces to fibres over fields and to artinian local rings. The proof of the second theorem uses the first, extended to all rings.

Let $R$ be a ring and $s : X \to \mathrm{Spec}\, R$ a morphism of schemes. The functor $U \mapsto \mathcal{O}(U)$ on the category of affine opens of $X$ takes values in $R$-algebras. We write $H^i(X, \mathcal{O})$, for $i = 0, 1, 2$, for the Čech type cohomology of this functor, computed from cochains indexed by chains of affine opens. It is an $R$-module, and there is a cup product $H^1(X, \mathcal{O}) \times H^1(X, \mathcal{O}) \to H^2(X, \mathcal{O})$. For a ring map $R \to R'$ and a cartesian square with $X' = X \times_R R'$, pullback gives $R$-linear maps $H^i(X, \mathcal{O}) \to H^i(X', \mathcal{O})$.

**Definition 1.11.1 (Base change for $H^i$).** We say that *$H^i$ commutes with base change for $X$* if for every $R$-algebra $R'$ and every cartesian square with $X' = X \times_R R'$, there is an isomorphism of $R'$-modules $R' \otimes_R H^i(X, \mathcal{O}) \to H^i(X', \mathcal{O})$ that sends $1 \otimes c$ to the pullback of $c$. We say that *global functions stay constant for $X$* if for every $R$-algebra $R'$ and every such $X'$, the map $R' \to H^0(X', \mathcal{O})$ is bijective.

**Definition 1.11.2 (Structure cohomology).** Let $A$ be an abelian scheme over $R$, smooth of relative dimension $g$. We say that *$A$ has the structure cohomology of dimension $g$* if these conditions hold.

1. $H^1(A, \mathcal{O})$ is a finite projective $R$-module, and its rank at each prime of $R$ is $g$.
2. There is an isomorphism $e : \bigwedge^2_R H^1(A, \mathcal{O}) \to H^2(A, \mathcal{O})$ with $e(a \wedge b) = a \cup b$ for all $a, b$.
3. $H^1$ and $H^2$ commute with base change for $A$.

We use the following facts. In each one, a base change of an abelian scheme along $\mathrm{Spec}\, R' \to \mathrm{Spec}\, R$ is an abelian scheme over $R'$, smooth of the same relative dimension.

1. (Base change criterion.) Let $R$ be noetherian and $s : X \to \mathrm{Spec}\, R$ [[proper|9537RKBZPP]] and flat, such that global functions stay constant for $X$. Suppose that for each artinian local $R$-algebra $R'$, each field $k$ and each surjective map $\alpha : R' \to k$ of $R$-algebras, the pullback maps $H^i(X_{R'}, \mathcal{O}) \to H^i(X_k, \mathcal{O})$ are surjective for $i = 1, 2$. Then $H^1(X, \mathcal{O})$ and $H^2(X, \mathcal{O})$ are finite projective $R$-modules, and $H^1$ and $H^2$ commute with base change for $X$.
2. (Constant functions.) Global functions stay constant for each abelian scheme.
3. (Artinian rings.) Let $R'$ be an artinian local ring, $A$ an abelian scheme over $R'$, smooth of relative dimension $g$, and $R' \to k$ a surjection onto a field. Then the pullback maps $H^i(A, \mathcal{O}) \to H^i(A_k, \mathcal{O})$ are surjective for $i = 1, 2$.
4. (Fields.) Let $K$ be a field and $A$ an abelian scheme over $K$, smooth of relative dimension $g$. Then $H^1(A, \mathcal{O})$ has dimension $g$, and condition 2 of the definition holds for $A$.
5. (Cup squares.) Let $R$ be noetherian and $A$ an abelian scheme over $R$, smooth of relative dimension $g$. Then $x \cup x = 0$ for each $x \in H^1(A, \mathcal{O})$.
6. (Wedge from fibres.) Let $s : X \to \mathrm{Spec}\, R$ be such that $H^1(X, \mathcal{O})$ and $H^2(X, \mathcal{O})$ are finite projective, $H^1$ and $H^2$ commute with base change for $X$, and $x \cup x = 0$ for each $x \in H^1(X, \mathcal{O})$. Suppose that condition 2 of the definition holds for $X_k$ for each field $k$ that is an $R$-algebra. Then condition 2 holds for $X$.

Fact 1 is a form of the theorem on cohomology and base change, with the surjectivity on artinian rings as its input. Fact 2 holds because $A$ is proper and flat with geometrically connected and reduced fibres. In fact 5, the cup product is alternating on $H^1$ in the Čech model.

**Theorem 1.11.3 (Structure cohomology).** Let $R$ be a noetherian ring and $A$ an abelian scheme over $R$, smooth of relative dimension $g$. Then $A$ has the structure cohomology of dimension $g$.

Lean: `GlobalTheory.AbCohRing.oStr_noetherian` (also `GlobalTheory.T.abelianScheme_structureSheafCohomology_noetherian`, a second name).

*Proof.* An abelian scheme is proper and smooth, so $A$ is proper and flat over $R$. By fact 2, global functions stay constant for $A$. Let $R'$ be an artinian local $R$-algebra and $\alpha : R' \to k$ a surjective map of $R$-algebras onto a field. The base change $A_{R'}$ is an abelian scheme over $R'$, smooth of relative dimension $g$. By fact 3, the pullback maps $H^i(A_{R'}, \mathcal{O}) \to H^i(A_k, \mathcal{O})$ are surjective for $i = 1, 2$. So fact 1 applies: $H^1(A, \mathcal{O})$ and $H^2(A, \mathcal{O})$ are finite projective, and $H^1$ and $H^2$ commute with base change for $A$. This gives condition 3.

For condition 1, let $\mathfrak{p}$ be a prime of $R$ and $\kappa$ its residue field. For a finite projective module $M$, the rank of $M$ at $\mathfrak{p}$ is $\dim_\kappa (\kappa \otimes_R M)$: the localization $M_\mathfrak{p}$ is free over the local ring $R_\mathfrak{p}$, and its rank does not change under $R_\mathfrak{p} \to \kappa$. Base change for $H^1$ along $R \to \kappa$ gives $\kappa \otimes_R H^1(A, \mathcal{O}) \cong H^1(A_\kappa, \mathcal{O})$. By fact 4 applied to the abelian scheme $A_\kappa$ over $\kappa$, this has dimension $g$. So the rank of $H^1(A, \mathcal{O})$ at $\mathfrak{p}$ is $g$.

For condition 2, we apply fact 6 to $A$. Its hypotheses on finiteness and base change hold by the first paragraph. By fact 5, $x \cup x = 0$ for each $x \in H^1(A, \mathcal{O})$. For a field $k$ that is an $R$-algebra, $A_k$ is an abelian scheme over $k$, smooth of relative dimension $g$, so condition 2 holds for $A_k$ by fact 4. So condition 2 holds for $A$. $\square$

The theorem extends to all rings. An abelian scheme over $R$ is the base change of an abelian scheme over a finitely generated subring of $R$, which is noetherian. The three conditions pass to the base change by condition 3. We use this as fact 7.

7. (All rings.) Let $R$ be a ring and $A$ an abelian scheme over $R$, smooth of relative dimension $g$. Then $A$ has the structure cohomology of dimension $g$.
8. (Invariant forms.) Let $R$ be a ring and $A$ an abelian scheme over $R$, smooth of relative dimension $g$. Then the module of differentials of $A$ over $R$ has a frame of global 1-forms $w_1, \dots, w_n$: on each affine open, each 1-form $\omega$ is $\sum_i \delta_i(\omega) w_i$ for maps $\delta_i$ compatible with restriction. Also, global functions stay constant for $A$, and each global 1-form $w$ is primitive: $m^* w = p_1^* w + p_2^* w$ on $A \times A$, where $m$ is the group law and $p_1, p_2$ are the projections.
9. (Unobstructedness from structure.) Suppose that the conclusion of fact 7 holds and that the conclusion of fact 8 holds for every abelian scheme over every ring. Then the conclusion of Theorem (Unobstructedness) below holds.

The proof of fact 9 first reduces to abelian schemes of constant relative dimension $g$. It then uses the frame of invariant forms, the vanishing of primitive classes in $H^2(A, \mathcal{O})$, and the vanishing of classes in $H^1(A \times A, \mathcal{O})$ that are zero on both axes $A \times \{1\}$ and $\{1\} \times A$. The last two follow from conditions 1 and 2 of the definition, and the proof extends them to square zero extensions of the base.

**Theorem 1.11.4 (Unobstructedness).** Let $R$ be a ring, $I$ an ideal of $R$ with $I^2 = 0$, and $\pi : R \to R_0$ a surjective ring map with kernel $I$. Let $A_0$ be an abelian scheme over $R_0$. Then there are an abelian scheme $A$ over $R$ and a morphism $i : A_0 \to A$ such that the square formed by $i$, the structure maps and $\mathrm{Spec}\, R_0 \to \mathrm{Spec}\, R$ is cartesian and $i$ is compatible with the group laws.

Lean: `GlobalTheory.UnobTop.abelianUnobstructed`.

*Proof.* Fact 7 gives the first hypothesis of fact 9. For an abelian scheme $A$ over a ring $R$, smooth of relative dimension $g$, fact 8 gives the frame, the constant functions and the primitive forms. So fact 9 applies, and its conclusion is the theorem. $\square$

So $A$ is a lift of $A_0$ to $R$ as a group scheme. The theorem does not say that the lift is unique. The last section of this part uses it as one of its inputs.

**Remark 1.11.5 (Formalization).** Facts 1 to 6 are `GlobalTheory.T.structure_cohomology_residue_field_fibre`, `GlobalTheory.T.globalFunctionsConstantAfterBaseChange_of_abelianScheme`, `GlobalTheory.T.abelianSchemeSpecialFibre_cohomology_lift_artinian`, `GlobalTheory.T.abelianVariety_structureSheaf_cohomology_anyField`, `GlobalTheory.T.cup_self_zero_abelian_h1` and `GlobalTheory.T.wedge_property_from_fibres`. Facts 7 to 9 are `GlobalTheory.T.abelian_structure_cohomology_statement`, `GlobalTheory.T.abelianScheme_oneFormFrame_and_primitiveOneForms` together with fact 2, and `GlobalTheory.T.abelianScheme_unobstructed_of_cohomology_structure`. They are cited by their statements; the sentences on why they hold are not read from proofs, except for fact 7, whose proof `GlobalTheory.AbCoh.oStr_of_noetherian` descends $A$ to a finitely generated subring and calls the second name of Theorem (Structure cohomology). The three conditions of the definition are `GlobalTheory.AbCoh.FP`, `GlobalTheory.AbCoh.WedgeO`, `GlobalTheory.AbCoh.StructureSheafH1BaseChange` and `GlobalTheory.AbCoh.StructureSheafH2BaseChange`, and their conjunction over all rings is `GlobalTheory.AbCoh.OStr`. The groups $H^i(X, \mathcal{O})$ are `HO1` and `HO2`, the cohomology of the functor `OAff` on affine opens; this section does not compare them with sheaf cohomology. The base change of an abelian scheme is `GlobalTheory.AbCohRing.exists_grpObj_of_isPullback`, and the rank at a prime is `GlobalTheory.AbCohRing.rankAtStalk_eq_finrank_residueField`. Fact 4 also gives two more vanishing results that the proof drops. The statement of Theorem (Unobstructedness) has no dimension hypothesis and no noetherian hypothesis; the reduction to constant relative dimension is inside fact 9. The module name `AbelianSchemeUnobstructedSquareZeroAffine` of the theorem does not match its content, which is about any ring. The second name of Theorem (Structure cohomology) is closed by a `first` list under `set_option maxHeartbeats 1000000`, and its file imports `Mathlib` twice.
