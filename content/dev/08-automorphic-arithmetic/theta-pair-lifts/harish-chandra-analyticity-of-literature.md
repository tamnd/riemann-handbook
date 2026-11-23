---
id: harish-chandra-analyticity-of-literature
title: Analytic matrix coefficients and dense Levi submodules, from the literature
kind: theorem
decl: UpperTheory.LiteratureTheorems.harish_chandra_analyticity_of_literature
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.EveryCharacterOfLiteratureOfVWin
covers: 314
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It takes the argument $O$ of type [OpenLiteratureStatements](/step/open-literature-statements-def/), ignores it, and returns the theorem [`harishChandra_analyticity_density`](/entry/harish-chandra-analyticity-density/), which has the real content (313 of the 314 declarations below this one). Its result fills the field `harishChandraAnalyticity` of the bundle [UnitaryGroupThirdPlaceHypotheses](/step/published-results-eigen/).

## Statement

Let $G = U(p,q)$ be the group of complex matrices $g$ with $g^* J g = J$, where $J$ is diagonal with entries $\pm 1$. Let $K = U(p) \times U(q)$ be the unitary matrices that commute with $J$. The statement has two parts.

1. Let $\pi$ be a continuous admissible representation of $G$ on a Hilbert space that is unitary on $K$. For $K$-finite vectors $v$ and $w$, the coefficient $g \mapsto \langle w, \pi(g) v \rangle$ is real analytic on $G$: near each point it agrees with a real-analytic function of the matrix entries.
2. Let $W$ be an isotropic flag for $J$, and let $M$ be the Levi group of $g$ such that $g$ and $g^*$ keep each piece of the flag and $\lvert \det \rvert = 1$ on each piece. Let $\sigma$ be a unitary irreducible representation of $M$. Then a nonzero subspace of $K \cap M$-finite vectors that is stable under the derivatives along one-parameter subgroups of $M$ is dense.

Part 1 has the form of a theorem of Harish-Chandra (Trans. Amer. Math. Soc. 75, 1953), for vectors of a [[Harish-Chandra module|2MKHH636C3]]. I have not compared part 2 with a source.

## Proof

The proof is `GlobalTheory.CompanionTheory.Hypotheses₂.harishChandra_analyticity_density`, with no change.

## In the Lean code

The theorem is at [EveryCharacterOfLiteratureOfVWin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L411). The statement `HarishChandraAnalyticity` is at [AdmissibleCoefficientsAnalytic.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/AdmissibleCoefficientsAnalytic.lean#L26).

- The argument $O$ is not used.
- `HarishChandraAnalyticity` is the conjunction `AdmissibleCoefficientsAnalytic ∧ LeviSubmoduleDense` of two statements that do not depend on each other.
- The proof at [AdmissibleOfIwasawaDecomposition.lean](lean:Development/AutomorphicSpectrum/Proofs/GlobalProofs/AdmissibleOfIwasawaDecomposition.lean#L172) pairs the two lemmas `admissibleCoefficientsAnalytic` and `leviSubmoduleDense`.
