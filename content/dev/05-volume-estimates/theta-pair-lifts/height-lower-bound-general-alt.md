---
id: height-lower-bound-general-alt
title: A lower bound for the heights of the cover components
kind: theorem
decl: SelfIntersectionVolumeEstimates.height_lower_bound_general_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.HeightLowerBoundGeneral
covers: 1865
status: drafted
drafted_by: writer@claude
---
This theorem proves `HeightCondition`, a lower bound for the heights of the components of a good cover. It is the step where the positivity statement $\mathsf{DeepStR}$ of [deep_slim_use](/entry/deep-slim-use/) enters the [covolume bound](/entry/top-covol-g-alt-alt/). Its only caller is that theorem, which feeds the result to a uniform lower bound for slopes. Below it are 1,865 declarations.

## Statement

We use the level and cover statements of [the covolume bound](/entry/top-covol-g-alt-alt/). Fix a point $p$, a level $i$ with $i + 1 < m$, a good cover $Y$ and a weight $u$ that satisfies the quotient condition `Quo`. Let $L$ be the integer `lenT`, $d$ the flag dimension, $\rho$ the number `rhoB` of $u$ and $h(Z)$ the height of $u$ on a component $Z$ of $Y$. Then `HeightAt` with constant $C$ says: there are $c_s, c_c, X \ge 0$ and a function $s$ on the components with

$$h(Z) + c_s \ge 0, \qquad (1 - \rho)\max(0, s(Z) + c_s) \le h(Z) + c_s + c_c, \qquad -X \le \frac{1}{\#\{Z\}} \sum_Z s(Z),$$

and $L X$, $L c_c$ and $c_s(6d + 10 + L(\mathrm{zed} + 2\rho))$ are at most $C\,\mathrm{unitE}$.

**Theorem.** Suppose $\mathsf{VolumeEstimateHypotheses}$, $\mathsf{HypothesesX}$, `GrothendieckDeformation`, `Quoted`, `PublishedHodgeBundleTheorems`, $\mathsf{HypothesesH}$ and $\mathsf{DeepStR}$, and the cover statements `DeepGoodness`, `SizeCondition`, `CoverDegree` and `FlatDegreeCondition`. Then `HeightCondition` holds: `HeightAt` holds for all such $p, i, Y, u$, with one constant $C$.

## Proof

The proof is one call of `height_of_meanAll_bound`. That theorem needs four more cover statements, and the proof supplies them.

1. `ShortAlt`, short generators of the cusp lattices, from `covering_short_of_deep_size_flatDeg`.
2. `GeometricCondition`, goodness, birationality and a degree bound on each component, from `covHt_geom_of_siegel_toroidal_semiAbelian`.
3. `MultiplicityConstantCondition`, from `carrying_section_integral_frame_alt` applied to [refW_of_prints_deepGood_size_flatDeg](/entry/ref-w-of-prints-deep-good-size-flat-deg/) and to `exists_section_bounded_by_bergman_kernel_alt`.
4. `ErrorBudgetCondition`, from `budget_of_hostN_of_liftWeight_of_size`, `hostN_forall` and `lift_weight_numerator`.

Inside `height_of_meanAll_bound`, $\mathsf{DeepStR}$ gives `MeanAll` for $Y$ at level $i + 1$: a lower bound for the mean volume slope of the components. Then `heightAt_eq_of_cover` turns that mean bound and the four conditions into `HeightAt`, with constant $C_s + C_m + C_b + C_0 C_b$. The rest is bookkeeping with `Closed.and`.

## In the Lean code

The theorem is at [HeightLowerBoundGeneral.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/HeightLowerBoundGeneral.lean#L21). The proof is one term.

- `height_of_meanAll_bound` is in [HeightOfSteps.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/HeightOfSteps.lean#L19). Its last hypothesis is written out in full, and it is the definition of $\mathsf{DeepStR}$.
- `heightAt_eq_of_cover` is in [HeightAddLogNonneg.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/HeightAddLogNonneg.lean#L66). Its name says "eq", but its conclusion is the inequalities of `HeightAt`.
- `Quoted` and `GrothendieckDeformation` are used only in step 2.
- We have not unfolded `Mult`, `IsShortGen`, `delPrime` or the height `Y.ht`.
