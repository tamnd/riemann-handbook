---
id: aux-of-ok-of-pins
title: The forms map at true columns, a second name
kind: theorem
decl: GlobalTheory.T.aux_of_ok_of_pins
module: Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.FormsMapAtEveryTrueColumnMemberStatement
covers: 456
status: drafted
drafted_by: writer@claude
---
This theorem is a second name of [the forms map at every true column member](/entry/forms-map-at-every-true-column-member/). It has no content of its own. Its only user is [the forms map at a bundle point over true columns](/entry/constructed-point-reference-chain-word-forms-map/), which applies it at the column datum under a constructed point.

## Statement

Let $B$ be a base, $X$ a `PreX` over it, and $I$ a true column input (`TC B X`, which is `ColIn B X`). Assume `I.Ok` and the pins `TC.Pins B X`. Let $l$ be the laws `I.Laws`, and $Z$ later stages over the columns `I.cols l`. Let $D$ be the assembled datum `I.rec7 l Z`. Then `Conclusion6 D u` holds for every word $u$ of $D$.

[The forms map from a symmetric comparison](/entry/forms-map-of-symmetric-comparison-lower-map-finite-char/) says what `Conclusion6` means.

## Proof

The proof is `first | exact @GlobalTheory.Mem.Col2.TC.formsMap_at_every_trueColumnMember | ...`. The two statements are the same, word for word.

## In the Lean code

The theorem is in [FormsMapAtEveryTrueColumnMemberStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/FormsMapAtEveryTrueColumnMemberStatement.lean#L8). It is used once, in [ReferenceChainEvaluationBundlePointsOverColumnsA.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/ReferenceChainEvaluationBundlePointsOverColumnsA.lean#L15).

The name "aux of ok of pins" names two hypotheses and nothing of the conclusion.
