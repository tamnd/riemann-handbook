---
id: weil-unitary-entries-prime
title: The defect row at the parameters of an extension, in statement form
kind: theorem
decl: GlobalTheory.T.weil_unitary_entries'
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.PointEvaluationSideStatement
covers: 1187
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`linkedAt_prmR_df_of_cuspRapidDecay`](/entry/linked-at-prm-r-df-of-cusp-rapid-decay/). Its only user is [`open_orbit_of_unramified_exponents_alt`](/entry/open-orbit-of-unramified-exponents-alt/), which takes from it the defect row, the last of the twelve open parameter statements of branch 3 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). The real content is in [`linkedAt_df_of_parameters`](/entry/linked-at-df-of-parameters/).

## Statement

Assume `WeilRepresentationUnitaryPair`, `DiscreteSeriesExists`, `HarishChandraFinite` and `CuspRapidDecay`. Let $h_L$ be a proof of `RecTExists`, $N$ a norm choice extension for $h_L$, $S$ an `SExt` and $\Gamma$ a `GeoP`. Then `LinkedAt (parametersOfExtension N S Γ) RowDefectCondition` holds.

`RowDefectCondition` is the row form of the [definite side condition](/step/definite-side-condition-def/). The entry [`linkedAt_prmR_df_of_cuspRapidDecay`](/entry/linked-at-prm-r-df-of-cusp-rapid-decay/) unfolds it.

## Proof

The proof applies `linkedAt_prmR_df_of_cuspRapidDecay`. Nothing else happens.

## In the Lean code

The theorem is at [PointEvaluationSideStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PointEvaluationSideStatement.lean#L14). The proof is the tactic `first | exact @GlobalTheory.Fc.RL.linkedAt_prmR_df_of_cuspRapidDecay | ...`, so the theorem only passes its hypotheses along. The four named hypotheses are not used: `linkedAt_prmR_df_of_cuspRapidDecay` drops them. The name speaks of the Weil representation of a unitary pair, but the conclusion does not depend on that hypothesis. The caller supplies the four hypotheses from fields of `UnitaryGroupThirdPlaceHypotheses` (line 67 of `OpenOrbitOfUnramifiedExponents.lean`).
