---
id: adm-at-inert-of-range
title: The local conditions at inert primes of the middle range, the statement form
kind: theorem
decl: GlobalTheory.T.adm_at_inert_of_range
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ImportsFurtherBisStatement
covers: 3370
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It states the result of [the inert step](/entry/inert-step-main-alt-alt/) and proves it by calling that theorem. The real content is in that entry. Its only user is [the middle range bounds in the setting](/entry/rows-ad-in-setting-alt/), where it fills the field for inert primes of the step data `StepAD`.

## Statement

Take the data and the hypotheses of [the middle range bounds in the setting](/entry/rows-ad-in-setting-alt/): `Hypotheses₂`, a datum $D$ with size data $L$ and hub data $X$ in setup, $C_2 \ge 1$, `Conclusion2 D C₂` and the joint hub conditions for `rowC C₂`. Let $i$ be a twisted local index of $D$ with prime $\ell_i$. Assume that $\ell_i$ is not one of the two primes $g_0, g_1$, that $\ell_i$ is in the middle range (`RangeAD`: not small, not $3$, not $q$ or $d$, and not both above $\ell^*$ and outside the excluded set), and that $\ell_i$ is inert (`InertK`). Then at each good point $\pi$ of $i$, the condition `admitted` holds for the hub data $X$ at $i$.

`admitted` is a conjunction of 20 named local conditions. We have not unfolded most of them.

## Proof

The proof is `first | exact @GlobalTheory.NLink.InertStep.main_alt_alt | ...`. It applies that theorem. The two statements are the same, word for word.

## In the Lean code

The theorem is in [ImportsFurtherBisStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ImportsFurtherBisStatement.lean#L11). It is used once, in [RowsADInSetting.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowsADInSetting.lean#L21). In the target theorem, one of the 20 conditions, `LiftExponentAtPlaces`, holds for an empty reason: it quantifies over a set of places that is empty at inert primes ([ImportsFurtherBis.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ImportsFurtherBis.lean#L46)).
