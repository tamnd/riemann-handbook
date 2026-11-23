---
id: main-theorem-from-published-results-alt-alt-alt-alt
title: The period identity from the family conditions, renamed
kind: theorem
decl: GlobalTheory.T.main_theorem_from_published_results_alt_alt_alt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.MainTheoremFromPublishedResultsAltAltAltAlt
covers: 10206
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [the period identity from the family conditions](/entry/mi-star2-of-all-true-alt-alt/), which has the content. Its only user is [the period identity for a true pack](/entry/mi-at-of-true-pack-alt-alt/), which calls it after a case analysis.

## Statement

**Theorem.** Assume the thirteen literature hypotheses from `HarishChandraFinite` to `StrongApproxSU`. Let $D$ be a datum `I.rec7 l Z` built from a base $B$, and $W$ a real pack over an extra datum for $D$. Assume `AllFamilyConditions W`, $1 \le r_S$ for $B$, and `PuNZ D`. Then the period identity `MIstar2` holds for the coefficient space of $W$.

The words are defined in the [entry of the theorem it renames](/entry/mi-star2-of-all-true-alt-alt/). The two statements are the same.

## Proof

The proof is the term `GlobalTheory.Fam.miStar2_of_allTrue_alt_alt`. There is nothing else.

## In the Lean code

The theorem is in [MainTheoremFromPublishedResultsAltAltAltAlt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MainTheoremFromPublishedResultsAltAltAltAlt.lean#L37), in the same file as the theorem it renames (line 23). The proof is `first | exact @miStar2_of_allTrue_alt_alt | ...`. The two types are the same text, word for word.

The name does not describe the statement. It is not a main theorem. It is the period identity for one pack. The four "alt" give no information.
