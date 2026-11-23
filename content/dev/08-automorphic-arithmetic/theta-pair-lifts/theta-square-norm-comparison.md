---
id: theta-square-norm-comparison
title: The square comparison, as the top stage calls it
kind: theorem
decl: GlobalTheory.T.theta_square_norm_comparison
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.ThetaSquareNormComparison
covers: 349
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`theta_square_comparison`](/entry/theta-square-comparison/). [The top stage lemma](/entry/theta-tower-top-stage-norm-eq/) calls it to write each square constant as a unit factor times the factor $\lambda(t)$ of a triangle. That entry has the statement and the proof.

## Statement

**Theorem.** Assume [`ThetaLocalInputs`](/step/theta-local-inputs-def/), [`ThetaIntegralsAgree`](/step/theta-integrals-agree-def/) and [`LocalMatching`](/step/local-matching-def/). For every large datum and grid with base point $\mu_0$, every Weil datum, real match $\rho$ and stage $(i, j)$, and every top stage triangle $X$ with a factor $\lambda$ (`Factor X λ`), there is $\kappa$ with:

- $\kappa(t) \neq 0$ and $\kappa(t) = \zeta\, \kappa(\mu_0)$, with $\zeta$ a unit away from $Q_n(t)$;
- each square constant $c'$ at $t$ equals $\kappa(t)\, \lambda(t)$.

The statement is word for word that of `theta_square_comparison`.

## Proof

The proof is one tactic, `first | exact @… | exact … | (intros; apply … <;> assumption)`, with the name `theta_square_comparison`. There is no mathematics here.

## In the Lean code

The theorem is at [ThetaSquareNormComparison.lean line 49](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/ThetaSquareNormComparison.lean#L49), in the same file as the theorem that it renames. The name says "norm comparison", but the statement compares constants of theta integrals; no norm appears.
