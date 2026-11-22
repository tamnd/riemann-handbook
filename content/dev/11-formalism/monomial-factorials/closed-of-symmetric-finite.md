---
id: closed-of-symmetric-finite
title: Orthogonal families in the block lattices from symmetry and finiteness
kind: theorem
decl: Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_symmetric_finite
module: Formalism.SharpRestriction.GrowthBounds.MonomialFactorials.SymmetryFinitenessWindowLevelDimOnAdmissible
covers: 2472
status: drafted
drafted_by: writer@claude
---
This theorem is the tenth link of the chain of reductions that proves the averaged bad-share bound `IntegralityFromMetricForLargeConstants D` (see [`theorem_A_closed_form_holds`](/entry/theorem-a-closed-form-holds/)). [`closed_of_coefficient_function`](/entry/closed-of-coefficient-function/) calls it. It applies the abstract lattice statement `OrthLat` to each block lattice, and so replaces the symmetry and the finiteness of the lattices by an orthogonal family in each of them. Then it passes the rest on to [`integrality_from_metric_of_orthogonality_window`](/entry/integrality-from-metric-of-orthogonality-window/).

## Statement

`OrthLat` is stated in [`closed_of_orthogonal_basis`](/entry/closed-of-orthogonal-basis/), `RestYbc` in [`closed_of_coefficient_function`](/entry/closed-of-coefficient-function/), and `SymmetryFinitenessWindowLevelDimOnAdmissible D` (with `RestLjjFin`) in [`closed_of_symmetric_windows`](/entry/closed-of-symmetric-windows/). The block lattices $\Lambda$, the pairing $\beta_\Phi$, $\delta = D_1(C_M)$ and the nest $\mathcal{T}$ are as in [`integralityFromMetric_of_orthBasisLat`](/entry/integrality-from-metric-of-orth-basis-lat/).

- `RestOrth` $C_M$: for each index there are $\mathbb{Z}_p$-linearly independent $e_1, \dots, e_n \in \Lambda$ with $\beta_\Phi(e_a, e_b) = 0$ for $a \ne b$, $\beta_\Phi(e_a, e_a) \ne 0$ and $v_p(\beta_\Phi(e_a,e_a)) \le \lfloor \delta \rfloor$ for all $a$, and $n \le \operatorname{rk} \Lambda \le n + \mathrm{bad}(\beta_\Phi, \Lambda, \lfloor \delta \rfloor)$.
- `OrthogonalityWindowLevelDimOnAdmissible D`: the nest $\mathcal{T}$ of "for all $C_\kappa, C_s$, all $C_M \ge 1$ and each $X$ with `AdmNoK`, `HI` implies `RestOrth` $C_M$, `RestWin` $C_M$ and `RestLvlDim`".

**Theorem.** For each datum $D$, `RestYbc`, `OrthLat` and `SymmetryFinitenessWindowLevelDimOnAdmissible D` imply `IntegralityFromMetricForLargeConstants D`.

## Proof

The lemma `orthogonal_of_symmetric_finite` proves `OrthogonalityWindowLevelDimOnAdmissible D` from `OrthLat` and `SymmetryFinitenessWindowLevelDimOnAdmissible D`. Fix the constants, with $C_{Yb} \ge 1$, and an $X$ with `AdmNoK` and `HI`.

1. `HI` and $C_{Yb} \ge 1$ give the list `HIFacts` (`hiFacts`). It contains $m \ge 4$ and $(m+1)^2 \le p$, so $p \ge 25$ (`p25`) and $p \ne 2$.
2. `restOrth_of` proves `RestOrth` $C_M$ from $p \ne 2$, `OrthLat`, `RestSymm` and `RestLjjFin`. At each index it applies `OrthLat` to $B = \beta_\Phi$, $L = \Lambda$, the space $W$ of `RestLjjFin` and $k = \lfloor \delta \rfloor$. The linearity of $\beta_\Phi$ in the first variable is `bePhi_smul_left` and `bePhi_add_left`; the symmetry is `RestSymm`.

`RestWin` and `RestLvlDim` pass through. The bound $C_{Yb} \ge 1$ comes from `thr_mono_ge`, a form of `thr_mono` that raises the threshold $T_2$ to at least 1. Then `integrality_from_metric_of_orthogonality_window` is applied to `RestYbc` and the new statement.

## In the Lean code

The theorem is in [SymmetryFinitenessWindowLevelDimOnAdmissible.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/SymmetryFinitenessWindowLevelDimOnAdmissible.lean#L29), with `orthogonal_of_symmetric_finite` at line 18. The lemmas it calls:

- `thr_mono_ge` and `hiFacts`, in [CountingStatementReduction.lean](lean:Formalism/SharpRestriction/GrowthBounds/CountingStatementReduction.lean#L3850) (`hiFacts` at line 1633).
- `p25`, in [KappaZeroNonneg.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/KappaZeroNonneg.lean#L50).
- `restOrth_of` and `bePhi_add_left`, in [BePhiAddLeft.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/BePhiAddLeft.lean#L47). `RestOrth` is in [BejjSmulLeft.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/BejjSmulLeft.lean#L116).
- `integrality_from_metric_of_orthogonality_window`, in [IntegralityFromMetricOfOrthogonalityWindow.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/IntegralityFromMetricOfOrthogonalityWindow.lean#L23).

`hY` passes through unchanged. This is the first link since [`closed_of_orthogonal_basis`](/entry/closed-of-orthogonal-basis/) where `OrthLat` is used; the links between only carry it. The four statements `RestSymm`, `RestLjjFin`, `RestOrth` and `RestWin` all use the block datum with $a_+ = 0$ (`gB C0 CE1 CE2 X aTop 0 x.1`); the other values of $a_+$ enter only through the pairings $\beta_{a_+}$ in `RestWin`.
