---
id: exists-full-level-model-ample-frames
title: A projective model with ample frames, from ten inputs (statement form)
kind: theorem
decl: GlobalTheory.T.exists_fullLevel_model_ample_frames
module: Development.AbelianVarietyTheory.Proofs.ModuliProofs.ExistsFullLevelModelAmpleFramesStatement
covers: 1048
status: drafted
drafted_by: writer@claude
---
This theorem is the statement form of [`Models.topAmpExists`](/entry/top-amp-exists/), with the same type. Its only caller is [`topAmpExists_of_semistableReduction`](/entry/top-amp-exists-of-semistable-reduction/), which supplies the inputs.

## Statement

**Theorem.** Ten inputs about abelian schemes imply `TopAmpExists`. The inputs are `HomExtSt`, `Out.Laws`, `Out.Laws2`, `SemistableReductionSt`, `ThmUSt`, `UTorsSt`, `ZHGeoSt`, a good reduction statement for theta objects, the theorem of the cube and `ThetaUnifAV`. The entry [`topAmpExists`](/entry/top-amp-exists/) says what each input states and gives `TopAmpExists` in full.

## Proof

The proof is the tactic `first | exact @GlobalTheory.Models.topAmpExists | ...`. The first branch succeeds. So this theorem is `Models.topAmpExists` under a second name.

## In the Lean code

The theorem is in [ExistsFullLevelModelAmpleFramesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/ExistsFullLevelModelAmpleFramesStatement.lean#L21). It is a renaming, with no content of its own. The real proof is in [`topAmpExists`](/entry/top-amp-exists/).
