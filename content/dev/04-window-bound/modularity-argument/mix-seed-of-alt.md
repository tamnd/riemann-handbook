---
id: mix-seed-of-alt
title: Ordinary Hilbert lifts of mixed weight
kind: theorem
decl: UpperTheory.Esk.mixSeed_of_alt
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.MixSeedOf
covers: 1285
status: drafted
drafted_by: writer@claude
---
This theorem proves `MixSeedP`, the existence of ordinary two-dimensional lifts with mixed weights at the places above $\ell$, from the published hypotheses `HypothesesH'` and the Eisenstein congruence `PropMHol`. It feeds [`seedII_Z_alt`](/entry/seed-ii-z-alt/), which turns it into the seed in case II. It only adds one input, the weight-changing congruence [`holWC`](/entry/hol-wc/), and passes the rest along. The content is in `holWC` and in `mix_birth_of_prints`.

## Statement

**Theorem.** Assume `HypothesesH'` and `PropMHol`. Let $F$ be a totally real field of even degree in which the odd prime $\ell$ splits completely. Let $\xi$ be a character with open kernel of $G_F$ that is odd at each complex conjugation, unramified above $\ell$, ramified at some place of norm 2, with $\xi^2$ not residually trivial, and with $\xi$ not residually trivial on each decomposition group above $\ell$. Let $P$ be a set of places that contains some, but not all, of the places above $\ell$. Then there are $k, t \geq 2$ with $\ell - 1 \mid k$ and $\ell - 1 \mid t$, a cuspidal representation $\pi$ of $\mathrm{GL}_2$ over $F$, and a continuous irreducible $r \colon G_F \to \mathrm{GL}_2(\overline{\mathbb{Q}}_\ell)$ attached to $\pi$, such that:

1. $\det r = \chi_{\mathrm{cyc}}^k \xi$, and $r$ is residually $1 \oplus \xi$;
2. at $w \in P$ above $\ell$, $r$ is ordinary with weights $(k+t, -t)$, and $\pi$ has the matching infinitesimal character;
3. at $w \notin P$ above $\ell$, $r$ is ordinary with weights $(k, 0)$, and $\pi$ has the matching infinitesimal character.

The conditions `TypeAway` and `PR` on $r$ also hold. We have not unfolded them.

## Proof

The proof is `mixSeed_of_holWC_alt holWC P h`. That lemma is one term: `pf_HRep_alt` and `pf_PropMV_sv_alt` combine `PropMHol` with `holWC`, and `mix_birth_of_prints` turns the result into `MixSeedP`. `holWC` is a weight-changing congruence: from a cuspidal Hilbert eigenform of weight $k_0 \geq 4$ it makes a congruent cusp form whose weight is raised by $2t$, with $\ell - 1 \mid t$, at a chosen set of infinite places.

## In the Lean code

The theorem is in [MixSeedOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/MixSeedOf.lean#L13). The lemma is in [MixSeedOfHolWC.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/MixSeedOfHolWC.lean#L15). `MixSeedP` is in [MixSeedPAlt.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/AutomorphyLifting/PrimeIndexConstruction/MixSeedPAlt.lean#L35). `holWC` is proved in [MixSeedOf.lean](lean:PositivityTheory/AutomorphicForms/PublishedInputs/JacquetLanglands/TorusKernels/MixSeedOf.lean#L8), a second file with the same name in another folder.
