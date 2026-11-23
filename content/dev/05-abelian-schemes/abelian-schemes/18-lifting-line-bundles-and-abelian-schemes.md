---
title: Lifting line bundles and abelian schemes
decls:
  - GlobalTheory.T.exists_lineBundle_lift_squareZero_of_mumfordBundle
  - GlobalTheory.LBObs.exists_lift_of_lam_iso_pull
  - GlobalTheory.T.abelianScheme_unobstructed_of_cohomology_structure
  - GlobalTheory.abelianUnobstructed_of_struct
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Lifting line bundles and abelian schemes

This section proves two lifting results over a square zero thickening $R \to R_0$. The first lifts a line bundle $L_0$ on an abelian scheme over $R_0$ to a given lift of the abelian scheme, as soon as its Mumford bundle $\Lambda(L_0)$ lifts and $R_0$ is local (Theorem (Lifting line bundles)). The second is fact 9 of the section on the cohomology of the structure sheaf: the cohomological facts of that section imply that every abelian scheme lifts over a square zero thickening (Theorem (Unobstructedness from structure)). That fact gives [Theorem 1.11.4](/entry/abelian-unobstructed/) (Unobstructedness). Both proofs rest on one principle: an obstruction class that is additive for the group law of an abelian scheme vanishes. The first result lifts a polarization step by step along the thickenings $R/\mathfrak{m}^{e+1} \to R/\mathfrak{m}^e$ of a local ring, which is used for the algebraization of the next sections. Both are used on the way to [EveryCharacter](/step/every-character/).

Throughout, $\pi : R \to R_0$ is a surjective ring map whose kernel $I$ has $I^2 = 0$. As in the section on additive line bundles, line bundles are given by Čech data on affine opens, $\mathrm{Pic}$ is written additively, and for a line bundle $L$ on a commutative group scheme $B_0$ the *Mumford bundle* is the bundle on $B_0 \times B_0$
$$\Lambda(L) = m^* L - p_1^* L - p_2^* L + 1^* L,$$
where $m$ is the group law, $p_1$, $p_2$ are the projections and $1$ is the constant map to the unit. For a group scheme $B$ over $R$ and a group scheme $B_0$ over $R_0$, a morphism $i : B_0 \to B$ is a *group pullback* if the square formed by $i$, the structure maps and $\mathrm{Spec}\, \pi$ is cartesian and $i$ respects the group laws. A morphism $i_2 : B_0 \times B_0 \to B \times B$ is *compatible with $i$* if $p_k \circ i_2 = i \circ p_k$ for $k = 1, 2$; then $i_2 = i \times i$.

**Obstructions.** Let $X_0$ be a scheme over $R_0$ and $X$ a smooth scheme over $R$ with $X_0 = X \times_R R_0$. Let $R_1$ be an $R_0$-algebra with a retraction $q : R_1 \to R_0$ whose kernel has square zero and is identified with $I$, for example $R_1 = R_0 \oplus I$. A line bundle $L_0$ on $X_0$ has an *obstruction class* $\mathrm{ob}(L_0) \in H^2(X_0, R_1 \otimes_{R_0} \mathcal{O})$, defined from a lift system of $X_0$ in the sense of the section on square zero lifts: one lifts the transition functions of $L_0$ to the lifted rings and measures the failure of the cocycle rule, a 2-cochain with values in $I \otimes \mathcal{O}$. We use the following facts.

