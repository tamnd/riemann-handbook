---
id: sum-pt-of-size
title: The oscillation bound at the core level, renamed
kind: theorem
decl: GlobalTheory.T.sum_pt_of_size
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.SumPtOfSizeStatement
covers: 733
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It restates [sumPt_of_size_alt](/entry/sum-pt-of-size-alt/) with the same statement. It is step 1 of [the reference exponent bound](/entry/refined-sum-weight-of-size-alt/), which passes its result to [reference_core_of_size_and_sum_point](/entry/reference-core-of-size-and-sum-point/). Below this theorem are 733 declarations.

## Statement

We use $\mathrm{Lifts}(Q)$ of [the covolume bound](/entry/top-covol-g-alt-alt/) and the notation of [the reference exponent bound](/entry/refined-sum-weight-of-size-alt/). Let $a_u$ (`aOf`) be the exponents of the theta weight $G_u$.

For a prime $q$ and a function $c$, `OscLe` with bound $b$ says: above each point of the flag model at $q$ there is $A \in \mathbb{N}$ such that a valuation $\nu_q(y, c)$ of integral points $y$ is at least $A$, and at most $A + b$ when $y$ is algebraic. We have not unfolded $\nu_q$ (`nuP`).

`SumPtAlt` is $\mathrm{Lifts}$ of: if $i + 1 < m$, then for each weight $u$ with `Quo` there are a finite set $S$ of primes and numbers $e_q \ge 0$, zero off $S$, and $s$ with

$$\sum_{q \in S} e_q \log q \le s, \qquad L s \le C\,\mathrm{unitE},$$

and `OscLe` with bound $e_q$ holds on the core tower at level $i + 1$ for the function `gap` of $a_u$, at each prime $q$ that is not a host prime $g_0, g_1$.

**Theorem.** `SizeCondition` implies `SumPtAlt`.

## Proof

The proof is `first | exact @sumPt_of_size_alt | ...`. There is no other step.

## In the Lean code

The theorem is at [SumPtOfSizeStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SumPtOfSizeStatement.lean#L12). `SumPtAlt` is at [RefTheta.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RefTheta.lean#L22), and `SumAt` and `OscLe` are at [EightDvdNCol.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/EightDvdNCol.lean#L76).

- `SizeCondition` is not used in the end (see [sumPt_of_size_alt](/entry/sum-pt-of-size-alt/)).
- The content is in [sumAt_of_sizes](/entry/sum-at-of-sizes/).
