---
id: t-good-tower-intersection-extra
title: The components of a good tower have equal volumes (statement form)
kind: theorem
decl: GlobalTheory.T.good_tower_intersection_extra
module: Development.AutomorphicSpectrum.Proofs.DivisibilityProofs.GoodTowerIntersectionExtraStatement
covers: 428
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It has the same statement as [the relay](/entry/relay-good-tower-intersection-extra/), and its proof applies the relay. The relay in turn applies [`volEq_of_isFullIntersectionSystem`](/entry/vol-eq-of-is-full-intersection-system/), which has the content. The one user is [the volume theorem for good root towers](/entry/volume-theorem-x-of-inputs/), which needs the property `VolEq` of a good tower.

## Statement

Use the notation of [the volume theorem for good root towers](/entry/volume-theorem-x-of-inputs/). For a component $c$ of a root tower $T$, the volume is
$$\mathrm{vol}(c) = \frac{\deg_{M_{2,c}}(L_\rho^d)}{\deg_{\mathrm{Fl}}(L_\rho^d)}, \qquad \rho = (N-1, \dots, 0),$$
where the numerator is the geometric degree on the root model $M_{2,c}$.

**Theorem.** Assume `CmpSt` and $\mathrm{Given}$. Let $E$ be a CM field, abelian over $\mathbb{Q}$, with host $H$ and datum $D$ with $q \geq 1$ and $3q + 1 \leq p + q$. Let $Y$ be a global integral model, $T$ a root tower for $N = p + q$, $o$ a good origin of $Y$ for $T$ with `Extra`, and $II$ a full intersection system. Then $\mathrm{vol}(c) = \mathrm{vol}(c')$ for all components $c, c'$ of $T$.

The conclusion does not involve $II$.

## Proof

Apply `Relay.good_tower_intersection_extra`.

## In the Lean code

The theorem is in [GoodTowerIntersectionExtraStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/GoodTowerIntersectionExtraStatement.lean#L16). The proof is `first | exact @… | exact … | (intros; apply … <;> assumption)`. `VolEq` and `vol` are in [Proportional.lean](lean:Development/AutomorphicSpectrum/Definitions/DivisibilityTowers/Proportional.lean#L129).

The name speaks of an intersection and of `Extra`. The conclusion is an equality of geometric volumes. The full intersection system $II$ is a hypothesis, but `VolEq` does not depend on it.
