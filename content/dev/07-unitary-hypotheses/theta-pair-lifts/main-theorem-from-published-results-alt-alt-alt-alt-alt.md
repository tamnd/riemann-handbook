---
id: main-theorem-from-published-results-alt-alt-alt-alt-alt
title: The period identity for a true pack, renamed
kind: theorem
decl: GlobalTheory.T.main_theorem_from_published_results_alt_alt_alt_alt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.MainTheoremFromPublishedResultsAltAltAltAltAlt
covers: 10209
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [the period identity for a true pack](/entry/mi-at-of-true-pack-alt-alt/). Its only user is [the row theorem](/entry/fam-mi-star-row-alt-alt/), which applies it at the pack of each linked bundle. The content is two levels down, in [the period identity from the family conditions](/entry/mi-star2-of-all-true-alt-alt/).

## Statement

**Theorem.** Assume the thirteen literature hypotheses from `HarishChandraFinite` to `StrongApproxSU`. Let $D$ be a datum, $\mathrm{ex}$ an extra datum over $D$ and $W$ a real pack over $\mathrm{ex}$. Assume that $W$ is a true pack (`TruePackAlt W`), that $1 \le r_S$ for $D$, and `PuNZ D`. Then `RealPackageCondition W`, that is, the period identity `MIstar2` for the coefficient space of $W$.

The words are defined in the [entry of the theorem it renames](/entry/mi-at-of-true-pack-alt-alt/) and in the [entry of the row theorem](/entry/fam-mi-star-row-alt-alt/). The two statements are the same.

## Proof

The proof is the term `GlobalTheory.Fam.miAt_of_truePack_alt_alt`. There is nothing else.

## In the Lean code

The theorem is in [MainTheoremFromPublishedResultsAltAltAltAltAlt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MainTheoremFromPublishedResultsAltAltAltAltAlt.lean#L38), in the same file as the theorem it renames (line 21). The proof is `first | exact @miAt_of_truePack_alt_alt | ...`. The two types are the same text, word for word.

The name does not describe the statement. It is not a main theorem, and the five "alt" give no information. It is the period identity for one pack, and its neighbour one level down, [`main_theorem_from_published_results_alt_alt_alt_alt`](/entry/main-theorem-from-published-results-alt-alt-alt-alt/), has a different statement.
