---
id: proposition5-holds
title: The numerical Proposition 5, from three proved parts
kind: theorem
decl: Formalism.MainNotions.Proposition5Numerics.proposition5_holds
module: Formalism.SharpRestriction.GrowthBounds.DiagonalSupport
covers: 431
status: drafted
drafted_by: writer@claude
---
This theorem proves `Proposition5Gram D CLa Ck Crk Cdeg 26 2 24 60` for every datum $D$ and all four constants. It is the second input of [`stmtE_of_mem`](/entry/stmt-e-of-mem/), which passes it to [`stmtE_of_MP`](/entry/stmt-e-of-mp/). That entry says what `Proposition5At` and its conclusion `NSConcl` ask. Here we describe how the three parts fit together.

## Statement

**Theorem.** For each $D$ of type `D7` and all real $C_\Lambda, C_k, C_{rk}, C_{\deg}$: if `admitted D CLa Ck Crk Cdeg` holds, there are $C_D, C_1 > 0$ such that `Proposition5At C CD CLa 26 2 24 60` holds for all $C \ge C_1$.

## Proof

`proposition5_of_three_parts` combines three facts. Each has the form "under `admitted`, there are positive constants such that a step holds for all $C$ above a threshold". The steps quantify over the same local data as `Proposition5At` and assume `DataII`.

1. `restPick` gives $C_{Dn}$ and `PickStep`. For each $G$ of multidegree `dT TT lam0` with the two `InWj` conditions and `MemAt`, `PickAt` picks signed chain data, a plane polynomial $F_2$ with `XX` and `vBB F2 = 0`, a normalizing polynomial $N_0$ and a scalar $k_0$. The valuation of $k_0$ is at most $v_p(\prod d!) - n_0 + D_n$, and for every integral $A$ of the plane degree the valuation of $\langle G, \mathrm{asm}(A, N_0)\rangle - k_0\, B(F_2, A)$ is at least $c_P + v_p(\prod d!) - \kappa$, where $c_P$ is the parameter `cPrime`.
2. `restMemb` gives `MembStep`. It writes each $\mathrm{asm}(\mathrm{ph}(G_p), N_0)$, for integral $G_p$ with `YY 24 60`, as a sum of one-sided "Lemma 4" elements of multidegree $d$.
3. `restNum` gives $C_{Dm} = 20$ and `NumStep`. This gives `Hyp 26` for the chain data, $4(D_m + D_l + 3k_p) < c$, $k_p \ge 0$, and $D_m + D_l + 3k_p \le C_{Dm} \cdot |T| (m+1)^2 \log_p a$.

The combination takes $C_D = C_{Dn} + 2C_{Dm} + 1$, and as threshold the largest of the three thresholds and $C_{Dn} + 3C_{Dm}$. For each $C$ above it, `proposition5_at_of_three_parts` gives `Proposition5At`. Its last step is `value_core`, which we have not unfolded.

## In the Lean code

The theorem is in [DiagonalSupport.lean](lean:Formalism/SharpRestriction/GrowthBounds/DiagonalSupport.lean#L13). The combination is in [Proposition5OfThreeParts.lean](lean:Formalism/SharpRestriction/GrowthBounds/DiagonalSupport/Proposition5OfThreeParts.lean#L176). `PickAt`, `MembAt` and `NumAt` are in [TwiceValuationFactorialProduct.lean](lean:Formalism/SharpRestriction/GrowthBounds/DiagonalSupport/TwiceValuationFactorialProduct.lean#L58), and `RestPick`, `RestMemb` and `RestNum` are at [line 127](lean:Formalism/SharpRestriction/GrowthBounds/DiagonalSupport/TwiceValuationFactorialProduct.lean#L127). The three parts are `restPick` in [GramExponentArithmetic.lean](lean:Formalism/SharpRestriction/GrowthBounds/DiagonalSupport/GramExponentArithmetic.lean#L223), `restNum` in [LeOfOneLeMul.lean](lean:Formalism/SharpRestriction/GrowthBounds/DiagonalSupport/LeOfOneLeMul.lean#L232), and `restMemb` in [MembFinal.lean](lean:Formalism/SharpRestriction/GrowthBounds/DiagonalSupport/MembFinal.lean#L10).

`restPick` and `restNum` start with `intro _`, so they do not use `admitted`. `restMemb` calls `membership_of_three_parts`, which we have not unfolded. We do not know which source the name "Proposition 5" refers to.
