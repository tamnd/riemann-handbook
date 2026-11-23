---
id: height-polynomial-reflection-sum
title: The reflection sum of the limit height polynomial, the statement form
kind: theorem
decl: GlobalTheory.T.height_polynomial_reflection_sum
module: Development.AutomorphicSpectrum.Proofs.MetricProofs.HeightPolynomialReflectionSumStatement
covers: 407
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It states the reflection sum for the limit height polynomial along a square system, and its proof applies [the reflection sum as a limit](/entry/thm-a-limit/), where the real content is. Its user is [the adjacent swap relation](/entry/thm-a-swap/), which specializes it to a swap of two adjacent weights.

## Statement

We use the notation of [the adjacent swap relation](/entry/thm-a-swap/) for $\mathrm{PB}$, $\deg_S$, $L_{c,\varepsilon}$, $T_{D,\kappa}$ and $\kappa$, now on any finite index set $\sigma$.

**Theorem.** Assume `Inputs` and `FibreLocal.Statement`. Let $I$ be a full intersection system, $S$ an analytic system of dimension $d + 1$ on $\sigma$, and $\mathrm{Re}$ a realization of $S$. Let $a_0 \in \sigma$ and $\varepsilon \colon \sigma \to \mathbb{Z}$, with a square system for $(a_0, \varepsilon)$. Then for each $c \colon \sigma \to \mathbb{R}$ with $c(a_0) = 0$ and each $u \in \mathbb{R}$,

$$\mathrm{PB}\bigl(c - \tfrac{u}{2}\varepsilon\bigr) + \mathrm{PB}\bigl(c + \tfrac{u}{2}\varepsilon\bigr) = T_{d+1,\kappa}\bigl(L_{c,\varepsilon}(\deg_S)\bigr)(u).$$

The left side is even in $u$. So is the right side: $T$ keeps only the odd coefficients $P_n$ and puts them on $u^{n+1}$.

## Proof

The proof is `first | exact @GlobalTheory.CompanionTheory.Ar.PB.thmA_limit | ...`. It applies the theorem with the same statement. That proof passes to the limit $t \to 0^+$ in identities for the polar forms of the intersection numbers at $t > 0$. It calls `agreement_positive`, `polar_identity_from_symmetric_forms`, `square_system_polar_vanishing`, `analytic_square_regularized_convergence` and `square_polar_integral_identity`; we have not unfolded them.

## In the Lean code

The theorem is in [HeightPolynomialReflectionSumStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/MetricProofs/HeightPolynomialReflectionSumStatement.lean#L9), and the proof that it calls is in [HeightPolynomialReflectionSum.lean](lean:Development/AutomorphicSpectrum/Proofs/MetricProofs/HeightPolynomialReflectionSum.lean#L41).

The hypothesis `FibreLocal.Statement` is a proved theorem, `FibreLocal.proof` in [PFibreLocal.lean](lean:GroundTheory/HeightsAndTheta/Heights/Intersections/PFibreLocal.lean#L166). It holds sphere integrals and the formula $\kappa(k) = \tfrac12 \sum_{i<k} \frac{1}{2i+1}$. Only `square_polar_integral_identity` uses it. It could be removed from the statement; [the adjacent swap relation](/entry/thm-a-swap/) supplies it.
