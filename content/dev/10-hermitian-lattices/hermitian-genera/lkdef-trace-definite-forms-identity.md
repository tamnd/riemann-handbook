---
id: lkdef-trace-definite-forms-identity
title: The sum over definite pairs is an automorphic trace
kind: theorem
decl: GlobalTheory.LKDef.trace_definite_forms_identity
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.LieModelBaseChangeMap
covers: 344
status: drafted
drafted_by: writer@claude
---
This theorem proves `TraceDefinitePairsEqAutomorphicTrace`: the weighted sum `dSumIrr` over definite pairs equals a sum of Hecke traces on spaces of automorphic forms of definite unitary groups. The proof is short. It puts together three lemmas and compares the two sides term by term. Its second name is [cnt-trace-definite-forms-identity](/entry/cnt-trace-definite-forms-identity/), and the sum on the left is the one of [the weighted count](/entry/weighted-count-definite-unitary/).

## Statement

The statement and the names $\Gamma_\beta$, $\mathcal{A}_\beta(\xi)$, $\mathrm{wt}$, $f$ and $f'$ are as in [the second name](/entry/cnt-trace-definite-forms-identity/). We recall two points. The condition on $\xi$ is: $\operatorname{tr}\xi(y) = \mathrm{wt}(P_y)$ for each $y \in \Gamma_\beta$ whose minimal polynomial $P_y$ over $F$ has degree $n$ and is separable. The vanishing condition is: the orbital sum `orbK` of $f \otimes f'$ at $y$ is $0$ for each $y$ that is not `RegIrr` (degree $n$, separable and irreducible).

## Proof

Fix a class $[\beta]$ of definite forms and a representative $\beta$ (`Quot.out`). For a conjugacy class $c$ of $\Gamma_\beta$, with representative $y_c$, let $S_\beta(c)$ be the term `centSum` at $y_c$. It is a sum over double cosets of the centralizer of $y_c$, with weights $1/|\mathrm{stab} \cap \mathrm{centralizer}|$.

1. Regroup the left side (`bi_invariant_test_function_sum`):
$$\mathrm{dSumIrr} = \sum_{[\beta]} \sum_{c} [\text{$y_c$ is RegIrr}] \cdot \mathrm{wt}(P_{y_c}) \cdot S_\beta(c).$$
2. Expand each trace on the right (`heckeTrace_definiteForm_eq_sum_conjClasses`):
$$\operatorname{tr}\bigl(T \mid \mathcal{A}_\beta(\xi)\bigr) = \sum_{c} \operatorname{tr}\xi(y_c) \cdot S_\beta(c).$$
3. Compare the terms for each $[\beta]$ and $c$. If $y_c$ is `RegIrr`, then $\operatorname{tr}\xi(y_c) = \mathrm{wt}(P_{y_c})$ by the condition on $\xi$. If not, the vanishing condition gives `orbK` $= 0$ at $y_c$, and `centSum_eq_zero_of_orbitalIntegral_eq_zero` turns this into $S_\beta(c) = 0$. So both terms are $0$.

The sums are `finsum`, and the proof compares them with `finsum_congr`. It does not need to know that they are finite.

## In the Lean code

The theorem is in [LieModelBaseChangeMap.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LieModelBaseChangeMap.lean#L14). The statement and `dTrace` are in [TraceDefinitePairsEqAutomorphicTrace.lean](lean:Development/AbelianVarietyTheory/Statements/PlaceShiftStatements/TraceDefinitePairsEqAutomorphicTrace.lean#L87). The three lemmas are aliases. Their real proofs are `GlobalTheory.LKDef.Regroup.regroup` in [RelIndexPrincipalCongruenceNeZero.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/RelIndexPrincipalCongruenceNeZero.lean#L10), `GlobalTheory.HeckeTrace.dform_trace_eq` in [HeckeTraceDefiniteFormEqSumConjClasses.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HeckeTraceDefiniteFormEqSumConjClasses.lean#L228), and `GlobalTheory.LKDef.DForm.centSum_eq_zero_of_orbK` in [CentSumEqZeroOfOrbitalIntegralEqZero.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CentSumEqZeroOfOrbitalIntegralEqZero.lean#L152). We have not opened those proofs.

The vanishing condition is stated for every trivialization $(x, t)$ of $\beta$ at $p$. The proof uses it only at the trivialization that `B.trivAf` chooses. The module name `LieModelBaseChangeMap` has no relation to the content.
