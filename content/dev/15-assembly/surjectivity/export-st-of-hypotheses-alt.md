---
id: export-st-of-hypotheses-alt
title: The export statement from thirteen conditions at twisted places
kind: theorem
decl: GlobalTheory.BigOn.Exp.exportSt_of_hypotheses_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ExportStOfPrints
covers: 666
status: drafted
drafted_by: writer@claude
---
This theorem proves `ExportedStatement` by proving thirteen conditions at twisted places and joining them. It is used through three second names, the nearest being [`exportSt_of_discrete_series_cover`](/entry/export-st-of-discrete-series-cover/). At the top of that chain, [the surjectivity statement](/entry/onto-x-of-hypotheses-alt-alt/) passes the result to the twist bound.

## Statement

A statement holds *eventually at points* of a family $F_m$ if there is $x_0$ such that it holds for all $x \ge x_0$, all indices $i$ and all points $p$ at $(x, i)$ with the point conditions and `More p`.

**Theorem.** Assume `CuspRapidDecay`, `GlobalArtinReciprocity`, `RayClassFieldSt`, `DiscreteSeriesCover`, `CasselmanWallach` and `SeriesRatS`. Then for each closed family hypothesis, eventually at points $p$, for each twisted place $v$ of $p$ and each level $j$, `ExportTie` holds at $v$ and $j$, with the prime `ownAt v`.

`ExportTie` says: there is a semilinear map $r$ from $L^{n_W(j)}$ to the extended space of forms at $v$ such that `Reads` holds for $r$, the idempotent operator of level $j$, the theta base lattice and the theta tuple. We have not unfolded `Reads` or the six inputs.

## Proof

Each condition has the form `TwistConditions Q`: eventually at points, $Q$ holds at each twisted place $w$ and level $j$.

1. With no input: a canonical map exists with a basis of linearly independent images (`bigOn_canEx`), it commutes with the projection (`bigOn_canProj`), the twist is admissible (`twist_admissible'`), each prime that divides a fixed integer of the host lies in the set $S_0$ of the twist (`lowAt`), and an adapted setup exists (`adaptEx'`).
2. From the twist condition: the twist character with `GlobalArtinReciprocity` (`twist_character_of_artin'`), and the recursive side (`reciprocity_side_of_twAdm`).
3. The rationality at the place, from four inputs and step 1 (`at_statement_of_low_weight_twAdm`). Then the rational compatibility (`tieRat_of_twAdm_and_at`).
4. The base lattice does not change under a change of setup (`conjBase_of_ray_class_field_and_seriesRat`). Nor does the twisted lattice (`conjTw_of_discrete_series_and_casselman_wallach`). This is the only use of `DiscreteSeriesCover` and `CasselmanWallach`.
5. Two inequalities each way between the lattices of the canonical map and the base and twisted lattices (`baseLe_…`, `baseGe_…`, `twist_upper_bound_of_prints`, `twist_lower_bound_of_prints`).

Then `InductionConditions.exportSt` joins them. At a point, it takes an export tie $Z$ and a setup that fits, gets equality of lattices from step 5, and moves it to the setup of $Z$ by step 4.

## In the Lean code

The theorem is in [ExportStOfPrints.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExportStOfPrints.lean#L27). The conditions and `InductionConditions.exportSt` are in [RowAtOfRatStep.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowAtOfRatStep.lean#L111). `ExportedStatement` is in [ExportSt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExportSt.lean#L33), and `ExportTie` in [LeafTW1OfAllConjugatesGood.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/LeafTW1OfAllConjugatesGood.lean#L365).

We read the steps from the names of the conditions and have not opened the thirteen lemmas. A parallel copy, `GlobalTheory.BigOn.Exp.exportSt_of_hypotheses`, is in [ExportStatementOfDiscreteSeries.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExportStatementOfDiscreteSeries.lean#L31).
