---
id: stage2
title: The Chern number relations, given the first two chart conditions
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Num.CkTop.stage2
module: Development.AutomorphicSpectrum.Proofs.AlgebraProofs.DescentRelationsFromModels
covers: 408
status: drafted
drafted_by: writer@claude
---
This theorem is the fourth link of the chain of [`ckRelations_of_model`](/entry/ck-relations-of-model/). It passes to a finer model on which the second set of chart conditions, `Good₂`, holds, and then calls [`stage3`](/entry/stage3/). Its one user is [`stage1b`](/entry/stage1b/).

## Statement

Take the setting of [`stage1`](/entry/stage1/): $O$ of characteristic $0$, a model $x$ of dimension $d$ with function field $\Omega$, a prime $p$, a lattice family $D$ with `Good₁` on each chart. Assume also $w R^n \subseteq \mathfrak{a}_\tau$ on each chart with ring $R$ and for each $\tau$, with $\mathfrak{a}_\tau$ as in [`stage1b`](/entry/stage1b/).

**Theorem.** Then `CkRelations` holds for all chart bundles with the lattices of $D$.

## Proof

1. `lattice_family_model_comparison` gives coordinates $z$ such that $(x, z)$ is a model of dimension $d$ on which the pulled family satisfies `Good₂`. It uses `Good₁` and the inclusion $w R^n \subseteq \mathfrak{a}_\tau$.
2. `lattice_family_injective_model` shows that the pulled family is a lattice family and that `Good₁` and the inclusion pass to it.
3. `chart_rings_noetherian_fraction` shows that the function field of $(x, z)$ is $\Omega$.
4. `stage3` on $(x, z)$ gives the relations there, and `descend` brings them back to $x$.

The condition `Good₂` asks, on each chart: the subspaces `annSub` (vectors whose first $i$ coordinates vanish) are direct summands of $\mathfrak{a}_\tau$; and three families of lattices built from the fields $\Theta$ and $\Delta$ of $D$ (`kk`, the images of `stepGraph`, and `imH`) are locally free of ranks $r(\tau)$, $r(\tau)$ and $s(\tau)$.

## In the Lean code

The theorem is in [DescentRelationsFromModels.lean](lean:Development/AutomorphicSpectrum/Proofs/AlgebraProofs/DescentRelationsFromModels.lean#L135). `Good₂` is in [LieLatticeData.lean](lean:Development/AutomorphicSpectrum/Definitions/CommutativeAlgebra/LieLatticeData.lean#L133). It is a refinement step with the same form as `stage1`; the content is in `lattice_family_model_comparison`, a statement form that we have not opened.