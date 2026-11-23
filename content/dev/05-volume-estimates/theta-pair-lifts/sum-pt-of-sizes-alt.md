---
id: sum-pt-of-sizes-alt
title: The oscillation bound at all points from the bound at one point
kind: theorem
decl: GlobalTheory.RefSum.sumPt_of_sizes_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.SumPtOfSizes
covers: 703
status: drafted
drafted_by: writer@claude
---
This theorem proves the oscillation bound `SumPtAlt` from the weight bounds `WtPtAlt` and the number bounds `NumPtAlt`. It lifts the pointwise lemma [sumAt_of_sizes](/entry/sum-at-of-sizes/) to all points. Its only user is its renaming [sum_pt_of_wt_pt_num_pt](/entry/sum-pt-of-wt-pt-num-pt/). Below this theorem are 703 declarations.

## Statement

We use the notation of [sum_pt_of_size](/entry/sum-pt-of-size/). At a point $p$ and a level $i$, let $(p_0, q_0)$ be the signature of the datum at level $i + 1$, let $r, f, k, m$ be the ranks, and let $x$, $b$, $\lambda$ be the scales `L.sc.x`, `L.sc.b`, `L.sc.L`.

`WtAt` with constant $C$ for a weight $u$ says: $p_0 + q_0 + 1 = k + m$, $q_0 \le m \le k$, $1 \le m$, $2 \le k$, $k \le p_0 + 1$, $[E : \mathbb{Q}] = 2f$, and there are $B \in \mathbb{N}$ and $\Sigma$ such that each $u_\tau$ is decreasing, $u_\tau(k - 2) = 0$, $u_\tau(p_0 - 1) - u_\tau(p_0) \ge n + 1$ with $n$ = `nCol`, $|u_\tau(j)| \le B$, $\sum_{j < k - 2} u_\tau(j) \le \Sigma$, and

$$1 \le L, \qquad L(B + 1) \le C b, \qquad L \Sigma \le C b.$$

`NumAt` with constant $C$ says: $1 \le \lambda$, $1 \le b$, $1 \le \log\log x$, $\log b$, $\log r$ and the number `vd2` are at most $C\lambda$, $\log\log k \le C \log\log x$, $f m b \lambda \log\log x \le C\,\mathrm{unitE}$, $L r^3 \le C b$, and $r \log t/(t - 1) \le C m \lambda$ for the two numbers $t$ = `host.q` and $t$ = `host.d`.

`WtPtAlt` is $\mathrm{Lifts}$ of: if $i + 1 < m$, `WtAt` holds for each $u$ with `Quo`. `NumPtAlt` is $\mathrm{Lifts}$ of: if $i + 1 < m$, `NumAt` holds.

**Theorem.** `WtPtAlt` and `NumPtAlt` imply `SumPtAlt`. If they hold with constants $C_1$ and $C_2$, then `SumPtAlt` holds with

$$C = 40\bigl(4 C_1 K^2 + C_2 K + 2 C_1\bigr) C_2, \qquad K = 2C_1 + C_2 + 1.$$

## Proof

The proof combines the two statements with `Closed.and` and `Closed.imp` (see [Closed](/step/closed-def/)), and takes the larger of the two thresholds in $x$. Above it, at each point $p$ with `RowsTAlt`, each level $i$ with $i + 1 < m$ and each $u$ with `Quo`, [sumAt_of_sizes](/entry/sum-at-of-sizes/) turns `WtAt` with $C_1$ and `NumAt` with $C_2$ into `SumAt` with the constant $C$ above.

The work is in `sumAt_of_sizes`. It takes $S$ to be the primes up to $2B + 1$, with explicit exponents $e_q$ (`eOf`), and proves `OscLe` with bound $e_q$ by [depthOscillation_le_bound_every_prime](/entry/depth-oscillation-le-bound-every-prime/).

## In the Lean code

The theorem is at [SumPtOfSizes.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SumPtOfSizes.lean#L20). `WtAt` and `NumAt` are at [ESmall.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ESmall.lean#L58).

- The proof term is the same, character for character, as that of `sumPt_of_sizes : WtPt → NumPt → SumPt` in [SumPointOfWeightNumerical.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SumPointOfWeightNumerical.lean#L101). There the statements are built with `Lifts`, here with `LiftsCondition`. We have not compared the two.
- `WtPtAlt` holds outright, by `wtPt_of_wtN_alt lift_weight_numerator`, and `NumPtAlt` by `numPt_alt` (see [sumPt_of_size_alt](/entry/sum-pt-of-size-alt/)).
