---
id: has4-of-has3-of-lv3-mv
title: From level three to level four, restated
kind: theorem
decl: GlobalTheory.T.has4_of_has3_of_lv3Mv
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.LevelThreeToFour
covers: 2285
status: drafted
drafted_by: writer@claude
---
This theorem is a copy of [`has4_of_has3_of_sExt_none`](/entry/has4-of-has3-of-s-ext-none/) under a second name. It says that, for all large contexts, each pinned column with a point of level three also has a point of level four. Its user is [`memberE_closing_alt_alt`](/entry/member-e-closing-alt-alt/), in branch 1 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). Below this theorem are 2,285 declarations, one more than below the copy.

## Statement

The statement is the statement of [`has4_of_has3_of_sExt_none`](/entry/has4-of-has3-of-s-ext-none/), word for word. Assume nine named statements (`DSInfChar`, `HarishChandraFinite`, `CuspRapidDecay`, `DiscreteSeriesUpqUnique`, `RowsFinDim`, `SiegelWeilUnitaryConvergent`, `DiscreteSeriesExist`, `FormalDegreeFormula₂`, `SiegelMassRatioCM`). Let $h_L$ be a proof of `RecTExists` and $p$ parameters over $h_L$ with S-extension `SExt.none` and with `LevelThreeCondition p.s`. Then `StepW (pinAnd (Has3 p.s)) (Has4 p.s)`. The entry of the copy says what these objects are.

## Proof

The proof is `exact has4_of_has3_of_sExt_none`, inside a `first | … | …` tactic that tries three forms of the same call. There is no other content.

## In the Lean code

The theorem is in [LevelThreeToFour.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LevelThreeToFour.lean#L29), ten lines below the copy. It sits in the namespace `GlobalTheory.T` and the copy in `GlobalTheory.Mem.SRe.UpS`.

[`memberE_closing_alt_alt`](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MemberEClosing.lean#L17) calls it twice: once at the parameters of a norm choice extension $N$, and once at those of a second extension $N_g$. Both times the S-extension is `SExt.none` and the geometry is `geoCl anyGeometry`.

The letters `lv3Mv` in the name suggest "level 3 move", which fits the hypothesis `LevelThreeCondition`. No object in the code has the name `Mv` in this sense. The hypothesis `SiegelMassRatioCM` is not used by the copy, so it is not used here either.
