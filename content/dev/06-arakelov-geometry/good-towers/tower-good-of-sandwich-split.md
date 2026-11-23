---
id: tower-good-of-sandwich-split
title: The height bounds of a good tower from a sandwich at each prime
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.TopGood.tower_good_of_sandwich_split
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.TowerIntersectionOfSandwichSplit
covers: 819
status: drafted
drafted_by: writer@claude
---
This theorem proves the two height bounds `I5` and `I6` for a root tower with a good origin. These bounds have the form of the hypotheses of the two successive minima bounds (see [the Siegel lemma entry](/entry/line-of-large-degree-of-use/)): a lower bound for the heights of all points, and an upper bound on a dense set. Its one user is the renaming [`T.tower_intersection_of_sandwich_split`](/entry/tower-intersection-of-sandwich-split/).

## Statement

A root tower $T$ (`Top.RootTower`) is a family of root models $M_{B,c}$, one for each $B$ and each component $c$. Each root model is an arithmetic variety with hermitian line bundles $x_r$, indexed by a CM type and $N = p + q$ positions. A good origin $g$ (`Top.GoodOrigin`) gives the tower its geometry: Hodge components $\mathfrak{M}$ at each $B$ and $c$, a finite set $S_B$ of primes, and a reference root model $R_c$ for each component with a flag and root lines. Let $II$ be an intersection system and $h_{II}$ the height of points that it defines (`mbarHt`).

- `I5`: for each $c_0 > 0$ there are $\theta_0 > 0$ and $C$ such that for all $B \geq 2$, each component and each rational weight $\lambda$ with $\|\lambda\| \leq 1$ and gaps at least $\theta$, and $s = \theta^2$, every point $W$ has $h_{II}(W) \geq -C \log(B/s)$.
- `I6`: under the same conditions, there is a Zariski dense set of points $W$ with $h_{II}(W) \leq C \log B$.

The sandwich condition at a prime $p$ says: at each point of the fibre at $p$, two integral lattices of the Lie model, `M.omLat` and the lattice `omP` built from the $p^{R}$-torsion, contain each other up to the factor $\kappa$, and the same holds for the de Rham lattices. Here $\kappa = \zeta_p - 1$ for a primitive $p$-th root of unity $\zeta_p$, and $\kappa = 4$ for $p = 2$ (`HT.IsCp`).

**Theorem.** Assume `Top.Given` and `Flat.FlatLineGenerator`. Let $T$ have a good origin $g$ over a model $Y$ with split components (`SplitComps`), and let $II$ satisfy the axioms `IsIntersectionSystem`. If the sandwich condition holds for each $B$, each component and each $p \in S_B$, then `I5` and `I6` hold.

## Proof

1. From the sandwich condition, `has_reference_of_sandwich_all_primes` gives `Ht.HasRef`: the reference models $R_c$ are close to the models $M_{B,c}$, with errors of size $C \log B$.
2. `I6` follows from `HasRef` alone, by `tower_i6_of_reference`.
3. `I5` follows from `HasRef` and three facts on each $R_c$, by `tower_i5_of_fibre_input` (through `tower_intersection_of_ample_flat`, which only writes $p = j + 1$ and $q = k + 1$):
   - the line $A$ of $R_c$ is ample (`AmpleQ`), a field of the good origin;
   - `FlatUnit`, from `flat_unit_of_split_root_lines`, which uses the flat line generator and the split components;
   - `FibreInput`, from [`root_model_flag_height`](/entry/root-model-flag-height/), which uses five parts of `Top.Given`: `PartI`, `N1ab`, `SemiAbelianHomExtension`, `ResKStatement` and `SlopeBoundSt`.

The bounds $1 \leq p$ and $1 \leq q$ come from $1 \leq j < N$ in the tower. The rest is bookkeeping.

## In the Lean code

The theorem is in [TowerIntersectionOfSandwichSplit.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/TowerIntersectionOfSandwichSplit.lean#L27). The definitions of `I5` and `I6` are in [Proportional.lean](lean:Development/AutomorphicSpectrum/Definitions/DivisibilityTowers/Proportional.lean#L94), and `HasRef`, `FlatUnit` and `FibreInput` in [ArchBetween.lean](lean:Development/AutomorphicSpectrum/Definitions/GlobalGeometry/ArchBetween.lean#L66). The lemmas:

- `T.has_reference_of_sandwich_all_primes` in [HasReferenceOfSandwichAllPrimesStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/HasReferenceOfSandwichAllPrimesStatement.lean#L11);
- `T.tower_i5_of_fibre_input`, `T.tower_i6_of_reference` and `T.flat_unit_of_split_root_lines`, each in a file `<Name>Statement.lean` of the same folder.

The last lemma and `root_model_flag_height` are applied with the empty set of primes for the Hodge component of the reference.

Of the fourteen parts of `Top.Given`, the proof uses five. We have not opened the proofs of the four lemmas.
