---
id: final-theorem-of-inputs-right
title: Restatement of the good tower and volume theorem from seventeen inputs
kind: theorem
decl: GlobalTheory.T.final_theorem_of_inputs_right
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.FinalTheoremOfInputsRightStatement
covers: 21074
status: drafted
drafted_by: writer@claude-opus-5-5
---
This theorem is a copy of [`goodTower_volume_of_reduced`](/entry/good-tower-volume-of-reduced/) under another name. It has the same seventeen hypotheses and the same conclusion, `GoodTowerExistsX` and `VolumeTheoremX`. Its only caller is [`good_tower_volume_theorem_bis`](/entry/good-tower-volume-theorem-bis/). The mathematics is in the entry for `goodTower_volume_of_reduced`.

## Statement

If the seventeen inputs listed in [the entry for `goodTower_volume_of_reduced`](/entry/good-tower-volume-of-reduced/) hold, then a good tower exists (`GoodTowerExistsX`) and the volume theorem holds (`VolumeTheoremX`). The [entry above](/entry/good-tower-volume-theorem-bis/) states both conclusions.

## Proof

The proof applies `goodTower_volume_of_reduced`. It is the tactic

```
first | exact @goodTower_volume_of_reduced | exact goodTower_volume_of_reduced | (intros; apply goodTower_volume_of_reduced <;> assumption)
```

with full names. The first branch succeeds, because the two statements are the same.

## In the Lean code

The theorem is in [FinalTheoremOfInputsRightStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/FinalTheoremOfInputsRightStatement.lean#L19). It is in the namespace `GlobalTheory.T`, where the code puts restatements of this kind. The file imports `Mathlib` twice.

The name is misleading. "Final theorem" here is the tower and volume pair, not the final theorem of the proof. "Right" pairs it with [`final_theorem_of_inputs_left`](/entry/final-theorem-of-inputs-left/), which builds the bundle `Top.Given` from the first twelve inputs.
