---
id: open-orbit-of-unramified-exponents-alt
title: The twelve open parameter statements from the unitary group hypotheses
kind: theorem
decl: GlobalTheory.Fc.S0.Open0ProofU.open_orbit_of_unramified_exponents_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.OpenOrbitOfUnramifiedExponents
covers: 12607
status: drafted
drafted_by: writer@claude
---
This theorem is branch 3 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). It proves the twelve row statements of `OpenParameterStatements` at the parameters of dependence, from the record of literature hypotheses. Its only user is [`open0_of_unitary_group_hypotheses`](/proof/unitary-hypotheses/), a renaming in the same file. The [top node](/step/nonempty-hyps/) calls that renaming, and branch 1 calls it again. Below this theorem are 12,607 declarations. Most of them (10,941) are below [`main_theorem_published_inputs_third_alt_alt`](/entry/main-theorem-published-inputs-third-alt-alt/), which gives the multiplicity row.

## Statement

**Theorem.** Let $P$ be a proof of [`UnitaryGroupThirdPlaceHypotheses`](/step/unitary-group-third-place-hypotheses-def/), let $h_L$ be a proof of `RecTExists`, and let $c_{\mathrm{Dep}} \in \mathbb R$. Write $p$ for `parametersOfDependence hL cDep`, that is, the parameters of the extension `extensionWithList hL cDep` with `SExt.none` and `geoCl anyGeometry`. Then `OpenParameterStatements p` holds.

`OpenParameterStatements p` is a structure of twelve fields. Each field is `LinkedAt p r` for one row statement $r$ (see section 5 of the chapter for `LinkedAt` and `Row`). The twelve rows are: primitivity, a lambda prime condition, a divisor condition, a decomposition point condition, a selection jump condition, a tie condition, a label condition, a goodness condition, a weak geometric compatibility, a multiplicity condition, a kappa condition, and the defect condition `RowDefectCondition`. The last is the row form of the [definite side condition](/step/definite-side-condition-def/).

## Proof

First, two small facts. Each element of `extensionWithList` gives an element of `extensionWithLaw` (its first component), and each weighted point of $p$ has the law `BkLaw` (read off from a field of the point). Then each row comes from one lemma, with fields of $P$ as inputs:

- primitivity, from `linkedAt_hPA_prmR`, and the decomposition point row, from `linkedAt_hDcPtG_prmR`, with no literature input;
- the tie row, from `linkedAt_tie_of_nonempty_extensionWithLaw`, with seven fields of $P$ (discrete series, Harish-Chandra theory, Casselman-Wallach, the Weil representation, rapid decay);
- the selection jump row, from `entries_combined_real_alt`, which also uses the three rows above;
- the multiplicity row, and a row that `MIstar2` holds at all selected bundles, from [`main_theorem_published_inputs_third_alt_alt`](/entry/main-theorem-published-inputs-third-alt-alt/), with thirteen fields of $P$ and the proved theorem `howeUnram_holds`;
- the divisor row, from `bk_law_entries_alt`, which uses `BkLaw` and the `MIstar2` row;
- the lambda prime row, from `real_group_inputs_combined_alt_alt`, and the kappa row, from `harish_chandra_inputs_combined_alt_alt`, which uses the lambda prime row;
- the goodness row, from `linked_bundles_good_of_local_langlands_alt_alt`, with the Green input made by `green_of_regular` from `greenRegularCharacters`; its first part gives the label row through `good_ft_entries_alt_alt`;
- the weak geometric row, from `linkedAt_geometricWeakTies_of_tie`, with `rayClassFieldSt`, the divisor row and the tie row;
- the defect row, from [`weil_unitary_entries'`](/entry/weil-unitary-entries-prime/).

The rest is bookkeeping.

## In the Lean code

The theorem is in [OpenOrbitOfUnramifiedExponents.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OpenOrbitOfUnramifiedExponents.lean#L39). `OpenParameterStatements` is in [GeometricWeakTies.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/GeometricWeakTies.lean#L39). We have not unfolded the twelve row predicates except the multiplicity row (see the entry of [`miStarRow_alt_alt`](/entry/global-theory-mi-star-row-alt-alt/)).

The name does not describe the statement. No open orbit and no unramified exponent appears in the hypotheses or the conclusion. The chapter notes the same.

All the lemmas are stated for any norm choice extension $N$, any $S$ and any geometry $\Gamma$. The proof uses them only with `extensionWithList`, `SExt.none` and `geoCl anyGeometry`. The hypothesis `HoweUnram` of the multiplicity lemma is not taken from $P$: the proof supplies the theorem `GlobalTheory.Hk3.howeUnram_holds`. The fields `siegelWeilUnitaryConvergent` and `siegelWeilUnitaryConvergent2` of $P$ have types with the same last name `SiegelWeilUnitaryConvergent`, in two namespaces and with different statements. Both go to the multiplicity lemma.
