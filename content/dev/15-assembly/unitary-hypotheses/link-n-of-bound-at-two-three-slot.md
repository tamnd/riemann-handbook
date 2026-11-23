---
id: link-n-of-bound-at-two-three-slot
title: The closed link bound on one slot
kind: theorem
decl: UpperTheory.GalC.linkN_of_boundAtTwoThree_slot
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.LinkNFam
covers: 14242
status: drafted
drafted_by: writer@claude
---
This theorem proves the closed bound for the link inequality `LinkN` on the families that one slot row selects. It applies [the link bound for one family](/entry/link-n-of-tw-good-galois-preconditions/) to each such family. That lemma has the real content. The caller is [the linked form](/entry/linked-at-link-n-of-bound-at-two-three/), which puts the result into the `LinkedAt` form that [the closed link bound](/entry/final-alt-alt/) needs.

## Statement

Fix a slot $Q$ and a bundle linkage $L_k$. A *row statement* `Row Q Lk H` says: there is a property $E$ of bundles such that `RowE Q Lk E` holds (eventually, $E$ holds at each bundle of the slot $Q$ that $L_k$ links), and $H(\mathcal{A}, \sigma)$ holds for each family class $\mathcal{A}$ and each choice $\sigma$ of bundles that is a selection for $E$ (`IsSel`). The *slot norm condition* for a property $N$ of family classes is the row statement $H(\mathcal{A}, \sigma) = N(\mathcal{D}_3(\mathcal{A}))$. Here $\mathcal{D}_3(\mathcal{A})$ is `D3 3 𝒜`: the families $F$ with `WithChN 𝒜 F`, `DGamSmooth`, `TwGood`, a chosen datum `ChosenE` with constant 3, `TuSize` and `DGamSize`. We have not unfolded these conditions, except that `WithChN 𝒜 F` implies $F \in \mathcal{A}$.

**Theorem.** Assume `Hypotheses₂` and `CutGivesAlt`. Suppose that:

1. `RowE Q Lk` holds for the property "the datum $D$ and its norm choice satisfy `GaloisPreconditions` and `Tie4`";
2. the slot norm condition holds for $\mathcal{C} \mapsto$ `Closed 𝒞 BoundAtTwoThreeFamilyFonAlt`.

Then the slot norm condition holds for $\mathcal{C} \mapsto$ `Closed 𝒞 LinkN`. The closed bound `Closed` and the link bound are defined in [the closed link bound, given a cut](/entry/final-of-alt/).

## Proof

`RowE.row` turns hypothesis 1 into the row statement "every bundle that $\sigma$ selects satisfies the preconditions". `Row.and` joins it with hypothesis 2, and `Row.imp` reduces the claim to one selection $(\mathcal{A}, \sigma)$. Hypothesis 2 at $(\mathcal{A}, \sigma)$ gives $\varepsilon_1 > 0$ and, for each $\varepsilon \in (0, \varepsilon_1]$, a threshold $K$. The proof keeps the same $\varepsilon_1$ and $K$. Let $F$ be a family in $\mathcal{D}_3(\mathcal{A})$ that is large for $K$. Then $F$ is `TwGood`, and $F \in \mathcal{A}$, so the preconditions hold at each $D_{x,i}$ of $F$. Now `linkN_of_twGood_galoisPreconditions` gives `LinkN F`.

## In the Lean code

The theorem is in [LinkNFam.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkNFam.lean#L54). The lemmas it calls:

- `RowE.row`, `Row.and` and `Row.imp` in [ValidForConstructedPointClassesEventuallyWorking.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/ValidForConstructedPointClassesEventuallyWorking.lean#L313);
- `d3_a` in [CountsIrreducibilityConstants.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/CountsIrreducibilityConstants.lean#L37);
- `linkN_of_twGood_galoisPreconditions`, in the same file.

The bound of hypothesis 2 is never used. The proof takes only $\varepsilon_1$ and $K$ from it, and drops the bound `hK` and the largeness `hL` of $F$ ([L61 to 63](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkNFam.lean#L61)). The bound at two and three is proved again, for every family, by `at23_family_alt hP` inside `linkN_of_twGood_galoisPreconditions` ([L51](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkNFam.lean#L51)). So any $\varepsilon_1$ and $K$ would do, and hypothesis 2 can be dropped. The name says "of bound at two three", which suggests the opposite.
