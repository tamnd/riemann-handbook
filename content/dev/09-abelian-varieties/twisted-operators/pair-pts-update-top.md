---
id: pair-pts-update-top
title: Moving an inner top point by its level group fixes the pairing
kind: theorem
decl: GlobalTheory.ExpansionInvariance.pairPts_update_top
module: Development.AbelianVarietyTheory.Proofs.TwistedOperators.ExpansionPairingInvariantInnerVertexLevel
covers: 338
status: drafted
drafted_by: writer@claude
---
This theorem proves the first part of [`levels_invariant`](/entry/levels-invariant/): the pairing of points does not change when an inner top point $x_j$ moves by an element of its level group. It reaches its user through the renaming [`expansionPairing_invariant_inner_vertex_level`](/entry/expansion-pairing-invariant-inner-vertex-level/). The proof moves the translation from the point into the [[Weil representation|H3Q2703KKV]] on two theta functions, and then reduces the claim to an identity of functions, [`expansion_product_invariant_inner_vertex_level`](/entry/expansion-product-invariant-inner-vertex-level/).

## Statement

The statement is the one in [`expansionPairing_invariant_inner_vertex_level`](/entry/expansion-pairing-invariant-inner-vertex-level/): for $0 < j < m$ and $k$ with image in $K^{\mathrm{top}}_j$,

$$P_\tau(x_j \mapsto x_j k,\ y)\bigl(\Psi(x_0), F(y_0)\bigr) = P_\tau(x, y)\bigl(\Psi(x_0), F(y_0)\bigr).$$

Here $P_\tau(x, y) = \sum_d \tau(d)\, \bigl[C_d(x), R_d(y)\bigr]$. The column map $C_d(x)$ is a composite over the edges $(j', j'+1)$, $j' < m$, of kernel maps $K_{j'}(v_{d,j'})(x_{j'} u_{j'}, x_{j'+1} u_{j'+1})$. The map $K_{j'}$ is `fockComp`, $v_{d,j'}$ is the theta function `S.Z.vec (d.1 j')` of the datum $d$ on that edge, and $u_{j'}$ is the fixed element `S.N.u` of the vertex. The row map $R_d(y)$ is built in the same way, and $[\cdot,\cdot]$ is the bracket `brPair`.

## Proof

Write $j = j' + 1$, let $u = u_j$ and $g = u^{-1} k u$. Then $x_j k u = x_j u g$.

1. **Only two edges see $x_j$.** The point $x_j$ enters the kernels of the edges $j'$ and $j$, and no others.
2. **Translation into the Weil action.** `fockComp_translate` says $K(f)(a k_1, b k_2) = K\bigl(\omega(k_1, k_2) f\bigr)(a, b)$ for a theta function $f$ and finite adelic points $k_1, k_2$, where $\omega$ is the Weil action `W.om`. Applied to the two edges, it replaces $v_{d,j'}$ by $\omega(1, g) v_{d,j'}$ and $v_{d,j}$ by $\omega(g, 1) v_{d,j}$. The new column of functions is `movedCol S d j' g`. The lemma `colMapV_congr` (same file) turns these edge identities into $C_d(x_j \mapsto x_j k) = C_d^{\mathrm{moved}}(x)$.
3. **Reduction to functions.** `pairV_eq_of_prodFun_eq` says that the pairing depends only on the function $(w, z) \mapsto \sum_d \tau(d) \prod_{j'} c_{d,j'}(w_{j'}) \prod_i r_{d,i}(z_i)$, if all $c$ and $r$ are theta functions. They are: `vec_isThetaFunO` for the vectors, and the Weil action keeps theta functions (`om_pres`).
4. **The identity of functions** is [`expansion_product_invariant_inner_vertex_level`](/entry/expansion-product-invariant-inner-vertex-level/) at the edge $j'$.

The rest is bookkeeping with `Function.update`.

## In the Lean code

The theorem is in [ExpansionPairingInvariantInnerVertexLevel.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExpansionPairingInvariantInnerVertexLevel.lean#L33). The lemmas it calls:

- `pairPts_eq_pairV` and `movedCol` in [ColMapEqColMapV.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/ColMapEqColMapV.lean#L35). The first is `rfl`.
- `GlobalTheory.FockTranslate.fockComp_translate` in [FockCompTranslate.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/FockCompTranslate.lean#L22).
- `pairV_eq_of_prodFun_eq` in [PairVEqOfProdFunEq.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/PairVEqOfProdFunEq.lean#L171).
- `GlobalTheory.VecThetaDef.vec_isThetaFunO`, and `colMapV_congr` in the same file.
- `GlobalTheory.T.expansion_product_invariant_inner_vertex_level`.

The hypotheses `hL`, `hde`, `hc`, `ht`, `hβ` and `hτ` are only passed to the last lemma. The hypothesis $0 < j$ is used to write $j = j' + 1$.
