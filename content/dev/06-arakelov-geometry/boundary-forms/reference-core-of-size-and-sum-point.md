---
id: reference-core-of-size-and-sum-point
title: The reference exponent bound on the core tower, renamed
kind: theorem
decl: GlobalTheory.T.reference_core_of_size_and_sum_point
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.RefCoreOfSumPtStatement
covers: 428
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It restates [refCore_of_size_sumPt](/entry/ref-core-of-size-sum-pt/) with the same statement. It is step 2 of [the reference exponent bound](/entry/refined-sum-weight-of-size-alt/): it takes the oscillation bound of [sum_pt_of_size](/entry/sum-pt-of-size/) and gives the bound on the core tower, which `refTheta_of_size_refCore` then moves to the good covers. Below this theorem are 428 declarations.

## Statement

We use the notation of [the reference exponent bound](/entry/refined-sum-weight-of-size-alt/): the reference exponent $r_q(G)$ of a weight $G$, the statement `RefAt`, and the theta weight $G_u$ (`GOf`) of a weight $u$.

`ReferenceCore` is the level statement $\mathrm{Lifts}$ of: if $i + 1 < m$, then for each weight $u$ with `Quo`, `RefAt` holds for the core tower at level $i + 1$ (the family `p.T.U (i + 1)`) and the weight $G_u$. That is, there are a finite set $S$ of primes, numbers $e_q \ge 0$ zero off $S$, and $s$ with $\sum_{q \in S} e_q \log q \le s$, $L s \le C\,\mathrm{unitE}$ and $r_q(G_u) \le e_q$ for every prime $q$.

**Theorem.** `SizeCondition` and `SumPtAlt` imply `ReferenceCore`.

## Proof

The proof is `first | exact @refCore_of_size_sumPt | ...`. The tactic tries `exact` with [refCore_of_size_sumPt](/entry/ref-core-of-size-sum-pt/) first. There is no other step.

## In the Lean code

The theorem is at [RefCoreOfSumPtStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RefCoreOfSumPtStatement.lean#L15). `ReferenceCore` is at [RefTheta.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RefTheta.lean#L23).

- The file opens about thirty namespaces for a proof that names one lemma.
- The content is in [refCore_of_size_sumPt](/entry/ref-core-of-size-sum-pt/).
