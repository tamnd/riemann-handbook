---
id: test-height-bound
title: The lower bound for the coefficient at the base (statement form)
kind: theorem
decl: GlobalTheory.T.test_height_bound
module: Development.AutomorphicSpectrum.Proofs.DivisibilityProofs.TestHeightBoundStatement
covers: 779
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It has the same statement as [`test_height_bound_slope_flat`](/entry/test-height-bound-slope-flat/), which has the real content, and its proof applies that theorem. Its user is [the chain of tower estimates](/entry/chain-tower/), step 7, where it turns the slope bound `SlopeLower` into a lower bound for the coefficient $A_0$ of the tower height identity.

## Statement

Let $II$ be an intersection system, $T$ a root tower with index $j$ and $N$ variables per label, $\Psi$ a nonempty finite set of labels, $h$ a linear form on $\mathbb{R}[x_{\tau, i}]$, $\mathrm{frob}$ a Frobenius map, and $C, C' \ge 0$, $\mathrm{rd} \ge 1$, $L$ real numbers.

**Theorem.** If $T$ has `Proportional`, $h$ has `I9`, $T$ has `PropF` with constant $C'$ and `SlopeLower` with constant $C$, and

$$h(F_T) \le (D + 1)\, \delta \, |\Psi| \tfrac{m}{2} \log(N + 1),$$

then $T$ has `LowerBoundAtBase` with constant $2(C + C') + 3$.

Here $F_T$ is the test polynomial, $D = |\Psi|\, j (N - j)$, $\delta$ the flag degree of $\mu^D \cdot \mathrm{fib}$, and $m = \min(j, N - j)$. These objects and the properties are defined in [the entry for `test_height_bound_slope_flat`](/entry/test-height-bound-slope-flat/).

## Proof

Apply `test_height_bound_slope_flat`.

## In the Lean code

The theorem is in [TestHeightBoundStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/TestHeightBoundStatement.lean#L11). The proof is the `first | exact @… | exact … | (intros; apply … <;> assumption)` pattern of the other statement files. The name says "test height bound", but the conclusion bounds the coefficient $A_0$, not a height. The bound on the height $h(F_T)$ is a hypothesis.
