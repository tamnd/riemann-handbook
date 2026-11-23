---
id: twisted-torsion-class-theorem-good-case
title: The local torsion bounds at good triples, a second name
kind: theorem
decl: GlobalTheory.T.twistedTorsionClassTheorem_goodCase
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.TwistedTorsionClassTheoremGoodCaseStatement
covers: 625
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the assembly of the local torsion bounds](/entry/tb-assembled/). That entry has the proof. Its only user is [theorem TB from three local inputs](/entry/aux-of-bloch-kato-tate-duality-euler-char/), which applies it in the last step.

## Statement

**Theorem.** Let $D$ be a datum (`D7`) with local data $HW$ and $F$. Assume `admitted D HW F` and `Conclusion5 D`. Then `Conclusion4 D HW F` holds.

`admitted` is a list of nine local facts. Two of them are Tate local duality and the local Euler characteristic formula. `Conclusion5` gives the Bloch-Kato facts at each local field. `Conclusion4` says that `TBat` and `TBeAt` hold at each prime and each good triple. These are stated in [the parent entry](/entry/aux-of-bloch-kato-tate-duality-euler-char/).

## Proof

The proof applies `GlobalTheory.TheoremTB.tb_assembled`, which has the same statement. Nothing else happens. That proof gets `TBat` from [the crystalline extension class bound](/entry/crystalline-extension-class-bound/), which uses `admitted` only. It gets `TBeAt` from `weight_good_reduction_at_prime`, which uses both hypotheses.

## In the Lean code

The theorem is in [TwistedTorsionClassTheoremGoodCaseStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TwistedTorsionClassTheoremGoodCaseStatement.lean#L9). The proof is a `first | exact ... | ...` combinator with three tries. Each try applies the same lemma. The file has `set_option maxHeartbeats 1000000` (line 8), which a one-line proof does not need.

The name speaks of a twisted torsion class theorem in a good case. The statement has no twist of its own. It is the pair `TBat` and `TBeAt` at all good triples.
