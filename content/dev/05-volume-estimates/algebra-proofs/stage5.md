---
id: stage5
title: The Chern number relations on a model with normal charts
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Num.CkTop.stage5
module: Development.AutomorphicSpectrum.Proofs.AlgebraProofs.DescentRelationsFromModels
covers: 325
status: drafted
drafted_by: writer@claude
---
This theorem is the last link of the chain of [`ckRelations_of_model`](/entry/ck-relations-of-model/). Its one user is [`stage4`](/entry/stage4/), which calls it on a refined model. It is the only link that does not refine the model: it proves the relations from the chart conditions. The proof is short and calls two lemmas, which carry the content.

## Statement

Let $O$ be a discrete valuation ring and $x$ coordinates in a field $\Omega$ whose ideal is a model of dimension $d$ with function field $\Omega$. Let $p$ be a prime and $D$ a lattice family. Assume, on each chart with ring $R$:

- the chart ring $R$ is integrally closed in $\Omega$ (`NormalCharts`);
- `Good₁` and `Good₂` hold, as in [`stage2`](/entry/stage2/);
- for each $\tau$ and $i$, the ideals `xId` form a line, as in [`stage3`](/entry/stage3/).

**Theorem.** Then `CkRelations` holds for all chart bundles with the lattices of $D$.

Unlike the other links, this theorem does not ask that $O$ have characteristic $0$.

## Proof

1. On each chart, `lattice_facts_of_normal_holds` proves `Facts`. Its inputs are: `charData_of`, which writes $p = c\,w$ with $c = u^{-1} w^{p-2}$ in $R$ from the relation $w^{p-1} = u\,p$ of the family; the inclusions `base` of the family; the facts that $R$ is Noetherian and has fraction field $\Omega$ (`chart_rings_noetherian_fraction`); the normality of $R$; the field `test` of the family, which says that `Facts` hold after base change to each test point (an algebraically closed field with a valuation $v$, $v(p) < 1$, whose ring of integers is $p$-adically complete); and `Good₁`, `Good₂`.
2. `model_over_mod_p_lattice_eigen_split` turns the family, `Good₁`, `Good₂`, `Facts` on each chart and the lines into `CkRelations`.

`Facts` says, for each $\tau$: $w R^n \subseteq \mathfrak{a}_\tau$; the image lattice `imH` is the lattice `om` of $D$; the kernel `kerH` is $w^{-1}$ times the lattice `lie` of $D$; the ideals `dId` and `xId` agree; and two statements on the graph `stepGraph`, one of surjectivity onto `kk` and one that identifies a preimage with the $p$-power span of `xId`.

## In the Lean code

The theorem is in [DescentRelationsFromModels.lean](lean:Development/AutomorphicSpectrum/Proofs/AlgebraProofs/DescentRelationsFromModels.lean#L99), and `Facts` in [LieLatticeData.lean](lean:Development/AutomorphicSpectrum/Definitions/CommutativeAlgebra/LieLatticeData.lean#L139). Both lemmas are statement forms. They point to `Ar.Num.lattice_facts_of_normal` and `GoodModel.relations`, whose proofs we have not opened. The step from `TestFacts` to `Facts` looks like a descent from test points to a normal Noetherian ring, but we have not checked this in the proof. The first field of `Facts` is the inclusion $w R^n \subseteq \mathfrak{a}_\tau$, so this link recovers the hypothesis that `stage4` discards.
