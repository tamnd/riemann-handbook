---
id: pointwise-bound-discrete-series-coefficients
title: The pointwise bound for discrete series coefficients from two inputs (restatement)
kind: theorem
decl: GlobalTheory.T.pointwiseBound_discreteSeries_coefficients
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.PointwiseBoundDiscreteSeriesCoefficientsStatement
covers: 1095
status: drafted
drafted_by: writer@claude
---
This theorem is a restatement. It gives the two-input form of the bound `ThmBpDS` a second name. Its caller [A pointwise bound for discrete series coefficients](/entry/discrete-series-coef-pointwise-bound/) applies it to two proved inputs. The real content is in [`BpDiscreteSeriesTwoInputs.pointwise_bound_discreteSeries`](/entry/pointwise-bound-discrete-series/).

## Statement

**Theorem.** $\mathrm{BesselXiIntegrable} \Rightarrow \mathrm{ThmPActualCpt} \Rightarrow \mathrm{ThmBpDS}$.

`ThmBpDS` is the pointwise bound for $K$-finite matrix coefficients of discrete series of $U(H_{k,r})$, stated in full in [the entry above](/entry/discrete-series-coef-pointwise-bound/). `BesselXiIntegrable` is `B.XiExists`, the existence of a function $\Xi$ with a coefficient bound and an integrability condition at each real place datum. `ThmPActualCpt` says: for each real place datum $D$ there are submodules $K_0, \dots, K_r$ of a space of functions with three properties (`ThmPOn`, `SliceIn`, `CompositeFormulaLevelZero`, which we have not unfolded), and a fourth. For each compactly supported smooth $F$ with all weighted derivative bounds and with $G_f \ge \varepsilon$ on its support, the restriction of the transform `JF D F` agrees with an element of $K_0$.

## Proof

The statement is the same as the statement of `BpDiscreteSeriesTwoInputs.pointwise_bound_discreteSeries`. The proof is that theorem. There is no other step.

## In the Lean code

The theorem is in [PointwiseBoundDiscreteSeriesCoefficientsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/PointwiseBoundDiscreteSeriesCoefficientsStatement.lean#L9). The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)`, with `BpDiscreteSeriesTwoInputs.pointwise_bound_discreteSeries` in each branch. The two statements are the same text, so the first branch is enough. Many modules of this folder have this pattern: a file `…Statement.lean` that gives a theorem a name in the namespace `GlobalTheory.T`.
