---
id: mi-star-row-closing-alt-alt
title: The period row from published inputs and the point lines
kind: theorem
decl: GlobalTheory.miStarRowClosing_alt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.MainTheoremPublishedInputsVariant
covers: 10718
status: drafted
drafted_by: writer@claude
---
This theorem proves that the period datum `MIstar2` holds at the linked bundles of good points, from named literature hypotheses. It only passes its hypotheses on, and adds one row. The content is in [`main_theorem_published_results_final_alt_alt`](/entry/main-theorem-published-results-final-alt-alt/) and below it in [`miStar_row_alt_alt`](/entry/fam-mi-star-row-alt-alt/). Its only user is its renaming [`main_theorem_published_inputs_variant_alt_alt`](/entry/main-theorem-published-inputs-variant-alt-alt/), which [`miStarRow_alt_alt`](/entry/global-theory-mi-star-row-alt-alt/) calls.

## Statement

**Theorem.** Assume thirteen named propositions: Harish-Chandra finiteness, rapid decay of cusp forms, `DiscreteSeriesCover`, Harish-Chandra modules, Casselman-Wallach, `HoweUnram`, the Weil representation of a unitary pair, the Weil-Siegel formula, `SiegelWeilUnitaryConvergent`, the doubling method, unramified doubling for $\mathrm{GL}$, the classification of discrete series and strong approximation for $\mathrm{SU}$. Assume the diagonal row `RowDiag` for the predicate "`IsScaleWithBoundedGamma D L C'` and `RankMu D u` for all $u$". Let $h_L$ prove `RecTExists`, let $p$ be parameters for $h_L$, and suppose that each weighted point $q$ of $p$ has an element of `RXs q.x.what₂`. Then `RowE (IsGoodE p.s) (BundleLinkage p)` holds for the period identity `MIstar2`: for large parameters, at each point of the slot `IsGoodE p.s` and each bundle $b$ that `BundleLinkage p` links to it, `MIstar2` holds for $b$.

## Proof

The proof is one call of [`main_theorem_published_results_final_alt_alt`](/entry/main-theorem-published-results-final-alt-alt/) with all the hypotheses. That theorem needs one more input: the same `RowE` statement for `BundlePointConditions`. The proof gets it from `point_lines_of_cusp_rapid_decay`, with five of the hypotheses (`DiscreteSeriesCover`, Harish-Chandra modules, Casselman-Wallach, Harish-Chandra finiteness, rapid decay).

## In the Lean code

The theorem is in [MainTheoremPublishedInputsVariant.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MainTheoremPublishedInputsVariant.lean#L21). The lemmas it calls are `main_theorem_published_results_final_alt_alt` in [MainTheoremPublishedResultsFinal.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MainTheoremPublishedResultsFinal.lean#L43) and `point_lines_of_cusp_rapid_decay` in [BundlePackEqAdelicDataStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BundlePackEqAdelicDataStatement.lean#L16). Both are renamings: the first of `GlobalTheory.Fam.miStar_row_alt_alt`, the second of `good_linked_ptR_of_cuspRapidDecay`.

The name says "closing", but the theorem closes nothing. Its conclusion is a `RowE` statement, the input form of a row. We have not unfolded `BundlePointConditions`, `RXs`, `IsScaleWithBoundedGamma` or `RankMu`.
