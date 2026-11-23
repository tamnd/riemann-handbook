---
id: theorem-a-closed-of-eight-open-bounds
title: From a rank bound at each level to a rank bound for the block lattice
kind: theorem
decl: Formalism.MainNotions.G.SymmetricFormBlocks.theorem_A_closed_of_eight_open_bounds
module: Formalism.SharpRestriction.GrowthBounds.MonomialFactorials.RestrictedBoundsWeakenFromEightToSeven
covers: 2398
status: drafted
drafted_by: writer@claude
---
This theorem is the thirteenth link of the chain of reductions that proves the averaged bad-share bound `IntegralityFromMetricForLargeConstants D` (see [`theorem_A_closed_form_holds`](/entry/theorem-a-closed-form-holds/)). [`theorem_A_closed_of_nine_open_bounds`](/entry/theorem-a-closed-of-nine-open-bounds/) calls it. It replaces a rank bound at each level by a rank bound for the whole block lattice, and passes the result on to [`closed_of_open_base_dims`](/entry/closed-of-open-base-dims/).

## Statement

The notation is that of [`theorem_A_closed_of_nine_open_bounds`](/entry/theorem-a-closed-of-nine-open-bounds/), where `RestOpen8E D` is also stated. Let $O$ be the discrete valuation ring `X.O` of the instance and $K$ its fraction field (`KK`). The block datum $G$ is `gmB` applied to a datum $G^O$ over $O$ (`blockData`). Let $\mathrm{gens}^O_x$ be the generators of $G^O$ at the level $x$, and let $S^O$ be their $O$-span. Let $\Lambda_x$ be the $\mathbb{Z}_p$-lattice `Ljj` of $G$ at $x$, and let $M$ be the $O$-lattice `blockLat` of the block.

- `RestBClvl`: for each level $x \in \mathrm{lv}$, $\dim_K \langle \mathrm{gens}^O_x \rangle_K \le \operatorname{rk}_{\mathbb{Z}_p} \Lambda_x$.
- `RestBCdim`: $\operatorname{rk}_O M \le \sum_{x \in \mathrm{lv}} \operatorname{rk}_{\mathbb{Z}_p} \Lambda_x$.
- `RestOpen7E D`: as `RestOpen8E D`, with `RestBCdim` in place of `RestBClvl`.

Both conditions are quantified over $a_{\mathrm{top}} \in A^s$, $a_+ \in A$ and blocks $b$ with `Kept`. We have not unfolded `blockLat`, `Ljj` or the generators.

**Theorem.** For each datum $D$, `RestOpen8E D` implies `IntegralityFromMetricForLargeConstants D`.

## Proof

The lemma `restricted_bounds_weaken_from_eight_to_seven` proves `RestOpen7E D` from `RestOpen8E D`. It opens the nest with `thr_mono`, keeps the last three conditions and replaces the first by `restBCdim_of`. That lemma has three steps.

1. `finrank_blockLat` gives $\operatorname{rk}_O M = \dim_K \langle S^O \rangle_K$ (this is `blockRank`). It uses `valuation_properties_hold`, whose statement we have not unfolded.
2. Each generator of $S^O$ lies in $\mathrm{gens}^O_x$ for a level $x$ that satisfies `LevelOK`, and `mem_levels_iff'` says that these $x$ are the elements of $\mathrm{lv}$. So $\langle S^O \rangle_K \subseteq \sum_{x \in \mathrm{lv}} \langle \mathrm{gens}^O_x \rangle_K$, by induction on the span.
3. The dimension of a finite sum of subspaces is at most the sum of their dimensions (`finrank_biSup_le`). Then `RestBClvl` bounds each term.

Then `closed_of_open_base_dims` is applied. The rest is bookkeeping.

## In the Lean code

The theorem is in [RestrictedBoundsWeakenFromEightToSeven.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/RestrictedBoundsWeakenFromEightToSeven.lean#L23), with `RestOpen8` at line 10, `RestOpen8E` at line 14 and the weakening lemma at line 18. The lemmas it calls:

- `thr_mono`, in [CountingStatementReduction.lean](lean:Formalism/SharpRestriction/GrowthBounds/CountingStatementReduction.lean#L2456).
- `RestBClvl`, `mem_levels_iff'` and `restBCdim_of`, in [MemLevelsIff.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/MemLevelsIff.lean#L34). `RestBCdim` is in [BlockBoundUniformiser.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/BlockBoundUniformiser.lean#L121).
- `finrank_blockLat`, in [CountingStatementReduction.lean](lean:Formalism/SharpRestriction/GrowthBounds/CountingStatementReduction.lean#L3717).
- `finrank_biSup_le`, in [FinrankSpanImageLe.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/FinrankSpanImageLe.lean#L74).

`RestBClvl` itself is proved one link up, in [`integrality_from_metric_of_orthogonality_window`](/entry/integrality-from-metric-of-orthogonality-window/), from the hypothesis `RestYbc` by `restBClvl_of`. As with the other links, "eight" is a stage label: `RestOpen8` has four conditions.
