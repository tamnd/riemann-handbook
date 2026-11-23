---
id: exists-good-tower
title: Building a good root tower from the components of the model
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.TopTower.exists_good_tower
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.ExistsGoodRootTower
covers: 516
status: drafted
drafted_by: writer@claude
---
This theorem builds the root tower and its good origin that `GoodTowerExistsX` asks for. Its statement form is [`T.exists_good_root_tower`](/entry/exists-good-root-tower/), which states it in full; [the good tower theorem](/entry/good-tower-and-volume/) uses that form. The work on each component is in [`comp_data`](/entry/comp-data/). This proof makes one reference origin for each irreducible component of the model, changes it to each level $B$, and puts the pieces into the structures `RootTower`, `TowerOrigin` and `GoodOrigin`.

## Statement

The statement is that of [`T.exists_good_root_tower`](/entry/exists-good-root-tower/): from `Top.Given`, `Out.WeilSt` and the two flat generator statements, for a global model $Y$ with split components and $p, q \geq 1$, there are a root tower $T$ and a good origin $o$ with the two conditions of `Extra`.

## Proof

1. `T.generic_points_finite_nonempty` shows that the set $C$ of points of $Y$ with no proper generization (the generic points of the irreducible components) is finite and not empty. These points are the components of $T$.
2. For each $x \in C$, [`comp_data`](/entry/comp-data/) gives an analytic system, fixed data, a reference root model $R_x$ and a reference origin $o_x$ with an empty set of primes. The origin has flag degree $1$ and is ample, and the lifts of condition 1 of `Extra` exist.
3. Let $M'$ be the number `l.M'`, the lcm of the two integers $M$ and $A$ of the level, so $M' \neq 0$. Let the bad set be the primes that divide $2\,|d_E|\,M'$; it contains $2$. For each $B$, let $S_B$ be the primes $p \leq B$ together with the bad primes. Each $S_B$ contains the primes that divide $d_E$.
4. For each $B$ and $x$, `level_data` (in the same file) moves $o_x$ to a root model $M_{B,x}$ and an origin over $S_B$. The new origin satisfies `OmVB`, has $R(p) = 4$ for $p \in S_B$ and $J = \top$ for its realization, and its generic fibre is smooth. `level_data` calls `T.root_origin_good_primes_finite`, which uses `Out.WeilSt`, and `T.root_origin_coords_over_field`.
5. The tower $T$ has $j = p$, components $C$, the bad set of step 3, the weight $\nu(\tau, i) = -i$ and the models $M_{B,x}$. The tower origin uses $S_B$ and the origins of step 4. The good origin adds the reference data of step 2. Its fields `smooth` and `flat` come from steps 4 and 2. The rest is bookkeeping.

## In the Lean code

The theorem is in [ExistsGoodRootTower.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/ExistsGoodRootTower.lean#L77), with `comp_data` at line 20 and `level_data` at line 59. The structures are in [Proportional.lean](lean:Development/AutomorphicSpectrum/Definitions/DivisibilityTowers/Proportional.lean#L10), [TowerOrigin.lean](lean:Development/AutomorphicSpectrum/Definitions/GlobalGeometry/TowerOrigin.lean#L105) and [GoodOrigin.lean](lean:Development/AutomorphicSpectrum/Definitions/DivisibilityTowers/GoodOrigin.lean#L55).

The weight $\nu$ of the tower is the same for each CM type: $\nu(\tau, i) = -i$. The index $j$ of the tower is $p$, and $j < N$ needs $q \geq 1$. The reference origin of step 2 does not depend on $B$. Only the level origins of step 4 do.
