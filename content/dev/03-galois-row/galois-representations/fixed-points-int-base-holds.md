---
id: fixed-points-int-base-holds
title: Fixed points of Hecke correspondences on fibre powers, by complex uniformisation
kind: theorem
decl: UpperTheory.Gal.W2.fixedPoints_int_base_holds
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.SphericalCoordinates.FixedPointsIntBaseHolds
covers: 1644
status: drafted
drafted_by: writer@claude
---
This theorem counts the fixed points of a Hecke correspondence on a fibre power of the universal abelian scheme over a moduli model, and writes the sum of their Lefschetz terms as a weighted count of group elements. It is used twice in [tower_fixed_points_of_isogeny_data](/entry/tower-fixed-points-of-isogeny-data/): directly, and through `FixZ_holds`, which changes the level in the formula.

## Statement

Let $p$, $D$, $G$, $L$ be as in [kodaira_spencer_of_weight_one](/entry/kodaira-spencer-of-weight-one/), with $D.a = D.m = 1$, so that all embeddings $\tau_i$ of $F$ are one embedding $t_0$. Let $v$ be an infinite place where the hermitian form has one positive eigenvalue, and `gb` the standard base point over $\mathbb{C}$. Let $N \mid N'$ be levels and $h$ an element with $h K_{N'} h^{-1} \subseteq K_N$ (`LevOk`). Let $X$ and $X'$ be the fine moduli models at levels $N$ and $N'$, and $c_1$, $c_2$ two Hecke translations from $X'$ to $X$, by $1$ and by $h$ (`Leg`). Write $Z = A^k$ and $Z' = A'^k$ for the $k$-th fibre powers of the universal abelian schemes, $\mathrm{pw}_1 \colon Z' \to Z$ for the map of $c_1$, and $\mathrm{tw}_\alpha \colon Z' \to Z$ for the map of $c_2$ followed by $\alpha_s$ on the $s$-th factor. Assume that each $g$ with $hg \in K_N$ is regular, that each $\alpha_s$ is even, and that $\mathrm{pw}_1$ is étale.

**Theorem.** $Z$ is smooth of dimension $n - 1 + kg$ over $\mathbb{C}$, where $g$ is the relative dimension of the abelian scheme. The points $x \in Z'(\mathbb{C})$ with $\mathrm{pw}_1(x) = \mathrm{tw}_\alpha(x)$ form a finite set $F$, with tangent matrices $A_x$ and $\det(1 - A_x) \neq 0$. A set of group-side fixed points is finite, and their stabilizers at level $K_N$ are trivial. For all $t \in \mathbb{C}$,
$$\sum_{x \in F} \frac{\det(1 - tA_x)}{\det(1 - A_x)} = \mathrm{cxTotalM}\bigl(\mathrm{wtFix}(\alpha, t), K_{N'}, 1_{\{g : hg \in K_N\}}\bigr).$$

We have not unfolded the weight `wtFix` or the count `cxTotalM`.

## Proof

The proof is `fixedPoints_integral_base_of_uniformisation` applied to 16 facts, each proved in the same file.

1. `RhoSig` gives a complex representation $\rho$ of the order of $D$ with the right signature. `GUnif` gives complex uniformisations of $X$ and $X'$: both are smooth of dimension $n - 1$, and the universal abelian schemes are quotients of $\mathbb{C}^g$ by period lattices. Its proof starts from [model_nonempty](/entry/model-nonempty/).
2. `PowSm` gives the smoothness of the fibre powers, and `TanExists` gives the tangent matrices.
3. `UnifG` gives a bijection between $X'(\mathbb{C})$ and group-side data: a class of hermitian forms with a coordinate point.
4. A fixed point of $Z'$ lies over a base point $u$ with $c_1(u) = c_2(u)$ (`PwOver`). At such $u$, `FixFwd` gives a group element $y$ that fixes the coordinate point, and `StabTriv` shows that $y$ is unique.
5. `FixLoc` computes in the fibre over $u$: the fixed points there form a nonempty finite set, each with $\det(1 - A) \neq 0$, and their Lefschetz terms add up to the weight `wtFix` at $y$.
6. `FixFinite` gives finiteness. `EigSame` and `SumPts` add the weights over all base points and get `cxTotalM`.

## In the Lean code

The theorem is in [FixedPointsIntBaseHolds.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/SphericalCoordinates/FixedPointsIntBaseHolds.lean#L256). Its proof is in [FixedPointsIntegralBaseOfUniformisation.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/SphericalCoordinates/FixedPointsIntegralBaseOfUniformisation.lean#L70), and the statement `HeckeFixedPointCMCycleClass` in [HeckeFixedPointCMCycleClass.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/SphericalCoordinates/HeckeFixedPointCMCycleClass.lean#L108).

The name of the statement says "CM cycle class", but no cycle class appears in it: it is a fixed-point count. The hypotheses ask that each $\alpha_s$ be even, but not that it be nonzero. `FixK` adds $\alpha_s \neq 0$.
