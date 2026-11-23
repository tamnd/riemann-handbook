---
id: jacquet-rallis-unit-match-succ
title: The induction step for unit matching (named form)
kind: theorem
decl: GlobalTheory.T.jacquetRallisUnitMatch_succ
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.JacquetRallisUnitMatchSuccStatement
covers: 327
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`UnitStep.unitMatch_succ`](/entry/unit-match-succ/), which has the proof. It is the induction step in [unit matching from the quadratic Weil representation](/entry/unit-match-of-weil-field/): it goes from the fundamental lemma for unit functions in rank $r$ to rank $r + 1$. Below it are 327 declarations of the proof.

## Statement

Assume $\mathrm{WeilEt}$ and $\mathrm{GammaOne}$. Then for every $r \ge 0$,

$$\mathrm{FourierMatch}(r + 1) \text{ and } \mathrm{UnitMatch}(r) \implies \mathrm{UnitMatch}(r + 1).$$

$\mathrm{UnitMatch}$ is defined in [the entry with the induction](/entry/unit-match-of-weil-field/). $\mathrm{FourierMatch}$, $\mathrm{WeilEt}$ and $\mathrm{GammaOne}$ are defined in [the entry on Fourier matching](/entry/fourier-match-of-weil-field/). In short: the Weil representation exists for every étale algebra, its constant is $1$ for the standard Hermitian space, and matching survives the partial Fourier transform in rank $r + 1$.

## Proof

The proof is the term `GlobalTheory.JR.UnitStep.unitMatch_succ`. Its type is the statement, so Lean accepts it at once.

## In the Lean code

The theorem is in [JacquetRallisUnitMatchSuccStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/JacquetRallisUnitMatchSuccStatement.lean#L6). The proof is the tactic `first | exact @GlobalTheory.JR.UnitStep.unitMatch_succ | ...`, and the first branch closes the goal. Its one use is in `unitMatch_of_weilField`, which supplies the three hypotheses from $\mathrm{WeilField}$ and from `weilConstantStandardHermitian_eq_one`.
