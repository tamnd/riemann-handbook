---
id: closing-true-cols
title: Sharp column bounds for true columns, folded form
kind: theorem
decl: GlobalTheory.LvT.Built.TrueCols.closing_true_cols
module: Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.ClosingTrueCols
covers: 2424
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It is [sharp row bounds for true columns, the statement form](/entry/true-columns-row-sharp-bounds/) with the predicate `TwistedColumnBoundAtT` folded back. The real content is in [sharp column bounds for the datum of a true column choice](/entry/row-true/). Its only user is [column valuations at bundle points from true columns](/entry/row-level-valuations/).

## Statement

Let $B$ be a base, $X$ a `PreX` over it and $I$ a true column choice (`TC B X`) with `I.Ok`, the jet condition `ColIn.JetsIn I` and `BaseSigns B`. Let $l$ be laws for $I$, $Z$ later stages, $l_0$ a law at level $0$, $Y$ a division datum `DivX` of $D = $ `I.rec7 l Z` and $u$ a word of $D$. Then

- `Conclusion5Sharp D u`, and
- `TwistedColumnBoundAtT Y (I.tw l l0 Z) u`.

[Sharp column bounds for the datum of a true column choice](/entry/row-true/) defines these objects and predicates.

## Proof

The proof is one line: `exact GlobalTheory.T.trueColumns_row_sharp_bounds B X I hOk hJ hS l l0 Z Y u`. The conclusion of that theorem is the unfolded form of `TwistedColumnBoundAtT`: the definition of `TwistedColumnBoundAtT Dx T u` in [AdmissibleAtGeneratorPlaces.lean](lean:Formalism/LocalToGlobal/GroupLattices/AdmissibleAtGeneratorPlaces.lean#L20) is word for word the second conjunct there. So Lean accepts it with no rewriting.

## In the Lean code

The theorem is in [ClosingTrueCols.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/ClosingTrueCols.lean#L12). Two differences from the theorem it calls are only of form. The arguments $l_0$ and $Z$ come in the other order. The jet condition is written `ColIn.JetsIn I` instead of `I.JetsIn`; these are the same, since `TC B X` is an abbreviation of `ColIn B X`.
