---
id: integrality-from-metric-of-orthogonality-window
title: Adding the base-change dimension bound to the window count
kind: theorem
decl: Formalism.MainNotions.G.SymmetricFormBlocks.integrality_from_metric_of_orthogonality_window
module: Formalism.SharpRestriction.GrowthBounds.MonomialFactorials.IntegralityFromMetricOfOrthogonalityWindow
covers: 2462
status: drafted
drafted_by: writer@claude
---
This theorem is the eleventh link of the chain of reductions that proves the averaged bad-share bound `IntegralityFromMetricForLargeConstants D` (see [`theorem_A_closed_form_holds`](/entry/theorem-a-closed-form-holds/)). [`closed_of_symmetric_finite`](/entry/closed-of-symmetric-finite/) calls it. It uses `RestYbc` to prove a dimension bound for each block, adds it to the window hypothesis, and passes the result to [`theorem_A_closed_of_nine_open_bounds`](/entry/theorem-a-closed-of-nine-open-bounds/). This is the last use of `RestYbc` in the chain.

## Statement

`RestYbc` is stated in [`closed_of_coefficient_function`](/entry/closed-of-coefficient-function/), and `OrthogonalityWindowLevelDimOnAdmissible D` in [`closed_of_symmetric_finite`](/entry/closed-of-symmetric-finite/). Let $K$ be the fraction field of the ring $O$ of the instance $X$.

- `RestBClvl`: for each $a_{\mathrm{top}} \in A^s$, each $a_+ \in A$, each $b$ with `Kept` and each level $l$ in the set `lv`,
$$ \dim_K \operatorname{span}_K(\mathrm{gens}_l) \le \operatorname{rk}_{\mathbb{Z}_p} \Lambda_l , $$
where $\mathrm{gens}_l$ is the set `gens` of the block datum at $(a_{\mathrm{top}}, a_+, b)$ and level $l$, and $\Lambda_l$ is the block lattice `Ljj` at the same place. We have not unfolded `Kept`, `lv` or `gens`.
- `RestOpen9E D`: the nest $\mathcal{T}$ of "for all $C_\kappa, C_s$, all $C_M \ge 1$ and each $X$ with `AdmNoK`, `HI` implies `RestBClvl`, `RestOrth` $C_M$, `RestWin` $C_M$ and `RestLvlDim`".

**Theorem.** For each datum $D$, `RestYbc` and `OrthogonalityWindowLevelDimOnAdmissible D` imply `IntegralityFromMetricForLargeConstants D`.

## Proof

The lemma `open_conditions_base_change` proves `RestOpen9E D`. It opens the nest with `thr_mono` and inserts `RestBClvl` from `restBClvl_of`, which holds for all $X$ and all constants once `RestYbc` holds. Then `theorem_A_closed_of_nine_open_bounds` is applied.

`restBClvl_of` is the private lemma `finrank_span_blockData_gens` at each place. Let $W$ be the $\mathbb{Q}_p$-span of $\Lambda_l$, finite-dimensional by `Ljj_span_fd`. The proof builds a $K$-subspace $T$ with $\dim_K T \le \dim_{\mathbb{Q}_p} W$. It shows that each generator lies in $T$: a generator is a product of an element of $Y_O$ with another factor, and `RestYbc` puts the first factor in the $K$-span of $\iota(Y_{\mathbb{Z}_p})$. So $\dim_K \operatorname{span}(\mathrm{gens}_l) \le \dim_K T \le \dim_{\mathbb{Q}_p} W = \operatorname{rk} \Lambda_l$, the last step by `finrank_Ljj_span`. We have read only the end of this proof, not the construction of $T$.

## In the Lean code

The theorem is in [IntegralityFromMetricOfOrthogonalityWindow.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/IntegralityFromMetricOfOrthogonalityWindow.lean#L23), with the definitions at lines 10 and 14 and `open_conditions_base_change` at line 18. The lemmas it calls:

- `thr_mono`, in [CountingStatementReduction.lean](lean:Formalism/SharpRestriction/GrowthBounds/CountingStatementReduction.lean#L2456).
- `restBClvl_of` and `finrank_span_blockData_gens`, in [RestBCdimOfYbc.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/RestBCdimOfYbc.lean#L108). `RestBClvl` is in [MemLevelsIff.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/MemLevelsIff.lean#L27).
- `theorem_A_closed_of_nine_open_bounds` and `RestOpen9E`, in [RestrictedBoundsWeakenFromNineToEight.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/RestrictedBoundsWeakenFromNineToEight.lean#L23).

The hypothesis `h` passes through unchanged. The name speaks of an orthogonality window, but the only new input is the dimension bound `RestBClvl`. The code does not say what "BC" in `RestBClvl` and "base change" in `open_conditions_base_change` stand for; the statement compares a dimension over $K$ with a rank over $\mathbb{Z}_p$. `RestBClvl` is used two links down, in [`theorem_A_closed_of_eight_open_bounds`](/entry/theorem-a-closed-of-eight-open-bounds/), through `restricted_bounds_weaken_from_eight_to_seven` and `restBCdim_of` in [MemLevelsIff.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/MemLevelsIff.lean#L34). That lemma bounds the rank of a whole block by the sum of the ranks $\operatorname{rk} \Lambda_l$ over its levels.
