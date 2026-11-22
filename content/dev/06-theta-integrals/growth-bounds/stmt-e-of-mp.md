---
id: stmt-e-of-mp
title: The closed form of the valuation bound, from the membership step and Proposition 5
kind: theorem
decl: Formalism.MainNotions.TestSideWords.stmtE_of_MP
module: Formalism.SharpRestriction.GrowthBounds.TwistedSubstitution
covers: 874
status: drafted
drafted_by: writer@claude
---
This theorem proves `ClosedFormOfAdmitted D` from the membership step `RestMEM` and the numerical statement `Proposition5Gram`. It is a pass-through. It supplies the proved operator fact `TenOp` and calls [`stmtE_of_TenMP`](/entry/stmt-e-of-ten-mp/). Its only user is [the version from the membership step](/entry/stmt-e-of-mem/), which also supplies `Proposition5Gram`.

## Statement

Let $D$ be a datum of type `D7`. The [entry for `stmtE_of_mem`](/entry/stmt-e-of-mem/) defines `RestMEM`, `Proposition5Gram` and the conclusion.

**Theorem.** Assume that `RestMEM D CLa Ck Crk Cdeg` and `Proposition5Gram D CLa Ck Crk Cdeg 26 2 24 60` hold for all real $C_\Lambda, C_k, C_{rk}, C_{\deg}$. Then `ClosedFormOfAdmitted D` holds.

## Proof

The proof is one line: `stmtE_of_TenMP tensor_operators_holds D hM hP`. The first argument is [the proof of `TenOp`](/entry/tensor-operators-holds/). It is the only new input. The rest of the work is in `stmtE_of_TenMP` and the lemmas below it.

## In the Lean code

The theorem is at [TwistedSubstitution.lean line 23](lean:Formalism/SharpRestriction/GrowthBounds/TwistedSubstitution.lean#L23). `tensor_operators_holds` is in [OperatorWeightBoundHolds.lean](lean:Formalism/SharpRestriction/GrowthBounds/TwistedSubstitution/OperatorWeightBoundHolds.lean#L84).

- It adds no mathematics. It only removes the hypothesis `TenOp` from `stmtE_of_TenMP`.
- The conclusion does not depend on $D$, because `aux₃` ignores its first argument; see [Statement E](/entry/stmt-e/).
