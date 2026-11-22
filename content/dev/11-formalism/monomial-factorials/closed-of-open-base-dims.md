---
id: closed-of-open-base-dims
title: The bad count of the levels from an orthogonal family
kind: theorem
decl: Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_open_base_dims
module: Formalism.SharpRestriction.GrowthBounds.MonomialFactorials.RestrictedBoundsWeakenFromSevenToSix
covers: 2383
status: drafted
drafted_by: writer@claude
---
This theorem is the fourteenth link of the chain of reductions that proves the averaged bad-share bound `IntegralityFromMetricForLargeConstants D` (see [`theorem_A_closed_form_holds`](/entry/theorem-a-closed-form-holds/)). [`theorem_A_closed_of_eight_open_bounds`](/entry/theorem-a-closed-of-eight-open-bounds/) calls it. It combines an orthogonal family in each block lattice with the window count, to bound the bad count of the levels. It passes the result on to [`closed_of_open_dimensions`](/entry/closed-of-open-dimensions/).

## Statement

The indices $(d, a_{\mathrm{top}}, x)$, the lattice $\Lambda$ (`Ljj`), the pairings $\beta_\Phi$ and $\beta_{a_+}$, the number $\delta = D_1(C_M)$, the bad count $\mathrm{bad}(\beta, L, e)$ and `RestWin` $C_M$ are as in [`integralityFromMetric_of_orthBasisLat`](/entry/integrality-from-metric-of-orth-basis-lat/). `RestOpen7E D` is stated in [`theorem_A_closed_of_eight_open_bounds`](/entry/theorem-a-closed-of-eight-open-bounds/). Let $Y$ be the parameter `X.L.Y` and $A$ the window `X.winA`.

- `RestOrth` $C_M$: for each index there are $n_1$ and $e_1, \dots, e_{n_1} \in \Lambda$, linearly independent over $\mathbb{Z}_p$ and orthogonal for $\beta_\Phi$, with $\beta_\Phi(e_a, e_a) \ne 0$ and $v_p(\beta_\Phi(e_a, e_a)) \le \lfloor \delta \rfloor$, such that $n_1 \le \operatorname{rk} \Lambda \le n_1 + \mathrm{bad}(\beta_\Phi, \Lambda, \lfloor \delta \rfloor)$.
- `RestPlusB` $C_M$: for each index,
$$\sum_{a_+ \in A} \mathrm{bad}(\beta_{a_+}, \Lambda, \lfloor Y\delta \rfloor) \le |A| \Bigl( \mathrm{bad}(\beta_\Phi, \Lambda, \lfloor \delta \rfloor) + \frac{5}{Y} \operatorname{rk} \Lambda \Bigr).$$
- `RestOpen6E D`: $\mathcal{T}$ of the statement "for all $C_\kappa, C_s$, all $C_M \ge 1$ and each $X$ with `AdmNoK`, `HI` implies `RestBCdim`, `RestPlusB` $C_M$ and `RestDirQ`".

**Theorem.** For each datum $D$, `RestOpen7E D` implies `IntegralityFromMetricForLargeConstants D`.

## Proof

The lemma `restricted_bounds_weaken_from_seven_to_six` proves `RestOpen6E D` from `RestOpen7E D`. It opens the nest with `thr_mono`. `RestBCdim` and `RestDirQ` pass through. `HI` contains the window hypotheses, whose first condition is $1 \le Y$, so $Y > 0$. Then `restPlusB_of` gives `RestPlusB` from `RestOrth` and `RestWin`, in four steps.

1. `RestOrth` gives the family $e$. Let $L_1 = \operatorname{span}_{\mathbb{Z}_p}(e)$. Then $L_1 \subseteq \Lambda$ and $\operatorname{rk} L_1 = n_1$.
2. `bad_le_sub`: for each $a_+$, $\mathrm{bad}(\beta_{a_+}, \Lambda, \lfloor Y\delta \rfloor) \le (\operatorname{rk} \Lambda - n_1) + \mathrm{bad}(\beta_{a_+}, L_1, \lfloor Y\delta \rfloor)$. The reason: a good family in $L_1$ is a good family in $\Lambda$. The lemma needs the good count on $\Lambda$ to be bounded, which is `bejj_bdd`.
3. `RestWin`, applied to $e$, bounds the sum over $a_+$ of the second term by $|A| \cdot 5 n_1 / Y$.
4. `RestOrth` gives $\operatorname{rk}\Lambda - n_1 \le \mathrm{bad}(\beta_\Phi, \Lambda, \lfloor \delta \rfloor)$ and $n_1 \le \operatorname{rk}\Lambda$. Sum step 2 over $A$ and use $5/Y \ge 0$.

Then `closed_of_open_dimensions` is applied. The rest is bookkeeping.

## In the Lean code

The theorem is in [RestrictedBoundsWeakenFromSevenToSix.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/RestrictedBoundsWeakenFromSevenToSix.lean#L24), with `RestOpen7` at line 10, `RestOpen7E` at line 14 and the weakening lemma at line 18. The lemmas it calls:

- `thr_mono`, in [CountingStatementReduction.lean](lean:Formalism/SharpRestriction/GrowthBounds/CountingStatementReduction.lean#L2456).
- `restPlusB_of`, with `RestOrth` (line 116), `RestWin` (line 129), `bad_le_sub` (line 45) and `bejj_bdd` (line 103), in [BejjSmulLeft.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/BejjSmulLeft.lean#L143). `RestPlusB` is in [RestPlusOf.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/RestPlusOf.lean#L43).
- `closed_of_open_dimensions`, in [PositiveOfDimensionChange.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/PositiveOfDimensionChange.lean#L23).

The bad counts are natural numbers, so $\operatorname{rk}\Lambda - n_1$ is truncated subtraction; this is harmless because $n_1 \le \operatorname{rk}\Lambda$. The last step of `restPlusB_of` is `nlinarith`. The name speaks of base dimensions, but `RestBCdim` only passes through here. The step that this link does is the passage from `RestOrth` and `RestWin` to `RestPlusB`.
