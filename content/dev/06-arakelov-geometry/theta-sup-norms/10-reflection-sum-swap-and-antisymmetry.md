---
title: The reflection sum, the swap relation and antisymmetry
decls:
  - GlobalTheory.T.antisymmetry'
  - GlobalTheory.CompanionTheory.Ar.PB.Top.antisymmetry
  - GlobalTheory.T.adjacent_swap_height_polynomial_relation
  - GlobalTheory.CompanionTheory.Ar.PB.thmA_swap
  - GlobalTheory.T.height_polynomial_reflection_sum
  - GlobalTheory.CompanionTheory.Ar.PB.thmA_limit
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The reflection sum, the swap relation and antisymmetry

This section proves that the height polynomial of a flag system is antisymmetric under the adjacent swaps, after we subtract a multiple of the height polynomial of the flag variety. The proof has three steps. A square system at $(a_0, \varepsilon)$ gives a reflection sum: the height polynomial at $c - (u/2)\varepsilon$ plus the height polynomial at $c + (u/2)\varepsilon$ is an explicit polynomial in $u$ that depends only on the degree polynomial. For an adjacent swap in weight coordinates, the two points are a weight and its swap. Two systems with proportional degree polynomials then have the same swap sums up to the factor of proportionality. The antisymmetry statement is used by the swap relation on a good tower ([the swap relation on a good tower](/entry/good-tower-antisymmetry-of/)) and so in the [proof of the Weil bound](/proof/weil-bound/). For the background we use [heights](/learn/arakelov/#heights) and [arithmetic intersection numbers](/learn/arakelov/#arithmetic-varieties-and-intersection-numbers).

### Height polynomials

Let $S$ be an analytic system of dimension $D$ indexed by a finite set $\sigma$. A realization of $S$ in an arithmetic variety consists of a log resolution, a map of degree $\deg$ onto the space of $S$, and hermitian lines $L_a(t)$ for $a \in \sigma$ and $0 < t \leq t_0$ whose metrics differ from fixed reference metrics by the regularized potentials of $S$. For a word $w = (w_1, \dots, w_{D+1})$ in $\sigma$ put
$$
\operatorname{num}_t(w) = \frac{1}{\deg} \bigl(L_{w_1}(t) \cdots L_{w_{D+1}}(t)\bigr), \qquad \operatorname{lim}(w) = \lim_{t \to 0^+} \operatorname{num}_t(w),
$$
where the product is the arithmetic intersection number of the intersection system. For a function $a$ on words of length $n$ let
$$
\operatorname{form}_n(a) = \sum_{w} a(w)\, X_{w_1} \cdots X_{w_n} .
$$
The height polynomial of the realization is $H = \operatorname{form}_{D+1}(\operatorname{lim})$, and the degree polynomial of $S$ is $\operatorname{Deg} = \operatorname{form}_D(\operatorname{deg})$ with the mixed degrees of Section 9.

For a polynomial $P$ in one variable and an integer $D$ put
$$
\operatorname{tsg}_D(P) = \sum_{n \text{ odd}} \frac{(D + 1)\, \kappa\bigl(\tfrac{n+1}{2}\bigr)}{(n+1)/2}\, P_n\, X^{n+1},
$$
where $P_n$ is the coefficient of $X^n$ in $P$ and $\kappa$ is the constant of Section 9. For $c$ real and $\varepsilon$ integral on $\sigma$ and a polynomial $Q$ on $\sigma$, the line polynomial $\operatorname{line}_{c,\varepsilon}(Q)$ is the polynomial $X \mapsto Q(c - (\varepsilon/2) X)$ in one variable.

### The reflection sum

**Theorem 10.10.1 (Reflection sum).** Assume the inputs and the fibre local statement, and let the intersection system be full. Let $S$ be an analytic system of dimension $d + 1$ with a realization, let $a_0 \in \sigma$, let $\varepsilon$ be integral on $\sigma$, and assume that there is a square system for the realization at $(a_0, \varepsilon)$. Then for every real $c$ on $\sigma$ with $c(a_0) = 0$ and every $u \in \mathbb{R}$
$$
\begin{aligned}
H\bigl(c - \tfrac{u}{2}\varepsilon\bigr) &+ H\bigl(c + \tfrac{u}{2}\varepsilon\bigr) \\
&= \operatorname{tsg}_{d+1}\bigl(\operatorname{line}_{c,\varepsilon}(\operatorname{Deg})\bigr)(u) .
\end{aligned}
$$

Lean: `GlobalTheory.CompanionTheory.Ar.PB.thmA_limit` (also `GlobalTheory.T.height_polynomial_reflection_sum`, a second name).

*Proof.* Step 1: the forms are symmetric. The intersection numbers do not change under a permutation of the lines, so $\operatorname{num}_t$ and $\operatorname{lim}$ are symmetric functions of the word. The mixed degrees are symmetric for the same reason. By the agreement theorem for positive systems, $\operatorname{num}_t(w)$ converges to $\operatorname{lim}(w)$ for every $w$.

Step 2: the polar identities at a fixed scale. Let $n$ be integral on $\sigma$ with $n(a_0) = 0$. A lemma on square systems gives, for $0 < t$ at most the scale of the square,
$$
\operatorname{pol}_{d+2}(\operatorname{num}_t)(n, \dots, n) = 0
$$
and, for $1 \leq k$ with $2k \leq d + 2$,
$$
\begin{aligned}
\operatorname{pol}_{d+2}&(\operatorname{num}_t)\bigl(\operatorname{mix}_{2k}(\varepsilon, n)\bigr) \\
&= -\sum_{i < k} \operatorname{pol}_{d+2}\Bigl(w \mapsto \int_{S_W} g_{T,t}\, \operatorname{MA}(\theta + \varphi_t)_w\Bigr)(W^{(i)}),
\end{aligned}
$$
where $\operatorname{mix}_{2k}(\varepsilon, n)$ is $2k$ copies of $\varepsilon$ followed by copies of $n$, $g_{T,t}$ is the norm function of the square at scale $t$ and $W^{(i)}$ is the sequence of coefficients of Section 9 for $c = n$.

Step 3: the limit. The polar forms are finite sums, so they converge with $\operatorname{num}_t$, and the first identity gives $\operatorname{pol}_{d+2}(\operatorname{lim})(n, \dots, n) = 0$. The regularized convergence of the square gives that the mixed integrals of the regularized potentials against $g_{T,t}$ converge to those of the singular potentials against $g_H$. By the polar identity of a square (Section 9) the limit of the right side is $-2\kappa(k)\, \operatorname{pol}_{d+1}(\operatorname{deg})(\operatorname{mix}_{2k-1}(\varepsilon, n))$. So
$$
\operatorname{pol}_{d+2}(\operatorname{lim})\bigl(\operatorname{mix}_{2k}(\varepsilon, n)\bigr) = -2\kappa(k)\, \operatorname{pol}_{d+1}(\operatorname{deg})\bigl(\operatorname{mix}_{2k-1}(\varepsilon, n)\bigr) .
$$

Step 4: from polar identities to the reflection sum. Write $A$ and $B$ for the symmetric multilinear forms of $\operatorname{lim}$ and $\operatorname{deg}$, so that $H(x) = A(x, \dots, x)$ and $\operatorname{Deg}(x) = B(x, \dots, x)$, and let $D = d + 1$. The identities of Step 3 hold for integral $n$ with $n(a_0) = 0$, and so by multilinearity for real $c$ with $c(a_0) = 0$. By the binomial formula,
$$
H\bigl(c - \tfrac{u}{2}\varepsilon\bigr) + H\bigl(c + \tfrac{u}{2}\varepsilon\bigr) = 2 \sum_{m \text{ even}} \binom{D+1}{m} \Bigl(\frac{u}{2}\Bigr)^{m} A(\varepsilon^{m}, c^{D+1-m}) .
$$
The term $m = 0$ is $0$ by the first identity. For $m = 2k$ the second identity gives
$$
2 \binom{D+1}{2k} \Bigl(\frac{u}{2}\Bigr)^{2k} A(\varepsilon^{2k}, c^{D+1-2k}) = -\frac{4\kappa(k)}{2^{2k}} \binom{D+1}{2k} B(\varepsilon^{2k-1}, c^{D+1-2k})\, u^{2k} .
$$
On the other side, the coefficient of $X^{2k-1}$ in $\operatorname{line}_{c,\varepsilon}(\operatorname{Deg})$ is $\binom{D}{2k-1} (-1/2)^{2k-1} B(\varepsilon^{2k-1}, c^{D+1-2k})$. With $\binom{D+1}{2k} = \frac{D+1}{2k} \binom{D}{2k-1}$ the two terms of degree $2k$ in $u$ agree. $\square$

### The swap relation

Let $\Psi$ be a finite set and $N \geq 2$, and index the steps by $\Psi \times \{0, \dots, N-1\}$. For a weight $\lambda$ the gap at $(\tau, i)$ is
$$
\gamma_\lambda(\tau, i) = \lambda(\tau, i) - \lambda(\tau, i + 1),
$$
with $\lambda(\tau, N) = 0$. The weight transform of a polynomial $Q$ is the polynomial $\operatorname{wt}(Q)$ with $\operatorname{wt}(Q)(\lambda) = Q(\gamma_\lambda)$. For an adjacent swap $(\tau, a, b)$ with $b = a + 1$, let $s$ be the transposition of $(\tau, a)$ and $(\tau, b)$ and let $\xi_{\tau,a}$ be the coefficient of Section 8.

**Theorem 10.10.2 (Swap relation).** Assume the inputs and let the intersection system be full. Let $S$ be an analytic system of dimension $d + 1$ indexed by the steps, with a realization, let $(\tau, a, b)$ be an adjacent swap, and assume that there is a square system for the realization at $((\tau, a), \xi_{\tau,a})$. For a weight $\lambda$ let $u = \gamma_\lambda(\tau, a)$ and $c = \gamma_\lambda + (u/2)\, \xi_{\tau,a}$. Then
$$
\operatorname{wt}(H)(\lambda) + \operatorname{wt}(H)(\lambda \circ s) = \operatorname{tsg}_{d+1}\bigl(\operatorname{line}_{c,\xi_{\tau,a}}(\operatorname{Deg})\bigr)(u) .
$$

Lean: `GlobalTheory.CompanionTheory.Ar.PB.thmA_swap` (also `GlobalTheory.T.adjacent_swap_height_polynomial_relation`, a second name).

*Proof.* Since $\xi_{\tau,a}(\tau, a) = -2$, we have $c(\tau, a) = u - u = 0$. By definition $\gamma_\lambda = c - (u/2)\xi_{\tau,a}$. The swap changes only the gaps at $(\tau, a - 1)$, $(\tau, a)$ and $(\tau, a + 1)$: the gap at $(\tau, a)$ changes sign, and the two neighbouring gaps change by $+u$. So $\gamma_{\lambda \circ s} = \gamma_\lambda + u\, \xi_{\tau,a} = c + (u/2)\xi_{\tau,a}$. With $\operatorname{wt}(H)(\lambda) = H(\gamma_\lambda)$, the reflection sum for $a_0 = (\tau, a)$, $\varepsilon = \xi_{\tau,a}$ and this $c$ gives the claim. The fibre local statement is available, so it is not a hypothesis here. $\square$

### Antisymmetry

Let $\delta = \lvert \Psi \rvert \binom{N}{2}$ be the dimension of the flag variety. An adjacent swap $(\tau, a, b)$ is allowed for $j \leq N$ if $b < j$ or $j \leq a$. The antisymmetric space for $j$ is the space of homogeneous polynomials $P$ of degree $\delta + 1$ in the steps such that $P \circ s = -P$ for the transposition $s$ of every allowed swap.

**Definition 10.10.3.** A flag system for a realization of an analytic system $S$ of dimension $d + 1$ indexed by the steps, at $j \leq N$, consists of the equality $d + 1 = \delta$, the condition that $S$ is uniformised at $j$, and a square system at $((\tau, a), \xi_{\tau,a})$ for every allowed adjacent swap.

Let $H_{\mathrm{Fl}}$ be the height polynomial of the flag variety for the Fubini-Study lines in weight coordinates, let $\operatorname{Deg}_{\mathrm{Fl}}$ be its degree polynomial, and let $\rho(\tau, i) = -i$. The volume of $S$ is
$$
\operatorname{vol}(S) = \frac{\operatorname{wt}(\operatorname{Deg}_S)(\rho)}{\operatorname{Deg}_{\mathrm{Fl}}(\rho)} .
$$

**Theorem 10.10.4 (Antisymmetry).** Assume the inputs and let the intersection system be full. Let $\Psi$ be nonempty, $N \geq 2$ and $j \leq N$, and let a realization of $S$ carry a flag system at $j$. Then $\operatorname{wt}(H) - \operatorname{vol}(S)\, H_{\mathrm{Fl}}$ is in the antisymmetric space for $j$.

Lean: `GlobalTheory.CompanionTheory.Ar.PB.Top.antisymmetry` (also `GlobalTheory.T.antisymmetry'`, a second name).

*Proof.* Step 1: the reference system. The flag variety carries an analytic system $S_0$ of dimension $\delta$ with a realization of degree $1$ whose lines are the Fubini-Study lines and do not depend on $t$, and with a flag system at $N$, so that every adjacent swap is allowed for $S_0$. Since the lines are constant, the numbers $\operatorname{num}_t$ of $S_0$ are the intersection numbers of the Fubini-Study lines. A computation of the lines of the flag variety in the two coordinate systems and the compatibility of potentials and degrees give $\operatorname{wt}(H_0) = H_{\mathrm{Fl}}$ and $\operatorname{wt}(\operatorname{Deg}_0) = \operatorname{Deg}_{\mathrm{Fl}}$.

Step 2: proportional degrees. Since $S$ is uniformised at $j$ and has dimension $\delta$, the proportionality theorem gives $\operatorname{wt}(\operatorname{Deg}_S) = \operatorname{vol}(S)\, \operatorname{Deg}_{\mathrm{Fl}}$. The weight transform is injective, so $\operatorname{Deg}_S = \operatorname{vol}(S)\, \operatorname{Deg}_0$.

Step 3: homogeneity. The height polynomial $H$ is homogeneous of degree $\delta + 1$, the weight transform preserves this degree, and $H_{\mathrm{Fl}}$ is homogeneous of the same degree. So $F = \operatorname{wt}(H) - \operatorname{vol}(S)\, H_{\mathrm{Fl}}$ is homogeneous of degree $\delta + 1$.

Step 4: the swaps. Let $(\tau, a, b)$ be an allowed swap and $\lambda$ a weight, with $u$ and $c$ as in the swap relation. The swap relation for $S$ and Step 2 give
$$
\operatorname{wt}(H)(\lambda) + \operatorname{wt}(H)(\lambda \circ s) = \operatorname{vol}(S)\, \operatorname{tsg}_{\delta}\bigl(\operatorname{line}_{c,\xi_{\tau,a}}(\operatorname{Deg}_0)\bigr)(u),
$$
because the line polynomial and the operator $\operatorname{tsg}$ are linear. The swap relation for $S_0$ and Step 1 give
$$
H_{\mathrm{Fl}}(\lambda) + H_{\mathrm{Fl}}(\lambda \circ s) = \operatorname{tsg}_{\delta}\bigl(\operatorname{line}_{c,\xi_{\tau,a}}(\operatorname{Deg}_0)\bigr)(u) .
$$
So $F(\lambda) + F(\lambda \circ s) = 0$ for every weight $\lambda$. A polynomial over $\mathbb{R}$ that vanishes at every point is $0$, so $F \circ s = -F$, and $F$ is in the antisymmetric space. $\square$

**Remark 10.10.5 (Formalization).** The second names only restate their theorems (`Development/AutomorphicSpectrum/Proofs/MetricProofs/HeightPolynomialReflectionSumStatement.lean:9`, `AdjacentSwapHeightPolynomialRelationStatement.lean:9`, `AntisymmetryStatement.lean:9`). The antisymmetry theorem has the type `Antisymmetry`, a proposition defined in `Development/AutomorphicSpectrum/Statements/MetricStatements/AgreementIffGuarded.lean:82`, with `FlagSys` at line 36 and `volOf` at line 31; its user is `GoodTowerAntisymmetryOf.lean:24`. The reflection sum is at `HeightPolynomialReflectionSum.lean:41`. It carries the fibre local statement as a hypothesis, while the swap relation passes the proof `FibreLocal.proof` (`AdjacentSwapHeightPolynomialRelation.lean:17`). The gap identities of the swap relation are `gap_swap_decomp`, which sits in `EtaleAwayOfIsEtaleAtOffSubmonoid.lean:44`, and the pointwise criterion for the antisymmetric space is `mem_antisymSpace_of_pointwise` in `EtaleLocalizationAtPrimeTensorOfEtaleAway.lean:11`; both file names have no relation to their content. The statement `GlobalTheory.T.weight_transform_injective_linear` packs three facts (the linearity of $\operatorname{tsg}$, the linearity of the line polynomial and the injectivity of the weight transform), and `GlobalTheory.T.weighted_polynomial_homogeneous_coeff_bound` is used in `Antisymmetry.lean:60` only for its homogeneity part. The operator $\operatorname{tsg}$ is `tsgPoly` in `CompRightEqZero.lean:23`, and the weight transform is `toWt` in `Definitions/MetricPeriods/PairRelationOfScaledRatio.lean:21`. I did not unfold the lemma on square systems at a fixed scale (`GlobalTheory.T.square_system_polar_vanishing`), the agreement theorem for positive systems, the regularized convergence of the square, the existence of the reference system, the proportionality theorem, nor the computation of the flag lines; Step 4 of the reflection sum is my account of `GlobalTheory.T.polar_identity_from_symmetric_forms`, which I did not unfold either.
