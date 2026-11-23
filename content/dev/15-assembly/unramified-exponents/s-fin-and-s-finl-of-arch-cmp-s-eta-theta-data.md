---
id: s-fin-and-s-finl-of-arch-cmp-s-eta-theta-data
title: The finiteness statements, the relay in the namespace T
kind: theorem
decl: GlobalTheory.T.sFin_and_sFinl_of_archCmp_sEta_thetaData
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.FinitenessOfHyp
covers: 732
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It has the same statement as [the finiteness statements from theta data](/entry/s-fin-and-s-finl-of-theta-data-exists/), in the same file, and it proves it by calling that theorem. The real content is in [the lattice point at a third level datum](/entry/lv3-of-third-alt-alt/). The user is [the stage statements from the published inputs](/entry/all-stages-of-specializations-alt/), which takes from it item 6 and its list form.

## Statement

Assume `WeilRepresentationUnitaryPair`, `DiscreteSeriesExists`, `PublishedInputsThirdLayerAlt`, an element $h_L$ of `RecTExists`, and the statements `ArchimedeanComparison' hL`, `EtaStatement' hL` and `ThetaDataExists hL`. Then `FinitenessStatement hL` holds, and `FinitenessListStatement hL c` holds for each real $c$. [The finiteness statements from theta data](/entry/s-fin-and-s-finl-of-theta-data-exists/) says what they mean.

## Proof

The proof is

```
first | exact @GlobalTheory.HeightCounting.Fin3.sFin_and_sFinl_of_theta_data_exists | ...
```

The two statements are the same text, so the first branch closes the goal.

## In the Lean code

The theorem is in [FinitenessOfHyp.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FinitenessOfHyp.lean#L102). It differs from the original only in the namespace and in the option `maxHeartbeats 1000000`. The name lists three of the seven hypotheses.
