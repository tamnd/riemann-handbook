---
id: first-theorem-admitted-closed
title: The hypotheses of the base-level projection bound, for large constants
kind: theorem
decl: Formalism.MainNotions.G.first_theorem_admitted_closed
module: Formalism.SharpRestriction.GrowthBounds.PlaneCountTheoremWithConstants
covers: 312
status: drafted
drafted_by: writer@claude
---
This theorem proves `AdmBE D`: the five hypotheses `AdmB` of the base-level projection bound hold when the constants are chosen in the right order and are large. [`first_theorem_with_constants`](/entry/first-theorem-with-constants/) applies the field `p13B` of `Loc8All` to it. The proof does no new estimates. It merges nests of thresholds and passes their outputs to lemmas in `Joints`. Below it are 312 declarations.

## Statement

**Theorem.** Assume `ExtremalProjectorTools` and `Loc8All`. Then for each datum $D$, `AdmBE D` holds.

`AdmBE D` is `ClosedA (AdmB D)`. This nest says: for each $C_c \ge 0$ there is $T_0 > 0$; for each $C_0 \ge T_0$ there is $T_1 > 0$; for all $C_{E1}, C_{E2}, C_m \ge T_1$ there is $T_2 > 0$; for each $C_H \ge T_2$ there are $C_A, C_\kappa, C_t, C_s > 0$ with `AdmB D`. `AdmB D` is the conjunction of `PathPairCorrespondence`, `admB2`, `admB3`, `ColumnFamilyLowerSet` and `AdmT D`. We have not unfolded the first four.

## Proof

The proof uses three nests.

1. `extended_windows_theorem` applies the field `p15` to `inequality_admissions_hold`. It gives `ColumnSystems.Closed (ExtendedAllConclusions D)`. This nest has $C_c$, $C_0$, then $C_{E1}, C_{E2}, C_m$, then five constants $C_{Yb}, C_{de}, C_k, C_D, C_b$, and it gives $C_\kappa, C_t, C_s > 0$ with ten statements.
2. `thresholds_and` joins the field `p13A` with the fields `thresholdClauseOne` and `thresholdClauseThree`. The result is one `TransportedAlt` nest with the same levels, but without $C_m$.
3. At each level the threshold is the maximum of the two thresholds. All five constants $C_{Yb}, \dots, C_b$ are set to $C_H$.

Then:

- Step 1 gives $C_\kappa, C_t, C_s > 0$. The proof uses six of its ten statements. The threshold gives $C_m \ge 0$.
- `p13A`, at $C_\kappa$ and $C_s + C_\kappa$, gives $C_A > 0$. For each instance $X$ it turns eleven conditions into `Conclusion1`, a bound $C (t+1) N_1 / Y$ on a mean. The conditions come from `adm1`, `adm3`, `tKP1` to `tRES`, `instanceClauseEight`, and four `Joints` lemmas. One of these lemmas uses the conjunct `hT12` of `tool_statements_hold`.
- The output is $(C_A, C_\kappa, C_t, C_s + C_\kappa)$. Four `Joints` lemmas give the first four conjuncts of `AdmB`. `first_theorem_tools_admitted` gives `AdmT D`.

## In the Lean code

The theorem is in [PlaneCountTheoremWithConstants.lean](lean:Formalism/SharpRestriction/GrowthBounds/PlaneCountTheoremWithConstants.lean#L1238). `ClosedA` and `AdmB` are in [ProjectionLemmaBaseLevel.lean](lean:Formalism/SharpRestriction/GrowthBounds/ProjectionLemmaBaseLevel.lean#L239). `TransportedAlt` is in [FlipOneThree.lean](lean:Formalism/SharpRestriction/GrowthBounds/FlipOneThree.lean#L312), and `ColumnSystems.Closed` is in [ColumnSystems.lean](lean:Formalism/SharpRestriction/GrowthBounds/ColumnSystems.lean#L272).

Odd points:

- The proof calls `tool_statements_hold` but uses only one conjunct of it, `hT12`. The parts that [`splitting_package_holds`](/entry/splitting-package-holds/) proves are discarded here. They enter through `inequality_admissions_hold` and `first_theorem_tools_admitted`.
- One constant $C_H$ stands in for five constants. This is allowed, because the nests only ask for constants above a threshold.
- The datum $D$ only routes inputs. `flipOneThree.Conclusion1` takes its datum as `_D`.
