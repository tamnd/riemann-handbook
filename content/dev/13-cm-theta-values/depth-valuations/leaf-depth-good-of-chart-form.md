---
id: leaf-depth-good-of-chart-form
title: The depth bound at good places, given the packages at all points
kind: theorem
decl: GlobalTheory.leafDepthGood_of_chartForm
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.DepthTableGoodPrimesOfChartForm
covers: 4644
status: drafted
drafted_by: writer@claude
---
This theorem proves the bound `LeafDepthGood` at the good places of a leaf object from the chart statement `UpFSt`. It does so in one step: it removes the hypothesis "the seven package statements hold" from a lemma that has it, because [`goodPrime_packages`](/entry/good-prime-packages/) proves those statements from `UpFSt`. Its alias [`depthTable_goodPrimes_of_chartForm`](/entry/depth-table-good-primes-of-chart-form/) gives the result to [`leafDepth_all_run`](/entry/leaf-depth-all-run/).

## Statement

Use the datum $D$, the core $T$, the leaf object $O$, the numerical datum $N$ and the map $\iota \colon J \to \mathbb{N}$ from [the entry for `leafDepth_all_run`](/entry/leaf-depth-all-run/). That entry also states `LeafDepthGood N O`: nonnegativity of the weights $\theta$ and $a$, two bounds on sums $\sum_p \theta(p)\log p$ and $\sum_p a(p) \log p$, and, at each place $w$ with good residue characteristic $\ell$, the bound $e_0 \le F_0 + a_E(j,\ell) + 1$ for $\ell \le Y$ and $e_0 = 0$ for $\ell > Y$.

**Theorem.** Assume `UpFSt p` for all primes $p$. Then there is $C_0 \in \mathbb{R}$ such that, for all data with `LawsM T`, `RunTie T EX Tp hK O ι`, $C_0 \le C$, `LeafPage O`, `LeafSizes O`, $10 \le C_{nW}$, $3 \le x^{e_z/5}$, $x \ge 3$, $k b' \le b$ and $F_0$ equal to the content of $D$, the bound `LeafDepthGood N O` holds.

## Proof

The lemma `GlobalTheory.T.depthLeaf_goodPrimes_of_point_data` gives a constant $C_0$ and proves `LeafDepthGood N O` under the same hypotheses and one more: for each $j \in J$, the package statement `PkgSt` holds for the moduli scheme $X_{\iota(j)}$ of the core and its coefficient field $F$. The proof takes this $C_0$. For each $j$ it proves `PkgSt` by [`allGoodPrimeDepthDataExist_proof`](/entry/all-good-prime-depth-data-exist-proof/), applied to `UpFSt`, $X_{\iota(j)}$ and $F$. The other hypotheses pass through unchanged.

So the work is split in two. The packages at all integral points come from `UpFSt` through [`goodPrime_packages`](/entry/good-prime-packages/) (3,594 declarations). The depth bound from the packages is `depthLeaf_goodPrimes_of_point_data`, which is an alias of `GlobalTheory.GoodDepth.leafGood_run`.

## In the Lean code

The theorem is in [DepthTableGoodPrimesOfChartForm.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/DepthTableGoodPrimesOfChartForm.lean#L12). The lemmas it calls:

- `GlobalTheory.T.depthLeaf_goodPrimes_of_point_data` in [DepthLeafGoodPrimesOfPointDataStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/DepthLeafGoodPrimesOfPointDataStatement.lean#L8), proved by `leafGood_run` in [DepthLeafGoodPrimesOfPointData.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/DepthLeafGoodPrimesOfPointData.lean#L47);
- `GlobalTheory.T.allGoodPrimeDepthDataExist_proof`.

We have not unfolded the proof of `leafGood_run`. It starts from `GlobalTheory.T.depthTable_goodPrimeLeaf` with the parameter $100$.

The module name `DepthTableGoodPrimesOfChartForm` is the name of the alias, not of this theorem. The hypothesis `UpFSt` is used only to build `PkgSt`.
