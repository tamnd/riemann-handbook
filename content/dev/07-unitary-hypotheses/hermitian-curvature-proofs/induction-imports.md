---
id: induction-imports
title: The twelve step facts in the model setting
kind: theorem
decl: Formalism.FourierDecayAlt.P.induction_imports
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.IsAdmissibleSplittingCharPairMulTwist
covers: 366
status: drafted
drafted_by: writer@claude
---
This theorem proves `StepImportsQ`: each step of the model energy system satisfies twelve facts, with three constants that do not depend on the data. It is a bundle of twelve lemmas, which have no entries of their own. [The energy limit in the model setting](/entry/lemma-model/) gives it to `lemma_model_of_parts`.

## Statement

Fix model data that satisfy `Hyps`, a cutoff $c$, and a list $w$ of points in the boxes of the system `sysQ` with fewer than $N$ points. Let $S$ be the step of `sysQ` at $w$ and put $\sigma = 4N$. The step has a vector $X$, weights $d_w$ and $d_Y$, an operator $g_Y$ with a partner $g_Y^*$, matrices $e_Y$ and a function $P$, for $Y$ in an interval $J$. The values of $g_Y$ have coordinates $(b, i)$ with $b \in \{0, 1\}$.

**Theorem.** There are $C_R \ge 0$, $C_d \ge 0$ and $C_P \ge 0$ such that each such step satisfies `Imports c σ C_R C_d C_P`. Its twelve conjuncts fall into four groups:

- Regularity: $X$, $d_w$, $d_Y$ and the shifted vectors are measurable (`Meas`), $d_w > 0$ and $d_Y > 0$ (`WPos`), and $P$ is continuous and nonzero on $J$ (`PReg`).
- Identities: $g_Y^*(d_Y \, g_Y X) = |P(Y)| \, d_w X$ (`I3`), an adjoint relation for $g_Y$ against cutoff functions (`AdjB`), and the shift formula (`ShiftFormula`). The shift formula writes the shifted vector at $Y$ through $g_{Y+s} X$ and $e_Y - e_{Y+s}$.
- Shift behaviour: the jet property `Jet` and the polynomial property `I4` of degree $r + 1$, and integrability and continuity of the shifted energies (`I4'`).
- Bounds: $\sum_i d_Y(1, i) \, |((e_Y - e_{Y+s}) v)_i|^2 \le C_R^2 \sum_i d_Y(0, i) \, |v_i|^2$ (`Residues`), $d_Y \le C_d \, d_{Y+s}$ (`WeightRatio`) and $|P(Y+s)| \le C_P |P(Y)|$ (`PRatio`), for $Y, Y + s \in J$.

We have not unfolded `JetLocal`, `PolyS`, `gs` or `sysQ`.

## Proof

`induction_imports_of_parts` takes $C_R$ from `residuesAlt` and $C_d$ from `weight_ratio`, and puts $C_P = e^3$. Then each conjunct is one lemma. There is no other step.

## In the Lean code

The theorem is in [IsAdmissibleSplittingCharPairMulTwist.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/IsAdmissibleSplittingCharPairMulTwist.lean#L17973). `StepImportsQ` is in [StatementMA.lean](lean:Formalism/HermitianCurvature/StatementMA.lean#L681), `Imports` in [StatementLE.lean](lean:Formalism/HermitianCurvature/StatementLE.lean#L208), and `induction_imports_of_parts` in [SquareIntegrableGammaZetabarInv.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/SquareIntegrableGammaZetabarInv.lean#L989).

`polynomial_regular` and `probability_ratio` are the two halves of one lemma, `imported_results_hold`, applied with `roots_outside`.

Several names do not match their statements. No induction appears. `probability_ratio` proves `PRatio`, a bound on the ratio of values of $P$; no probability appears. `fourth_identity_dual` proves `I4'`, which is integrability and continuity, not an identity. `fifth_identity_first` proves the shift formula.
