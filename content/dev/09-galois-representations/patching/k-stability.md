---
id: k-stability
title: Homological stability for general linear groups, a second name
kind: theorem
decl: PositivityTheory.v8.KStability.kStability
module: Development.AutomorphicArithmetic.AutomorphicVarieties.LiteratureResults.KTheoryStability.HomologicalStability.KStability
covers: 341
status: drafted
drafted_by: writer@claude
---
This theorem proves `KStability`, homological stability for $\mathrm{GL}_n$ over a commutative ring of finite stable range. It is a second name: its proof is the single term `kStability_main`, and the [entry for that theorem](/entry/k-stability-main/) has the real content. Below [the bound on the second Galois cohomology](/entry/lemma-k-lit-n-alt/), two lemmas call this name with $s = 2$ for a Dedekind domain.

## Statement

Let $R$ be a commutative ring. Say that $R$ has stable range at most $s$ if for each $n \geq s$ and each unimodular row $(r_1, \dots, r_{n+1})$ of $R$ there are $t_1, \dots, t_n \in R$ such that $(r_1 + t_1 r_{n+1}, \dots, r_n + t_n r_{n+1})$ is unimodular. Let $\mathrm{GL}_n(R) \to \mathrm{GL}_{n+1}(R)$ be the map $g \mapsto \mathrm{diag}(g, 1)$.

**Theorem.** If $R$ has stable range at most $s$, and $n \geq 2i + s + 2$, then the induced map
$$H_i(\mathrm{GL}_n(R); \mathbb{Z}) \to H_i(\mathrm{GL}_{n+1}(R); \mathbb{Z})$$
is an isomorphism.

## Proof

The proof is `GlobalTheory.HomStab.kStability_main`, with no change.

## In the Lean code

- The theorem is in [KStability.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/HomologicalStability/KStability.lean#L3). The statement `KStability` is in [KAcyclicHomology.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PublishedTheorems/KAcyclicHomology.lean#L21). `StableRangeLe`, `stab` and `grpHMap` are in [StabDirectedSystem.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/TensorHomCubes/StabDirectedSystem.lean#L61).
- The two callers are `UpperTheory.V.ZK.Up.torsStab` in [TorsStab.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ClassCounting/TorsionRankCounts/TorsStab.lean#L21), for the ring of integers $\mathcal{O}_L$ of a number field, and `isIso_stab` in [BaseChangeBijective.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults/KTheoryStability/ReductionBoundsTorsion/BaseChangeStability/BaseChangeBijective.lean#L33), for a Dedekind domain. Both get the stable range bound from `dedekindSR` and use the range $n \geq 2i + 4$.
- `dedekindSR` proves that a Dedekind domain has stable range at most $2$.
- The structures `KPublished` and `KPublishedW` in [KBridgeOfKPublished.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/TensorHomCubes/KBridgeOfKPublished.lean#L29) and its sibling file also have a field of type `KStability`.
