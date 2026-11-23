---
id: global-model-tower-fifth-condition
title: The height bounds I5 and I6 for a tower over a global model
kind: theorem
decl: RootFieldNumerics.global_model_tower_fifth_condition
module: Development.WeilBound.CoreStatements.FlagImmersions.GlobalModelTowerFifthCondition
covers: 825
status: drafted
drafted_by: writer@claude
---
This theorem proves the two height bounds `I5` and `I6` for a root tower with a good origin over a global model. It checks the hypotheses of [`tower_intersection_of_sandwich_split`](/entry/tower-intersection-of-sandwich-split/), a renaming of [`tower_good_of_sandwich_split`](/entry/tower-good-of-sandwich-split/), which has the content. Its one user is [`i5_and_i6_of_isGlobal_of_goodOrigin`](/entry/i5-and-i6-of-is-global-of-good-origin/), which has the same statement.

## Statement

Assume `Given`, the conjunction of the inputs from the literature. Let $E$ be a CM field, abelian over $\mathbb{Q}$, with host datum $H$ and a datum $D$ of signature $(p, q)$. Let $X_o$ be a family of moduli spaces over the levels of $H$, let $l$ be a level and $c$ a coefficient, and let $Y$ be an integral model of $X_o(l)$. Let $T$ be a root tower of length $p + q$ with a good origin $o$ over $Y$, and let $II$ be an intersection system.

**Theorem.** Suppose that $Y$ is global (`IsGlobal`), that $o$ has the extra data `Extra`, that $II$ is a full intersection system, and that $p, q \ge 1$. Then $T$ satisfies `I5` and `I6` for $II$.

The bounds `I5` and `I6` and the sandwich condition are stated in [the entry on `tower_good_of_sandwich_split`](/entry/tower-good-of-sandwich-split/).

## Proof

The proof takes three parts of `Given`: `ResKStatement`, `FarguesHodgeTate` and `GagaSections`. It then supplies the hypotheses of `tower_intersection_of_sandwich_split`.

1. `flat_zero_from_resolution_and_gaga` turns `ResKStatement` and `GagaSections` into the flat line generator `FlatLineGenerator`.
2. `splitComps_of_origin` gives the split components of $Y$ from the tower origin of $o$.
3. $II$ satisfies `IsIntersectionSystem`, the first part of `IsFullIntersectionSystem`.
4. For each $B$, each component $a$ and each prime $\ell \in S_B$, the field `omVB` of $o$ gives `HTFree` at $\ell$. Then `exists_sandwich_of_hodge_tate_free`, with `FarguesHodgeTate` and $p + q > 0$, gives $\kappa$ with `IsCp ℓ κ` and the sandwich condition.

## In the Lean code

The theorem is in [GlobalModelTowerFifthCondition.lean](lean:Development/WeilBound/CoreStatements/FlagImmersions/GlobalModelTowerFifthCondition.lean#L22). Several hypotheses are never used: `IsGlobal`, `o.Extra` and $q \ge 1$. Of `IsFullIntersectionSystem` only the first part is used, and $p \ge 1$ is used only to get $p + q > 0$. The class `IsAbelianGalois ℚ E` is not needed by the lemmas that the proof calls. The name speaks of a "fifth condition"; the conclusion is the pair `I5` and `I6`.
