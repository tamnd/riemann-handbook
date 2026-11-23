---
id: theta-tower-top-stage-norm-eq
title: A top stage triangle whose constant gives the square constant
kind: theorem
decl: GlobalTheory.SqTower.theta_tower_top_stage_norm_eq
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.WittTowerTopStageThetaNormFormula
covers: 364
status: drafted
drafted_by: writer@claude
---
This theorem gives the first step of [the tower of theta lifts](/entry/tower-alt-bis/). At the stage $(i, j)$ it finds a top triangle of theta integrals with a constant $c(t)$, and a nonzero factor $\kappa(t)$ with $c' = \kappa(t)\, c(t)$ for each square constant $c'$ at $t$. The ratio $\kappa(t)/\kappa(\mu_0)$ is a unit away from the level. The tower calls it through its renaming [`witt_tower_top_stage_theta_norm_formula`](/entry/witt-tower-top-stage-theta-norm-formula/).

## Statement

A *triangle* $X$ (`Tri`) has three Hermitian spaces $A$, $A'$ and $V$ with $\operatorname{rank} A + \operatorname{rank} A' = \operatorname{rank} V$, Weil representations, theta test vectors and Haar measures on fundamental domains. For each $t$ and test polynomial $P$ it has theta integrals $I_t(P)(h) = \int \theta_t(g, h; \varphi_P)\, dg$ over a fundamental domain in the adelic unitary group of $A$, and $I'_t(P')(h)$ in the same way for $A'$. `X.IsConst c` says: $c(t) \neq 0$ for some $t$, and there are $P$, $P'$ with integrable kernels, $I'_t(P') \neq 0$, and $I_t(P) = c(t)\, I'_t(P')$ for all $t$.

**Theorem.** Assume [`ThetaLocalInputs`](/step/theta-local-inputs-def/), [`ThetaIntegralsAgree`](/step/theta-integrals-agree-def/) and [`LocalMatching`](/step/local-matching-def/). Then `GBig Q` holds, where $Q$ says: for each Weil datum $W$ with a standard character, each grid choice $S$ with `NumbersIn S μ₀`, each real match $\rho$ and all $i, j$, there are a triangle $X$ and functions $c, \kappa$ on $T$ with:

1. $X$ is a stage of type $(p, q)$ (`IsStageC`), where $p = \lfloor (m-j-1)/2 \rfloor$ and $q = \lfloor (m-j)/2 \rfloor$. So $A$ and $A'$ have the ranks of the grid at $(i+1, j+1)$ and $(i, j)$, with fixed characters and the index conditions `NegIdx`;
2. `X.IsConst c`;
3. for each $t$: $\kappa(t) \neq 0$ and $\kappa(t) = \zeta\, \kappa(\mu_0)$ for some $\zeta$ in the field $L$ that is a unit away from $Q_n(t)$ (`IsAwayUnit`: $\zeta\, Q_n(t)^k = a$ with $a \mid Q_n(t)^{k'}$ in $\mathcal{O}_L$);
4. for each $t$ and each square constant $c'$ at $t$ (`IsSquareConst`, with `SquareNonzero`), $c' = \kappa(t)\, c(t)$.

A square constant compares two theta integrals over a fundamental domain: $\deg(z) \int K_{\mathrm{big}} = c' \int z \cdot K_{\mathrm{small}}$ for every matched pair of test vectors. We have not unfolded `IsStdChar`, `NumbersIn` or `RealMatch`.

## Proof

`gBig_of₃` joins the thresholds of three lemmas.

1. `exists_grid_of_square_tower` gives a triangle $X$ on the grid spaces with `TopGrid` and `IsStageC` of type $(p, q)$.
2. `exists_factor_of_isStageC` gives $\lambda$ with `Factor X λ`: $\lambda(t) \neq 0$ and $I_t(P) = \lambda(t)\, J_t(pP)$, $I'_t(P') = J_t(p'P')$ for linear maps $p, p'$ and injective $J_t$. This gives `X.IsConst λ`.
3. [`theta_square_norm_comparison`](/entry/theta-square-norm-comparison/) gives $\kappa$ with clause 3 and $c' = \kappa(t)\, \lambda(t)$.

Take $c = \lambda$.

## In the Lean code

The theorem is at [WittTowerTopStageThetaNormFormula.lean line 21](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/WittTowerTopStageThetaNormFormula.lean#L21). `Tri` and `Tri.IsConst` are in [UnitCharTriangle.lean](lean:Development/AbelianVarietyTheory/BlockTheory/TwistedDiscreteSeries/UnitCharTriangle.lean#L76), `IsStageC` in [NegIdxOfIsStd.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/NegIdxOfIsStd.lean#L24), and `IsSquareConst` in [ExistsNotRelZero.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ExistsNotRelZero.lean#L213). The proof is bookkeeping. The real content is in the third lemma, through [`regulator_constant_eq`](/entry/regulator-constant-eq/).
