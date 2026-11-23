---
id: adelic-data-extend-larger-fields-of-hypotheses
title: Adelic data extend to larger fields (second name)
kind: theorem
decl: GlobalTheory.T.adelicData_extend_largerFields_of_hypotheses
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.AdelicDataExtendLargerFieldsOfPublishedStatement
covers: 600
status: drafted
drafted_by: writer@claude
---
This theorem is a second name of [`datExt0_of_hypotheses`](/entry/dat-ext0-of-hypotheses/). It has the same statement and no proof of its own. That entry has the statement in words and the proof. It sits under the [membership theorem](/entry/member-bundles-large-unramified-exponents-alt/), which reaches it through `compatibleSystem_weightOne_saturated` (step 3 there).

## Statement

Assume seven propositions named after published results: `DiscreteSeriesCover`, `HarishChandraModules`, `CuspRapidDecay`, `CasselmanWallach`, `WeilRepresentationUnitaryPair`, `DiscreteSeriesExists` and `HarishChandraFinite`. Then `DatExt0` holds.

`DatExt0` says, in short: eventually in the context, a fine adelic datum over a base $B$ extends to a fine adelic datum over each enlargement $B'$ of $B$ with the same coefficient field, and the extension agrees with the old datum in every clause of `Ext`. The [entry of `datExt0_of_hypotheses`](/entry/dat-ext0-of-hypotheses/) gives the full form.

## Proof

The proof is the tactic `first | exact @datExt0_of_hypotheses | ...` (namespace shortened), which tries three ways to apply `datExt0_of_hypotheses`. The two statements are the same text.

## In the Lean code

The theorem is in [AdelicDataExtendLargerFieldsOfPublishedStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/AdelicDataExtendLargerFieldsOfPublishedStatement.lean#L21). Three theorems in the source use it:

- `weightOne_saturated_of_hypotheses` (second name `compatibleSystem_weightOne_saturated`) passes it to `exists_bare_form_of_saturation`;
- `w1Sat_of_hyps` passes it to `start_state_untwisted_empty_local`;
- `datExt_of_hypotheses` composes it with `datExt_of_datExt0`, which gives the same statement for enlargements in the sense `Enl`, because `Enl` implies `Enl0`.

This page does not unfold the seven hypotheses.
