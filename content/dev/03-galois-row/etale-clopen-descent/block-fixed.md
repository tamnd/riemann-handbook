---
id: block-fixed
title: The Lefschetz formula on one diagonal block
kind: theorem
decl: UpperTheory.Core.block_fixed
module: Development.AutomorphicArithmetic.Foundations.EtaleClopenDescent.LefschetzFixedPointFiniteEtaleCorrespondence
covers: 1750
status: drafted
drafted_by: writer@claude
---
This lemma is step 4 of the proof of the [Lefschetz formula for finite étale correspondences](/entry/cb-lefschetz-fixed-point-finite-etale-correspondence/). That proof cuts $Z$ into integral pieces $V_j$ and $Y$ into pieces $W_{jk}$. This lemma gives the formula on one piece $W \to V$. It restricts the data to $V$ and $W$ and applies [the integral case](/entry/holomorphic-lefschetz-finite-etale-correspondence/). The rest is bookkeeping.

## Statement

Let $Z$, $Y$, $c_1$, $c_2$, $d$, $F$ and $A_y$ be as in the [Lefschetz formula](/entry/cb-lefschetz-fixed-point-finite-etale-correspondence/): $Z$ smooth of relative dimension $d$ and projective over $\mathbb{C}$, $c_1, c_2 \colon Y \to Z$ over $\mathbb{C}$, $F$ the finite set of $\mathbb{C}$-points $y$ with $c_1(y) = c_2(y)$, and $A_y$ a matrix with the condition `IsTan` for $c_1, c_2$ and $\det(1 - A_y) \neq 0$. Let $V \subset Z$ be an open and closed subscheme that is integral. Let $W \subset Y$ be open, and let $c'_1, c'_2 \colon W \to V$ be finite étale maps that are the restrictions of $c_1$ and $c_2$. Fix $a$. Then each $H^b(V, \Omega^a)$ has finite dimension, and

$$\sum_{b=0}^{d} (-1)^b \operatorname{tr}\bigl(c'_{1*} c'^{*}_2 \mid H^b(V, \Omega^a)\bigr) = \sum_{y \in F \cap W} \frac{[t^a] \det(1 + t A_y)}{\det(1 - A_y)}.$$

The lemma does not ask that $W = c_1^{-1} V \cap c_2^{-1} V$. In the proof above it is used with that $W$.

## Proof

1. $V$ is smooth of relative dimension $d$, because an open immersion is smooth of relative dimension $0$ (`smoothOfRelativeDimension_comp`). $V$ is projective, because it is closed in $Z$ (`isProjOver_restrict_clopen`).
2. A $\mathbb{C}$-point $y$ of $W$ is fixed by $c'_1, c'_2$ if and only if its image in $Y$ is in $F$. This holds because the inclusion $V \to Z$ is a monomorphism.
3. The condition `IsTan` for $c_1, c_2$ at $y$ is equivalent to the condition for $c'_1, c'_2$ at $y$ (`isTangentMatrix_iff_restrict_open`).
4. The [integral case](/entry/holomorphic-lefschetz-finite-etale-correspondence/) now gives the formula for $W \to V$, summed over the fixed points of $W$. The map from $\mathbb{C}$-points of $W$ to $\mathbb{C}$-points of $Y$ is injective (`ptIn_injective`), so this sum is the sum over $F \cap W$ (`sum_pre`).

## In the Lean code

The lemma is private, in [LefschetzFixedPointFiniteEtaleCorrespondence.lean](lean:Development/AutomorphicArithmetic/Foundations/EtaleClopenDescent/LefschetzFixedPointFiniteEtaleCorrespondence.lean#L183). The sum is over the $y \in F$ in the range of `ptIn W`, the map of $\mathbb{C}$-points from $W$ to $Y$. The maps $c'_1, c'_2$ are given with the equations $\iota_V \circ c'_i = c_i \circ \iota_W$. Finiteness and étaleness of $c'_1$ are instance arguments, and those of $c'_2$ are explicit arguments.
