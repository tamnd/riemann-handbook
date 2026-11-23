---
id: depth-leaf-good-primes-of-point-data
title: The depth bound at good places from the packages (statement form)
kind: theorem
decl: GlobalTheory.T.depthLeaf_goodPrimes_of_point_data
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.DepthLeafGoodPrimesOfPointDataStatement
covers: 922
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`leafGood_run`](/entry/leaf-good-run/), which has the content. Its one user is [`leafDepthGood_of_chartForm`](/entry/leaf-depth-good-of-chart-form/), which proves its package hypothesis from the chart statement `UpFSt` and so gets the bound `LeafDepthGood` from `UpFSt` alone.

## Statement

Use the datum $D$, the core $T$, the leaf object $O$, the numerical datum $N$ and the map $\iota \colon J \to \mathbb{N}$ from [the entry for `leafDepth_all_run`](/entry/leaf-depth-all-run/), which also states `LeafDepthGood`.

**Theorem.** There is $C_0 \in \mathbb{R}$ such that, for all data with `LawsM T`, `RunTie T EX Tp hK O ι`, the package statement `PkgSt` for the moduli scheme $X_{\iota(j)}$ of the core and its coefficient field for each $j \in J$, $C_0 \le C$, `LeafPage O`, `LeafSizes O`, $10 \le C_{nW}$, $3 \le x^{e_z/5}$, $x \ge 3$, $k b' \le b$ and $F_0$ equal to the content of $D$, the bound `LeafDepthGood N O` holds.

This is the statement of [`leafDepthGood_of_chartForm`](/entry/leaf-depth-good-of-chart-form/) with the hypothesis `UpFSt` replaced by `PkgSt` at each $j$. [The entry for `goodPrime_packages`](/entry/good-prime-packages/) states `PkgSt`.

## Proof

The proof is one line: `first | exact @GlobalTheory.GoodDepth.leafGood_run | ...`. The statement is the same as that of `leafGood_run`, word for word.

## In the Lean code

The theorem is in [DepthLeafGoodPrimesOfPointDataStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/DepthLeafGoodPrimesOfPointDataStatement.lean#L8). It calls `GlobalTheory.GoodDepth.leafGood_run` in [DepthLeafGoodPrimesOfPointData.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/DepthLeafGoodPrimesOfPointData.lean#L47).
