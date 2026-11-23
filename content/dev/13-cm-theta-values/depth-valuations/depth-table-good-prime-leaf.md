---
id: depth-table-good-prime-leaf
title: The depth bound at good places of a leaf (statement form)
kind: theorem
decl: GlobalTheory.T.depthTable_goodPrimeLeaf
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.DepthTableGoodPrimeLeafStatement
covers: 869
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It states `LeafGoodSt` and proves it by [`leafGood`](/entry/leaf-good/), which has the real content. Its one user is [`leafGood_run`](/entry/leaf-good-run/), which applies it with $C_1 = 100$ and gets the bound `LeafDepthGood` at the good places of a leaf object.

## Statement

**Theorem.** `LeafGoodSt` holds.

`LeafGoodSt` says: for each $C_1 \ge 0$ there is $C_0$ such that, for a leaf object $O$ whose exponents and elements come from depth data $D$ over a CM field $E$, with $C_0 \le C$ and the package statements `PkgSt` for each moduli space $X_{\iota(j)}$, the bound `LeafDepthGood N O` holds. [The entry for `leafGood`](/entry/leaf-good/) gives all the hypotheses, and [the entry for `leafDepth_all_run`](/entry/leaf-depth-all-run/) states `LeafDepthGood` in full.

## Proof

The statement is that of `GlobalTheory.GoodDepth.leafGood`, and the proof applies it.

## In the Lean code

The theorem is in [DepthTableGoodPrimeLeafStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/DepthTableGoodPrimeLeafStatement.lean#L6). The proof is `first | exact @GlobalTheory.GoodDepth.leafGood | ...`, a tactic that tries the alias in three forms, under `set_option maxHeartbeats 1000000`. The statement `LeafGoodSt` is in [DepthNumbersThresholdEq.lean](lean:Development/AbelianVarietyTheory/Definitions/Jets/DepthNumbersThresholdEq.lean#L198). The words "depth table" in the name do not match a defined object: the conclusion is the single predicate `LeafDepthGood`.
