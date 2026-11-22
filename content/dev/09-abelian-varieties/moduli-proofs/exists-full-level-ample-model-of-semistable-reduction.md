---
id: exists-full-level-ample-model-of-semistable-reduction
title: A projective model with ample frames, from semistable reduction (statement form)
kind: theorem
decl: GlobalTheory.T.exists_fullLevelAmpleModel_of_semistableReduction
module: Development.AbelianVarietyTheory.Proofs.ModuliProofs.ExistsFullLevelAmpleModelOfSemistableReductionStatement
covers: 1072
status: drafted
drafted_by: writer@claude
---
This theorem is the statement form of [`topAmpExists_of_semistableReduction`](/entry/top-amp-exists-of-semistable-reduction/), with the same type. It feeds `modelsSt_of_semistableReduction`, which builds the local model systems of [Part I](/entry/part-i-of-semistable-reduction/). Its dominator in the proof is the step [EveryCharacter from the literature and VWin](/step/every-character-of-literature/).

## Statement

**Theorem.** The semistable reduction theorem `SemistableReductionSt` implies `TopAmpExists`.

`TopAmpExists` says: for each CM field $E$ with its datum $H$, each PEL datum $D$ of signature $(p, q)$ with $p + q \ge 1$, each family $X_l$ of moduli spaces and each auxiliary prime $n$, there are $J \ge 1$, $k$ and a projective model of level $n^J$ over $\mathbb{Z}[\tfrac{1 + \sqrt{-d}}{2}, \tfrac1n, \zeta_{n^J}]$ that carries ample frames of level $(n^k)^2$. The entry [`topAmpExists`](/entry/top-amp-exists/) states it in full.

## Proof

The proof is the tactic `first | exact @GlobalTheory.topAmpExists_of_semistableReduction | ...`. The first branch succeeds, so the theorem is `topAmpExists_of_semistableReduction` under a second name.

## In the Lean code

The theorem is in [ExistsFullLevelAmpleModelOfSemistableReductionStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/ExistsFullLevelAmpleModelOfSemistableReductionStatement.lean#L14). It is a renaming, with no content of its own. The real work is in [`topAmpExists`](/entry/top-amp-exists/), three levels below.
