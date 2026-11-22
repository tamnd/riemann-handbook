---
id: all-rows-of-open0-alt
title: All rows of the record from the open parameter statements
kind: theorem
decl: GlobalTheory.Fc.AllAtMemberStage0.allRows_of_open0_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.LinkROfIsLinked
covers: 33892
status: drafted
drafted_by: writer@claude
---
This theorem fills the 26 rows of the record `AllRowsAlt`. It is the last large step of [the proof that HypsAlt is nonempty](/proof/unitary-hypotheses/), branch 1 of [the unitary hypotheses node](/proof/unitary-hypotheses/). There `nonempty_hyps_of_allRows_alt` reads the fields of [HypsAlt](/step/hyps-alt-def/) off these rows. Most rows come from the twelve open parameter statements. Two parts have large proofs: three rows from one Siegel-Weil hypothesis, and the service row from global Artin reciprocity.

## Statement

Three notions of the Lean code:

- `Row Q Lk H`, for a slot $Q$ (a predicate on points) and a linkage $L_k$ (a predicate on bundles at points): there is a property $E$ of bundles that, eventually, each bundle at a point of $Q$ linked by $L_k$ has; and $H(\mathcal A, \sigma)$ holds for each family class $\mathcal A$ and each selection $\sigma$ of such bundles with property $E$.
- `Lg1 KP Q Q' r`: there is a slot $R$ with `LargeBaseCondition KP Q R` and $r(Q' \wedge R)$.
- `LinkedAt p r` is `Lg1 KPx (IsBuiltE p.s) (IsGoodE p.s) (fun S => r S (BundleLinkage p))`.

**Theorem.** Assume the seven named results `GlobalArtinReciprocity`, `SiegelWeilUnitaryConvergent` (in `HeckeCharacterZeroLocus.SiegelWeilU`), `DiscreteSeriesCover`, `HarishChandraModules`, `CuspRapidDecay`, `CasselmanWallach`, `DiscreteSeriesClassification`, and the two estimates `SurjectiveOntoX` and `LambdaLowerBound₂`. Let $h_L$ witness [RecTExists](/step/rect-exists-def/), let $p$ = `parametersOfExtension N S Γ`, and let $\mathcal N$ be any predicate on family classes. Assume `OpenParameterStatements p` (twelve statements `LinkedAt p r`) and three more statements `LinkedAt p r`: the covolume bound, the functional condition and the norm row for $\mathcal N$. Then `AllRowsAlt KPx (IsBuiltE p.s) (IsGoodE p.s) (BundleLinkage p) 𝒩 DefiniteSideCondition` holds.

Each field of this record is a statement `LinkedAt p r` for one row $r$. The field `rRows` carries the [definite side condition](/step/definite-side-condition-def/).

## Proof

1. **Copied.** `hPA`, `hLamP`, `hDivG`, `hDcPtG` and `selJ` are fields of `OpenParameterStatements p`. `nRest` is the hypothesis on $\mathcal N$.
2. **One step from an open statement.** `row_jOn_of_row_hPA_alt` and `zL_of_hPA` give `jOn` and `zL` from the primitivity row, `row_hTw_of_tie_alt` gives `hTw` from the tie row, and `row_counts_of_labels_alt` gives `c30` from the label row and Siegel-Weil.
3. **No hypothesis.** `classCountBound_paramsLambda_constructedPoints` gives `hn4`, `divisionSecondComplement_constructedPoints` gives `aC2`, `row_aAtG_at_built_alt` gives `aAtG`, and [`period_entries_tie_and_level_valuations_at_built`](/entry/period-entries-tie-and-level-valuations-at-built/) gives six fields.
4. **Siegel-Weil.** `volumeRatio` and `row_hInstR_of_hU` give `hInstR`. [`lg1_sLp_sO_hTF`](/entry/lg1-s-lp-s-o-h-tf/) gives `sLp`, `sO` and `hTF`.
5. **Representation theory.** `row_hRB_univ_alt` gives `hRB` from `DiscreteSeriesCover`, `HarishChandraModules`, `CuspRapidDecay` and `CasselmanWallach`.
6. **Artin reciprocity.** `linkR_of_isLinked'` shows that a bundle linked by `BundleLinkage p` has its reciprocity record linked by `ReciprocityLinkage p`. Then [`hServ_of_linkR`](/entry/h-serv-of-link-r/) and `LinkedAt.of_row` give `hServ`.
7. **Definite rows.** `forall_linked_bundles_and_alt` (a copy of `RowL.and`) joins nine rows: primitivity, divisor, goodness, weak geometric compatibility, covolume, functional, multiplicity, kappa and defect. `row_rRows_stage0_alt` gives `rRows` from this row, the five other named results and the two estimates.

The rest is bookkeeping.

## In the Lean code

The theorem is at [LinkROfIsLinked.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkROfIsLinked.lean#L50), the record at [AllRows.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AllRows.lean#L12), and `Lg1` at [AllRows.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/AllRows.lean#L15). The largest parts are `lg1_sLp_sO_hTF` (13,601 declarations), `hServ_of_linkR` (10,829), `period_entries_tie_and_level_valuations_at_built` (3,302) and `row_counts_of_labels_alt` (2,598). Each hypothesis is used.

Odd points:

- `largeBaseProperty_true` proves `LargeBaseCondition KP Q R` for the slot $R$ that is always true. So `Lg1 KP Q Q' r` follows from $r(Q' \wedge \mathrm{True})$, and `LinkedAt.of_row` uses this. In these uses the large base condition asks for nothing.
- The nine fields of step 3 have no hypothesis. We have not unfolded those rows, so we do not know if they are trivial.
- $\mathcal N$ is arbitrary, and `nRest` only passes its hypothesis on. The caller sets $\mathcal N$ = `NL`.
- The file is named after the helper `linkR_of_isLinked'` (line 45), not after this theorem.
