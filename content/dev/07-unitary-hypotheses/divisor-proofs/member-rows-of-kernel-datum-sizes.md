---
id: member-rows-of-kernel-datum-sizes
title: The body of the column rows for tied kernel entries, the statement form
kind: theorem
decl: GlobalTheory.T.memberRows_of_kernelDatum_sizes
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.MemberRowsOfKernelDatumSizesStatement
covers: 1055
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It states the result of [the body of the column rows for tied kernel entries](/entry/rows-body-of-ker-ties/) and proves it by calling that theorem. That theorem is itself a specialization; the real content is in [the body of the column rows at one member](/entry/rows-body-col-face/). Its only user is [the rows from the column pins](/entry/rows-u-of-col-pins-alt/), which takes the constant $C_0$ from it.

## Statement

For all reals $C_Y$ and $C_T \ge 0$ there is $C_0$ with this property. Let $t$ be a record of kernel entries tied to a datum $D$, with $t.X.K$ totally complex. Take column data at each tuple, pulled back from $D$, a word $u$ and the record of numbers $R$ built from the datum at the letter of $u$. If the ties `KerTies` and the size bounds `KerSizes` hold, $C_0 \le C_h$, the matrix at the base tuple is positive definite at each infinite place and the evaluation bound holds, then `RowsBody` holds at $u$ and the frames of `MramH` have unit determinant.

[The body of the column rows for tied kernel entries](/entry/rows-body-of-ker-ties/) gives the full statement and defines each object.

## Proof

The proof is `first | exact @GlobalTheory.ColRows.rowsBody_of_kerTies | ...`. It applies that theorem. The two statements are the same, word for word.

## In the Lean code

The theorem is in [MemberRowsOfKernelDatumSizesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/MemberRowsOfKernelDatumSizesStatement.lean#L8). The proof it calls is in [MemberRowsOfKernelDatumSizes.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/MemberRowsOfKernelDatumSizes.lean#L10). The name speaks of "member rows" and "kernel datum sizes"; the statement is about the rows at one word $u$ and the size bounds `KerSizes`.
