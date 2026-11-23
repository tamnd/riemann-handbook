---
title: The even sigma function at a point of order two
decls:
  - Formalism.L2.Th1.B.BeE.CubeE_of
  - Formalism.L2.Th1.B.cubeE
  - Formalism.L2.Th1.B.th0Vanish
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The even sigma function at a point of order two

Let $T$ be a point of order $2$ on a Weierstrass curve with integral coefficients. The theta function attached to $T$ is built from the even sigma function $\sigma_1$, whose second logarithmic derivative is $-\wp(z + \omega/2)$. This section proves two results on its pullback to the formal group. First, its coboundary satisfies the cocycle condition up to integral terms. This follows from the [first level theorem](/entry/first-level-all-formal-groups/) of the last section. Second, if the curve has an endomorphism $\alpha$ that is a unit at $2$ and whose conjugate is not, then the theta function itself is an integral series with constant term $1$. The [next section](/entry/th0-two-analytic-of/) applies this second result to a curve with complex multiplication.

We keep the setting of the last section: $K$ is a field of characteristic $0$ with an ultrametric absolute value, $P$ is a [Weierstrass series](/entry/frob-stick-log/) for $(g_2, g_3)$, and $(F, l, i)$ is a [Weierstrass parameter](/entry/par-three/) for $P$ with data $(e_p, c_0, a_1, a_3)$. So $\wp(l(X)) = x + c_0$ and $\wp'(l(X)) = 2y + a_1 x + a_3$, with $x = e_p / X^2$ and $y = -e_p / X^3$.

**Definition 8.3.1 (Point of order two).** Let $x_T, y_T \in K$ and put $e_1 = x_T + c_0$ and $\kappa = 3 e_1^2 - g_2/4$. We say that $(x_T, y_T)$ is an *integral point of order two* if
$$
2 y_T + a_1 x_T + a_3 = 0, \qquad 4 e_1^3 - g_2 e_1 - g_3 = 0,
$$
and $|x_T| \leq 1$, $|y_T| \leq 1$, $|a_1| \leq 1$, $|\kappa| \leq 1$.

The first equation says that the tangent at $(x_T, y_T)$ is vertical, and the second says that $e_1$ is a root of $4t^3 - g_2 t - g_3$. Over $\mathbb{C}$ we have $e_1 = \wp(\omega/2)$ for a half period $\omega/2$, and $\kappa = (e_1 - e_2)(e_1 - e_3)$ for the other two roots $e_2, e_3$.

**Definition 8.3.2 (Even sigma series).** With $e_1$ and $\kappa$ as above, let
$$
w = \frac{z^2}{1 + z^2 P - e_1 z^2} \in K[[z]],
$$
so that $w = 1/(\wp - e_1)$. Let $\Sigma_1 = -\iint (e_1 + \kappa w)$, with constant and linear coefficients $0$, and put $\sigma_1 = \exp(\Sigma_1)$. For $s_2 \in K$ let
$$
\theta(z) = \sigma_1(z) \exp(-\tfrac{s_2}{2} z^2), \qquad \varphi_E = -\Sigma_1(l) + \tfrac{s_2}{2} l^2 .
$$

Over $\mathbb{C}$, $\wp(z + \omega/2) = e_1 + \kappa / (\wp(z) - e_1)$ (Whittaker and Watson, Ch. XX). So $(\log \sigma_1)'' = -\wp(z + \omega/2)$, and $\sigma_1$ is the classical even function $\sigma(z + \omega/2) / \sigma(\omega/2)$ times an exponential of a linear term. In the formal parameter we have $\varphi_E(0) = 0$ and $\theta(l(X)) = \exp(-\varphi_E(X))$.

**Lemma 8.3.3 (Comparison with the sigma logarithm).** Assume that $(x_T, y_T)$ is an integral point of order two. Let $\varphi$ be the [pulled back sigma logarithm](/entry/par-three/) and $H_E = \operatorname{cob} \varphi_E$, $H = \operatorname{cob} \varphi$. Then $H_E \simeq H$.

Lean: `Formalism.L2.Th1.B.beESim`.

