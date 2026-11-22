---
id: exists-index-bound-hypotheses-with-net-all-valued-points
title: The net inputs of the index bound at all valued points (statement form)
kind: theorem
decl: GlobalTheory.T.exists_indexBoundHypothesesWithNet_allValuedPoints
module: Development.AbelianVarietyTheory.Proofs.HeightProofs.ExistsIndexBoundHypothesesWithNetAllValuedPointsStatement
covers: 4549
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`inputsNet_recPlus`](/entry/inputs-net-rec-plus/), which has the real content. Its one user is [`runHolds_of_parOK`](/entry/run-holds-of-par-ok/), which takes from it the constants $C_L$, $C_q$, $Z_0$ and the inputs `InputsNet` of the index bound.

## Statement

Use the datum $D$, the record $T$ with `h : LawsP T`, the algebra of forms $X_j$ (`recPJ h j hj`) and the conditions `ParOK` and `PageOK` from [the entry for `runHolds_of_parOK`](/entry/run-holds-of-par-ok/). Let $X_j^+$ (`recPlus h j hj`) be $X_j$ with the points of `extAll` added: over each prime $\lambda$, all valuations in `valSet` under the trivial class condition.

**Theorem.** There are $C_L \in \mathbb{R}$ and $C_q, Z_0 \colon \mathbb{R}^2 \to \mathbb{R}$ such that the following holds for all $D$, $T$, $h$, injective `OtoLL`, `EX`, $p$, $j \in [1, m]$, size data $L$, constants $H$, $C_2$, $A_2$, $C_T$, weights $\kappa, w_L, w_F$ and integers. If `ParOK T EX p j`, `PageOK` for $X_j$ and $Z_0(H.C_A, H.C_K) \le$ `zBase L` hold, then:

1. `InputsNet` holds for $X_j^+$ with the constants `kR C_L`, $C_q(H.C_A, H.C_K)$, the scalars `scalOfP` and the function `nusR h j wL`;
2. `PageSupp` holds.

[The entry for `inputsNet_recPlus`](/entry/inputs-net-rec-plus/) says what `InputsNet` contains.

## Proof

The statement is the same as that of `GlobalTheory.InputsAtRecord.inputsNet_recPlus`, and the proof applies it.

## In the Lean code

The theorem is in [ExistsIndexBoundHypothesesWithNetAllValuedPointsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/HeightProofs/ExistsIndexBoundHypothesesWithNetAllValuedPointsStatement.lean#L8). The proof is `first | exact @GlobalTheory.InputsAtRecord.inputsNet_recPlus | ...`, a tactic that tries the alias in three forms. The words "all valued points" in the name refer to $X_j^+$, which `recPlus` builds from `extAll` in [IntAtExtExtAll.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/IntAtExtExtAll.lean#L50).
