---
id: first-theorem-with-constants
title: The base-level projection bound from the two tool records
kind: theorem
decl: Formalism.MainNotions.G.first_theorem_with_constants
module: Formalism.SharpRestriction.GrowthBounds.PlaneCountTheoremWithConstants
covers: 313
status: drafted
drafted_by: writer@claude
---
This theorem gives the base-level projection bound for each datum $D$, from the two records `ExtremalProjectorTools` and `Loc8All`. It is a pass-through: it applies one field of `Loc8All` to [the hypotheses of the bound](/entry/first-theorem-admitted-closed/). It feeds [the same bound with uniform thresholds](/entry/first-theorem-uniform-thresholds/). Below it are 313 declarations.

## Statement

**Theorem.** Assume `ExtremalProjectorTools` and `Loc8All`. Then `projection_lemma_base_level D` holds for each $D$.

Here `projection_lemma_base_level D` is `ClosedP (Conclusion2 D)`: there is $T_0 > 0$ such that for each $C_0 \ge T_0$ there are $T_2 > 0$ and $C > 0$ with `Conclusion2` $(D, C_0, C_H, C)$ for all $C_H \ge T_2$. [`theorem_I_closed_form_holds`](/entry/theorem-i-closed-form-holds/) describes `Conclusion2`.

## Proof

The field `p13B` of `Loc8All` gives `SecondPartClosed D` for each $D$. This is the implication `AdmBE D → projection_lemma_base_level D`. The theorem applies it to `first_theorem_admitted_closed`, which proves `AdmBE D`. The proof is one line.

## In the Lean code

The theorem is in [PlaneCountTheoremWithConstants.lean](lean:Formalism/SharpRestriction/GrowthBounds/PlaneCountTheoremWithConstants.lean#L1269). `ClosedP`, `projection_lemma_base_level` and `SecondPartClosed` are in [ProjectionLemmaBaseLevel.lean](lean:Formalism/SharpRestriction/GrowthBounds/ProjectionLemmaBaseLevel.lean#L253).

The field `p13B` is an input of `Loc8All`, not a proof. `loc8All_of` (line 1316 of the same file) copies it from the field `p13B` of the record `Loc8`. So this theorem proves the bound only up to that field. Two other namespaces define a `SecondPartClosed` with other meanings: `CovariantDegrees` in [StatementOfDegreeAndBound.lean](lean:Formalism/SharpRestriction/GrowthBounds/StatementOfDegreeAndBound.lean#L512) and `SelectionLemmas` in [ValuationLowestDegreeRename.lean](lean:Formalism/SharpRestriction/GrowthBounds/ValuationLowestDegreeRename.lean#L274). The one used here is `flipOneThree.SecondPartClosed`.
