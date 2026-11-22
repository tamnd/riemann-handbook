---
id: field0
title: The proof of the Čech form of the Lefschetz formula, as a chain of named facts
kind: theorem
decl: field0
module: Development.AutomorphicArithmetic.Foundations.EtaleClopenDescent.ExistsChartLiftOfFiniteCover
covers: 1192
status: drafted
drafted_by: writer@claude
---
This private theorem proves the [Čech form of the holomorphic Lefschetz formula](/entry/t-exists-chart-lift-of-finite-cover/), under the public name [`Cb.exists_chart_lift_of_finite_cover`](/entry/cb-exists-chart-lift-of-finite-cover/). It does no mathematics itself. It chains about 95 named facts and passes them to `fieldLe_of`, which has the real content.

## Statement

The statement is the proposition `Field0`. It is the [Čech form of the formula](/entry/t-exists-chart-lift-of-finite-cover/), with all its hypotheses.

## Proof

The proof has three parts.

1. **Named facts.** There are 95 `have` lines. Each proves one proposition of the namespace `UpperTheory.Gal.productCup_of_system` by one lemma, often from earlier lines: for example Koszul complexes (`koszulExactBelowLengthOfWeaklyRegular_of_htpy`), filtrations and cocycle lifts (`filtrationCocycleLiftCriterion_of_wdBasic`), Čech-Koszul systems (`coordinateSystem_degree_two_of_universalDerivation`), edge maps (`edgeB_of`) and traces (`trTop_of`, `trLin_of`). We have not unfolded these propositions.
2. **The case $a \leq d$.** `fieldLe_of` takes 14 of the facts and proves `FieldLe`. This is the same trace identity with three changes: the coordinates $x_i$ are units, the hypotheses are packed in a structure `Y1`, and only $a \leq d$ is asked. `FieldLe` has no hypothesis on regular parameters on $K$ or on finite dimension. The proof of `fieldLe_of` starts with a top-degree coefficient form (`exists_topDegreeCoefficientForm_and_eq_on_top_forms`) and a Laurent constant term form (`exists_laurentConstantTermForm_functionField`), and it uses the fact `ResidueOfTraceIsFiberSum`. We have not read the rest of it.
3. **Assembly.** `field0_of` turns `FieldLe` into `Field0`. For $a \leq d$ it builds `Y1` from the hypotheses and applies `FieldLe`. In the tangent condition it divides by $c$, which is not $0$ because $e(c) \neq 0$ (`val_div`). For $a > d$ both sides are $0$. The $a$-forms on the charts are $0$ (`dlog_basis_and_vanishing_above_dimension`), so each trace is $0$ (`trace_eq_zero_of_bot`). The coefficient of $t^a$ in $\det(1 + tA_e)$, a polynomial of degree at most $d$, is $0$ (`coeff_det_eq_zero`).

## In the Lean code

`field0` is at [ExistsChartLiftOfFiniteCover.lean](lean:Development/AutomorphicArithmetic/Foundations/EtaleClopenDescent/ExistsChartLiftOfFiniteCover.lean#L101). The call to `fieldLe_of` is at line 195 and the call to `field0_of` at line 196.

- `Field0` and `FieldLe` are in [ResidueOfTraceIsFiberSum.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/LocalMaximality/ResidueOfTraceIsFiberSum.lean#L270).
- `fieldLe_of` is in [PFieldLe.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/LocalMaximality/PFieldLe.lean#L216).
- `field0_of` is in [TraceEqZeroOfBot.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/LocalMaximality/TraceEqZeroOfBot.lean#L49).

`field0_of` takes `ValBasic` as a hypothesis and does not use it. It also binds the regular parameter hypothesis and the finite dimension hypothesis of `Field0` (as `hgen` and `hfd`) and does not use them. Its other bound names do not match their hypotheses: `hred` is the cover condition, `hnf` is the reduced fibre, and `hz` says that charts $i \neq 0$ have no fixed points.
