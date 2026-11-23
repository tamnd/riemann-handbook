---
id: jacquet-rallis-unit-match-of-weil-rep-quadratic
title: Unit matching from the quadratic Weil representation (statement file)
kind: theorem
decl: GlobalTheory.T.jacquetRallisUnitMatch_of_weilRep_quadratic
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.JacquetRallisUnitMatchOfWeilRepQuadraticStatement
covers: 1043
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [unit matching in every rank from the quadratic Weil representation](/entry/unit-match-of-weil-field/). That entry has the content. This one passes the result to [unit matching in all ranks](/entry/unit-match-all/), which supplies the hypothesis. Below it are 1,043 declarations of the proof.

## Statement

If $\mathrm{WeilField}$ holds, then $\mathrm{UnitMatch}(r)$ holds for every $r \geq 0$.

$\mathrm{UnitMatch}(r)$ is the Jacquet-Rallis fundamental lemma for unit functions on $\mathfrak{gl}_{r+1}(F)$ under $\mathrm{GL}_r(F)$ and on the Hermitian $(r+1) \times (r+1)$ matrices under $U_r$, for an unramified quadratic extension $E/F$ of $p$-adic fields. $\mathrm{WeilField}$ is the existence of the [Weil representation](/learn/theta/#the-weil-representation) of $\mathrm{SL}_2(K)$ on test functions on $L = K \otimes_F E$, when $K$ and $L$ are fields. Both are stated in full in [the entry with the proof](/entry/unit-match-of-weil-field/).

## Proof

The proof is `unitMatch_of_weilField`. Its type is the statement, so Lean accepts it at once. There is nothing more.

## In the Lean code

The theorem is at [JacquetRallisUnitMatchOfWeilRepQuadraticStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/JacquetRallisUnitMatchOfWeilRepQuadraticStatement.lean#L6). The proof is the tactic `first | exact @GlobalTheory.JR.unitMatch_of_weilField | ...`. The first branch closes the goal, since the two types are the same. The file is one of the many statement files of the Lean code that give a theorem a name in the namespace `GlobalTheory.T`. The name says "Weil representation, quadratic", and the hypothesis `WeilField` is the Weil representation for a quadratic extension $L/K$ of fields, so the name and the statement agree.
