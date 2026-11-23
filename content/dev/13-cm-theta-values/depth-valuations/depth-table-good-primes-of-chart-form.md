---
id: depth-table-good-primes-of-chart-form
title: The depth bound at good places from the chart statement (statement form)
kind: theorem
decl: GlobalTheory.T.depthTable_goodPrimes_of_chartForm
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.DepthTableGoodPrimesOfChartFormStatement
covers: 4645
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`leafDepthGood_of_chartForm`](/entry/leaf-depth-good-of-chart-form/), which has the real content. Its one user is [`leafDepth_all_run`](/entry/leaf-depth-all-run/), which takes from it the constant $C_0$ and the first of its four depth bounds, the bound `LeafDepthGood` at the good places.

## Statement

Use the datum $D$, the core $T$, the leaf object $O$, the numerical datum $N$ and the map $\iota$ from [the entry for `leafDepth_all_run`](/entry/leaf-depth-all-run/).

**Theorem.** Assume `UpFSt p` for all primes $p$. Then there is $C_0 \in \mathbb{R}$ such that, for all such data with `LawsM T`, `RunTie`, $C_0 \le C$, `LeafPage O`, `LeafSizes O`, $10 \le C_{nW}$, $3 \le x^{e_z/5}$, $x \ge 3$, $k b' \le b$ and `ContentEqualsDatumContent`, the bound `LeafDepthGood N O` holds.

[The entry for `leafDepth_all_run`](/entry/leaf-depth-all-run/) states `LeafDepthGood` in full, and [the entry for `goodPrime_packages`](/entry/good-prime-packages/) states `UpFSt`.

## Proof

The statement is the same as that of `GlobalTheory.leafDepthGood_of_chartForm`, and the proof applies it.

## In the Lean code

The theorem is in [DepthTableGoodPrimesOfChartFormStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/DepthTableGoodPrimesOfChartFormStatement.lean#L9). The proof is `first | exact @GlobalTheory.leafDepthGood_of_chartForm | ...`, a tactic that tries the alias in three forms. It runs under `set_option maxHeartbeats 1000000`, which a one-line alias does not need. The words "depth table" in the name do not match a defined object: the conclusion is the single predicate `LeafDepthGood`. "Chart form" refers to the hypothesis `UpFSt`, which is in the namespace `ChartF`.
