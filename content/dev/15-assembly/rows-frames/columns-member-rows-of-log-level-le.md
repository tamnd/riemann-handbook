---
id: columns-member-rows-of-log-level-le
title: The body of the column rows, the statement form
kind: theorem
decl: GlobalTheory.T.columnsMemberRows_of_logLevel_le
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ColumnsMemberRowsOfLogLevelLeStatement
covers: 1041
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It states the result of [the body of the column rows at one member](/entry/rows-body-col-face/) and proves it by calling that theorem. The real content is in that entry. Its only user is [the body of the column rows for tied kernel entries](/entry/rows-body-of-ker-ties/).

## Statement

For all reals $C_Y$ and $C_T \ge 0$ there is $C_0$ with this property. Take a field record $X$ with $X.K$ totally complex, a definite side, column data at each tuple, a member $x$ with word $u$ and level prime $T$, and a record of numbers $R$. Assume the ties, the conditions at the base tuple, the size conditions, $\log T \le C_T\, m\, L$, that $R$ reads the numbers of the datum, $C_0 \le R.C_h$, positive definiteness at the base tuple and the bound for the evaluation map. Then `RowsBody` holds for the column face at $x$, and the frame matrices of the lattice `MramH` at $u$ have unit determinant at each infinite place.

[The body of the column rows at one member](/entry/rows-body-col-face/) gives the full statement and defines each object.

## Proof

The proof is `first | exact @GlobalTheory.ColRowsTopS.rowsBody_colFace | ...`. It applies that theorem. The two statements are the same, word for word.

## In the Lean code

The theorem is in [ColumnsMemberRowsOfLogLevelLeStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ColumnsMemberRowsOfLogLevelLeStatement.lean#L11). The proof it calls is in [ColumnsMemberRowsOfLogLevelLe.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ColumnsMemberRowsOfLogLevelLe.lean#L25). The name speaks of the bound on the logarithm of the level prime, which is one of the fourteen hypotheses that follow the data.
