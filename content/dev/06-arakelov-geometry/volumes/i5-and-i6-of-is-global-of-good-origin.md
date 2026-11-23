---
id: i5-and-i6-of-is-global-of-good-origin
title: The height bounds of points on a good tower
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Top.i5_and_i6_of_isGlobal_of_goodOrigin
module: Development.AutomorphicSpectrum.Proofs.DivisibilityProofs.GoodTowerI5
covers: 826
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. Its statement is that of [the statement form](/entry/good-tower-i5/): under $\mathrm{Given}$, a root tower with a good origin with `Extra` over a global integral model satisfies the height bounds `I5` and `I6` for each full intersection system. Its proof is the term `global_model_tower_fifth_condition`, which has the same statement. That theorem, [`global_model_tower_fifth_condition`](/entry/global-model-tower-fifth-condition/), has the content.

## Statement

See [the statement form](/entry/good-tower-i5/), which defines `I5` and `I6`.

## Proof

The proof is `RootFieldNumerics.global_model_tower_fifth_condition`. That proof does three things. It takes `ResKStatement`, `FarguesHodgeTate` and `GagaSections`, the fifth, seventh and eighth parts of $\mathrm{Given}$. It gets a flat line generator from `ResKStatement` and `GagaSections` by `flat_zero_from_resolution_and_gaga`, and split components from the origin by `splitComps_of_origin`. For each $B$, each component and each prime $p$ of the set $S_B$ of the origin, it gets the sandwich condition from `FarguesHodgeTate` and the property `omVB` of the origin, by `exists_sandwich_of_hodge_tate_free`. Then [`tower_intersection_of_sandwich_split`](/entry/tower-intersection-of-sandwich-split/) gives `I5` and `I6`.

## In the Lean code

The theorem is in [GoodTowerI5.lean](lean:Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/GoodTowerI5.lean#L19). The proof of `global_model_tower_fifth_condition` is in [GlobalModelTowerFifthCondition.lean](lean:Development/WeilBound/CoreStatements/FlagImmersions/GlobalModelTowerFifthCondition.lean#L22). It names only $\mathrm{Given}$, the first part of `IsFullIntersectionSystem` and $1 \leq p$. It does not name the hypotheses `IsGlobal`, `Extra` and $1 \leq q$.
