---
id: regulator-constant-eq
title: The regularized square constant is an away unit times the factor of a triangle
kind: theorem
decl: GlobalTheory.ThetaRegularizationComparison.regulator_constant_eq
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.RegConstEqAwayUnitMulFactor
covers: 320
status: drafted
drafted_by: writer@claude
---
This theorem computes the regularized constant of a theta square at the top stage of a grid. The constant at a point $t$ is $\kappa(t)\,\lambda(t)$. Here $\lambda$ is the factor of a triangle, and $\kappa(t)$ is $\kappa(\mu_0)$ times a unit away from a level. The second name [`regConst_eq_away_unit_mul_factor`](/entry/reg-const-eq-away-unit-mul-factor/) passes it to [the square comparison](/entry/theta-square-comparison/). Below this theorem are 320 declarations.

## Statement

**Theorem.** Assume [`ThetaLocalInputs`](/step/theta-local-inputs-def/), [`ThetaIntegralsAgree`](/step/theta-integrals-agree-def/) and [`LocalMatching`](/step/local-matching-def/). Then `GBig Q` holds, where `Q` is as follows.

Take a Weil datum $W$ with a standard character, a grid choice $S$ with `NumbersIn S μ₀`, a real match $\rho$ with `ρ.Tied`, and indices $i, j$. Take a triangle $X$ (`TriG G i j`) between the stages $(i+1, j+1)$ and $(i, j)$ that fits the grid (`TopGrid`) and has the characters of the stage (`IsStageC`). Take $\lambda : T \to \mathbb{C}$ with `Factor X λ`. This says that $\lambda(t) \neq 0$, and that the theta integral $I_t$ of $X$ is $\lambda(t)$ times the integral $I'_t$ of the smaller side, after injective maps to a common space. Then there is $\kappa : T \to \mathbb{C}$ with:

- for each $t$, $\kappa(t) \neq 0$ and $\kappa(t) = \zeta\,\kappa(\mu_0)$, with $\zeta$ in the field `LL` and `IsAwayUnit (Qn G t) ζ`;
- for each $t$ and $c_0$, if `RegConst W S.B ρ t i j c₀`, then $c_0 = \kappa(t)\,\lambda(t)$.

`IsAwayUnit m ζ` says that there are an algebraic integer $a$ and $k, k'$ with $a \mid m^{k'}$ and $\zeta m^k = a$. So $\zeta$ is a unit away from the primes of $m$. `RegConst` is as in [the second name](/entry/reg-const-eq-away-unit-mul-factor/). `TopGrid` says that the lattices and frames of $X$ are those of the grid. We have not unfolded `NumbersIn` or `RealMatch.Tied`.

## Proof

1. The three inputs go to five lemmas: twisted local factors match, twisted square theta integrals agree, a dictionary of theta parameters, an involutive flip correspondence, and a match of finite data at each stage. The flip gives $\kappa$ with the away unit property.
2. The thresholds are maxima of the thresholds of these lemmas, and $x \ge 12^{5/\varepsilon}$. Every square at the grid stands.
3. The dictionary gives linear equivalences that turn the kernels of $X$ into theta kernels of a Fock model.
4. Fix $t$. A nonzero theta integral exists by `exists_integral_ne_zero`, which uses strong approximation for $\mathrm{SU}$. The helper `regularised_thetaInt_comparison_smul` in this file gives a constant $c \neq 0$ that relates the big and the small integral. Haar measures are rescaled by `exists_haar_smul`. Then `eq_of_regConst` gives $c_0 = l(t)\,m(t)\,\kappa(t)\,\lambda(t)$.
5. The scalars $l$ and $m$ do not depend on $t$, by injectivity of scalar multiplication on a nonzero vector. The answer is $l(\mu_0)\,m(\mu_0)\,\kappa$.

## In the Lean code

The theorem is at [RegConstEqAwayUnitMulFactor.lean line 51](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/RegConstEqAwayUnitMulFactor.lean#L51), with `maxHeartbeats 1000000`. The helper is at line 23 of the same file. `RegConst` and `TriG` are in [RegConst.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/RegConst.lean#L22). `IsAwayUnit` is in [TupleConstantsNeZero.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/TupleConstantsNeZero.lean#L15). `Factor` is in [RatInOfUnit.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/RatInOfUnit.lean#L75). `eq_of_regConst` is in [StageFactorNonvanishingScalars.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/StageFactorNonvanishingScalars.lean#L78).

Odd points:

- The name says "regulator", but the statement is about the regularized constant `RegConst`, not a regulator of units.
- The same statement is proved again by a `first | exact` wrapper at line 224.
