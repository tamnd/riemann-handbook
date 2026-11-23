---
id: term-pair-count-bound-of-siegel-mass-ratios
title: The pair count from the mass formulas, statement form
kind: theorem
decl: GlobalTheory.T.termPairCountBound_of_siegelMassRatios
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.TermPairCountBoundOfSiegelMassRatiosStatement
covers: 1179
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`pair_count_bound_of_siegel_mass`](/entry/pair-count-bound-of-siegel-mass/). Its only user is [`typeBound_of_gap`](/entry/type-bound-of-gap/), which supplies both hypotheses as proved theorems. The content is in [`pair_count_bound_of_siegel_mass`](/entry/pair-count-bound-of-siegel-mass/).

## Statement

**Theorem.** If `MaxMass` and `SiegelMassRatio` hold, then the pair count `PairsP` holds.

`MaxMass` says that the mass of a maximal lattice in a positive definite Hermitian space over a CM field is a constant times a product of local factors at the primes where the lattice is not unimodular. `SiegelMassRatio` gives the ratio of the masses of the standard lattices of ranks $M$ and $M - 1$ by a closed formula. Both are stated in full in [the entry below](/entry/pair-count-bound-of-siegel-mass/), and `PairsP` in [the entry for `typeBound_of_gap`](/entry/type-bound-of-gap/).

## Proof

The proof is the term `GlobalTheory.TypeAsm.pair_count_bound_of_siegel_mass`. There is nothing else.

## In the Lean code

The theorem is at [TermPairCountBoundOfSiegelMassRatiosStatement.lean line 7](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/TermPairCountBoundOfSiegelMassRatiosStatement.lean#L7). The proof is a tactic `first | exact @… | exact … | (intros; apply … <;> assumption)` with `maxHeartbeats` set to 1,000,000. The two statements are the same, so the first alternative already fits. The name speaks of "mass ratios" only, but the first hypothesis is the mass formula for maximal lattices.
