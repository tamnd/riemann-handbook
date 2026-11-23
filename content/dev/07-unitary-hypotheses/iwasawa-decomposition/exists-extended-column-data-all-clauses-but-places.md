---
id: exists-extended-column-data-all-clauses-but-places
title: An extension with all clauses but the places (second name)
kind: theorem
decl: GlobalTheory.T.exists_extendedColumnData_all_clauses_but_places
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ExistsExtendedColumnDataAllClausesButPlacesStatement
covers: 362
status: drafted
drafted_by: writer@claude
---
This theorem is a second name of [`exists_ext_build`](/entry/exists-ext-build/). It has the same statement and no proof of its own. It is step 1 of [`datExt0_of_hypotheses`](/entry/dat-ext0-of-hypotheses/), its only caller in the spine.

## Statement

The hypotheses are those of `DatExt0`, as stated in the [entry of `datExt0_of_hypotheses`](/entry/dat-ext0-of-hypotheses/): the seven named hypotheses, a pinned column datum $w'$ over $B'$, a pinned $w$ over $B$ with `Enl0 B B'`, a fine adelic datum $z$ at a later stage of $w$, and a later stage $Z'$ of $w'$. The conclusion is weaker than in `DatExt0`. There is a fine adelic datum $z'$ at $Z'$ with `ExtN z z'` in place of `Ext z z'`.

`Ext` is `ExtN` together with one more clause, `W1`, on the marked places. So the name is exact: the extension meets all clauses of `Ext` but the one on places. That clause is proved apart, by `extendedData_nonzero_index_places_correspond_alt`.

## Proof

The proof is the tactic `first | exact @exists_ext_build | ...` (namespace shortened), which tries three ways to apply `exists_ext_build`.

## In the Lean code

The theorem is in [ExistsExtendedColumnDataAllClausesButPlacesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsExtendedColumnDataAllClausesButPlacesStatement.lean#L22). The statement is written out in full, not as a named proposition. It repeats the statement of `exists_ext_build` word for word. The name says "column data", but the object built is an adelic datum `Dat`, not a column datum `ColW`.
