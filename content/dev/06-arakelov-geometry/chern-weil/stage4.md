---
id: stage4
title: The Chern number relations, given that the ideals are lines
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Num.CkTop.stage4
module: Development.AutomorphicSpectrum.Proofs.AlgebraProofs.DescentRelationsFromModels
covers: 326
status: drafted
drafted_by: writer@claude
---
This theorem is the sixth link of the chain of [`ckRelations_of_model`](/entry/ck-relations-of-model/). It passes to a finer model with normal charts and then calls [`stage5`](/entry/stage5/). Its one user is [`stage3`](/entry/stage3/). It only passes hypotheses along; the content is in `stage5` and the lemmas it calls.

## Statement

Take the setting of [`stage3`](/entry/stage3/): $O$ of characteristic $0$, a model $x$ of dimension $d$ with function field $\Omega$, a prime $p$, a lattice family $D$ with `Good₁`, $w R^n \subseteq \mathfrak{a}_\tau$ and `Good₂` on each chart. Assume also that for each label $\tau$ and index $i$ the ideals `xId` form a line (`IsLine`), as defined in [`stage3`](/entry/stage3/).

**Theorem.** Then `CkRelations` holds for all chart bundles with the lattices of $D$.

## Proof

1. `model_refinement_exists` gives coordinates $z$ such that $(x, z)$ is a model of dimension $d$ whose chart rings are integrally closed in $\Omega$ (`NormalCharts`). This is the one place where the characteristic $0$ is used.
2. `lattice_family_injective_model` shows that the pulled family is a lattice family, and that `Good₁`, `Good₂` and the lines pass to it. The inclusion $w R^n \subseteq \mathfrak{a}_\tau$ is needed only to unlock the transfer of `Good₂`.
3. `chart_rings_noetherian_fraction` shows that the function field of $(x, z)$ is $\Omega$.
4. `stage5` on $(x, z)$ gives the relations there, and `descend` brings them back to $x$.

## In the Lean code

The theorem is in [DescentRelationsFromModels.lean](lean:Development/AutomorphicSpectrum/Proofs/AlgebraProofs/DescentRelationsFromModels.lean#L117). The lemmas in steps 1 to 3 are statement forms whose proofs we have not opened. The transfer lemma also gives the inclusion $w R^n \subseteq \mathfrak{a}_\tau$ on the new model, but the proof throws it away (line 123), because `stage5` does not ask for it. On this link the inclusion is used only to move `Good₂`.
