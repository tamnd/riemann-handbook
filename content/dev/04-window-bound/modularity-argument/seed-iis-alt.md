---
id: seed-iis-alt
title: The automorphic seed in case II, from the published hypotheses
kind: theorem
decl: UpperTheory.V.Z.Bc.seedIIs_alt
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.BcIndCs
covers: 3287
status: drafted
drafted_by: writer@claude
---
This theorem proves `SeedIIAlt`, the existence of an automorphic seed in case II, from the published hypotheses `HypothesesH'`. It is one of the five inputs of [`sp4In0_alt`](/entry/sp4-in0-alt/). It only assembles other results: [`seedII_Z_alt`](/entry/seed-ii-z-alt/) and an automorphy result for induced representations, which rests on [`indCs`](/entry/ind-cs/). Most of its size is below those two.

## Statement

**Theorem.** Assume `HypothesesH'`. Let $D$ be a residually reducible $\mathrm{GSp}_4$ datum in case II (the condition `Ctx2`: $D$ is `Good`, and a host, $e < t$ and $\psi$ put it in case II). Let $T$ be a tower for $D$ that meets `Ok`, `Two` and `Deep`, and let $\iota \colon \overline{\mathbb{Q}}_\ell \cong \mathbb{C}$. Then there are a larger coefficient ring $\mathcal{O}_1 \supseteq \mathcal{O}$ and a lift $Q$ over $\mathcal{O}_1$ such that:

1. $Q$ is a seed pair: it is a continuous pair for the frame of $T$ with the right reduction, and its $\ell$-adic representation is irreducible and, after a twist by a character, attached to a regular algebraic cuspidal representation of $\mathrm{GL}_4$ over the totally complex field of $T$; consecutive weights differ by $2n$ with $n \geq 2$;
2. the reduction of $Q$ meets the condition `Fr.InV` of the frame;
3. the reduction of $Q$ has a nonzero matrix entry of root weight $(-1,0)$, or nonzero entries of root weights $(-1,1)$ and $(-1,-1)$.

We have not unfolded `Ok`, `Two`, `Deep` or `Fr.InV`.

## Proof

The proof is one term. It builds the structure `Hypotheses4Z'` from `hH`, the weight-one Hilbert Eisenstein series `hilbert_eisenstein_weight_one_holds` and the congruence input `Lit.oneUse`. It gives that and an `IndAutLP` to [`seedII_Z_alt`](/entry/seed-ii-z-alt/). The `IndAutLP` comes from `indAutLP_of_printsH_upQuad_upSol_indCs`, with three inputs:

- `upQuadI_of_alt`, from the base change field `bc` of `hH` through `quadLiftRealToComplex_of_base_change`;
- `upSolI_of_alt`, from the cyclic base change field `cyc` of `hH` through `cyclicLiftRankTwo_of_cyclic_base_change`;
- [`indCs`](/entry/ind-cs/).

## In the Lean code

The theorem is in [BcIndCs.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/BcIndCs.lean#L16). `SeedIIAlt` is in [PotentialModularityTower.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/PotentialModularityTower.lean#L57). The file name refers to `indCs`, not to the theorem.
