---
id: odd-level-block-bound-attained
title: The odd-level block bound is attained in every window (second name)
kind: theorem
decl: GlobalTheory.T.oddLevelBlock_bound_attained
module: Development.AbelianVarietyTheory.Proofs.UnramifiedDepth.OddLevelBlockBoundAttainedStatement
covers: 578
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`oddBlock_supply`](/entry/odd-block-supply/). It has the same statement, `BiSupply ∧ RF.BiSupply`, and its proof only calls `oddBlock_supply`. The content is in that entry and in [`window_letterDet`](/entry/window-letter-det/). It is one of the three supplies that the depth bound at good places uses; see [the depth at good places](/entry/nu-good/).

## Statement

**Theorem.** `BiSupply` and `RF.BiSupply` hold.

In words: for an alternating row datum $X$ with $n \ge 1$, a flag $F$, a prime $\ell \ge 5$, a big pair $(g, a)$ and an odd $i < d$, the set of exponents $y$ for which the jet value of $\Delta^{\ell^i y} \Delta'^{y}$ has valuation at most the block bound contains $0$ and meets every interval of length $S_0(\ell, i, n)$. Here $\Delta$ and $\Delta'$ are the $n \times n$ minors on the first $n$ letters of type $a$ and of type $a + i$ that the flag lists. The precise form is in [the entry for `window_letterDet`](/entry/window-letter-det/).

## Proof

The proof is `exact @GlobalTheory.oddBlock_supply`.

## In the Lean code

The theorem is at [OddLevelBlockBoundAttainedStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/OddLevelBlockBoundAttainedStatement.lean#L8). Its three users take only the second part, `RF.BiSupply`: [GoodPlaceDepthBoundProof.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/GoodPlaceDepthBoundProof.lean#L61), [ComplexConjFrobeniusDepthContentBoundProof.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/ComplexConjFrobeniusDepthContentBoundProof.lean#L362) and [InertPrimeDepthContentBoundProof.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/InertPrimeDepthContentBoundProof.lean#L212). The first part, `BiSupply`, is never used.
