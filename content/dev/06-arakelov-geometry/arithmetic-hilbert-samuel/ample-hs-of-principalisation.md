---
id: ample-hs-of-principalisation
title: Counting small sections of an ample bundle, from principalisation
kind: theorem
decl: GlobalTheory.HSNef.ampleHS_of_principalisation
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.AmpleArithHilbertSamuelOfPrincipalisation
covers: 543
status: drafted
drafted_by: writer@claude
---
This theorem proves $\mathrm{AmpleHS}$, the arithmetic Hilbert-Samuel limit for an ample line bundle with a semipositive metric, from principalisation of ideals. It is the ample case in the proof of [the formula for nef bundles](/entry/arith-hilbert-samuel-of-principalisation/), which reaches it through the renaming [`T.ampleArithHilbertSamuel_of_principalisation`](/entry/ample-arith-hilbert-samuel-of-principalisation/).

## Statement

Let $X \to \operatorname{Spec} k$ be an arithmetic variety of dimension $D+1$. A pair $P$ (the structure `Pair`) is two hermitian line bundles $\overline{L}$, $\overline{A}$ with a rational section of each. For $m \geq 0$ and $R > 0$, let $\lambda_P(m, R)$ (the Lean `P.lc m 1 R`) be the logarithm of the number of sections of $L^m \otimes A$ whose pointwise norm is at most $R$ at every complex point. Let $g = \deg L$ (the Lean `gdeg P.L D`).

**Theorem.** Assume principalisation. Let $L$ be ample, with a semipositive metric and arithmetic self-intersection $a$. Then there is $t_0$ such that for all $t \geq t_0$

$$\frac{\lambda_P(m, e^{tm})}{m^{D+1}} \longrightarrow \frac{a + (D+1)\, t\, g}{(D+1)!} \qquad (m \to \infty).$$

The limit is the self-intersection that the rule `ArShift` gives to $\overline{L}$ with its metric shifted by $t$, divided by $(D+1)!$. The statement is a form of the arithmetic Hilbert-Samuel theorem for ample bundles (Gillet and Soulé, Invent. Math. 110, 1992; for semipositive metrics, Zhang, J. Amer. Math. Soc. 8, 1995), with an extra twist by $A$ and only for large $t$.

## Proof

The proof changes the metric of $\overline{L}$ by small weights, counts for the new metrics, and compares.

1. `MixHt.arCalc_of_principalisation` gives the [rules of arithmetic intersection](/entry/ar-calc-of-principalisation/) $\mathrm{ArCalc}$.
2. `T.exists_basepointFreeSectionTuple_ample_arith` gives $e$ and $D+1$ sections $x_0, \dots, x_D$ of $L^e$ with the property `Gens`, which we have not unfolded.
3. `T.exists_fubiniStudyWeights_bounded_difference` gives $B \geq 0$ and, for each $n \geq 1$, a weight $u_n$ with `IsCan` and $|u_n| \leq B$. Let $\overline{L}_n$ be $\overline{L}$ with its metric changed by $u_n$.
4. For each $n$: $\overline{L}_n$ is semipositive (`T.fubiniStudyWeightIncrement_semiPositive_curvature`) and has the same degree $g$ (`T.hermLineBundleGeometricDegree_raiseWeight`). Its self-intersection $a_n$ exists by `ArExists`, and $|a_n| \leq C/n$ by `T.selfIntersection_canonicalWeights_tendsto_zero`. In the metric of $\overline{L}_n$, each $x_l$ has norm at most $1$, and at each point some $x_l$ has norm at least $\kappa_n = (D+1)^{-1/(2n)}$ (`T.norm_basepointFree_sections_le_one_fubiniStudy`).
5. **Count for $\overline{L}_n$.** `T.sectionCount_growth_metric_near_generatorMax` uses these bounds on the $x_l$. For each $\varepsilon > 0$ and large $m$, the count for $\overline{L}_n$, divided by $m^{D+1}$, lies between $g t/D! - \varepsilon$ and $(g/D!)(t + \log(D+1)/(2ne)) + \varepsilon$.
6. **Change of metric.** `T.arithHilbertSamuel_smallSections_change_of_metric` is the one direct use of principalisation. With `T.isGoodSectionGroupFamily_ampleMultiples`, it gives $t_0$ such that for $t \geq t_0 + B$ the difference of the counts for $\overline{L}_n$ and $\overline{L}$, divided by $m^{D+1}$, tends to $(a_n - a)/(D+1)!$.

Steps 5 and 6 give, for $t \geq \max(t_0 + B, 1)$, each $n$ and each $\varepsilon$, and all large $m$,

$$\Bigl| \frac{\lambda_P(m, e^{tm})}{m^{D+1}} - \frac{g t}{D!} - \frac{a}{(D+1)!} \Bigr| \leq \frac{|g| \log(D+1)}{2 n e\, D!} + \frac{|C|}{n\, (D+1)!} + 2\varepsilon.$$

The right side tends to $0$ as $n \to \infty$ and $\varepsilon \to 0$. The rest is bookkeeping.

## In the Lean code

The theorem is in [AmpleArithHilbertSamuelOfPrincipalisation.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/AmpleArithHilbertSamuelOfPrincipalisation.lean#L26). `AmpleHS` is in [SmallFam.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/SmallFam.lean#L69), and `Pair` and `lc` are in [CharZeroFunctionField.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/CharZeroFunctionField.lean#L37). We have opened the statements of the lemmas of steps 2 to 6, not their proofs. We have not unfolded `Gens`, `IsCan` or `GoodFam`. The lemma names speak of Fubini-Study and canonical weights, but the statements give only the properties above. The final threshold is $\max(t_0 + B, 1)$, because step 5 needs $t > 0$.
