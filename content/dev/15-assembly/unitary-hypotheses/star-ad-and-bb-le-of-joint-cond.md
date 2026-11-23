---
id: star-ad-and-bb-le-of-joint-cond
title: The middle range bounds StarAD and BBLe, the statement form
kind: theorem
decl: GlobalTheory.T.star_ad_and_bb_le_of_joint_cond
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.RowsADInSettingStatement
covers: 3410
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It states the result of [the middle range bounds in the setting](/entry/rows-ad-in-setting-alt/) and proves it by calling that theorem. The real content is in that entry. Its only user is [the closing theorem for ConclF](/entry/nlink-close-main-alt-alt/), which gets from it the fields `mid` and `bb` of `Concl`.

## Statement

Assume `Hypotheses₂`. Let $D$ be a datum with size data $L$, a parameter choice $P$, a norm choice $n$, local data `HW`, `F`, `Cm`, hub data $X$ and a real $C_2$. Assume that $X$ is in setup (`SetupAlt L n HW X C₂`), that $C_2 \ge 1$, that `Conclusion2 D C₂` holds, and that the joint hub conditions `JointParametersHubConditions L HW X (rowC C₂)` hold. Then `StarAD L X` and `BBLe L X 7200` hold.

[The middle range bounds in the setting](/entry/rows-ad-in-setting-alt/) says what each of these predicates means.

## Proof

The proof is `first | exact @GlobalTheory.NLink.rowsAD_in_setting_alt | ...`. It applies that theorem. The two statements are the same, word for word.

## In the Lean code

The theorem is in [RowsADInSettingStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowsADInSettingStatement.lean#L11). It is used once, in [ImportsFurtherTail.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ImportsFurtherTail.lean#L64).
