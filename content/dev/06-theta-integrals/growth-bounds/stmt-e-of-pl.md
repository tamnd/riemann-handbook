---
id: stmt-e-of-pl
title: Statement E from the plane bound
kind: theorem
decl: Formalism.MainNotions.PairMembershipBlocks.stmtE_of_pl
module: Formalism.SharpRestriction.GrowthBounds.PlaneCoefficients
covers: 1837
status: drafted
drafted_by: writer@claude
---
This theorem reduces [Statement E](/entry/stmt-e/) for a datum $D$ to the plane bound `RestPl`. It fills in two of the three hypotheses of [Statement E from the last steps](/entry/stmt-e-of-last/) with proved facts and applies that theorem. Its only user is [Statement E from the chain bound](/entry/stmt-e-of-chain/), which proves `RestPl`. The real content is in [Statement E from the last steps](/entry/stmt-e-of-last/).

## Statement

**Theorem.** Let $D$ be a datum of the type `D7`. If `RestPl` holds, then `ClosedFormOfAdmitted D` holds.

`RestPl` is the conjunction of the chain bound and the link bound, see [Statement E from the chain bound](/entry/stmt-e-of-chain/). `ClosedFormOfAdmitted D` is stated in [Statement E](/entry/stmt-e/).

## Proof

The proof is `stmtE_of_last D noOpStep hPl hAr`, with these two inputs.

1. `noOpStep` proves `NoOpStep`. This is a statement about the operators `derN`, `mulN` and their product on polynomials over the fraction field of $O$, under a projector condition `IsJProj`. We have not unfolded it further.
2. `hAr` is the pair $C_1 = 1$, $0 < 1$, and the map that sends $C \ge 1$ and $C_\Lambda$ to `arithCondition_of_one_le C CLa`. This proves that `RestArithStep C CLa` holds for all $C \ge 1$ and all $C_\Lambda$. `RestArithStep C CLa` says that, under the hypotheses `DataII` on the local data, the frames have $J \ge 2$, and the degree term `dwB` of [Statement E from the chain bound](/entry/stmt-e-of-chain/) is at most $\frac18$ of a term `slU`. We have not unfolded `DataII` or `slU`.

## In the Lean code

The theorem is at [PlaneCoefficients.lean line 46](lean:Formalism/SharpRestriction/GrowthBounds/PlaneCoefficients.lean#L46), and `stmtE_of_last` at line 42.

- The theorem only passes its hypothesis along, with two proved facts filled in.
- `NoOpStep` is in [NoOpStep.lean line 91](lean:Formalism/SharpRestriction/GrowthBounds/PlaneCoefficients/NoOpStep.lean#L91) and its proof `noOpStep` in [Lam1SPderivAndXMulLeAddIndicator.lean line 38](lean:Formalism/SharpRestriction/GrowthBounds/MonomialSupport/Lam1SPderivAndXMulLeAddIndicator.lean#L38). `RestArithStep` is in [PlaneCoeffOneTTens.lean line 183](lean:Formalism/SharpRestriction/GrowthBounds/PlaneCoefficients/PlaneCoeffOneTTens.lean#L183) and `arithCondition_of_one_le` in [FortyEightBoundArith.lean line 51](lean:Formalism/SharpRestriction/GrowthBounds/PlaneCoefficients/FortyEightBoundArith.lean#L51).
