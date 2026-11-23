---
id: theta-square-comparison
title: Square constants are unit factors times the stage factor
kind: theorem
decl: GlobalTheory.SqCompare.theta_square_comparison
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.ThetaSquareNormComparison
covers: 348
status: drafted
drafted_by: writer@claude
---
This theorem writes each square constant at a point $t$ as $\kappa(t)\, \lambda(t)$, where $\lambda$ is the factor of a top stage triangle and $\kappa(t)/\kappa(\mu_0)$ is a unit away from the level. Its renaming [`theta_square_norm_comparison`](/entry/theta-square-norm-comparison/) goes to [the top stage lemma](/entry/theta-tower-top-stage-norm-eq/) of the tower. The proof moves from an arbitrary real match to a tied one and then uses the result for regularized constants.

## Statement

Notation is as in [the top stage lemma](/entry/theta-tower-top-stage-norm-eq/). A triangle $X$ on the grid at $(i, j)$ (`TriG`) uses the spaces $V_{i+1, j+1}$, $V_{i, j}$ and $V_{i, j+1} \oplus V_{i+1, j}$. `TopGrid` says that its lattices and real data are those of the grid. `Factor X λ` says: $\lambda(t) \neq 0$ for all $t$, and there are a space $\Pi$, a surjective linear map $p$, a linear map $p'$ and injective maps $J_t$ with $I_t(P) = \lambda(t)\, J_t(pP)$ and $I'_t(P') = J_t(p'P')$ when the kernel of $P'$ is integrable, and some integrable $P'$ has $p'P' \neq 0$.

**Theorem.** Assume [`ThetaLocalInputs`](/step/theta-local-inputs-def/), [`ThetaIntegralsAgree`](/step/theta-integrals-agree-def/) and [`LocalMatching`](/step/local-matching-def/). Then `GBig Q` holds, where $Q$ says: for each Weil datum $W$ with a standard character, grid choice $S$ with `NumbersIn S μ₀`, real match $\rho$, stage $(i, j)$, and triangle $X$ with `TopGrid`, `IsStageC` of type $(p, q)$ and `Factor X λ`, there is $\kappa \colon T \to \mathbb{C}$ with

1. $\kappa(t) \neq 0$ and $\kappa(t) = \zeta\, \kappa(\mu_0)$ for some $\zeta \in L$ that is a unit away from $Q_n(t)$;
2. $c' = \kappa(t)\, \lambda(t)$ for each $t$ and each square constant $c'$ at $t$ (`IsSquareConst`) with `SquareNonzero`.

## Proof

`gBig_three` joins the thresholds of three lemmas. Fix the data.

1. `exists_tied_theta_pair` gives a real match $\rho_0$ with the same vacuum vectors as $\rho$ that is tied (`ρ₀.Tied`), and a regularized constant $c_0(t)$ for $\rho_0$ at each $t$ (`RegConst`).
2. `theta_real_places_separation` gives $l \neq 0$ such that $c' = l\, c_0$ whenever $c'$ is a square constant for $\rho$ and $c_0$ a regularized constant for $\rho_0$ at the same $t$.
3. [`regConst_eq_away_unit_mul_factor`](/entry/reg-const-eq-away-unit-mul-factor/), applied to $\rho_0$, gives $\kappa_0$ with clause 1 and $c_0 = \kappa_0(t)\, \lambda(t)$.

Put $\kappa = l\, \kappa_0$. Clause 1 holds with the same $\zeta$, since $l$ cancels. Then $c' = l\, c_0(t) = \kappa(t)\, \lambda(t)$. The real content is in [`regulator_constant_eq`](/entry/regulator-constant-eq/), the theorem behind step 3.

## In the Lean code

The theorem is at [ThetaSquareNormComparison.lean line 17](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/ThetaSquareNormComparison.lean#L17). `Factor` is in [RatInOfUnit.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/RatInOfUnit.lean#L75), and `TriG`, `TopGrid` and `RegConst` in [RegConst.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/RegConst.lean#L22). We have not unfolded `RealMatch.Tied`.

Odd points:

- The hypothesis `SquareNonzero` is not used: line 28 binds it as `_`. Clause 2 holds for every square constant.
- `gBig_three` in [ExistsNonvanishingFactorStage.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsNonvanishingFactorStage.lean#L17) and `gBig_of₃` in [ExistsStageConstantTriangle.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsStageConstantTriangle.lean#L26) have the same statement. A third copy, with the extra hypothesis `Lc.Is μ₀`, is in [DefiniteBottomDictionaryFramesExponentsKernel.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/DefiniteBottomDictionaryFramesExponentsKernel.lean#L26).
