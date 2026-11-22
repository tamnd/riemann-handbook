---
id: rest-mem-of-last
title: The membership input, from the operator rule, the plane bound and the arithmetic step
kind: theorem
decl: Formalism.MainNotions.PairMembershipBlocks.restMEM_of_last
module: Formalism.SharpRestriction.GrowthBounds.PlaneCoefficients
covers: 375
status: drafted
drafted_by: writer@claude
---
This lemma builds the membership input `RestMEM D` from the three hypotheses of [`stmtE_of_last`](/entry/stmt-e-of-last/). That entry lists the hypotheses and the two parts of the proof. This entry adds what the two parts give and how they join. The user of `RestMEM` is [`stmtE_of_mem`](/entry/stmt-e-of-mem/).

## Statement

**Theorem.** Assume `NoOpStep`, `RestPl`, and that there is $C_1 > 0$ such that `RestArithStep C CLa` holds for all $C \ge C_1$ and all $C_\Lambda$. Then for each $D$ of type `D7` and all real $C_\Lambda, C_k, C_{rk}, C_{\deg}$, the statement `RestMEM D CLa Ck Crk Cdeg` holds: under `admitted`, there is $C_1' > 0$ such that `MemStep C CLa` holds for all $C \ge C_1'$.

`MemStep` asks that each $G$ in the operator closure `OpCl` of the span of the symbols `symP (B b)` satisfies `MemAt`. By `memAt_iff`, `MemAt` is `MemAtG (1/8) (3/8)`. `MemAtG sc sL` asks that each plane coefficient of $G$, for signed chain data with the growth bound `TwistedSubstitutionGrowthBound` at the two scales `sc` and `sL`, satisfies `XX`.

## Proof

`memCondition_of_theoremII` joins two inputs and takes the larger of their thresholds.

1. `Lemma5aTheoremII`, from `lemma5a_of_monomial` and `rest5aMono_of_cut`: each symbol `symP (B b)` satisfies `MemAtG 0 (1/8)`.
2. `RestWord`, from `restWord_of_steps` and `opSteps_of`: if $F$ satisfies `MemAtG 0 (1/8)`, then for each word $l$ with letters in $T$ and at most $c_0$ letters for each block, `opWord l F` satisfies `MemAtG (1/8) (3/8)`.

Then `memAt_of_wordConditionAt` runs two inductions over spans. The first puts the whole span of the symbols in `MemAtG 0 (1/8)`. The second puts `OpCl` in `MemAtG (1/8) (3/8)`. Both use that `MemAtG` is closed under $0$, sums and scalar multiples.

## In the Lean code

The lemma is in [PlaneCoefficients.lean](lean:Formalism/SharpRestriction/GrowthBounds/PlaneCoefficients.lean#L34). `memCondition_of_theoremII`, `Lemma5aAt` and `WordConditionAt` are in [MemRed.lean](lean:Formalism/SharpRestriction/GrowthBounds/TwistedSubstitution/MemRed.lean#L72), and `MemAtG` is in [MemLin.lean](lean:Formalism/SharpRestriction/GrowthBounds/TwistedSubstitution/MemLin.lean#L39).

Two of the proved parts do not use `admitted`. `rest5aMono_of_cut` in [PlaneCoeffOneTTens.lean](lean:Formalism/SharpRestriction/GrowthBounds/PlaneCoefficients/PlaneCoeffOneTTens.lean#L281) introduces it as `_`. `restOneOp_of` in [RestOneOpOf.lean](lean:Formalism/SharpRestriction/GrowthBounds/PlaneCoefficients/RestOneOpOf.lean#L133) is `fun _ => ...` with threshold $1$.
