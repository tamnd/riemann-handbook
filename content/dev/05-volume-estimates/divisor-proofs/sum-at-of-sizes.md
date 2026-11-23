---
id: sum-at-of-sizes
title: The oscillation bound at one point from the weight and number bounds
kind: theorem
decl: GlobalTheory.RefSum.sumAt_of_sizes
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.SumPointOfWeightNumerical
covers: 702
status: drafted
drafted_by: writer@claude
---
This theorem is the pointwise step of [sumPt_of_sizes_alt](/entry/sum-pt-of-sizes-alt/), which lifts it to all points. At a point $p$, a level $i$ and a weight $u$, it turns the weight bound `WtAt` and the number bound `NumAt` into the oscillation bound `SumAt`. It picks the primes up to a bound with explicit exponents. Then it checks a sum bound, which is real arithmetic, and the oscillation bound at each prime, which is [depthOscillation_le_bound_every_prime](/entry/depth-oscillation-le-bound-every-prime/).

## Statement

We use the notation of [sumPt_of_sizes_alt](/entry/sum-pt-of-sizes-alt/): $L$ = `lenT`, $r, f, k, m$ the ranks, $x, b, \lambda$ the scales, $(p_0, q_0)$ the signature. `SumAt` with constant $C$ says: there are a finite set $S$ of primes, numbers $e_q \geq 0$ with $e_q = 0$ off $S$, and $s$ with

$$\sum_{q \in S} e_q \log q \le s, \qquad L s \le C \cdot \mathrm{unitE}.$$

Also, at each prime $q$ that is not a host prime $g_k$, `OscLe` (see [sum_pt_of_size](/entry/sum-pt-of-size/)) holds with bound $e_q$ for the gap of the exponents of $u$.

**Theorem.** Let $C_1, C_2 \geq 0$. If `WtAt` holds for $u$ with $C_1$ and `NumAt` holds with $C_2$, then `SumAt` holds for $u$ with $C = 40(4C_1K^2 + C_2K + 2C_1)C_2$, where $K = 2C_1 + C_2 + 1$.

## Proof

Take $B$ and $\Sigma$ from `WtAt`. Put $M = 2B + 1$, $M_b = B + 1$ and $S_m = f(\Sigma + 2q_0B)$.

1. `thetaExponents_bigSmallFactorBounds` gives `ExpBd` for the gaps of the exponents: sums over big factors at most $M_b$, a spread sum over small factors at most $S_m$, each gap at most $M$.
2. `small_vd_sum` bounds the sum of `vdH` over the small primes of the host, puts $2$ among them, and says that the host is unramified at each other prime except `host.q` and `host.d`. `twoPlaces_host` gives `SplitPlaces` at the small primes.
3. `weightedPrimeLogSum_oscillationBound_le` takes $S$ to be the primes up to $M$ and $e_q$ given by `eOf`. It proves the first inequality with $s = 40\bigl((f m M_b + S_m) K\lambda \cdot K \log\log x + f r^3 K\lambda + M\bigr)$. It uses the bounds of `NumAt` and $\log M \le K\lambda$ from `log_top_le`.
4. `len_mul_total_le` is an inequality of real numbers. It gives $L s \le C \cdot \mathrm{unitE}$ from the bounds of `WtAt` and `NumAt`.
5. `depthOscillation_le_bound_every_prime`, with step 2, gives `OscLe` with bound $e_q$ at each prime.

## In the Lean code

The theorem is in [SumPointOfWeightNumerical.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SumPointOfWeightNumerical.lean#L55), and `eOf`, `WtAt` and `NumAt` are in [ESmall.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ESmall.lean#L46). `len_mul_total_le` and `log_top_le` are in the same file, proved by `nlinarith`. `SumAt` asks for `OscLe` only at primes that are not host primes, but the proof shows it at every prime: the hypothesis is not used (line 89). We have not opened the proofs of the lemmas in steps 1 to 3.
