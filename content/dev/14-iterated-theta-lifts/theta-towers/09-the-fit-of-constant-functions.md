---
title: The joined estimates and the fit of constant functions
decls:
  - GlobalTheory.SqTop.square_top_term_joined_estimates
  - GlobalTheory.T.square_leading_term_bound
  - GlobalTheory.BigTop.Fun.Close.fittedFunction_at_zero_close_alt
  - GlobalTheory.BigTop.Fun.Close.fourier_coefficient_fit_of_join_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The joined estimates and the fit of constant functions

This section joins the results of the chapter into the bound that makes a constant function fit: an upper bound for the maximal slope of a Hermitian lattice at each point of a large family that carries a fitted grid. The proof has two parts. First, twelve estimates on Hecke $L$-values, toric values and bottom pairs are proved together at large scale, from the functional equation of Hecke $L$-functions, the norms of [Section 3.8.4](/entry/norm-big-alt/) and the local inputs. Second, these estimates, the five row properties of [Section 3.6.6](/entry/theta-lift-row-properties-conj/) and the separation of rows of [Section 3.7.8](/entry/functionals-separate-of-howe-unram-of-siegel-weil/) give sixteen leaf bounds, which one lemma joins into the slope bound. The result is the end of the third item of the step [the hypotheses are not empty](/step/nonempty-hyps/).

We fix the local inputs of [ThetaLocalInputs](/step/theta-local-inputs-def/) and keep the notation of Section 8. "At large scale" has the meaning of Section 8: there is $C_{F,0}$ such that for all $\varepsilon$ and $C_F \ge C_{F,0}$ there are $C_0$ and $x_0$ such that the statement holds for all $C \ge C_0$, all data $D$ with size data $L$ of exponent $\varepsilon$, $x \ge x_0$ and the size record of $L$, all good level characters with base point $\mu_0$ and all grids at the constants $(1, C_F, b)$. The size record asks, among other things, that $F$ is the maximal real subfield of the CM field $E$ of $D$.

**Theorem 3.9.1 (Functional equation of Hecke $L$-functions).** Let $E$ be a CM field with a CM type $\Phi$, and let $\chi$ be a unitary Hecke character of $E$ with infinity type $n \neq 0$ with respect to $\Phi$ and conductor exponents $a$. Then there are completed $L$-functions $\Lambda$ of $\chi$ and $\Lambda'$ of $\chi^{-1}$ such that

$$\Lambda(s) = \varepsilon_\infty(n)\, \varepsilon_f(\chi, a, s)\, \Lambda'(1 - s)$$

for all $s \in \mathbb C$, with explicit archimedean and finite factors.

