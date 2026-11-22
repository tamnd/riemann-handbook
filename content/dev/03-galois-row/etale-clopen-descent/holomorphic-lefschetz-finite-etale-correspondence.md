---
id: holomorphic-lefschetz-finite-etale-correspondence
title: The holomorphic Lefschetz formula when the base is integral
kind: theorem
decl: UpperTheory.Cb.holomorphic_lefschetz_finiteEtale_correspondence
module: Development.AutomorphicArithmetic.Foundations.EtaleClopenDescent.HolomorphicLefschetzFiniteEtaleCorrespondence
covers: 1727
status: drafted
drafted_by: writer@claude
---
This theorem is the [Lefschetz formula for finite étale correspondences](/entry/cb-lefschetz-fixed-point-finite-etale-correspondence/) in the case where $Z$ is integral. The lemma [`block_fixed`](/entry/block-fixed/) applies it to each integral piece of a general $Z$. The proof cuts $Y$ into its integral pieces and applies [the case where $Y$ is integral too](/entry/holomorphic-lefschetz-finite-etale-integral/).

## Statement

The statement is that of the [Lefschetz formula](/entry/cb-lefschetz-fixed-point-finite-etale-correspondence/), with one more hypothesis: $Z$ is integral. Let $Z$ be integral, smooth of relative dimension $d$ and projective over $\mathbb{C}$. Let $c_1, c_2 \colon Y \to Z$ be finite étale over $\mathbb{C}$. Let $F$ be the finite set of $\mathbb{C}$-points $y$ of $Y$ with $c_1(y) = c_2(y)$, and let $A_y$ satisfy `IsTan` with $\det(1 - A_y) \neq 0$. Then for each $a$, each $H^b(Z, \Omega^a)$ has finite dimension, and

$$\sum_{b=0}^{d} (-1)^b \operatorname{tr}\bigl(c_{1*} c_2^* \mid H^b(Z, \Omega^a)\bigr) = \sum_{y \in F} \frac{[t^a] \det(1 + t A_y)}{\det(1 - A_y)}.$$

## Proof

1. $Z$ is compact, so $Y$ is compact, because $c_1$ is finite (`compactSpace_of_projective_and_of_finite`). $Y$ is smooth of relative dimension $d$, because $c_1$ is étale (`smoothOfRelativeDimension_comp_etale`).
2. $Y$ is a finite disjoint union of integral open pieces $W_m$ (`exists_integral_clopen_decomposition_of_smooth`). Each $W_m$ is also closed, because its complement is the union of the other pieces. So $W_m \to Y$ is a closed immersion, and $c_i|_{W_m}$ is finite étale.
3. The fixed points of $c_1|_{W_m}, c_2|_{W_m}$ are the points of $F$ in $W_m$. The condition `IsTan` passes to $W_m$ by `isTangentMatrix_iff_restrict_open`, applied with the open set $Z$ itself, and by the private lemma `isTan_of_iso`, which transports `IsTan` along the isomorphism from that open set to $Z$.
4. For each $m$, the [case where $Y$ is integral](/entry/holomorphic-lefschetz-finite-etale-integral/) gives the formula for $c_1|_{W_m}, c_2|_{W_m}$.
5. The trace along $c_1$ is the sum of the traces along the $c_1|_{W_m}$ (`hodgeTrace_eq_sum_clopen_decomposition`), and pullback commutes with composition (`hodgePull_comp`). So $c_{1*} c_2^* = \sum_m (c_1|_{W_m})_* (c_2|_{W_m})^*$.
6. Each $\mathbb{C}$-point of $Y$ lies in exactly one $W_m$ (`existsUnique_complexPoint_lift_clopen_cover`). So the sum over $F$ is the sum over $m$ of the sums over $F \cap W_m$.

Finite dimension comes from step 4 when there is a piece. When $Y$ is empty, it comes from `finiteDimensional_hodgeCohomology_of_smooth_proj`. The rest is bookkeeping.

## In the Lean code

The theorem is in [HolomorphicLefschetzFiniteEtaleCorrespondence.lean](lean:Development/AutomorphicArithmetic/Foundations/EtaleClopenDescent/HolomorphicLefschetzFiniteEtaleCorrespondence.lean#L43). Its name does not say that $Z$ is integral. The general case carries the name `lefschetz_fixedPoint_finite_etale_correspondence`, and the two names do not show which one is more general. In both, finite dimension is in the end the statement of `finiteDimensional_hodgeCohomology_of_smooth_proj`, whose proof we have not read.
