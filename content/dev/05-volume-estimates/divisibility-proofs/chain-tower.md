---
id: chain-tower
title: The chain of tower estimates
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Top.chain_tower
module: Development.AutomorphicSpectrum.Proofs.DivisibilityProofs.TowerWeilInputsCombined
covers: 1193
status: drafted
drafted_by: writer@claude
---
This theorem turns seventeen properties of a root tower into its four main estimates: the limit `T1`, the height formula `ThmB`, the lower bound `T2` and the mean slope bound `MeanSlope`. It has no geometry of its own. It puts twelve lemmas in a row. Its statement form is [`tower_weil_inputs_combined`](/entry/tower-weil-inputs-combined/), and its user is [the volume theorem for good root towers](/entry/volume-theorem-x-of-inputs/), where the notation is set up.

## Statement

**Theorem.** Assume `PB.FlagHeight`, `PB.Inputs`, the two successive minima bounds of Zhang (see [heights](/learn/arakelov/#heights)), `AntisymPerturbation.Statement` and `GrassmannianHeightZTwo.Statement`. Let $II$ be a full intersection system, $\Psi$ a nonempty finite set, $T$ a root tower, $\mathrm{frob}$ a choice of Frobenius data, and $C, C' \geq 0$, $\mathrm{rd} \geq 1$. Assume:

- `FrobShape`: for each $p$ and $n$, $\mathrm{frob}(p, \tau, n)$ is on the same side for all $\tau$;
- `Proportional`, `VolEq`: the volumes are positive, equal, and give the geometric degrees;
- `I1`, `I2`: the intersection numbers of monomials are $O(\log B)$, and the perturbation by $s$ changes the top numbers by $O(s)$;
- `A1`, `ModelNefStatement`, `M2`, `ANef`, `I7`: semipositivity and nefness of the lines;
- `I5`, `I6`: lower bounds $-C\log(B/s)$ for the heights of all points, and a Zariski dense set of points of height at most $C \log B$;
- `I8`: the [antisymmetry](/entry/full-intersection-tower-i8-identity/) of $\mathrm{PP}_{B,c} - \mathrm{vol}(c)\,h_{\mathrm{Fl}}$ under swaps of adjacent entries $a, a+1$ with $a + 1 \neq j$;
- `Prop6`: from $B_0$ to $B$, $\mathrm{PP}_{B,c}(p_k Q)$ changes by $\mathrm{vol}(c)$ times a sum of local terms over the good primes in $(B_0, B]$;
- `PropA`: $\mathrm{PP}_B$ is invariant under a subgroup of permutations of $\Psi$ that acts transitively;
- `PropF`: $\mathrm{PP}_{B,c}(p_1 Q) = h\,\mathrm{vol}(c)\deg_{\mathrm{Fl}} Q$ with $|h| \leq C' N \Lambda_B$;
- `SlopeLower`: a lower bound with constant $C$ for $\mathrm{PP}_B$ of one test polynomial.

Then $T$ has `T1` and `ThmB`, and has `T2` and `MeanSlope` with the constant $2C + 3C' + 5$.

## Proof

From $1 \leq j < N$ we get $N \geq 2$.

1. `tower_I3_of_semipositive_nef` gives `I3`, nefness and semipositivity for small perturbations, from `A1`, `ModelNefStatement`, `M2`, `ANef`.
2. `tower_T1_limit` gives `T1` from `Proportional`, `I2`, `I3`.
3. `tower_weil_theorem` gives `ThmW`: $|\mathrm{PP}_B(L_\lambda^{d+1})| \leq C \log B / B$ for $\lambda$ on a wall. It uses a part of `PB.Inputs`, two more published inputs, the two Zhang bounds and `Proportional`, `I1`, `I2`, `I3`, `I5`, `I6`, `I7`.
4. `flag_height_I9_properties` gives `I9`: $h_{\mathrm{Fl}}(L_\lambda^{d+1})$ vanishes for dominant $\lambda$ with two equal adjacent entries, is nonnegative on dominant weights and vanishes on $p_1 Q$.
5. `tower_theorem_B` gives `ThmB` from `AntisymPerturbation.Statement`, `ThmW`, `I8` and `I9`.
6. `flag_variety_boundary_dimension_drop` shows that the flag model has dimension $d + 1$. Then `flag_height_label_invariant` shows that $h_{\mathrm{Fl}}$ is invariant under permutations of $\Psi$, and `tower_theorem_B_averaged` with `PropA` makes $\alpha, \beta$ constant.
7. `flag_height_test_bound` bounds $h_{\mathrm{Fl}}$ of the test polynomial. With `PropF` and `SlopeLower`, `test_height_bound` bounds the coefficient $A_0$ below by $-(2(C + C') + 3)\Lambda_{B_0}$.
8. `tower_T2` gives `T2` with constant $2(C+C') + 3 + C' + 2 = 2C + 3C' + 5$, from `Prop6`, `ThmBA`, `PropF` and step 7.
9. `mean_slope_proportional_volume` gives `MeanSlope` from `Proportional`, `VolEq` and `T2`.

## In the Lean code

The theorem is in [TowerWeilInputsCombined.lean](lean:Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/TowerWeilInputsCombined.lean#L22). The properties are in [Proportional.lean](lean:Development/AutomorphicSpectrum/Definitions/DivisibilityTowers/Proportional.lean#L67) and [HeckeSectionsIsotropicCommutatorPairingPower.lean](lean:Development/AutomorphicSpectrum/Definitions/DivisibilityTowers/HeckeSectionsIsotropicCommutatorPairingPower.lean#L48). All hypotheses are used. Step 3 takes the sixth part of `PB.Inputs` by position. The dimension $d$ appears as `antisymDegree` in one lemma and as `dimFl` in another, and a `simp` step shows that they are equal. The bound variable in `I3` is named `abelian₂`, a name with no relation to its role. We have not unfolded the twelve lemmas.
