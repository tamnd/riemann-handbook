---
id: crystalline-smooth-lift-of-relations
title: Crystalline cohomology in degrees 1 and 2 from a smooth lift
kind: theorem
decl: GlobalTheory.SmoothLift.crystallineSmoothLift_of_relations
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.CrystallineSmoothLiftOfRelations
covers: 634
status: drafted
drafted_by: writer@claude
---
This theorem compares crystalline cohomology with de Rham cohomology of a smooth lift, in degrees 1 and 2. It proves the statement `CrystallineSmoothLift`, with cup products, the comparison map in degree 1 and functoriality. Its 14 direct users are in files on abelian schemes: the de Rham cohomology of an abelian scheme and its Hodge sequence, lifts of abelian schemes over square-zero thickenings, the dual crystal, and the Frobenius on crystalline cohomology. Their common dominator is the step [EveryCharacter](/step/every-character/).

## Statement

A *datum* $D$ (`SmoothLift.Data`) is: a ring $R$, an ideal $I$ with nilpotent divided powers $\kappa$, a smooth, separated, quasi-compact scheme $X$ over $R$, and a closed immersion $i \colon X_0 \to X$ that identifies $X_0$ with $X \times_R R/I$.

The two sides are as follows.

- $H^q_{\mathrm{cris}}(D)$ (`CatCoh.H1 (O D.κ D.t)` and `H2`). Let $\mathrm{Thick}(D)$ be the category of PD thickenings of $X_0$: an $R$-algebra $B$ with an ideal $J$ that has nilpotent divided powers $\delta$ compatible with $\kappa$, and a map $\operatorname{Spec}(B/J) \to X_0$ over $R$. The functor $O$ sends a thickening to $B$. $H^q_{\mathrm{cris}}(D)$ is the cohomology of the category $\mathrm{Thick}(D)$ with coefficients in $O$: cochains on chains $T_0 \to \dots \to T_q$ of morphisms, with the usual differential.
- $H^q_{\mathrm{dR}}(X)$ (`HH1 D.s` and `HH2`). This is the cohomology of the total complex of the double complex of cochains on chains of affine opens of $X$, with values in the algebraic de Rham complex $\Omega^\bullet_{\mathcal{O}(U)/R}$.

**Theorem** (`CrystallineSmoothLift`). There are $R$-linear isomorphisms $e_1(D) \colon H^1_{\mathrm{cris}}(D) \to H^1_{\mathrm{dR}}(X)$ and $e_2(D) \colon H^2_{\mathrm{cris}}(D) \to H^2_{\mathrm{dR}}(X)$ for each $D$ such that:

1. $e_2(a \cup b) = e_1(a) \cup e_1(b)$;
2. let $c$ be a class in $H^1$ of the thickenings of $X$ over $R$ with the zero ideal; then $e_1$ of the pullback of $c$ along $i$ is the image of $c$ under the comparison map `cmp1`;
3. $e_1$ and $e_2$ commute with pullback along each morphism of data $(\sigma, \varphi, \varphi_0)$ that is compatible with the divided powers.

This is a form, in degrees 1 and 2, of the comparison theorem of crystalline and de Rham cohomology (P. Berthelot, *Cohomologie cristalline des schémas de caractéristique p > 0*, Lecture Notes in Math. 407, 1974, Chapter V; P. Berthelot and A. Ogus, *Notes on Crystalline Cohomology*, 1978, §7). The Lean models of both sides are cohomologies of categories, not sheaf cohomology. We have not checked that they agree with the standard groups.

## Proof

1. Choose a lift $\Lambda$ (`Lift D`) by `nonempty_smoothLiftAffineThickenings`. It makes each affine open $U$ of $X$ a PD thickening of $U \cap X_0$, with $J = I \cdot \mathcal{O}(U)$.
2. For each $\Lambda$, the relations $\mathrm{Rel}_1, \mathrm{Rel}_2$ between $H^q_{\mathrm{cris}}(D)$ and $H^q_{\mathrm{dR}}(X)$ are total, surjective and detect zero: [`crystallineCechDeRham_relations_total_detect_zero`](/entry/crystalline-cech-de-rham-relations-total-detect-zero/).
3. They respect sums and scalars (`smoothLift_comparisonRelations_add_smul`).
4. The lemma `exists_linearEquiv_of_rel` of the same file: a relation with these five properties is the graph of a linear isomorphism. This gives $e_1, e_2$.
5. Clause 1 is `comparison_relations_respect_cup`, clause 2 is `smoothLift_degreeOne_comparisonRelation`, and clause 3 is `crystallineDeRhamRelation_natural_smoothLift_morphism`.

## In the Lean code

The theorem is in [CrystallineSmoothLiftOfRelations.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CrystallineSmoothLiftOfRelations.lean#L52). The statement is in [BijectiveCechDeRhamComparisonDegreeOne.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/BijectiveCechDeRhamComparisonDegreeOne.lean#L130), and the relations `Lift.Rel1`, `Lift.Rel2` are in [DivPowerCompatTwoFormDerivativeCompOneForm.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/DivPowerCompatTwoFormDerivativeCompOneForm.lean#L437).

The maps of a thickening $\operatorname{Spec}(B/J) \to X_0$ need not be open immersions, so $\mathrm{Thick}(D)$ is a large category, with no topology. The lift $\Lambda$ is chosen with `Classical.choice`, so $e_1$ and $e_2$ may depend on it. The statement only claims that they exist.
