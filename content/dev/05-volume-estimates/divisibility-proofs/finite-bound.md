---
id: finite-bound
title: The prime remainder over a finite set of primes
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Top.TestRest.finite_bound
module: Development.AutomorphicSpectrum.Proofs.DivisibilityProofs.TestPolynomialRemainderBound
covers: 773
status: drafted
drafted_by: writer@claude
---
This theorem bounds the prime remainder of the test polynomial over each finite set of large primes. It translates the problem into the setting of the remainder terms of the heights chapter and applies [`RestBound.full`](/entry/rest-bound-full/) there. Its user is [`testRest_bound`](/entry/test-rest-bound/), which passes to the infinite sum.

## Statement

Let $\Psi$ be a nonempty finite set, $j, k \ge 1$ and $N = j + k$. Let $B_0 \ge 4|\Psi| N^2$, let $\mathrm{frob}$ be a Frobenius map, and let $F_T = \sum_{\tau} \sum_{m=1}^{N} p_{\tau,m} Q_{\tau,m}$ with $Q_{\tau,m}$ homogeneous of degree $\dim \mathrm{Fl} + 1 - m$.

**Theorem.** For each finite set $P$ of primes $p > B_0$,

$$\Bigl| \sum_{p \in P} \sum_{\tau} \sum_{m=1}^{N} r_p(\tau, m, Q_{\tau,m}) \Bigr| \le 1.6\, (D + 1)\, \delta.$$

The terms $r_p$ are defined in [the entry for `testRest_bound`](/entry/test-rest-bound/), and $F_T$, $D$, $\delta$ in [the lower bound for the coefficient at the base](/entry/test-height-bound-slope-flat/).

## Proof

Fix a bijection $e \colon \Psi \to \{1, \dots, f\}$, $f = |\Psi|$, and rename the variables $x_{\tau,i} \mapsto x_{e(\tau),i}$ (`rl`). Let $I = \deg_{\mathrm{Fl}} \circ\, e^{-1}$ (`flagI`).

1. $I$ is a flag integral (`isFlag`): it kills $p_{\tau,m} G$ for $m \ge 1$ (`flag_degree_power_sum_mul_zero`), and it is nonzero on the staircase monomial, where it is $\pm 1$ (`degFl_permExp`).
2. The class $\mu$ goes to the class `muClass` of the smaller block (`mu_eq`). The product $\mathrm{fib}$ goes to $\pm$ `fibClass`, since each block factor is a Vandermonde product up to sign (`fib_sg`, `vandermonde_sg`). So $F_T$ goes to $\varepsilon \cdot$ `restPoly` and $\mu^D \mathrm{fib}$ to $\varepsilon \cdot$ `degPoly`, with $\varepsilon = \pm 1$, and $\varepsilon\, e(Q)$ is a power sum decomposition of `restPoly`.
3. The Frobenius labels go to pairs in $\{1, \dots, f\} \times \{\pm\}$ (`conv`, `lie_eq`). Then the term `restAt` of the heights chapter at $p$, with volume $1$, is $\varepsilon \sum_\tau \sum_m r_p(\tau, m, Q_{\tau,m})$. The term $m = 1$ is $0$ on both sides.
4. `RestBound.full`, through `RestBound.imp`, gives $\bigl|\sum_{p \in P} \mathrm{restAt}_p\bigr| \le 1.6\,(D+1)\,|I(\varepsilon\,\mu^D \mathrm{fib})| = 1.6\,(D+1)\,\delta$, as $\delta > 0$ (`test_polynomial_shift_total`).

The rest is bookkeeping with $|\varepsilon| = 1$.

## In the Lean code

The theorem is in [TestPolynomialRemainderBound.lean](lean:Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/TestPolynomialRemainderBound.lean#L300). The target setting (`IsFlagIntegral`, `restPoly`, `degPoly`, `restAt` and the statement `RestBound.Statement`) is in [IsFlagIntegralOne.lean](lean:GroundTheory/HeightsAndTheta/Heights/RemainderTerms/IsFlagIntegralOne.lean#L142). The bridge `RestBound.imp` is in [RestAt.lean](lean:GroundTheory/HeightsAndTheta/Heights/RemainderTerms/RestAt.lean#L120); it turns a second form of the statement, in `RemainderTerms/Statements.lean`, into this one. We have not unfolded its proof or the proof of `RestBound.full`. The theorem is stated with $N$ written as $j + k$, so its user must rewrite $N$. The bound is uniform in $P$, in $\mathrm{frob}$ and in the decomposition $Q$. The set of bad primes plays no role here.
