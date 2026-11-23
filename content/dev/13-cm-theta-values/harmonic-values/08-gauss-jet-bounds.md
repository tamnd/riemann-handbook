---
title: Gauss jet bounds
decls:
  - Formalism.DworkPowerSeriesWeights.thmAGauss
  - Formalism.DworkPowerSeriesWeights.thmAGauss_of
  - Formalism.DworkPowerSeriesWeights.theorem_A_generic
  - Formalism.DworkPowerSeriesWeights.theorem_A_frame
  - Formalism.DworkPowerSeriesWeights.lemmaS
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Gauss jet bounds

The previous sections bound harmonic values from below at each place. This section gives the upper bound at a prime $l$ for the jets of a theta series of Dwork type. The series is the product of an integral series, pulled back along the inverse of a twisted logarithm, and an exponential of a power series $\beta$ in one letter per residue class. The jets are measured by pairing the series with products of minors. The main result bounds every coefficient of such a pairing by an explicit power of $|l|$. The exponent is a sum of a term for each row type, the value of a linear program, and a loss of order $\log_l a$. The proof passes to a field with a residually generic point, where the Gauss norm of a polynomial equals the norm of its value. The section ends with the weight bound for $\beta$ itself. The [theorem A](/entry/thm-a-of/) uses the main result, and the step [theta local matching](/step/theta-local-matching/) uses the weight bound. The background is in [$p$-adic numbers and local fields](/learn/number-fields/#p-adic-numbers-and-local-fields), [formal group laws](/learn/formal-groups/#formal-group-laws) and [the logarithm](/learn/formal-groups/#the-invariant-derivation-and-the-logarithm).

### Setting

Let $l \ge 3$ be a prime and let $d \ge 2$ be even. Let $K$ be a field of characteristic $0$ with an ultrametric norm such that $|l| < 1$. Let $\zeta \in K$ be a primitive root of unity of order $l^d - 1$. Let $K_0 \subset K$ be a subfield that is *unramified*: every nonzero element of $K_0$ has norm $|l|^k$ for an integer $k$.

The letters are the triples $y = (s, i, b)$ with $s \in \mathbb{Z}/d$, $0 \le i < N_0$ and $0 \le b < N_1$. We call $s$ the *row type*, $i$ the *row* and $b$ the *column*.

**Definition 2.8.1 (twisted logarithm).** For a letter $y = (s, i, b)$, put
$$\mathrm{L}(y) = \sum_{e \ge 0} l^{-e}\, X_{(s - 2e, i, b)}^{l^{2e}}.$$
A *twisted exponential* is a family of series $g(y)$ with $g(y)(0) = 0$ and $\mathrm{L}(y)(g) = X_y$ for every letter $y$.

The series $\mathrm{L}$ is a twisted form of the logarithm of the Lubin-Tate formal group of height $2$. The shift $s \mapsto s - 2e$ records the action of the Frobenius of the unramified extension of degree $d$.

**Definition 2.8.2 (weight hypothesis).** A power series $\beta$ in the letters $X_s$, $s \in \mathbb{Z}/d$, satisfies the *weight hypothesis* if four conditions hold.

1. The coefficients of $\beta$ lie in $K_0$.
2. $\beta$ is invariant under the torus action $X_s \mapsto \zeta^{w(s)} X_s$, where $w(s) = l^s$ for $s$ even and $w(s) = -l^s$ for $s$ odd. Here $s$ is read as an integer $0 \le s < d$.
3. $\beta$ has no terms of low bidegree: every monomial of $\beta$ has positive degree in the even letters and in the odd letters, and it does not have bidegree $(1, 1)$.
4. Let $X'$ be a second copy of the letters. Let $\delta_1(\beta)$ be the additivity defect of $\beta$ in the even letters, $\beta(X_{\mathrm{ev}} + X'_{\mathrm{ev}}, X_{\mathrm{odd}}) - \beta(X_{\mathrm{ev}}, X_{\mathrm{odd}}) - \beta(X'_{\mathrm{ev}}, X_{\mathrm{odd}})$, and let $\delta_2(\beta)$ be the same defect in the odd letters. After the substitution of the letter logarithms $\sum_e l^{-e} X_{s - 2e}^{l^{2e}}$ in $X$ and $X'$, the series $\exp(\delta_1(\beta))$ and $\exp(\delta_2(\beta))$ are integral with constant term $1$.

Condition 4 is a version of Dwork's lemma: a series $F$ with $F(0) = 1$ has integral coefficients if a Frobenius twist of $F$ divided by $F$ is congruent to $1$. The classical example is the Artin-Hasse exponential.

**Definition 2.8.3 (theta series and frame jet).** Let $g$ be a twisted exponential, let $U$ be an integral series in the letters and let $\varepsilon = \pm 1$. The *theta series* is
$$\Theta = U(g) \cdot \exp\Big(\varepsilon \sum_{y} \beta(y)\Big),$$
where the sum places a copy of $\beta$ on the letters of each row and column. Let $x = (x_{s,i,a})$ be a matrix of frame variables. For each row type $s$, let $p_s(c)$ for $c = 1, \dots, \nu_1(s)$ be a list of positive sizes at most $N_0$, and let $I_s(c)$ be a choice of $p_s(c)$ columns. The rows $r_{s,i,b} = \sum_a x_{s,i,a} X_{s,a,b}$ define a product of minors
$$M = \prod_s \prod_c \det\big(r_{s,i,I_s(c)(j)}\big)_{1 \le i, j \le p_s(c)}.$$
The *frame jet* is the polynomial in $x$ obtained by the pairing
$$\langle M, \Theta \rangle = \sum_\kappa \mathrm{coeff}_\kappa(M)\, \kappa!\, \mathrm{coeff}_\kappa(\Theta),$$
where $\kappa$ runs over the monomials in the letters.

The pairing $\langle M, \Theta\rangle$ is the value at $0$ of the differential operator $M(\partial)$ applied to $\Theta$. So the frame jet is a jet of $\Theta$ along the frame $x$.

### The main bound

Let $TT \subset \mathbb{Z}/d$ be the set of top row types. Put $\nu_1(s) = $ the number of minors of type $s$, $\nu_2(s) = $ the number of those minors of size at least $2$, and $\mathrm{size}(s) = \sum_c p_s(c)$. Let $a \ge 1$ be a bound with $\mathrm{size}(s) \le a$ for all $s$. Put $\gamma = l/(l^2 - 1)$. The bound uses three quantities that depend only on $l$, $d$, $TT$, $\nu_1$, $\nu_2$ and $\mathrm{size}$: a *top term* $\mathrm{top}(s)$, a *cap* $W(s)$, and the value $F(D)$ of a linear program on a vector $D$ of row demands. The linear program is $\gamma \sum D$ minus a maximal flow. We do not unfold these quantities.

**Theorem 2.8.4 (Gauss jet bound).** Let $K = \mathbb{C}_l$. Assume the setting above, the weight hypothesis for $\beta$, and $2 \log_l a + 2 \le N_0 - 1$. Then every coefficient of the frame jet of $\Theta$ has norm at most $|l|^{E}$, where
$$E = \sum_{s \in TT} \big(\mathrm{top}(s) - \gamma\, W(s)\big) + F(D) - d N_0 N_1 (\log_l a + 1).$$
Lean: `Formalism.DworkPowerSeriesWeights.thmAGauss`

The last term is the loss. It is linear in the number of letters and logarithmic in the size of the minors. The condition $2 \log_l a + 2 \le N_0 - 1$ says that there are enough rows to place the labels of the next proof.

**Theorem 2.8.5 (reduction to a generic frame).** The Gauss jet bound follows from four statements: (1) the hypotheses of the setting transfer along an isometric embedding of fields; (2) evaluation of the frame jet at a point $x$ equals the pairing of $\Theta$ with the minors of the rows at $x$; (3) labels exist; and (4) the Gauss norm property for powers of a generic point.
Lean: `Formalism.DworkPowerSeriesWeights.thmAGauss_of`

Here a *labelling* is, for each row type $s$, an injective list of pairs $(s_0, j)$ with $s_0 \in TT$, $j$ odd and $s = s_0 + j$, such that $l^j \le \nu_1(s_0)$ when $j > 0$ and $l^{-j} \le \mathrm{size}(s)$ when $j < 0$. The list must contain every such pair, its length $J(s)$ satisfies $J(s) + [s \in TT] \le N_0$, and every negative $j$ satisfies $-j \le m$ for a fixed $m$. A point $Y$ of $K$ indexed by the frame variables is *generic* if $|P(Y)| = 1$ for every polynomial $P$ with integer coefficients that is nonzero modulo $l$.

*Proof.* There is an extension $K \supset \mathbb{C}_l$ with an isometric embedding and a generic point $Y$ such that $|P(Y)|$ is the Gauss norm, that is the maximum of the norms of the coefficients, for every polynomial $P$ over $\mathbb{C}_l$. For example, one can take a completed algebraic closure of the completion of $\mathbb{C}_l(Y)$ for the Gauss norm. By statement (3), labels $(J, \mathrm{lab}, m)$ exist. By statement (1), the hypotheses on $K_0$, $\zeta$, $\beta$, $g$ and $U$ hold over $K$. Let $\mathrm{gen}(Y)$ be the frame that raises $Y_{s,0,a}$ to the power $l^m$ for $s \in TT$ and keeps the other entries. The generic theorem below bounds the pairing of $\Theta$ with the minors at $\mathrm{gen}(Y)$ by $|l|^E$. By statement (2), this pairing is the value of the frame jet at $\mathrm{gen}(Y)$. By statement (4), each coefficient of a polynomial has norm at most the norm of its value at a point whose entries are nonzero powers of the entries of $Y$. $\square$

All four statements are proved, and the Gauss jet bound is the application of this reduction to them. Statement (4) is the classical fact that the Gauss norm is multiplicative and that the substitution $Y \mapsto Y^k$ with $k \ge 1$ maps distinct monomials to distinct monomials.

### Generic frames and frames with a labelling

**Theorem 2.8.6 (generic frame).** Let $K$ be any field as in the setting, and let $Y$ be generic. Let $(J, \mathrm{lab}, m)$ be a labelling. Then the pairing of $\Theta$ with the minors of the rows at $\mathrm{gen}(Y)$ has norm at most $|l|^E$.
Lean: `Formalism.DworkPowerSeriesWeights.theorem_A_generic`

*Proof.* Put $x = \mathrm{gen}(Y)$. Every entry of $Y$ has norm $1$, because $Y$ is generic, so every entry of $x$ has norm $1$. For each label $(s_0, j)$ of row type $s$, put $\lambda_a = Y_{s_0,0,a}^{l^{m + j}}$. This is defined because $-j \le m$. Since $x_{s_0,0,a} = Y_{s_0,0,a}^{l^m}$, we get $\lambda = x_{s_0,0}^{l^j}$ when $j > 0$ and $\lambda^{l^{-j}} = x_{s_0,0}$ when $j < 0$. Assign to the $i$-th label of type $s$ the row $e(i) = i + 1$ if $s \in TT$ and $e(i) = i$ otherwise. This avoids row $0$ of the top types, and it fits because $J(s) + [s \in TT] \le N_0$. The determinant of the matrix $\big(\sum_a \lambda_{i,a}\, x_{s,e(i'),a}\big)$ is the value at $Y$ of a polynomial with integer coefficients. This polynomial is nonzero modulo $l$: the labels give distinct pairs of a type and an exponent, and a determinant of distinct monomials of this shape is nonzero over every nonzero ring. By genericity, the determinant has norm $1$. The frame theorem below now applies. $\square$

**Theorem 2.8.7 (frame with a labelling).** Let $x$ be a frame with $|x_{s,i,a}| \le 1$. Let $(J, \mathrm{lab})$ be a labelling and let $\lambda$ be vectors of norm at most $1$ such that $\lambda = x_{s_0,0}^{l^j}$ for $j > 0$ and $\lambda^{l^{-j}} = x_{s_0,0}$ for $j < 0$. Let $e$ be an injective assignment of rows that avoids row $0$ of the top types, and assume that the determinant of the matrix $\big(\sum_a \lambda_{i,a}\, x_{s,e(i'),a}\big)$ has norm $1$ for each $s$. Then the pairing of $\Theta$ with the minors of the rows at $x$ has norm at most $|l|^E$.
Lean: `Formalism.DworkPowerSeriesWeights.theorem_A_frame`

*Proof.* Fix a row type $s$. The determinant condition says that the vectors $\lambda_i$ and the rows $x_{s,e(i)}$ form dual frames over the integers. So there is a new frame $x'$ with entries of norm at most $1$ and an integral matrix $T$ with three properties: $x'$ agrees with $x$ on row $0$ of the top types; every other row of $x$ is $T$ times the rows of $x'$ outside row $0$ of the top types; and $\lambda_i$ is orthogonal to every row $x'_k$ with $k \neq e(i)$ outside row $0$ of the top types. Assign to the row $e(i)$ of $x'$ its label, and leave the other rows without a label. This reduces the claim to an operator form of the bound, stated for a frame of the form $T x'$ with labelled rows. The operator form is proved by linearity of the pairing in the minors and by the bound for each labelled row, which uses the relation between $\lambda$ and the top row together with the twisted logarithm. The bounds for the labels combine into the top terms and the caps, and the sum over the rows without a label is the linear program $F(D)$. The loss term counts the monomials that contribute. $\square$

### The weight of one letter

The last result bounds the coefficients of $\beta$. Put $\rho = 1/(l^2 - 1)$. For a monomial $n$ in the letters $X_s$, let $|n|$ be its weighted degree, where $X_s$ has weight $1$. A monomial is a *bipower* if it equals $X_s^{l^\alpha} X_{s'}^{l^{\alpha'}}$ with $s$ even, $s'$ odd, $(\alpha, \alpha') \neq (0, 0)$ and $s + \alpha = s' + \alpha'$ in $\mathbb{Z}/d$.

**Lemma 2.8.8 (one letter weight).** Let $K$ be as in the setting, with $l$ odd, and let $\beta$ satisfy the weight hypothesis. Then for every monomial $n$,
$$|\mathrm{coeff}_n \beta| \le |l|^{\frac{1}{l-1} - 1 - \rho |n|}.$$
If $n$ is not a bipower, then
$$|\mathrm{coeff}_n \beta| \le |l|^{\frac{1}{l-1} - \rho |n|}.$$
Lean: `Formalism.DworkPowerSeriesWeights.lemmaS`

*Proof.* Let $F_i$ be $\exp(\delta_i(\beta))$ after the substitution of the letter logarithms, for $i = 1, 2$. By the weight hypothesis, $F_i$ is integral with constant term $1$. The letter logarithm has weight $\rho$ in the following sense. Its term of index $e$ has a coefficient of norm $|l|^{-e}$ and degree $l^{2e}$, and
$$e \le \frac{l^{2e} - 1}{l^2 - 1} = \rho\, (l^{2e} - 1).$$
The inverse series of the letter logarithm then has the same weight. Take the logarithm of $F_i$. Since $F_i$ is integral with constant term $1$, the derivative $F_i'/F_i$ is integral. Passing from $\log F_i$ back to $\delta_i(\beta)$ and controlling the exponential costs the constant $1/(l-1)$ in the exponent, which comes from $v_l(n!) \le n/(l-1)$. A comparison of weights after the substitution, a quantization of the weights, and an induction on the degree give a bound of this form for $\delta_i(\beta)$. The coefficients of $\beta$ are extracted from those of $\delta_1(\beta)$ and $\delta_2(\beta)$ by binomial coefficients. A monomial of $\beta$ that is not a bipower appears in $\delta_1(\beta)$ or $\delta_2(\beta)$ with a binomial coefficient that is a unit at $l$. For a bipower the binomial coefficient can be divisible by $l$, which costs the extra factor $|l|^{-1}$ in the first bound. $\square$

The exponent $1/(l-1)$ is the valuation of $\pi$ with $\pi^{l-1} = -l$, which is the radius of convergence of the exponential. This is the same constant as in Dwork's splitting function. See Koblitz, *$p$-adic Numbers, $p$-adic Analysis, and Zeta-Functions*, Chapter IV, Section 2.

**Remark 2.8.9 (Formalization).** The Gauss jet bound is in [ThmAGauss.lean](lean:Formalism/GaussJetBounds/ThmAGauss.lean#L8), with the statement in [StatementP.lean](lean:Formalism/GaussJetBounds/StatementP.lean#L33). The reduction is in [ThmAGaussOf.lean](lean:Formalism/GaussJetBounds/GaussJetProofs/ThmAGaussOf.lean#L13), and its four inputs are stated in [FrameJetEval.lean](lean:Formalism/GaussJetBounds/FrameJetEval.lean#L10). The generic theorem is in [Generic.lean](lean:Formalism/GaussJetBounds/GaussJetProofs/Generic.lean#L133), and the frame theorem in [FrameA.lean](lean:Formalism/GaussJetBounds/GaussJetProofs/FrameA.lean#L287). The frame theorem applies a general frame argument to an operator form of the bound in [ConstantCoeffAevalLinP.lean](lean:Formalism/GaussJetBounds/GaussJetProofs/ConstantCoeffAevalLinP.lean#L409), which uses a `first` combinator for one constant coefficient. The linear program is in [IncomingBound.lean](lean:Formalism/IncomingBounds/IncomingBound.lean). The one letter weight is in [OneLetterRadius.lean](lean:Formalism/GaussJetBounds/OneLetterRadius.lean#L17), with the weight hypothesis and the statement in [Statement.lean](lean:Formalism/GaussJetBounds/Statement.lean#L85). It applies a conditional form to eight proved inputs. The short name of the lemma is shared with unrelated statements in other folders of the library.
