---
id: stage3
title: The Chern number relations, given the summand and freeness conditions
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Num.CkTop.stage3
module: Development.AutomorphicSpectrum.Proofs.AlgebraProofs.DescentRelationsFromModels
covers: 360
status: drafted
drafted_by: writer@claude
---
This theorem is the fifth link of the chain of [`ckRelations_of_model`](/entry/ck-relations-of-model/). It passes to a finer model on which the ideals `xId` of the family are lines, and then calls [`stage4`](/entry/stage4/). Its one user is [`stage2`](/entry/stage2/).

## Statement

Take the setting of [`stage2`](/entry/stage2/): $O$ of characteristic $0$, a model $x$ of dimension $d$ with function field $\Omega$, a prime $p$, a lattice family $D$ with `Good₁` and $w R^n \subseteq \mathfrak{a}_\tau$ on each chart. Assume also `Good₂` on each chart.

**Theorem.** Then `CkRelations` holds for all chart bundles with the lattices of $D$.

## Proof

1. `lattice_family_model_chern` gives coordinates $z$ such that $(x, z)$ is a model of dimension $d$ on which each family of ideals `xId` is a line. It uses only `Good₁`.
2. `lattice_family_injective_model` shows that the pulled family is a lattice family, and that `Good₁`, the inclusion and `Good₂` pass to it. In its statement, the transfer of `Good₂` needs the inclusion $w R^n \subseteq \mathfrak{a}_\tau$ as well.
3. `chart_rings_noetherian_fraction` shows that the function field of $(x, z)$ is $\Omega$.
4. `stage4` on $(x, z)$ gives the relations there, and `descend` brings them back to $x$.

For a label $\tau$ and an index $i$, the ideal `xId` on a chart is the set of $c \in \Omega$ with $c \cdot (y \mapsto \chi_\tau(y_i)) \in M + V_{i+1}$, where $V_{i+1}$ is the space of functions on $F^n$ that vanish when the coordinates $y_j$, $j \geq i + 1$, are all $0$ (`vanSub`). It is a line (`IsLine`) if there are $u \neq 0$ in $\Omega$ and degrees $a$ such that on each chart $s$ the ideal is $R_s \cdot u\, m_s(a)$, with $m_s(a)$ the chart monomial $\prod_k x_{k, s_k}^{a_k}$.

## In the Lean code

The theorem is in [DescentRelationsFromModels.lean](lean:Development/AutomorphicSpectrum/Proofs/AlgebraProofs/DescentRelationsFromModels.lean#L126). `xId` is in [LieLatticeData.lean](lean:Development/AutomorphicSpectrum/Definitions/CommutativeAlgebra/LieLatticeData.lean#L87) and `IsLine` in [TrivFlagMod.lean](lean:Development/AutomorphicSpectrum/Definitions/CommutativeAlgebra/TrivFlagMod.lean#L37). It is a refinement step with the same form as [`stage2`](/entry/stage2/). The content is in `lattice_family_model_chern`, a statement form that we have not opened. Its name speaks of Chern classes, but its conclusion is only that the ideals are lines.
