---
id: s-fin-and-s-finl-of-theta-data-exists
title: The finiteness statements from theta data
kind: theorem
decl: GlobalTheory.HeightCounting.Fin3.sFin_and_sFinl_of_theta_data_exists
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.FinitenessOfHyp
covers: 731
status: drafted
drafted_by: writer@claude
---
This theorem gives a lattice point at every stage with a `StrictHenselianAcyclicLevel` datum, in two forms. It passes its inputs, stage by stage, to [the lattice point at a third level datum](/entry/lv3-of-third-alt-alt/), which has the real content. The result goes through [a relay](/entry/s-fin-and-s-finl-of-arch-cmp-s-eta-theta-data/) to item 6 of [the stage statements](/entry/all-stages-of-specializations-alt/), whose words we use.

## Statement

**Theorem.** Assume `WeilRepresentationUnitaryPair`, `DiscreteSeriesExists`, `PublishedInputsThirdLayerAlt`, $h_L \in$ `RecTExists`, `ArchimedeanComparison' hL`, `EtaStatement' hL` and `ThetaDataExists hL`. Then:

1. `FinitenessStatement hL`: at every stage $x$ of a datum $P$, for every `StrictHenselianAcyclicLevel` datum $l$ over $x$, every $S$ and every $\Gamma$, there is a lattice point $v$ of type `Lv3` at the parameters from `extensionWithLaw hL`, $S$ and $\Gamma$, with $v.\mathrm{Wt} = P.\mathrm{Wt}$ and its norm choice kept by the character choice of $l$.
2. For each real $c$, `FinitenessListStatement hL c`: the same for stages with `ListSt c x`, with `extensionWithList hL c`.

## Proof

`start_at_all_pre2` gives `RowsAt P`, and `StepW.and` joins it to the two assumed statements. At one stage, [the lattice point at a third level datum](/entry/lv3-of-third-alt-alt/) gives the point from `RowsAt P`, the eta statement at $l$, and theta data. In form 2, an element of `extensionWithList` pairs an element of `extensionWithLaw` with a `ListPin` from `ListSt c x`.

## In the Lean code

The theorem is in [FinitenessOfHyp.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FinitenessOfHyp.lean#L85). `ThetaDataExists` ([ThetaDataExists.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ThetaDataExists.lean#L40)) speaks of second level data. The proof uses it at a third level datum $l$, through `⟨l.toLI, l.b.toSeriesState⟩`. We have not unfolded `Lv3` or `Kept`.
