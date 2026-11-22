---
id: cb-lefschetz-fixed-point-finite-etale-correspondence
title: The holomorphic Lefschetz formula for finite étale correspondences
kind: theorem
decl: UpperTheory.Cb.lefschetz_fixedPoint_finite_etale_correspondence
module: Development.AutomorphicArithmetic.Foundations.EtaleClopenDescent.LefschetzFixedPointFiniteEtaleCorrespondence
covers: 1812
status: drafted
drafted_by: writer@claude
---
This theorem proves the holomorphic Lefschetz formula $\mathrm{HLF}$ that the [geometric realization of the Galois row](/entry/geometric-realization-of-weight-one/) takes as its hypothesis. Its [restatement in the abelian variety files](/entry/t-lefschetz-fixed-point-finite-etale-correspondence/) is applied in the step [GeoOne holds](/step/geo-one-holds/). The proof reduces a general $Z$ to its connected components, where [the integral case](/entry/holomorphic-lefschetz-finite-etale-correspondence/) applies.

## Statement

Let $Z$ be a scheme over $\mathbb{C}$, smooth of relative dimension $d$, with a closed immersion into some $\mathbb{P}^N$. Let $c_1, c_2 \colon Y \to Z$ be finite étale maps over $\mathbb{C}$. Let $F$ be a finite set of $\mathbb{C}$-points of $Y$ such that $y \in F$ if and only if $c_1(y) = c_2(y)$. For each $y \in F$ let $A_y$ be a $d \times d$ complex matrix with $\det(1 - A_y) \neq 0$ that is the matrix of $c_2^*$ on cotangent vectors at $y$, in local coordinates $c_1^* t_1, \dots, c_1^* t_d$ (the condition `IsTan`). Fix $a \geq 0$. Then each $H^b(Z, \Omega^a)$ has finite dimension, and

$$\sum_{b=0}^{d} (-1)^b \operatorname{tr}\bigl(c_{1*} c_2^* \mid H^b(Z, \Omega^a)\bigr) = \sum_{y \in F} \frac{[t^a] \det(1 + t A_y)}{\det(1 - A_y)}.$$

Here $H^b(Z, \Omega^a)$ is `hodgeH s a b`, the cohomology `coh` of the sheafified $a$-forms. We have not unfolded `coh`. The map $c_2^*$ is `hodgePull` and $c_{1*}$ is the trace `hodgeTrace` along the finite étale map $c_1$. The number $[t^a]\det(1 + tA)$ is the sum of the principal $a \times a$ minors of $A$, that is $\operatorname{tr} \Lambda^a A$.

This is the holomorphic Lefschetz formula of Atiyah and Bott (Ann. of Math. 88, 1968), in the form for correspondences. See [[Atiyah-Bott fixed-point theorem|PKS8JE1PW1]] and [the Learn page](/learn/geometry/#complex-manifolds).

## Proof

1. $Z$ is compact (`compactSpace_of_projective_and_of_finite`). Since $Z$ is smooth, it is a finite disjoint union of integral open and closed pieces $V_j$ (`exists_integral_clopen_decomposition_of_smooth`).
2. Let $W_{jk} = c_1^{-1} V_j \cap c_2^{-1} V_k$. These sets are open and closed, and they cover $Y$ disjointly. The maps $c_1, c_2$ restrict to finite étale maps $W_{jk} \to V_j$ and $W_{jk} \to V_k$ (`exists_finite_etale_restrict_clopen`).
3. The cohomology of $Z$ is the product of the cohomology of the $V_j$ (`pull_bij`). In this product, $c_{1*} c_2^*$ is a block matrix whose $(j,k)$ block comes from $W_{jk}$ (`key_id`). Its trace is the sum of the diagonal blocks (`glue_trace`).
4. For each $j$, [`block_fixed`](/entry/block-fixed/) gives the formula for the diagonal block $W_{jj} \to V_j$, with the fixed points of $F$ that lie in $W_{jj}$.
5. A fixed point $y$ has $c_1(y) = c_2(y)$, so it lies in exactly one diagonal piece $W_{jj}$ (`fixed_part`). Summing over $j$ gives the formula (`final_sum`).

## In the Lean code

The theorem is in [LefschetzFixedPointFiniteEtaleCorrespondence.lean](lean:Development/AutomorphicArithmetic/Foundations/EtaleClopenDescent/LefschetzFixedPointFiniteEtaleCorrespondence.lean#L255). The helpers `pull_bij`, `key_id`, `glue_trace`, `fixed_part`, `final_sum` and `block_fixed` are private lemmas in the namespace `UpperTheory.Core` of the same file. The set $F$ and the matrices $A_y$ are inputs: the theorem does not prove that the fixed points are finite or compute $A_y$. `IsProjOver` asks for a closed immersion into projective space. The matrix in `IsTan` is the matrix on cotangent vectors, which is the transpose of the tangent map. This does not change $\det(1 - A)$ or the coefficients of $\det(1 + tA)$.
