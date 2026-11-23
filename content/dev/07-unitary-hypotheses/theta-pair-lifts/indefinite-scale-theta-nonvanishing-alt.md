---
id: indefinite-scale-theta-nonvanishing-alt
title: A second name for the placement of a realisation
kind: theorem
decl: GlobalTheory.T.indefinite_scale_theta_nonvanishing_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.PlacementOfRealisationStatement
covers: 482
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`placement_of_realisation_alt`](/entry/placement-of-realisation-alt/). Its statement is the same, and its proof applies that theorem. Its only user is [`row_rRows_stage0_alt`](/entry/row-r-rows-stage0-alt/), which applies it at each point summand of a compatible selection to get the property `VisibleExamplePointSummands`. The content is in the entry for `placement_of_realisation_alt`.

## Statement

Assume `DiscreteSeriesClassification`. Let $D$ be a datum, with the extra data `ex` built from it, an element `Rc` of `RecTAlt ex`, a row side family $P$, spectral ties $S$, a number field $K_s$ with an algebra map to the field $L$ of $D$, and an indefinite realisation $Q$ over these data. If $Q$ has the normalisation `IndefiniteRealisationNormalisation` and the map $\iota_E$ of $S$ is the identity (in the form of a heterogeneous equality), then `IndefiniteRealisationExtends Q` holds.

The data and the conclusion are explained in [`placement_of_realisation_alt`](/entry/placement-of-realisation-alt/).

## Proof

The proof is `exact placement_of_realisation_alt`, wrapped in the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)`.

## In the Lean code

The theorem is at [PlacementOfRealisationStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PlacementOfRealisationStatement.lean#L15). It calls `GlobalTheory.RowPlacementReal.placement_of_realisation_alt` ([PlacementOfRealisation.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PlacementOfRealisation.lean#L18)).

The name is misleading. No theta series, no scale and no nonvanishing statement appear in the hypotheses or in the conclusion. The file name matches the theorem that it renames.
