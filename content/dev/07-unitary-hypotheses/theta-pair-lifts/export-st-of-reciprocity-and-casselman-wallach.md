---
id: export-st-of-reciprocity-and-casselman-wallach
title: The export statement from six inputs, first name
kind: theorem
decl: GlobalTheory.T.exportSt_of_reciprocity_and_casselman_wallach
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ExportStOfReadingStatement
covers: 669
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`exportSt_of_reading_alt`](/entry/export-st-of-reading-alt/), which is itself a second name. The real content is in [`exportSt_of_hypotheses_alt`](/entry/export-st-of-hypotheses-alt/). The only user is [the surjectivity statement](/entry/onto-x-of-hypotheses-alt-alt/), in branch 2 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). It uses the result for the export step.

## Statement

Assume `CuspRapidDecay`, `GlobalArtinReciprocity`, `RayClassFieldSt`, `DiscreteSeriesCover`, `CasselmanWallach` and `SeriesRatS`. Then `ExportedStatement` holds. The six inputs and `ExportedStatement` are described in [the entry with the content](/entry/export-st-of-hypotheses-alt/).

## Proof

The proof is `exact exportSt_of_reading_alt`, inside a `first | … | …` tactic that tries three forms of the same call. There is no other content.

## In the Lean code

The theorem is at [ExportStOfReadingStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExportStOfReadingStatement.lean#L11). The caller is at [OntoXOfPrints.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OntoXOfPrints.lean#L36). It applies this theorem and closes the six goals with `with_reducible assumption`.

- The proof sets `maxHeartbeats` to 1000000 for a one-line call.
- The name names two of the six inputs. All six are used further down, in the entry with the content. "Reading" in the file name says nothing about the statement.
