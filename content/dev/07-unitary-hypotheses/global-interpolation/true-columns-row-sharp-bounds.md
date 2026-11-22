---
id: true-columns-row-sharp-bounds
title: Sharp row bounds for true columns, the statement form
kind: theorem
decl: GlobalTheory.T.trueColumns_row_sharp_bounds
module: Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.TrueColumnsRowSharpBoundsStatement
covers: 2423
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It states the result of [sharp column bounds for the datum of a true column choice](/entry/row-true/) and proves it by calling that theorem. The real content is in that entry. Its only user is [sharp column bounds for true columns, folded form](/entry/closing-true-cols/).

## Statement

Let $B$ be a base, $X$ a `PreX` over it and $I$ a true column choice with `I.Ok`, `I.JetsIn` and `BaseSigns B`. Let $l$, $l_0$, $Z$ be laws, a law at level $0$ and later stages, let $D$ be the assembled datum `I.rec7 l Z`, let `Dx` be a division datum of $D$ and let $u$ be a word. Then `Conclusion5Sharp D u` holds, and for each place $w$ over $T_u$, each tuple $\mu$ with three side conditions and each $x$ in the lattice $N_\lambda(w)$, the twisted column bound `ColGeTw` holds with exponent $-m\,E_T(w)$.

[Sharp column bounds for the datum of a true column choice](/entry/row-true/) gives the full statement and defines each object.

## Proof

The proof is `first | exact @GlobalTheory.LvT.Built.TrueCols.row_true | ...`. It applies that theorem. The two statements are the same, word for word.

## In the Lean code

The theorem is in [TrueColumnsRowSharpBoundsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/TrueColumnsRowSharpBoundsStatement.lean#L8). The proof it calls is in [TrueColumnsRowSharpBounds.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/TrueColumnsRowSharpBounds.lean#L36).
