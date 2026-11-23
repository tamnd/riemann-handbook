---
id: hecke-weight-two-of-fe
title: The Hilbert Eisenstein series of weight 2, from the functional equation of partial zeta functions
kind: theorem
decl: GlobalTheory.HeckeTwo.heckeWeightTwo_of_fe
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.HeckeWeightTwoContinuationOfFunctionalEquation
covers: 428
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement `HeckeWeightTwo` from the functional equation of the partial zeta functions of a totally real field. Its second name is [the weight 2 continuation from the functional equation](/entry/hecke-weight-two-continuation-of-functional-equation/). That entry is below [the join of the five inputs](/entry/join-out-of-five/).

## Statement

Let $F$ be a totally real field of degree $n$, with discriminant $d_F$, different $\mathfrak d$ and real embeddings $\tau_1, \dots, \tau_n$. A *partial zeta function* of an ideal class $C$ is a function $Z$, holomorphic on $\mathbb C \setminus \{1\}$, with $Z(s) = \sum_{J \in C} N(J)^{-s}$ for $\operatorname{Re} s > 1$ (integral ideals $J$).

**Hypothesis (FE).** If $C C' = [\mathfrak d]$, there are partial zeta functions $Z$ of $C$ and $Z'$ of $C'$ with $d_F^{s/2}\,\Gamma_{\mathbb R}(s)^n Z(s) = d_F^{(1-s)/2}\,\Gamma_{\mathbb R}(1-s)^n Z'(1-s)$ for all $s$ with $s, 1-s \notin \{0, -2, -4, \dots\}$. This is Hecke's functional equation for the zeta function of an ideal class (Neukirch, *Algebraic Number Theory*, Chapter VII, §5).

**Theorem.** Assume FE. Let $n \geq 2$ and let $\mathfrak a, \mathfrak b$ be fractional ideals. For $\operatorname{Re}\sigma > 0$ and $z \in \mathfrak H^n$ put

$$E(\sigma, z) = \sum_{(c,d)} \ell(z)^{-2}\,\lvert \ell(z)\rvert^{-2\sigma}, \qquad \ell(z) = \prod_{i} 2\pi i(\tau_i c + \tau_i d\, z_i),$$

over the nonzero $(c, d) \in \mathfrak d^{-1}\mathfrak a^{-1} \times \mathfrak b$ modulo the diagonal action of the units. Then there is a function $G(\sigma, z)$ with:

1. $G = E$ for $\operatorname{Re}\sigma > 0$, where $E$ converges;
2. for $\operatorname{Re}\sigma > -\tfrac12$, $G(\sigma, \cdot)$ is smooth on $\mathfrak H^n$, and each iterated Wirtinger derivative in $z$ is holomorphic in $\sigma$;
3. $G(0, \cdot)$ is holomorphic on $\mathfrak H^n$;
4. for a partial zeta function $Z_{\mathfrak a}$ of $[\mathfrak a]^{-1}$ and $\omega = d_F^{1/2} N\mathfrak a$,
$$\frac{d_F^{1/2}\, G(0,z)}{\omega^2} = 2^{-n} Z_{\mathfrak a}(-1) + \sum_{(\alpha, \beta)} \frac{|N\alpha|}{N\mathfrak a}\, e^{2\pi i \sum_i \tau_i(\alpha\beta) z_i},$$
over $(\alpha, \beta) \in \mathfrak a \times \mathfrak b$ with $\alpha\beta \gg 0$, modulo $(\alpha, \beta) \sim (\varepsilon^{-1}\alpha, \varepsilon\beta)$ for units $\varepsilon$.

So $G(0, \cdot)$ has the Fourier expansion of a holomorphic Hilbert Eisenstein series of parallel weight 2. The statement does not say that $G(0, \cdot)$ is modular.

## Proof

The function is $G = A + B_0 + k(\sigma)\,\omega\, B_1$ (Lean `gFun`), with $k(\sigma) = \bigl((2\pi i)^{-2}(2\pi)^{-2\sigma}\bigr)^n$. $A(\sigma)$ is the sum of the terms with $d = 0$. $B_0$ is a multiple of $Z_{\mathfrak b}(1 + 2\sigma) \prod_i (\operatorname{Im} z_i)^{-1-2\sigma}$, with $Z_{\mathfrak b}$ a partial zeta function of $[\mathfrak b]^{-1}$. $B_1$ holds the other Fourier terms.

1. FE for $[\mathfrak b]^{-1}$ and `partialZeta_totallyReal_at_most_simple_pole` give $Z_{\mathfrak b}(s) = R(s)/(s-1)$ with $R$ entire.
2. `heckeWeightTwoContinuation_eq_latticeSeries` gives property 1.
3. Property 2 holds for each part: `heckeEisensteinConstantTermPart_differentiableOn` for $A$, `heckeEisensteinZeroFrequencyPart_isSmoothHolomorphic` for $B_0$ (the only use of $n \geq 2$ and of the pole), `heckeEisensteinNonconstantFourierSum_smoothHolomorphic` for $B_1$.
4. $B_0(0, z) = 0$. `heckeEisenstein_weight_two_qExpansion` turns $k(0)\,\omega\,B_1(0, z)$ into the $q$-series, and `differentiableOn_hilbertEisensteinWeightTwoSeries` makes it holomorphic. This gives property 3.
5. FE for $[\mathfrak d][\mathfrak a]$ and $[\mathfrak a]^{-1}$, with `heckeWeightTwo_constantTerm_eq_partialZeta_neg_one`, turns $A(0)$ into $2^{-n} Z_{\mathfrak a}(-1)$. This gives property 4.

The rest is bookkeeping.

## In the Lean code

The theorem is at [HeckeWeightTwoContinuationOfFunctionalEquation.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HeckeWeightTwoContinuationOfFunctionalEquation.lean#L22). `HeckeWeightTwo` and its parts are in [OmegaFactorization.lean](lean:Development/AbelianVarietyTheory/BlockTheory/DivisorBase/OmegaFactorization.lean#L131). FE is `Published.PartialZetaFunctionalEquation` in [PartialZetaFunctionalEquation.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/PartialZetaFunctionalEquation.lean#L11).

- The eight lemmas above are one-line wrappers in `GlobalTheory.T`. We have not opened their proofs.
- `bZero` in [KFacDifferentiable.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KFacDifferentiable.lean#L47) is set to $0$ at $\sigma = 0$ by an `if`. Elsewhere it has the factor $c(\sigma)^n$ with $c(\sigma) = \int_{\mathbb R} (t+i)^{-2}\lvert t+i\rvert^{-2\sigma}\,dt$ (`cConst`), and $c(0) = 0$. For $n \geq 2$ this cancels the pole of $Z_{\mathfrak b}(1+2\sigma)$, and the lemma for $B_0$ shows that $0$ is the right value.
- The factor $d_F^{1/2}$ in property 4 is the Lean constant `cK F 2`.
