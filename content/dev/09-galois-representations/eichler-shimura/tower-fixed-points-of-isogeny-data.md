---
id: tower-fixed-points-of-isogeny-data
title: The fixed-point count on the tower, from the count on the moduli models
kind: theorem
decl: UpperTheory.Gal.FixZ.tower_fixed_points_of_isogeny_data
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.IsogenyEtaleTranslation.TranslationFiniteEtaleOfIsogenyData
covers: 1788
status: drafted
drafted_by: writer@claude
---
This theorem proves `FixK`, the fixed-point count for Hecke correspondences on a tower of fibre powers, from five facts about isogenies and fibre powers. [FixK_holds](/entry/fix-k-holds/) applies it to those five facts, and the result goes to [ksHodge_of_geo](/entry/ks-hodge-of-geo/). The count itself is proved on the moduli models by [fixedPoints_int_base_holds](/entry/fixed-points-int-base-holds/). This theorem moves it to the tower.

## Statement

Let $p$, $D$, $G$, $L$ satisfy the scope condition `Sc` of [kodaira_spencer_of_weight_one](/entry/kodaira-spencer-of-weight-one/), and let $T$ be a tower `KS L gb k` over $\mathbb{C}$ at the standard base point. Write $Z_N$ for its level $N$, $K_N$ for the level group, and $\mathrm{tr}_h \colon Z_{N'} \to Z_N$ for the transition map of a Hecke element $h$ (when $h$ is admissible). For $\alpha \in \mathcal{O}_F^k$ let $[\alpha]$ act on $Z_N$ by $\alpha_s$ on the $s$-th factor of the fibre power.

$\mathrm{FixK}$: let $v$ be an infinite place where the hermitian form has one positive eigenvalue, $N \mid N'$ levels, $Z_N$ smooth of dimension $d$, $h$ with $\mathrm{tr}_1$ and $\mathrm{tr}_h$ admissible from $N'$ to $N$, and assume that each $g$ in the double coset $K_N h^{-1} K_N$ is regular. Let each $\alpha_s$ be nonzero and even, and put $\ell = [\alpha] \circ \mathrm{tr}_h$. Then:

1. a set of complex fixed points (`CxFin`) on the group side is finite;
2. $\ell$ is finite and étale;
3. the points $x \in Z_{N'}(\mathbb{C})$ with $\mathrm{tr}_1(x) = \ell(x)$ form a finite set $F$, with tangent matrices $A_x \in M_d(\mathbb{C})$ and $\det(1 - A_x) \neq 0$;
4. for all $y \in \mathbb{C}$,
$$\sum_{x \in F} \frac{\det(1 - yA_x)}{\det(1 - A_x)} = [K_N \cap h^{-1} K_N h : K_{N'} \cap h^{-1} K_N h] \cdot \mathrm{cxTotalM}\bigl(\mathrm{cW}(\alpha, y), K_N, 1_{K_N h^{-1} K_N}\bigr).$$

Here `cxTotalM` is a weighted count of group elements at $v$, and the weight `cW` depends on $\alpha$ and $y$. We have not unfolded them.

**Theorem.** `SysOf`, `RelComp`, `WitUniq`, `IsogFEt` and `PowSm` (see [FixK_holds](/entry/fix-k-holds/)) imply `FixK`.

## Proof

The proof is `bridge_of` with seven inputs, applied to `W2.fixedPoints_int_base_holds` and `W2.FixZ_holds`.

1. `translation_finite_etale_of_isogeny_data` proves that every $\mathrm{tr}_h$ is finite étale. It uses the five hypotheses, a factorization of $h$ by scalars and descent of étaleness and finiteness.
2. `alFEt_of`: $[\alpha]$ is finite étale when no $\alpha_s$ is $0$. With step 1 this gives clause 2.
3. `legOf_of`: through the isomorphism of $Z_N$ with the fibre power over the model `M N`, the maps $\mathrm{tr}_1$ and $\ell$ become the legs of a correspondence between models.
4. On the models, `FixZ_holds` gives the fixed points, tangent matrices and the sum formula. `fixedPoints_int_base_holds` gives only the finiteness and the trivial stabilizers. With `cxFinOf_of` these give clause 1.
5. `wtEq_of` rewrites the weight of the model formula as `cW`.
6. If $Z_N$ is not empty, `dimUniq_of` forces $d = n - 1 + kg$, and `tanIso_of` moves fixed points and tangent matrices to the tower. If $Z_N$ is empty, $F$ is empty and both sides are $0$.

## In the Lean code

The theorem is in [TranslationFiniteEtaleOfIsogenyData.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IsogenyEtaleTranslation/TranslationFiniteEtaleOfIsogenyData.lean#L24). `bridge_of` is in [PBridge.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IsogenyEtaleTranslation/PBridge.lean#L40). Its inputs are stated in [EtCancel.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IsogenyEtaleTranslation/EtCancel.lean#L45), and `FixK` in [HodgeTraceFromLefschetzAndGroupSide.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/LefschetzSigmaSums/HodgeTraceFromLefschetzAndGroupSide.lean#L125).

The name says "of isogeny data", and the five hypotheses are about isogenies, but the main input is the model-level count, which the proof uses as a fixed theorem and not as a hypothesis. In Lean the index is `(L.KN N'.1).relIndex (G3.lev (L.KN N.1) h)`. `bridge_of` uses `HeckeFixedPointCMCycleClass` only for its finiteness and stabilizer clauses, and the sum formula comes from `FixZ`.
