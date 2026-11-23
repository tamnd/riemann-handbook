---
id: lifting-theorem-of-uniform-link
title: The local colength bound from 28 leaf lemmas and the first frame proposition
kind: theorem
decl: Formalism.MainNotions.N.Ln34.lifting_theorem_of_uniform_link
module: Formalism.SharpRestriction.LevelLetterCocycles.DvrLatticeRank.MainPf
covers: 870
status: drafted
drafted_by: writer@claude
---
This theorem is [the local colength bound for each $C \ge 160$](/entry/integrality-from-metric-of-large-constant/), with one of the 29 leaf lemmas kept as a hypothesis. The parent entry states the bound and explains the proof. The parent is `lifting_theorem_of_uniform_link u1link_pf`.

## Statement

**Theorem.** Assume `FirstFrameOfModels`. Then for each datum $D$ with local data $HW$, $F$, $C_m$ and reals $C_A, C_B, C_K, C$ with $C \ge 160$: if `FontExAll`, `DdRFull` and `DiRank` hold, then `IntegralityFromMetric D HW F Cm CA CB CK C` holds.

`FirstFrameOfModels` says: for each $D$, $HW$, $F$, $C_m$, if `adm1`, `DdRFull`, `DiRank`, `modelLR` and `modelFR` hold, then `u1R D HW` holds. `u1R` asks that `FirstPropositionFrame` holds at each good pair and each frame (`IsFrame`). We have not unfolded `FirstPropositionFrame`.

## Proof

The proof is one application of `local_theorem_of_leaf_lemmas`. It supplies 28 leaf lemmas by name, from `generator_bound_of_hypotheses` to `u3mixlink_pf`, and passes the hypothesis as the 23rd. In `local_theorem_of_leaf_lemmas`, the hypothesis is used only through `first_frame_of_models`, whose result goes into the universal link step `univR` and from there into `killR`, the third of the three facts in the parent entry.

## In the Lean code

The theorem is at [MainPf.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/DvrLatticeRank/MainPf.lean#L38). `FirstFrameOfModels` is at [SecondPropositionHypothesis.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/SecondPropositionHypothesis.lean#L11), `u1R` at [DownSlotProposition.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/DownSlotProposition.lean#L288), and its proof `u1link_pf` at [U1linkPf.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/DvrLatticeRank/U1linkPf.lean#L16).

- The name says "uniform link", but the hypothesis is the "U1 link" (`hU1L`, proved by `u1link_pf`). The name looks like a misreading of "U1".
- The theorem is a pass-through: it adds no step to `local_theorem_of_leaf_lemmas`.
