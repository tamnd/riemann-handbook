---
id: tuples-have-local-models-at-constructed-point-over-true-columns
title: Local models at a constructed point, restated
kind: theorem
decl: GlobalTheory.T.tuplesHaveLocalModels_at_constructedPoint_over_trueColumns
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.TuplesHaveLocalModelsAtConstructedPointOverTrueCStatement
covers: 2860
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`modelsAt_bpt`](/entry/models-at-bpt/). It has the same statement, and its proof applies that theorem. Its user is [`servH_row`](/entry/serv-h-row/), which uses it to get local models at every point of a slot. The content is in `modelsAt_bpt`, which dominates 2,859 of the 2,860 declarations below this theorem.

## Statement

Assume `AdmAtEnt2` and `CurveEx`. Let $K$ be a context and $\beta$ a constructed point over $K$ (`BPt K`) whose core is in `positionOf HasPart`. Then `ModelsAt β.D β.O`: the object of $\beta$ has local models. The notions are explained in [`modelsAt_bpt`](/entry/models-at-bpt/), and the two hypotheses in [`servH_row`](/entry/serv-h-row/).

## Proof

Apply `modelsAt_bpt`. Nothing else is used.

## In the Lean code

The theorem is at [TuplesHaveLocalModelsAtConstructedPointOverTrueCStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/TuplesHaveLocalModelsAtConstructedPointOverTrueCStatement.lean#L7). Its proof is the tactic

```
first | exact @modelsAt_bpt | exact modelsAt_bpt | (intros; apply modelsAt_bpt <;> assumption)
```

(namespaces shortened), under `set_option maxHeartbeats 1000000`. The first branch closes the goal, so the theorem is a renaming. The file name is cut short ("OverTrueC"). The name speaks of "true columns", but the statement only asks that the core of $\beta$ comes from some column at which a `Part` exists.
