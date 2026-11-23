---
id: export-st-of-discrete-series-cover
title: The export statement from six inputs, third name
kind: theorem
decl: GlobalTheory.T.exportSt_of_discrete_series_cover
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ExportStOfPrintsStatement
covers: 667
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`exportSt_of_hypotheses_alt`](/entry/export-st-of-hypotheses-alt/), which has the real content. Its only user is [`exportSt_of_reading_alt`](/entry/export-st-of-reading-alt/), which is itself a second name. That chain ends in the export step of [the surjectivity statement](/entry/onto-x-of-hypotheses-alt-alt/), in branch 2 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). Below this theorem are 667 declarations, one more than below the copy.

## Statement

**Theorem.** Assume `CuspRapidDecay`, `GlobalArtinReciprocity`, `RayClassFieldSt`, `DiscreteSeriesCover`, `CasselmanWallach` and `SeriesRatS`. Then `ExportedStatement` holds.

The six inputs and `ExportedStatement` are described in [the copy](/entry/export-st-of-hypotheses-alt/). We have not unfolded the inputs.

## Proof

The proof applies `GlobalTheory.BigOn.Exp.exportSt_of_hypotheses_alt` to the six hypotheses in the same order. There is nothing else.

## In the Lean code

The theorem is in [ExportStOfPrintsStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExportStOfPrintsStatement.lean#L11). Its type is the type of the copy. The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)`.

The same statement has four names in a row. [`exportSt_of_reciprocity_and_casselman_wallach`](/entry/export-st-of-reciprocity-and-casselman-wallach/) in [ExportStOfReadingStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExportStOfReadingStatement.lean#L11) calls `exportSt_of_reading_alt` in [ExportStOfReading.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExportStOfReading.lean#L11), which calls this theorem, which calls the copy. The name "discrete series cover" names one of the six inputs, and "prints" in the file name says nothing about the statement.
