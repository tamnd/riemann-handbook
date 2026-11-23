---
id: test-rest-bound
title: The prime remainder of the test polynomial is bounded
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Top.testRest_bound
module: Development.AutomorphicSpectrum.Proofs.DivisibilityProofs.TestPolynomialRemainderBound
covers: 774
status: drafted
drafted_by: writer@claude
---
This theorem bounds the sum over primes in the tower height identity, evaluated on a decomposition of the test polynomial. It passes from the bound for finite sets of primes, [`finite_bound`](/entry/finite-bound/), to the infinite sum by a limit. Its statement form is [`test_polynomial_remainder_bound`](/entry/test-polynomial-remainder-bound/), used in [the lower bound for the coefficient at the base](/entry/test-height-bound-slope-flat/).

## Statement

Let $\Psi$ be a finite set and $1 \le j < N$. For a label $\sigma$, put $\ell_m(\sigma^{+}) = \sum_{i < j} x_{\sigma,i}^m$ and $\ell_m(\sigma^{-}) = \sum_{i \ge j} (-x_{\sigma,i})^m$. A Frobenius map gives, for each prime $p$, label $\tau$ and $n \ge 0$, a signed label $\mathrm{frob}(p, \tau, n)$. For $k \ge 2$ put

$$r_p(\tau, k, Q) = k \log p \sum_{n \ge 0} p^{-k(n+1)} \deg_{\mathrm{Fl}}\bigl(\ell_{k-1}(\mathrm{frob}(p,\tau,n))\, Q\bigr),$$

and $r_p(\tau, 1, Q) = 0$. Let $R_{\tau,k}(Q) = \sum r_p(\tau, k, Q)$ over the primes $p > B_0$ that are not in a finite set $S$.

**Theorem.** Let $B_0 \ge 4|\Psi| N^2$. If $F_T = \sum_{\tau} \sum_{k=1}^{N} p_{\tau,k} Q_{\tau,k}$ with $Q_{\tau,k}$ homogeneous of degree $\dim \mathrm{Fl} + 1 - k$, then

$$\Bigl| \sum_{\tau} \sum_{k=1}^{N} R_{\tau,k}(Q_{\tau,k}) \Bigr| \le 1.6\, (D + 1)\, \delta.$$

The test polynomial $F_T$, $D$ and $\delta$ are as in [the lower bound for the coefficient at the base](/entry/test-height-bound-slope-flat/).

## Proof

Write $N = j + k$ with $k \ge 1$. If $\Psi$ is empty, the left side is $0$ and the right side is $1.6\,\delta \ge 0$, since $\delta > 0$ by `test_polynomial_shift_total`. Otherwise, `remainder_term_summable` shows that each $R_{\tau,k}(Q)$ is the limit as $B \to \infty$ of the sum of $r_p$ over the good primes in $(B_0, B]$. For each $B$, the double sum over $\tau, k$ of these finite sums is bounded by `finite_bound`, applied to that finite set of primes. Pass to the limit (`le_of_tendsto`). The rest is a change of the order of summation.

## In the Lean code

The theorem is in [TestPolynomialRemainderBound.lean](lean:Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/TestPolynomialRemainderBound.lean#L417). The definitions of $r_p$ (`restTerm`) and $R_{\tau,k}$ (`restSum`) are in [HeckeSectionsIsotropicCommutatorPairingPower.lean](lean:Development/AutomorphicSpectrum/Definitions/DivisibilityTowers/HeckeSectionsIsotropicCommutatorPairingPower.lean#L20). `restSum` is a `tsum` over all natural numbers, with value $0$ off the good primes. A Lean `tsum` is $0$ when the series does not converge, so the step through `remainder_term_summable`, which proves convergence, is needed to identify $R_{\tau,k}$ with the limit. The statement has no `Nonempty` hypothesis on $\Psi$, so the proof treats the empty case apart.
