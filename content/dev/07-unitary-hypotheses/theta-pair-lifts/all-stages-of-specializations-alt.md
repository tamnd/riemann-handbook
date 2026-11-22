---
id: all-stages-of-specializations-alt
title: The stage statements from the published inputs
kind: theorem
decl: GlobalTheory.HeightCounting.Up.all_stages_of_specializations_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.AllStagesAtMemberOfSpecializations
covers: 2431
status: drafted
drafted_by: writer@claude
---
This theorem joins thirteen statements about stages into one conjunction. Each comes from other lemmas. Through [a relay](/entry/all-stages-at-member-of-specializations-alt/), the result goes to [the base lattice at the prime](/entry/exists-base-lattice-of-prime-alt/), which uses it to build the condition `Has3` for the parameters of branch 1 in [the unitary hypotheses chapter](/proof/unitary-hypotheses/).

## Statement

A *stage* is a point $x$ of the type `St P`, where $P$ is a datum `Pre2 K w` over a context $K$ and a column $w$. A statement `AllSt p` says that $p(x)$ holds at every stage $x$ of every such datum, along the steps that `StepW Start` admits. We have not unfolded `StepW` or `St`.

Over a stage $x$ there is a ladder of data: a *same Galois level* datum; an *intermediate level* datum, which adds data of the types `InMt`, `InRat` and `RowCusp`; a *first*, *second* or *third* level datum, which adds settings forms data, series data or moduli points data; and a `StrictHenselianAcyclicLevel` datum, which adds a field of the type `HeightCountingCharacterData`.

**Theorem.** Assume `CasselmanWallach`, `HarishChandraModules`, `WeilRepresentationUnitaryPair`, `DiscreteSeriesExists`, `DiscreteSeriesUpqUnique`, the records `MultiplicityCoverHypotheses` ($H$), `PublishedInputsThirdLayerAlt` ($P$, fourteen named inputs) and `SerN` ($S$, six), an element $h_L$ of `RecTExists`, and `ArchimedeanComparison' hL` ($A$) and `PointStatement hL`. Then at every stage $x$:

1. if the local index set of $x$ is empty, there is a stage $x'$ with a same Galois level datum and with the same Galois data as $x$;
2. $x$ has an `InMt` datum, and an `InRat` datum when it has a same Galois level datum;
3. each same Galois level datum over $x$ satisfies `RowCusp`;
4. an intermediate level datum over $x$ gives a stage with a first level datum, a first level datum gives one with a second level datum, and a second gives one with a third;
5. each third level datum over $x$ extends to a `StrictHenselianAcyclicLevel` datum;
6. each such datum gives, for each `S` and `Γ`, a lattice point `Lv3` at the parameters built from `extensionWithLaw`, with the same set `Wt` and a kept norm choice.

Also, for each real $c$, the three steps of item 4 hold with the property `ListSt c` carried along, and item 6 holds for stages with `ListSt c`, at the parameters built from `extensionWithList hL c`.

## Proof

Each item comes from the lemmas below. We have read their statements, not their proofs.

- Item 2: `sMt_of_published_inputs'` from $P$, and `sRat_of_isotInternal_inputs`, which uses `isotInternal_at_states`.
- Item 3: `parSt_of_third_layer_sMt` gives `ParameterStatement`, then `sCusp_of_parSt_alt_alt`.
- Item 1: `stageASameGalois_of_inputs_phtCmp`, from $P$ and the field `pht` of $A$.
- Item 4 with lists: `settingsFormsExistList_of_inputs_serN`, `seriesExistList_of_inputs_serN` and `moduliPointsExistList_of_inputs_serN`, from $P$ and $S$. Item 4 without lists: the same at $c = 0$, then `steps_pin_alt`, which forgets `ListSt`.
- Item 5: `stage_c_nonempty_of_prints_third_layer`, from the field `cover` of $H$, Casselman-Wallach, Harish-Chandra modules, $P$ and $S$.
- Item 6 and its list form: `sEta_alt_alt_alt` gives `EtaStatement'` from `PointStatement`; `sXd_all_alt` gives `ThetaDataExists`; then `sFin_and_sFinl_of_archCmp_sEta_thetaData`.

The rest is bookkeeping.

## In the Lean code

The theorem is in [AllStagesAtMemberOfSpecializations.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AllStagesAtMemberOfSpecializations.lean#L32). The level structures are in [SameGaloisLevelExists.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SameGaloisLevelExists.lean#L42) and [SettingsFormsExistList.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SettingsFormsExistList.lean#L22).

- Item 4 without lists is a weak form of item 4 with lists: [StepsPin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/StepsPin.lean#L18) only drops the list part. The caller [ExistsBaseLatticeOfPrime.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsBaseLatticeOfPrime.lean#L64) discards item 4 without lists and item 6 without lists.
- Each hypothesis is used.
- The words "specializations" and "strict Henselian acyclic" in the names match no specialization map and no strictly Henselian ring in the statement. We have not unfolded `HeightCountingCharacterData`.
