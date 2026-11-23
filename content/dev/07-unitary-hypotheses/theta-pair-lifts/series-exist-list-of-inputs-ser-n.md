---
id: series-exist-list-of-inputs-ser-n
title: From a first level to a second level, the relay in the namespace T
kind: theorem
decl: GlobalTheory.T.seriesExistList_of_inputs_serN
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.SecondBoundOfPrimitive
covers: 358
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It has the same statement as [`sb1l_alt_alt`](/entry/sb1l-alt-alt/), in the same file, and it proves it by calling that theorem. The real content is in that entry. Its only user is [the stage statements from the published inputs](/entry/all-stages-of-specializations-alt/), where it gives the middle step of item 4.

## Statement

Assume `PublishedInputsThirdLayerAlt` and `SerN`. Let $h_L$ be an element of `RecTExists` and $c_{\mathrm{Dep}} \in \mathbb R$. Then `SeriesExistList' hL cDep` holds: at every stage $x$, a first intermediate level datum gives a stage $x'$ over the same datum $P$ with a second intermediate level datum, and `ListSt cDep` passes from $x$ to $x'$. The entry [`sb1l_alt_alt`](/entry/sb1l-alt-alt/) explains these words.

## Proof

The proof is the other theorem. The rest is bookkeeping.

## In the Lean code

The theorem is at [SecondBoundOfPrimitive.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SecondBoundOfPrimitive.lean#L40). Its statement is that of `sb1l_alt_alt` (line 25). The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)`, with `sb1l_alt_alt` in each branch.

No bound and no primitive object appear, in spite of the module name. The hypothesis `SerN` is passed along, but no proof below this theorem uses it (see [`series_copy_embedding_alt`](/entry/series-copy-embedding-alt/)).
