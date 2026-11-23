---
id: stmt-e-of-op-ns
title: The closed form of the valuation bound, from the two test-side halves
kind: theorem
decl: Formalism.MainNotions.TestSideCounting.stmtE_of_OpNS
module: Formalism.SharpRestriction.GrowthBounds.DualFockLinear
covers: 498
status: drafted
drafted_by: writer@claude
---
This theorem proves `ClosedFormOfAdmitted D` from two test-side hypotheses, `RestTSOp` and `RestNS`. It builds from them the test bound `RemainingInputsAfter` for `theorem_II_closed_of_test_bound`. Its only user is [the version with `TenOp`](/entry/stmt-e-of-ten-ns/), which proves `RestTSOp`. The chain goes up through [`stmtE_of_mem`](/entry/stmt-e-of-mem/) to [`stmtE`](/entry/stmt-e/).

## Statement

Let $D$ be a datum of type `D7`. For real constants $C_\Lambda, C_k, C_{rk}, C_{\deg}$, write $\mathrm{adm}$ for `admitted D CLa Ck Crk Cdeg`.

**Theorem.** Assume that for all four constants both of these hold:

1. `RestTSOp`: if $\mathrm{adm}$, there is $C_1 > 0$ such that `TSOpStep C` holds for all $C \ge C_1$;
2. `RestNS` with the constants $26, 2, 24, 60$: if $\mathrm{adm}$, there are $C_D, C_1 > 0$ such that `NSStep C CD CLa 26 2 24 60` holds for all $C \ge C_1$.

Then `ClosedFormOfAdmitted D` holds.

`TSOpStep C` quantifies over the local data of `aux₃`, a Witt identification, an edge $e$ whose target is the standard lattice, and a true theta map $\Theta$ (`IsTrueTheta`). It asks for `TSOpAt`: two dualities $\Psi_0, \Psi_f$ with the property `TSProp`, such that each pairing against a product $\Theta(F)\, s$ equals, up to a power of $p$, a pairing with $\Theta(F')$ for some $F'$ in the operator closure `OpCl` of $F$. `NSStep` is described in [the entry for `stmtE_of_mem`](/entry/stmt-e-of-mem/). We have not unfolded `TSProp` or `IsTrueTheta`.

## Proof

1. `theorem_II_closed_of_test_bound` gives $C \ge 1$ such that, for every $D$ and all constants, $\mathrm{adm}$ and `RemainingInputsAfter D ... C (C+1) C 26 2 24 60` imply `ConclusionE D`. Its proof uses `cleaning_of_admitted`, `plane_gram_of_admitted` (which calls [the plane Gram estimate](/entry/stmt/)), `rest6a` and `theorem_II_of_split_cloud_bounds`.
2. `test_bound_of_two_halves` builds `RemainingInputsAfter` from two halves, `RestCloudB` and `RestFlat`. It adds the two constants and takes the larger of the two thresholds.
3. `restCloudB_of_op` gives `RestCloudB` from `RestTSOp`. It adds the proved size bound `restSize` (with constant $4$ and threshold $2$) through `restCloudB_of_two`.
4. `restXi_of_NS` gives `RestXi` from `RestNS`, and `restFlat_of_Xi` gives `RestFlat` from it with the proved fact `restReal`. In `restXiP_of_NS`, the plane Gram estimate turns each `NSAt` into `XiAtP`.

## In the Lean code

The theorem is in [DualFockLinear.lean](lean:Formalism/SharpRestriction/GrowthBounds/DualFockLinear.lean#L14). The lemmas it calls:

- `theorem_II_closed_of_test_bound` in [Closed.lean](lean:Formalism/SharpRestriction/GrowthBounds/DualFockLinear/Closed.lean#L42);
- `test_bound_of_two_halves` in [TestSideExplicitIdentification.lean](lean:Formalism/SharpRestriction/GrowthBounds/DualFockLinear/TestSideExplicitIdentification.lean#L149);
- `restCloudB_of_op` in [LogSizeBoundLe.lean](lean:Formalism/SharpRestriction/GrowthBounds/DualFockLinear/LogSizeBoundLe.lean#L170);
- `restFlat_of_Xi` in [ScaleZeroIff.lean](lean:Formalism/SharpRestriction/GrowthBounds/DualFockLinear/ScaleZeroIff.lean#L180);
- `restXi_of_NS` and `RestNS` in [RestXiPOfNS.lean](lean:Formalism/SharpRestriction/GrowthBounds/DualFockLinear/RestXiPOfNS.lean#L87).

`RestTSOp` is in [RestCloudBOfThree.lean](lean:Formalism/SharpRestriction/GrowthBounds/DualFockLinear/RestCloudBOfThree.lean#L102).

The proof repeats the proof of `stmtE_of_rests` in [Closed.lean](lean:Formalism/SharpRestriction/GrowthBounds/DualFockLinear/Closed.lean#L49), with the two halves built inside instead of taken as a hypothesis. The hypothesis is asked for all four constants, but the proof uses it only at the constants of the call.
