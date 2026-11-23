---
id: fourier-expansion-holds
title: The Fourier expansion of the weight one Eisenstein series
kind: theorem
decl: UpperTheory.HilbertEisensteinWeightOne.fourier_expansion_holds
module: PositivityTheory.AutomorphicForms.PublishedInputs.HilbertEisenstein.FourierExpansionHolds
covers: 443
status: drafted
drafted_by: writer@claude
---
This theorem computes the Fourier expansion of the theta integral $E = $ `Eis ω (Phi c)`: up to a nonzero constant, its coefficients are the divisor sums $\sum_{\mathfrak{r} \mid \mathfrak{m}} \omega(\mathfrak{r})$. It is the input `hE` of the assembly in [the weight one Eisenstein series](/entry/hilbert-eisenstein-weight-one-holds/), which defines $E$, $\Phi$ and the character $\omega(\mathfrak{r})$.

## Statement

**Theorem.** Assume Poisson summation `SPois` and integrability `SInt`. Let $\omega$ and $c$ be as in [the weight one Eisenstein series](/entry/hilbert-eisenstein-weight-one-holds/) (the predicate `Hyp ω c`). Then there are $C_0 \neq 0$ and $L$ such that $E$ has the expansion `HasExp E 1 (fun _ => L) a` with
$$a(\mathfrak{m}) = C_0 \sum_{\mathfrak{r} \mid \mathfrak{m}} \omega(\mathfrak{r}).$$

## Proof

Write $g = \begin{pmatrix} y & x \\ 0 & 1 \end{pmatrix}_\infty \begin{pmatrix} y_f & 0 \\ 0 & 1 \end{pmatrix}_f$ and $\tau$ for the idele of the integration variable. The proof is `sExp_assembly`, with six inputs.

1. `pointwise_theta_expansion` (`SPoint`, from `SPois`). The theta sum at $\tau g$ splits into three parts: the terms $\xi = (0, b)$ with $b \in F^\times$ (`zeroRow`); the zeroth Fourier coefficient; and $\sum_{\xi \in F^\times} e^{2\pi i \operatorname{Tr} \xi x}\, \kappa(\tau, \xi)$. Here $\kappa$ (`coefK`) is a sum over $a \in F^\times$ of adelic Fourier transforms of $\Phi$ in its second variable.
2. `zero_term_holds` (`SZero`). The `zeroRow` part is integrable. It does not depend on $g$, and its integral is the constant term $L$.
3. `null_term_holds` (`SNull`). The zeroth Fourier coefficient integrates to $0$ over the norm one ideles.
4. `absolute_convergence_holds` (`SAbs`). The sum over $\xi$ converges absolutely after integration, so it can be integrated term by term.
5. `sUnfold_statement` (`SUnfold`). Each term unfolds from an integral over $\mathbb{R}_{>0} \times F^\times \backslash \mathbb{A}^1$ to an integral over all of $\mathbb{A}^\times$.
6. `local_expansion_holds` (`SLocal`). That integral is $C_0\, a(\xi y_f \mathfrak{d})\, e^{-2\pi \operatorname{Tr} \xi y}$ if $\xi$ is totally positive, and $0$ if not.

Terms with $\xi$ not totally positive drop out, and $e^{2\pi i \operatorname{Tr}\xi x} e^{-2\pi \operatorname{Tr}\xi y} = e^{2\pi i \operatorname{Tr} \xi(x + iy)}$. Steps 1, 3, 4 and 6 also use `finite_expansion_holds` (the support of $c$ is finite) and `kernel_expansion_holds` (`SKern`: the Fourier transform of $\Phi$ in the second variable is a nonzero constant times an explicit kernel `kernF`).

## In the Lean code

The theorem is in [FourierExpansionHolds.lean](lean:PositivityTheory/AutomorphicForms/PublishedInputs/HilbertEisenstein/FourierExpansionHolds.lean#L258), and `sExp_assembly` is in the same file at [line 111](lean:PositivityTheory/AutomorphicForms/PublishedInputs/HilbertEisenstein/FourierExpansionHolds.lean#L111). The six statements are in [SExpDefs.lean](lean:PositivityTheory/AutomorphicForms/PublishedInputs/HilbertEisenstein/SExpDefs.lean#L66) and `SExp` is in [SSmooth.lean](lean:PositivityTheory/AutomorphicForms/PublishedInputs/HilbertEisenstein/SSmooth.lean#L112). We have not unfolded the proofs of the six inputs.

The theorem has the type `SPois → SInt → SSmooth → SExp`, but it does not use the smoothness hypothesis `SSmooth`.
