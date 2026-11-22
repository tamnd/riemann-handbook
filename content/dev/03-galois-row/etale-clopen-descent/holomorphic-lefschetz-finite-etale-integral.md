---
id: holomorphic-lefschetz-finite-etale-integral
title: The holomorphic Lefschetz formula for integral varieties, by function fields
kind: theorem
decl: UpperTheory.Cb.holomorphic_lefschetz_finiteEtale_integral
module: Development.AutomorphicArithmetic.Foundations.EtaleClopenDescent.HolomorphicLefschetzFiniteEtaleIntegral
covers: 1717
status: drafted
drafted_by: writer@claude
---
This theorem is the Lefschetz formula for finite étale correspondences when both $Z$ and $Y$ are integral. The [case of an integral $Z$](/entry/holomorphic-lefschetz-finite-etale-correspondence/) applies it to each integral piece of $Y$. The proof moves the problem to the function fields of $Z$ and $Y$ and to Čech cohomology on the charts of a finite map $Z \to \mathbb{P}^d$. Then it applies [the Čech form of the formula](/entry/t-exists-chart-lift-of-finite-cover/).

## Statement

The statement is that of the [Lefschetz formula](/entry/cb-lefschetz-fixed-point-finite-etale-correspondence/), with $Z$ and $Y$ integral. Let $Z$ be integral, smooth of relative dimension $d$ and projective over $\mathbb{C}$. Let $Y$ be integral, and let $c_1, c_2 \colon Y \to Z$ be finite étale over $\mathbb{C}$. Let $F$ be the finite set of $\mathbb{C}$-points $y$ with $c_1(y) = c_2(y)$, and let $A_y$ satisfy `IsTan` with $\det(1 - A_y) \neq 0$. Then for each $a$, each $H^b(Z, \Omega^a)$ has finite dimension, and

$$\sum_{b=0}^{d} (-1)^b \operatorname{tr}\bigl(c_{1*} c_2^* \mid H^b(Z, \Omega^a)\bigr) = \sum_{y \in F} \frac{[t^a] \det(1 + t A_y)}{\det(1 - A_y)}.$$

## Proof

1. $Y$ is smooth of relative dimension $d$. Finite dimension is `finiteDimensional_hodgeCohomology_of_smooth_proj`.
2. Let $K$ and $K'$ be the function fields of $Z$ and $Y$. The maps $c_1$ and $c_2$ give $\mathbb{C}$-algebra maps $K \to K'$ (`exists_ffMap`). The first makes $K'$ an extension of $K$, and the second is $j_2$.
3. `exists_finiteCover_projSpace_reduced_fibre_origin`, applied to the images in $Z$ of the fixed points, gives a field $F_0$ with a map to $K$, elements $x_0, \dots, x_d$ of $F_0$ and affine charts $U_i$ of $Z$. The function field $K$ is a finite cover of $\mathbb{P}^d$ on these charts, the fibre over the origin of chart $0$ is reduced, and the images of the fixed points lie in $U_0$ over the origin. `isFinCover_pull` gives the same cover data for $K'$ on the charts $c_1^{-1} U_i$.
4. $\mathbb{C}$-points of $c_1^{-1} U_i$ are the $\mathbb{C}$-algebra maps from the chart ring to $\mathbb{C}$ (`complexPoints_bijective_algHom_affineOpen`). A point is fixed by $c_1, c_2$ if and only if the algebra map is fixed in the sense of the Čech form (`etaleCorrespondence_complexPoints_statement`). This gives a bijection from $F$ to the fixed points in the fibre over the origin.
5. At each fixed point, `exists_regular_parameters_of_reduced_quotient` writes $c\, j_2(t_m) = \sum_l g_l t_l$ with $c(y) \neq 0$. This defines a matrix $A'_y$ with $A'_{y,ml} = g_l(y)/c(y)$. `etaleCorrespondence_local_parameters_statement` gives an invertible $P$ with $A'_y = P A_y P^{-1}$. Conjugation does not change $\det(1 - A)$ or the coefficients of $\det(1 + tA)$ (the private lemma `conj_inv`).
6. `exists_hodge_cohomology_equiv_cech_differentials` gives an isomorphism $E$ from $H^p(Z, \Omega^a)$ to the Čech group $H^p$ of the $a$-forms on the charts, compatible with pullback and trace. Let $u_p = E \circ c_{1*} c_2^* \circ E^{-1}$. It has the lift property of the Čech form (`etaleCorrespondence_family_statement`), and its trace is that of $c_{1*} c_2^*$ (`LinearMap.trace_conj'`).
7. The other hypotheses of the [Čech form](/entry/t-exists-chart-lift-of-finite-cover/) come from `etaleCorrespondence_sections_statement`, `etaleCorrespondence_fieldExtension_statement`, `etaleCorrespondence_differentials_statement` and `exists_regular_parameters_of_reduced_quotient`. The Čech form then gives the formula with $A'_y$, and step 5 replaces $A'_y$ by $A_y$.

## In the Lean code

The theorem is in [HolomorphicLefschetzFiniteEtaleIntegral.lean](lean:Development/AutomorphicArithmetic/Foundations/EtaleClopenDescent/HolomorphicLefschetzFiniteEtaleIntegral.lean#L74). The lemmas named `etaleCorrespondence_*_statement` and the two `GlobalTheory.T.exists_*` lemmas of steps 3 and 6 carry the geometry. We have read their statements as they are used here, not their proofs. The proof also proves the regular parameter hypothesis and the finite dimension hypothesis of the Čech form. The Čech form does not use them (see [`field0`](/entry/field0/)).
