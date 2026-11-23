---
id: product-invariant
title: The product function of an expansion is invariant at an inner top vertex
kind: theorem
decl: GlobalTheory.ExpansionInvariance.product_invariant
module: Development.AbelianVarietyTheory.Proofs.TwistedOperators.ExpansionProductInvariantInnerVertexLevel
covers: 314
status: drafted
drafted_by: writer@claude
---
This theorem is the identity of functions behind the first part of [`levels_invariant`](/entry/levels-invariant/). The parent [`expansion_product_invariant_inner_vertex_level`](/entry/expansion-product-invariant-inner-vertex-level/) is a second name for it, and [`pairPts_update_top`](/entry/pair-pts-update-top/) uses it to show that the pairing of points does not change when an inner top point moves by its level group. The proof writes each theta function of the expansion as the image of a finite function under one fixed linear map per edge, and then uses a scalar identity for the finite functions.

## Statement

The statement is the one written out in [`expansion_product_invariant_inner_vertex_level`](/entry/expansion-product-invariant-inner-vertex-level/): with $g = u^{-1} k u$ and $k$ in the level group $K^{\mathrm{top}}_{j+1}$, replacing $v_{d,j}$ by $\omega(1, g) v_{d,j}$ and $v_{d,j+1}$ by $\omega(g, 1) v_{d,j+1}$ does not change the function

$$(w, z) \mapsto \sum_d \tau(d) \prod_{j'} v_{d,j'}(w_{j'}) \prod_i r_{d,i}(z_i).$$

The group $K^{\mathrm{top}}_{j+1}$ is `S.levTop t Φ β (j + 1)`: a product over the places of `locPl G t` of the level groups `pr` of the local unfolded terms at $\beta$, read in the frame `S.βp (j + 1)`.

## Proof

1. **Empty expansion.** If $\tau = 0$, both sides are $0$.
2. **One model per edge.** The expansion gives one idempotent sum $e$ shared by all data in the support of $\tau$. From one datum $d_0$, the hypothesis `HasVec` gives for each column edge $j'$ a linear map $T_{j'}$ that is a place model of the vacuum `S.Z.vac` for $e$ (`IsPlaceModel`, which we have not unfolded), and maps $T'_i$ for the row edges. Then `vec_eq_model` gives $v_{d,j'} = T_{j'}(f_{d,j'})$ and $r_{d,i} = T'_i(f'_{d,i})$ for every $d$, where $f$ and $f'$ are the finite functions `fn` of the data.
3. **The vacuum moves by a scalar.** `columnArrow_realAverage_howeDuality_fockComponent` (a second name of `vac_move_low`) and `vac_move_high` give scalars $c_1, c_2$ such that $\omega(1, g)$ of the vacuum of edge $j$ is $c_1 T_j$ of a translate of the function `halfInd`, and the same for $\omega(g, 1)$ at edge $j + 1$ with $c_2$. With `SplitLinear.om_model_of_base`, this gives $\omega(1, g) v_{d,j} = c_1 T_j(f^{g}_{d,j})$ and $\omega(g, 1) v_{d,j+1} = c_2 T_{j+1}(f^{g}_{d,j+1})$. Here $f^{g}$ is `movedFn`: the function $f$ composed with the action of $g^{-1}$ on the argument.
4. **The scalar identity.** `unfoldingExpansion_productFunction_localInvariant` says that, pointwise,
$$\sum_d \tau(d)\, c_1 c_2 \prod_{j'} f^{g}_{d,j'} \prod_i f'_{d,i} = \sum_d \tau(d) \prod_{j'} f_{d,j'} \prod_i f'_{d,i}.$$
5. **Through the models.** `sum_prod_map_congr` says: if two finite sums of products of functions agree at every point, they still agree after one applies a fixed linear map to each factor. This is the fact that $\bigotimes_a T_a$ is well defined on the tensor product. Apply it with the maps $T_{j'}$ and $T'_i$ to the identity of step 4. By step 3 the left side is the moved sum, and by step 2 the right side is the original sum.

## In the Lean code

The theorem is in [ExpansionProductInvariantInnerVertexLevel.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExpansionProductInvariantInnerVertexLevel.lean#L17). The lemmas it calls:

- `vec_eq_model`, `sum_prod_map_congr` and `movedFn` in [SumProdPartialEqZero.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/SumProdPartialEqZero.lean#L57).
- `GlobalTheory.T.columnArrow_realAverage_howeDuality_fockComponent` and `vac_move_high` in [VacMoveHigh.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/VacMoveHigh.lean#L21).
- `GlobalTheory.SplitLinear.om_model_of_base`, and `VecEx.isSBHalf_of_lattices` for its side condition.
- `GlobalTheory.T.unfoldingExpansion_productFunction_localInvariant`, a second name of `GlobalTheory.TopLevelInv.local_invariant`, in [UnfoldingExpansionProductFunctionLocalInvariantStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/UnfoldingExpansionProductFunctionLocalInvariantStatement.lean#L9).

The hypotheses `hL₀`, `hde`, `hcc` and `hβ` are only passed to step 4. The name `columnArrow_realAverage_howeDuality_fockComponent` says more than its statement, which is only the existence of the scalar $c_1$ of step 3.
