---
id: expansion-product-invariant-inner-vertex-level
title: The product function of an expansion is invariant at an inner top vertex (named form)
kind: theorem
decl: GlobalTheory.T.expansion_product_invariant_inner_vertex_level
module: Development.AbelianVarietyTheory.Proofs.TwistedOperators.ExpansionProductInvariantInnerVertexLevelStatement
covers: 315
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It gives [`product_invariant`](/entry/product-invariant/), which has the real content, a second name in the namespace `GlobalTheory.T`. Its one user, [`pairPts_update_top`](/entry/pair-pts-update-top/), uses it as the last step.

## Statement

Take the grid data, the expansion $\tau$ and the hypotheses of [`levels_invariant`](/entry/levels-invariant/). Let $j + 1 < m$, let $k$ be a point of the top vertex $j + 1$ with image in $K^{\mathrm{top}}_{j+1}$, and let $g = u^{-1} k u$ with $u$ = `S.N.u (.top (j + 1))`. For each datum $d$ let $v_{d,j'}$ be the theta function `S.Z.vec (d.1 j')` of the column edge $j'$, and let $v^{g}_{d,j'}$ be the column `movedCol S d j g`: it is $\omega(1, g) v_{d,j}$ at $j' = j$, $\omega(g, 1) v_{d,j+1}$ at $j' = j + 1$, and $v_{d,j'}$ at the other edges. Then for all $w$ and $z$,

$$\sum_d \tau(d) \prod_{j'} v^{g}_{d,j'}(w_{j'}) \prod_i r_{d,i}(z_i) = \sum_d \tau(d) \prod_{j'} v_{d,j'}(w_{j'}) \prod_i r_{d,i}(z_i),$$

where $r_{d,i}$ = `S.Z.vec (d.2 i)` are the functions of the row edges.

## Proof

The proof is the term `GlobalTheory.ExpansionInvariance.product_invariant`. Nothing else happens.

## In the Lean code

The theorem is in [ExpansionProductInvariantInnerVertexLevelStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExpansionProductInvariantInnerVertexLevelStatement.lean#L9). The proof is the tactic `first | exact @GlobalTheory.ExpansionInvariance.product_invariant | ...`, and the first branch closes the goal. The statement is word for word that of `product_invariant`.
