---
id: stage1b
title: The Chern number relations on a model with normal charts
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Num.CkTop.stage1b
module: Development.AutomorphicSpectrum.Proofs.AlgebraProofs.DescentRelationsFromModels
covers: 421
status: drafted
drafted_by: writer@claude
---
This theorem is the third link of the chain of [`ckRelations_of_model`](/entry/ck-relations-of-model/). It does not change the model. On normal charts it proves the condition $w R^n \subseteq \mathfrak{a}_\tau$, and then it calls [`stage2`](/entry/stage2/). Its one user is [`stage1`](/entry/stage1/), which supplies the normal charts.

## Statement

Take the setting of [`stage1`](/entry/stage1/): $O$ of characteristic $0$, a model $x$ of dimension $d$ with function field $\Omega$, a prime $p$, a lattice family $D$ with `Good₁` on each chart. Assume also that each chart ring $R$ is integrally closed in $\Omega$ (`NormalCharts`).

**Theorem.** Then `CkRelations` holds for all chart bundles with the lattices of $D$.

## Proof

Fix a chart with ring $R$ and a label $\tau$. Let $M_1 = M + pR^{F^n}$ (`l1`), and let $\mathfrak{a}_\tau \subseteq \Omega^n$ be the set of $v$ with $\sum_i v_i\, \chi_\tau(y_i) \in M_1$ as a function of $y \in F^n$ (`af`). The lemma `hodge_annihilator_lattice_holds` gives $w R^n \subseteq \mathfrak{a}_\tau$. Its inputs are:

- `CharData`: $p \neq 0$ in $\Omega$, $w \in R$, $p = c w$ with $c \in R$, $\chi_\tau(0) = 0$, $\chi_\tau(1) = 1$ and all values of $\chi_\tau$ in $R$. The helper `charData_of` proves it from `IsLatticeFamily`, with $c = u^{-1} w^{p-2}$ from $w^{p-1} = u p$.
- the fields `Base` and `TestFacts` of the lattice family;
- $R$ Noetherian with fraction field $\Omega$, from `chart_rings_noetherian_fraction`;
- $R$ integrally closed in $\Omega$, and `Good₁`.

Then `stage2` with this inclusion gives the relations.

## In the Lean code

The theorem is in [DescentRelationsFromModels.lean](lean:Development/AutomorphicSpectrum/Proofs/AlgebraProofs/DescentRelationsFromModels.lean#L143), and `charData_of` is at [line 40](lean:Development/AutomorphicSpectrum/Proofs/AlgebraProofs/DescentRelationsFromModels.lean#L40). The proof is one term. We have not opened the proof of `hodge_annihilator_lattice_holds` or unfolded `TestFacts`. `stage2` does not take normality as a hypothesis. [`stage4`](/entry/stage4/) makes the charts normal again for the last link.
