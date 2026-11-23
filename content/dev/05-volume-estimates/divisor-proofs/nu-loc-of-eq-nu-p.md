---
id: nu-loc-of-eq-nu-p
title: The local depth of a column polynomial, computed
kind: theorem
decl: GlobalTheory.ColDepth.nuLocOf_eq_nuP
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ColumnPolynomialLocalDepthEqPlaceDepth
covers: 357
status: drafted
drafted_by: writer@claude
---
This theorem computes the local depth of a column polynomial $\mathrm{polyT}(B, c_x)$ at a point $y$: it is the depth $\nu_p(y, c_x)$, for every $k$. The proof is a chain of three equalities, and the middle one is an approximation argument in a valued field. Its only user is its renaming [columnPolynomial_localDepth_eq_placeDepth](/entry/column-polynomial-local-depth-eq-place-depth/), step 3 of [exists_polyBetween](/entry/exists-poly-between/). Below this theorem are 357 declarations.

## Statement

The statement is the one of [columnPolynomial_localDepth_eq_placeDepth](/entry/column-polynomial-local-depth-eq-place-depth/): if $B$ has `IsCols`, then $\nu_{\mathrm{loc}}(\mathrm{Ch}, v_T(p), k, \mathrm{polyT}(B, c_x)) = \nu_p(y, c_x)$ for all $k$.

`IsCols` says: there is an injection of the pairs $(f, j)$, with $c_x(f) \ne 0$ and $j < 2\,\mathrm{rk}(f)$, into the $n$ columns, such that each $B_f$ is zero outside its block, has an invertible $\mathrm{rk}(f) \times \mathrm{rk}(f)$ minor, and is, to each precision $p^N$, the image of a matrix $x$ over $\mathcal{O}_E$ whose rows are isotropic modulo $p^N$ for the hermitian form $\sum_j x_{bj}\bar x_{b'j}$.

## Proof

Choose an extension $X$ of the valuation (`ValExt T p`); `nonempty_valExt_of_overLa` gives one. Let $C$ be its field and $v$ its valuation.

1. `localDepth_over_dvr_eq_over_closed_field` moves the local depth from $T$ to $C$: $\nu_{\mathrm{loc}} = \nu_{\mathrm{loc}, X}$ (`nuLocX_vp`), an infimum of $v(\nabla_k g)$ over integral power series $g$ in $n$ columns, where $\nabla_k$ (`nabX`) is an operator built from the chart that we have not unfolded.
2. $\nu_{\mathrm{loc}, X} = \nu_{H}$ (`nuH_vp`), an infimum of $v$ over integral power series $f$ on the copies `Col` $c_x$, composed with `expH`, which is built from the formal group law `fgl` of the chart. The two families approximate each other: `exists_integral_germ_on_columns_same_value` gives, for each $g$ and each $N$, an $f$ with difference of valuation at least $N$, and `exists_integral_germ_on_copies_same_value` gives the converse. Then `iInf_eq_of_approx` says the two infima agree.
3. `isotropicFactor_depth_eq_sum_factor_depths` gives $\nu_H = \nu_p(y, c_x)$.

Step 2 rests on the ultrametric fact `val_eq_of_lt_sub`: if $v(x) < v(x - y)$, then $v(y) = v(x)$. So an element approximated to precision above its valuation has the same valuation as its approximation.

## In the Lean code

The theorem is at [ColumnPolynomialLocalDepthEqPlaceDepth.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ColumnPolynomialLocalDepthEqPlaceDepth.lean#L60). `IsCols` is at [NonemptyValExtOfOverLa.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/NonemptyValExtOfOverLa.lean#L339), `nuLocX_vp` and `nuH_vp` at [LocalValuationColumns.lean](lean:Development/AbelianVarietyTheory/BlockTheory/DivisorBase/LocalValuationColumns.lean#L42).

- `val_eq_of_lt_sub`, `iInf_le_of_approx` and `iInf_eq_of_approx` are in the same file. They hold for any additive valuation with values in $\mathbb{R} \cup \{\infty\}$.
- `IsCols` is used only in step 2. Step 1 holds for any $B$.
- The right side does not depend on $k$, so the local depth of a column polynomial does not depend on $k$.
- We have not unfolded `nuLocOf`, `nabX`, `expH` or the four lemmas of steps 1 to 3.
