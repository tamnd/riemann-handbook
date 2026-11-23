---
id: two-mul-def-bound-sub-le-mu-core-of-gram-at
title: The defect bound below the core slope, second name
kind: theorem
decl: GlobalTheory.T.two_mul_defBound_sub_le_muCore_of_gramAt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.DefectBoundOfConnected
covers: 873
status: drafted
drafted_by: writer@claude
---
This theorem is a second name of [lifts_two_mul_defBound_sub_unitE_le_muCore](/entry/lifts-two-mul-def-bound-sub-unit-e-le-mu-core/). Its only user is [the low defect bound](/entry/covering-low-defect-alt/), where it is the first step of the chain. Below this theorem are 873 declarations.

## Statement

We use the notation of [the low defect bound](/entry/covering-low-defect-alt/). Let $\mathrm{defBound}(c_1)$ be the number `defBound` of the datum at level $i + 1$ and the weight $(a, n)$ of the point, and let $\mathrm{flatDegVal} = \tfrac{p_i - q_i}{2} \log\Omega + q_i(\log d - \mathrm{lrd}(E))$, where $d$ is the integer `H.d` of the host and $\mathrm{lrd}(E)$ is a constant of the CM field $E$ that we have not unfolded.

**Theorem.** If `PublishedHodgeBundleTheorems` holds, then the following level statement holds: there is $C \ge 0$ such that, at each large point $p$ and each level $i$ with $i + 1 = m$ and `GramAt`,
$$2\,\mathrm{defBound}(-\mathrm{flatDegVal}) - C u \le \mu_{\mathrm{core}}(p, i).$$

## Proof

The proof is `exact lifts_two_mul_defBound_sub_unitE_le_muCore`, inside a `first | ...` that tries three forms of the same call. The statement is the same, word for word.

## In the Lean code

The theorem is at [DefectBoundOfConnected.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/DefectBoundOfConnected.lean#L63), in the same file as the theorem that it renames. The name says "of gramAt" because `GramAt` is the only hypothesis at a point, apart from the last level condition. The real content is in [defect_bound_of_connected_alt](/entry/defect-bound-of-connected-alt/).
