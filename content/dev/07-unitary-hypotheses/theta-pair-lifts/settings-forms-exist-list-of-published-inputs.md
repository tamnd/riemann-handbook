---
id: settings-forms-exist-list-of-published-inputs
title: First level data from the published inputs, with the list condition
kind: theorem
decl: GlobalTheory.HeightCounting.Up.PointwiseSettings.settings_forms_exist_list_of_published_inputs
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ReductionSeriesB0
covers: 795
status: drafted
drafted_by: writer@claude
---
This theorem lifts an intermediate level datum at a stage to a first level datum at a stage of the same datum, with the list condition. It joins a grid lemma to [the pointwise step](/entry/pointwise-alt-alt/), which has the real content. The result goes through [a relay](/entry/settings-forms-exist-list-of-inputs-ser-n/) to [the stage statements](/entry/all-stages-of-specializations-alt/), whose words for stages and levels we use.

## Statement

An *intermediate level* datum is a same Galois level datum with the fields `InMt`, `InRat` and `RowCusp`. A *first level* datum adds a field of type `SettingsFormsData`. For a real $c$, `ListSt c x` says: there is a grid datum $G$ for the level characters of $x$ such that $G$ has `FieldHas` and the twist datum of $x$ is fully tied to $\lambda(G)$ (`IsLamTieFull`).

**Theorem.** Assume `PublishedInputsThirdLayerAlt`, `SerN` and $h_L \in$ `RecTExists`. Let $c$ be real. At every stage $x$ of every datum, an intermediate level datum over $x$ gives a stage $x'$ of the same datum with a first level datum and with `ListSt c x'`.

## Proof

`exists_lam_grid_fieldHas_at_member` gives at every stage a grid datum $G$ with `FieldHas` that fits $x$. `StepW.trans` and `StepW.of_all` reduce the claim to one stage, where [the pointwise step](/entry/pointwise-alt-alt/) takes $G$ and gives $x'$.

## In the Lean code

The theorem is in [ReductionSeriesB0.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ReductionSeriesB0.lean#L87), the grid lemma in [ExistsGridAtMember.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsGridAtMember.lean#L29). We have not opened `GridLg.exists_large_grid_alt` or unfolded `SettingsFormsData`. Of `SerN`, only the field `ratio` is used, in the pointwise step.
