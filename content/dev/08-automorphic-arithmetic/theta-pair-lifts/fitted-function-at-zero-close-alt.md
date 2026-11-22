---
id: fitted-function-at-zero-close-alt
title: A bound on the maximal slope at fitted points
kind: theorem
decl: GlobalTheory.BigTop.Fun.Close.fittedFunction_at_zero_close_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.FittedFunctionAtZeroClose
covers: 4154
status: drafted
drafted_by: writer@claude
---
This theorem proves `ConstantFunctionFits Fld`, an upper bound for the maximal slope of a lattice at each point of a large family that carries a fitted grid. It is the content of [the constant function fits](/entry/fourier-coefficient-fit-of-join-alt/), which only repackages its hypotheses, and through it of item 3 of [HypsAlt is nonempty from the closed bound](/step/nonempty-hyps/). The proof collects sixteen "leaf" estimates and joins them with one assembly lemma.

## Statement

Assume `ThetaLocalInputs`, `HeckeFunctionalEquationAbs`, `ToricDenominator`, `Transport`, `TwistedTransport`, `ZetaDenominators`, `Refl`, [`ThetaIntegralsAgree`](/step/theta-integrals-agree-def/), [`LocalMatching`](/step/local-matching-def/), `FunctionalsSeparate` and `LambdaLowerBound₂`. These are the hypotheses of the [previous entry](/entry/fourier-coefficient-fit-of-join-alt/), in a new form.

Then `ConstantFunctionFits Fld` holds. It says: there is $C_{F,0}$ such that for each $C_F \ge C_{F,0}$ we have [`Closed`](/step/closed-def/) `FamHyp` $P$, where $P(F, C_H)$ is the statement below. Here `FamHyp` is a class of families, a conjunction of conditions such as `PageFix`, `PageWin` and `TwGood` that we have not unfolded.

$P(F, C_H)$: if `DIVinN F` holds, then there is $x_0$ such that for each $x \ge x_0$, each index $i$ and each point $p$ of $F$ at $(x, i)$ that meets `PointConditions'`, the following holds. If $p$ has a grid $G$ at level $C_F$ with a Weil datum $W$ over the real data of $p$, with `GridFit p G` and `Fld p C_F G W`, then for every real $C$

$$2\,\mu_{\max}(R_p) - \log 2 + \frac{\ell_K}{[K:\mathbb{Q}]} \le x_p^{C_H}\, b_p - \frac{1}{n_K} \sum_{v \mid \infty} \log \kappa_p(v).$$

Here $K$ is the number field of the side datum $S_p$ (`p.S false`), $R_p$ is its glued $\mathcal{O}_K$-lattice `RR` with the metrics `XE` at the infinite places, $\kappa_p$ is a positive function on the infinite places, and $x_p, b_p$ are the scale of $p$. The terms $\mu_{\max}$, $\ell_K$ and $n_K$ are `muMax`, `logDisc K` and `nPl K`. By their names they are the [maximal slope](/learn/arakelov/#hermitian-lattices-and-slopes) of a Hermitian lattice, the log of the discriminant and the number of infinite places; we have not unfolded them. In Lean the inequality is `(p.S false).FUN (p.N C CH)`.

`Fld p C_F G W` says that a record `SlopeTestRemainingChoices` exists whose four conditions `OK` hold.

## Proof

1. [`square_leading_term_bound`](/entry/square-leading-term-bound/) gives twelve facts about Hecke L-values, toric values and bottom pairs.
2. [`sum_size_bound_all_places`](/entry/sum-size-bound-all-places/) gives the bounds `FinK`, `AwayK` and `InfK`.
3. `local_sum_estimates_joined` gives five facts: `SumOKK`, `ConstK`, `LinK`, `Formula2K` and `SumRatK`.
4. `injK_of_separates` gives an injectivity fact from `FunctionalsSeparate` and `twisted_convergence_with_real_places`.
5. `abs_logDerivativeAtOne_le_x_rpow_eps` gives the bound $|\mathrm{logDerivativeAtOne}| \le x^{\varepsilon}$ along the families of `FamHyp`. With it, `toric_ratio_family_estimate'` (the one use of `TwistedTransport`) gives the condition `ThA`, and `sq_ratio_mem_range_emb_ll` puts each square ratio in the image of an embedding of a number field.
6. Each of the sixteen leaf conditions comes from one lemma. For example, `leafFixedPoint_of_finK_awayK` uses `FinK` and `AwayK`, `leafHeightMapBound_of_infK` uses `InfK`, and `leafInfinitePlaceBound_of_lamLow` is the one use of `LambdaLowerBound₂`.
7. `fun0Fit_of_leaves_alt` joins the sixteen leaves and calls `functional_lower_bound_of_conditions_numeric`, which proves the slope inequality for one side datum from the leaf bounds.

## In the Lean code

The theorem is in [FittedFunctionAtZeroClose.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FittedFunctionAtZeroClose.lean#L42). The main lemmas:

- `fun0Fit_of_leaves_alt`, `ConstantFunctionFits` and `BundleCondition` in [LeafInfinitePlaceBound.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LeafInfinitePlaceBound.lean#L83);
- `functional_lower_bound_of_conditions_numeric` in [FunctionalLowerBoundOfConditionsNumeric.lean](lean:Formalism/LocalToGlobal/IndefiniteForms/IndefiniteTree/FunctionalLowerBoundOfConditionsNumeric.lean#L1035);
- `Fld` in [SlopeTestRemainingChoicesAlt.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/SlopeTestRemainingChoicesAlt.lean#L81).

Each hypothesis is used. Several inputs are proved with no hypothesis: `cmThetaNormBoundHypotheses_satisfied`, `size_at'`, `bundle_of_rows_alt`, `scaling_function_bound'`, `desHLeaf_alt`, `rank_gap_bound`, `ramified_sum_bound'` and `polynomial_descent_estimate'`.

Two odd points. The conclusion quantifies over a real $C$, but the inequality does not depend on $C$: `IndefScale.num` sets the bound to $x^{C_H} b$ and leaves $C$ out. The name says "at zero" and "close", and neither word matches an object in the statement.
