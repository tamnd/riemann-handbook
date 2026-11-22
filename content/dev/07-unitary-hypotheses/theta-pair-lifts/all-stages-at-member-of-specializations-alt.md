---
id: all-stages-at-member-of-specializations-alt
title: The stage statements, the relay in the namespace T
kind: theorem
decl: GlobalTheory.T.all_stages_at_member_of_specializations_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.AllStagesAtMemberOfSpecializations
covers: 2436
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It has the same statement as [the stage statements from the published inputs](/entry/all-stages-of-specializations-alt/), in the same file, and it proves it by calling that theorem. The real content is in that entry. Its only user is [the base lattice at the prime](/entry/exists-base-lattice-of-prime-alt/), which takes the stage statements from it and builds the condition `Has3` for the parameters of [the unitary hypotheses chapter](/proof/unitary-hypotheses/).

## Statement

Assume eleven inputs: five named published results (`CasselmanWallach`, `HarishChandraModules`, `WeilRepresentationUnitaryPair`, `DiscreteSeriesExists`, `DiscreteSeriesUpqUnique`), the records `MultiplicityCoverHypotheses`, `PublishedInputsThirdLayerAlt` and `SerN`, an element $h_L$ of `RecTExists`, and the statements `ArchimedeanComparison' hL` and `PointStatement hL`. Then thirteen stage statements hold. [The stage statements from the published inputs](/entry/all-stages-of-specializations-alt/) lists and explains each of them.

## Proof

The proof is

```
first | exact @GlobalTheory.HeightCounting.Up.all_stages_of_specializations_alt | ...
```

The two statements are the same text, so the first branch closes the goal. The other branches of `first` are fallbacks that are not needed.

## In the Lean code

The theorem is in [AllStagesAtMemberOfSpecializations.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AllStagesAtMemberOfSpecializations.lean#L52). The two theorems differ only in the namespace (`GlobalTheory.T` here, `GlobalTheory.HeightCounting.Up` for the original) and in the option `maxHeartbeats 1000000` on this one. The words "at member" and "specializations" in the name do not match any object in the statement.
