---
id: exists-row-placement-finite-element-matches-levels
title: A row placement with matching levels, a second name
kind: theorem
decl: GlobalTheory.T.exists_rowPlacement_finiteElement_matches_levels
module: Development.AbelianVarietyTheory.Proofs.TwistedOperators.ExistsRowPlacementFiniteElementMatchesLevelsStatement
covers: 451
status: drafted
drafted_by: writer@claude
---
This theorem is a second name of [`rowPlacement_exists`](/entry/row-placement-exists/). It has no content of its own. Its only user is [a normalised indefinite realisation extends](/entry/placement-of-realisation-alt/), which applies it to the data of a realisation $Q$ and three fields of its normalisation. That entry also sketches the proof of `rowPlacement_exists`.

## Statement

Assume `DiscreteSeriesClassification` (see [the parent entry](/entry/placement-of-realisation-alt/)). Let $D$ be a datum, $R$ real data over a family $A$, $F$ a face, $X$ a Hida setting with a good operator, $\iota$ an isomorphism `GA D (Yc D 0) ≃* X.B.I.GA` and $t_S \in$ `GfC (Yc D 0)`. Assume about ten further hypotheses on these data: a level character, `IsGrp`, `IsModels`, `HostHyp D`, `IdempotentRealFixed D`, that $\iota$ and `X.ιE` are the standard maps, and a matching of places with the idempotent of $A$. Write $P(t)$ for the conjunction of the level conjugation `ConjLevel` at $t^{-1}$ and `RowLevelMatchAt R F X h t`. Assume finally that if some $t \in$ `GfC (Yc D 0)` has $P(t)$, then $P(t_S)$ holds.

**Theorem.** There is $t \in$ `GfC (Yc D 0)` with $P(t)$, and there is $c' \in \mathbb R$ with the evaluation tie `EvalTieT … X Gd ι tS c'`.

We have not unfolded `ConjLevel`, `RowLevelMatchAt` or `EvalTieT`.

## Proof

The proof is `first | exact @GlobalTheory.rowPlacement_exists | ...`. The two statements are the same, word for word.

## In the Lean code

The theorem is in [ExistsRowPlacementFiniteElementMatchesLevelsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExistsRowPlacementFiniteElementMatchesLevelsStatement.lean#L12). `rowPlacement_exists` is in [ExistsRowPlacementFiniteElementMatchesLevels.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExistsRowPlacementFiniteElementMatchesLevels.lean#L24). The only user is in [PlacementOfRealisation.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PlacementOfRealisation.lean#L26).

The last hypothesis moves $P$ from any $t$ to $t_S$. The conclusion only states that some $t$ has $P(t)$; the proof uses $P(t_S)$ for the evaluation tie.
