---
id: multiplicity-bound-of-local-components-alt
title: Moving a third level datum to an enlarged base
kind: theorem
decl: GlobalTheory.HeightCounting.Up.multiplicity_bound_of_local_components_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.MultiplicityBoundOfLocalComponents
covers: 401
status: drafted
drafted_by: writer@claude
---
This theorem proves `MoveToBase`: a third level datum at a stage over a base $B$ gives a third level datum at a stage over an enlarged base $B'$. It joins two steps of the level ladder. It goes through [a relay](/entry/move-to-base-of-inputs-ser-n/) to [the second nonvanishing statement](/entry/second-no-of-s-mt-s-rat-s-cusp-s-finl/), on the way to [the base lattice at the prime](/entry/exists-base-lattice-of-prime-alt/) in branch 1 of [the unitary hypotheses chapter](/proof/unitary-hypotheses/).

## Statement

The words for stages and levels are those of [the stage statements](/entry/all-stages-of-specializations-alt/). Write $D(x)$ for the datum `Dof x` of a stage $x$.

`StepW p q` says: eventually in the context $K$ (in the sense of `EvG`), for every base $B'$ admitted by `large₂` (not unfolded) with frame $f'$ and twist datum $T'$ that satisfy `KPx` and `Forced`, every column $w'$ with $p$ has $q$. `MoveToBase hL` is `StepW Start q`, where $q$ at $w'$ says the following. Let $B'$ enlarge $B$ (`Enl`: the same `Pre` datum, the same images of two subrings, and the image of $B$ inside that of $B'$). Let $w$ be a column over $B$ with `Start`, the same frame as $w'$, and the same components `px`, `sel`, `J`, $\delta$. Let $x$ be a stage of a datum $P$ over $w$ with a third level datum. Let $P'$ over $w'$ have the same core as $P$ (`Ext`), and let $x'$ be a stage of $P'$ with an intermediate level datum and `SameGal` $(D(x), D(x'))$ (the same Galois data and the same place data). Then there is a stage $x''$ of $P'$ with:

1. a third level datum;
2. `Carried` $(D(x), D(x''))$: the same export data (`SameExport`, not unfolded), and the embeddings of the twist data agree on elements with equal images;
3. `ListSt c x` implies `ListSt c x''` for every real $c$.

**Theorem.** `PublishedInputsThirdLayerAlt`, `SerN` and $h_L \in$ `RecTExists` imply `MoveToBase hL`.

## Proof

1. [A second level datum after a change of base](/entry/exists-level-b1-carried-of-level-i-same-gal/), through its relay `levelI_same_gal_transfer_to_levelB1_list`, gives the same statement with a second level datum at $x''$.
2. `exists_levelB2_carried_of_levelB1` says: at every stage, a second level datum and `Carried` $(D_0, D(x))$ give a stage of the same datum with a third level datum, `Carried` $(D_0, \cdot)$ and the list transfer.
3. `StepW.and` and `StepW.trans` combine the two. Step 1 gives $x_1$, and step 2 with $D_0 = D(x)$ gives $x_2$. The list implications compose.

The real content is in step 1.

## In the Lean code

The theorem is in [MultiplicityBoundOfLocalComponents.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MultiplicityBoundOfLocalComponents.lean#L17). `MoveToBase` is in [ExtensionWithOrigin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExtensionWithOrigin.lean#L40), `StepW` in [PositionOfIntro.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/PositionOfIntro.lean#L70), and step 2 in [PointsPreservedUnderLevelTransferOfCmDatum.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PointsPreservedUnderLevelTransferOfCmDatum.lean#L46). We have read the statement of step 2, not its proof.

The name speaks of a multiplicity bound and of local components. Neither appears in the statement.
