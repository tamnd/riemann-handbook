---
id: stmt-e-of-ten-ns
title: The closed form of the valuation bound, from the tensor operator fact and the test-side step
kind: theorem
decl: Formalism.MainNotions.TestSideCounting.stmtE_of_TenNS
module: Formalism.SharpRestriction.GrowthBounds.DualFockLinear
covers: 549
status: drafted
drafted_by: writer@claude
---
This theorem proves `ClosedFormOfAdmitted D` from the operator fact `TenOp` and the test-side hypothesis `RestNS`. It turns `TenOp` into `RestTSOp` and passes both inputs to [`stmtE_of_OpNS`](/entry/stmt-e-of-op-ns/). Its only user is [`stmtE_of_TenMP`](/entry/stmt-e-of-ten-mp/), which builds `RestNS` from the membership step and Proposition 5.

## Statement

Let $D$ be a datum of type `D7`. Fix the four constants $C_H = 26$, $C_E = 2$, $C_6 = 24$, $C_{18} = 60$.

**Theorem.** Assume `TenOp`. Assume that `RestNS D CLa Ck Crk Cdeg 26 2 24 60` holds for all real $C_\Lambda, C_k, C_{rk}, C_{\deg}$. Then `ClosedFormOfAdmitted D` holds.

`TenOp` says that, under the Fock pairing, multiplication by elements of a tensor product of dual Weyl modules is given by words in the polarization operators $X_{t,i}\,\partial/\partial X_{t,j}$. [Its entry](/entry/tensor-operators-holds/) states it in full. `RestNS` says: if `admitted D` holds for the four constants, then there are $C_D, C_1 > 0$ such that the test-side statement `NSStep` holds for all $C \ge C_1$. The [entry for `stmtE_of_mem`](/entry/stmt-e-of-mem/) describes the bound `NSConcl` that `NSStep` gives.

## Proof

The proof is one term. For each choice of constants, `restTSOp_of_ten hT D` gives `RestTSOp D CLa Ck Crk Cdeg`, and the hypothesis gives `RestNS`. The pair goes to `stmtE_of_OpNS`. We have not unfolded the proof of `restTSOp_of_ten`. It calls `restOpF_of_ten` and `restTSOp_of_opF`.

## In the Lean code

The theorem is in [DualFockLinear.lean](lean:Formalism/SharpRestriction/GrowthBounds/DualFockLinear.lean#L24). `restTSOp_of_ten` is in [FirstWeightLeConductor.lean](lean:Formalism/SharpRestriction/GrowthBounds/DualFockLinear/FirstWeightLeConductor.lean#L174), and `TenOp` is at [line 16](lean:Formalism/SharpRestriction/GrowthBounds/DualFockLinear/FirstWeightLeConductor.lean#L16) of the same file.

This is a pass-through. The real content is in `stmtE_of_OpNS` and in `tensor_operators_holds`, which proves `TenOp`. `stmtE_of_TenMP` also takes `TenOp` as a hypothesis, and [`stmtE_of_MP`](/entry/stmt-e-of-mp/) supplies the proof.
