---
id: pins-finite-integrals
title: Finite integral laws for all tuples, from pinned level data and a lattice shape
kind: theorem
decl: GlobalTheory.SeeSaw.pins_finiteIntegrals
module: Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.SeeSawLatticeFramePinsFiniteIntegralLaws
covers: 1355
status: drafted
drafted_by: writer@claude
---
This theorem chooses the local constants of a see-saw argument once, and then proves the finite integral laws for every family of tuples that meets a list of local conditions. Its only user is the restatement [`seeSaw_latticeFramePins_finiteIntegralLaws`](/entry/see-saw-lattice-frame-pins-finite-integral-laws/), which [`lawsLinks_of_geo_rows_cols_alt`](/entry/laws-links-of-geo-rows-cols-alt/) calls. This is in branch 3 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/).

## Statement

Fix a datum $D$ and a common datum $c$ (`Comm D`): a chain of hermitian spaces $V_j$, $X_j$ and a top space $T$, with theta data, Jacquet and Bessel subgroups and Haar measures. Let $v$ be level data (`VCom c`): a finite set $P_G$ of level places, a disjoint finite set $P_T$ of twist places, lattices $N_j$, compact open subgroups $J_j$ at $P_G$, test vectors and operators. Let $K_j$ be the set of products $\kappa k$ with $\kappa$ in the stabiliser of $N_j$ off $P_G$ and $k \in J_j$. The volume ratio $\kappa(j, \sigma)$ (`v.kap`) is a product of two ratios $\mu(K_i)/\rho(K_i \cap R)$, for a Jacquet subgroup at $i = j+1$ and a Bessel subgroup at $i = j+2$.

The hypotheses:

- `c.Is` and `v.Is` (we have not listed their fields);
- `c.VolLast`: at the last step, the measure on $V_{j+1}$ is the pushforward of the measure of the lattice datum under an embedding;
- $k$ is a nonarchimedean local field and $o$ (`TDat`) is a lattice shape datum over $k$: split points, a uniformiser, characters of conductor 1, frames and lattices;
- `ShapeOff v o`: $o$ fits $v$ at the places off $P_T$ (good and split conditions, glued cores, a representation of the vacuum vectors, and equality of the ramified sets);
- `GPin G`: local data $G_1, \dots, G_n$ at distinct places with union $P_G$, such that $J_j$ is cut out by the local level conditions and the test vectors of $v$ at $P_G$ are products of local ones.

**Theorem.** There are units $\varepsilon$ of the ring of integers of $k$, operators `op`, reals $r_j(i) > 0$, integers $e_j(i)$ and constants $a_j \neq 0$ such that:

1. $\kappa(j, \sigma) \neq 0$ for all $j, \sigma$;
2. the modified data $v' = $ `(v.withT (o.S ε) op).withCG a` satisfy `Is`;
3. for each family $(t_s, w_s)$ of tuples and decorated tuples, if every $s$ meets twelve conditions, then each $t_s$ satisfies `LocFin`, and the family satisfies `ValX` and `ValLastX`.

The twelve conditions: $t_s$ satisfies `Is`; `VForm v' w_s`; `WeilOK` and `TopSph` for $v$; $t_s$ is unramified at the places outside $P_G$ and $Q$, and its theta kernels are unramified at $P_T$; the characters of $t_s$ fit each $G_i$; `QLaw`, `QLast` and `QFin` for $v$ and $w_s$ (see [laws-of-pin-resc](/entry/laws-of-pin-resc/)); $c_T(j) = \prod_i r_j(i)\, \chi(\varpi_i)^{e_j(i)}$, with $\chi$ the Weil character of $t_s$ and $\varpi_i$ the idele of the uniformiser at the split point $p_i$; and `CVEq v' w_s`, which ties the constant of $t_s$ to $\kappa$, the scales, $c_Q$, $a$ and $c_T$.

`LocFin` is a finiteness of cells: a compact open $K_1$ and a finite $T_1$ such that the nonzero terms of the integrand lie in the cells of $T_1$ and $K_1$ (we have not unfolded `InCell`). `ValX` and `ValLastX` say that the double step and last step integrals equal the constant of $t_s$ times a period, with a real constant $C$ that does not depend on $s$.

## Proof

1. `seesaw_levelPrime_law_all_tuples` (from `ShapeOff`) gives $\varepsilon$, `op`, $r$, $e$, the fact that `v.withT (o.S ε) op` satisfies `Is`, and a law `TLaw` for every tuple that meets its conditions.
2. `seeSawUnfolded_support_and_value_at_fixed_level` (from `GPin`) gives $a$ with $a_j \neq 0$, and the support law `GSupp` and value law `GValue` at $P_G$.
3. `is_withCG` gives (2), since `withCG` changes only the constants $c_G$.
4. `kap_ne_zero` gives (1). Each ratio is a quotient of two Haar measures of $K_i$. The set $K_i$ is open and compact and contains $1$ (`level_open_compact`, through the splitting `grp_split` of the finite adelic group at $P_G$). So both measures are positive (`real_pos_of_open_compact`).
5. For each $s$, build the twelve fields of `PlaceLaws v' w_s`. `OffLaw` comes from `seesaw_support_off_level_of_lattice_shape`, using that $Q$ and $P_T$ are disjoint (from `VForm`). `VacLaw` comes from `seeSawUnfoldedVacuaOfShape_proof`. `unrOn_mono` shrinks the unramified set to $P_T$, using that $P_T$ meets neither $P_G$ nor $Q$, and then step 1 gives `TLaw`. Step 2 gives `GSupp` and `GValue`. The other fields are hypotheses.
6. `seesaw_place_laws_give_finite_integral_laws` turns `PlaceLaws` into (3).

## In the Lean code

The theorem is at [SeeSawLatticeFramePinsFiniteIntegralLaws.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SeeSawLatticeFramePinsFiniteIntegralLaws.lean#L109). The helper lemmas of steps 3 to 5 are in the same file, lines 25 to 104. The definitions are in [VacOfShape.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/VacOfShape.lean#L88) (`ShapeOff`), [HzUnit.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/HzUnit.lean#L88) (`GPin`), [PlaceLaws.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/PlaceLaws.lean#L272) (`PlaceLaws`) and [ValLastX.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/ValLastX.lean#L186) (`ValX`). We have not opened the proofs of the four lemmas of steps 1, 2, 5 and 6.

All hypotheses and all twelve conditions are used. The statement asks for `WeilOK`, `TopSph`, `QLaw`, `QLast` and `QFin` for $v$, while `PlaceLaws` needs them for $v'$. The proof uses the laws for $v$ as laws for $v'$ with no conversion, and `weilOK_of_tau` with `rfl`. This works because `withT` and `withCG` change only the operators $S$, `op` and $c_G$, and these laws do not read them. For the same reason, (1) is stated for $v$ but also holds for $v'$, which `CVEq v' w_s` uses.
