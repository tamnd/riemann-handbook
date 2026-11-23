---
id: conclusion41-of-p-adic-hodge-alt
title: The congruence length bound at one datum, restated
kind: theorem
decl: GlobalTheory.T.conclusion41_of_pAdicHodge_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.AdmG14OfAuxStatement
covers: 3256
status: drafted
drafted_by: writer@claude
---
This theorem is a copy of [`ClosingLocalInputs.main_alt_alt`](/entry/closing-local-inputs-main-alt-alt/) under a second name. It proves the bound `PairedCharacterConditionAlt D C CT` at one datum $D$: at each local index, the length of a congruence module is at most a weighted sum of local terms. Its user is [`NormFromFacts.main_alt_alt`](/entry/norm-from-facts-main-alt-alt/), in branch 1 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). Below this theorem are 3,256 declarations, one more than below the copy.

## Statement

The statement is the statement of the copy, word for word. Assume six named inputs (`GlobalArtinReciprocity`, `BhattScholzeIntegral`, `FontaineBcris`, `BlochKatoLocal`, `LocalTateDualityK`, `LocalEulerCharK`). Let $D$ be a datum with local data $HW$, $F$, $Cm$, and let $C_T \ge 40$ and $8 C_T \le C$. Assume a pending datum $P$ with `admDZ P` and `EigSpan P`, and twelve named conditions on $D$. Then `PairedCharacterConditionAlt D C CT`. The entry of the copy says what the bound is.

## Proof

The proof is `exact ClosingLocalInputs.main_alt_alt`, inside a `first | … | …` tactic that tries three forms of the same call. There is no other content.

## In the Lean code

The theorem is in [AdmG14OfAuxStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AdmG14OfAuxStatement.lean#L12). It sits in the namespace `GlobalTheory.T` and the copy in `GlobalTheory.ClosingLocalInputs`.

The name does not match the conclusion. No object named "conclusion 41" appears in it; the number 41 occurs only in the hypothesis `provisionFortyOne`. The words "p-adic Hodge" fit the hypotheses `BhattScholzeIntegral`, `FontaineBcris` and `BlochKatoLocal`, but we have not checked these against the literature.
