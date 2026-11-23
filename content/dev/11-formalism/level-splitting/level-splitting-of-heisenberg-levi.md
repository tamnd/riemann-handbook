---
id: level-splitting-of-heisenberg-levi
title: The level splitting from the Heisenberg and Levi parts
kind: theorem
decl: PI.LevelKSplit.W.Top6.levelSplitting_of_heisenberg_levi
module: Formalism.PeriodIntegrals.UnitaryGroupMassFormula.LevelSplitting.LevelSAllOfHL
covers: 335
status: drafted
drafted_by: writer@claude
---
This theorem proves `LevelSAll`, the splitting of the Haar volume of a level subgroup, from two facts about a unipotent group: a Heisenberg part and a Levi part. It is a pass-through. Its only user is [the level splitting for all CM extensions](/entry/level-s-all-split/), which proves the two facts.

## Statement

Fix a CM extension $E/F$ and a nondegenerate Hermitian form $J$. Take a standard frame $(e, f, z)$ with $h(z, z) = -T \ne 0$. Let $S$ be the subgroup that is unipotent on the flag $(e_1, \dots, e_r, z)$. Let $H$ fix $e$, $z$ and $f$, and let $N$ be the unipotent part `Nsub`. `LevelS` says: for adapted lattices and Haar measures $\mu_N, \mu_H$, there is a Haar measure $\mu_S$ with $\int \varphi\, d\mu_S = \int\int \varphi(nh)\, d\mu_H\, d\mu_N$. Each such $\mu_S$ gives $\mu_S(K_S) = \mu_N(N_O) \cdot \mu_H(K_H)$, where $K_S, N_O, K_H$ are the parts that keep the lattice. `LevelSAll` asks this for all $E/F$ and $J$.

Let $W'$ be the vectors orthogonal to all $e_a$ and $f_a$. `HeisP` asks for a continuous section $s_H$ from $W'^r$ into the level unipotent subgroup. Each element of that subgroup is $s_H(y)\, \zeta$ with $\zeta$ in a central subgroup $Z$. `LevP` asks for a closed subgroup $A \le N$ and a continuous map $\mathrm{Lev}: N \to A$ with $\mathrm{Lev}(n)^{-1} n$ in the level unipotent subgroup. Both also ask for compatibility with $H$.

**Theorem.** `HeisPAll` and `LevPAll` imply `LevelSAll`.

## Proof

`levelSAll_of_semiNHS_heis_lev` takes the two hypotheses and three proved lemmas: `semidirect_topological_all` ($S = N \rtimes H$), `modulus_all_extensions` (unitary elements keep additive Haar measure) and `normal_conjugation_all`. From `HeisP` and `LevP` it builds a homeomorphism $A \times W'^r \times Z \cong N$ (`ncoord_of_parts`).

## In the Lean code

The theorem is at [LevelSAllOfHL.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/LevelSplitting/LevelSAllOfHL.lean#L9). `LevelS` is in [LevelKSplit.lean](lean:Formalism/PeriodIntegrals/LevelKSplit.lean#L27). `HeisP` and `LevP` are in [NCIface.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/LevelSplitting/NCIface.lean#L16). The main lemma is in [LevelSAllOfSemiNHSHeisLev.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/LevelSplitting/LevelSAllOfSemiNHSHeisLev.lean#L80). We have not unfolded the proofs of the three lemmas.
