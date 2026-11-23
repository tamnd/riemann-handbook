---
id: good-chern-weil
title: Chern numbers from good metrics, and the flag push-forward
kind: theorem
decl: GlobalTheory.GoodMetric.goodChernWeil
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.GoodChernWeil
covers: 1442
status: drafted
drafted_by: writer@claude
---
This theorem proves $\mathrm{GoodChernWeil}$, with no hypothesis. Its only caller is [the literature form of the statement](/entry/good-chern-weil-of-literature/), which fills the field `p16` of the bundle [PublishedHodgeBundleTheorems](/step/published-results-arithmetic/). From there the statement goes to [proportionality on toroidal flag spaces](/entry/toroidal-flag-proportionality-of-good-chern-weil/). It rests on 1,442 declarations.

## Statement

**Theorem.** $\mathrm{GoodChernWeil}$ holds. It is the conjunction of two statements.

1. $\mathrm{GoodChernNumbers}$. Let $X$, $Y$ be smooth projective varieties over a field $F$, let $E = (E_\tau)$ be a finite family of vector bundles on $X$ of ranks $m_\tau$, and let $f \colon Y \to X$ carry a full flag of $f^*E$ with graded pieces given by divisors $x_{\tau,i}$ on $Y$. Let $\sigma \colon F \to \mathbb{C}$, let $U \subset X$ be open, and let $H$ be a hermitian metric on $E$ over $U(\mathbb{C})$ that is good along $X \setminus U$ in the sense of Mumford. Then for each real polynomial $R$ in the Chern classes, the top Chern form $R(c(E, H))$ is integrable on $U(\mathbb{C})$, and its integral is the intersection number $\int_Y R(x)\, \varpi$, with $\varpi = \prod_{\tau,i} (-x_{\tau,i})^{m_\tau - 1 - i}$.
2. $\mathrm{FlagPushForward}$. If $F$ has characteristic $0$ and $\sum_w \operatorname{sgn}(w)\, w(Q) = R(x)\, \Delta$, where $w$ runs over $\prod_\tau S_{m_\tau}$ and $\Delta = \prod_\tau \prod_{i<j}(x_{\tau,j} - x_{\tau,i})$, then $\int_Y Q = \int_Y R(x)\, \varpi$.

[The parent entry](/entry/good-chern-weil-of-literature/) gives the definitions in more detail. "Integrable with integral $t$" is `HasChernIntegral`: the positive and negative parts of the top Chern measure are finite, and their difference is $t$.

## Proof

Part 2 is `T.fullFlagBundle_pushForward_formula`, a restatement of `FlagPushProof.flagPushForward`. That proof uses a sign rule for adjacent swaps of the flag (`T.flagSpace_intersectionNumber_adjacent_swap_neg`) and a lemma on linear forms with that rule (`T.linearForm_eq_of_weylAntisymmetrization_eq`).

Part 1 is `goodChernWeil_of_goodTopChernForm`, applied to part 2 and to:

- `GoodTopChernForm` (from `GoodTop.goodTopChernForm`): for one bundle of rank $m$, a good metric $H$ on $U$ and a smooth metric $H_0$ on all of $X$, if the top Chern form $c_{\dim X}(E, H_0)$ has integral $t$ on $X(\mathbb{C})$, then $c_{\dim X}(E, H)$ has integral $t$ on $U(\mathbb{C})$;
- `ChernWeilNumbers` (from `ChernDegree.chernWeilNumbers_holds`): part 1 for smooth metrics on all of $X$, that is, with $U = X$.

1. Write the top-degree part of $R$ as $\sum_j a_j\, c_{\dim X} \circ \rho_j$ for polynomial representations $\rho_j$ of the general linear groups (`T.topDegreeFormCoeff_chernPoly_eq_sum_representations`). The curvature of the induced bundle $\rho_j(E)$ is $\rho_j$ of the curvature of $E$ (`curvPoly_polyRep`), so $R(c(E, H)) = \sum_j a_j\, c_{\dim X}(\rho_j(E), \rho_j(H))$ pointwise.
2. Choose a smooth metric $H_0$ on $E$ over all of $X$ (`T.exists_smooth_hermitianMetric_projective_variety`), and the induced bundles and metrics (`T.exists_polyRep_inducedBundle_and_metric`). The induced metric of a good metric is good (`isGood_polyRep`).
3. For each $j$, `ChernWeilNumbers` gives an integral $t_j$ of $c_{\dim X}(\rho_j(E), \rho_j(H_0))$, and `GoodTopChernForm` gives the same $t_j$ for $\rho_j(H)$ on $U$.
4. By linearity (`T.hasChernIntegral_linear_of_density_eq_sum`), $R(c(E,H))$ on $U$ and $R(c(E,H_0))$ on $X$ both have integral $\sum_j a_j t_j$. `ChernWeilNumbers` for $H_0$ identifies this with $\int_Y R(x)\, \varpi$.

## In the Lean code

The theorem is in [GoodChernWeil.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/GoodChernWeil.lean#L10). Its proof is one term:

```
goodChernWeil_of_goodTopChernForm T.goodMetric_topChernForm_integral_eq_smooth
  T.chernNumbers_eq_integral_chernForms_smoothMetric T.fullFlagBundle_pushForward_formula
```

The lemmas:

- `GoodMetric.goodChernWeil_of_goodTopChernForm` in [GoodChernWeilOfGoodTopChernForm.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/GoodChernWeilOfGoodTopChernForm.lean#L149);
- `GoodTop.goodTopChernForm` in [GoodMetricTopChernFormIntegralEqSmooth.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/GoodMetricTopChernFormIntegralEqSmooth.lean#L20);
- `ChernDegree.chernWeilNumbers_holds` in [ChernNumbersEqIntegralChernFormsSmoothMetric.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ChernNumbersEqIntegralChernFormsSmoothMetric.lean#L8);
- `FlagPushProof.flagPushForward` in [FullFlagBundlePushForwardFormula.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/FullFlagBundlePushForwardFormula.lean#L13).

The three `T.` names are `first | exact ...` restatements of these lemmas, with statements in [MumfordProportionality.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/MumfordProportionality.lean#L16), [GoodTopChernForm.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/GoodTopChernForm.lean#L10) and [ChernWeilNumbers.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/ChernWeilNumbers.lean#L10).

Odd points. $\mathrm{FlagPushForward}$ has no metric and passes through unchanged. `ChernWeilNumbers` is `GoodChernNumbers` with $U = X$ and without the condition `IsGood`. It is proved on its own and enters as an input.
