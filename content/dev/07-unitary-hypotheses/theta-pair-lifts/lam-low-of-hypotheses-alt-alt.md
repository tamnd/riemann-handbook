---
id: lam-low-of-hypotheses-alt-alt
title: The lambda lower bound from seven published inputs
kind: theorem
decl: GlobalTheory.BigTop.lamLow_of_hypotheses_alt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.LamLowOfPublished
covers: 312
status: drafted
drafted_by: writer@claude
---
This theorem proves `LambdaLowerBound₂`, the second half of branch 2 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). Its only user is [`ontoX_and_lamLow_of_unitaryGroupHypotheses'`](/proof/unitary-hypotheses/), which pairs it with [the surjectivity statement](/entry/onto-x-of-hypotheses-alt-alt/). The proof checks two size bounds along the family and passes everything else to one closing lemma. Below this theorem are 312 declarations.

## Statement

**Theorem.** Assume the seven inputs `CuspRapidDecay`, `WeilSiegelFormulaUnitary`, `SiegelWeilUnitaryConvergent`, `DoublingMethodLocalZetaIntegrals`, `UnramifiedDoublingGL`, `BernsteinZelevinskyFiniteness` and `FormalDegreeCompactDual`. Then for each closed family hypothesis and each family $F_m$ in it, eventually at points $p$ of $F_m$, the statement `L6` holds for the data `p.S true` at the numbers `p.N C CH`, for every $C$.

The names of the inputs say: rapid decay of cusp forms, the Siegel-Weil formula for unitary groups and its convergent range, local zeta integrals of the doubling method, the unramified doubling computation for $\mathrm{GL}$, a finiteness theorem of Bernstein-Zelevinsky type, and formal degrees with a compact dual. We have not unfolded them or `L6`.

## Proof

1. `closed_Csz_ge FamHyp 8` lets us assume that the size constant of the family is at least 8.
2. `thetaLift_weightSizes_eventually_along_family` gives $x_0$ such that, for $x \ge x_0$, the size condition `Sizes` holds at each level $j$ with the constant $b$ of the point.
3. `finiteness_inputs_real_data_three_alt` gives `L6` from the seven inputs, from the data and thirteen fields of the point $p$, from step 2 and from two inequalities for each level $j$:
   - $\ell_{6,m}(j) \le \mathrm{lowB}(j, b)$. This is `hookLogSum_sub_sizeTerm_le_lowerBound`: a sum of log hook terms minus $C_{\mathrm{sz}} f\, n_V^2 L_p$ is at most $\mathrm{lowB}(j, b)$, and it uses $C_{\mathrm{sz}} \ge 8$.
   - $\ell_6(j) \le \ell_{6,m}(j)$. Here $\ell_6(j)$ unfolds to $\ell_{6,m}(j) - C \cdot 0$, so the bound is an equality.

## In the Lean code

The theorem is in [LamLowOfPublished.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LamLowOfPublished.lean#L17). `LambdaLowerBound₂` is in [Realised.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/Realised.lean#L126). `finiteness_inputs_real_data_three_alt` is in [FinitenessInputsRealDataThree.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/FinitenessInputsRealDataThree.lean#L35). It is a second name for `LowRow.lamLow_closing_alt`, which has the real content and which we have not opened.

The second inequality is proved by `show _ - C * 0 ≤ _`, then `mul_zero`, `sub_zero` and `le_rfl`. So in this step the constant $C$ enters only through a factor 0, and the bound is the same for all $C$. A parallel copy, `GlobalTheory.BigTop.lamLow_of_classicalTheorems`, is in [LamLowOfPublished.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LamLowOfPublished.lean#L30).
