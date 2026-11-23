---
id: hodge-metric-lie-gram-is-good-mumford
title: The Hodge metric on a Lie base is good, restated
kind: theorem
decl: GlobalTheory.T.hodgeMetric_lieGram_isGood_mumford
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.HodgeMetricLieGramIsGoodMumfordStatement
covers: 359
status: drafted
drafted_by: writer@claude
---
This theorem is a second name of [`lieGram_isGood`](/entry/lie-gram-is-good/). It has the same statement and no proof of its own. [The good base](/entry/exists-good-base/) uses it for its property 4: the metric `lieGram` is good in the sense of Mumford at the boundary of the open part. The mathematics is in the entry of `lieGram_isGood`.

## Statement

Use the setting and notation of [the good base](/entry/exists-good-base/).

**Theorem.** Assume `GoodEmb` and `IsUnf`. Let $C$ be a component of a flag space over the toroidal model, and $(X, j, f, f_0, \mathcal{E}, A_0)$ a Lie base for $C$ (`IsLieBase`). Then the metric $h = $ `lieGram` on $\mathcal{E}$ is good on $O = $ `openPart j` (`IsGood`): near each point of $X(\mathbb{C}) \setminus O(\mathbb{C})$ there is a holomorphic chart in which the boundary is a union of coordinate hyperplanes, and $h$ satisfies the bounds `GoodBound` there.

## Proof

The proof is `first | exact @GlobalTheory.LieBaseGood.lieGram_isGood | …`. The first branch closes the goal.

## In the Lean code

The theorem is in [HodgeMetricLieGramIsGoodMumfordStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/HodgeMetricLieGramIsGoodMumfordStatement.lean#L8). Its statement is word for word that of `lieGram_isGood` in [HodgeMetricLieGramIsGoodMumford.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/HodgeMetricLieGramIsGoodMumford.lean#L19). The component $C$ is any `FlagCpt`, not only a component $\Phi.C\,k$ of a toroidal flag space; the good base applies it with $C = \Phi.C\,k$.
