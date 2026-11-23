---
id: sum-size-bound-all-places
title: The sum size bounds at all places, restated
kind: theorem
decl: GlobalTheory.T.sum_size_bound_all_places
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.SumSizeFiniteAwayArchimedeanCombined
covers: 1151
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the sum size bounds at finite, away and archimedean places](/entry/sum-size-finite-away-archimedean-combined/). Its statement is the same and its proof applies that theorem. [The bound on the maximal slope at fitted points](/entry/fitted-function-at-zero-close-alt/) calls it in its second step. Below it are 1,151 declarations of the proof; all of them except this theorem are below `sum_size_finite_away_archimedean_combined`.

## Statement

Assume [`ThetaLocalInputs`](/step/theta-local-inputs-def/). Then `FinK`, `AwayK` and `InfK` hold. These are the denominator bound at the finite places, the condition that each place is away from the level, and the height bound at the infinite places. The [entry of the original theorem](/entry/sum-size-finite-away-archimedean-combined/) states them.

## Proof

The proof is `exact sum_size_finite_away_archimedean_combined`. The types are equal, so no step does any work.

## In the Lean code

The theorem is in [SumSizeFiniteAwayArchimedeanCombined.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/SumSizeFiniteAwayArchimedeanCombined.lean#L50), in the same file as the original at line 26. The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)`, and its first branch succeeds.

The declaration has `set_option maxHeartbeats 1000000`, five times the default limit, although its proof is one `exact`. The theorem adds nothing to the original; the content is in [the sum size bounds](/entry/sum-size-finite-away-archimedean-combined/).
