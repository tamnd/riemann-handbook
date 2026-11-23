---
id: sb1l-alt-alt
title: A twisted copy turns a first level into a second level
kind: theorem
decl: GlobalTheory.HeightCounting.Up.SeriesStep.sb1l_alt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.SecondBoundOfPrimitive
covers: 357
status: drafted
drafted_by: writer@claude
---
This theorem proves the middle rung of the ladder of levels over a stage: from a first intermediate level datum it makes a second intermediate level datum, on a twisted copy of the stage. It reaches [the stage statements from the published inputs](/entry/all-stages-of-specializations-alt/) through the relay [`seriesExistList_of_inputs_serN`](/entry/series-exist-list-of-inputs-ser-n/). The work is done by [`series_copy_embedding_alt`](/entry/series-copy-embedding-alt/).

## Statement

Stages $x$ over a datum $P$ and the ladder of levels are as in [the stage statements](/entry/all-stages-of-specializations-alt/). An *intermediate level* datum over $x$ has base data $a$, a choice $P_q$ of a place of the CM field $E$ above each finite place of its maximal real subfield, a datum `InMt`, a rationality datum `InRat` and a cusp condition. A *first* level datum adds `SettingsFormsData`: a side datum $B_s$, two inclusions of sets of places, and a $\lambda$-datum with `IsLamTieFull`. A *second* level datum adds instead `SeriesData`, which extends `SettingsFormsData` by a series datum and the conditions `SerAt` and `TauTrue`. `ListSt c x` says that some grid datum for the level character of $x$ at $c$ has a $\lambda$-datum that is `IsLamTieFull` for the twist of $x$.

**Theorem.** Assume `PublishedInputsThirdLayerAlt` and `SerN`. Let $h_L$ be an element of `RecTExists` and $c_{\mathrm{Dep}} \in \mathbb R$. Then at every stage $x$ (along the steps that `StepW Start` admits), each first level datum over $x$ gives a stage $x'$ over the same $P$ with a second level datum, and `ListSt cDep x` implies `ListSt cDep x'`.

## Proof

1. `exists_matrix_input_identity_frame_of_inputs` gives, at every stage, an `InMt` datum $m$ whose frames `m.ad.PV i` are all identity frames (`IdFrame`).
2. Fix $x$ and a first level datum $l$. [`series_copy_embedding_of_cmDatum_alt`](/entry/series-copy-embedding-of-cm-datum-alt/) gives a new twist $N$ of type `TwNew (Dof x)` that keeps `IsLamTieFull`, and a transport statement.
3. `twisted_state_transport_heq_levels'` gives a stage $x'$ with $x'.o = $ `oTw x N` and an intermediate level datum $l'$ whose data are the twists of those of $l$.
4. Step 1 at $x'$ gives $m$. The transport statement of step 2, applied to $x'$, $l'$ and $m$, gives `SeriesData`.
5. The second level datum is $l'$ with its `InMt` field replaced by $m$, together with this `SeriesData`. `listSt_oTw` carries `ListSt` from $x$ to $x'$.

## In the Lean code

The theorem is at [SecondBoundOfPrimitive.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SecondBoundOfPrimitive.lean#L25). Besides `series_copy_embedding_of_cmDatum_alt`, it calls:

- `exists_matrix_input_identity_frame_of_inputs` in [MemMatrixGroupIdentityFrame.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MemMatrixGroupIdentityFrame.lean#L32). Its proof is `fun _ => …`: it ignores the published inputs and uses only `inMt_state` and the pin of `Start`.
- `twisted_state_transport_heq_levels'` in [RestageCopyRealStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RestageCopyRealStatement.lean#L15).
- `listSt_oTw` in [SecondBoundOfPrimitive.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/SecondBoundOfPrimitive.lean#L28).

The hypothesis `SerN` goes only to `series_copy_embedding_of_cmDatum_alt`, which does not use it. Of `PublishedInputsThirdLayerAlt`, only global Artin reciprocity (the field `what₂.art`) is used below this theorem. The name `sb1l` does not say what the theorem does.
