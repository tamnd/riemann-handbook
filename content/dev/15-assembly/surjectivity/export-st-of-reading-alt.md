---
id: export-st-of-reading-alt
title: The export statement from six inputs, second name
kind: theorem
decl: GlobalTheory.BigOn.exportSt_of_reading_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ExportStOfReading
covers: 668
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`exportSt_of_discrete_series_cover`](/entry/export-st-of-discrete-series-cover/), which is a second name for [`exportSt_of_hypotheses_alt`](/entry/export-st-of-hypotheses-alt/). The last one has the real content. The only user is [`exportSt_of_reciprocity_and_casselman_wallach`](/entry/export-st-of-reciprocity-and-casselman-wallach/), which gives the result to [the surjectivity statement](/entry/onto-x-of-hypotheses-alt-alt/) in branch 2 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/).

## Statement

Assume `CuspRapidDecay`, `GlobalArtinReciprocity`, `RayClassFieldSt`, `DiscreteSeriesCover`, `CasselmanWallach` and `SeriesRatS`. Then `ExportedStatement` holds. The inputs and the conclusion are described in [the entry with the content](/entry/export-st-of-hypotheses-alt/). We have not unfolded the inputs.

## Proof

The proof is the term `exportSt_of_discrete_series_cover`. The type is the same, so there is no other content.

## In the Lean code

The theorem is at [ExportStOfReading.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExportStOfReading.lean#L11). Unlike the other names in the chain, it is a term, not a `first | … | …` tactic.

- The same statement has four names in a row. Three of them only call the next one.
- "Reading" and the suffix `_alt` say nothing about the statement. A parallel `exportSt_of_reading` is in [ExportFromReciprocityTheorems.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExportFromReciprocityTheorems.lean#L14), which this file imports. It has the same six inputs, but its conclusion is `ExportSt`, and it calls `export_statement_of_discrete_series`.
