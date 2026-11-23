---
id: stmt-e-of-ten-mp
title: The closed form of the valuation bound, from the tensor operator fact, the membership step and Proposition 5
kind: theorem
decl: Formalism.MainNotions.TestSideWords.stmtE_of_TenMP
module: Formalism.SharpRestriction.GrowthBounds.TwistedSubstitution
covers: 556
status: drafted
drafted_by: writer@claude
---
This theorem proves `ClosedFormOfAdmitted D` from `TenOp`, `RestMEM` and `Proposition5Gram`. It is a pass-through. It joins the last two inputs into the test-side hypothesis `RestNS` and calls [`stmtE_of_TenNS`](/entry/stmt-e-of-ten-ns/). Its only user is [`stmtE_of_MP`](/entry/stmt-e-of-mp/), which supplies `TenOp`.

## Statement

Let $D$ be a datum of type `D7`. The [entry for `stmtE_of_mem`](/entry/stmt-e-of-mem/) defines `RestMEM` and `Proposition5Gram`. The [entry for `stmtE_of_TenNS`](/entry/stmt-e-of-ten-ns/) states `TenOp` and `RestNS`.

**Theorem.** Assume `TenOp`. Assume that `RestMEM D CLa Ck Crk Cdeg` and `Proposition5Gram D CLa Ck Crk Cdeg 26 2 24 60` hold for all real $C_\Lambda, C_k, C_{rk}, C_{\deg}$. Then `ClosedFormOfAdmitted D` holds.

## Proof

Fix the constants and assume `admitted`. `RestMEM` gives $C_1 > 0$ such that `MemStep C CLa` holds for $C \ge C_1$. `Proposition5Gram` gives $C_D > 0$ and $C_2 > 0$ such that `Proposition5At` holds for $C \ge C_2$. The lemma `restNS_of` takes $\max(C_1, C_2)$. For $C$ above it, `nsStep_of` gives `NSStep`: `MemStep` supplies the condition `MemAt` that `Proposition5At` asks for. This is `RestNS`. Then `stmtE_of_TenNS` gives the result.

## In the Lean code

The theorem is at [TwistedSubstitution.lean line 18](lean:Formalism/SharpRestriction/GrowthBounds/TwistedSubstitution.lean#L18). `RestMEM`, `Proposition5Gram` and `restNS_of` are in [Proposition5Gram.lean](lean:Formalism/SharpRestriction/GrowthBounds/TwistedSubstitution/Proposition5Gram.lean#L100).

- `MemStep C CLa` reads only $C$ and $C_\Lambda$. So `RestMEM` does not use $C_k$, $C_{rk}$ or $C_{\deg}$ after `admitted`.
- `nsStep_of` is at line 89 of the same file.
