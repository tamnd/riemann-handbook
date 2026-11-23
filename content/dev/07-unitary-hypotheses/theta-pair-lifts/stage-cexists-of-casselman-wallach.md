---
id: stage-cexists-of-casselman-wallach
title: Character data at third level stages, second name
kind: theorem
decl: GlobalTheory.T.stageCExists_of_casselmanWallach
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.LevelComparisonChoicesExistAtAllPlaces
covers: 566
status: drafted
drafted_by: writer@claude
---
This theorem is a second name of [`stageCExists_of_harishChandra_serN`](/entry/stage-cexists-of-harish-chandra-ser-n/), which has the real content. It gives the statement `ThirdStageExists` to two callers in the subtree of [membership and bundles at the origin parameters](/entry/exists-base-lattice-of-prime-alt/): `sc_of_sck_alt` in SeriesCoverOfPrimitive.lean and a stage list in FiniteLevelAndSecond.lean.

## Statement

**Theorem.** Assume `DiscreteSeriesCover`, `CasselmanWallach`, `HarishChandraModules`, `PublishedInputsThirdLayerAlt` and `SerN`, and let $h_L$ be a proof of `RecTExists`. Then `ThirdStageExists` $h_L$ holds.

`ThirdStageExists` says: eventually, at large bases $B$ with `KPx`, for each column datum $w$ with `Start`, each $P$ of type `Pre2` over $w$ and each stage $x$ of $P$, the following holds. Let $l$ be a third level datum at $x$. Let $s$ map each place $v$ of $B$ to a twist index of $D(x)$, so that $s(v)$ is read at $v$ (`ReadsAt`) and $s(\bar v) = s(v)$. Then there is a character datum $c$ (a `HeightCountingCharacterData` for $l$, $T.k$ and $T.\psi$) whose twist index map is $s$.

## Proof

The proof is `exact stageCExists_of_harishChandra_serN`, tried in three forms by `first`. It passes the six hypotheses along.

## In the Lean code

The theorem is in [LevelComparisonChoicesExistAtAllPlaces.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LevelComparisonChoicesExistAtAllPlaces.lean#L133). `ThirdStageExists` is in [ExtensionWithOrigin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExtensionWithOrigin.lean#L37).

The name speaks of Casselman-Wallach. `CasselmanWallach` is one of three representation theory hypotheses, and the proof only passes it on. The word "stage C" matches the third stage of `ThirdStageExists`.
