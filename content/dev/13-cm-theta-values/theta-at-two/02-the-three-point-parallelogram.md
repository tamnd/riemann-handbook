---
title: The three-point parallelogram law on a formal group
decls:
  - Formalism.L2.Th1.B.parThree
  - Formalism.L2.Th1.B.first_level_all_formal_groups
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The three-point parallelogram law on a formal group

Let $F$ be the formal group of a Weierstrass curve with integral coefficients over a complete field. Pull the logarithm of the modified sigma function back along the formal logarithm. This gives a series $\varphi$ in the formal parameter. This section proves that the coboundary of $\varphi$ satisfies the cocycle condition up to integral terms, and that the higher invariant derivatives of $\varphi$ at $0$ are integral. An older argument gets the cocycle condition from the two-point parallelogram law, but it divides by $2$. Here we use a three-point law instead, which comes from the Frobenius-Stickelberger formula of the [previous section](/entry/frob-stick-star/). So no division by $2$ occurs, and the result holds at the prime $2$. The next section applies it to the even sigma function at a point of order $2$.

**Definition 8.2.1 (Integral series and the relation $\simeq$).** Let $K$ be a field of characteristic $0$ with a non-archimedean absolute value (see [$p$-adic numbers and local fields](/learn/number-fields/#p-adic-numbers-and-local-fields)). A series in $K[[X_1, \dots, X_m]]$ is *integral* if all its coefficients have absolute value at most $1$. For two such series we write $f \simeq g$ if $f - g$ has constant term $0$ and $\exp(f - g)$ is integral.

So $f \simeq 0$ says that $f$ is the logarithm of an integral series with constant term $1$. The relation has these rules.

**Lemma 8.2.2 (Rules for $\simeq$).** The relation $\simeq$ is an equivalence relation. If $f \simeq g$ and $f' \simeq g'$, then $f + f' \simeq g + g'$. If $f \simeq g$ and $\psi_1, \dots, \psi_m$ are integral series with constant term $0$, then $f(\psi) \simeq g(\psi)$. If $N$ is integral with $N(0) = 1$, then $\log N \simeq 0$ and $-\log N \simeq 0$.

Lean: `Formalism.InvariantFactorPaths.G7.equivalence_rules`, `Formalism.L2.Th1.B.simeqLog`.

*Proof.* The absolute value is ultrametric, so a product of integral series is integral. An integral series $N$ with $N(0) = 1$ has an integral inverse $\sum_k (1 - N)^k$. All rules follow from $\exp(a + b) = \exp(a)\exp(b)$, from $\exp(f(\psi)) = (\exp f)(\psi)$, and from $\exp(\pm \log N) = N^{\pm 1}$. $\square$

**Definition 8.2.3 (Formal group with a logarithm).** Let $F \in K[[X_0, X_1]]$ and $l \in K[[X]]$. We say that $F$ is a *law with logarithm* $l$ if $F(0, 0) = 0$, $F$ is integral, $l(0) = 0$, $l'(0) = 1$ and
$$
l(F(X_0, X_1)) = l(X_0) + l(X_1) .
$$
A series $i \in K[[X]]$ is an *inverse* for $l$ if $i(0) = 0$, $i$ is integral and $l(i(X)) = -l(X)$.

Since $l$ has an inverse series over $K$, the identity determines $F$, and $F$ is a commutative [formal group law](/learn/formal-groups/#formal-group-laws) over $K$ with integral coefficients. Then $i$ is its inverse series. We write $F_3 = F(F(X_0, X_1), X_2)$ and $F^-(X_0, X_1) = F(X_0, i(X_1))$. Over the formal group, $F^-$ is the parameter of the difference of two points.

**Lemma 8.2.4 (Difference of two points).** Let $F$ be a law with logarithm $l$ and $i$ an inverse for $l$. Then $F^-(X_0, X_1) = (X_0 - X_1)\, n$ for an integral series $n$ with $n(0, 0) = 1$.

Lean: `Formalism.L2.Th1.B.fIUnit`.

*Proof.* We have $l(F(X, i(X))) = l(X) - l(X) = 0$, so $F(X, i(X)) = 0$. Substitute $X_0 = X_1 + t$ in $F^-$. Since $F$ and $i$ are integral, the result is an integral series in $t$ and $X_1$, and its part of degree $0$ in $t$ is $F(X_1, i(X_1)) = 0$. So $F^- = t \, n$ with $n$ integral. Comparing linear terms in $l(F) = l(X_0) + l(X_1)$ and $l(i) = -l$ gives $F = X_0 + X_1 + \cdots$ and $i = -X + \cdots$. So $F^- = X_0 - X_1 + \cdots$ and $n(0, 0) = 1$. $\square$

**Definition 8.2.5 (Weierstrass parameter).** Let $P$ be a [Weierstrass series](/entry/frob-stick-log/) for $(g_2, g_3)$, let $F$ be a law with logarithm $l$, $i$ an inverse, and let $c_0, a_1, a_3 \in K$ and $e_p \in K[[X]]$. We say that $(F, l, i)$ is a *Weierstrass parameter* for $P$ with data $(e_p, c_0, a_1, a_3)$ if:

1. $e_p$ is integral with $e_p(0) = 1$, and $X^2 (1 + l^2 P(l)) = l^2 (e_p + c_0 X^2)$;
2. there is an integral $c \in K[[X_0, X_1]]$ with $c(0, 0) = -1$ and $X_1^2 e_p(X_0) - X_0^2 e_p(X_1) = c \, F \, F^-$;
3. $X^3 (-2 + l^3 P'(l)) = l^3 (-2 e_p + a_1 X e_p + a_3 X^3)$;
4. there is an integral $e \in K[[X_0, X_1, X_2]]$ with $e(0) = -1$ and
$$
\det \begin{pmatrix} X_j^3 & X_j e_p(X_j) & -e_p(X_j) \end{pmatrix}_{j = 0, 1, 2} = e \, F_3 \, (X_0 - X_1)(X_0 - X_2)(X_1 - X_2) .
$$

Put $x = e_p / X^2$ and $y = -e_p / X^3$. Then items 1 and 3 say $\wp(l(X)) = x + c_0$ and $\wp'(l(X)) = 2y + a_1 x + a_3$. These are the coordinates of a point of a [Weierstrass model](/learn/elliptic-curves/#reduction-and-minimal-models) in its formal parameter $X$. Item 2 says that $x(X_0) - x(X_1)$ is a unit times $F F^- / (X_0 X_1)^2$: it vanishes exactly when the two points are equal or opposite. Item 4 says that $\det(1, x_j, y_j)$ is a unit times $F_3 \prod_{j<k} (X_j - X_k) / (X_0 X_1 X_2)^3$: three points are on a line exactly when two agree or their sum is $0$.

**Definition 8.2.6 (Pulled back sigma logarithm).** For $s_2 \in K$ put
$$
\varphi = -S(l) + \tfrac{s_2}{2} l^2 - \log(l / X) ,
$$
where $S = -\iint P$ and $l/X$ is the series with $(l/X)(0) = 1$.

Then $\varphi(0) = 0$ and $\sigma^*(l(X)) = X \exp(-\varphi(X))$, since $\sigma^*(z) = z \exp(S(z) - \tfrac{s_2}{2} z^2)$.

**Definition 8.2.7 (Coboundaries and parallelograms).** For $f \in K[[X]]$ and a law $F$ with inverse $i$ put
$$
\begin{aligned}
\operatorname{cob} f &= f(F(X_0, X_1)) - f(X_0) - f(X_1), \\
\operatorname{par} f &= f(F) + f(F^-) - 2 f(X_0) - 2 f(X_1), \\
\operatorname{par}_3 f &= f(F_3) + \sum_{j < k} f(F^-(X_j, X_k)) - 3 \sum_j f(X_j) .
\end{aligned}
$$
For $H \in K[[X_0, X_1]]$ put $d_1 H = H(F(X_0, X_1), X_2) - H(X_0, X_2) - H(X_1, X_2)$ and let $H^{\mathrm{sw}}(X_0, X_1) = H(X_1, X_0)$. Let $\mathcal{D} = l'(X)^{-1} \, d/dX$ be the [invariant derivation](/learn/formal-groups/#the-invariant-derivation-and-the-logarithm).

If $f$ were additive on $F$, all of these would vanish. The series $\operatorname{cob} f$ is the obstruction, and $d_1 \operatorname{cob} f = 0$ would mean that $\operatorname{cob} f$ is bilinear. For a quadratic function $f$ on a group, the parallelogram combinations vanish. The point of the next lemma is that $\operatorname{par}$ and $\operatorname{par}_3$ control $d_1 \operatorname{cob} f$.

**Lemma 8.2.8 (Cube from parallelograms).** Let $F$ be a law with logarithm $l$, $i$ an inverse and $f \in K[[X]]$. Then
$$
d_1 \operatorname{cob} f = \operatorname{par}_3 f - \sum_{j < k} (\operatorname{par} f)(X_j, X_k) .
$$
So if $\operatorname{par} f \simeq 0$ and $\operatorname{par}_3 f \simeq 0$, then $d_1 \operatorname{cob} f \simeq 0$.

Lean: `Formalism.L2.Th1.B.cubeFromPars`.

*Proof.* Expand. The sum of the three parallelograms is $\sum_{j<k} f(F(X_j, X_k)) + \sum_{j<k} f(F^-(X_j, X_k)) - 4 \sum_j f(X_j)$. Subtracted from $\operatorname{par}_3 f$, it leaves $f(F_3) - \sum_{j<k} f(F(X_j, X_k)) + \sum_j f(X_j)$, which is $d_1 \operatorname{cob} f$. The second claim follows from the rules for $\simeq$, since $X_j, X_k$ are integral with constant term $0$. $\square$

No factor $2$ is inverted here. The older route proves $d_1 \operatorname{cob} f \simeq 0$ from $\operatorname{par} f \simeq 0$ alone, and needs $|2| = 1$ for this.

**Lemma 8.2.9 (Two-point parallelogram).** Let $P$ be a Weierstrass series, $(F, l, i)$ a law with logarithm and inverse that satisfies items 1 and 2 of a Weierstrass parameter, and $s_2 \in K$. Then $\operatorname{par} \varphi \simeq 0$.

Lean: `Formalism.L2.Th1.B.parO`.

*Proof.* The addition formula for sigma of [the previous section](/entry/frob-stick-log/), with $\sigma^*$ in place of $\sigma$, reads $z_0^2 z_1^2 \sigma^*(z_0 + z_1)\sigma^*(z_0 - z_1) = \sigma^*(z_0)^2 \sigma^*(z_1)^2 w_{01}$. Substitute $z_j = l(X_j)$. Then $l(X_0) \pm l(X_1) = l(F)$ and $l(F^-)$, and $\sigma^*(l) = X \exp(-\varphi)$. By item 1, $w_{01}$ becomes $-(l_0 l_1 / X_0 X_1)^2 (X_1^2 e_p(X_0) - X_0^2 e_p(X_1))$, and by item 2 this is $-c \, F F^-$ times $(l_0 l_1/X_0 X_1)^2$. After cancelling, $\exp(-\operatorname{par} \varphi) = -c$. Since $-c$ is integral with constant term $1$, the rules give $\operatorname{par} \varphi = -\log(-c) \simeq 0$. $\square$

**Theorem 8.2.10 (Three-point parallelogram).** Let $K$ be a field of characteristic $0$ with an ultrametric absolute value. Let $g_2, g_3, s_2, c_0, a_1, a_3 \in K$, let $P$ be a Weierstrass series for $(g_2, g_3)$, let $F$ be a law with logarithm $l$, $i$ an inverse for $l$, and let $(F, l, i)$ be a Weierstrass parameter for $P$ with data $(e_p, c_0, a_1, a_3)$. Then
$$
\operatorname{par}_3 \varphi \simeq 0 .
$$

Lean: `Formalism.L2.Th1.B.parThree`.

*Proof.* Substitute $z_j = l(X_j)$ in the modified form of the [Frobenius-Stickelberger formula](/entry/frob-stick-star/). Write $l_j = l(X_j)$.

On the right side, $l_0 + l_1 + l_2 = l(F_3)$ and $l_j - l_k = l(F^-(X_j, X_k))$. So $\sigma^*(l_0 + l_1 + l_2) = F_3 \exp(-\varphi(F_3))$ and $\sigma^*(l_j - l_k) = F^-(X_j, X_k) \exp(-\varphi(F^-(X_j, X_k)))$. By the lemma on the difference of two points, $F^-(X_j, X_k) = (X_j - X_k) n_{jk}$ with $n_{jk} = n(X_j, X_k)$.

On the left side, $\sigma^*(l_j) = X_j \exp(-\varphi(X_j))$. By items 1 and 3, row $j$ of the matrix of $D$ becomes $(l_j / X_j)^3 (X_j^3, \; X_j e_p + c_0 X_j^3, \; -2 e_p + a_1 X_j e_p + a_3 X_j^3)$, with $e_p = e_p(X_j)$. Subtract $c_0$ times the first column from the second, then $a_3$ times the first and $a_1$ times the new second column from the third. The rows become $(X_j^3, X_j e_p, -2 e_p)$. By item 4,
$$
D(l_0, l_1, l_2) = 2 \Bigl( \frac{l_0 l_1 l_2}{X_0 X_1 X_2} \Bigr)^3 e \, F_3 \prod_{j<k} (X_j - X_k) .
$$
Insert both sides in the formula and cancel the factor $2 (l_0 l_1 l_2)^3 F_3 \prod_{j<k}(X_j - X_k)$, which is not a zero divisor. What is left is
$$
n_{01} n_{02} n_{12} \exp(-\operatorname{par}_3 \varphi) = -e .
$$
Here $N = n_{01} n_{02} n_{12}$ and $-e$ are integral with constant term $1$. So $\operatorname{par}_3 \varphi = \log N - \log(-e)$, and the rules for $\simeq$ give $\operatorname{par}_3 \varphi \simeq 0$. $\square$

**Theorem 8.2.11 (First level on a formal group).** Under the hypotheses of the three-point parallelogram theorem, put $H = \operatorname{cob} \varphi$. Then:

1. every coefficient of $X_0^{a} X_1^{b}$ in $H$ with $a = 0$ or $b = 0$ is $0$;
2. $H^{\mathrm{sw}} = H$;
3. $d_1 H \simeq 0$ and $d_1 H^{\mathrm{sw}} \simeq 0$;
4. for every $n \geq 3$, the constant term of $\mathcal{D}^n \varphi$ has absolute value at most $1$.

Lean: `Formalism.L2.Th1.B.first_level_all_formal_groups`.

*Proof.* By the two-point parallelogram lemma, $\operatorname{par} \varphi \simeq 0$. By the three-point theorem, $\operatorname{par}_3 \varphi \simeq 0$. The cube lemma gives $d_1 H \simeq 0$. Since $\operatorname{par} \varphi$ has constant term $-2 \varphi(0)$, we get $\varphi(0) = 0$. Then $H(X_0, 0) = \varphi(X_0) - \varphi(X_0) - \varphi(0) = 0$, since $F(X_0, 0) = X_0$, and in the same way $H(0, X_1) = 0$. This is item 1. Item 2 holds because $F$ is commutative. So $d_1 H^{\mathrm{sw}} = d_1 H \simeq 0$, which completes item 3.

For item 4, let $\mathcal{D}_j$ be the invariant derivation in $X_j$. It is $(l'(X_j))^{-1} \partial_j$, and $(l')^{-1}$ is integral since $l'(X)^{-1} = (\partial_1 F)(X, 0)$, as one sees by applying $\partial_1$ to $l(F) = l(X_0) + l(X_1)$ and setting $X_1 = 0$. So $\mathcal{D}_j$ preserves integral series. If $T \simeq 0$, then $\partial_j T = \exp(-T) \partial_j \exp(T)$ is integral. So $\mathcal{D}_0^{k+1} \mathcal{D}_1 \mathcal{D}_2 \, d_1 H$ is integral for all $k \geq 0$. Since $\mathcal{D}_j$ commutes with substitution into $F$, it kills every term of $d_1 H = \varphi(F_3) - \sum_{j<k} \varphi(F(X_j, X_k)) + \sum_j \varphi(X_j)$ except the first. So $\mathcal{D}_0^{k+1} \mathcal{D}_1 \mathcal{D}_2 \, d_1 H = (\mathcal{D}^{k+3} \varphi)(F_3)$. Set all $X_j = 0$: the constant term of $\mathcal{D}^{k+3} \varphi$ is integral. $\square$

Over $\mathbb{C}$ the theorem has a clear meaning. The function $\log \sigma^*$ is a quadratic function on the group up to theta multipliers, so its coboundary is a bilinear form plus a coboundary. The theorem is a formal, integral version of this fact near the origin, for any formal group with the structure of a Weierstrass curve.

**Remark 8.2.12 (Formalization).** The Lean name speaks of all formal groups, but the theorem is about one law $F$ with the hypotheses above. The law $F$ is not assumed to be a formal group law; this follows from the identity for $l$. The two lemmas on parallelograms and the cube lemma are `Formalism.L2.Th1.B.parO`, `Formalism.L2.Th1.B.cubeFromPars` and the step `Formalism.L2.Th1.B.E3.parallelogram_three_sub_pairs` ([FirstLevelOfThreeVarParallelogram.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/LogarithmicSubstitution/FirstLevelOfThreeVarParallelogram.lean#L11)). Item 4 is `Formalism.L2.Th1.B.jetsThree`. The proof of the three-point theorem is in [ConstantCoeffLawWithInverseThree.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/LogarithmicSubstitution/ConstantCoeffLawWithInverseThree.lean#L341). Items 1 and 2 use only $\varphi(0) = 0$ and the law, through `Formalism.L2.Th1.B.cobRules`. The older cube statement `Formalism.L2.Th1.B.Cube` asks for $|2| = 1$; the theorem here does not.
