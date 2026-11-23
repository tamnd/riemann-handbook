---
id: row-cusp-multiplicity-input-alt
title: The second step, the relay in the namespace T
kind: theorem
decl: GlobalTheory.T.row_cusp_multiplicity_input_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.SecondStepStatement
covers: 549
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It has the same statement as [the second step](/entry/second-step-alt/), and it proves it by calling that theorem. The real content is in that entry. The user is [the pointwise step](/entry/pointwise-alt-alt/).

## Statement

The statement is that of [the second step](/entry/second-step-alt/). In short: under global Artin reciprocity, `GalEx D`, `RowCusp` and six more conditions on a datum $D$ of type `D7`, there is a bound $c_0$ on the local coefficient fields such that, over twist rings with any larger bound, there are twist data and a datum `ex` with finitely generated spanning lattices for which the side record `SideB` holds.

## Proof

The proof is

```
first | exact @GlobalTheory.HeightCounting.FormsStep.second_step_alt | ...
```

The two statements are the same text, so the first branch closes the goal.

## In the Lean code

The theorem is in [SecondStepStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SecondStepStatement.lean#L11). It differs from the original only in the namespace and in the option `maxHeartbeats 1000000`. The name is misleading. `RowCusp` is only one of nine hypotheses, and no multiplicity appears in the statement. The hypothesis `MtInput D M tup Q` is carried along, and [the second step](/entry/second-step-alt/) never uses it. An older form, `row_cusp_multiplicity_input`, is in [RowCuspMultiplicityInputStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/RowCuspMultiplicityInputStatement.lean#L7); we have not compared the two statements.
