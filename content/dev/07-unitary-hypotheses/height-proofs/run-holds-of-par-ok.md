---
id: run-holds-of-par-ok
title: The index bound on every run, from the parameter conditions
kind: theorem
decl: GlobalTheory.FinalJoin.runHolds_of_parOK
module: Development.AbelianVarietyTheory.Proofs.HeightProofs.ExistsThresholdRunHolds
covers: 5710
status: drafted
drafted_by: writer@claude
---
This theorem gives one threshold $x_0$ such that, for every record with the parameter conditions, the index bound `Concl` holds at every run whose size parameter is above $x_0$. It is the largest part below [`ontoX_of_hypotheses_alt_alt`](/entry/onto-x-of-hypotheses-alt-alt/), in branch 2 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). The real work is in [`inputsNet_recPlus`](/entry/inputs-net-rec-plus/).

## Statement

Let $D$ be a datum (`D7`) with an integer $m$, and let $T$ be a record (`Top D`) with the laws `LawsP T`. For $1 \le j \le m$, $T$ gives an algebra of forms $X_j$ (`recPJ h j hj`, a `PJ` structure). It is an algebra over a number field $K$ that contains the cusp forms of each weight $w$. Over each prime $\lambda$ of $\mathcal O_K$ it has a set of points $y$, each with a valuation $v_y$ on forms. The lattice $M_w$ is the set of cusp forms of weight $w$ with $v_y \ge 0$ at all points. Let $\ell(\lambda) = \log N\lambda / [K:\mathbb{Q}]$.

*The index bound.* Let $\Theta \subseteq X_j$ be the submodule spanned by products of $T_n$ scaled theta forms of weight $w_L$ with short theta forms (`PJ.Theta`). `Concl X S κ wL wF Tn ν β` says: there are $r(\lambda) \ge 0$ with $\sum_\lambda r(\lambda)\ell(\lambda) \le \beta$, such that for each $\lambda$, each integer $e \ge T_n \nu(\lambda)$ and each $K_\lambda$-subspace $V'$ of the span of $M_\kappa$,

$$\operatorname{length}_{\mathcal{O}_\lambda} \bigl( (M_\kappa)_\lambda \cap V' \big/ \Theta_\lambda \cap V' \bigr) \le e \dim V' + r(\lambda) < \infty.$$

**Theorem.** There is $x_0 \colon \mathbb{R}^2 \to \mathbb{R}$ as follows. Let `OtoLL` be injective, `EX : ErrX D` and $p \in \mathbb{N}$, and suppose `ParOK T EX p j` for all $j \in [1, m]$. Let $j \in [1,m]$, and fix size data $L$, constants $H$, weights $\kappa, w_L, w_F$ and integers. If `PageRun` holds and $x_0(H.C_A, H.C_K) \le L.x$, then:

1. for some second norm $n$ (`SecNorm`, norms below the sup norm) and constants $K$, $C_q$, `Inputs4` and `Concl` hold for the algebra with all valued points, renormed by $n$;
2. `HypC` holds for $X_j$;
3. `Concl` holds for $X_j$ with $\beta = \operatorname{rk}(M_\kappa) \cdot f \cdot m \cdot b \cdot d_{e2}$.

This is `RunHolds x₀ h hinj EX p`. `ParOK` has seven fields, among them the laws `LawsSh`, an orientation and `FnAlgClosed`. `PageRun` is the page hypothesis `HypPage` with ties between the constants.

## Proof

1. [`exists_indexBoundHypothesesWithNet_allValuedPoints`](/entry/exists-index-bound-hypotheses-with-net-all-valued-points/) gives constants $C_L$, $C_q$, $Z_0$, and from `ParOK`, `PageOK` and $Z_0 \le$ `zBase` it gives `InputsNet` for the algebra with all valued points.
2. `runNumericalConditions_of_indexBound_beyond_threshold` turns $Z_0$ into $x_0$: `PageRun` and $x_0 \le L.x$ give `PageOK` and $Z_0 \le$ `zBase`.
3. `inputs4_of_net` turns `InputsNet` into $n$, `Inputs4` and `Concl`. It calls `exists_secNorm_inputsR_of_inputsNet`, `indexBoundIntrinsicHypotheses_netBound_degreeTwo`, `indexBoundChosenFamily_of_intrinsicHypotheses` and `concl_of_inputs4`.
4. `hypC_xplus` and `concl_xplus` move `HypC` and `Concl` back to $X_j$.

The rest is bookkeeping.

## In the Lean code

The theorem is in [ExistsThresholdRunHolds.lean](lean:Development/AbelianVarietyTheory/Proofs/HeightProofs/ExistsThresholdRunHolds.lean#L58). `RunHolds` is in [ConclOfInputs4.lean](lean:Development/AbelianVarietyTheory/Definitions/HeightFunctions/ConclOfInputs4.lean#L101), `ParOK` in [GrowthConstantBoundGcR.lean](lean:Development/AbelianVarietyTheory/Definitions/HeightFunctions/GrowthConstantBoundGcR.lean#L24) and `Concl` in [WeightAlgebra.lean](lean:Formalism/SharpRestriction/Divisibility/WeightAlgebra.lean#L424). We have not unfolded `HypC`, `HypPage`, `LawsP`, `D7` or the theta forms `thAll` and `shortTh`.

- `concl_xplus`, `indexBoundConclusion_secondNorm_iff` and `scalOfP_base` are `Iff.rfl` or `rfl`. So `Concl` does not see the extra points or the second norm, and item 3 is item 1 read through these equalities.
- The field `own` of `ParOK` says that $p$ is the prime of every `T.dδ j n`. So, when $m \ge 1$, the hypothesis holds for at most one $p$ per record.
- The caller `hyp_concl_at_run` keeps only items 2 and 3.
