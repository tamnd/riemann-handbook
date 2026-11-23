---
id: chern-numbers-eq-integral-chern-forms-smooth-metric
title: Chern numbers as integrals of Chern forms, for smooth metrics (restatement)
kind: theorem
decl: GlobalTheory.T.chernNumbers_eq_integral_chernForms_smoothMetric
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ChernNumbersEqIntegralChernFormsSmoothMetricStatement
covers: 901
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`ChernDegree.chernWeilNumbers_holds`](/entry/chern-weil-numbers-holds/). It proves $\mathrm{ChernWeilNumbers}$, the Chern-Weil formula for smooth metrics on a projective variety. [`goodChernWeil`](/entry/good-chern-weil/) uses it as the input `ChernWeilNumbers`, and there it is the smooth case to which good metrics are compared. The real content is in [the proof from the complex degree formula](/entry/chern-weil-numbers-of-chern-degree-complex/).

## Statement

**Theorem.** $\mathrm{ChernWeilNumbers}$ holds. Take $F$, $\sigma \colon F \to \mathbb{C}$, smooth projective varieties $X$ and $Y$, a family $E = (E_\tau)$ of vector bundles on $X$ of ranks $m_\tau$, a map $f \colon Y \to X$ with a full flag of $f^*E$ that refines $E$ (`Refines`), and divisors $x_{\tau,i}$ on $Y$ for the graded pieces (`IsGraded`), as in [`goodChernWeil`](/entry/good-chern-weil/). Let $H$ be a smooth hermitian metric on $E$ over all of $X(\mathbb{C})$ (`IsMetricOn E ⊤ H`). Then for each real polynomial $R$ in the Chern classes, the top-degree part of $R(c(E, H))$ is integrable on $X(\mathbb{C})$, and

$$\int_{X(\mathbb{C})} R(c(E, H)) = \int_Y R(x)\, \varpi, \qquad \varpi = \prod_{\tau,i} (-x_{\tau,i})^{m_\tau - 1 - i}.$$

This is $\mathrm{GoodChernNumbers}$ with $U = X$ and with no growth condition on $H$.

## Proof

The proof is `first | exact @GlobalTheory.ChernDegree.chernWeilNumbers_holds | ...`. The first branch closes the goal.

## In the Lean code

The theorem is in [ChernNumbersEqIntegralChernFormsSmoothMetricStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ChernNumbersEqIntegralChernFormsSmoothMetricStatement.lean#L5). The statement $\mathrm{ChernWeilNumbers}$ is in [ChernWeilNumbers.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/ChernWeilNumbers.lean#L10). "Integrable with integral $t$" is `HasChernIntegral` in [InterPolyProdSum.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/InterPolyProdSum.lean#L134): the positive and negative parts of the top Chern measure are finite, and their difference is $t$. The right side is an intersection number on $Y$, not on $X$.
