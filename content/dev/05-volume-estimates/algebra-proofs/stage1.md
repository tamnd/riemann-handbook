---
id: stage1
title: The Chern number relations, given the first chart condition
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Num.CkTop.stage1
module: Development.AutomorphicSpectrum.Proofs.AlgebraProofs.DescentRelationsFromModels
covers: 433
status: drafted
drafted_by: writer@claude
---
This theorem is the second link of the chain of [`ckRelations_of_model`](/entry/ck-relations-of-model/), which calls it on a refined model. It passes to a finer model whose chart rings are integrally closed, and then calls [`stage1b`](/entry/stage1b/). The chain and the descent step are described in [the entry on `ckRelations_of_model`](/entry/ck-relations-of-model/).

## Statement

Take the setting of [`ckRelations_of_model`](/entry/ck-relations-of-model/): $O$ of characteristic $0$, a model $x$ of dimension $d$ with function field $\Omega$, a prime $p$ and a lattice family $D$. Assume in addition `Good₁` for $D$ on each chart: the lattice $M + pR^{F^n}$ is locally free of rank $|F|^n$, the image of the map of each $\chi_\tau$ is a direct summand of it, and the subspaces `vanSub` and `charSub` are direct summands of $M$.

**Theorem.** Then `CkRelations` holds for all chart bundles $\mathrm{Lie}, W, \Omega_1, \Omega_{\mathrm{HT}}$ with the lattices of $D$.

## Proof

1. `model_refinement_exists` gives coordinates $z$ such that $(x, z)$ is a model of dimension $d$ with normal charts (`NormalCharts`). It needs $\operatorname{char} O = 0$.
2. `lattice_family_injective_model` shows that the pulled family is a lattice family on $(x, z)$ and that `Good₁` passes to it.
3. `chart_rings_noetherian_fraction` shows that the function field of $(x, z)$ is $\Omega$.
4. `stage1b` on $(x, z)$ gives the relations there, and `descend` brings them back to $x$.

## In the Lean code

The theorem is in [DescentRelationsFromModels.lean](lean:Development/AutomorphicSpectrum/Proofs/AlgebraProofs/DescentRelationsFromModels.lean#L149). It is a refinement step: the real work is in the lemmas it calls, which are statement forms that we have not opened, and in the later links. `Summand L U` means that there is a projection onto $U$ that maps $L$ into $L$; `Good₁` is in [LieLatticeData.lean](lean:Development/AutomorphicSpectrum/Definitions/CommutativeAlgebra/LieLatticeData.lean#L127).
