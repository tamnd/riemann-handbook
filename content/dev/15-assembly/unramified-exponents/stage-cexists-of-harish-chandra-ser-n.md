---
id: stage-cexists-of-harish-chandra-ser-n
title: Character data with a given twist index at third level stages
kind: theorem
decl: GlobalTheory.LevCmp.stageCExists_of_harishChandra_serN
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.LevelComparisonChoicesExistAtAllPlaces
covers: 565
status: drafted
drafted_by: writer@claude
---
This theorem proves `ThirdStageExists`: at a stage with a third level datum, each admissible choice of twist indices comes from a character datum. It reaches [membership and bundles at the origin parameters](/entry/exists-base-lattice-of-prime-alt/) through the second name [`stageCExists_of_casselmanWallach`](/entry/stage-cexists-of-casselman-wallach/).

## Statement

**Theorem.** Assume `DiscreteSeriesCover`, `CasselmanWallach`, `HarishChandraModules`, `PublishedInputsThirdLayerAlt` and `SerN`, and let $h_L$ prove `RecTExists`. Then `ThirdStageExists` $h_L$.

So, eventually at large bases, for each stage $x$ with a third level datum $l$ and each map $s$ from places to twist indices of $D(x)$ that is read at each place and constant on conjugate places, there is a character datum $c$ for $l$ with twist index map $s$. A character datum is a choice $C$ (an `NChoice`), a tuple tie for $C$ with characters $\xi$ of $w$ and $\psi$ of $T$, the equalities $C.Q = Q(P)$ and $C.k' = T.k$ at twisted places, a `ChoiceSide` record, the condition `TwOK` and a theta condition `EMtTheta`.

## Proof

1. `StepW.and` joins eight lemmas of the same "eventually at all stages" form. The first, `nonGalois_exists_choice_alt`, turns a choice $C$ with a tuple tie, the right $\xi$, $\psi$, $Q$ and $k$, a `ChoiceSide` record and `TwOK` into a character datum with the twist index map of $C$. The other seven give local facts at twisted places: `gPlaces_of_levelA`, `twistConductors_avoid_excludedPrimes`, `badV_subset_gPl_union_qPl_of_admTw`, `paraShape_of_twisted_sideRead_readsHecke`, `level_uniformity_of_cmDatum_alt`, `joint_level_of_cm_datum_twOK` and `cellWt_of_sideRead_of_twOK`.
2. `StepW.of_all` reduces the claim to one stage. There `exists_level_comparison_choice_alt` takes $\chi = T.\psi$, $Q = Q(P)$, $k = T.k$ and $s$. Its main hypothesis, a level equality `LevEq` with a cell weight condition, comes from `levEq`, `gPlaces_of_levelA` and the last five facts. `twistConductors_avoid_excludedPrimes` gives the disjointness of $Q(v)$ from the excluded set.
3. This gives a choice $C$ as in step 1 with $C.\mathrm{twI} = s$, and `nonGalois_exists_choice_alt` gives $c$.

The proof of `exists_level_comparison_choice_alt` picks, by `Classical.epsilon`, a Galois character $\psi_0(v)$ attached to $\chi(v)$ of order dividing $\ell^{k(v)}$, through `exists_galoisCharacter_of_finiteOrder_heckeCharacter` and the global Artin map. It then builds readings of $\psi_0(v)$ and the choice `choiceOf`, and checks the fields of `ChoiceSide`.

## In the Lean code

The theorem is in [LevelComparisonChoicesExistAtAllPlaces.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LevelComparisonChoicesExistAtAllPlaces.lean#L107), with `exists_level_comparison_choice_alt` at [line 35](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LevelComparisonChoicesExistAtAllPlaces.lean#L35). Character data are `HeightCountingCharacterData` in [RootsOfUnityRingLeWittIntegers.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RootsOfUnityRingLeWittIntegers.lean#L63).

Odd points:

- The eight lemmas of step 1 are second names. We have read their statements, not the lemmas behind them.
- Four subfields of `ChoiceSide` are proved by `hE.elim`, because the type `Loc` of $D(x)$ is empty. They ask for nothing here.
- The name speaks of Harish-Chandra modules and `SerN`. Both pass only to `nonGalois_exists_choice_alt`, which is also the only user of `DiscreteSeriesCover` and `CasselmanWallach`.
