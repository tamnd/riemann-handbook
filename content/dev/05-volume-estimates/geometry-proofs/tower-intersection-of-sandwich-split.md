---
id: tower-intersection-of-sandwich-split
title: The height bounds of a good tower, restated
kind: theorem
decl: GlobalTheory.T.tower_intersection_of_sandwich_split
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.TowerIntersectionOfSandwichSplitStatement
covers: 820
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`tower_good_of_sandwich_split`](/entry/tower-good-of-sandwich-split/), which proves the two height bounds `I5` and `I6` for a root tower with a good origin. That entry has the content. The one user of this theorem is [`global_model_tower_fifth_condition`](/entry/global-model-tower-fifth-condition/). That theorem supplies the flat line generator from `ResKStatement` and `GagaSections`, the split components from the origin, and the sandwich condition at each prime from `FarguesHodgeTate`.

## Statement

The statement is the same as that of [`tower_good_of_sandwich_split`](/entry/tower-good-of-sandwich-split/). Assume `Top.Given` and `Flat.FlatLineGenerator`. Let $T$ be a root tower with a good origin over a global integral model $Y$, and $II$ an intersection system. If $Y$ has split components and the sandwich condition holds at each prime of each Hodge component of the origin, then $T$ satisfies `I5` and `I6` for $II$: a lower bound for the heights of all points, and an upper bound on a Zariski dense set of points.

## Proof

The proof applies `tower_good_of_sandwich_split`.

## In the Lean code

The theorem is in [TowerIntersectionOfSandwichSplitStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/TowerIntersectionOfSandwichSplitStatement.lean#L11). The proof is

```
first | exact @GlobalTheory.CompanionTheory.Ar.TopGood.tower_good_of_sandwich_split | ...
```

The name speaks of an intersection; the conclusion is a pair of height bounds for points. The word "intersection" comes from the intersection system $II$ that computes the heights.
