---
id: global-model-tower-final-condition
title: Flat sections of near record height on a good tower, a pass-through
kind: theorem
decl: RootFieldNumerics.global_model_tower_final_condition
module: Development.WeilBound.CoreStatements.FlagImmersions.GlobalModelTowerFinalCondition
covers: 364
status: drafted
drafted_by: writer@claude
---
This theorem gives, for each component of a good root tower and each CM type, a flat section of near record height. Its proof only applies the tower form `OnHodge.tower` to [`rootFlatOnHodge`](/entry/root-flat-on-hodge/), which has the content. Its one user is the relay [`good_tower_real_extra`](/entry/relay-good-tower-real-extra/), which has the same statement.

## Statement

Take $E$, $H$, $D$ of signature $(p,q)$, $X_o$, $l$, $c$, $Y$, the root tower $T$, the good origin $o$ and the intersection system $II$ as in [the entry on the bounds `I5` and `I6`](/entry/global-model-tower-fifth-condition/). Let $\mathrm{rd}_E$ be the root discriminant of $E$ and $L_H = \operatorname{Re} L'(1,\chi)/L(1,\chi)$ for the quadratic character $\chi$ modulo the prime $d_H$ of $H$.

**Theorem.** Assume `FlatDegree` and `Given`. If $Y$ is global, $o$ has `Extra`, $II$ is a full intersection system and $p, q \ge 1$, then for each component $a$ of $T$ and each CM type $\tau$ there is a flat root datum $R$ on $M_{2,a}$ at $\tau$ whose height satisfies `NearRecord` for $p + q$, the bad primes of $T$, $\mathrm{rd}_E$ and $L_H$.

The objects `RootFlat` and `NearRecord` are stated in [the entry on `rootFlatOnHodge`](/entry/root-flat-on-hodge/).

## Proof

`OnHodge.tower` applies `rootFlatOnHodge` to the root origin $o_{2,a}$. It uses that the prime set $S_2$ of the origin is the bad set of $T$, and that the index $j$ of the tower equals $p$ with $1 \le j < p + q$. This gives $p, q \ge 1$.

## In the Lean code

The theorem is in [GlobalModelTowerFinalCondition.lean](lean:Development/WeilBound/CoreStatements/FlagImmersions/GlobalModelTowerFinalCondition.lean#L32). The hypotheses `o.Extra`, `IsFullIntersectionSystem II`, $p \ge 1$ and $q \ge 1$ are never used, and $II$ plays no part. The name "final condition" does not describe the statement.
