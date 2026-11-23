---
id: test-height-bound-slope-flat
title: The lower bound for the coefficient at the base
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Top.test_height_bound_slope_flat
module: Development.AutomorphicSpectrum.Proofs.DivisibilityProofs.TestHeightBound
covers: 778
status: drafted
drafted_by: writer@claude
---
This theorem bounds the coefficient $A_0$ of the tower height identity from below, by evaluating the identity at one test polynomial. Its statement form is [`test_height_bound`](/entry/test-height-bound/), which [the tower chain](/entry/chain-tower/) uses in step 7.

## Statement

Let $T$ be a root tower with index $1 \le j < N$, labels $\Psi \neq \emptyset$, bad primes $S$ and volume $\mathrm{vol}$. Write $\mathrm{PP}_B$ for the intersection form at level $B$ (not unfolded here) on polynomials in the $x_{\tau,i}$. The flag degree $\deg_{\mathrm{Fl}}$ is the signed sum of the coefficients at the permuted staircase monomials. Let $p_{\tau,k} = \sum_i x_{\tau,i}^k$.

- $\mathrm{Sh}_\tau(F) = \deg_{\mathrm{Fl}} \sum_{i < j} \partial F / \partial x_{\tau,i}$ and $\mathrm{Tot}_\tau$ is the same with all $i$.
- Test polynomial: $F_T = \mu^{D+1} \mathrm{fib}$, with $D = |\Psi| j (N-j)$, $\mu$ the sum of the variables of the smaller block (negated for the block $i < j$), and $\mathrm{fib}$ the product of $x_{\tau,b} - x_{\tau,a}$ over $a < b$ in the same block. Let $\delta = \deg_{\mathrm{Fl}}(\mu^D \mathrm{fib})$ and $m = \min(j, N-j)$.
- $\Lambda_B = \log(B \cdot \mathrm{rd}) + |L|$.
- `IdentAt` $(B_0, A_0, b_0)$: for each $\tau$, $1 \le k \le N$ and homogeneous $Q$ of the right degree, $\mathrm{PP}_{B_0}(p_{\tau,k} Q) = \mathrm{vol}\,\bigl(h - A_0 \sum_\sigma \mathrm{Sh}_\sigma - b_0 \sum_\sigma \mathrm{Tot}_\sigma\bigr)(p_{\tau,k} Q) + \mathrm{vol}\, R_{\tau,k}(Q)$, with $R_{\tau,k}$ a sum over the good primes $p > B_0$ ([remainder bound](/entry/test-rest-bound/)).
- `LowerBoundAtBase` with constant $c$: $A_0 \ge -c\,\Lambda_{B_0}$ whenever `IdentAt` $(B_0, A_0, b_0)$ holds, $B_0 \ge 128$, $B_0 \ge 4|\Psi| N^2$ and $B_0 \ge |S|$.

**Theorem.** Let $C, C' \ge 0$ and $\mathrm{rd} \ge 1$. Assume `Proportional`, `I9` for $h$, `PropF` with $C'$, `SlopeLower` with $C$, which says $\mathrm{PP}_B(F_T) \ge -C |\Psi| m \Lambda_B (D+1)\,\mathrm{vol}\,\delta$, and $h(F_T) \le (D+1)\delta|\Psi| \tfrac{m}{2} \log(N+1)$. Then `LowerBoundAtBase` holds with $c = 2(C + C') + 3$.

## Proof

Fix $B_0, A_0, b_0$ and put $\ell = \log(N+1)$.

1. `test_polynomial_shift_total` computes $\delta > 0$, $\mathrm{Sh}(F_T)$ and $\mathrm{Tot}(F_T)$. `homogeneous_power_sum_decomposition` writes $F_T = \sum p_{\tau,k} Q_{\tau,k}$. `tower_height_identity_expansion` sums `IdentAt` over it.
2. `test_polynomial_remainder_bound` gives $|R| \le 1.6 (D+1)\delta$. `cutoff_coefficients_bound` gives $|j A_0 + N b_0| \le C' N \Lambda_{B_0}$.
3. If $N - j \le j$, $\mathrm{Sh}(F_T) = 0$ and $\mathrm{Tot}_\tau(F_T) = (D+1) m \delta$. `SlopeLower` over $\mathrm{vol}$ and the bound for $h(F_T)$ give $b_0 \le C\Lambda + \ell/2 + 1.6$. With step 2, $j A_0 \ge -N(C\Lambda + \ell/2 + 1.6 + C'\Lambda)$, and $N \le 2j$.
4. If $N - j > j$, then $\mathrm{Sh}_\tau = \mathrm{Tot}_\tau = -(D+1) j \delta$. Then $-(A_0 + b_0) \le C\Lambda + \ell/2 + 1.6$. Since $(N-j)A_0 = N(A_0 + b_0) - (jA_0 + N b_0)$ and $N \le 2(N - j)$, the same bound holds for $A_0$.
5. Both cases give $A_0 \ge -2(C\Lambda + C'\Lambda + \ell/2 + 1.6)$ (`lower_bound_finite_arith`). The bounds on $B_0$ and $\mathrm{rd} \ge 1$ give $\ell, 1.6 \le \log B_0 \le \Lambda$. So $A_0 \ge -(2(C+C') + 3)\Lambda$.

## In the Lean code

The theorem is in [TestHeightBound.lean](lean:Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/TestHeightBound.lean#L32). The properties are in [HeckeSectionsIsotropicCommutatorPairingPower.lean](lean:Development/AutomorphicSpectrum/Definitions/DivisibilityTowers/HeckeSectionsIsotropicCommutatorPairingPower.lean#L62) and [Proportional.lean](lean:Development/AutomorphicSpectrum/Definitions/DivisibilityTowers/Proportional.lean#L123). All hypotheses are used, and the two helper inequalities are proved by `nlinarith`. `Proportional` gives $\mathrm{vol} > 0$. `I9` and `PropF` go only to `cutoff_coefficients_bound`, which we have not unfolded. The Frobenius map has no condition and enters only through `IdentAt`. The name says "slope flat", but the statement has no flatness.
