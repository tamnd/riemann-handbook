---
id: lifts-two-mul-def-bound-sub-unit-e-le-mu-core
title: The defect bound below the core slope, as a level statement
kind: theorem
decl: GlobalTheory.CovTop.DefCore.lifts_two_mul_defBound_sub_unitE_le_muCore
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.DefectBoundOfConnected
covers: 872
status: drafted
drafted_by: writer@claude
---
This theorem turns the pointwise bound of [defect_bound_of_connected_alt](/entry/defect-bound-of-connected-alt/) into a level statement. Its only user is its renaming [two_mul_defBound_sub_le_muCore_of_gramAt](/entry/two-mul-def-bound-sub-le-mu-core-of-gram-at/), which gives the first step of [the low defect bound](/entry/covering-low-defect-alt/). Below this theorem are 872 declarations.

## Statement

The statement is the same as that of [its renaming](/entry/two-mul-def-bound-sub-le-mu-core-of-gram-at/): if `PublishedHodgeBundleTheorems` holds, then there is $C \ge 0$ such that, at each large point $p$ and each level $i$ with $i + 1 = m$ and `GramAt`,
$$2\,\mathrm{defBound}(-\mathrm{flatDegVal}) - C u \le \mu_{\mathrm{core}}(p, i).$$

## Proof

The pointwise theorems need two more hypotheses at the point: `WtNum` (the shape of the weight) and `HostNum` with a constant $M$ (sizes of the host field). Their level statements hold with no hypothesis: `wtN_z` proves `LiftWeightNumerator`, and `hostN_alt M` proves `HostNAlt M` for each $M$.

The proof splits on `FnAlgClosed`: the base field is algebraically closed in the function field of each component of the moduli space at level $i + 1$.

1. If it holds, [defect_bound_of_connected_alt](/entry/defect-bound-of-connected-alt/) gives the bound with a constant $C_1$.
2. If it does not hold, `two_defBound_sub_unitError_le_muCore_alt` gives the bound with a constant $C_2$.

Take $C = \max(C_1, C_2)$. Since $u \ge 0$ (`unitE_nonneg`), a bound with $C_j$ gives the bound with $C$. The rest is bookkeeping with `Closed.imp` and the maximum of three thresholds.

## In the Lean code

The theorem is at [DefectBoundOfConnected.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/DefectBoundOfConnected.lean#L32). It calls `defect_bound_of_connected_alt`, `two_defBound_sub_unitError_le_muCore_alt`, `GlobalTheory.CovTop.WtShape.wtN_z`, `GlobalTheory.CovTop.Sizes.hostN_alt` and `unitE_nonneg`.

The second case is empty. `two_defBound_sub_unitError_le_muCore_alt` is a renaming of `isDefined_of_not_functionField_algClosed_alt` in [IsDefinedOfNotFunctionFieldAlgClosed.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/IsDefinedOfNotFunctionFieldAlgClosed.lean#L14). That proof derives a contradiction from `fnAlgClosed_core_alt`, which proves `FnAlgClosed` at each level from `RowsTAlt` alone. So the case split could be replaced by one call of `fnAlgClosed_core_alt`. The hypothesis `PublishedHodgeBundleTheorems` is passed to both theorems, and neither reads it.
