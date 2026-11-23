---
id: inputs4-of-net
title: From the net inputs to the index bound, through a second norm
kind: theorem
decl: GlobalTheory.FinalJoin.inputs4_of_net
module: Development.AbelianVarietyTheory.Proofs.HeightProofs.ExistsThresholdRunHolds
covers: 882
status: drafted
drafted_by: writer@claude
---
This theorem is step 3 of [`runHolds_of_parOK`](/entry/run-holds-of-par-ok/), in branch 2 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). It takes the inputs `InputsNet` that [`inputsNet_recPlus`](/entry/inputs-net-rec-plus/) proves, and returns a second norm $n$, the refined inputs `Inputs4` and the index bound `Concl`, all for the algebra renormed by $n$. The proof joins four lemmas and does no analysis of its own.

## Statement

Use the algebra of forms $X_j$, the constants $H$, the weights $\kappa, w_L, w_F$ and the index bound `Concl` of [the entry for `runHolds_of_parOK`](/entry/run-holds-of-par-ok/), and `InputsNet` of [the entry for `inputsNet_recPlus`](/entry/inputs-net-rec-plus/). A *second norm* (`SecNorm`) is a family of norms $N$ on the cusp forms, one for each weight and each complex embedding $\sigma$ of $K$, with $N(aF) = |\sigma(a)| N(F)$ and $N \le \|\cdot\|_{\sup}$.

**Theorem.** Let $X$ be a family of algebras $X_j$, $1 \le j \le m$. Assume `InputsNet` for $X_j$ with the constants `kR CL`, the ties $H.C_1 = H.C_c = C_2$, $H.A_1 = H.A_c = A_2$, $H.CR_c = 7$, $A_2 \ge 12$, and `PageAt` and `PageSupp`. Then there is a second norm $n$ such that, for $X_j$ renormed by $n$ and the scalars $S$ renormed by $n$,

1. `Inputs4` holds with the constants `k4 large₂ CL`;
2. `Concl` holds with $\beta = \operatorname{rk}(M_\kappa) \cdot f \cdot m \cdot b \cdot d_{e2}$.

## Proof

1. `exists_secNorm_inputsR_of_inputsNet` turns the net of `InputsNet` into a second norm $n$, and gives `InputsR` for the renormed algebra. `InputsR` replaces the net condition `NetIn` by three facts: `SupBoundByL2AtWeight` (the sup norm squared is at most $e^{P(1 + \log |\kappa|)}$ times the $L^2$ norm squared), `DeepHerm` and `DeepLogD` ($\log \dim_K$ of the cusp forms of weight $\kappa$ is at most $P_d$).
2. `indexBoundIntrinsicHypotheses_netBound_degreeTwo` changes the constants from `kR CL` to `k4 large₂ CL`. The pair $(C_G, A_G)$ of the sup bound goes from $(1041, 3)$ to $(1041\, z, 2)$, where $z$ is `zBase large₂`.
3. The ties and $A_G = 2$ give `TieC`. Then `indexBoundChosenFamily_of_intrinsicHypotheses`, with `PageAt` and `PageSupp`, gives `Inputs4`.
4. `concl_of_inputs4` gives `Concl`. It calls `theorem_zero_of_refined_inputs`.

The rest is bookkeeping.

## In the Lean code

The theorem is in [ExistsThresholdRunHolds.lean](lean:Development/AbelianVarietyTheory/Proofs/HeightProofs/ExistsThresholdRunHolds.lean#L33). `InputsNet`, `InputsR`, `Inputs4`, `k4` and `concl_of_inputs4` are in [ConclOfInputs4.lean](lean:Development/AbelianVarietyTheory/Definitions/HeightFunctions/ConclOfInputs4.lean#L51), `SecNorm` in [SWEqSOf.lean](lean:Development/AbelianVarietyTheory/Definitions/ThetaValues/SWEqSOf.lean#L23), and `TieC` in [WeightAlgebra.lean](lean:Formalism/SharpRestriction/Divisibility/WeightAlgebra.lean#L659). We have not read the proofs of the four lemmas, and we have not unfolded `DeepHerm`, `PageSupp` or most of the 27 parts of `Inputs4`.

- `TieC` asks for $A_G \le 2$, and `kR` has $A_G = 3$. This is why step 2 is needed.
- $X$ is a family over all $j$, but the statement uses only $X_j$.
- `concl_of_inputs4` drops the last part of `Inputs4`, the local point data for $j \ge m$.
