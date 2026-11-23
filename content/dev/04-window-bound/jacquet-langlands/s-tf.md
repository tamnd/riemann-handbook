---
id: s-tf
title: A trace formula with only elliptic terms
kind: theorem
decl: UpperTheory.Esk.s_TF
module: PositivityTheory.AutomorphicForms.PublishedInputs.JacquetLanglands.TorusKernels.FinalTF
covers: 525
status: drafted
drafted_by: writer@claude
---
This theorem is a trace formula for Hecke operators on holomorphic forms of a datum $D$: the trace is a finite sum of elliptic orbital terms. The set of terms does not depend on the weight. [The five-input weight congruence](/entry/hol-wc-of/) uses this to compare traces in two weights.

## Statement

A datum $D$ (`Dat F I Gf`) has a field $F$, real embeddings $\sigma_v$ for $v \in I$, a group $G_f$ with a map $j \colon \mathrm{GL}_2(F) \to G_f$, a subgroup $H$ with a character $\chi$, and a height function. Let $X = (\mathbb{C} \setminus \mathbb{R})^I$ and $\Omega = G_f / H$. For a weight $k \colon I \to \mathbb{N}$, a form is a function $f$ on $X \times G_f$ that is holomorphic in $z$, with $f(\gamma z, j(\gamma) x) = J_k(\gamma, z) f(z, x)$, $f(z, xh) = \chi(h) f(z, x)$ and $|f(z,x)| \prod_v |\operatorname{Im} z_v|^{k_v/2}$ bounded. Let $M_k$ be their span. For $a = (a_i)$ in $G_f$, let $T_a f(z, x) = \sum_i f(z, x a_i)$.

**Theorem** (`TF`). Let $D$ meet the axioms `Ax` and fix $a$. There is a finite set $S$ of pairs $(\gamma, \omega)$, with $\gamma \in \mathrm{PGL}_2(F)$ elliptic at every $\sigma_v$ ($\sigma_v(\operatorname{tr}\gamma)^2 < 4\sigma_v(\det\gamma)$) and $\omega \in \Omega$ with finite stabilizer $\Gamma_{\gamma,\omega}$, such that for each $k$ with `Hyp k a`, if $M_k$ has finite dimension and $T_a$ preserves it, then
$$\operatorname{tr}(T_a \mid M_k) = \sum_{(\gamma,\omega) \in S} \frac{1}{|\Gamma_{\gamma,\omega}|}\, \mathrm{Te}_a(\gamma, \omega) \prod_{v \in I} -\frac{\rho_v^{k_v-1} - \bar\rho_v^{k_v-1}}{\rho_v - \bar\rho_v}\, \sigma_v(\det\gamma)^{1 - k_v/2}.$$
Here $\rho_v, \bar\rho_v$ are the roots of $X^2 - \sigma_v(\operatorname{tr}\gamma) X + \sigma_v(\det\gamma)$ (the Lean code uses the recursion `ch`), and $\mathrm{Te}_a(\gamma, \omega) = \sum_i \chi^0(x^{-1} j(\gamma)^{-1} x a_i)$ with $x$ a representative of $\omega$ and $\chi^0$ the extension of $\chi$ by zero. `Hyp` asks that $k_v \geq 4$, signs are compatible, and $a$ is `Good` and `Reg`.

The product has the shape of the elliptic terms of the Eichler-Selberg trace formula (Zagier, appendix to Lang, *Introduction to Modular Forms*, 1976). We do not claim that the Lean statement is a given published form.

## Proof

`pf_TF` combines five facts, all for a cut-off function $b$ (`IsCut`, not unfolded) that plays the role of a fundamental domain.

1. `linear_trace_identity_holds` (`E6`): the trace equals $\int b(y) \sum_{\gamma \in \mathrm{PGL}_2(F)} k_\gamma(y)\, dy$ for the kernel `kk`.
2. `kernel_sum_bounded_holds` (`E2`): the sum over $\gamma$ converges absolutely, so it splits into elliptic and non-elliptic $\gamma$ (`IsEll`: no eigenvector in $F^2$).
3. `s_Fell` (`Fell`): the elliptic part integrates to the sum over $S$ above.
4. `s_Fhyp` (`Fhyp`): the non-elliptic part integrates to zero.
5. `s_Ecut` (`Ecut`): a cut-off function exists.

So the identity, hyperbolic and parabolic terms all vanish. We have not unfolded `pf_Fell` or `pf_Fhyp`.

## In the Lean code

The theorem is in [FinalTF.lean](lean:PositivityTheory/AutomorphicForms/PublishedInputs/JacquetLanglands/TorusKernels/FinalTF.lean#L92); `TF` is in [MultivariableReproducingFormula.lean](lean:PositivityTheory/AutomorphicForms/PublishedInputs/JacquetLanglands/TorusKernels/MultivariableReproducingFormula.lean#L360), and `pf_TF` is in [SplitTsum.lean](lean:PositivityTheory/AutomorphicForms/PublishedInputs/JacquetLanglands/TorusKernels/SplitTsum.lean#L21).

- `Fhyp` covers all non-elliptic elements, central and parabolic ones too, not only hyperbolic ones.
- `Fell` puts only totally elliptic elements in $S$. Elements elliptic over $F$ but split at some $\sigma_v$ give no term.
- `kernel_inverse_symmetry_holds` proves a statement named `faceMap_zero_comp_eq_one`, which is about the summability, measurability and a bound of the kernel `Kern`. Neither name describes it.
