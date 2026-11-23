---
id: relay-good-tower-real-extra
title: A flat root line of bounded height on each component (relay)
kind: theorem
decl: GlobalTheory.CompanionTheory.Relay.good_tower_real_extra
module: Development.AutomorphicSpectrum.Proofs.DivisibilityProofs.GoodTowerRealExtra
covers: 365
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. Its statement is that of [the statement form](/entry/t-good-tower-real-extra/): under `FlatDegree` and $\mathrm{Given}$, each component of a good tower at level $B = 2$ has, for each $\tau$, a flat root line whose height is near the record. Its proof applies [`global_model_tower_final_condition`](/entry/global-model-tower-final-condition/), which has the same statement.

## Statement

See [the statement form](/entry/t-good-tower-real-extra/), which defines flat root lines and the record bound.

## Proof

The proof is `first | exact @RootFieldNumerics.global_model_tower_final_condition | exact …`. That theorem is two lines. It builds `RootFlatOnHodge` from `FlatDegree` and $\mathrm{Given}$ by [`rootFlatOnHodge`](/entry/root-flat-on-hodge/), and applies `OnHodge.tower` to it, to `IsGlobal` and to the origin with its property `omVB`. `RootFlatOnHodge` is the same bound for one root origin whose bad set is the set of primes dividing $2\,d_E\,M'$ for an integer $M'$ of the level. `OnHodge.tower` shows that the bad set of the origin at $B = 2$ is the bad set of the tower, and gets $p, q \geq 1$ from $1 \leq j < N$.

## In the Lean code

The theorem is in [GoodTowerRealExtra.lean](lean:Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/GoodTowerRealExtra.lean#L16). `global_model_tower_final_condition` is in [GlobalModelTowerFinalCondition.lean](lean:Development/WeilBound/CoreStatements/FlagImmersions/GlobalModelTowerFinalCondition.lean#L32), and `RootFlatOnHodge` and `OnHodge.tower` are in [NearRecordOfValue.lean](lean:Development/AutomorphicSpectrum/Statements/GeometryStatements/NearRecordOfValue.lean#L13).

Five hypotheses are not used in `global_model_tower_final_condition`: `Extra`, `IsFullIntersectionSystem`, $1 \leq p$, $1 \leq q$, and the intersection system $II$ itself.
