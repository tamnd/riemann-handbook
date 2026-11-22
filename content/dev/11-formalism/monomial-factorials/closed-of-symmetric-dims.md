---
id: closed-of-symmetric-dims
title: Adding the level dimension bound to the window count
kind: theorem
decl: Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_symmetric_dims
module: Formalism.SharpRestriction.GrowthBounds.MonomialFactorials.SymmetryWindowOnAdmissible
covers: 2607
status: drafted
drafted_by: writer@claude
---
This theorem is the seventh link of the chain of reductions that proves the averaged bad-share bound `IntegralityFromMetricForLargeConstants D` (see [`theorem_A_closed_form_holds`](/entry/theorem-a-closed-form-holds/)). [`closed_of_orthogonal_lattice`](/entry/closed-of-orthogonal-lattice/) calls it. It adds a proved dimension bound to the window hypothesis and passes the rest on to [`closed_of_symmetric_windows`](/entry/closed-of-symmetric-windows/). It has no mathematical content of its own.

## Statement

`RestFunY` is stated in [`closed_of_orthogonal_lattice`](/entry/closed-of-orthogonal-lattice/), `OrthLat` in [`closed_of_orthogonal_basis`](/entry/closed-of-orthogonal-basis/), and `SymmetryWindowOnAdmissible D` (with `RestSymm`, `RestWin` and the nest of quantifiers $\mathcal{T}$) in [`integralityFromMetric_of_orthBasisLat`](/entry/integrality-from-metric-of-orth-basis-lat/).

- `RestLvlDim`: for each $a_{\mathrm{top}} \in A^s$, each $a_+ \in A$, each $b$ with `Kept` and each $x$ in the set `lv`, the number $r_L(a_{\mathrm{top}}, b, x)$ (`rL`) is at most the $\mathbb{Q}_p$-dimension of the span of the generators of the block datum at $x$. We have not unfolded `Kept`, `lv`, `rL` or `gens`.
- `SymmetryWindowLevelDimOnAdmissible D`: as `SymmetryWindowOnAdmissible D`, but `HI` implies `RestSymm`, `RestWin` $C_M$ and `RestLvlDim`.

**Theorem.** For each datum $D$, `RestFunY`, `OrthLat` and `SymmetryWindowOnAdmissible D` imply `IntegralityFromMetricForLargeConstants D`.

## Proof

The lemma `windows_of_symmetric_dims` proves `SymmetryWindowLevelDimOnAdmissible D` from `SymmetryWindowOnAdmissible D`. It uses `thr_mono`, which says that $\mathcal{T}(P)$ implies $\mathcal{T}(Q)$ when $P$ implies $Q$ for all constants. The step from $P$ to $Q$ adds `RestLvlDim` from `lvlDimCondition`, which holds for all $X$ and all constants with no hypothesis. Then `closed_of_symmetric_windows` is applied to `RestFunY`, `OrthLat` and the new statement. The rest is bookkeeping.

## In the Lean code

The theorem is in [SymmetryWindowOnAdmissible.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/SymmetryWindowOnAdmissible.lean#L22), with `SymmetryWindowOnAdmissible` at line 13 and `windows_of_symmetric_dims` at line 17. The lemmas it calls:

- `thr_mono`, in [CountingStatementReduction.lean](lean:Formalism/SharpRestriction/GrowthBounds/CountingStatementReduction.lean#L2456).
- `lvlDimCondition`, in [LvlDimCondition.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/LvlDimCondition.lean#L68). `RestLvlDim` is in [RestSumSpan.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/RestSumSpan.lean#L11).
- `closed_of_symmetric_windows`, in [SymmetryWindowLevelDimOnAdmissible.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/SymmetryWindowLevelDimOnAdmissible.lean#L23).

The hypotheses `hF`, `hO` and `h` pass through unchanged. The file is named after the definition `SymmetryWindowOnAdmissible`, not after the theorem. The two lemma names are swapped in sense: `windows_of_symmetric_dims` adds the dimension bound, and `symmetric_dims_of_windows` (in [`integralityFromMetric_of_orthBasisLat`](/entry/integrality-from-metric-of-orth-basis-lat/)) adds only the symmetry.
