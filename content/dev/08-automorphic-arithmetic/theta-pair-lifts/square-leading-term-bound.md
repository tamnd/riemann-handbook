---
id: square-leading-term-bound
title: The square top term estimates, restated
kind: theorem
decl: GlobalTheory.T.square_leading_term_bound
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.SquareTopTermJoinedEstimates
covers: 2313
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the square top term estimates](/entry/square-top-term-joined-estimates/). Its statement is the same, word for word, and its proof applies that theorem. [The bound on the maximal slope at fitted points](/entry/fitted-function-at-zero-close-alt/) calls it in its first step and uses all twelve conclusions. Below it are 2,313 declarations of the proof; all of them except this theorem are below `square_top_term_joined_estimates`.

## Statement

Assume `HoweDualityReal`, `ThetaLocalInputs`, `HeckeFunctionalEquationAbs`, `ToricDenominator`, `Transport`, `ZetaDenominators`, `Refl`, `ThetaIntegralsAgree` and `LocalMatching`. Then the twelve statements `DenSum`, `ThbSt`, `OneSqSt`, `BotSmall`, `BotNe`, `FieldDat`, `TorEx`, `DenEx`, `BotEx`, `LNe`, `TriEx` and `Tower` hold. The [entry of the original theorem](/entry/square-top-term-joined-estimates/) says what each of them means.

## Proof

The proof is `exact square_top_term_joined_estimates`. The types are equal, so no step does any work.

## In the Lean code

The theorem is in [SquareTopTermJoinedEstimates.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/SquareTopTermJoinedEstimates.lean#L40), in the same file as the original at line 13. The proof is a tactic `first | exact @… | exact … | (intros; apply … <;> assumption)`. It tries three ways to close the goal with the original theorem, and the first one succeeds.

The name speaks of a bound on a "leading term", but the statement is a conjunction of twelve facts, and most of them are not bounds (`LNe` and `BotNe` are nonvanishing statements, `TorEx`, `DenEx`, `BotEx` and `TriEx` are existence statements). The theorem adds nothing to the original; the content is in [the square top term estimates](/entry/square-top-term-joined-estimates/).
