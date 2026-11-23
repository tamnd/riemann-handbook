---
id: mi-star2-of-pu-nz
title: The period identity from nonvanishing periods (renaming)
kind: theorem
decl: GlobalTheory.T.mi_star2_of_pu_nz
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.MiStar2OfFamiliesStatement
covers: 301
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`miStar2_of_bot_lev_fam_served_puNZ`](/entry/mi-star2-of-bot-lev-fam-served-pu-nz/). It adds no mathematics. Its user is [the period identity from the family conditions](/entry/mi-star2-of-all-true-alt-alt/), where it is step 4. The proof is in the entry of the original.

## Statement

Let $W$ be a real pack. Assume the published inputs `DiscreteSeriesClassification`, `CuspRapidDecay` and `HarishChandraModules`. Assume also:

- `BottomHypotheses W` and `LevelHypothesis W`, the package hypotheses;
- `FamilyAllConditions W`: a central element $z$ and, for each word $u$, a family character and bottom data with a pin at $z$ and link conditions;
- `FamilyServedCondition W`: for each $w$ and each prime $p$ with `qPrime_alt W (μ w) p`, $p$ is not in the ideal of $w$;
- `PuNZ D`: for each $u$ the period map $\mathrm{Pu}_u$ is nonzero at some vector.

**Theorem.** Then the period identity `MIstar2` holds for the coefficient space of $W$.

`MIstar2` is described in the [parent entry](/entry/mi-star2-of-all-true-alt-alt/).

## Proof

The proof is the term `miStar2_of_bot_lev_fam_served_puNZ`, tried in three forms by a `first | exact @X | exact X | (intros; apply X <;> assumption)` tactic. The two statements are the same, so the first form works.

## In the Lean code

The theorem is at [MiStar2OfFamiliesStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MiStar2OfFamiliesStatement.lean#L20). The original is `GlobalTheory.MiTop.miStar2_of_bot_lev_fam_served_puNZ` in [MiStar2OfFamilies.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MiStar2OfFamilies.lean#L23). The name keeps only the last hypothesis, `PuNZ`.
