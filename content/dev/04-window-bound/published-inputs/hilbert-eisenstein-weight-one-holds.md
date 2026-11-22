---
id: hilbert-eisenstein-weight-one-holds
title: The Hilbert Eisenstein series of weight one
kind: theorem
decl: UpperTheory.V.Published.hilbert_eisenstein_weight_one_holds
module: PositivityTheory.AutomorphicForms.PublishedInputs.HilbertEisenstein.HilbertEisensteinWeightOneHolds
covers: 921
status: drafted
drafted_by: writer@claude
---
This theorem makes, for a ramified totally odd character $\omega$ of finite order of a totally real field, a holomorphic Hilbert modular form of parallel weight one whose Fourier coefficients are the divisor sums $\sum_{\mathfrak{r} \mid \mathfrak{m}} \omega(\mathfrak{r})$. It fills the field `eis` of the hypotheses `Hypotheses4Z'` that [the case II seed](/entry/seed-iis-alt/) builds.

## Statement

Let $F$ be totally real and $\omega$ a Hecke character of $F$ of finite order with $\omega_v(-1) = -1$ at each real place $v$. Let $c(w)$ be the conductor exponent of $\omega$ at each finite place $w$ (`IsCondAt`), and suppose $c(w) \neq 0$ for some $w$. For an ideal $\mathfrak{r}$ let $\omega(\mathfrak{r}) = \prod_w \omega(\varpi_w)^{\operatorname{ord}_w \mathfrak{r}}$, with the factor $0$ at places where $\omega$ ramifies (`chiI`).

**Theorem** (`HilbertEisOne`). There are an automorphic form $\varphi$ on $\mathrm{GL}_2(\mathbb{A}_F)$ and $L \in \mathbb{C}$ such that:

1. $\varphi$ is holomorphic of parallel weight 1, fixed by $K_1(\varpi_w^{c(w)})$ at each $w$, with central character $\omega$ (`IsHol 1 c ω φ`);
2. for $x \in \mathbb{R}^n$, $y \in \mathbb{R}_{>0}^n$ and a finite idele $y_f$,
$$\frac{\varphi\!\left(\begin{pmatrix} y & x \\ 0 & 1\end{pmatrix}_{\!\infty} \begin{pmatrix} y_f & 0 \\ 0 & 1\end{pmatrix}_{\!f}\right)}{(N(y)\,|y_f|)^{1/2}} - L = \sum_{\xi \gg 0} a(\xi y_f \mathfrak{d})\, e^{2\pi i \operatorname{Tr} \xi (x + iy)},$$
where $\mathfrak{d}$ is the different, $a(\mathfrak{m}) = \sum_{\mathfrak{r} \mid \mathfrak{m}} \omega(\mathfrak{r})$ when $\mathfrak{m} = \xi y_f \mathfrak{d}$ is a nonzero integral ideal, and the term is $0$ otherwise (`HasExp`).

This is the weight one Eisenstein series attached to the pair of characters $(1, \omega)$. Eisenstein series of this kind for Hilbert modular forms are in Shimura (Duke Math. J. 45, 1978).

## Proof

The form is $\varphi = C_0^{-1} E$, where $E = $ `Eis ω (Phi c)` is a theta integral:
$$E(g) = |\det g|^{1/2} \int_{\mathbb{R}_{>0}} \int_{F^\times \backslash \mathbb{A}^1} \sum_{\xi \in F^2 \setminus 0} \Phi(\xi\, t u g)\, \omega(tu)^{-1}\, t \; du\, dt.$$
Here $\Phi$ (`Phi c`) is $\prod_v (x_v + i y_v) e^{-\pi(x_v^2 + y_v^2)}$ at the real places times the indicator of $\{(\xi_0, \xi_1) : \xi_0 \in \varpi^c,\ \xi_1 \in 1 + \varpi^c\}$ at the finite places.

The assembly `top` takes 14 facts. Poisson summation `SPois` is `poisson_summation_holds`; integrability `SInt` (`s_integrality`) and smoothness (`smoothness_holds`) follow from it, and the other facts are stated under these three:

- $E$ is of moderate growth, left invariant under $\mathrm{GL}_2(F)$, $K$-finite and $Z$-finite, with open stabilizer;
- the level, central character, weight 1 and the second Lie algebra equation `low` (`level_holds`, `central_character_holds`, `weight_holds`, `low_weight_holds`);
- the Fourier expansion [`fourier_expansion_holds`](/entry/fourier-expansion-holds/), with a constant $C_0 \neq 0$ in front of the divisor sums;
- `scalar_action_holds`: scaling by $C_0^{-1}$ keeps these properties.

## In the Lean code

The theorem is in [HilbertEisensteinWeightOneHolds.lean](lean:PositivityTheory/AutomorphicForms/PublishedInputs/HilbertEisenstein/HilbertEisensteinWeightOneHolds.lean#L19). `HilbertEisOne` is in [Hilbert.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/PublishedTheorems/Hilbert.lean#L13), `top` in [ImportsAlt.lean](lean:PositivityTheory/AutomorphicForms/PublishedInputs/HilbertEisenstein/ImportsAlt.lean#L12), and `Eis` and `Phi` in [SSmooth.lean](lean:PositivityTheory/AutomorphicForms/PublishedInputs/HilbertEisenstein/SSmooth.lean#L29). `IsHol` and `HasExp` are in [IsCondAt.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/IdeleGenerators/IsCondAt.lean#L81). We have not unfolded `TR.IsAutForm` or the Lie algebra operators `Eop`.

The constant term $L$ does not depend on $y_f$. In the proof it is the integral of the terms $\xi = (0, b)$, which do not depend on $g$. The file holding `s_integrality` is named `InvMulVecScalarMul.lean`, which does not describe it.
