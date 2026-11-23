---
id: level-s-all-split
title: The level subgroup of the flag group splits as unipotent part times stabilizer
kind: theorem
decl: level_s_all_split
module: Formalism.PeriodIntegrals.OrbitalBoundsConclusion.LevelKSplit
covers: 560
status: drafted
drafted_by: writer@claude
---
This theorem proves `LevelSAll`: for a group $S$ attached to the flag of a standard frame, the level subgroup $S \cap K_f$ has Haar volume equal to the product of the volumes of the level subgroups of a unipotent part $N$ and of a tuple stabilizer $H$. It lies below the step [HypsAlt is nonempty from the closed bound](/step/nonempty-hyps/). It is a pass-through: it applies [`levelSplitting_of_heisenberg_levi`](/entry/level-splitting-of-heisenberg-levi/) to two proved theorems, and that entry has the real content.

## Statement

Let $E/F$ be a CM extension, $J$ a nondegenerate Hermitian matrix, and $(e, f, z)$ a standard frame: $e$ and $f$ span hyperbolic planes, $z$ is orthogonal to them, and $h(z,z) = -T \neq 0$. Over the finite adeles let

- $S$ be the group of $g$ such that $g e_b - e_b$ lies in the span of the earlier vectors of the tuple $(e, z)$;
- $H$ be the stabilizer of the tuple $(e, z, f)$;
- $N$ be the group that is unipotent on $e$ and moves each $v \perp e$ inside $\operatorname{span}(e)$.

Let $\Lambda_X \subseteq \operatorname{span}(e)$, $\Lambda_Y \subseteq \operatorname{span}(f)$, and $\Lambda_W$ orthogonal to all $e_a$ and $f_a$. Let $K_f$ stabilize the $\mathcal O_v$-span of $\Lambda = \Lambda_X \cup \Lambda_W \cup \Lambda_Y$ at each finite place.

**Theorem.** For Haar measures $\mu_N$ on $N$ and $\mu_H$ on $H$, there is a Haar measure $\mu_S$ on $S$ with $\int_S f\,d\mu_S = \int_N \int_H f(mh)\,d\mu_H\,d\mu_N$. For every such $\mu_S$,
$$\mu_S(S \cap K_f) = \mu_N(N \cap K_f)\,\mu_H(H \cap K_f).$$

## Proof

The proof passes the proved theorems `heisenberg_parabolic_all` and `levi_part_all` to [`levelSplitting_of_heisenberg_levi`](/entry/level-splitting-of-heisenberg-levi/).

## In the Lean code

The theorem is in [LevelKSplit.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/LevelKSplit.lean#L7). `LevelSAll` is in [LevelKSplit.lean](lean:Formalism/PeriodIntegrals/LevelKSplit.lean#L47) and `LevelS` at line 27 of that file.

`LevelSAll` quantifies over $J$ with `IsHermND`, and `LevelS` asks `IsHermND` again. The sets $\Lambda_X, \Lambda_W, \Lambda_Y$ are arbitrary sets of vectors, not lattices. One caller, [ProductDecompositionHolds.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/WeightedMeasureSplitting/ProductDecompositionHolds.lean#L38), passes the empty sets and uses only the existence of $\mu_S$.
