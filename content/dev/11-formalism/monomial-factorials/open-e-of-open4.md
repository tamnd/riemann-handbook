---
id: open-e-of-open4
title: Four open bounds give the four bounds of the window count
kind: theorem
decl: Formalism.MainNotions.G.SymmetricFormBlocks.openE_of_open4
module: Formalism.SharpRestriction.GrowthBounds.MonomialFactorials.ThresholdsMonoNormalized
covers: 2194
status: drafted
drafted_by: writer@claude
---
This theorem is a link of the chain that proves the averaged bad-share bound `IntegralityFromMetricForLargeConstants D` (see [`theorem_A_closed_form_holds`](/entry/theorem-a-closed-form-holds/)). [`closed_of_open_directions`](/entry/closed-of-open-directions/) calls it. It turns the four open bounds of `RestOpen4E D` into the four bounds of `RestOpenE D`. Two come from proved lemmas, one from [`restTM_closed`](/entry/rest-tm-closed/), and one passes through.

## Statement

Instances $X$, the window $A$, $s$, $r$, the number $t$ of ties and $Y \ge 1$ are as in [`theorem_A_closed_form_holds`](/entry/theorem-a-closed-form-holds/). $\mathcal{T}(P)$ is the nest of thresholds `TransportedAlt` (see [`integralityFromMetric_of_orthBasisLat`](/entry/integrality-from-metric-of-orth-basis-lat/)).

For a $\mathbb{Z}_p$-lattice $L$ with a pairing $\beta$ and $D \in \mathbb{Z}$, the *good count* $g_\beta(L, D)$ is the largest $n$ with $x_1, \dots, x_n, y_1, \dots, y_n \in L$ and $\beta(x_i, y_j) = p^D \delta_{ij}$, and $\mathrm{bad}_\beta(L, D) = \operatorname{rk} L - g_\beta(L, D)$. For a top $a \in A^s$, a block $b$ and a level $\ell = (j, j')$, there is a lattice $Y_\ell$ (`YZ`) and a level lattice $L_\ell$ (`Ljj`) spanned by products of elements of $Y_\ell$ and integral homogeneous polynomials of degree $n_\ell = B_+ - j'$ in $r$ further variables $\xi$. Let $d_\xi(n) = \binom{n+r-1}{r-1}$ and $r_\ell = \operatorname{rk} Y_\ell \cdot d_\xi(n_\ell)$ (`rL`). The depth is $D_1 = t(Y\kappa + C_M\kappa) + C_M\kappa$ with $\kappa = 3(s+2)r^2\lambda$. We have not unfolded the block data `gB`, `Kept`, `lv` or the pairings.

The open bounds, for each kept block $b$ and level $\ell$:

- `RestBCdim`: the rank of the block lattice $\Lambda(a, a_+, b)$ is at most $\sum_\ell \operatorname{rk} L_\ell$.
- `RestPlusA` $C_M$: $\mathrm{bad}(L_\ell, \lfloor D_1 \rfloor) \le \mathrm{bad}(Y_\ell, \lfloor D_1 \rfloor)\, d_\xi(n_\ell)$.
- `RestPlusB` $C_M$: $\sum_{a_+ \in A} \mathrm{bad}(L_\ell(a_+), \lfloor Y D_1 \rfloor) \le |A| \bigl(\mathrm{bad}(L_\ell, \lfloor D_1 \rfloor) + \tfrac{5}{Y} \operatorname{rk} L_\ell\bigr)$.
- `RestDir`: $\sum_\ell r_\ell$ is at most the block rank `bRank`.

`RestOpen4E D` is $\mathcal{T}(P)$, where $P$ says: for all $C_\kappa, C_s$ and all $C_M \ge 1$, each $X$ with `AdmNoK` and `HI` satisfies these four bounds. `RestOpenE D` is $\mathcal{T}(Q)$, where $Q$ says: for all $C_\kappa, C_s$ there is $C_M \ge 0$ such that each $X$ with `AdmNoK` and `HI` satisfies `RestDir` and three more bounds. `BlockBoundUniformiser`: for each $D \ge 0$, $\Lambda$ has a sublattice $L_2$ with good pairings at depth $D$ plus a loss (`GoodSub`) and $\operatorname{rk} \Lambda \le \operatorname{rk} L_2 + \sum_\ell \mathrm{bad}(L_\ell(a_+), D)$. `RestPlus` $C_M$: `RestPlusB` with $\mathrm{bad}(Y_\ell, \lfloor D_1 \rfloor)\, d_\xi(n_\ell) + \tfrac{5}{Y} r_\ell$ in the bracket. `RestTM` $C_M$ is stated in [`restTM_closed`](/entry/rest-tm-closed/).

**Theorem.** For each datum $D$, `RestOpen4E D` implies `RestOpenE D`.

## Proof

1. `thresholds_mono_normalized` is a form of `thr_mono`: $\mathcal{T}(P)$ implies $\mathcal{T}(Q)$ if $P$ implies $Q$ whenever $C_0 \ge 1$, $C_{Yb} \ge 2$, $C_D \ge 0$, $C_b \ge 1$ and $C_{E1}, C_{E2} \ge 0$.
2. Take $C_M \ge 1$ from `restTM_closed`.
3. `BlockBoundUniformiser`: `block_valuation_over_Zp_holds` proves `BlockBoundIntegers` from `HI`. This gives dual families $x_i, y_i$ (pairing $p^e \delta_{ij}$) with $\sum_\ell \operatorname{rk} L_\ell \le n + \sum_\ell \mathrm{bad}(L_\ell, D)$. Then `block_bound_of_dual_families` combines it with `RestBCdim`.
4. `RestPlus`: `restPlus_of` puts `RestPlusA` into `RestPlusB`, with $\operatorname{rk} L_\ell \le r_\ell$ from `restRankL_proved` and $Y > 0$ from `HI`.
5. `RestTM` is `restTM_closed`, and `RestDir` passes through.

## In the Lean code

The theorem is in [ThresholdsMonoNormalized.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/ThresholdsMonoNormalized.lean#L40), with `thresholds_mono_normalized` at line 13 and `RestOpen4E` at line 36. `RestOpenE` is in [ClosedOfOpenConditions.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/ClosedOfOpenConditions.lean#L30). The bounds are in [BlockBoundUniformiser.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/BlockBoundUniformiser.lean#L98) and [RestPlusOf.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/RestPlusOf.lean#L33).

The hypothesis is stronger than needed: `RestOpen4E` asks for every $C_M \ge 1$, but the proof uses only the value from `restTM_closed`. The datum $D$ and the hypothesis `AdmNoK` are only passed on.
