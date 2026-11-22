---
id: stmt-e-of-mem
title: The closed form of the valuation bound, from the membership step
kind: theorem
decl: Formalism.MainNotions.Proposition5Numerics.stmtE_of_mem
module: Formalism.SharpRestriction.GrowthBounds.DiagonalSupport
covers: 1316
status: drafted
drafted_by: writer@claude
---
This theorem proves `ClosedFormOfAdmitted D` from one hypothesis, the membership statement `RestMEM`. It supplies the second input, a numerical "Proposition 5", by a proof in the same folder. Its only user is [the version from the plane step](/entry/stmt-e-of-last/), which builds `RestMEM`. The chain goes up to [`stmtE`](/entry/stmt-e/).

## Statement

Let $D$ be a datum of type `D7`. Let $\mathrm{adm}(D; C_\Lambda, C_k, C_{rk}, C_{\deg})$ be the conjunction of 37 conditions `admitted`, and let $\mathrm{Concl}$ be `ConclusionE D`: there is $C_0 > 0$ with `aux₃ D C` for all $C \ge C_0$. The [entry above](/entry/stmt-e-of-last/) says what `aux₃` asks.

For constants $C$ and $C_\Lambda$, `MemStep C CLa` says: for each prime $p$, each setting of discrete valuation rings, each orbit and weight datum, each frame $F$ and each linearly independent family $B$ that together satisfy `DataII`, each polynomial $G$ in the operator closure `OpCl` of the span of the symbols `symP` of $B$ satisfies `MemAt`. We have not unfolded `OpCl`, `symP` or `MemAt`.

**Theorem.** Assume that for all constants $C_\Lambda, C_k, C_{rk}, C_{\deg}$, $\mathrm{adm}(D; \dots)$ implies that there is $C_1 > 0$ with `MemStep C CLa` for all $C \ge C_1$. Then for all constants, $\mathrm{adm}(D; \dots)$ implies $\mathrm{Concl}$.

## Proof

The proof is one line: `stmtE_of_MP D hM (proposition5_holds D ...)`. The work is in the two lemmas.

1. `proposition5_holds` proves `Proposition5Gram D CLa Ck Crk Cdeg 26 2 24 60` for all constants. This says: under $\mathrm{adm}$, there are $C_D, C_1 > 0$ such that for $C \ge C_1$ the statement `Proposition5At` holds, with the four constants $C_H = 26$, $C_E = 2$, $C_6 = 24$, $C_{18} = 60$. `Proposition5At` gives a number $D_X \le C_D \, |T| \, (m+1)^2 \log_p a$ and, for each $G$ as above that also satisfies `MemAt`, a degree condition and two conditions `InWj`, the conclusion `NSConcl`. That conclusion ends in a bound `ValLe` by $D_X$ on a Fock pairing of $G$. The proof `proposition5_of_three_parts` combines three proved parts, `restPick`, `restMemb` and `restNum`.
2. `stmtE_of_MP` takes `RestMEM` and `Proposition5Gram`. It calls `stmtE_of_TenMP` with the proved fact `tensor_operators_holds` (the statement `TenOp`, on words of operators on tensor products of dual Weyl modules). Then `restNS_of` joins the two inputs into `RestNS`, and `stmtE_of_TenNS` and `stmtE_of_OpNS` finish with `theorem_II_closed_of_test_bound`.

We have not unfolded `NSConcl` or the proof of `theorem_II_closed_of_test_bound`.

## In the Lean code

The theorem is in [DiagonalSupport.lean](lean:Formalism/SharpRestriction/GrowthBounds/DiagonalSupport.lean#L16), with `proposition5_holds` at [line 13](lean:Formalism/SharpRestriction/GrowthBounds/DiagonalSupport.lean#L13). The lemmas it calls:

- `stmtE_of_MP` in [TwistedSubstitution.lean](lean:Formalism/SharpRestriction/GrowthBounds/TwistedSubstitution.lean#L23);
- `proposition5_of_three_parts` in [Proposition5OfThreeParts.lean](lean:Formalism/SharpRestriction/GrowthBounds/DiagonalSupport/Proposition5OfThreeParts.lean#L176);
- `restNS_of`, `RestMEM` and `Proposition5Gram` in [Proposition5Gram.lean](lean:Formalism/SharpRestriction/GrowthBounds/TwistedSubstitution/Proposition5Gram.lean#L100);
- `stmtE_of_TenNS` in [DualFockLinear.lean](lean:Formalism/SharpRestriction/GrowthBounds/DualFockLinear.lean#L24).

We do not know which source the name "Proposition 5" refers to. As in the entry above, the conclusion does not depend on $D$, because `aux₃` ignores its first argument.
