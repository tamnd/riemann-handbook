---
id: hecke-weight-two-continuation-of-functional-equation
title: The Hilbert Eisenstein series of weight two, from the functional equation of partial zeta functions (statement)
kind: theorem
decl: GlobalTheory.T.heckeWeightTwoContinuation_of_functionalEquation
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.HeckeWeightTwoContinuationOfFunctionalEquationStatement
covers: 429
status: drafted
drafted_by: writer@claude
---
This theorem says that the functional equation of partial zeta functions implies `HeckeWeightTwo`: the Hilbert Eisenstein series of weight two continues in Hecke's parameter $\sigma$, is holomorphic at $\sigma = 0$, and has the expected $q$-expansion. It restates [`HeckeTwo.heckeWeightTwo_of_fe`](/entry/hecke-weight-two-of-fe/), which has the proof. Four lemmas below [`joinOut_of_five`](/entry/join-out-of-five/) use it (`jetInt`, `latAlg_of_siegelKlingen`, `latConj`, `joinOut_of_jetInt`), each to turn `PartialZetaFunctionalEquation` into `HeckeWeightTwo`.

## Statement

Let $F$ be a totally real field of degree $n$, with discriminant $d_F$ and different $\mathfrak{d}$. A partial zeta function for an ideal class $C$ (`IsPartialZeta C Z`) is a function $Z$, holomorphic on $\mathbb{C} \setminus \{1\}$, with $Z(s) = \sum_{J \in C} N(J)^{-s}$ for $\operatorname{Re} s > 1$, the sum over integral ideals $J$.

`PartialZetaFunctionalEquation` says: for $C C' = [\mathfrak{d}]$ there are partial zeta functions $Z$ for $C$ and $Z'$ for $C'$ with
$$|d_F|^{s/2}\, \Gamma_{\mathbb{R}}(s)^n Z(s) = |d_F|^{(1-s)/2}\, \Gamma_{\mathbb{R}}(1-s)^n Z'(1-s)$$
for $s, 1-s \notin \{0, -2, -4, \dots\}$. This is Hecke's functional equation for partial zeta functions (Neukirch, *Algebraic Number Theory*, Springer 1999, Chapter VII, §5).

For fractional ideals $\mathfrak{a}, \mathfrak{b}$, $z \in \mathfrak{H}^n$ and $\operatorname{Re}\sigma > 0$, let
$$E(\sigma, z) = \sum_{(d, c)} N(d + cz)^{-2}\, |N(d + cz)|^{-2\sigma}, \qquad N(d + cz) = \prod_\tau 2\pi i\,(\tau(d) + \tau(c) z_\tau),$$
the sum over nonzero $(d, c) \in \mathfrak{d}^{-1}\mathfrak{a}^{-1} \times \mathfrak{b}$ modulo the units of $\mathcal{O}_F$ (`eisSum 𝔞 𝔟 2`).

`HeckeWeightTwo` says: if $n \geq 2$, then for all $\mathfrak{a}, \mathfrak{b}$ there is $G(\sigma, z)$ with

1. for $\operatorname{Re}\sigma > 0$ the series converges and $G(\sigma, z) = E(\sigma, z)$;
2. for $\operatorname{Re}\sigma > -\tfrac12$, $G(\sigma, \cdot)$ is $C^\infty$ on $\mathfrak{H}^n$, and each iterated derivative in the $z_\tau$ and $\bar z_\tau$ is holomorphic in $\sigma$;
3. $G(0, \cdot)$ is holomorphic on $\mathfrak{H}^n$;
4. with a partial zeta function $Z$ for the class of $\mathfrak{a}^{-1}$, $\omega = |d_F|^{1/2} N\mathfrak{a}$ and $c_2 = |d_F|^{1/2}$,
$$\frac{c_2\, G(0, z)}{\omega^2} = 2^{-n} Z(-1) + \sum_{(a, b)} \frac{|N(a)|}{N\mathfrak{a}}\, e^{2\pi i \operatorname{Tr}(abz)},$$
the sum over $(a, b) \in \mathfrak{a} \times \mathfrak{b}$ with $ab \gg 0$, modulo $(a, b) \sim (\varepsilon^{-1}a, \varepsilon b)$.

**Theorem.** `PartialZetaFunctionalEquation` implies `HeckeWeightTwo`.

The method of adding $|N(cz+d)|^{-2\sigma}$ and letting $\sigma \to 0$ is Hecke's (E. Hecke, Abh. Math. Sem. Hamburg 3 (1924)). We have not checked the constants against that source.

## Proof

The proof is `HeckeTwo.heckeWeightTwo_of_fe`. It splits $E$ into the terms with $c = 0$, the zero Fourier mode of the other terms, and their other modes, and continues each part.

## In the Lean code

The theorem is in [HeckeWeightTwoContinuationOfFunctionalEquationStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HeckeWeightTwoContinuationOfFunctionalEquationStatement.lean#L6). The proof is `first | exact @GlobalTheory.HeckeTwo.heckeWeightTwo_of_fe | ...`; the two statements are identical. `HeckeWeightTwo`, `IsContinuation` and `HasExpansion` are in [OmegaFactorization.lean](lean:Development/AbelianVarietyTheory/BlockTheory/DivisorBase/OmegaFactorization.lean#L131), and `PartialZetaFunctionalEquation` is in [PartialZetaFunctionalEquation.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/PartialZetaFunctionalEquation.lean#L11).

- The hypothesis $n \geq 2$ is necessary: for $F = \mathbb{Q}$ the limit at $\sigma = 0$ is a multiple of $E_2(z) - 3/(\pi y)$, which is not holomorphic (D. Zagier, in *The 1-2-3 of Modular Forms*, Springer 2008, Section 2). In the proof it goes only to the lemma for the zero Fourier mode, `heckeEisensteinZeroFrequencyPart_isSmoothHolomorphic`.
- The lattice $\mathfrak{d}^{-1}\mathfrak{a}^{-1}$ is `latM 𝔞`; `latM_eq_dual` proves that it is the trace dual of $\mathfrak{a}$.
