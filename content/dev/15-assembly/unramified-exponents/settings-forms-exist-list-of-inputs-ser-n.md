---
id: settings-forms-exist-list-of-inputs-ser-n
title: First level data with the list condition, the relay in the namespace T
kind: theorem
decl: GlobalTheory.T.settingsFormsExistList_of_inputs_serN
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ReductionSeriesB0
covers: 796
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It has the same statement as [first level data from the published inputs](/entry/settings-forms-exist-list-of-published-inputs/), in the same file, and it proves it by calling that theorem. The real content is in [the pointwise step](/entry/pointwise-alt-alt/). The user is [the stage statements from the published inputs](/entry/all-stages-of-specializations-alt/), which takes from it the first of the three steps of its item 4, in the form with the list condition.

## Statement

Assume the record `PublishedInputsThirdLayerAlt` ($P$), the record `SerN` ($S$) and an element $h_L$ of `RecTExists`. Then for each real $c$ the statement `SettingsFormsExistList' hL c` holds: at every stage $x$, each intermediate level datum over $x$ gives a stage $x'$ of the same datum $P$ that has a first level datum and satisfies the list condition `ListSt c`. [First level data from the published inputs](/entry/settings-forms-exist-list-of-published-inputs/) says what these words mean.

## Proof

The proof is

```
first | exact @GlobalTheory.HeightCounting.Up.PointwiseSettings.settings_forms_exist_list_of_published_inputs | ...
```

The two statements are the same text, so the first branch closes the goal.

## In the Lean code

The theorem is in [ReductionSeriesB0.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ReductionSeriesB0.lean#L98). It differs from the original only in the namespace (`GlobalTheory.T` here, `GlobalTheory.HeightCounting.Up.PointwiseSettings` for the original) and in the option `maxHeartbeats 1000000`. The words "settings forms" refer to the field `SettingsFormsData` of a first level datum, which we have not unfolded.