This is the functional equation of E. Hecke, *Eine neue Art von Zetafunktionen und ihre Beziehungen zur Verteilung der Primzahlen*, Math. Z. 1 (1918) and 6 (1920), in the form of J. Tate's thesis, *Fourier analysis in number fields and Hecke's zeta-functions* (1950), in Cassels and Fröhlich, *Algebraic Number Theory* (1967); see [Tate's thesis](/learn/class-field-theory/#tates-thesis-and-hecke-l-functions). A lemma turns it into the form we use: for all completed $L$-functions $\Lambda$ of $\chi$ and $\Lambda'$ of $\chi^{-1}$ there is $\varepsilon$ with $|\varepsilon| = 1$ and

$$\Lambda(s) = \varepsilon\, \bigl(|d_E|\, N(\mathfrak a)\bigr)^{1/2 - s}\, \Lambda'(1 - s),$$

where $d_E$ is the discriminant and $\mathfrak a$ the ideal of the exponents $a$.

We also use four inputs of other chapters, which we do not unfold: a bound on toric denominators, the transport of lattice norms, the twisted transport of toric ratios and the denominators of zeta values. The fifth input, the reflection condition, says that at large scale, for $1 - e_0 \le s \le 0$,

$$\Lambda(s)\, \Lambda_0(1 - s) = \epsilon\, \Lambda(1 - s)\, \Lambda_0(s)$$

for the $L$-functions of the bottom stages, with $\epsilon$ a unit away from the level. Howe duality at the real places is part of the local inputs: the polynomial Fock space at the real places has finite length as a module for the dual pair, and the sum of two proper theta submodules is proper. This is the archimedean Howe duality of R. Howe, *Transcending classical invariant theory*, J. Amer. Math. Soc. 2 (1989).

**Definition 3.9.2 (The twelve estimates).** Put $b_{TH} = C f b (\log b + \log x)$. The twelve estimates are these statements at large scale.

1. Field data: $E$ is CM and abelian over $\mathbb Q$, with field data and an integral lattice.
2. Nonvanishing of $L$-values ($\mathrm{LNe}$ of Section 8): the $L$-functions of the characters $\nu_t$ of the bottom stages have no zero at the integers $s$ with $1 - e_0 \le s \le h$, and those of a family of twists have no zero at the integers $s \ge 1$.
3. Toric values: each such value $\Lambda(s)$ is a nonzero toric value whose period normalization is algebraic.
4. Denominators: each toric value has a denominator function $n$ with finite support on the primes.
5. Sum of denominators: $\sum_{l \in S} n(l) \log l \le b_{TH}$.
6. Heights: the toric values have height at most $b_{TH}$.
7. Small bottom: the small bottom condition of Section 8.
8. Bottom pairs exist.
9. Bottom pairs are nonzero: they have a nonzero coordinate.
10. Bottom triangles with constant coefficients exist.
11. Square ratios: the valuations of each square ratio are bounded at each place.
12. Tower: a quotient of products of $L$-values is a unit away from the level times a product of step ratios.

We have not unfolded the toric values, the square ratios or the step ratios.

**Theorem 3.9.3 (Joined estimates).** Assume Howe duality at the real places, the local inputs, the functional equation of Hecke $L$-functions in the absolute value form, the four inputs above, the reflection condition, the agreement of theta integrals [ThetaIntegralsAgree](/step/theta-integrals-agree-def/) and the [local matching](/step/local-matching-def/). Then the twelve estimates hold.

Lean: `GlobalTheory.SqTop.square_top_term_joined_estimates` (also `GlobalTheory.T.square_leading_term_bound`, a second name).

*Proof.* We prove the estimates in an order where each uses only earlier ones.

1. Completed Hecke $L$-functions are bounded in vertical strips, the record of facts $\mathrm{Inp}(D)$ holds for each $D$, and the field data hold; these three facts have no hypothesis.
2. The functional equation, the bound in vertical strips and the field data give $\mathrm{LNe}$, and an upper bound for the $L$-values at permuted weights.
3. The transport of lattice norms gives the toric values, and with the upper bound a bound on the archimedean means of the period normalizations. The denominators of zeta values give the denominators and their sum. The bound on toric denominators then gives the heights, and also a lower bound for ratios of $L$-values.
4. The small bottom condition holds. The record $\mathrm{Inp}$ gives bottom pairs at a base tuple and at every tuple.
5. The local inputs, the agreement of theta integrals, the local matching, the small bottom condition and $\mathrm{LNe}$ give constant bottom coefficients, the tower, and, with Howe duality at the real places, the bottom triangles.
6. [The norm of the large member](/entry/norm-big-alt/) follows from $\mathrm{LNe}$.
7. Bottom pairs are nonzero. The proof uses the [bottom formula](/entry/rallis-bottom-formula-large-rank/), the bottom triangles, and the fact that the norm of the large member is not zero, which follows from the norm theorem and $\mathrm{LNe}$.
8. The bound on square ratios combines eleven of these facts with the reflection condition and the lower bound for ratios of $L$-values. $\square$

The second part needs the notion of a fit. A family of points is a family in the class of families of the closed bound; this class is a conjunction of conditions that we have not unfolded. Each point $p$ at $(x, i)$ has a side datum with a number field $K$, a glued $\mathcal O_K$-lattice $R_p$ with metrics at the infinite places, a positive function $\kappa_p$ on the infinite places, and a scale $(x_p, b_p)$. We write $\mu_{\max}$ for the [maximal slope](/learn/arakelov/#hermitian-lattices-and-slopes), $\ell_K$ for the logarithm of the discriminant of $K$ and $n_K$ for its number of infinite places; we have not unfolded them.

**Definition 3.9.4 (Constant functions fit).** Constant functions fit if there is $C_{F,0}$ such that for each $C_F \ge C_{F,0}$ the following statement is [closed](/step/closed-def/) in the class of families, as a statement about a family $F$ and an exponent $C_H$. If $F$ meets the divisor condition, there is $x_0$ such that for each $x \ge x_0$, each index $i$ and each point $p$ of $F$ at $(x, i)$ with the point conditions, the following holds: if $p$ has a grid $G$ at level $C_F$ with a Weil datum $W$ over the real data of $p$, the grid fits $p$, and the remaining choices of the slope test exist at $(p, C_F, G, W)$, then

$$\begin{aligned} 2\,\mu_{\max}(R_p) &- \log 2 + \frac{\ell_K}{[K : \mathbb Q]} \\ &\le x_p^{C_H}\, b_p - \frac{1}{n_K} \sum_{v \mid \infty} \log \kappa_p(v). \end{aligned}$$

**Theorem 3.9.5 (Slope bound at fitted points).** Assume the local inputs, the functional equation of Hecke $L$-functions in the absolute value form, the four inputs above, the reflection condition, the agreement of theta integrals, the local matching, the separation of rows by real functionals, and the lower bound for $\Lambda$ along the families. Then constant functions fit.

Lean: `GlobalTheory.BigTop.Fun.Close.fittedFunction_at_zero_close_alt`.

*Proof.* We collect the inputs of the sixteen leaves.

1. [Theorem 3.9.3](/entry/square-top-term-joined-estimates/) gives the twelve estimates, with Howe duality at the real places taken from the local inputs.
2. A lemma gives bounds on the sums of sizes at the finite places, away from the level and at the infinite places.
3. The local inputs, the agreement of theta integrals and the local matching give the five row properties of Section 6.
4. The separation of rows and the convergence of the twisted lifts at the real places give an injectivity statement.
5. Along the families, the logarithmic derivative of the $L$-function at $1$ is at most $x^{\varepsilon}$. With the twisted transport this gives a bound on toric ratios, and with the row properties it puts each square ratio in the image of an embedding of a number field.

Each of the sixteen leaf bounds then follows from a few of these facts. For example, the fixed point leaf uses the bounds at the finite places and away from the level, the height map leaf uses the bound at the infinite places, and the leaf at the infinite places is the one use of the lower bound for $\Lambda$. Several leaves have no hypothesis: the bundle condition, a scaling bound, a rank gap bound, a ramified sum bound and a polynomial descent bound. One lemma joins the sixteen leaves and proves the slope inequality for one side datum from the leaf bounds. $\square$

**Theorem 3.9.6 (Constant functions fit).** Assume the local inputs, the four inputs above and the reflection condition, the functional equation of Hecke $L$-functions, the agreement of theta integrals, the local matching, the separation of rows by real functionals, and the lower bound for $\Lambda$ along the families. Then constant functions fit.

Lean: `GlobalTheory.BigTop.Fun.Close.fourier_coefficient_fit_of_join_alt`.

*Proof.* The functional equation gives its absolute value form. Then [Theorem 3.9.5](/entry/fitted-function-at-zero-close-alt/) applies. $\square$

**Remark 3.9.7 (Formalization).** In the top theorem the four inputs and the reflection condition come as one conjunction, which the proof splits. The name of the top theorem speaks of a Fourier coefficient, but none appears in it ([FourierCoefficientFitOfJoin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FourierCoefficientFitOfJoin.lean#L12)). In the slope bound ([FittedFunctionAtZeroClose.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FittedFunctionAtZeroClose.lean#L42)) the conclusion holds for every real $C$, but the inequality does not depend on $C$; the words "at zero" and "close" match nothing in the statement. In the joined estimates ([SquareTopTermJoinedEstimates.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/SquareTopTermJoinedEstimates.lean#L13)) Howe duality at the real places is a hypothesis although it is a field of the local inputs, and it is used only for the bottom triangles. The reflection condition looks like a consequence of the functional equation, but it is assumed, not derived. The small bottom condition is proved with no hypothesis. We have not opened the sixteen leaf lemmas or the joining lemma.
