---
id: closed-of-open-positive
title: Adding the product bound for the level lattices
kind: theorem
decl: Formalism.MainNotions.G.SymmetricFormBlocks.closed_of_open_positive
module: Formalism.SharpRestriction.GrowthBounds.MonomialFactorials.DirectionsOfPositivePart
covers: 2361
status: drafted
drafted_by: writer@claude
---
This theorem is a link of the chain of reductions that proves the averaged bad-share bound `IntegralityFromMetricForLargeConstants D` (see [`theorem_A_closed_form_holds`](/entry/theorem-a-closed-form-holds/)). [`closed_of_open_dimensions`](/entry/closed-of-open-dimensions/) calls it. It adds the proved bound `RestPlusA` to the open bounds and passes them to [`closed_of_open_directions`](/entry/closed-of-open-directions/). Its only content is the proof of `RestPlusA`.

## Statement

The bounds `RestBCdim`, `RestPlusA`, `RestPlusB`, `RestDir` and the statement `RestOpen4E D` are in [`openE_of_open4`](/entry/open-e-of-open4/). `RestOpen5E D` is the same as `RestOpen4E D` without `RestPlusA`.

**Theorem.** For each datum $D$, `RestOpen5E D` implies `IntegralityFromMetricForLargeConstants D`.

## Proof

`directions_of_positive_part` proves that `RestOpen5E D` implies `RestOpen4E D`. It uses `thr_mono`: for the nest of thresholds $\mathcal{T}$ of [`openE_of_open4`](/entry/open-e-of-open4/), $\mathcal{T}(P)$ implies $\mathcal{T}(Q)$ when $P$ implies $Q$ for all constants. The step from $P$ to $Q$ inserts `plusACondition`, which proves `RestPlusA` for every instance and every $C_M$, with no hypothesis.

The proof of `plusACondition` is a product argument. Let $x_1, \dots, x_g, y_1, \dots, y_g$ be a good family of $Y_\ell$ at depth $D$ (`goodCount_mem`). For each monomial $\xi^m$ of degree $n_\ell$, the products $x_i \xi^m$ and $\binom{n_\ell}{m}\, y_i \xi^m$ (a multinomial coefficient) lie in $L_\ell$, and the code proves that they pair to $p^D \delta$ (`plusAW_of_blockOK`). So $g(L_\ell) \ge g(Y_\ell)\, d_\xi(n_\ell)$. With $\operatorname{rk} L_\ell \le \operatorname{rk} Y_\ell \, d_\xi(n_\ell)$ (`finrank_Ljj_le`) this gives $\mathrm{bad}(L_\ell) \le \mathrm{bad}(Y_\ell)\, d_\xi(n_\ell)$ (`plusA_of`). Then `closed_of_open_directions` is applied.

## In the Lean code

The theorem is in [DirectionsOfPositivePart.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/DirectionsOfPositivePart.lean#L23), with `RestOpen5E` at line 14 and `directions_of_positive_part` at line 18. `plusAW_of_blockOK` and `plusACondition` are in [PlusAWICondition.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/PlusAWICondition.lean#L63), and `plusA_of` in [RestPlusAOf.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/RestPlusAOf.lean#L19).

The name `directions_of_positive_part` does not say what the lemma does: it adds the bound `RestPlusA` and leaves `RestDir` as it is.
