---
id: seed-ii-z-alt
title: The seed in case II, from a mixed-weight seed and induced automorphy
kind: theorem
decl: UpperTheory.V.Z.Bc.seedII_Z_alt
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.SeedIIZ
covers: 1695
status: drafted
drafted_by: writer@claude
---
This theorem proves `SeedIIAlt`, the automorphic seed in case II, from the hypotheses `Hypotheses4Z'` and the induced automorphy statement `IndAutLP`. It is the main step of [`seedIIs_alt`](/entry/seed-iis-alt/), which supplies both hypotheses. It only passes them along. The content is in `seedII_of_p_alt` and, below it, in [`mixSeed_of_alt`](/entry/mix-seed-of-alt/).

## Statement

`Hypotheses4Z'` is a structure with three fields: the published hypotheses `HypothesesH'`, the existence of weight-one Hilbert Eisenstein series (`HilbertEisOne`), and a congruence input `Lit.OneUse` about Hilbert modular forms congruent to $1$. `IndAutLP` says: given induction data for a tower (a two-dimensional representation $r$ of a totally real field, a four-dimensional $R$ of $G_{\mathbb{Q}}$ and a character $\delta$) with $r$ satisfying `PR`, the restriction of $R$ to the field $L$ of the tower is automorphic and meets the weight condition `AllW`. We have not unfolded `IndDat`, `PR` or `AllW`.

**Theorem.** If `Hypotheses4Z'` and `IndAutLP` hold, then `SeedIIAlt` holds. See [the entry above](/entry/seed-iis-alt/) for `SeedIIAlt` in words.

## Proof

The proof is one term:

1. `propMHolZ_alt` proves `PropMHol` from `Hypotheses4Z'`. It uses the Eisenstein field and the congruence field. `PropMHol` gives, for a totally real field, an odd finite-order Hecke character $\omega$ and each bound $B$, a cuspidal Hilbert eigenform of weight $k+1$ with $k \geq B$ and $\ell - 1 \mid k$ whose Hecke eigenvalues are congruent to those of an Eisenstein series.
2. [`mixSeed_of_alt`](/entry/mix-seed-of-alt/) turns `HypothesesH'` and `PropMHol` into `MixSeedP`, a family of ordinary representations with mixed weights at the places above $\ell$.
3. `mixOfP` turns `MixSeedP` into `MixOfP`, its form for the data of a tower.
4. `seedII_of_p_alt` combines `MixOfP` with `IndAutLP` to get `SeedIIAlt`. It builds an induced representation, proves it irreducible (`induced_irreducible`), and applies `IndAutLP` and `induced_final_statement_alt`.

## In the Lean code

The theorem is in [SeedIIZ.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/SeedIIZ.lean#L17). The lemmas are in [MPropMHol.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/MPropMHol.lean#L108), [ContRes.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/AutomorphyLifting/PrimeIndexConstruction/ContRes.lean#L29) and [BirthSeedII.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/BirthSeedII.lean#L120). The structure `Hypotheses4Z'` is in [Hypotheses4Z.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/Hypotheses4Z.lean#L10).
