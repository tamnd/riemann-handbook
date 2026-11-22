---
id: fourth-initial-of-prints-h
title: Seeds in case III from the published hypotheses
kind: theorem
decl: UpperTheory.V.Z.Win.Birth.fourth_initial_of_prints_h
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.BirthTop
covers: 326
status: drafted
drafted_by: writer@claude
---
This theorem proves `SeedIVAlt`, the existence of seeds in case III, from the published hypotheses `HypothesesH'`. Its result goes through [`sp4In0_alt`](/entry/sp4-in0-alt/) to [`main4_alt`](/entry/main4-alt/). The proof is one call to `fourth_initial_of_rank_four_data`.

## Statement

**Theorem.** `HypothesesH'` implies `SeedIVAlt`.

`SeedIVAlt` says: let $D$ be raw data in case III, $T_0$ a tower of $D$ with the conditions `Ok` and `Four`, $\iota \colon \overline{\mathbb{Q}}_\ell \to \mathbb{C}$ and $\mathfrak{a}$ an ambient coefficient datum with residue field $k$. Then there are a prime $w$ that splits in $T_0$ and a residual representation $s$ over $k$ that has the residual type of $T_0$ with the extra place $w$ (`IsRes`) and the support condition `Supp nM`. For each larger tower $T \ge T_0$ with `Ok` in which $w$ meets the condition `Dies`, there are a larger coefficient ring $\mathcal{O}_1$ and a representation $Q$ over $\mathcal{O}_1$ such that:

- $Q$ is a seed pair (`SeedPairAlt`): it is continuous, meets the conditions `IsPair` and `Res`, and over $\overline{\mathbb{Q}}_\ell$ it is a seed. A seed is irreducible on the subgroup $G'$ of the tower, has weights with $h_i - h_{i+1} = 2n$ for some $n \ge 2$, and its restriction to $G_L$, twisted by a continuous character $\kappa$, is attached to a regular algebraic cuspidal $\pi$ of $\mathrm{GL}_4$ over $L$;
- its reduction lies over $s$ (`OverT`), satisfies `InA`, and has nonzero entries at the roots `-wBe` and `-wTh` (`Ent`).

We have not unfolded `Four`, `Dies`, `OverT` and `InA`.

## Proof

`fourth_initial_of_rank_four_data` takes fifteen inputs. The main ones:

1. `rank_four_automorphy_of_tensor_of_base_change_of_induction` proves `RankFourAutomorphyOfTensor` from `HypothesesH'`, `upQuadI_of_alt`, `upSolI_of_alt`, [`indCs`](/entry/ind-cs/), `polOf4_alt` and `badOfW`. It says: for an imaginary quadratic $K'$ and a modular, irreducible 2-dimensional $\rho$ that satisfies `PR`, there is $j$ with $1 \le j \le 9$ such that the tensor product of $\rho$ with each $\tau$ of type `TauDat` for $\kappa^j$ is automorphic over $K'$ (`AutOffS`).
2. `Cu2.rhoExP` proves `RhoExP`: there are $w$, a character $\theta$ with $\theta^\ell = 1$, a large weight $k$ and an Eisenstein-congruent $\rho$ (`EisRep`) with an integral model $\rho_1$. It needs `PropEGP`, from `propEGP_of_printsH`.
3. `tauEx'` gives the 2-dimensional $\tau$ from an algebraic Hecke character $\kappa$ of $K'$.

Inside `fourth_initial_of_rank_four_data`, $K'$ is the imaginary quadratic field of `Four`. The seed is the 4-dimensional `rep4` built from $\rho_1$ and $\tau$, restricted to $G_F$. The inputs `pairOf4`, `resOf4`, `contOf4`, `entOf4`, `overOf4`, `wtsOf4`, `irrOf4_of` and `autOf4_of`, which we have not unfolded, prove its properties.

## In the Lean code

The theorem is in [BirthTop.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/BirthTop.lean#L82). The lemmas:

- `fourth_initial_of_rank_four_data` in [BirthSeedIV.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/BirthSeedIV.lean#L18);
- `rank_four_automorphy_of_tensor_of_base_change_of_induction` in [AutomorphicLiftGsp4OfInputs.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/AutomorphicLiftGsp4OfInputs.lean#L69), with its statement in [RankFourAutomorphyOfTensor.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/AutomorphyLifting/PrimeIndexConstruction/RankFourAutomorphyOfTensor.lean#L43);
- `RhoExP` in [MixSeedPAlt.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/AutomorphyLifting/PrimeIndexConstruction/MixSeedPAlt.lean#L55), and `SeedIVAlt` in [PromodularityCaseThree.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/PromodularityCaseThree.lean#L19).

The lemma `fourth_initial_of_rank_four_data` asks for `Hypotheses'`, and gets the field `toClassicalTheorems` of `HypothesesH'`. The line above proves `seed2_alt` with the same `propEGP_of_printsH`.
