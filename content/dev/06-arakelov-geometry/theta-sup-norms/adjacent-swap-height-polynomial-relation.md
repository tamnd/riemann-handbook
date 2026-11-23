---
id: adjacent-swap-height-polynomial-relation
title: The adjacent swap relation, the statement form
kind: theorem
decl: GlobalTheory.T.adjacent_swap_height_polynomial_relation
module: Development.AutomorphicSpectrum.Proofs.MetricProofs.AdjacentSwapHeightPolynomialRelationStatement
covers: 615
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It states the adjacent swap relation for the limit height polynomial, and its proof applies [the adjacent swap relation](/entry/thm-a-swap/). That entry reduces the relation to [the reflection sum](/entry/height-polynomial-reflection-sum/), and the analysis is in [the reflection sum as a limit](/entry/thm-a-limit/). The user is [the sign change of the height defect](/entry/antisymmetry/), which applies it twice: once to a realization and once to the flag variety.

## Statement

The statement is the same as in [the adjacent swap relation](/entry/thm-a-swap/). In short: assume `Inputs`, a full intersection system $I$, and a realization $\mathrm{Re}$ of an analytic system $S$ of dimension $d + 1$. Let $(\tau, a)$ and $(\tau, b)$ with $b = a + 1$ be adjacent, with a square system for $(\tau, a)$ and coefficients $\xi_{\tau,a}$. Then for each weight $\lambda$, with $s$ the swap of the two entries and $u = \lambda_{\tau,a} - \lambda_{\tau,b}$,

$$\mathrm{PB}^{\mathrm{wt}}(\lambda) + \mathrm{PB}^{\mathrm{wt}}(\lambda \circ s) = T_{d+1,\kappa}\bigl(L_{c,\xi}(\deg_S)\bigr)(u),$$

where $c = \mathrm{gap}_\lambda + \tfrac{u}{2}\xi_{\tau,a}$.

## Proof

The proof is `first | exact @GlobalTheory.CompanionTheory.Ar.PB.thmA_swap | ...`. It applies the theorem with the same statement.

## In the Lean code

The theorem is in [AdjacentSwapHeightPolynomialRelationStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/MetricProofs/AdjacentSwapHeightPolynomialRelationStatement.lean#L9). Its user is in [Antisymmetry.lean](lean:Development/AutomorphicSpectrum/Proofs/MetricProofs/Antisymmetry.lean#L74).
