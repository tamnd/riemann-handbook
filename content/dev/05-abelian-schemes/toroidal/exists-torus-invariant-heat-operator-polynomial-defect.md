---
id: exists-torus-invariant-heat-operator-polynomial-defect
title: A torus-invariant heat operator with polynomial defect (statement form)
kind: theorem
decl: GlobalTheory.T.exists_torusInvariant_heatOperator_polynomial_defect
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsTorusInvariantHeatOperatorPolynomialDefectStatement
covers: 472
status: drafted
drafted_by: writer@claude
---
This theorem is the statement form of [`exists_basic_heat_polyDefect`](/entry/exists-basic-heat-poly-defect/), which has the real content. [`heat_commuting_periods_exists`](/entry/heat-commuting-periods-exists/) uses it as its first step, and then removes the defect.

## Statement

Use the setting and the names of [the entry above](/entry/exists-torus-invariant-heat-operator-commuting-periods/): a complete Noetherian local domain $R \supseteq \mathbb{Q}$, a degeneration datum with abelian part $B$ and character group $X$, the Raynaud extension $q \colon \tilde G \to B$ with invariant vector fields $\partial_1, \dots, \partial_n$, monomial periods in nonzero $t_1, \dots, t_m$, and a derivation $D$ of $R$ with $D(t_i) \in (t_i)$.

**Theorem.** There are a basic heat operator $h$ for $D$, a map $w \colon X \to \operatorname{Hom}(X, R)$ and maps $\pi, \pi' \colon X \to R$ such that the defect of $h$ is

$$c(k, \mu, \alpha) = 2k\, w(\mu)(\alpha) + 2k^2 \pi(\mu) + 2k\, \pi'(\mu).$$

So the defect is a polynomial in the level $k$ with no constant term, and it is additive in the weight $\alpha$.

## Proof

The proof is one line: it applies `GlobalTheory.HeatEx.exists_basic_heat_polyDefect`. See [that entry](/entry/exists-basic-heat-poly-defect/).

## In the Lean code

The theorem is in [ExistsTorusInvariantHeatOperatorPolynomialDefectStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsTorusInvariantHeatOperatorPolynomialDefectStatement.lean#L16). Its statement is the same as that of `exists_basic_heat_polyDefect`, word for word. The proof is the tactic `first | exact @GlobalTheory.HeatEx.exists_basic_heat_polyDefect | ...`. It is a second name and adds nothing.
