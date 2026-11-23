---
id: relay-good-tower-intersection-extra
title: The components of a good tower have equal volumes (relay)
kind: theorem
decl: GlobalTheory.CompanionTheory.Relay.good_tower_intersection_extra
module: Development.AutomorphicSpectrum.Proofs.DivisibilityProofs.GoodTowerIntersectionExtra
covers: 427
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. Its statement is that of [the statement form](/entry/t-good-tower-intersection-extra/): under `CmpSt` and $\mathrm{Given}$, with $q \geq 1$ and $3q + 1 \leq p + q$, all components of a good tower have the same volume. Its proof applies [`volEq_of_isFullIntersectionSystem`](/entry/vol-eq-of-is-full-intersection-system/), which has the same statement and the content.

## Statement

See [the statement form](/entry/t-good-tower-intersection-extra/).

## Proof

The proof is `first | exact @SheetDecomposition.volEq_of_isFullIntersectionSystem | exact …`. The proof of that theorem is one term, `volEq_of_degPush degPush`. Here `DegPush` says, under its own hypotheses, that a degree `degMu` of a component origin is a nonzero constant $c_0(|\Psi|, p, q)$ times a degree of the origin, times $[F:\mathbb{Q}]$ for the coefficient field $F$, times $\mathrm{vol}(a)$. The lemma `volEq_of_degPush` combines it with eight further lemmas of the namespace `SheetDecomposition`, among them `ballVolEq`. We have not unfolded these lemmas.

## In the Lean code

The theorem is in [GoodTowerIntersectionExtra.lean](lean:Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/GoodTowerIntersectionExtra.lean#L16). `volEq_of_isFullIntersectionSystem` is in [VolEqOfIsFullIntersectionSystem.lean](lean:Development/WeilBound/CoreStatements/VolumeEquality/VolEqOfIsFullIntersectionSystem.lean#L16). `DegPush` is in [BaseUnifEx2.lean](lean:Development/WeilBound/CoreStatements/VolumeEquality/BaseUnifEx2.lean#L58).

The conditions $q \geq 1$ and $3q + 1 \leq p + q$ also appear in `BallVolEq` (line 52 of the same file). That statement says that two integrals of a density `ballDens` over fundamental sets are equal. This is probably where the two conditions are used, but we have not traced it.
