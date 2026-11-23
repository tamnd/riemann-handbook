---
id: test-polynomial-remainder-bound
title: The prime remainder of the test polynomial is bounded (statement form)
kind: theorem
decl: GlobalTheory.T.test_polynomial_remainder_bound
module: Development.AutomorphicSpectrum.Proofs.DivisibilityProofs.TestPolynomialRemainderBoundStatement
covers: 775
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It has the same statement as [`testRest_bound`](/entry/test-rest-bound/), which has the real content, and its proof applies that theorem. Its user is [the lower bound for the coefficient at the base](/entry/test-height-bound-slope-flat/), where it bounds the remainder term $R$ in step 2.

## Statement

Let $\Psi$ be a finite set, $1 \le j < N$, $S$ a finite set of bad primes, $\mathrm{frob}$ a Frobenius map and $B_0 \ge 4 |\Psi| N^2$. Let $F_T$ be the test polynomial of index $j$, $D = |\Psi| j (N-j)$ and $\delta = \deg_{\mathrm{Fl}}(\mu^D \mathrm{fib})$, as in [the lower bound for the coefficient at the base](/entry/test-height-bound-slope-flat/).

**Theorem.** If $F_T = \sum_{\tau} \sum_{k=1}^{N} p_{\tau,k} Q_{\tau,k}$ with $Q_{\tau,k}$ homogeneous of degree $\dim \mathrm{Fl} + 1 - k$, then

$$\Bigl| \sum_{\tau} \sum_{k=1}^{N} R_{\tau,k}(Q_{\tau,k}) \Bigr| \le 1.6\, (D + 1)\, \delta,$$

where $R_{\tau,k}$ is the sum over primes $p > B_0$ outside $S$ defined in [the entry for `testRest_bound`](/entry/test-rest-bound/).

## Proof

Apply `testRest_bound`.

## In the Lean code

The theorem is in [TestPolynomialRemainderBoundStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/TestPolynomialRemainderBoundStatement.lean#L11). The proof is the `first | exact @… | exact … | (intros; apply … <;> assumption)` pattern of the other statement files. The bound does not depend on $S$, on $\mathrm{frob}$ or on the choice of the decomposition $Q$.
