---
id: main4-alt
title: Symplectic four-dimensional automorphy from promodularity
kind: theorem
decl: UpperTheory.V.Cu.main4_alt
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.CuFinal
covers: 1044
status: drafted
drafted_by: writer@claude
---
This theorem proves `AutomorphyRankFourDense`: six inputs imply `SymplecticFourImageDense`, the symplectic four-dimensional automorphy statement for cases II and III of the [window bound](/proof/vwin/). The theorem itself has no hypotheses. Its user [`sp4In_alt`](/entry/sp4-in-alt/) supplies the six inputs. The proof has two steps: first promodularity, then automorphy.

## Statement

**Theorem.** Assume `CohomologyHyp`, `FerreroWashington`, `HFit`, `SeedIIAlt`, `SeedIVAlt` and `PMExAlt`. Then `SymplecticFourImageDense` holds.

`CohomologyHyp` collects the Galois cohomology inputs (Poitou-Tate duality, the global Euler characteristic formula and the Greenberg-Wiles formula). `FerreroWashington` is the theorem of Ferrero and Washington (Ann. of Math. 109, 1979): for an abelian field $K$ that contains $\mu_l$ (and $\mu_4$ if $l = 2$), the $l$-rank of the class group is bounded along the cyclotomic $\mathbb{Z}_l$-tower of $K$. `HFit` holds by definition (see [`sp4In_alt`](/entry/sp4-in-alt/)). `SeedIVAlt` gives, for a case III tower, a prime $w$ and residual seed data that lift to each larger tower. We have not unfolded `SeedIIAlt` or `PMExAlt`.

`SymplecticFourImageDense` says: for good raw data $D$ in case II or case III, $D$ satisfies `Fin0` and `NoEnd`, and there is $\iota$ such that each irreducible piece of $D$ is `IsAut4Alt`. We have not unfolded `Fin0`, `NoEnd` or `IsAut4Alt`.

## Proof

The proof is one term:

```
modularity_rank_four_of_promodularity_case_three
  (promodularity_case_three_of_chain_reduction existsTensorSeedTower_holds
    (chain_rank_four_of_red_a_y_coin_fib_y (redA_of redTanA) yCoin (fibY_of torusY))
    chainDesc4 chainIV_alt)
```

1. **Promodularity in case III.** `promodularity_case_three_of_chain_reduction` proves `PromodularityCaseThreeDense`: in case III (`Ctx3 D`), each pair `KPair D 𝔞 r u` with `Star` gives `ProModAlt D ι 𝔞 r`. It takes four facts. `ExistsTensorFactorTower` (from `existsTensorSeedTower_holds`) gives a first tower $T_0$ with `Ok` and `Four`. `RankFourChainReductionDense` (from `chainIV_alt`) gives a larger tower with a seed pair and a chain of congruences. `ChainRankFour` (from `chain_rank_four_of_red_a_y_coin_fib_y`) says: for a potential modularity tower of depth $d \ge 30(C+1)^2$ and a residual point $x$ with `Good4`, `SomeIn J (ker x)` implies `AllIn J (ker x)`. We have not unfolded `SomeIn` and `AllIn`. `ChainDesc4` is `chainDesc4`. The proof grows the tower, gets the bound $C$ from `FerreroWashington` through the lemma `x2`, and then assembles the promodularity statement in `last_step`. We have not unfolded `ChainDesc4`, `ExistsTensorFactorTower`, `x2` or `last_step`.
2. **From promodularity to automorphy.** `modularity_rank_four_of_promodularity_case_three` proves `ProModAlt` for each `KPair` with `Star`. Case II uses `proMod_of_pmEx_of_ctx2_of_kPair_of_star`. Case III uses step 1. From `ProModAlt` it then proves `Con D`, `PurityAtPoints` and `AutmAlt`. Last, `fin0_no_end_all_irr_of_good_con_purity_aut` gives the conclusion. We have not unfolded these three statements.

## In the Lean code

The theorem is in [CuFinal.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/CuFinal.lean#L44). The statements `AutomorphyRankFourDense`, `PromodularityCaseThreeDense`, `RankFourChainReductionDense`, `ChainRankFour` and `SeedIVAlt` are in [PromodularityCaseThree.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/PromodularityCaseThree.lean#L19). The two steps are in [ModularityRankFourOfPromodularity.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/ModularityRankFourOfPromodularity.lean#L20) and [PromodularityCaseThreeOfLemmas.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/PromodularityCaseThreeOfLemmas.lean#L131).

The hypothesis `HFit` is not needed, since `hFit` proves it. `RankFourChainReductionDense` also takes `HFit` as a hypothesis.
