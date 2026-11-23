---
id: first-theorem-uniform-thresholds
title: The base-level projection bound, with thresholds that do not depend on the datum
kind: theorem
decl: Formalism.MainNotions.G.first_theorem_uniform_thresholds
module: Formalism.SharpRestriction.GrowthBounds.PlaneCountTheoremWithConstants
covers: 314
status: drafted
drafted_by: writer@claude
---
This theorem moves the quantifier over the datum $D$ to the inside of [the base-level projection bound](/entry/first-theorem-with-constants/). It feeds [the same bound with thresholds as functions](/entry/first-theorem-threshold-functions/), below the trunk step [EveryCharacter from theta integrals and local matching](/step/theta-local-matching/). The move is free, because the bound does not depend on $D$. Below it are 314 declarations.

## Statement

**Theorem.** Assume `ExtremalProjectorTools` and `Loc8All`. Then there is $T_0 > 0$ such that for each $C_0 \ge T_0$ there are $T_2 > 0$ and $C > 0$ with `flipOneThree.Conclusion2` $(D, C_0, C_H, C)$ for all $C_H \ge T_2$ and all data $D$.

`first_theorem_with_constants` gives the same nest for each $D$ separately, with $T_0$, $T_2$ and $C$ that could depend on $D$.

## Proof

There are two cases.

1. The type `D7` has an element $D_0$. Take $T_0$, $T_2$ and $C$ from `first_theorem_with_constants` at $D_0$. For another datum $D$, the proof uses the result at $D_0$. Lean accepts this because `Conclusion2` does not use its datum `_D`.
2. The type `D7` is empty. Then $T_0 = T_2 = C = 1$ work, because there is no $D$.

## In the Lean code

The theorem is in [PlaneCountTheoremWithConstants.lean](lean:Formalism/SharpRestriction/GrowthBounds/PlaneCountTheoremWithConstants.lean#L1271). `Conclusion2` is in [ProjectionLemmaBaseLevel.lean](lean:Formalism/SharpRestriction/GrowthBounds/ProjectionLemmaBaseLevel.lean#L78).

The step in case 1 (`fun CH hCH _ => hp CH hCH`) is correct only because `Conclusion2` ignores $D$. The real content is in [`first_theorem_admitted_closed`](/entry/first-theorem-admitted-closed/) and in the field `p13B` of `Loc8All`.