1. (Existence.) Each line bundle on $X_0$ has an obstruction class, for each lift system.
2. (Vanishing.) If $\mathrm{ob}(L_0) = 0$ and $X$ presents the lift system, then there is a line bundle $L$ on $X$ with $L|_{X_0} \cong L_0$.
3. (Additivity.) $\mathrm{ob}(L_0 + L_0') = \mathrm{ob}(L_0) + \mathrm{ob}(L_0')$.
4. (Restriction.) If $L_0 \cong P|_{X_0}$ for a line bundle $P$ on $X$ and $X$ presents the lift system, then $\mathrm{ob}(L_0) = 0$.
5. (Naturality.) Let $f_0 : Y_0 \to X_0$ be a morphism over $R_0$ that is the reduction of a morphism $f : Y \to X$ over $R$. Then $f_0^* \mathrm{ob}(L_0) = \mathrm{ob}(L_0')$ for each $L_0' \cong f_0^* L_0$.
6. (Primitive classes.) Let $A_0$ be an abelian scheme over $R_0$, smooth of relative dimension $g$, and $R_1$ as above. If $c \in H^2(A_0, R_1 \otimes \mathcal{O})$ and $c_1, c_2 \in H^2(A_0 \times A_0, R_1 \otimes \mathcal{O})$ satisfy $m^* c = c_1 + c_2$, $p_1^* c = c_1$ and $p_2^* c = c_2$, then $c = 0$.

Fact 6 extends to the coefficients $R_1 \otimes \mathcal{O}$ the vanishing of primitive classes in $H^2(A_0, \mathcal{O})$, which follows from $H^2 = \bigwedge^2 H^1$ and the primitivity of the classes in $H^1$: in $\bigwedge^2 H^1(A_0 \times A_0, \mathcal{O})$ the pullback $m^*(a \wedge b) = (p_1^* a + p_2^* a) \wedge (p_1^* b + p_2^* b)$ has the mixed terms $p_1^* a \wedge p_2^* b + p_2^* a \wedge p_1^* b$, which the sum $p_1^*(a \wedge b) + p_2^*(a \wedge b)$ does not have.

**Theorem 1.18.1 (Lifting line bundles).** Let $\pi : R \to R_0$ be surjective with $(\ker \pi)^2 = 0$, and assume $R_0$ is local. Let $B$ be an abelian scheme over $R$, $B_0$ a commutative group scheme over $R_0$ and $i : B_0 \to B$ a group pullback. Let $i_2 : B_0 \times B_0 \to B \times B$ be compatible with $i$. Let $P$ be a line bundle on $B \times B$ and $L_0$ a line bundle on $B_0$ with $\Lambda(L_0) \cong i_2^* P$. Then there is a line bundle $L$ on $B$ with $i^* L \cong L_0$.

Lean: `GlobalTheory.LBObs.exists_lift_of_lam_iso_pull` (also `GlobalTheory.T.exists_lineBundle_lift_squareZero_of_mumfordBundle`, a second name).

So the obstruction to lifting $L_0$ is the obstruction to lifting $\Lambda(L_0)$. In the application to a tower $R/\mathfrak{m}^{e+1} \to R/\mathfrak{m}^e$, the bundle $P$ is a fixed bundle on $B \times B$ over the top ring, and the theorem lifts $L_0$ one step.

*Proof.* As a base change of an abelian scheme, $B_0$ is an abelian scheme over $R_0$, smooth of some relative dimension $g$. Fix $R_1$ with a retraction as above; it exists for every square zero thickening. Since $B$ and $B \times B$ are smooth lifts of $B_0$ and $B_0 \times B_0$ (the latter through $i_2$, which is a pullback since $i_2 = i \times i$), each presents a lift system $S$ and $S_2$. Let $c = \mathrm{ob}(L_0)$ for $S$, and let $c_1$, $c_2$ be the obstruction classes of $p_1^* L_0$ and $p_2^* L_0$ for $S_2$ (fact 1).

Since $R_0$ is local, the line bundle $e^* L_0$ on $\mathrm{Spec}\, R_0$ is trivial, so $1^* L_0 = 0$ in $\mathrm{Pic}(B_0 \times B_0)$, as $1$ factors through the unit section. With $m = p_1 \cdot p_2$, the hypothesis then gives
$$m^* L_0 \cong p_1^* L_0 + p_2^* L_0 + i_2^* P.$$
By fact 4 the obstruction class of $i_2^* P$ is $0$, and by fact 3 the class of the right side is $c_1 + c_2$. The three maps $m$, $p_1$, $p_2$ of $B_0 \times B_0$ to $B_0$ are the reductions of the maps $m$, $p_1$, $p_2$ of $B \times B$ to $B$, since $i$ respects the group laws and $i_2$ is compatible with $i$. So fact 5 gives
$$m^* c = c_1 + c_2, \qquad p_1^* c = c_1, \qquad p_2^* c = c_2.$$
By fact 6, $c = 0$, and by fact 2, $L_0$ lifts to a line bundle $L$ on $B$. $\square$

The theorem assumes neither that $R$ is noetherian nor that $B$ is commutative. It does not say that $\Lambda(L)$ is isomorphic to $P$.

We turn to the lifting of abelian schemes. We use the conditions of the section on the cohomology of the structure sheaf: the structure cohomology of dimension $g$ (Definition (Structure cohomology)), and for an abelian scheme $A$ over a ring $R$, the frame of global 1-forms, the constancy of global functions and the primitivity of global 1-forms of fact 8 there.

**Theorem 1.18.2 (Unobstructedness from structure).** Suppose that the following two conditions hold.

1. For every ring $R$ and every abelian scheme $A$ over $R$, smooth of relative dimension $g$, $A$ has the structure cohomology of dimension $g$.
2. For every ring $R$ and every abelian scheme $A$ over $R$, smooth of relative dimension $g$, the differentials of $A$ have a frame of global 1-forms, global functions stay constant for $A$, and every global 1-form on $A$ is primitive.

Let $\pi : R \to R_0$ be surjective with kernel $I$, $I^2 = 0$, and let $A_0$ be an abelian scheme over $R_0$. Then there are an abelian scheme $A$ over $R$ and a group pullback $i : A_0 \to A$.

Lean: `GlobalTheory.abelianUnobstructed_of_struct` (also `GlobalTheory.T.abelianScheme_unobstructed_of_cohomology_structure`, a second name).

The proof uses five steps, which we state as facts. In facts 8 to 11, $A$ is an abelian scheme over a ring $R_0$, smooth of relative dimension $g$, and $R_1$ is an $R_0$-algebra with a retraction $q : R_1 \to R_0$ whose kernel has square zero.

7. (Forms.) Condition 2 implies: for each such $A$, the global 1-forms trivialize the differentials ($\mathcal{O}(U) \otimes_{R_0} \Omega(A) \to \Omega^1(U)$ is an isomorphism for each affine open $U$), $\Omega(A)$ is projective, and each global 1-form $w$ satisfies $m^* w = p_1^* w + p_2^* w$.
8. (Primitive classes in degree 2.) If $H^1(A, \mathcal{O})$ is finite projective of rank $g$ and cup product gives $\bigwedge^2 H^1(A, \mathcal{O}) \cong H^2(A, \mathcal{O})$ for all such $A$, then each $c \in H^2(A, \mathcal{O})$ with $m^* c = p_1^* c + p_2^* c$ (in the sense of fact 6) is $0$.
9. (Axes in degree 1.) Under the same hypothesis, each $c \in H^1(A \times A, \mathcal{O})$ whose pullbacks along $(\mathrm{id}, 1)$ and $(1, \mathrm{id}) : A \to A \times A$ vanish is $0$.
10. (Extension of coefficients.) If the conclusion of fact 8 holds for all such $A$, then it holds with coefficients $R_1 \otimes \mathcal{O}$, which is fact 6. If the conclusion of fact 9 holds for all such $A$, then it holds with coefficients $R_1 \otimes \mathcal{O}$.
11. (Lifting in constant dimension.) If the conclusions of facts 7 and 10 hold, then each $A_0$ of constant relative dimension $g$ lifts, and if each $A_0$ of constant relative dimension lifts, then each $A_0$ lifts.

*Proof.* Condition 1 gives the first two parts of the structure cohomology for each $A$: $H^1(A, \mathcal{O})$ is finite projective of rank $g$, and cup product gives $\bigwedge^2 H^1(A, \mathcal{O}) \cong H^2(A, \mathcal{O})$. The base change parts are not used. These are the hypotheses of facts 8 and 9, so primitive classes in $H^2(A, \mathcal{O})$ vanish and classes in $H^1(A \times A, \mathcal{O})$ that vanish on both axes vanish. Fact 10 extends both statements to coefficients $R_1 \otimes \mathcal{O}$. Condition 2 gives the conclusion of fact 7. So fact 11 applies and $A_0$ lifts. $\square$

**Remark 1.18.3 (Formalization).** Facts 1 to 6 are `GlobalTheory.T.exists_lineBundleLiftObstruction`, `GlobalTheory.T.exists_lineBundleLift_of_obstruction_zero`, `GlobalTheory.T.lineBundleLiftObstruction_tensor_additive`, `GlobalTheory.T.lineBundle_obstruction_zero_of_restriction`, `GlobalTheory.T.lineBundleLiftObstruction_natural` and `GlobalTheory.T.primitive_degree_two_any_ring`; the class is `GlobalTheory.Obs.IsObL` and the algebra $R_1$ is `GlobalTheory.Obs.Aug`, which records the retraction $q$ and an additive map $k : R_1 \to R$ that identifies $\ker q$ with $I$. The sentence on how the obstruction class is built describes these names; their proofs were not read. In the proof, $1^* L_0 = 0$ comes from `GlobalTheory.LB.exists_isGen_of_isLocalRing` and the cube relation of $\Lambda$ from `GlobalTheory.CechPic.cls_cube_two`. The main theorem sits under `set_option maxHeartbeats 1000000` followed by a blank line ([ExistsLineBundleLiftSquareZeroOfMumfordBundle.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsLineBundleLiftSquareZeroOfMumfordBundle.lean#L25), lines 25 to 26). Facts 7 to 11 are `GlobalTheory.T.abelianSchemeGlobalFormsPrimitive_of_frames`, `GlobalTheory.T.additiveClassDegreeTwo_structureSheaf_vanish`, `GlobalTheory.T.axesO1_of_projective_rank_cup`, `GlobalTheory.T.primitive_degree_two_extension` with `GlobalTheory.T.axes_vanishing_degree_one_extension`, and `GlobalTheory.T.abelianScheme_unobstructed_of_forms_structure` with `GlobalTheory.T.abelianSchemeUnobstructed_of_constantDimension`; their conclusions are `GlobalTheory.Obs.FormSt`, `GlobalTheory.Obs.PrimitiveStructureSheafDegTwoVanish`, `GlobalTheory.Obs.AxesVanishingStructureSheafDegOne`, `GlobalTheory.Obs.PrimitiveExtendedDegTwoVanish`, `GlobalTheory.Obs.AxesVanishingExtendedDegOne` and `GlobalTheory.Obs.UnobDim`. The facts are cited by their statements; their proofs were not read. The proof drops the two base change parts of condition 1 ([AbelianSchemeUnobstructedOfCohomologyStructure.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/AbelianSchemeUnobstructedOfCohomologyStructure.lean#L32)). A second definition with the name `AxesVanishingStructureSheafDegOne`, in the namespace `Over`, is in [AxesVanishingStructureSheafDegOne.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/AxesVanishingStructureSheafDegOne.lean#L187). Both second names are `first` wrappers under `set_option maxHeartbeats 1000000`.
