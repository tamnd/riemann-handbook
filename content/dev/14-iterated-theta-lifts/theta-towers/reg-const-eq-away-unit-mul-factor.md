---
id: reg-const-eq-away-unit-mul-factor
title: The regularized constant is a unit factor times the stage factor, as the comparison calls it
kind: theorem
decl: GlobalTheory.T.regConst_eq_away_unit_mul_factor
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.RegConstEqAwayUnitMulFactor
covers: 321
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`regulator_constant_eq`](/entry/regulator-constant-eq/), which has the real content. [The square comparison](/entry/theta-square-comparison/) calls it for a tied real match.

## Statement

**Theorem.** Assume [`ThetaLocalInputs`](/step/theta-local-inputs-def/), [`ThetaIntegralsAgree`](/step/theta-integrals-agree-def/) and [`LocalMatching`](/step/local-matching-def/). For every large datum and grid with base point $\mu_0$, every Weil datum with a standard character, grid choice $S$ with `NumbersIn S μ₀`, real match $\rho$ that is tied (`ρ.Tied`), stage $(i, j)$, and top stage triangle $X$ with a factor $\lambda$ (`TopGrid`, `IsStageC`, `Factor X λ`), there is $\kappa$ with:

- $\kappa(t) \neq 0$ and $\kappa(t) = \zeta\, \kappa(\mu_0)$, with $\zeta$ a unit away from $Q_n(t)$;
- each regularized constant $c_0$ at $t$ (`RegConst`) equals $\kappa(t)\, \lambda(t)$.

`RegConst c₀` says: for each volume datum at $t$, each matched pair of test vectors $\Theta, \Theta'$ and all $g, g_1$, there is $z$ with $\deg z \neq 0$ such that both integrals converge and $\deg(z) \int K_{\mathrm{big}} = c_0 \int z \cdot K_{\mathrm{small}}$. The statement is word for word that of `regulator_constant_eq`.

## Proof

The proof is one tactic, `first | exact @… | exact … | (intros; apply … <;> assumption)`, with the name `regulator_constant_eq`. There is no mathematics here.

## In the Lean code

The theorem is at [RegConstEqAwayUnitMulFactor.lean line 224](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/RegConstEqAwayUnitMulFactor.lean#L224), in the same file as `regulator_constant_eq` (line 51). `RegConst` is in [RegConst.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/RegConst.lean#L32).
