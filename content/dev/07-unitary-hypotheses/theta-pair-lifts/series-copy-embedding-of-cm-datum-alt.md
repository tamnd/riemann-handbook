---
id: series-copy-embedding-of-cm-datum-alt
title: The series datum on a twisted copy, the relay in the namespace T
kind: theorem
decl: GlobalTheory.T.series_copy_embedding_of_cmDatum_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.SeriesCopyEmbeddingOfCmDatum
covers: 351
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It has the same statement as [`series_copy_embedding_alt`](/entry/series-copy-embedding-alt/), in the same file, and it proves it by calling that theorem. The real content is in that entry. Its only user is [`sb1l_alt_alt`](/entry/sb1l-alt-alt/), which turns a first level datum into a second level datum with it.

## Statement

Assume `PublishedInputsThirdLayerAlt`, `SerN` and $h_L$ in `RecTExists`. Let $w$ be a column datum with `Start`, in a context $K$ over the base, with `Forced`. Let $x$ be a stage and $l$ a first level datum over $x$. Then there is a new twist $N$ of the datum of $x$ that keeps `IsLamTieFull`, such that each twisted copy $x'$ of $x$ along $N$, with the twist of $l$ as an intermediate level datum, has `SeriesData` for each `InMt` datum with identity frames. The entry [`series_copy_embedding_alt`](/entry/series-copy-embedding-alt/) lists the conditions in full.

## Proof

The proof is the other theorem. The rest is bookkeeping.

## In the Lean code

The theorem is at [SeriesCopyEmbeddingOfCmDatum.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SeriesCopyEmbeddingOfCmDatum.lean#L65). Its statement is the text of `series_copy_embedding_alt` (line 35). The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)`.

The name speaks of an embedding and a CM datum; the statement has neither. `SerN` and `Forced` are not used by the theorem that does the work.
