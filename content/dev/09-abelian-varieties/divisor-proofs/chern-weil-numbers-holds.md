---
id: chern-weil-numbers-holds
title: The Chern-Weil formula for smooth metrics holds
kind: theorem
decl: GlobalTheory.ChernDegree.chernWeilNumbers_holds
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ChernNumbersEqIntegralChernFormsSmoothMetric
covers: 900
status: drafted
drafted_by: writer@claude
---
This theorem proves $\mathrm{ChernWeilNumbers}$ with no hypothesis. It applies the reduction [`T.chernWeilNumbers_of_degree_eq_chernIntegral`](/entry/chern-weil-numbers-of-degree-eq-chern-integral/) to a proof of its one hypothesis, $\mathrm{ChernDegreeComplex}$. The result goes up under the second name [`T.chernNumbers_eq_integral_chernForms_smoothMetric`](/entry/chern-numbers-eq-integral-chern-forms-smooth-metric/) to [`goodChernWeil`](/entry/good-chern-weil/).

## Statement

**Theorem.** $\mathrm{ChernWeilNumbers}$ holds.

The statement is given in full in [the restatement entry](/entry/chern-numbers-eq-integral-chern-forms-smooth-metric/). For a smooth metric $H$ on a family $E$ of vector bundles on a smooth projective variety $X$, and a full flag of $E$ on $f \colon Y \to X$ with graded divisors $x_{\tau,i}$, it says that $\int_{X(\mathbb{C})} R(c(E, H)) = \int_Y R(x)\, \varpi$ for each real polynomial $R$ in the Chern classes.

## Proof

The hypothesis of the reduction is $\mathrm{ChernDegreeComplex}$. Let $Y$ be a smooth projective variety of dimension $n$ over $\mathbb{C}$. Let $L$ be a line bundle on $Y$ with rational sections $r$ whose divisor is $\Delta$ (`Presents Δ L r`), and let $\varphi$ be a smooth weight on $L$, that is, a smooth hermitian metric. Then the form $c_1(L, \varphi)^n$ is integrable on $Y(\mathbb{C})$, and

$$\int_{Y(\mathbb{C})} c_1(L, \varphi)^n = \Delta^n.$$

The proof of it, `ChernDegree.chernDegreeComplex`, has three steps:

1. integrability, from `T.chernIntegral_one_eq_mongeAmpereIntegral`, which also writes the integral as a Monge-Ampère integral of local potentials in an algebraic atlas;
2. $\int c_1(L, \varphi)^n$ is the top self-intersection of $L$, by `T.chernMass_eq_selfIntersection_lineBundle`;
3. that self-intersection is $\Delta^n$, by `T.intersection_divisor_eq_selfIntersection_presented`.

We have not opened the proofs of these three lemmas. The reduction then does the rest: see [its proof](/entry/chern-weil-numbers-of-chern-degree-complex/).

## In the Lean code

The theorem is in [ChernNumbersEqIntegralChernFormsSmoothMetric.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ChernNumbersEqIntegralChernFormsSmoothMetric.lean#L8). Its proof is one term:

```
GlobalTheory.T.chernWeilNumbers_of_degree_eq_chernIntegral GlobalTheory.T.degree_eq_integral_topChernForm_complex
```

`T.degree_eq_integral_topChernForm_complex` is a `first | exact ...` restatement of `ChernDegree.chernDegreeComplex` in [DegreeEqIntegralTopChernFormComplex.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/DegreeEqIntegralTopChernFormComplex.lean#L11). The statement $\mathrm{ChernDegreeComplex}$ is in [ChernDegreeComplex.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/ChernDegreeComplex.lean#L12). The theorem itself only joins two results; the work is in the three lemmas above and in the reduction.