*Proof.* Put $g = e_p - x_T X^2$, an integral series with $g(0) = 1$. By item 1 of a Weierstrass parameter, $\wp(l) - e_1 = g / X^2$. The square relation $\sigma_1^2 = \sigma^2 (\wp - e_1)$, a formal identity that holds because $e_1$ is a root of the cubic, gives $2(\varphi_E - \varphi) = -\log g$. So $2(H_E - H) = -\operatorname{cob} \log g$. Next, let $t = (e_p + y_T X^3)/g$ and
$$
L_T = X_1 t(X_0) + X_0 t(X_1) - a_1 X_0 X_1 .
$$
Since $|x_T|, |y_T|, |a_1| \leq 1$, $L_T$ is integral. From the addition formula for $w$ one gets the identity
$$
g(F) \, L_T^2 = g(X_0) \, g(X_1) \, F^2 \, d^2, \qquad d = 1 - \kappa \, w(l(X_0)) \, w(l(X_1)) .
$$
Here $w(l) = X^2 / g$ is integral and $|\kappa| \leq 1$, so $d$ is integral with $d(0) = 1$. The identity shows that $L_T$ vanishes on $X_1 = i(X_0)$, where $F$ vanishes. As in the [lemma on the difference of two points](/entry/par-three/), $L_T = F \nu$ with $\nu$ integral, and comparing the coefficients of $X_1$ gives $\nu(0) = 1$. Cancel $F^2$ and take logarithms: $\operatorname{cob} \log g = 2 \log d - 2 \log \nu$. So $2(H_E - H) = 2 \log \nu - 2 \log d$. Divide by $2$, which is allowed in $K$ and needs no bound on $|2|$. The rules for $\simeq$ give $H_E - H = \log \nu - \log d \simeq 0$. $\square$

**Theorem 8.3.4 (Cocycle condition for the even sigma function).** Let $g_2, g_3, s_2, c_0, a_1, a_3, x_T, y_T \in K$, let $P$ be a Weierstrass series for $(g_2, g_3)$, let $F$ be a law with logarithm $l$, $i$ an inverse, $(F, l, i)$ a Weierstrass parameter for $P$ with data $(e_p, c_0, a_1, a_3)$, and $(x_T, y_T)$ an integral point of order two. Put $H_E = \operatorname{cob} \varphi_E$. Then the coefficients of $X_0^a X_1^b$ in $H_E$ with $a = 0$ or $b = 0$ are $0$, $H_E^{\mathrm{sw}} = H_E$, $d_1 H_E \simeq 0$ and $d_1 H_E^{\mathrm{sw}} \simeq 0$.

Lean: `Formalism.L2.Th1.B.BeE.CubeE_of` (also `Formalism.L2.Th1.B.cubeE`, a second name).

*Proof.* Since $\varphi_E(0) = 0$, the first two claims hold as in the [first level theorem](/entry/first-level-all-formal-groups/). If $H \simeq H'$, then $d_1 H \simeq d_1 H'$: each of the three terms of $d_1$ is a substitution of integral series with constant term $0$, and the rules for $\simeq$ apply. By the comparison lemma, $d_1 H_E \simeq d_1 H$, and by the first level theorem, $d_1 H \simeq 0$. So $d_1 H_E \simeq 0$, and $d_1 H_E^{\mathrm{sw}} = d_1 H_E \simeq 0$. $\square$

Now we add the endomorphism. Let $l^{-1}$ be the inverse series of $l$, so $l(l^{-1}(X)) = X = l^{-1}(l(X))$. For $\alpha \in K$ put $[\alpha](X) = l^{-1}(\alpha \, l(X))$. Let $\mathcal{O} = \{a \in K : |a| \leq 1\}$. An element $c \in K$ is a *binomial scalar* if $\binom{c}{n} = c(c-1)\cdots(c-n+1)/n! \in \mathcal{O}$ for all $n \geq 0$. For example, every integer is a binomial scalar. Since $\binom{c}{n}$ is continuous in $c$, so is every element of the closure of $\mathbb{Z}$ when $\mathcal{O}$ is closed. We use the same words for any subring $R$ in place of $\mathcal{O}$.

**Definition 8.3.5 (Fibre data).** Let $\iota$ be a finite set, and for $Q \in \iota$ let $c_Q \in K$ and $w^+_Q, w^-_Q \in K[[z]]$. Let $\alpha, S \in K$. Put $W_c = 1 + z^2 (P - c)$, so that $W_c = z^2(\wp - c)$. The data are *fibre data* for the series $e_1 + \kappa w$ if

1. for each $Q$, $(\log W_{c_Q})'' = 2P - w^+_Q - w^-_Q$;
2. $\alpha^2 (e_1 + \kappa w)(\alpha z) = \sum_Q (w^+_Q + w^-_Q) - S$.

Over $\mathbb{C}$, take $c_Q = \wp(Q)$ and $w^\pm_Q = \wp(z \pm Q)$. Item 1 is the classical identity $(\log(\wp(z) - \wp(Q)))'' = -\wp(z + Q) - \wp(z - Q) + 2\wp(z)$. Item 2 says that $\wp(\alpha z + \omega/2)$ is, up to the factor $\alpha^2$ and a constant, the sum of $\wp$ over a fibre of $\alpha$.

