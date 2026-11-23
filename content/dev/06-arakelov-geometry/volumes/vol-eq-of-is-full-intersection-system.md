---
id: vol-eq-of-is-full-intersection-system
title: Equal volumes of the components of a good tower, a pass-through
kind: theorem
decl: SheetDecomposition.volEq_of_isFullIntersectionSystem
module: Development.WeilBound.CoreStatements.VolumeEquality.VolEqOfIsFullIntersectionSystem
covers: 426
status: drafted
drafted_by: writer@claude
---
This theorem says that all components of a root tower with a good origin have the same volume. Its proof only applies `volEq_of_degPush` to the proved lemma `degPush`. Its one user is the relay [`good_tower_intersection_extra`](/entry/relay-good-tower-intersection-extra/), which has the same statement.

## Statement

Take $E$, $H$, $D$ of signature $(p,q)$, $X_o$, $l$, $c$, $Y$, the root tower $T$, the good origin $o$ and the intersection system $II$ as in [the entry on the bounds `I5` and `I6`](/entry/global-model-tower-fifth-condition/). For a component $a$ of $T$, let $\operatorname{vol}(a)$ be the value of the geometric functional of $M_{2,a}$ on a power of the linear root, divided by the flag degree. We have not unfolded the functional `geoFun`.

**Theorem.** Assume the comparison statement `CmpSt` and `Given`. If $Y$ is global, $o$ has `Extra`, $II$ is a full intersection system, $q \ge 1$ and $3q + 1 \le p + q$, then $\operatorname{vol}(a) = \operatorname{vol}(a')$ for all components $a, a'$ (`T.VolEq`).

## Proof

The proof term is `volEq_of_degPush degPush`. In `volEq_of`, the degree of a pushforward is written in two ways: through sheets, as $\kappa \cdot \deg \cdot [F:\mathbb{Q}] \cdot v$ with one common ball volume $v$, and through `DegPush`, as $c_0 \cdot \deg \cdot [F:\mathbb{Q}] \cdot \operatorname{vol}(a)$ with $c_0 \ne 0$. Cancelling gives $c_0 \operatorname{vol}(a) = \kappa v$ for each $a$.

## In the Lean code

The theorem is in [VolEqOfIsFullIntersectionSystem.lean](lean:Development/WeilBound/CoreStatements/VolumeEquality/VolEqOfIsFullIntersectionSystem.lean#L16). The work is in [VolEqOfDegPush.lean](lean:Development/WeilBound/CoreStatements/VolumeEquality/VolEqOfDegPush.lean#L22) and [DegPush.lean](lean:Development/WeilBound/CoreStatements/VolumeEquality/DegPush.lean#L19), which have no entries. The name speaks of the full intersection system; the proof goes through `DegPush`.
