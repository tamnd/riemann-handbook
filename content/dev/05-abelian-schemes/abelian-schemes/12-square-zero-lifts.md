---
title: Square zero lifts
decls:
  - GlobalTheory.T.abelianSchemeSquareZeroLifts_of_hodgeDeRham
  - GlobalTheory.LiftSys.abelianSchemeLifts_of_hodgeDeRham
  - GlobalTheory.T.abelianSchemeSquareZeroLifts_of_deRhamCohomology
  - GlobalTheory.LiftSys.abelianSchemeLifts_of_abelianHodgeDeRham
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Square zero lifts

Let $A_0$ be an [[abelian scheme|JDDXZ89N33]] over $R_0 = R/I$ with $I^2 = 0$. This section classifies the [[smooth|EXKGG9X6J0]] lifts of $A_0$ to $R$ by submodules of a module that depends only on $A_0$ and the thickening (Theorem (Square zero lifts)). This module is the dual of the primitive crystalline $H^1$ of $A_0$. A lift $X$ gives the submodule cut out by the classes of 1-forms on $X$. The admissible submodules are the direct summands that reduce to the Hodge filtration of $A_0$. Every admissible submodule comes from a lift, and two lifts with the same submodule are isomorphic. This is the square zero case of the theorem of Grothendieck and Messing. The last section of this part extends it to nilpotent thickenings with divided powers.

Throughout, $R$ is a noetherian ring, $I \subset R$ an ideal with $I^2 = 0$, and $\pi : R \to R_0$ a surjective ring map with kernel $I$. The ideal $I$ has the divided powers $\gamma$ with $\gamma_1(x) = x$ and $\gamma_n = 0$ for $n \geq 2$. Let $A'$ be an abelian scheme over $R$, smooth of relative dimension $g$, and $i' : A_0 \to A'$ a morphism compatible with the group laws that makes $A_0$ the base change of $A'$ to $R_0$. The cohomology of a scheme is the Čech type cohomology on affine opens of the last section.

**Definition 1.12.1 (Crystal and Hodge filtration).**