**Lemma 8.3.6 (Isogeny relation for theta).** Let $P$ be a Weierstrass series, $e_1$ a root of the cubic, and fibre data as above with $(\alpha^2 - 2|\iota|) s_2 = S$. Then
$$
\theta(\alpha z) \, W_{e_1}^{|\iota|} = \theta(z)^{2|\iota|} \prod_{Q \in \iota} W_{c_Q} .
$$

Lean: `Formalism.L2.Th1.B.th0Isogeny`.

*Proof.* Compare the logarithms of the two sides. Their values and first derivatives at $0$ are $0$. Their second derivatives agree: on the left, $(\log \theta)''(z) = -(e_1 + \kappa w) - s_2$ and $(\log W_{e_1})'' = 2P - 2(e_1 + \kappa w)$, the case of the $2$-isogeny; on the right, item 1 of the fibre data. Item 2 and the relation for $S$ match the terms. $\square$

**Lemma 8.3.7 (Norm relation).** Let $P$ be a Weierstrass series for $(g_2, g_3)$, let $x_T, c_0 \in K$ with $|x_T| \leq 1$ such that $e_1 = x_T + c_0$ is a root of $4t^3 - g_2 t - g_3$, and let $l, l^{-1}$ be inverse series with $l(0) = 0$ and $l'(0) = 1$. Let $F \in K[[X_0, X_1]]$ and $i, e_p \in K[[X]]$ satisfy items 1 and 2 of a [Weierstrass parameter](/entry/par-three/) with this $c_0$. Let $x_Q \in K$ with $|x_Q| \leq 1$ for $Q \in \iota$. Assume fibre data with $c_Q = x_Q + c_0$, that $\alpha \bar\alpha = 2|\iota|$ and $\alpha(\alpha - \bar\alpha) s_2 = S$. Then $\varphi_E([\alpha] X) - \alpha \bar\alpha \, \varphi_E(X)$ has constant term $0$ and its exponential has coefficients in $\mathcal{O}$.

Lean: `Formalism.L2.Th1.B.phENorm`.

*Proof.* Since $\alpha \bar\alpha = 2|\iota|$, the relation for $S$ is $(\alpha^2 - 2|\iota|) s_2 = S$. Substitute $z = l(X)$ in the isogeny relation and take $-\log$. Then $l([\alpha]X) = \alpha l(X)$ turns $\theta(\alpha z)$ into $\exp(-\varphi_E([\alpha]X))$. The factors $W_c(l(X))$ are $(l/X)^2 (e_p + (c_0 - c) X^2)$, and for $c = e_1$ and $c = c_Q$ the second factor is integral with constant term $1$, since $|x_T|, |x_Q| \leq 1$. The factors $(l/X)^2$ cancel, as both sides contain $|\iota|$ pairs of them. $\square$

The last input is a vanishing theorem for a series on a formal group that is quadratic up to integral terms. It holds for any closed subring $R$ of a topological field $K$ of characteristic $0$. A *point* is a power series in any set of variables with constant term $0$ and coefficients in $R$. Write $f \equiv g$ if $f - g$ has constant term $0$ and $\exp(f - g)$ has coefficients in $R$. For inverse series $l, l^{-1}$ write $x +_l y = l^{-1}(l(x) + l(y))$ and $B(x, y) = \varphi(x +_l y) - \varphi(x) - \varphi(y)$.

