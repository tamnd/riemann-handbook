---
id: row-r-rows-stage0-alt
title: The definite rows from nine rows and two estimates
kind: theorem
decl: GlobalTheory.Fc.StageZeroRow.row_rRows_stage0_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.TupAllUsedAtPart
covers: 660
status: drafted
drafted_by: writer@claude
---
This theorem proves the row `SlotDefiniteRowsCondition DefiniteSideCondition Q Lk`. It is step 7 of [`allRows_of_open0_alt`](/entry/all-rows-of-open0-alt/), where it gives the field `rRows` of the record `AllRowsAlt`, and through it the field `rRows` of [HypsAlt](/step/hyps-alt-def/). Most of the 660 declarations below it are in [`indefinite_scale_theta_nonvanishing_alt`](/entry/indefinite-scale-theta-nonvanishing-alt/) (482).

## Statement

Let $Q$ be a slot and $L_k$ a linkage of bundles. A *row* `Row Q Lk H` is as in [`allRows_of_open0_alt`](/entry/all-rows-of-open0-alt/).

**Theorem.** Assume the named results `DiscreteSeriesCover`, `HarishChandraModules`, `CuspRapidDecay`, `CasselmanWallach` and `DiscreteSeriesClassification`, and the two estimates `SurjectiveOntoX` and `LambdaLowerBound₂` of [branch 2](/proof/unitary-hypotheses/). Assume nine rows at $(Q, L_k)$: primitivity, divisor, goodness, weak geometric compatibility, covolume (an $L^3$ bound), functional, multiplicity, kappa and defect. Then the row `SelectionDefiniteRows DefiniteSideCondition` holds at $(Q, L_k)$.

`SelectionDefiniteRows DR 𝒜 σ` says: it is [closed](/step/closed-def/) on `D3 3 𝒜` that there is $C \ge 0$ such that, eventually along the selection $\sigma$, each selected bundle $b$ has the constant bounds `IndefiniteRealisationConstantBounds` at $C$ and satisfies $\mathrm{DR}(b, C, C_H)$. The constant bounds are nine fields: `w1`, `covol`, `onto`, `lamLow`, `seeIso`, `miStar`, `fun0`, `pass` and `kap`.

## Proof

1. `row_rRows_of_parts_alt` reduces the theorem to four rows: one row with five eventual bounds on a compatible selection of point summands, and the multiplicity, kappa and defect rows. It takes the largest of the six constants and the largest of the eight thresholds. The defect row is the [definite side condition](/step/definite-side-condition-def/) itself, so that part of the conclusion is a hypothesis.
2. The first six rows are joined with `Row.and`. The weak geometric compatibility row gives, by choice, a compatible selection $\tau$ whose point summands satisfy `IotaPointSummands`, `ClassSumPin`, the compatibility conditions and `More`.
3. `eventually_pDiv_ties_of_class_sum_pin` gives the point conditions `RowPointSummands`, from the first four named results, primitivity, divisor and goodness. `p_div_at_piece_of_div3g` converts the divisor row first.
4. `eventually_norm_bound_of_more_points` gives the norm bound from `SurjectiveOntoX`, and `eventually_L6_bound_of_lamLow` gives the $L^6$ bound from `LambdaLowerBound₂`.
5. `eventually_small_of_seeEx_primitive` gives the small bounds from primitivity and `IndefiniteRealisationExtends` at each point summand. The latter is [`indefinite_scale_theta_nonvanishing_alt`](/entry/indefinite-scale-theta-nonvanishing-alt/), from `DiscreteSeriesClassification`.
6. The $L^3$ and functional bounds are the covolume and functional rows.

The rest is bookkeeping.

## In the Lean code

The theorem is at [TupAllUsedAtPart.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TupAllUsedAtPart.lean#L46). `row_rRows_of_parts_alt` is at [RowRRowsOfParts.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowRRowsOfParts.lean#L21), `SelectionDefiniteRows` at [CountsIrreducibilityConstants.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CountsIrreducibilityConstants.lean#L91). The four `eventually_` lemmas are one-line renamings of `evW_pRows_of_rows_alt`, `onto_at_chosen_alt`, `eventual_L6_of_lower_scalar_alt` and `small_along_alt`.

Odd points:

- Each hypothesis is used, but the definite side part of the conclusion is the hypothesis `RowDefectCondition` passed on.
- The name says "stage 0"; the file is named after the helper `tupAllUsed_at_part_alt` (line 30).
