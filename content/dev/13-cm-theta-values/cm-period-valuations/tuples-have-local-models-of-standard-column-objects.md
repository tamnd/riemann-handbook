---
id: tuples-have-local-models-of-standard-column-objects
title: Local models for objects with a column part, restated
kind: theorem
decl: GlobalTheory.T.tuplesHaveLocalModels_of_standardColumnObjects
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.TuplesHaveLocalModelsOfStandardColumnObjectsStatement
covers: 2851
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`modelsAt_of_part`](/entry/models-at-of-part/). It has the same statement, and its proof applies that theorem. Its user is [`modelsAt_bpt`](/entry/models-at-bpt/), which applies it at each column datum that the induction over constructed points reaches. The content is in `modelsAt_of_part`, which dominates 2,850 of the 2,851 declarations below this theorem.

## Statement

Assume the two statements `AdmAtEnt2` and `CurveEx`. Let $w$ be a column datum over a base $B$, a frame $f$ and twist data $T$, let $Z$ be a later stage of $w$, let $D$ be the datum of type `D7` that $w$ and $Z$ build, and let $O$ be an object over $D$. If $O$ has a part at $(w, Z)$, then `ModelsAt D O` holds: if the lattice instance of $O$ is tied and $2\,r_G \le k$, the local models of $O$ are good (`ModelsOK`). The hypotheses, the part and `ModelsAt` are described in [`modelsAt_of_part`](/entry/models-at-of-part/).

## Proof

Apply `modelsAt_of_part`. Nothing else is used.

## In the Lean code

The theorem is at [TuplesHaveLocalModelsOfStandardColumnObjectsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/TuplesHaveLocalModelsOfStandardColumnObjectsStatement.lean#L7). Its proof is the tactic

```
first | exact @modelsAt_of_part | exact modelsAt_of_part | (intros; apply modelsAt_of_part <;> assumption)
```

(namespaces shortened), under `set_option maxHeartbeats 1000000`. The first branch closes the goal, because the two statements are the same. So the theorem is a renaming.

The name says "standard column objects". The hypothesis is the structure `Part`, not the predicates `StdAt` or `StdTie` that are defined next to it in [HasPartAnd.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/HasPartAnd.lean#L16). The word "standard" in the name does not match a hypothesis.
