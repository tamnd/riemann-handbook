---
id: concl-f-of-family-facts-and-bound-at-two-three
title: The family conclusion ConclF, the statement form
kind: theorem
decl: GlobalTheory.T.conclF_of_family_facts_and_bound_at_two_three
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ImportsFurtherTailStatement
covers: 9873
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It states the result of [the closing theorem for ConclF](/entry/nlink-close-main-alt-alt/) and proves it by calling that theorem. The real content is in that entry. Its only user is [LinkN for one family by a cut of each datum](/entry/link-n-of-tw-good-galois-preconditions/), which applies it to the cut family.

## Statement

Assume `Hypotheses₂`. Let $F$ be a family with parameter $\varepsilon$, let $C \ge 0$ be real and $C_T$ a natural number. Assume `TwGood F`, `FactsFAlt F C CT` and `BoundAtTwoThreeFamilyFonAlt F`. Then `ConclF F` holds.

[The closing theorem for ConclF](/entry/nlink-close-main-alt-alt/) says what each of these predicates means.

## Proof

The proof is `first | exact @GlobalTheory.NLinkClose.main_alt_alt | ...`. It applies that theorem. The two statements are the same, word for word.

## In the Lean code

The theorem is in [ImportsFurtherTailStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ImportsFurtherTailStatement.lean#L11). It is used once, in [LinkNFam.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkNFam.lean#L51). There the hypothesis `BoundAtTwoThreeFamilyFonAlt` is not an input of the caller: the caller proves it with `at23_family_alt` from `Hypotheses₂` alone.
