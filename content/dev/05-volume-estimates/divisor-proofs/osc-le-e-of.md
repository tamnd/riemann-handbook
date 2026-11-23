---
id: osc-le-e-of
title: The depth oscillation bound at every prime
kind: theorem
decl: GlobalTheory.RefSum.oscLe_eOf
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.DepthOscillationLeBoundEveryPrime
covers: 662
status: drafted
drafted_by: writer@claude
---
This theorem bounds the oscillation of the depth $\nu_p$ at every prime $p$ by an explicit number $e(p)$. It sorts the primes into five classes, with one lemma for each. Its only user is its renaming [depthOscillation_le_bound_every_prime](/entry/depth-oscillation-le-bound-every-prime/), which [sumAt_of_sizes](/entry/sum-at-of-sizes/) uses to build the prime sum of `SumAt`. Below this theorem are 662 declarations.

## Statement

Let $E$ be a CM field with a host $H$, which includes a prime $d \equiv 7 \bmod 16$ with $\sqrt{-d} \in \mathcal{O}_E$. Let $\mathrm{Dw}$ be a hermitian datum of signature $(s, t)$, $N = s + t$, with a moduli space at a level. Let $c_x$ give a natural number to each factor $f$ (`Lt1 Dw`).

`OscLe` at $p$ with bound $b$ is as in [sum_pt_of_size](/entry/sum-pt-of-size/): above each point of the flag model at $p$ there is $A \in \mathbb{N}$ with $A \le \nu_p(y, c_x) \le A + b$ at the integral points $y$ (the upper bound for algebraic $y$). Here $\nu_p(y, c_x) = \sum_f \nu_f(y, c_x(f))$ (`nuP`) is a sum of factor depths.

**Theorem.** Suppose that:

1. (`Shape`) $s + t + 1 = k + m$, $t \le m \le k$, $m \ge 1$, $k \ge 2$ and $[E : \mathbb{Q}] = 2F$;
2. (`ExpBd`) $M_b \ge 0$; at each embedding $\tau$ the sum of $c_x(f)$ over the big factors is at most $M_b$; `sumSmallSpread` is at most $S_m$; and $c_x \le M$;
3. $v_d(q) \ge 0$ for all $q$, and `SplitPlaces` $q$ $H$ $F$ $v_d(q)$ holds for each prime $q \in S$;
4. $2 \in S$, $d \in R$, and no prime outside $S \cup R$ divides the discriminant of $E$.

Then `OscLe` holds at every prime $p$ with bound $e(p)$ (`eOf`), where

$$e(p) = \begin{cases} 0 & p > M, \\ F m (1 + v_d(p)/2) M_b + S_m & p \in S, \\ (F N M_b + S_m)/(p - 1) & p \in R, \\ e_{\mathrm{small}}(p) + 1 & mp < k, \\ (6 F m M_b + S_m)/(p - 1) + 1 & \text{otherwise}, \end{cases}$$

the first true line applying, and $e_{\mathrm{small}}(p) = \bigl(F m M_b (4 + \tfrac12 \log_p M) + S_m\bigr)/(p-1) + F(m+1) N^2 (\log_p M + 1)$.

We have not unfolded `SplitPlaces` in full. It asks for places $w_i$ above $q$, matched to the CM type, with $\sum n_i = F$ and $\sum n_i v_i = F v_d(q)$ for numbers $n_i$ and depths $v_i$.

## Proof

The proof takes the five lines of $e(p)$ in turn.

1. $p > M$: the first half of `depthOscillation_zero_above_and_degreeBound`.
2. $p \in S$: `depth_oscillation_le_at_two_cmField`, with `SplitPlaces` at $p$.
3. $p \in R$: the second half of the lemma of line 1, a bound valid at every prime.
4. Lines 4 and 5: $p \notin S \cup R$, so $p \ne 2$, $p \ne d$ and $p \nmid \operatorname{disc} E$. If $-d$ is a square mod $p$, then $p$ splits in $\mathbb{Q}(\sqrt{-d})$ and `depth_oscillation_le_odd_split_unramified_prime` gives $(F m M_b + S_m)/(p-1)$. `OscLe.mono` raises it to either line. If $-d$ is not a square, $p$ is inert: `depthOscillation_le_at_small_odd_inertPrime` gives line 4, and `depthOscillation_large_inertPrime` gives line 5 from $k \le mp$.

## In the Lean code

The theorem is at [DepthOscillationLeBoundEveryPrime.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/DepthOscillationLeBoundEveryPrime.lean#L17). `eOf` and `eSmall` are at [ESmall.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ESmall.lean#L41), `OscLe` and `OscLe.mono` at [EightDvdNCol.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/EightDvdNCol.lean#L33).

- The five lemmas are renamings; we have not opened the lemmas behind them.
- `depth_oscillation_le_at_two_cmField` has no hypothesis $p = 2$. The proof uses it at every $p \in S$.
- The inert lemma of line 4 does not need $mp < k$. The split by $mp < k$ only picks the better bound.
