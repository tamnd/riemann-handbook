---
id: backward-of-line-formula
title: From fast decay on lines to an L² embedding
kind: theorem
decl: CompanionTheory.RgExh.Dec.L.backward_of_line_formula
module: CompanionTheory.RealGroups.DiscreteSeries.DiscreteSeriesClassification.DiscreteSeriesExhaustion.MatrixCoefficientDecay.HilbertSchmidtDecay.BackwardOfLineFormula
covers: 313
status: drafted
drafted_by: writer@claude
---
This theorem proves `Back`, the third input of [the decay estimate](/entry/decay-estimate/). Its proof only applies [`back_of_lineFormula`](/entry/back-of-line-formula/) to the proved integration formula `line_formula`. It adds that formula and nothing else. The parent entry defines $A$, $P_A$, $\rho_A$ and the decay rate; we use the same names.

## Statement

**Theorem** (`Back`). Assume `StepChar`. Let $\sigma$ be a unitary, square-integrable representation of $G$, with module $D$ of $K$-finite vectors and character $\chi$, and let $s_1, \dots, s_m$ be any path. Assume that for each $A$ with `IsGrad` and each Haar measure on $P_A$, every coefficient of the end module $X$ decays at rate $-\rho_A - 1$:
$$\int_0^\infty |f(x \exp(tA))|^2 e^{2(\rho_A + 1)t} \, dt < \infty \quad \text{for almost all } x \in P_A.$$
Then $X$ has the property `L2Embedding`.

The statement has no hypothesis on the labels. Far labels enter only through `Labels`, which gives the decay hypothesis.

## Proof

`backward_of_line_formula` is `back_of_lineFormula line_formula`. The theorem `line_formula` ([LineFinal.lean](lean:CompanionTheory/RealGroups/DiscreteSeries/DiscreteSeriesClassification/DiscreteSeriesExhaustion/MatrixCoefficientDecay/LineFormulas/LineFinal.lean#L8)) proves `LineFormula` from three named statements: `FubiniParabolicMultiple`, `rgExh_lineFacts` and `ParabolicSubgroupEquality`. We have not unfolded these.

## In the Lean code

The theorem is in [BackwardOfLineFormula.lean](lean:CompanionTheory/RealGroups/DiscreteSeries/DiscreteSeriesClassification/DiscreteSeriesExhaustion/MatrixCoefficientDecay/HilbertSchmidtDecay/BackwardOfLineFormula.lean#L22). `Back` is in [KeepsMul.lean](lean:CompanionTheory/RealGroups/DiscreteSeries/DiscreteSeriesClassification/DiscreteSeriesExhaustion/MatrixCoefficientDecay/KeepsMul.lean#L113).

- The theorem is a pass-through. The mathematics of `Back` is in `SA.assembly_of`, reached through [`back_of_lineFormula`](/entry/back-of-line-formula/).
- `back_of` ([BackOf.lean](lean:CompanionTheory/RealGroups/DiscreteSeries/DiscreteSeriesClassification/DiscreteSeriesExhaustion/MatrixCoefficientDecay/HilbertSchmidtDecay/BackOf.lean#L7)) passes the `StepChar` argument of `Back` twice to `assembly_of`. `assembly_of` uses the first copy and drops the second with `intro _`.
