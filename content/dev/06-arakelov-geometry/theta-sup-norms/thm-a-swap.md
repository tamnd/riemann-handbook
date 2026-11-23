---
id: thm-a-swap
title: The adjacent swap relation
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.PB.thmA_swap
module: Development.AutomorphicSpectrum.Proofs.MetricProofs.AdjacentSwapHeightPolynomialRelation
covers: 608
status: drafted
drafted_by: writer@claude
---
This theorem computes the sum of the limit height polynomial at a weight $\lambda$ and at $\lambda$ with two adjacent entries swapped. The answer depends only on the degree polynomial of the analytic system. The proof is a change of variables in [the reflection sum](/entry/height-polynomial-reflection-sum/), which has the analysis. The result goes up through [the statement form](/entry/adjacent-swap-height-polynomial-relation/) to [the sign change of the height defect](/entry/antisymmetry/).

## Statement

We use the notation of [the sign change of the height defect](/entry/antisymmetry/): the gaps $\mathrm{gap}_\lambda$, the polynomial $\mathrm{PB}^{\mathrm{wt}}(\lambda) = \mathrm{PB}(\mathrm{gap}_\lambda)$ and the degree polynomial $\deg_S$. Fix $\tau \in \Psi$ and $a$ with $b = a + 1 < N$. Let $\xi_{\tau,a}(\tau, a) = -2$, $\xi_{\tau,a}(\tau, a \pm 1) = 1$, and $\xi_{\tau,a} = 0$ elsewhere. For $c \colon \sigma \to \mathbb{R}$, $\varepsilon \colon \sigma \to \mathbb{Z}$ and $Q \in \mathbb{R}[X_\sigma]$ let $L_{c,\varepsilon}(Q)(x) = Q(c - \tfrac{x}{2}\varepsilon)$ (`linePoly`). For a polynomial $P = \sum_n P_n x^n$ let

$$T_{D,\kappa}(P) = \sum_{n \text{ odd}} (D + 1)\, \frac{\kappa\bigl(\tfrac{n+1}{2}\bigr)}{(n+1)/2}\, P_n\, x^{n+1}$$

(`tsgPoly`). Here $\kappa(k)$ is a double integral over $S^2 \times S^2$ of $-\tfrac12 \log\bigl((1 - n_1 \cdot n_2)/2\bigr)$ against a polynomial. The proved statement `FibreLocal.Statement` gives $\kappa(k) = \tfrac12 \sum_{i < k} \frac{1}{2i+1}$.

**Theorem.** Assume `Inputs`. Let $I$ be a full intersection system, $S$ an analytic system of dimension $d + 1$ on $\Psi \times \{0, \dots, N-1\}$, and $\mathrm{Re}$ a realization of $S$ with a square system for $(\tau, a)$ and $\xi_{\tau,a}$. Let $s$ swap $(\tau, a)$ and $(\tau, b)$. For each $\lambda$, with $u = \mathrm{gap}_\lambda(\tau, a)$ and $c = \mathrm{gap}_\lambda + \tfrac{u}{2}\xi_{\tau,a}$,

$$\mathrm{PB}^{\mathrm{wt}}(\lambda) + \mathrm{PB}^{\mathrm{wt}}(\lambda \circ s) = T_{d+1,\kappa}\bigl(L_{c,\xi_{\tau,a}}(\deg_S)\bigr)(u).$$

## Proof

The swap changes $\mathrm{gap}_\lambda(\tau, a)$ to $-u$ and adds $u$ to the gaps at $(\tau, a \pm 1)$. So $\mathrm{gap}_{\lambda \circ s} = \mathrm{gap}_\lambda + u\,\xi_{\tau,a}$. With $c$ as above, `gap_swap_decomp` gives $c(\tau, a) = 0$, $\mathrm{gap}_\lambda = c - \tfrac{u}{2}\xi_{\tau,a}$ and $\mathrm{gap}_{\lambda \circ s} = c + \tfrac{u}{2}\xi_{\tau,a}$. Then [the reflection sum](/entry/height-polynomial-reflection-sum/), with $a_0 = (\tau, a)$ and $\varepsilon = \xi_{\tau,a}$, is the claim. Its hypothesis `FibreLocal.Statement` is given by `FibreLocal.proof`. The lemma `eval_toWt_gap` does the rewriting $Q^{\mathrm{wt}}(\lambda) = Q(\mathrm{gap}_\lambda)$.

## In the Lean code

The theorem is in [AdjacentSwapHeightPolynomialRelation.lean](lean:Development/AutomorphicSpectrum/Proofs/MetricProofs/AdjacentSwapHeightPolynomialRelation.lean#L14). The objects $\xi_{\tau,a}$, $L$ and the gaps are in [PairRelationOfScaledRatio.lean](lean:Development/AutomorphicSpectrum/Definitions/MetricPeriods/PairRelationOfScaledRatio.lean#L28), and $T$ is `tsgPoly` in [CompRightEqZero.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/ArithmeticIntersection/CompRightEqZero.lean#L23). `gap_swap_decomp` is in [EtaleAwayOfIsEtaleAtOffSubmonoid.lean](lean:Development/AutomorphicSpectrum/Proofs/MetricProofs/EtaleAwayOfIsEtaleAtOffSubmonoid.lean#L44), a file whose name has nothing to do with gaps. `FibreLocal.proof` is in [PFibreLocal.lean](lean:GroundTheory/HeightsAndTheta/Heights/Intersections/PFibreLocal.lean#L166).

The theorem needs no condition relating $a$ and $b$ to the integer $j$ of a flag system. That condition enters only in [the sign change of the height defect](/entry/antisymmetry/), where it says for which pairs the flag system gives a square system.
