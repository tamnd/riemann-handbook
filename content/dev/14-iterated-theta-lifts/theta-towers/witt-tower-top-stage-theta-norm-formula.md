---
id: witt-tower-top-stage-theta-norm-formula
title: The top stage norm formula, as the tower calls it
kind: theorem
decl: GlobalTheory.T.witt_tower_top_stage_theta_norm_formula
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.WittTowerTopStageThetaNormFormula
covers: 365
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`theta_tower_top_stage_norm_eq`](/entry/theta-tower-top-stage-norm-eq/). It is the form that [the tower of theta lifts](/entry/tower-alt-bis/) calls for its top stage. That entry gives the statement and the proof.

## Statement

**Theorem.** Assume [`ThetaLocalInputs`](/step/theta-local-inputs-def/), [`ThetaIntegralsAgree`](/step/theta-integrals-agree-def/) and [`LocalMatching`](/step/local-matching-def/). Then, for every large datum and grid with base point $\mu_0$, and for all $i, j$, there are a triangle $X$ of theta integrals at the top stage $(i, j)$, a constant $c(t)$ of $X$, and a nonzero factor $\kappa(t)$ such that:

- $\kappa(t) = \zeta\, \kappa(\mu_0)$ with $\zeta$ a unit away from the level $Q_n(t)$;
- each square constant $c'$ at $t$ equals $\kappa(t)\, c(t)$.

The statement is word for word that of `theta_tower_top_stage_norm_eq`.

## Proof

The proof is one tactic, `first | exact @… | exact … | (intros; apply … <;> assumption)`, with the name `theta_tower_top_stage_norm_eq`. There is no mathematics here.

## In the Lean code

The theorem is at [WittTowerTopStageThetaNormFormula.lean line 50](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/WittTowerTopStageThetaNormFormula.lean#L50), in the same file as the theorem that it renames. It sets `maxHeartbeats` to 1000000, as the other wrappers of this family do. The name speaks of a Witt tower and a norm formula. The statement names neither: it relates two constants of theta integrals at one stage.
