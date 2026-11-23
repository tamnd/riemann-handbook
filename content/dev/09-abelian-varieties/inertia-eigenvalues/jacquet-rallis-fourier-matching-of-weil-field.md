---
id: jacquet-rallis-fourier-matching-of-weil-field
title: Matching survives the partial Fourier transform (named form)
kind: theorem
decl: GlobalTheory.T.jacquetRallis_fourier_matching_of_weil_field
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.JacquetRallisFourierMatchingOfWeilFieldStatement
covers: 362
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`fourierMatch_of_weilField`](/entry/fourier-match-of-weil-field/), which has the proof. It says: if the Weil representation exists for quadratic extensions of fields, then matching of test functions in the Jacquet-Rallis setting survives the partial Fourier transform, in every rank. [Unit matching from the quadratic Weil representation](/entry/unit-match-of-weil-field/) uses it once in each step of its induction on the rank, at rank $r + 1$. Below it are 362 declarations of the proof.

## Statement

If $\mathrm{WeilField}$ holds, then $\mathrm{FourierMatch}(r)$ holds for every $r \ge 0$.

$\mathrm{WeilField}$ and the spaces $\mathfrak{g}_r$, $\mathfrak{h}_r$ of matrices are as in [the entry with the induction](/entry/unit-match-of-weil-field/). $\mathrm{FourierMatch}(r)$ says: for a character $\psi$ of $F$ of conductor $\mathcal{O}_F$, if two test functions $f'$ on $\mathfrak{g}_r$ and $f$ on $\mathfrak{h}_r$ match, then their partial Fourier transforms in the vector variables match. The entry [`fourierMatch_of_weilField`](/entry/fourier-match-of-weil-field/) gives the definitions in full.

## Proof

The proof is the term `GlobalTheory.JR.fourierMatch_of_weilField`. Its type is the statement, so Lean accepts it at once.

## In the Lean code

The theorem is in [JacquetRallisFourierMatchingOfWeilFieldStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/JacquetRallisFourierMatchingOfWeilFieldStatement.lean#L6). The proof is the tactic `first | exact @GlobalTheory.JR.fourierMatch_of_weilField | ...`, and the first branch closes the goal. The file sets `maxHeartbeats` to 1000000. `FourierMatch` is in [FourierMatch.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/FourierMatch.lean#L152).
