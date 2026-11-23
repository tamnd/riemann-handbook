---
title: The Frobenius-Stickelberger formula
decls:
  - Formalism.L2.Th1.B.frobStickLog
  - Formalism.L2.Th1.B.frobStick
  - Formalism.L2.Th1.B.frobStickStar
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Frobenius-Stickelberger formula

This section proves a formal power series form of the Frobenius-Stickelberger formula for three points. It expresses the determinant of the matrix with rows $(1, \wp(z_j), \wp'(z_j))$ through the sigma function. The proof uses only the differential equation of $\wp$, so it holds over each field of characteristic $0$. The next section uses the formula to prove that a certain three-point combination of the logarithm of the sigma function is integral on a formal group. That fact is the base of the whole chapter.

Throughout, $K$ is a field of characteristic $0$. All series are formal power series with coefficients in $K$. For a series $f(z)$ we write $f'$ for its formal derivative, and in $K[[z_0, z_1, z_2]]$ we write $\partial_j$ for the formal partial derivative in $z_j$.

**Definition 8.1.1 (Weierstrass series).** Let $g_2, g_3 \in K$. A series $P \in K[[z]]$ is a *Weierstrass series* for $(g_2, g_3)$ if $P(0) = 0$, every odd coefficient of $P$ is $0$, and
$$
(-2 + z^3 P')^2 = 4 (1 + z^2 P)^3 - g_2 z^4 (1 + z^2 P) - g_3 z^6 .
$$

To see why this is the right object, put $\wp = z^{-2} + P$, a Laurent series. Then $z^2 \wp = 1 + z^2 P$ and $z^3 \wp' = -2 + z^3 P'$. So the identity is the equation $\wp'^2 = 4 \wp^3 - g_2 \wp - g_3$, multiplied by $z^6$. For a lattice $L \subset \mathbb{C}$, the Laurent expansion at $0$ of the [Weierstrass function](/learn/elliptic-curves/#lattices-and-the-weierstrass-function) $\wp_L$ gives a Weierstrass series $P = \wp_L - z^{-2}$ for $(g_2(L), g_3(L))$ (Silverman, Ch. VI, §3). Below we use $\wp$ as a short name for $z^{-2} + P$, but every identity is an identity of power series.

**Definition 8.1.2 (Sigma series).** Let $P$ be a Weierstrass series. Let $S = -\iint P$ be the unique series with $S'' = -P$ and with constant and linear coefficients $0$. The *sigma series* is $\sigma(z) = z \exp(S(z))$. For $s_2 \in K$ the *modified sigma series* is $\sigma^*(z) = \sigma(z) \exp(-\tfrac{s_2}{2} z^2)$.

The series $S$ starts in degree $4$, so $\exp(S)$ is defined. Over $\mathbb{C}$, $\sigma$ is the expansion at $0$ of the Weierstrass sigma function, since $(\log \sigma)'' = -z^{-2} - P = -\wp$. The factor $\exp(-\tfrac{s_2}{2} z^2)$ appears in the theta functions of the later sections.

**Definition 8.1.3 (The three-point series).** In $K[[z_0, z_1, z_2]]$ put $P_j = P(z_j)$ and $P'_j = P'(z_j)$. Let
$$
D = \det \begin{pmatrix} z_0^3 & z_0 (1 + z_0^2 P_0) & -2 + z_0^3 P'_0 \\ z_1^3 & z_1 (1 + z_1^2 P_1) & -2 + z_1^3 P'_1 \\ z_2^3 & z_2 (1 + z_2^2 P_2) & -2 + z_2^3 P'_2 \end{pmatrix},
$$
let $V = (z_0 + z_1 + z_2)(z_0 - z_1)(z_0 - z_2)(z_1 - z_2)$, and for $f \in K[[z]]$ let
$$
E_f = f(z_0 + z_1 + z_2) + \sum_{j < k} f(z_j - z_k) - 3 \sum_{j} f(z_j) .
$$
For $j \neq k$ let $w_{jk} = z_j^2 - z_k^2 + z_j^2 z_k^2 (P_k - P_j)$.

Row $j$ of the matrix is $z_j^3 (1, \wp(z_j), \wp'(z_j))$. So $D = (z_0 z_1 z_2)^3 \det(1, \wp(z_j), \wp'(z_j))$, and $w_{jk} = z_j^2 z_k^2 (\wp(z_k) - \wp(z_j))$. The series $D$, $V$, $E_f$ and $w_{jk}$ have no poles; this is why we use them in place of $\wp$.

**Lemma 8.1.4 (Addition formula for sigma).** Let $P$ be a Weierstrass series. Then in $K[[z_0, z_1]]$
$$
w_{01} = (z_0^2 - z_1^2) \exp\bigl( S(z_0 + z_1) + S(z_0 - z_1) - 2 S(z_0) - 2 S(z_1) \bigr) .
$$

Lean: `Formalism.L2.Th1.B.addSigmaLog`.

*Proof.* Since $P$ is even, $P_1 - P_0$ is divisible by $z_0^2 - z_1^2$, so $w_{01} = (z_0^2 - z_1^2) N$ with $N \in K[[z_0, z_1]]$ and $N(0, 0) = 1$. Let $h$ be the difference of $\log N$ and the exponent on the right. We show that both terms have the same image under the wave operator $\Box = \partial_0^2 - \partial_1^2$. For the exponent, a series $f(z_0 \pm z_1)$ is killed by $\Box$, so $\Box$ of the exponent is $-2 S''(z_0) + 2 S''(z_1) = 2 P_0 - 2 P_1$. For $\log N$, the same holds for $\log(z_0^2 - z_1^2)$, and $\Box \log z_0^2 z_1^2 = -2 z_0^{-2} + 2 z_1^{-2}$. With $u = \wp(z_1) - \wp(z_0)$ one computes
$$
\Box \log u = \frac{-(\wp''(z_0) + \wp''(z_1))\, u + \wp'(z_1)^2 - \wp'(z_0)^2}{u^2} = -2u ,
$$
by $\wp'^2 = 4\wp^3 - g_2 \wp - g_3$ and $\wp'' = 6 \wp^2 - g_2/2$. So $\Box \log N = 2 P_0 - 2 P_1$ too, and $\Box h = 0$. At $z_1 = 0$ both $h$ and $\partial_1 h$ vanish: $\log N$ and the exponent are even in $z_1$, since $P$ and $S$ are even, and they vanish at $z_1 = 0$, since $N = 1$ there and $S(0) = 0$. In characteristic $0$, a series $h$ with $\Box h = 0$ and $h = \partial_1 h = 0$ at $z_1 = 0$ is $0$: the equation $\Box h = 0$ fixes the coefficient of $z_1^{m+2}$ from that of $z_1^m$. So $\log N$ equals the exponent. $\square$

Over $\mathbb{C}$ the lemma is the classical formula $\wp(z_1) - \wp(z_0) = \sigma(z_0 + z_1) \sigma(z_0 - z_1) / (\sigma(z_0)^2 \sigma(z_1)^2)$, multiplied by $z_0^2 z_1^2$.

**Lemma 8.1.5 (Shear uniqueness).** Let $A, B \in K[[z_0, z_1, z_2]]$. Assume $A \, (\partial_1 - \partial_2) B = B \, (\partial_1 - \partial_2) A$, that $A$ and $B$ agree after the substitution $z_2 = 0$, and that $B$ does not vanish after this substitution. Then $A = B$.

Lean: `Formalism.L2.Th1.B.shearLemma`.

*Proof.* Change variables to $z_0$, $s = z_1 + z_2$ and $t = z_2$. This is an invertible linear substitution, so it is an automorphism of the ring of series. In the new variables, $\partial_t$ at fixed $z_0, s$ is $-(\partial_1 - \partial_2)$, and $z_2 = 0$ is $t = 0$. Write $A = \sum_n a_n t^n$ and $B = \sum_n b_n t^n$ with $a_n, b_n \in K[[z_0, s]]$. The hypotheses say $A \, \partial_t B = B \, \partial_t A$, $a_0 = b_0$ and $b_0 \neq 0$. Assume $a_i = b_i$ for $i < n$. The coefficient of $t^{n-1}$ in $A \, \partial_t B - B \, \partial_t A$ is $\sum_{i + j = n} j (a_i b_j - b_i a_j)$. All terms with $i, j < n$ cancel, the term with $j = 0$ is $0$, and the term with $i = 0$ is $n a_0 (b_n - a_n)$. So $n a_0 (b_n - a_n) = 0$. Since $n \neq 0$ in $K$ and $K[[z_0, s]]$ is a domain, $a_n = b_n$. $\square$

**Lemma 8.1.6 (Derivative rules).** Let $P$ be a Weierstrass series. Then for $j \neq k$
$$
(z_j - z_k)(\partial_j - \partial_k) w_{jk} = w_{jk} \bigl( 2 + 2 (z_j - z_k)\bigl( S'(z_j - z_k) - S'(z_j) + S'(z_k) \bigr) \bigr),
$$
and
$$
\begin{aligned}
2 w_{01} w_{02} w_{12} \, (\partial_1 - \partial_2) D = D \bigl( &-(\partial_0 - \partial_1) w_{01} \cdot w_{02} w_{12} + (\partial_0 - \partial_2) w_{02} \cdot w_{01} w_{12} \\
&+ 2 (\partial_1 - \partial_2) w_{12} \cdot w_{01} w_{02} \bigr) .
\end{aligned}
$$

Lean: `Formalism.L2.Th1.B.tauRule`, `Formalism.L2.Th1.B.detRule`.

*Proof.* For the first rule, apply $\partial_j - \partial_k$ to the addition formula. It sends $z_j^2 - z_k^2$ to $2(z_j + z_k)$, a series $f(z_j + z_k)$ to $0$, and $f(z_j - z_k)$ to $2 f'(z_j - z_k)$. Multiply by $z_j - z_k$. For the second rule, write $x_j = z_j^2 \wp(z_j)$ and $y_j = z_j^3 \wp'(z_j)$. Then $D$ and the $w_{jk}$ are polynomials in $z_j, x_j, y_j$. The derivatives of $x_j$ and $y_j$ are given by $\wp' $ and $\wp'' = 6 \wp^2 - g_2/2$, and the points satisfy the curve equation. After multiplication by $z_0 z_1 z_2$, the rule is a polynomial identity in these quantities, which holds modulo the three curve equations. $\square$

**Theorem 8.1.7 (Frobenius-Stickelberger, logarithmic form).** Let $g_2, g_3 \in K$ and let $P$ be a Weierstrass series for $(g_2, g_3)$, with $S = -\iint P$. Then
$$
D = -2 \, V \exp(E_S) .
$$

Lean: `Formalism.L2.Th1.B.frobStickLog`.

*Proof.* Put $B = -2 V \exp(E_S)$. We apply the shear uniqueness lemma to $A = D$ and $B$.

At $z_2 = 0$, the last row of the matrix is $(0, 0, -2)$. So $D$ becomes $-2 z_0^3 z_1^3 (\wp(z_1) - \wp(z_0)) = -2 z_0 z_1 w_{01}$. Also $V$ becomes $z_0 z_1 (z_0^2 - z_1^2)$, and $E_S$ becomes $S(z_0 + z_1) + S(z_0 - z_1) - 2S(z_0) - 2S(z_1)$, since $S(0) = 0$. By the addition formula, $B$ becomes $-2 z_0 z_1 w_{01}$ too. This is not $0$, since $w_{01}$ is $z_0^2 - z_1^2$ times a unit.

For the derivative condition, put $\tau_{jk} = (\partial_j - \partial_k) w_{jk} / w_{jk}$, a series with denominators $z_j - z_k$. The first derivative rule gives $\tau_{jk} = 2/(z_j - z_k) + 2 S'(z_j - z_k) - 2 S'(z_j) + 2 S'(z_k)$. The second gives $(\partial_1 - \partial_2) D / D = \tfrac12 (-\tau_{01} + \tau_{02} + 2 \tau_{12})$. On the other side, $\partial_1 - \partial_2$ kills $z_0 + z_1 + z_2$, so
$$
\begin{aligned}
\frac{(\partial_1 - \partial_2) B}{B} &= -\frac{1}{z_0 - z_1} + \frac{1}{z_0 - z_2} + \frac{2}{z_1 - z_2} \\
&\quad - S'(z_0 - z_1) + S'(z_0 - z_2) + 2 S'(z_1 - z_2) - 3 S'(z_1) + 3 S'(z_2) .
\end{aligned}
$$
This is the same as $\tfrac12(-\tau_{01} + \tau_{02} + 2\tau_{12})$. To stay inside the ring of series, one multiplies all these identities by $2 w_{01} w_{02} w_{12}$, which is not a zero divisor, and cancels it at the end. So $D (\partial_1 - \partial_2) B = B (\partial_1 - \partial_2) D$, and the shear lemma gives $D = B$. $\square$

**Theorem 8.1.8 (Frobenius-Stickelberger, sigma form).** Let $P$ be a Weierstrass series for $(g_2, g_3)$ and $\sigma$ its sigma series. Then
$$
\bigl(\sigma(z_0)\sigma(z_1)\sigma(z_2)\bigr)^3 D = -2 (z_0 z_1 z_2)^3 \, \sigma(z_0 + z_1 + z_2) \prod_{j < k} \sigma(z_j - z_k) .
$$

Lean: `Formalism.L2.Th1.B.frobStick`.

*Proof.* We have $(\sigma(z_0)\sigma(z_1)\sigma(z_2))^3 = (z_0 z_1 z_2)^3 \exp(3 \sum_j S(z_j))$ and $\sigma(z_0 + z_1 + z_2) \prod_{j<k} \sigma(z_j - z_k) = V \exp(S(z_0+z_1+z_2) + \sum_{j<k} S(z_j - z_k))$. Multiply the logarithmic form by the first product and use $\exp(a)\exp(b) = \exp(a+b)$. $\square$

**Theorem 8.1.9 (Frobenius-Stickelberger, modified form).** Let $P$ be a Weierstrass series for $(g_2, g_3)$, let $s_2 \in K$, and let $\sigma^*$ be the modified sigma series. Then
$$
\bigl(\sigma^*(z_0)\sigma^*(z_1)\sigma^*(z_2)\bigr)^3 D = -2 (z_0 z_1 z_2)^3 \, \sigma^*(z_0 + z_1 + z_2) \prod_{j < k} \sigma^*(z_j - z_k) .
$$

Lean: `Formalism.L2.Th1.B.frobStickStar`.

*Proof.* Replace $\sigma$ by $\sigma^*$ in the sigma form. The left side gains the factor $\exp(-\tfrac{3 s_2}{2} \sum_j z_j^2)$, and the right side gains $\exp(-\tfrac{s_2}{2} q)$ with $q = (z_0 + z_1 + z_2)^2 + \sum_{j<k} (z_j - z_k)^2$. Expand: $q = 3 (z_0^2 + z_1^2 + z_2^2)$, because the mixed terms cancel. So the two factors agree. $\square$

Over $\mathbb{C}$, divide by $(z_0 z_1 z_2)^3 (\sigma(z_0)\sigma(z_1)\sigma(z_2))^3$. The sigma form becomes
$$
\det \begin{pmatrix} 1 & \wp(z_0) & \wp'(z_0) \\ 1 & \wp(z_1) & \wp'(z_1) \\ 1 & \wp(z_2) & \wp'(z_2) \end{pmatrix} = \frac{-2 \, \sigma(z_0 + z_1 + z_2) \prod_{j<k} \sigma(z_j - z_k)}{\sigma(z_0)^3 \sigma(z_1)^3 \sigma(z_2)^3} ,
$$
the case of three points of the formula of Frobenius and Stickelberger. In the next section the three points become the three points of a formal group, and the formula says that a determinant built from integral series is a known product.

**Remark 8.1.10 (Formalization).** Each result is a proposition quantified over all fields $K$ of characteristic $0$, and the theorems are proved in one file, one per line ([FinalD.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/FinalD.lean#L14)). The shear lemma is reduced to the version with $\partial_2$ alone, `Formalism.L2.Th1.B.WronskLemma`. The derivative rule for $D$ is proved by one polynomial identity in the points $(x_j, y_j)$, after the factor $z_0 z_1 z_2$ is cancelled. The addition formula is the proposition `Formalism.L2.Th1.B.AddSigmaLog` of [StatementA.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/StatementA.lean#L87), with $\log N$ written as the series $\log(1 - z_0^2 z_1^2 \, q(P))$ of a difference quotient $q(P)$; the wave equation argument is its proof. The constants $g_2, g_3$ enter only through the equation of a Weierstrass series, and $s_2$ is arbitrary.
