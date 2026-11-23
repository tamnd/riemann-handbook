---
id: low-def-of-gram-of-anchor
title: The low defect bound at the top level, renamed
kind: theorem
decl: GlobalTheory.T.lowDef_of_gram_of_anchor
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.CoveringLowDefectBound
covers: 897
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It restates [covering_low_defect_alt](/entry/covering-low-defect-alt/), in the same file, with the same statement. Its only caller is [the covolume bound](/entry/top-covol-g-alt-alt/), where it gives the lower bound for $\mu_{\mathrm{core}}$ at the top level $i + 1 = m$ in step 4. Below this theorem are 897 declarations.

## Statement

We use the level statements $\mathrm{Lifts}(Q)$ of [the covolume bound](/entry/top-covol-g-alt-alt/). At a point $p$ and a level $i$, let $\mathrm{mainT}_i$ be the main term and $\mu_{\mathrm{core}}$ the slope `muCore`.

- `GramCondition` is $\mathrm{Lifts}$ of `GramAt`: Gram norms, finite generation and a nonzero good sublattice at level $i$.
- `AnchorCondition` is $\mathrm{Lifts}$ of `AnchorAt`. Its first clause says that $\mathrm{mainT}_i$ is within $C\,\mathrm{unitE}$ of a sum $\sum_\tau (p_0 - q_0)\, w_\tau \log\Omega$ of anchor weights $w_\tau$, with $(p_0, q_0)$ the signature at level $i + 1$.
- `LowDefectCondition` is $\mathrm{Lifts}$ of: if $i + 1 = m$, then $-\mathrm{mainT}_i - C\,\mathrm{unitE} \le \mu_{\mathrm{core}}$ (`LowAt`).

**Theorem.** `PublishedHodgeBundleTheorems`, `GramCondition` and `AnchorCondition` imply `LowDefectCondition`.

## Proof

The proof is `first | exact @covering_low_defect_alt | ...`. The tactic tries `exact` with [covering_low_defect_alt](/entry/covering-low-defect-alt/) first. There is no other step. That theorem uses $q_0 = 0$ at the top level, the bound of [two_mul_defBound_sub_le_muCore_of_gramAt](/entry/two-mul-def-bound-sub-le-mu-core-of-gram-at/), and the first clause of `AnchorAt`.

## In the Lean code

The theorem is at [CoveringLowDefectBound.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CoveringLowDefectBound.lean#L53). The theorem that it restates is at line 17 of the same file.

- `covering_low_defect_alt` uses only the first of the three clauses of `AnchorAt`.
- A parallel version with older names, `covering_low_defect : PublishedHodgeBundleTheorems → Gram → Anchor → LowDef`, is in [HodgeBundleWeights/CoveringLowDefectBound.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/CoveringLowDefectBound.lean#L13), which this file imports. Its proof has the same steps.
