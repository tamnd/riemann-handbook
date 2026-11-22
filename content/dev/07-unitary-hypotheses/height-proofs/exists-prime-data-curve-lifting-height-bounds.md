---
id: exists-prime-data-curve-lifting-height-bounds
title: Local point data with the height bounds (statement form)
kind: theorem
decl: GlobalTheory.T.exists_primeData_curve_lifting_heightBounds
module: Development.AbelianVarietyTheory.Proofs.HeightProofs.ExistsPrimeDataCurveLiftingHeightBoundsStatement
covers: 1386
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`exists_primeData_heights`](/entry/exists-prime-data-heights/), which states the result in full. Its one user is [`inputsNet_recPlus`](/entry/inputs-net-rec-plus/), where it gives the local point data and the `Heights` bound of the part `PtIn` of the index bound inputs.

## Statement

Let $X_j$ be the algebra of forms of a record $T$ at index $j$, and let $G$ be a family of forms on $X_j$ (`GlobalFamilyData`). Suppose `FnAlgClosed`, `PageOK`, the run hypotheses `HypC`, $C_L > 0$, the lower bounds `LAMwAt` with constant $C_L$ at all weights, and the five conditions on $G$: `GenOK`, `EtaOK` when $j < m$, `TiedTh`, `InBasis` at each prime, and $\log \delta \le 1041 Z_b^3$. Suppose also `CombBound`.

**Theorem.** Then there is, at each prime $\lambda$, a local point datum for $G$ moved to the algebra $X_j^+$ with all valued points (`gd2Xplus G extAll`). These data meet `InCurve`, `InTie` and `InLiftC`, and the bound `Heights` holds with the constants `gcR`, `phR`, `prwR` and `PPv 200000 2`.

[The entry for `exists_primeData_heights`](/entry/exists-prime-data-heights/) writes out `Heights`.

## Proof

The statement is the same as that of `GlobalTheory.RunPrimeData.exists_primeData_heights`, and the proof applies it.

## In the Lean code

The theorem is in [ExistsPrimeDataCurveLiftingHeightBoundsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/HeightProofs/ExistsPrimeDataCurveLiftingHeightBoundsStatement.lean#L22). The proof is `first | exact @GlobalTheory.RunPrimeData.exists_primeData_heights | ...`, a tactic that tries the alias in three forms. The file imports about twenty modules, but the proof uses only the one theorem. The name says "prime data": in the Lean code this is the structure `LocalPointData`, one datum for each prime $\lambda$.
