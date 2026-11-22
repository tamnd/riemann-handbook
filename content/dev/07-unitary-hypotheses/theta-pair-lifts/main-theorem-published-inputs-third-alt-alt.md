---
id: main-theorem-published-inputs-third-alt-alt
title: The multiplicity row at the parameters of an extension, renamed
kind: theorem
decl: GlobalTheory.T.main_theorem_published_inputs_third_alt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.MainTheoremPublishedInputsThird
covers: 10941
status: drafted
drafted_by: writer@claude
---
This theorem is a copy of [`miStarRow_alt_alt`](/entry/global-theory-mi-star-row-alt-alt/) under a second name. Its only user is [branch 3](/entry/open-orbit-of-unramified-exponents-alt/), which takes the multiplicity row and the `MIstar2` row from it. Below this theorem are 10,941 declarations, one more than below the copy.

## Statement

The statement is the statement of [`miStarRow_alt_alt`](/entry/global-theory-mi-star-row-alt-alt/), word for word. Assume the fourteen named propositions listed there (Harish-Chandra theory, rapid decay, `HoweUnram`, the Weil representation, Siegel-Weil twice, the doubling method, discrete series, strong approximation). Let $h_L$ prove `RecTExists`, and let $N$, $S$ and $\Gamma$ be a norm choice extension, an S-extension and a geometry, with parameters $p$. Then `LinkedAt p` holds for the row "`MIstar2` at every selected bundle", and `LinkedAt p RowMultiplicityCondition` holds.

## Proof

The proof is `exact miStarRow_alt_alt`, inside a `first | … | …` tactic that tries three forms of the same call. There is no other content.

## In the Lean code

The theorem is in [MainTheoremPublishedInputsThird.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MainTheoremPublishedInputsThird.lean#L34), and the copy at [line 22](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MainTheoremPublishedInputsThird.lean#L22) of the same file.

The name does not describe the statement. It is not a main theorem, and "third" matches nothing in the statement. The [unitary hypotheses chapter](/proof/unitary-hypotheses/) lists this theorem as the largest part of branch 3; the content is in the copy and in [`miStarRowClosing_alt_alt`](/entry/mi-star-row-closing-alt-alt/).
