---
id: covering-low-defect-alt
title: The low defect bound at the last level
kind: theorem
decl: GlobalTheory.CovTop.DefLow.covering_low_defect_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.CoveringLowDefectBound
covers: 896
status: drafted
drafted_by: writer@claude
---
This theorem proves `LowDefectCondition`: at the last level of the tower, the core slope is bounded below by minus the main term, up to a multiple of the error unit. Its only user is its renaming [lowDef_of_gram_of_anchor](/entry/low-def-of-gram-of-anchor/), which [the covolume bound](/entry/top-covol-g-alt-alt/) uses for the lower bound at the top level $i + 1 = m$. Below this theorem are 896 declarations.

## Statement

We use the level statements of [the covolume bound](/entry/top-covol-g-alt-alt/). For a point $p$ and a level $i$ let $\mu_{\mathrm{core}}(p, i)$ be the slope of the type lattice for the norm `nrmK` (`muCore`), $T_i$ the main term (`mainT`), $u$ the error unit (`unitE`), $\log\Omega$ the log period of the record of $p$, and $(p_i, q_i)$ the signature of the datum at level $i + 1$. For $\tau \in \Psi$ let $a_\tau$ be the integer `anchor` of the weight.

- `GramCondition` is the level statement of `GramAt`: the norm has a Gram matrix, the full lattice is finitely generated, the good lattice is not zero, and the weight $G_k$ satisfies `GoodW`.
- `AnchorCondition` is the level statement of `AnchorAt` with constant $C$. Its first part is $\bigl|T_i - \sum_{\tau} (p_i - q_i)\, a_\tau \log\Omega\bigr| \le C u$.

**Theorem.** If `PublishedHodgeBundleTheorems`, `GramCondition` and `AnchorCondition` hold, then there is a constant $C \ge 0$ such that, at each large point and each level $i$ with $i + 1 = m$,
$$-T_i - C u \le \mu_{\mathrm{core}}(p, i).$$

## Proof

At the last level, $(p_i, q_i)$ is `sigW` at $m$, that is $(k + m - 1, 0)$, and $m + 3 \le k$. So $q_i = 0$ and $p_i \ge 1$. The bound is a chain of four inequalities.

1. [two_mul_defBound_sub_le_muCore_of_gramAt](/entry/two-mul-def-bound-sub-le-mu-core-of-gram-at/), with `GramAt`, gives $2\,\mathrm{defBound}(-\mathrm{flatDegVal}) - C_0 u \le \mu_{\mathrm{core}}$.
2. `two_definiteBound_ge_anchoredMainTerm_sub_crude_errors` (for $q = 0$, $p \ge 1$, $n$ even) gives a lower bound of $2\,\mathrm{defBound}(-\mathrm{flatDegVal})$ by $-\sum_\tau p_i a_\tau \log\Omega$ minus three error terms: $|\log\Omega|$ times the distance of the weight from the anchors, a sum of $\log \dim$, and a term in $|\mathrm{lrd}(E)|$.
3. `weight_dimension_log_bound'` bounds the sum of the three error terms by $C_3 u$.
4. `AnchorAt` with $q_i = 0$ gives $-\sum_\tau p_i a_\tau \log\Omega \ge -T_i - C_A u$.

With $C = C_A + C_3 + C_0$, `linarith` closes the proof. The rest is bookkeeping.

## In the Lean code

The theorem is at [CoveringLowDefectBound.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CoveringLowDefectBound.lean#L17). Step 2 is a renaming of `GlobalTheory.DefArith.two_defBound_ge`, and step 3 of `parameters_scale_rank_gap_bounds`. `wtN_z` (`WtNum`) gives the signature. Only the first clause of `AnchorAt` is used.

The hypothesis `PublishedHodgeBundleTheorems` is passed to step 1 only, and the chain below step 1 never reads it (see [defect_bound_of_connected_alt](/entry/defect-bound-of-connected-alt/)). We have not unfolded `nrmK`, `anchor`, `laOf`, `lrd` or `GoodW`. The real content is in step 1.