**Theorem 8.3.8 (Split vanishing).** Let $K$ be a topological field of characteristic $0$ with a topological ring structure, and $R \subseteq K$ a closed subring. Let $l, l^{-1} \in K[[X]]$ with $l(0) = 0$, $l'(0) = 1$, $l^{-1}(0) = 0$ and $l \circ l^{-1} = X = l^{-1} \circ l$, such that $X_0 +_l X_1$ has coefficients in $R$. Let $\varphi \in K[[X]]$ with $\varphi(0) = 0$, and assume $B(x +_l x', y) \equiv B(x, y) + B(x', y)$ for all points $x, x', y$. Let $\alpha, \bar\alpha \in K$ such that $[\alpha]$ has coefficients in $R$, $\alpha$ lies in the closure of $\mathbb{Z}$, $\varphi([\alpha]X) \equiv \alpha \bar\alpha \, \varphi(X)$, $\alpha \neq 0$, $\alpha \neq \bar\alpha$, $\bar\alpha \neq 1$, and $(\alpha(\alpha - \bar\alpha))^{-1}$ and $(\alpha(1 - \bar\alpha))^{-1}$ are binomial scalars for $R$. Then $\varphi \equiv 0$.

Lean: `Formalism.L2.Th1.B.Split.split_vanishing_at_two`.

*Proof.* If $f \equiv 0$ and $c$ is a binomial scalar, then $c f \equiv 0$, because $\exp(c f) = \sum_n \binom{c}{n} (\exp f - 1)^n$. Additivity gives $B([n]x, y) \equiv n B(x, y)$ for $n \in \mathbb{Z}$, and by continuity $B([\alpha]x, y) \equiv \alpha B(x, y)$; by symmetry the same holds in $y$. So $B([\alpha]x, [\alpha]y) \equiv \alpha^2 B(x, y)$. The norm relation gives $B([\alpha]x, [\alpha]y) \equiv \alpha \bar\alpha B(x, y)$. So $\alpha(\alpha - \bar\alpha) B \equiv 0$, and multiplying by the binomial scalar $(\alpha(\alpha - \bar\alpha))^{-1}$ gives $B \equiv 0$. Then $\varphi([n]X) \equiv n \varphi(X)$ for $n \in \mathbb{Z}$, and by continuity $\varphi([\alpha]X) \equiv \alpha \varphi(X)$. With the norm relation, $\alpha(1 - \bar\alpha) \varphi \equiv 0$, and the second binomial scalar gives $\varphi \equiv 0$. $\square$

**Theorem 8.3.9 (Integrality of theta at a point of order two).** Assume the hypotheses of the cocycle theorem, with $(x_T, y_T)$ an integral point of order two. Let $l^{-1}$ be the inverse series of $l$. Let $\iota$ be a finite set, $x_Q \in K$ with $|x_Q| \leq 1$, and $(c_Q = x_Q + c_0, w^\pm_Q, \alpha, S)$ fibre data for $e_1 + \kappa w$. Let $\bar\alpha \in K$ with $\alpha \bar\alpha = 2|\iota|$ and $\alpha(\alpha - \bar\alpha) s_2 = S$. Assume that $[\alpha]$ has coefficients in $\mathcal{O}$, that $\alpha$ lies in the closure of $\mathbb{Z}$, that $\alpha \neq 0$, $\alpha \neq \bar\alpha$, $\bar\alpha \neq 1$, and that $(\alpha(\alpha - \bar\alpha))^{-1}$ and $(\alpha(1 - \bar\alpha))^{-1}$ are binomial scalars. Then $\varphi_E \simeq 0$, and $\theta(l(X))$ has constant term $1$ and integral coefficients.

Lean: `Formalism.L2.Th1.B.th0Vanish`.

*Proof.* By the cocycle theorem, $d_1 \operatorname{cob} \varphi_E \simeq 0$. From this and $\varphi_E(0) = 0$, the result on the first level from a universal law gives two facts: the law $l^{-1}(l(X_0) + l(X_1))$, which is $F$, has coefficients in $\mathcal{O}$, and $B$ is additive up to $\equiv$. The norm relation gives $\varphi_E([\alpha]X) \equiv \alpha \bar\alpha \varphi_E(X)$. The split vanishing theorem gives $\varphi_E \equiv 0$, which is $\varphi_E \simeq 0$. Then $\theta(l) = \exp(-\varphi_E)$ is integral with constant term $1$. $\square$

**Remark 8.3.10 (Formalization).** The cocycle theorem uses only the third item of the [first level theorem](/entry/first-level-all-formal-groups/); the integrality of the jets is not used. The comparison lemma divides by $2$ in $K$ and does not need $|2| = 1$. Its two identities are `Formalism.L2.Th1.B.gCob` and `Formalism.L2.Th1.B.lDiv`; their proofs were not unfolded. The step from $d_1 \operatorname{cob} \varphi_E \simeq 0$ to integrality of $F$ and additivity of $B$ is `Formalism.L2.Th1.C.first_level_from_universal_law`, whose proof was not unfolded. In [CocycleDiffExpEquiv.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/LogarithmicSubstitution/CocycleDiffExpEquiv.lean#L162) a section variable asks for a $\mathbb{Q}_2$-algebra structure on $K$; no result uses it. The rule $H \simeq H' \Rightarrow d_1 H \simeq d_1 H'$ has the second name `Formalism.L2.Th1.B.first_cocycle_simeq_zero`, which does not describe it. The integrality theorem uses only $d_1 H_E \simeq 0$ from the cocycle theorem. Its name speaks of vanishing, but it states integrality. The ring $\mathcal{O}$ is `Formalism.G.unitBall`, defined by a `first` tactic that picks a subring from an unrelated file ([Statement.lean](lean:Formalism/FormalGroupLog/Statement.lean#L71)).
