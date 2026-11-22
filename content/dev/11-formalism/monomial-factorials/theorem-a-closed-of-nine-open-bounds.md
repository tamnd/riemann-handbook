---
id: theorem-a-closed-of-nine-open-bounds
title: Summing the level dimension bounds over the levels
kind: theorem
decl: Formalism.MainNotions.G.SymmetricFormBlocks.theorem_A_closed_of_nine_open_bounds
module: Formalism.SharpRestriction.GrowthBounds.MonomialFactorials.RestrictedBoundsWeakenFromNineToEight
covers: 2450
status: drafted
drafted_by: writer@claude
---
This theorem is the twelfth link of the chain of reductions that proves the averaged bad-share bound `IntegralityFromMetricForLargeConstants D` (see [`theorem_A_closed_form_holds`](/entry/theorem-a-closed-form-holds/)). [`integrality_from_metric_of_orthogonality_window`](/entry/integrality-from-metric-of-orthogonality-window/) calls it. It replaces a dimension bound at each level by its sum over the levels, and passes the result on to [`theorem_A_closed_of_eight_open_bounds`](/entry/theorem-a-closed-of-eight-open-bounds/). The only new fact is a proved inequality between dimensions.

## Statement

The nest of quantifiers $\mathcal{T}$ and `RestWin` $C_M$ are as in [`integralityFromMetric_of_orthBasisLat`](/entry/integrality-from-metric-of-orth-basis-lat/), and `RestLvlDim` is as in [`closed_of_symmetric_dims`](/entry/closed-of-symmetric-dims/). We use the same notation. For $a_{\mathrm{top}} \in A^s$, $a_+ \in A$ and a block $b$ with `Kept`, let $G$ be the block datum `gB`, let $\mathrm{lv}$ be its finite set of levels, and let $\mathrm{gens}_x$ be the generators of $G$ at the level $x$. These are polynomials over $\mathbb{Q}_p$. Let $S$ be the $\mathbb{Z}_p$-span of all of them (`SSZ`), and let $V$ be the $\mathbb{Q}_p$-span of $S$.

- `RestDirQ`: $\sum_{x \in \mathrm{lv}} r_L(x) \le \dim_{\mathbb{Q}_p} V$.
- `RestOpen9E D`: $\mathcal{T}$ of the statement "for all $C_\kappa, C_s$, all $C_M \ge 1$ and each $X$ with `AdmNoK`, `HI` implies `RestBClvl`, `RestOrth` $C_M$, `RestWin` $C_M$ and `RestLvlDim`".
- `RestOpen8E D`: the same, with `RestDirQ` in place of `RestLvlDim`.

`RestBClvl` is stated in [`theorem_A_closed_of_eight_open_bounds`](/entry/theorem-a-closed-of-eight-open-bounds/), and `RestOrth` in [`closed_of_open_base_dims`](/entry/closed-of-open-base-dims/).

**Theorem.** For each datum $D$, `RestOpen9E D` implies `IntegralityFromMetricForLargeConstants D`.

## Proof

The lemma `restricted_bounds_weaken_from_nine_to_eight` proves `RestOpen8E D` from `RestOpen9E D`. It opens the nest with `thr_mono` and keeps the first three conditions. The fourth comes from `restDirQ_of`. Sum `RestLvlDim` over the levels:

$$\sum_{x} r_L(x) \le \sum_{x} \dim_{\mathbb{Q}_p} \langle \mathrm{gens}_x \rangle \le \dim_{\mathbb{Q}_p} V.$$

The second inequality is `RestSumSpan`, which `restSumSpan_proved` proves with no hypothesis. Its proof calls `sum_gens_le`: the spans $\langle \mathrm{gens}_x \rangle$ for distinct levels are independent (`Formalism.GM.semisimple_direct_sum`, whose statement we have not unfolded), and all lie in $V$. So the sum of their dimensions is at most $\dim V$ (`sum_finrank_le_of_indep`). Then `theorem_A_closed_of_eight_open_bounds` is applied. The rest is bookkeeping.

## In the Lean code

The theorem is in [RestrictedBoundsWeakenFromNineToEight.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/RestrictedBoundsWeakenFromNineToEight.lean#L23), with `RestOpen9` at line 10, `RestOpen9E` at line 14 and the weakening lemma at line 18. The lemmas it calls:

- `thr_mono`, in [CountingStatementReduction.lean](lean:Formalism/SharpRestriction/GrowthBounds/CountingStatementReduction.lean#L2456).
- `restDirQ_of`, with `RestLvlDim` and `RestSumSpan`, in [RestSumSpan.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/RestSumSpan.lean#L29). `RestDirQ` is in [RestDirOf.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/RestDirOf.lean#L11).
- `restSumSpan_proved` and `sum_gens_le`, in [SumFinrankLeOfIndep.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/SumFinrankLeOfIndep.lean#L99).

The number nine is a stage label: `RestOpen9` has four conditions, not nine. The labels count down to `RestOpen4E` in [`closed_of_open_directions`](/entry/closed-of-open-directions/). The lemma `restDir_of_lvl` in RestDirOfLvl.lean, which this file imports, does this link and the link of [`closed_of_open_dimensions`](/entry/closed-of-open-dimensions/) in one step. We found no use of it in the source.
