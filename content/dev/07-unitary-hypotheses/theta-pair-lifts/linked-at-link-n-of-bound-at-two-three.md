---
id: linked-at-link-n-of-bound-at-two-three
title: The closed link bound in linked form
kind: theorem
decl: UpperTheory.GalC.linkedAt_linkN_of_boundAtTwoThree
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.LinkNFam
covers: 14244
status: drafted
drafted_by: writer@claude
---
This theorem moves [the slot form of the link bound](/entry/link-n-of-bound-at-two-three-slot/) to statements that are linked at a parameter set. Its only work is to join two large base conditions and to adjust the slots of the two hypotheses. Its caller is [the closed link bound, given a cut](/entry/final-of-alt/). The real content is in [the link bound for one family](/entry/link-n-of-tw-good-galois-preconditions/).

## Statement

A *slot* is a condition on the data of a base (columns, rows, stages and a core). Let $p$ be a parameter set over $h_L$ in `RecTExists`. A statement $r$ about a slot is *linked at* $p$ (`LinkedAt p r`) when there is a slot $R$ such that:

1. `LargeBaseCondition KPx (IsBuiltE p.s) R` holds: eventually, for every base that satisfies `KPx`, each core in the slot `IsBuiltE p.s` is in $R$;
2. $r$ holds for the slot "`IsGoodE p.s` and $R$" with the bundle linkage of $p$.

We have not unfolded `EvLg`, `KPx`, `IsBuiltE`, `IsGoodE` or the bundle linkage.

**Theorem.** Assume `Hypotheses₂` and `CutGivesAlt`. Let $p$ be a parameter set over $h_L$. Suppose that the following two statements are linked at $p$:

1. the row statement `RowE`: at each linked bundle, the datum $D$ and its norm choice satisfy `GaloisPreconditions` and `Tie4`;
2. the closed bound for `BoundAtTwoThreeFamilyFonAlt`, as a slot norm condition.

Then the closed bound for `LinkN`, as a slot norm condition, is linked at $p$.

## Proof

Let $R_1$ and $R_2$ be the slots that hypotheses 1 and 2 give. `LargeBaseCondition.and` gives the large base condition for $R_1 \wedge R_2$. On the slot "`IsGoodE p.s` and $R_1 \wedge R_2$", hypothesis 1 still holds by `EvP.mono`, because this slot is smaller than "`IsGoodE p.s` and $R_1$". Hypothesis 2 still holds by `Row.strengthen`, for the same reason with $R_2$. Then `linkN_of_boundAtTwoThree_slot` gives the conclusion on this slot. The rest is bookkeeping.

## In the Lean code

The theorem is in [LinkNFam.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkNFam.lean#L64). `LinkedAt` is in [RowGood.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowGood.lean#L38), and `Lg1` is in [AllRows.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/AllRows.lean#L15). `LargeBaseCondition`, `LargeBaseCondition.and` and `Row.strengthen` are in [EventuallyAllScaleContextsAndOfBoth.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/EventuallyAllScaleContextsAndOfBoth.lean#L42). `EvP.mono` is in [ValidForConstructedPointClassesEventuallyWorking.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/ValidForConstructedPointClassesEventuallyWorking.lean#L170).

`Hypotheses₂` and `CutGivesAlt` only pass through. The name says "bound at two three", but below this theorem only the constants $\varepsilon_1$ and $K$ of hypothesis 2 are used, not its bound: see [the slot form](/entry/link-n-of-bound-at-two-three-slot/).
