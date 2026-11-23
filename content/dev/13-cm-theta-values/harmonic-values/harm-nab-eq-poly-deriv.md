---
id: harm-nab-eq-poly-deriv
title: Harmonic values of the canonical connection are derivatives of theta functions
kind: theorem
decl: GlobalTheory.AnVal.harm_nab_eq_polyDeriv
module: Development.AbelianVarietyTheory.Proofs.CuspFormEvaluations.HarmonicValueCanonicalConnectionEqPolyDeriv
covers: 357
status: drafted
drafted_by: writer@claude
---
This theorem is the real proof of [harmonic-value-canonical-connection-eq-poly-deriv](/entry/harmonic-value-canonical-connection-eq-poly-deriv/), which is a second name for it. It computes the canonical connection at a complex point in an analytic chart. There the formal group is additive, so the connection becomes ordinary differentiation of theta functions.

## Statement

The statement is the one in the parent entry. Assume `ChartIndepSt2`. Take a complex framed point $y$ with an analytic uniformization $\Phi$ of dimension $g$, a canonical connection `nab`, sections $F_1, \dots, F_n$ of the $k$-th power with theta readings $\theta_b$, and a harmonic polynomial $P$ (`HHa`). Then

$$\sum_{m} P_m \prod_b \nabla_y(F_b)(m_b) = \partial_P\Bigl(z \mapsto \prod_b \theta_b(z_b)\Bigr)(0).$$

## Proof

1. Choose $N > 0$ with $N P$ in the integral harmonic set `harmA` (`exists_natCast_smul_mem_harmA`). This is needed because `ChartIndepSt2` speaks only of `harmA`.
2. `IsNab` gives a chart $C_1$ at $y$, germs $f_b$ of the $F_b$ in $C_1$, and the values $\nabla_y(F_b)(\alpha)$ as `nabVal` of $f_b$ in $C_1$.
3. [exists-analytic-biextension-chart-complex-point](/entry/exists-analytic-biextension-chart-complex-point/) gives a second chart $C$ of dimension $g$ with $h = 0$, the additive group law $X_0 + X_1$, unit directions given by `el`, and germs equal to the Taylor series of the $\theta_b$ at $0$.
4. Each $\theta_b$ is holomorphic (`section_reading_existsUnique_isTheta`).
5. `ChartIndepSt2` applied to $C_1$ and $C$ and to $N P$ gives `chartVal C₁ = chartVal C`. Cancel the factor $N$. Now the left side is a sum of `nabVal` values in $C$.
6. In an additive chart with $h = 0$, `nabVal` of a Taylor series is the polynomial derivative at $0$ (`nabVal_additive`).
7. `polyDeriv_prod_column_functions` writes the polynomial derivative of $\prod_b \theta_b(z_b)$ as the sum over $m$ of the products of the column derivatives. The two sides then agree term by term.

## In the Lean code

The theorem is at [HarmonicValueCanonicalConnectionEqPolyDeriv.lean](lean:Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/HarmonicValueCanonicalConnectionEqPolyDeriv.lean#L25). The helper `sum_support_natCast_smul` (L17) moves the factor $N$ out of the sum. Other lemmas:

- `ChartIndepSt2` and `chartVal` in [ThExprUniqOfChartIndep2.lean](lean:Formalism/SharpRestriction/Divisibility/GeneratorPowers/ThExprUniqOfChartIndep2.lean#L12) and [CIndSt.lean](lean:Formalism/SharpRestriction/Divisibility/GeneratorPowers/CIndSt.lean#L12).
- `nabVal_additive` in [TaylorPSEqTay.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/PullbackSections/HolomorphicFamilies/TaylorPSEqTay.lean#L29).
- `exists_natCast_smul_mem_harmA` in [ExistsNatCastSmulCoeffIsIntegral.lean](lean:Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/ExistsNatCastSmulCoeffIsIntegral.lean#L31).

`ChartIndepSt2` is proved as `chartIndep` in [EmbeddingsDifferOnInteger.lean](lean:Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/EmbeddingsDifferOnInteger.lean#L98), so the hypothesis is not a real assumption.
