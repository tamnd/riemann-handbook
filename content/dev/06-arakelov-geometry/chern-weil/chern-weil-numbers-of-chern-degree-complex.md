---
id: chern-weil-numbers-of-chern-degree-complex
title: Chern-Weil numbers by the splitting principle, from the degree formula
kind: theorem
decl: GlobalTheory.ChernCalc.chernWeilNumbers_of_chernDegreeComplex
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ChernWeilNumbersOfDegreeEqChernIntegral
covers: 761
status: drafted
drafted_by: writer@claude
---
This theorem proves the Chern-Weil formula for smooth metrics on vector bundles from the same formula for one line bundle over $\mathbb{C}$. The method is the splitting principle: pull back to the flag variety, where the bundle has a filtration by line bundles. The result goes up under the second name [`T.chernWeilNumbers_of_degree_eq_chernIntegral`](/entry/chern-weil-numbers-of-degree-eq-chern-integral/) to [`ChernDegree.chernWeilNumbers_holds`](/entry/chern-weil-numbers-holds/), which proves the hypothesis.

## Statement

**Theorem.** $\mathrm{ChernDegreeComplex}$ implies $\mathrm{ChernWeilNumbers}$.

$\mathrm{ChernDegreeComplex}$: for a smooth projective variety $Z$ of dimension $n$ over $\mathbb{C}$, a line bundle $L$ with rational sections whose divisor is $\Delta$, and a smooth hermitian metric $\varphi$ on $L$, the form $c_1(L, \varphi)^n$ is integrable on $Z(\mathbb{C})$ and $\int c_1(L, \varphi)^n = \Delta^n$.

$\mathrm{ChernWeilNumbers}$: let $F$ be a field with $\sigma \colon F \to \mathbb{C}$, let $E = (E_\tau)$ be a family of vector bundles of ranks $m_\tau$ on a smooth projective $X$ over $F$, and let $H$ be a smooth hermitian metric on $E$ over $X_\sigma(\mathbb{C})$. Let $f \colon Y \to X$ carry a full flag $E'$ of $f^*E$ that refines $E$, with graded pieces given by divisors $x_{\tau,i}$ on $Y$. Then for each real polynomial $R$ in the Chern classes, $R(c(E, H))$ is integrable on $X_\sigma(\mathbb{C})$ and $\int_{X_\sigma(\mathbb{C})} R(c(E, H)) = \int_Y R(x)\, \varpi$, with $\varpi = \prod_{\tau,i} (-x_{\tau,i})^{m_\tau - 1 - i}$ and $R(x)$ as in [`goodChernWeil`](/entry/good-chern-weil/).

## Proof

1. **Any field.** `T.degreeEqChernFormIntegral_of_complex_case` turns $\mathrm{ChernDegreeComplex}$ into $\mathrm{ChernDegree}$, the same statement for a variety over $F$ and an embedding $\sigma$. Its proof (`chernDegree_of_complex`) base-changes the variety along $\sigma$ to $\mathbb{C}$, identifies the complex points, and checks that the intersection number does not change.
2. **Finiteness.** $X_\sigma(\mathbb{C})$ is compact. The form $R(c(E, H))$ is a smooth top form in the holomorphic atlas (`T.isForm_evalRealPoly_chernForms_flaggedMetric`), so its positive and negative parts are finite measures (the first clause of `T.holAtlas_topFormIntegral_finite_additive_homogeneous`).
3. **Pull back to the flag.** The metric $H$ induces a metric $H'$ on the flag $E'$ (`pullGram`; it is a metric by `T.isFlaggedBundleMetric_pullGram_refinement`). Let $\gamma_{\tau,i}$ be the first Chern forms of the graded pieces for $H'$. Integration along the fibres gives $\int_X \alpha = \int_Y f^*\alpha \cdot \varpi(\gamma)$ for each top form $\alpha$ on $X$ (`T.flagBundle_fibreIntegral_pullback_mul_fibreClass`).
4. **Chern forms of the pull-back.** $f^* c(E, H) = c(E', H')$ (`T.chernForms_pullback_metric_flag_refinement`), so $f^* R(c(E, H)) = R(c(E', H'))$ (`T.pullback_real_polynomial_even_form_fields`).
5. **Splitting.** Under the integral over $Y$, the Chern forms of $(E', H')$ may be replaced by the elementary symmetric functions of the $\gamma_{\tau,i}$: $\int_Y R(c(E', H')) \cdot Q(\gamma) = \int_Y (R(x)\, Q)(\gamma)$ for each $Q$ (`T.integral_chernForms_eq_esymm_gradedForms_flag`). Take $Q = \varpi$.
6. **Line bundles.** Each $\gamma_{\tau,i}$ is $c_1(L_{\tau,i}, \psi_{\tau,i})$ for a line bundle $L_{\tau,i}$ with rational sections whose divisor is $x_{\tau,i}$, and a smooth weight $\psi_{\tau,i}$ (`T.flag_graded_metrics_weights_on_line_bundles`). Then `T.integral_chernFormPoly_eq_intersectionNumber`, with $\mathrm{ChernDegree}$, gives $\int_Y (R(x)\,\varpi)(\gamma) = \int_Y R(x)\,\varpi$.

The rest is bookkeeping: the top Chern measure is the measure of the form in the atlas (`T.chernTopFormSignedMeasure_eq_atlas_part`), and the set of points is all of $X_\sigma(\mathbb{C})$.

## In the Lean code

The theorem is in [ChernWeilNumbersOfDegreeEqChernIntegral.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ChernWeilNumbersOfDegreeEqChernIntegral.lean#L21). Each `T.` lemma above is a `first | exact ...` restatement of a lemma in the namespaces `ChernCalc`, `LineForm`, `ChernLine` or `ChernDegreeBaseChange`. `chernDegree_of_complex` is in [DegreeEqChernFormIntegralOfComplexCase.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/DegreeEqChernFormIntegralOfComplexCase.lean#L41). We have read the statements of the lemmas in steps 2 to 6, not their proofs. The hypothesis `IsGraded` is used only in step 6. The equation in step 5 holds for integrals, not for forms.