1. A *smooth lift* of $A_0$ is a smooth scheme $X$ over $R$ with a morphism $i : A_0 \to X$ such that the square formed by $i$, the structure maps and $\mathrm{Spec}\, R_0 \to \mathrm{Spec}\, R$ is cartesian.
2. Let $H(A_0)$ be the first crystalline cohomology of $A_0$ relative to $(R, I, \gamma)$, and $H^{\mathrm{pr}}(A_0) \subset H(A_0)$ its primitive part: the classes $c$ with $(f g)^* c = f^* c + g^* c$ for all pairs of morphisms $f, g$ into $A_0$. Let $D(A_0)$ be the $R$-dual of $H^{\mathrm{pr}}(A_0)$.
3. For an abelian scheme $A$ over a ring, let $D_{\mathrm{dR}}(A)$ be the dual of the primitive part of the first de Rham cohomology of $A$, and $\mathrm{Fil}(A) \subset D_{\mathrm{dR}}(A)$ the annihilator of the primitive classes of 1-forms.
4. The lift $A'$ gives a map $\gamma_{A'} : D(A_0) \to D_{\mathrm{dR}}(A')$, the dual of the pullback of primitive classes.
5. For a smooth lift $(X, i)$, the *Hodge classes* of $X$ are the primitive classes in $H(A_0)$ that are images of classes of 1-forms on $X$. Let $\mathrm{Fil}(X) \subset D(A_0)$ be their annihilator.
6. A submodule $F \subset D_{\mathrm{dR}}(A')$ is *admissible* if it is a direct summand and if an element $y$ of $D_{\mathrm{dR}}(A_0)$ lies in $\mathrm{Fil}(A_0)$ if and only if $y$ is the reduction of some $x \in F$.

**Definition 1.12.2 (Inputs).** We say that the *crystalline comparison* holds if for each ring $R$ with an ideal $I$ and nilpotent divided powers on $I$, each scheme $X_0$ over $R/I$, and each smooth, separated and quasicompact lift $X$ of $X_0$ to $R$, there are isomorphisms from the crystalline $H^1$ and $H^2$ of $X_0$ to the de Rham $H^1$ and $H^2$ of $X$. They must respect cup products, agree with the de Rham comparison when $I = 0$, and commute with pullbacks. We say that the *Hodge and de Rham structure* holds if for every abelian scheme $A$ over a ring $R$, smooth of relative dimension $g$:

1. the first de Rham cohomology $H^1_{\mathrm{dR}}(A)$ is finite projective of rank $2g$, and $\bigwedge^2 H^1_{\mathrm{dR}}(A) \cong H^2_{\mathrm{dR}}(A)$ by cup product;
2. the global 1-forms and $H^1(A, \mathcal{O})$ are finite projective of rank $g$;
3. every global 1-form is closed, the map from global 1-forms to $H^1_{\mathrm{dR}}(A)$ is injective, and the map $H^1_{\mathrm{dR}}(A) \to H^1(A, \mathcal{O})$ is surjective;
4. $H^1_{\mathrm{dR}}(A)$, the global 1-forms and $H^1(A, \mathcal{O})$ commute with base change.

A *lift system* $S$ for $A_0$ is a functor $U \mapsto F_S(U)$ from affine opens of $A_0$ to smooth $R$-algebras, with natural surjections $F_S(U) \to \mathcal{O}(U)$ over $\pi$ whose kernels are $I F_S(U)$. A scheme $X$ over $R$ with $i : A_0 \to X$ *presents* $S$ if there are open immersions $\mathrm{Spec}\, F_S(U) \to X$, natural in $U$ and compatible with $i$. Each $F_S(U)$ is a thickening of $\mathcal{O}(U)$ with divided powers, so $H(A_0)$ maps to the first cohomology of the functor $F_S$. Let $K(S) \subset H(A_0)$ be the kernel of this map. The system $S$ is *full* if each cocycle of $F_S$ with values in $I F_S$ is the image of an element of $I H(A_0)$. Let $\rho : H(A_0) \to H^1_{\mathrm{dR}}(A_0)$ be the reduction map and $F^1 \subset H^1_{\mathrm{dR}}(A_0)$ the Hodge filtration.

We use the following facts. In facts 1 to 3 and 7 to 9, assume the crystalline comparison and the Hodge and de Rham structure. In facts 4 to 6, 10 and 11, $S$, $S'$ and $T$ are lift systems.

1. (Reduction.) $A_0$ is an abelian scheme over $R_0$, smooth of relative dimension $g$.
2. (Good reduction.) For $R_0$ noetherian, $A_0$ is *good*: global functions are constants; on each affine open the 1-forms are the base change of the projective module of global 1-forms; each global 1-form comes from a closed form, and a closed form has zero class if and only if its global form is zero.
3. (Crystal and de Rham.) $\rho$ is surjective, and its kernel is $I H(A_0)$.
4. (Systems from lifts.) Each smooth lift of $A_0$ presents some lift system.
5. (Lifts from systems.) Each $S$ is presented by some $X$ and $i$ with $i$ a surjective closed immersion, and then $(X, i)$ is a smooth lift.
6. (Summands.) Suppose $A_0$ is good and fact 3 holds. If $S'$ is full and $K(S')$ is a direct summand, then $K(S)$ is a direct summand and $K(S) + I H(A_0) = K(S') + I H(A_0)$. If $S$ is full, then $c \in K(S) + I H(A_0)$ if and only if $\rho(c) \in F^1$. Each summand $K$ with $K + I H(A_0) = K(S') + I H(A_0)$ is $K(T)$ for some $T$.
7. (The lift $A'$.) If $A'$ presents $S'$, then $S'$ is full and $K(S')$ is a direct summand.
8. (Hodge classes.) If a smooth lift $X$ presents $S$, the Hodge classes of $X$ are $K(S) \cap H^{\mathrm{pr}}(A_0)$.
9. (Admissible submodules.) Let $K, K'$ be direct summands of $H(A_0)$, and write $K^\perp$ for the annihilator of $K \cap H^{\mathrm{pr}}(A_0)$ in $D(A_0)$. If $K + I H(A_0) = \rho^{-1}(F^1)$, there is an admissible $F$ with $K^\perp = \gamma_{A'}^{-1}(F)$. Each admissible $F$ arises in this way from some such $K$. If $K^\perp = K'^\perp$, then $K = K'$.
10. (Morphisms.) If global functions on $A_0$ are constants, then fullness passes from $S$ to $T$. If $A_0$ is good, fact 3 holds, $S$ is full and $K(S) = K(T)$, then there are maps $F_S(U) \to F_T(U)$ of $R$-algebras, natural in $U$ and compatible with the surjections. If $X$ presents $T$, $Y$ presents $S$, and such maps exist, then there is $f : X \to Y$ over $R$ with $f \circ i = j$.
11. (Nilpotent thickenings.) Let $X$ be flat over $R$, $Y$ over $R$, and $f : X \to Y$ a morphism over $R$ whose base change to $R_0$ is an isomorphism. Then $f$ is an isomorphism.

Fact 8 needs only the crystalline comparison, with $A_0$ proper and geometrically connected. Facts 1 to 3, 7 and 9 take both inputs as hypotheses.

**Theorem 1.12.3 (Square zero lifts).** Assume the crystalline comparison and the Hodge and de Rham structure. Then:

1. for each smooth lift $(X, i)$ of $A_0$ there is an admissible $F \subset D_{\mathrm{dR}}(A')$ with $\mathrm{Fil}(X) = \gamma_{A'}^{-1}(F)$;
2. for each admissible $F$ there is a smooth lift $(X, i)$ with $\mathrm{Fil}(X) = \gamma_{A'}^{-1}(F)$;
3. if $(X, i)$ and $(Y, j)$ are smooth lifts with $\mathrm{Fil}(X) = \mathrm{Fil}(Y)$, there is an isomorphism $e : X \to Y$ over $R$ with $e \circ i = j$.

Lean: `GlobalTheory.LiftSys.abelianSchemeLifts_of_hodgeDeRham` (also `GlobalTheory.T.abelianSchemeSquareZeroLifts_of_hodgeDeRham`, a second name).

*Proof.* The ring $R_0$ is noetherian, as a quotient of $R$. By fact 1, $A_0$ is an abelian scheme of relative dimension $g$, so by fact 2 it is good. Fact 3 holds. By fact 4, $A'$ presents a lift system $S'$, and by fact 7, $S'$ is full and $K(S')$ is a direct summand. By fact 6, for each lift system $S$, $K(S)$ is a direct summand with $K(S) + I H(A_0) = K(S') + I H(A_0) = \rho^{-1}(F^1)$. If a smooth lift $X$ presents $S$, fact 8 gives $\mathrm{Fil}(X) = K(S)^\perp$.

Part 1. Let $(X, i)$ be a smooth lift. By fact 4 it presents some $S$. By the first paragraph and fact 9, there is an admissible $F$ with $K(S)^\perp = \gamma_{A'}^{-1}(F)$, so $\mathrm{Fil}(X) = \gamma_{A'}^{-1}(F)$.

Part 2. Let $F$ be admissible. By fact 9 there is a direct summand $K$ with $K + I H(A_0) = \rho^{-1}(F^1)$ and $K^\perp = \gamma_{A'}^{-1}(F)$. Then $K + I H(A_0) = K(S') + I H(A_0)$, so by fact 6, $K = K(S)$ for some $S$. By fact 5, $S$ is presented by a smooth lift $(X, i)$. Then $\mathrm{Fil}(X) = K(S)^\perp = \gamma_{A'}^{-1}(F)$.

Part 3. By fact 4, $X$ presents some $S$ and $Y$ presents some $T$. Then $K(T)^\perp = \mathrm{Fil}(Y) = \mathrm{Fil}(X) = K(S)^\perp$, and $K(S)$ and $K(T)$ are direct summands. So the last part of fact 9 gives $K(T) = K(S)$. Global functions on $A_0$ are constants, and $S'$ is full, so $T$ is full by fact 10. By fact 10 again, there are compatible maps $F_T(U) \to F_S(U)$, and so a morphism $f : X \to Y$ over $R$ with $f \circ i = j$. The base change of $f$ to $R_0$ is the identity of $A_0$. Since $X$ is smooth, it is flat over $R$, and $I$ is nilpotent. By fact 11, $f$ is an isomorphism. $\square$

The crystalline comparison is proved in this development ([Theorem 5.10.8 of Volume 4](/entry/crystalline-smooth-lift-of-relations/)). So only the Hodge and de Rham structure stays as a hypothesis.

**Corollary 1.12.4 (Square zero lifts from de Rham cohomology).** If the Hodge and de Rham structure holds, then the three conclusions of Theorem (Square zero lifts) hold.

Lean: `GlobalTheory.LiftSys.abelianSchemeLifts_of_abelianHodgeDeRham` (also `GlobalTheory.T.abelianSchemeSquareZeroLifts_of_deRhamCohomology`, a second name).

*Proof.* Apply Theorem (Square zero lifts), with the crystalline comparison from [Theorem 5.10.8 of Volume 4](/entry/crystalline-smooth-lift-of-relations/). $\square$

The Hodge and de Rham structure is also proved ([Theorem 1.15.1](/entry/ab-coh-abelian-hodge-de-rham/)), and the last section of this part uses both.

**Remark 1.12.5 (Formalization).** The three conclusions are `GlobalTheory.Published.AbelianSchemeLifts`, the two inputs are `GlobalTheory.Published.CrystallineSmoothLift` and `GlobalTheory.Published.AbelianHodgeDeRham`, lift systems are `GlobalTheory.LiftSys.Sys`, and admissibility is `GlobalTheory.Published.GrothendieckMessing.IsAdmissible`. The modules of the definition are `prim`, `Crys`, `HdR`, `Fil`, `crysToDR`, `primitiveCrystalHodgeLiftClasses` and `schemeFil`, with $\gamma$ the divided powers `divided₂`. Facts 1 to 11 are `GlobalTheory.T.abelianLift_reduction_standard_facts`, `GlobalTheory.T.goodForSquareZeroLiftClassification_of_abelianScheme`, `GlobalTheory.T.abelianScheme_crystal_reduces_to_deRham_sqZero`, `GlobalTheory.T.exists_squareZeroSmoothLiftSystem_presents`, `GlobalTheory.T.exists_scheme_presenting_squareZeroSmoothLiftSystem` with `GlobalTheory.T.isSmoothLift_of_squareZeroLiftSystemPresents`, then `GlobalTheory.T.squareZeroLiftSystem_filtration_direct_summand`, `GlobalTheory.T.mem_liftSystemFiltration_sup_iff_hodgeFiltration` and `GlobalTheory.T.exists_squareZeroLiftSystem_of_summand_reduction`, then `GlobalTheory.T.abelian_scheme_presented_by_system`, `GlobalTheory.T.primitiveCrystalHodgeLiftClasses_eq_comap_sys`, `GlobalTheory.T.admissible_deRhamHomology_summands_crystal`, then `GlobalTheory.T.squareZeroLiftSystem_filtration_inf_eq_and_full`, `GlobalTheory.T.exists_squareZeroLiftSystem_hom_of_filtration_eq` and `GlobalTheory.T.exists_morphism_liftSystemPresents_of_hom`, and `GlobalTheory.NilThickIso.isIso_of_flat_of_isIso_reduction`. They are cited by their statements; the sentences on why they hold are not read from proofs. Fact 1 has eight outputs, and the proof drops the first six: three statements that all classes are primitive, the bijectivity of the comparison map for $A'$, and the finiteness and projectivity of $H(A_0)$. The smooth lifts in the theorem are schemes with no group law; the group law of $A'$ enters only through $D_{\mathrm{dR}}(A')$ and $\gamma_{A'}$. The noetherian hypothesis is on $R$, and the proof derives it for $R_0$. The corollary takes the crystalline comparison from `GlobalTheory.SmoothLift.crystallineSmoothLift_of_relations`, so the theorem keeps as a hypothesis a statement that is already proved. The second names are closed by a `first` list under `set_option maxHeartbeats 1000000`, and both of their files import `Mathlib` twice.
