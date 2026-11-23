---
id: exists-bound-tie-chi-of-prints
title: The congruence length bound from the norm choice facts, restated
kind: theorem
decl: GlobalTheory.T.exists_bound_tieChi_of_prints
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ImportsFurtherLastStatement
covers: 3258
status: drafted
drafted_by: writer@claude
---
This theorem is a copy of [`NormFromFacts.main_alt_alt`](/entry/norm-from-facts-main-alt-alt/) under a second name. It gives one constant $C_T$ for which the congruence length bound `PairedCharacterConditionAlt D (8 C_T) C_T` holds at each datum $D$ with the norm choice facts and the four ties. Its user is [`ExtraFromFacts.main_alt_alt`](/entry/extra-from-facts-main-alt-alt/), below [the bound LinkN for one family](/entry/link-n-of-tw-good-galois-preconditions/) in branch 1 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). Below this theorem are 3,258 declarations, one more than below the copy. The content is in [`ClosingLocalInputs.main_alt_alt`](/entry/closing-local-inputs-main-alt-alt/).

## Statement

The statement is the statement of the copy, word for word. Assume `Hypotheses₂`, the record of seven named inputs of `GlobalTheory.NLink`. Then there is $C_T \in \mathbb N$ such that for each datum $D$ and norm choice $n$ with `NormChoiceFacts D n` and `Tie4 D`, the bound `PairedCharacterConditionAlt D (8 C_T) C_T` holds. The statement writes `Tie4 D` out as its four parts: `tieChi`, a pending datum $P$ with `admDZ P` and `EigSpan P`, `TieInePoly` and `SerLoc`.

## Proof

The proof is `exact NormFromFacts.main_alt_alt`, inside a `first | … | …` tactic that tries three forms of the same call. There is no other content.

## In the Lean code

The theorem is in [ImportsFurtherLastStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ImportsFurtherLastStatement.lean#L12). It sits in the namespace `GlobalTheory.T` and the copy in `GlobalTheory.NormFromFacts`.

The name is partly misleading. `tieChi` is one of the hypotheses, not the subject of the bound. The word "prints" matches no object in the statement. The copy proves the statement with $C_T = 40$, so the existential hides a fixed number.
