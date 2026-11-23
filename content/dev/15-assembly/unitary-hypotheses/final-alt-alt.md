---
id: final-alt-alt
title: The closed link bound from the closed bound at two and three
kind: theorem
decl: UpperTheory.GalC.final_alt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.CFinal
covers: 15614
status: drafted
drafted_by: writer@claude
---
This theorem is step 4 of branch 1 in [the unitary hypotheses chapter](/proof/unitary-hypotheses/). [Its caller](/proof/unitary-hypotheses/) uses it to turn the [closed bound](/step/closed-def/) for the bound at two and three into the closed bound for the link inequality `LinkN`. That result is the row `NL` of [the record HypsAlt](/step/hyps-alt-def/). The theorem is a wrapper: it supplies two hypotheses of [the main lemma](/entry/final-of-alt/), which has the content together with [the link bound for one family](/entry/link-n-of-tw-good-galois-preconditions/).

## Statement

The statement is the proposition `NLink.Final.mainTheorem`. Assume:

1. `Hypotheses₂`, a record of seven named inputs: Fontaine's ring $B_{\mathrm{cris}}$, global Artin reciprocity, a local Bloch-Kato input, a Bhatt-Scholze integrality input, and three local Galois cohomology inputs with the suffix K (Tate duality, Euler characteristic, finiteness);
2. the records `PublishedInputsThirdLayerAlt`, `GeometricGaloisRepCompatibility` and `SerN`, and the input `DepthZeroSupport`;
3. `LocalFiniteness`, `LocalTateDuality` and `LocalEulerChar`.

Then for each $h_L$ in `RecTExists` and each real $c$, let $p$ be the parameters `parametersOfDependence hL c`. If the closed bound for `BoundAtTwoThreeFamilyFonAlt` holds in the slot rows linked at $p$, then the closed bound for `LinkN` holds in the same form. [The main lemma](/entry/final-of-alt/) states both conditions in full.

The inputs of item 3, in `GalCoh.lean`, are other definitions than those with the suffix K. We have not compared them or unfolded any input.

## Proof

The proof applies `final_of_alt` and gives it two facts.

- `CutGivesAlt`: each datum $D$ with the Galois preconditions and the four tie conditions `Tie4` has a good cut with the norm choice facts and `Tie4`. This is `exists_good_cut_facts_tie4`, from the field `cheb` of the published inputs and the inputs of item 3.
- The Galois preconditions at every layer point: `galois_preconditions_at_mem`, from the inputs of items 2 and 3.

Every hypothesis is used. The rest is bookkeeping.

## In the Lean code

The theorem is in [CFinal.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CFinal.lean#L19). Its type is the abbreviation in [MainTyzTer.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MainTyzTer.lean#L22). It calls `final_of_alt` ([LinkNFam.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkNFam.lean#L75)), `exists_good_cut_facts_tie4` ([CFacts.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CFacts.lean#L58)) and `galois_preconditions_at_mem` ([PreAtMem.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PreAtMem.lean#L86)).

The closed bound hypothesis is redundant. The lemma `boundAtTwoThree_linked_of_recT` in [At23OfAll.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/At23OfAll.lean#L24) proves it from `Hypotheses₂` alone, at every parameter set. [The top caller](/step/nonempty-hyps/) gets it that way. The name has the suffix `_alt_alt`, and no object in the statement matches it.
