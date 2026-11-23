---
id: exists-inputs-of-gal-hodge-n-roots
title: A second name for the inputs of the twist theorem
kind: theorem
decl: GlobalTheory.T.exists_inputs_of_galHodgeN_roots
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.InputsOfSidesStatement
covers: 561
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`exists_inputs_of_hkSup_galHodge`](/entry/exists-inputs-of-hk-sup-gal-hodge/). Its statement is the same, and its proof applies that theorem. Its only user is [`exportAt_of_bundles_alt`](/entry/export-at-of-bundles-alt/), where step 1 takes from it the integers $N_0$ and the record `Inputs D E N0` of 21 facts. The content is in the entry for `exists_inputs_of_hkSup_galHodge`.

## Statement

Assume `ChebotarevDegreeOne`, `GlobalArtinReciprocity` and `ToricDenominator`. Let $D$ be a datum, $X$ a real side, $E$ an element of `XD D`, $Y$ a series side over $X$ and $E$, and $G$ a Galois side (`GalSideAlt D`). Assume the rational rows `RatRow` at each index with a nonzero index place, the bound `XiBdd`, the Hecke support condition `HkSupAt` at each $j$, `GalHodgeN D G.wd`, and that each root of unity of order dividing $g_k(g_k - 1)$ lies in the image of the field `LL0`. Then there is $N_0$ with `Inputs D E N0`.

Each object is explained in [`exists_inputs_of_hkSup_galHodge`](/entry/exists-inputs-of-hk-sup-gal-hodge/).

## Proof

The proof is `exact exists_inputs_of_hkSup_galHodge`, wrapped in the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)`.

## In the Lean code

The theorem is at [InputsOfSidesStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/InputsOfSidesStatement.lean#L15). It calls `GlobalTheory.TwInputs.exists_inputs_of_hkSup_galHodge` ([InputsOfSides.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/InputsOfSides.lean#L15)).

The two names describe different hypotheses. This one names `GalHodgeN` and the roots of unity; the other names `HkSupAt` and `GalHodgeN`. Both theorems take all of them.
