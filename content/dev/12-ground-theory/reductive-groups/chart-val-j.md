---
id: chart-val-j
title: Chart values of harmonic polynomials lie in a power of an ideal
kind: theorem
decl: ReciprocityTheory.ChartRestriction.G.PullbackSections.Pf.chartValJ
module: ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.PullbackSections.HolomorphicFamilies.ChartValJ
covers: 310
status: drafted
drafted_by: writer@claude
---
This lemma is the common source of the two cases in [A lower bound on chart values over the host field at all places](/entry/ch-bound-host/). It says that a chart value, built from a harmonic polynomial and the canonical connection, lies in $J^e$ for an $R$-submodule $J$ and an exponent $e$ that counts opposite pairs of letters. With $J = 1$, the image of $R$, it gives integrality. With a larger $J$ it gives the ramified bound.

## Statement

Let $R \to k$ be injective, and let each $y \in k$ have $N y \in R$ for some integer $N > 0$ that depends on $y$ (`IsRQ`). Let $J$ be an $R$-submodule of $k$ with $1 \in J$. Let $B$ be a formal group datum of dimension $d$ with an action of $O$ (`FB`), $h$ a canonical gauge for $B$ (`IsCanonGauge`), $w_0 \in O$ with $w_0 + \bar w_0 = 1$, and $m \in \mathbb{N}$.

The letters $\ell = (\tau, i)$ have a type $\tau \in T$. An involution $\tau \mapsto \bar\tau$ of $T$ pairs the types, with a colour $c(\tau) = c(\bar\tau)$ and a side $s(\tau) \ne s(\bar\tau)$. Let $u, \varphi : \text{letters} \to R^d$ and $\psi : \text{letters} \to J^d$, and let $\sigma$ be the matrix `sg1 k h` (not unfolded). Suppose an orthogonality condition `heig` for letters of non-paired types, and three `OppositePairVanishing` conditions: the pairing $\beta_H$ of two of the vectors $(u, \varphi - \sigma u)$ and $(0, \psi)$ vanishes unless the letters have the same colour and opposite sides.

Let $P$ be a harmonic polynomial in letters of $n$ columns, with coefficients in $R$ (`HaO`). For a monomial $\mu$ and a column $b$, let $\mathrm{pm}(\mu_b) = \sum_q \min(\text{degree on side true},\ \text{degree on side false})$ over colours $q$ (`pairMin`). Suppose $\sum_b \mathrm{pm}(\mu_b) \le e$ for all $\mu$ in the support of $P$. Let $f_1, \dots, f_n$ be power series with coefficients in $R$ (`IntAA`).

**Theorem.**
$$\sum_{\mu} P_\mu \prod_{b=1}^{n} \mathrm{nabVal}\bigl(f_b,\ u,\ \mu_b\bigr) \in J^{e}.$$

Here `nabVal` is the constant coefficient of a differential polynomial (`DpolyOf`) applied to $f_b \cdot \exp(m\, h_L)$. We did not unfold `DpolyOf` or `expS`.

## Proof

1. Put $\varphi_K = \varphi + \psi - \sigma u$ and $g_b = \exp(m h_L) f_b$. The hypotheses `h21a`, `h21b`, `h21c` give `OppositePairVanishing` for the vectors $(u, 0)$ and $(0, \varphi_K)$ after a change of variables.
2. `CVA.harm_rename` moves harmonicity of $P$ to the renamed polynomial. `harmSecond_holds` then says that a second-order term vanishes.
3. `lemma_H_columns` rewrites the product of `nabVal` as the constant coefficients of the iterated connection operators `ordNabla`.
4. `scaled_connection_columns` gives that these constant coefficients lie in $J^e$, with $e$ bounded by `pairMin`. The rest is rewriting.

## In the Lean code

The theorem is at [ChartValJ.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/PullbackSections/HolomorphicFamilies/ChartValJ.lean#L31). `pairMin`, `OppositePairVanishing` and `ordNabla` are in [GermSC.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/TaylorDiscriminants/GermSC.lean#L22). `nabVal` is in [CocycleRightZeroThd.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/CocycleRightZeroThd.lean#L187).

The two users are `harmonic_value_integral_of_unit_discriminant`, with $J = 1$ and $\psi = 0$ ([HarmonicValueIntegralOfUnitDiscriminant.lean](lean:Development/AbelianVarietyTheory/Proofs/RingsOfIntegers/HarmonicValueIntegralOfUnitDiscriminant.lean#L142)), and `harmonicValue_bound_integralChart_ramified`, with $J$ = `Jv T e cJ` and $e = \mathrm{DF}(w)/2$ ([HarmonicValueBoundIntegralChartRamified.lean](lean:Development/AbelianVarietyTheory/Proofs/RingsOfIntegers/HarmonicValueBoundIntegralChartRamified.lean#L76)). We did not unfold `Jv`.
