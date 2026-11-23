---
id: mi-at-of-true-pack-alt-alt
title: The period identity for a true pack
kind: theorem
decl: GlobalTheory.Fam.miAt_of_truePack_alt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.MainTheoremFromPublishedResultsAltAltAltAltAlt
covers: 10207
status: drafted
drafted_by: writer@claude
---
This theorem proves the period identity `MIstar2` for a real pack over any datum, when the pack is true. It only unpacks the definition of a true pack and passes the result to [`main_theorem_from_published_results_alt_alt_alt_alt`](/entry/main-theorem-from-published-results-alt-alt-alt-alt/). The content is in [the period identity from the family conditions](/entry/mi-star2-of-all-true-alt-alt/). Its only user is the renaming [main-theorem-from-published-results-alt-alt-alt-alt-alt](/entry/main-theorem-from-published-results-alt-alt-alt-alt-alt/).

## Statement

A real pack $W$ (`RealPackAlt ex`) over an extra datum $\mathrm{ex}$ for a datum $D$ is a recursion datum $R$, spectral ties $S$, a row side family $P$, columns with their periods and scales, a number field $K_s$ and a realisation $Q$. `RealPackageCondition W` is by definition the period identity `MIstar2` for the coefficient space $Q.\mathrm{Rl}.\mathrm{toCx3}\,Q.F$. The [row theorem](/entry/fam-mi-star-row-alt-alt/) says what `MIstar2` means.

`TruePackAlt` is an inductive predicate with one constructor. $W$ is a true pack when $D$ is a datum `I.rec7 l Z`, built from a base $B$ and data `X`, `I : TC B X`, `l : I.Laws` and `Z : TC.Later`, and `AllFamilyConditions W` holds.

**Theorem.** Assume the thirteen literature hypotheses from `HarishChandraFinite` to `StrongApproxSU`. Let $W$ be a true pack over $D$ with $1 \le r_S$ for $D$ and `PuNZ D`. Then `RealPackageCondition W`.

## Proof

Case analysis on the true pack replaces $D$ by `I.rec7 l Z` and gives `AllFamilyConditions W`. Then [`main_theorem_from_published_results_alt_alt_alt_alt`](/entry/main-theorem-from-published-results-alt-alt-alt-alt/) gives `MIstar2`,, with the thirteen hypotheses passed on.

## In the Lean code

The theorem is in [MainTheoremFromPublishedResultsAltAltAltAltAlt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MainTheoremFromPublishedResultsAltAltAltAltAlt.lean#L21). `TruePackAlt` and `RealPackageCondition` are in [TruePack.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TruePack.lean#L13).

The hypothesis $1 \le r_S$ is stated for $D$. The callee wants $1 \le r_S$ for the base $B$. Lean accepts the same proof, so the two agree by definition after the case analysis. We have not unfolded `rec7`.

The name says "at", but no place or point appears in the statement.
