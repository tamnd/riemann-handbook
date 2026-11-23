---
id: casselman-wallach-of-literature
title: The Casselman-Wallach extension for U(p,q), from the literature
kind: theorem
decl: UpperTheory.LiteratureTheorems.casselman_wallach_of_literature
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.EveryCharacterOfLiteratureOfVWin
covers: 437
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It takes the argument $O$ of type [OpenLiteratureStatements](/step/open-literature-statements-def/), ignores it, and returns the theorem [`casselmanWallach`](/entry/casselman-wallach/), which has the real content (436 of the 437 declarations below this one). It is a cited result of the main theorem [every character of the literature](/step/every-character-of-literature/). Its result fills the field `casselmanWallach` of the bundles [UnitaryGroupThirdPlaceHypotheses](/step/published-results-eigen/) and [ThetaLocalInputs](/step/published-results-first/).

## Statement

Let $G = U(p,q)$, the complex matrices $g$ with $g^* J g = J$ for a diagonal sign matrix $J$, and $K = U(p) \times U(q)$. Let $\sigma$ be an irreducible unitary representation of $G$ on a Hilbert space $H$. Let $E$ be a complete Hausdorff locally convex space with a countable family of seminorms, and let $\pi$ be a smooth representation of $G$ on $E$ of moderate growth: each seminorm of $\pi(g)v$ is at most $(1 + s(g))^N$ times a continuous seminorm of $v$, for a fixed size function $s$. Let $T_0 : H \to E$ be linear and commute with $K$ and with the Lie algebra on the $K$-finite vectors. Then there is a linear map $T : H \to E$ such that:

1. $T = T_0$ on the $K$-finite vectors;
2. $T$ commutes with $G$ on the smooth vectors, and each seminorm of $T w$ is bounded by a Sobolev norm of $w$;
3. any other map with properties 1 and 2 agrees with $T$ on the smooth vectors;
4. the image of the smooth vectors under $T$ is closed;
5. if $T_0$ is not zero on the $K$-finite vectors, then each Sobolev norm of $w$ is bounded by a continuous seminorm of $T w$.

This has the form of the theorem of Casselman and Wallach on the smooth globalization of a [[Harish-Chandra module|2MKHH636C3]] (Casselman, Canad. J. Math. 41, 1989; Wallach, Real Reductive Groups II, chapter 11).

## Proof

The proof is `PositivityTheory.CWB.casselmanWallach`, with no change.

## In the Lean code

The theorem is at [EveryCharacterOfLiteratureOfVWin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L321). The statement `CasselmanWallach` is at [HasDRepIffHasDerivAt.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/HasDRepIffHasDerivAt.lean#L98).

- The argument $O$ is not used.
- I have not unfolded the size function `hs`.
- The proof at [FinalB.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/CasselmanWallach/FinalB.lean#L8) is `cw_of maxPr`. The maximum principle `maxPr` is in a file named [EtaleCohomologyNegativeVanishingDegreeZero.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/CasselmanWallach/EtaleCohomologyNegativeVanishingDegreeZero.lean#L91), a name with no relation to its content.
