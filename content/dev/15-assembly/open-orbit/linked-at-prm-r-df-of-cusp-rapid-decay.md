---
id: linked-at-prm-r-df-of-cusp-rapid-decay
title: The defect row at the parameters of an extension
kind: theorem
decl: GlobalTheory.Fc.RL.linkedAt_prmR_df_of_cuspRapidDecay
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.PointEvaluationSide
covers: 1186
status: drafted
drafted_by: writer@claude
---
This theorem gives the defect row `RowDefectCondition` at the parameters of an extension. Its only user is the restatement [`weil_unitary_entries'`](/entry/weil-unitary-entries-prime/), which gives the last of the twelve open parameter statements in [`open_orbit_of_unramified_exponents_alt`](/entry/open-orbit-of-unramified-exponents-alt/), branch 3 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). The theorem drops its four named hypotheses and applies [`linkedAt_df_of_parameters`](/entry/linked-at-df-of-parameters/), which has the real content (1,185 of 1,186 declarations).

## Statement

**Theorem.** Assume `WeilRepresentationUnitaryPair`, `DiscreteSeriesExists`, `HarishChandraFinite` and `CuspRapidDecay`. Let $h_L$ be a proof of `RecTExists`, $N$ a norm choice extension for $h_L$, $S$ an `SExt` and $\Gamma$ a `GeoP`. Let $p$ = `parametersOfExtension N S Γ`, the parameters with position `RX` and parts $N, S, \Gamma$. Then `LinkedAt p RowDefectCondition`.

Here `LinkedAt p r` is `Lg1 KPx (IsBuiltE p.s) (IsGoodE p.s) (fun S => r S (BundleLinkage p))`: there is a further slot $R$ with the large base condition, and the row $r$ holds on the slot $Q' \wedge R$ for the bundle linkage of $p$ ([`Lg1`](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/AllRows.lean#L15)). `RowDefectCondition Q Lk` is the row statement `Row Q Lk (EvWC (fun _ => True) q)` with

$$q(C, C_H)(D, O, c, b) = \mathrm{DefiniteSideCondition}\ D\ O\ c\ b\ C\ C_H.$$

So for each admissible selection $\sigma$ of bundles on a class $\mathcal A$: in the sense of `Closed` on the class `W3 𝒜`, each large family has a constant $C_0 \ge 0$ such that for all $C \ge C_0$, eventually in $x$, every selected bundle $b$ satisfies the [definite side condition](/step/definite-side-condition-def/) at $(C, C_H)$.

## Proof

The proof is one term:

```
fun _ _ _ _ _ N S Γ => linkedAt_df_of_parameters (parametersOfExtension N S Γ)
```

`linkedAt_df_of_parameters` proves `LinkedAt p RowDefectCondition` for every `Parameters hL`, with no named hypothesis. The rest is bookkeeping.

## In the Lean code

The theorem is at [PointEvaluationSide.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PointEvaluationSide.lean#L85). `linkedAt_df_of_parameters` is at [line 65](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PointEvaluationSide.lean#L65). `RowDefectCondition` and `LinkedAt` are at [RowGood.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowGood.lean#L36), and `EvWC` at [BaseRankDimension.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/BaseRankDimension.lean#L90).

Odd points:

- The four hypotheses `WeilRepresentationUnitaryPair`, `DiscreteSeriesExists`, `HarishChandraFinite` and `CuspRapidDecay` are bound by `_` and never used. So is $h_L$.
- The name says "of cusp rapid decay", but rapid decay of cusp forms plays no part in the proof.
- The theorem is a special case of `linkedAt_df_of_parameters`: it states the result only for parameters of the form `parametersOfExtension N S Γ`.
