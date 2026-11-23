---
title: The theta function of a half period
decls:
  - Formalism.L2.Th1.B.An2.Th0TwoAnalytic_of
  - Formalism.L2.Th1.B.th0TwoAnalytic
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The theta function of a half period

Let $L \subset \mathbb{C}$ be a lattice with an endomorphism $\alpha$, and let $\omega_0/2$ be a half period. This section moves the normalized theta function of $L$ at $\omega_0/2$ to the formal group of a Weierstrass model over $\mathbb{C}_2$, and proves that its image has integral coefficients when $\alpha$ is a $2$-adic unit and $\bar\alpha$ is not. The proof checks the hypotheses of the [integrality theorem](/entry/th0-vanish/) of the last section. The fibre data come from the classical addition theorems for $\wp$, and the $2$-adic scalar conditions come from $\mathbb{Z}_2$. The [next section](/entry/th0-two-final-of/) derives the conditions on the points from good reduction, and replaces the conditions on $\alpha$ by conditions on its trace and norm.

**Definition 8.4.1 (Normalized theta function).** Let $L = \mathbb{Z}\omega_1 + \mathbb{Z}\omega_2$ be a lattice in $\mathbb{C}$ with Weierstrass functions $\wp$, $\zeta$, $\sigma$ ([lattices and the Weierstrass function](/learn/elliptic-curves/#lattices-and-the-weierstrass-function)). Let $\eta$ be the $\mathbb{R}$-linear map with $\eta(\omega_k) = 2\zeta(\omega_k/2)$, let $A = |\operatorname{Im}(\bar\omega_1 \omega_2)|$ be the covolume, and $H(z, w) = z \bar w / A$. Put
$$
s_2(L) = \frac{\eta(\omega_1) \bar\omega_2 - \eta(\omega_2) \bar\omega_1}{\omega_1 \bar\omega_2 - \omega_2 \bar\omega_1}, \qquad \sigma^*(z) = \sigma(z) \exp\big(-\tfrac{s_2(L)}{2} z^2\big).
$$
For $t \in \mathbb{C}$ with $\sigma^*(t) \neq 0$, the *normalized theta function at $t$* is
$$
\theta_t(z) = \frac{\sigma^*(z + t)}{\sigma^*(t)} \exp\big(-\pi H(z, t)\big).
$$

By the Legendre relation, $\eta(\omega) = s_2(L) \omega + (\pi / A) \bar\omega$ for $\omega \in L$. So $s_2(L)$ is the constant that makes $\zeta(z) - s_2(L) z - (\pi/A) \bar z$ periodic. The factor $\exp(-\pi H(z,t))$ makes $|\theta_t|$ depend only on the class of $t$ in $\mathbb{C}/L$, up to a constant.

Now we fix the $2$-adic setting. Let $\mathbb{C}_2$ be the completion of an algebraic closure of $\mathbb{Q}_2$ ([p-adic numbers](/learn/number-fields/#p-adic-numbers-and-local-fields)). Fix a field isomorphism $\iota : \mathbb{C} \to \mathbb{C}_2$. It is not continuous. Let $W$ be a Weierstrass curve over $\mathbb{C}_2$ with coefficients $a_1, \dots, a_6$, and put $g_2(W) = c_4/12$ and $g_3(W) = c_6/216$. We say that $W$ is *uniformized by $L$ through $\iota$* if $g_2(W) = \iota(g_2(L))$ and $g_3(W) = \iota(g_3(L))$. Then for $t \notin L$, the point
$$
P_t = \Big(\iota \wp(t) - \tfrac{b_2}{12}, \ \tfrac{1}{2}\big(\iota \wp'(t) - a_1 x - a_3\big)\Big)
$$
lies on $W$, and we put $P_t = O$ for $t \in L$. We write $x(P_t)$ for its first coordinate.

Let $\hat W$ be the formal group of $W$ in the parameter $X = -x/y$, with law $F_W$, inverse $i_W$, logarithm $l_W$ and exponential $l_W^{-1}$ ([formal group laws](/learn/formal-groups/#formal-group-laws), [the logarithm](/learn/formal-groups/#the-invariant-derivation-and-the-logarithm)). For a function $f$ holomorphic near $0$ with Taylor series $\sum c_n z^n$, its *transport* is
$$
f^{\iota} = \sum_n \iota(c_n) \, l_W(X)^n \in \mathbb{C}_2[[X]] .
$$
Let $P_W$ be the constant term part of the Laurent series of $\wp$ for $W$, that is, $\wp_W(z) = z^{-2} + P_W(z)$. If $W$ is uniformized by $L$, then $P_W$ is the image under $\iota$ of the Taylor series of $\wp(z) - z^{-2}$.

**Lemma 8.4.2 (Formal group of an integral model).** Let $K$ be a field of characteristic $0$ with an ultrametric absolute value, and $W$ a Weierstrass curve over $K$ with $|a_k| \leq 1$ for all $k$. Put $e_W = X^2 x(X)$. Then $P_W$ is a [Weierstrass series](/entry/frob-stick-log/) for $(g_2(W), g_3(W))$, $F_W$ is a law with logarithm $l_W$ and inverse $i_W$, $l_W$ and $l_W^{-1}$ are inverse series, and $(F_W, l_W, i_W)$ is a [Weierstrass parameter](/entry/par-three/) for $P_W$ with data $(e_W, b_2/12, a_1, a_3)$.

Lean: `Formalism.L2.Th1.A.bridgeWp`, `Formalism.L2.Th1.A.bridgeLaw`, `Formalism.L2.Th1.A.bridgeCurve`, `Formalism.L2.Th1.A.bridgeCurve3`, `Formalism.L2.Th1.B.Crv2.logPair`.

*Proof.* By Silverman, Ch. IV, §1, $w(X) = X^3(1 + \cdots)$ has coefficients in $\mathbb{Z}[a_1, \dots, a_6]$, and so do $e_W = X^3 / w$, $F_W$ and $i_W$. The change of variables $x \mapsto x + b_2/12$ turns $W$ into $Y^2 = 4x^3 - g_2 x - g_3$, which gives $\wp_W(l_W) = x + b_2/12$ and $\wp_W'(l_W) = 2y + a_1 x + a_3$: these are items 1 and 3. The function $x(P) - x(Q)$ vanishes on $Q = P$ and $Q = -P$, which gives the factor $F_W(X_0, i_W X_1) F_W(X_0, X_1)$ of item 2. Item 4 is the same argument for the determinant, which vanishes when two points are equal or when the three points are collinear, that is, sum to $O$. $\square$

**Lemma 8.4.3 (Points of order two).** Let $W$ be as in the last lemma, and let $(x_T, y_T)$ be a point of $W$ with $2 y_T + a_1 x_T + a_3 = 0$ and $|x_T| \leq 1$. Then $(x_T, y_T)$ is an [integral point of order two](/entry/cube-e-of/) for the data $(g_2(W), g_3(W), b_2/12, a_1, a_3)$.

Lean: `Formalism.L2.Th1.A.bridgeTwoMore`, `Formalism.L2.Th1.B.Crv2.twoHyp`.

*Proof.* Put $g(x) = 4x^3 + b_2 x^2 + 2 b_4 x + b_6$. The curve equation is $(2y + a_1 x + a_3)^2 = g(x)$, so $g(x_T) = 0$. Under $x = e - b_2/12$, $g$ becomes $4e^3 - g_2(W) e - g_3(W)$, so $e_1 = x_T + b_2/12$ is a root. Next, $y_T$ is a root of the monic equation $y^2 + (a_1 x_T + a_3) y = x_T^3 + a_2 x_T^2 + a_4 x_T + a_6$ with integral coefficients, so $|y_T| \leq 1$. Finally $\kappa = 3 e_1^2 - g_2(W)/4 = g'(x_T)/4$, and with $b_2 = a_1^2 + 4a_2$, $b_4 = 2a_4 + a_1 a_3$ this is
$$
\kappa = 3 x_T^2 + 2 a_2 x_T + a_4 + \tfrac{1}{2} a_1 (a_1 x_T + a_3) = 3 x_T^2 + 2 a_2 x_T + a_4 - a_1 y_T ,
$$
which has absolute value at most $1$. $\square$

The fibre data come from three classical facts on a lattice with an endomorphism. Let $\alpha \in \mathbb{C}$, $\alpha \neq 0$, with $\alpha L \subseteq L$. A finite set $S \subset \mathbb{C}$ is a *set of kernel representatives* for $\alpha$ if its elements are distinct modulo $L$, lie outside $L$, satisfy $\alpha P \in L$, and every $z \notin L$ with $\alpha z \in L$ is congruent to an element of $S$. Such sets exist.

**Lemma 8.4.4 (Degree and quasi-period of an isogeny).** Let $S$ be a set of kernel representatives for $\alpha$. Then $|S| + 1 = |\alpha|^2$ and
$$
(\alpha^2 - |\alpha|^2) \, s_2(L) = \sum_{P \in S} \wp(P) .
$$

Lean: `Formalism.L2.Th1.F.kerRepsCard`, `Formalism.L2.Th1.F.quasiPeriodConstIsogeny`.

*Proof.* The degree of $z \mapsto \alpha z$ on $\mathbb{C}/L$ is $[L : \alpha L] = |\alpha|^2$, and $S \cup \{0\}$ is its kernel. The function $\alpha^2 \wp(\alpha z) - \sum_{P \in S \cup \{0\}} \wp(z + P)$ is elliptic without poles, so it is constant, and the Laurent expansion at $0$ gives $\alpha^2 \wp(\alpha z) = \sum_{P} \wp(z + P) - \sum_{P \in S} \wp(P)$. Integrate: $\alpha \zeta(\alpha z) = \sum_P \zeta(z + P) + (\sum_S \wp(P)) z + c$. Replace $z$ by $z + \omega$ with $\omega \in L$ and use $\eta(\omega) = s_2 \omega + (\pi/A)\bar\omega$. The left side changes by $\alpha (s_2 \alpha \omega + (\pi/A) \bar\alpha \bar\omega)$ and the right side by $|\alpha|^2 (s_2 \omega + (\pi/A) \bar\omega) + (\sum_S \wp(P)) \omega$. Compare the coefficients of $\omega$. $\square$

**Lemma 8.4.5 (Half fibres).** Let $\omega_0 \in L$ and assume $2z \notin L$ whenever $\alpha z - \omega_0/2 \in L$. Then there is a finite set $S_{1/2} \subset \mathbb{C}$ such that $\alpha Q - \omega_0/2 \in L$ and $2Q \notin L$ for $Q \in S_{1/2}$, no two elements are congruent up to sign modulo $L$, and each $z$ with $\alpha z - \omega_0/2 \in L$ is congruent to $Q$ or $-Q$ for some $Q \in S_{1/2}$. If $\omega_0/2 \notin L$ and $S$ is a set of kernel representatives, then $2|S_{1/2}| = |S| + 1$.

Lean: `Formalism.L2.Th1.B.halfFibreExists`, and the count is part of `Formalism.L2.Th1.B.fibreZInstance`.

*Proof.* The fibre of $\omega_0/2$ modulo $L$ is a coset of the kernel, so it has $|S| + 1$ classes. Since $\omega_0 \in L$, it is stable under $z \mapsto -z$, and by assumption this map has no fixed class. Pick one element from each pair $\{z, -z\}$. $\square$

**Lemma 8.4.6 (Fibre data over $\mathbb{C}$).** In the setting of the last lemma, with $\omega_0/2 \notin L$, put $e_1 = \wp(\omega_0/2)$ and $\kappa = 3e_1^2 - g_2(L)/4$. Then, as Taylor series at $0$,
$$
\wp(z + \tfrac{\omega_0}{2}) = e_1 + \frac{\kappa}{\wp(z) - e_1},
$$
and the data $c_Q = \wp(Q)$, $w^{\pm}_Q = \wp(z \pm Q)$ for $Q \in S_{1/2}$, with the scalar $\alpha$ and the constant $\sum_{P \in S} \wp(P)$, are [fibre data](/entry/th0-vanish/) for $\wp(z + \omega_0/2)$ and the series $\wp(z) - z^{-2}$.

Lean: `Formalism.L2.Th1.B.halfShiftSeries`, `Formalism.L2.Th1.B.fibreZInstance`.

*Proof.* The first identity is the addition formula for $\wp$ at a half period (Whittaker and Watson, Ch. XX). Item 1 of fibre data is $\frac{d^2}{dz^2} \log(\wp(z) - \wp(Q)) = 2\wp(z) - \wp(z+Q) - \wp(z-Q)$, which follows from $\wp(z) - \wp(Q) = -\sigma(z+Q)\sigma(z-Q)/(\sigma(z)^2\sigma(Q)^2)$. For item 2, take $u_0$ with $\alpha u_0 = \omega_0/2$ and put $z + u_0$ in the identity of the last proof: $\alpha^2 \wp(\alpha z + \omega_0/2)$ is the sum of $\wp(z + u)$ over the fibre, minus $\sum_S \wp(P)$, and the fibre is $\{\pm Q\}$. $\square$

Fibre data over $\mathbb{C}$ map to fibre data over $\mathbb{C}_2$ under $\iota$, applied to all coefficients, since the conditions are ring identities (Lean: `Formalism.L2.Th1.B.fibreMap`).

**Lemma 8.4.7 (Scalars from $\mathbb{Z}_2$).** Let $K$ be a field of characteristic $0$ with an ultrametric absolute value that is a normed algebra over $\mathbb{Q}_2$. Let $F$ be a law with logarithm $l$, $l^{-1}$ the inverse series of $l$, and $b, b' \in \mathbb{Z}_2$ with $|b| = 1$ and $|b'| < 1$. Put $\alpha = b$ and $\bar\alpha = b'$ in $K$. Then $[\alpha]$ is integral, $\alpha$ lies in the closure of $\mathbb{Z}$, $\alpha \neq 0$, $\alpha \neq \bar\alpha$, $\bar\alpha \neq 1$, and $(\alpha(\alpha - \bar\alpha))^{-1}$ and $(\alpha(1 - \bar\alpha))^{-1}$ are binomial scalars.

Lean: `Formalism.L2.Th1.B.twoAdicScalars`.

*Proof.* $\mathbb{Z}$ is dense in $\mathbb{Z}_2$, and the map $\mathbb{Z}_2 \to K$ is continuous. The set of $c$ with $[c]$ integral is closed and contains $\mathbb{Z}$, because $F$ is integral; the same holds for binomial scalars. So every element of $\mathbb{Z}_2$ has both properties. The three inequalities follow from $|b| = 1$, $|b'| < 1$. Since $|b - b'| = |1 - b'| = 1$, the elements $b(b - b')$ and $b(1 - b')$ are units of $\mathbb{Z}_2$, so their inverses lie in $\mathbb{Z}_2$. $\square$

**Theorem 8.4.8 (Integrality of the theta function of a half period).** Let $L$ be a lattice, $\iota : \mathbb{C} \to \mathbb{C}_2$ a field isomorphism, and $W$ a Weierstrass curve over $\mathbb{C}_2$, uniformized by $L$ through $\iota$, with $|a_k| \leq 1$ for all $k$. Let $\alpha, \omega_0 \in \mathbb{C}$ and $b, b' \in \mathbb{Z}_2$ with $\alpha \neq 0$, $\alpha L \subseteq L$, $\omega_0 \in L$, $\omega_0/2 \notin L$, $\iota(\alpha) = b$, $\iota(\bar\alpha) = b'$, $|b| = 1$ and $|b'| < 1$. Assume that $2z \notin L$ whenever $\alpha z - \omega_0/2 \in L$, that $|x(P_{\omega_0/2})| \leq 1$, and that $|x(P_z)| \leq 1$ whenever $\alpha z - \omega_0/2 \in L$. Let $\varphi_E$ be the [even sigma logarithm](/entry/cube-e-of/) of $W$ for $s_2 = \iota(s_2(L))$ and $x_T = x(P_{\omega_0/2})$. Then $\varphi_E \simeq 0$, and the transport $\theta_{\omega_0/2}^{\iota}$ has constant term $1$ and coefficients of absolute value at most $1$.

Lean: `Formalism.L2.Th1.B.th0TwoAnalytic` (also `Formalism.L2.Th1.B.An2.Th0TwoAnalytic_of`, the same result from the four lemmas on half fibres, fibre data, the half shift and the transfer of fibre data).

*Proof.* Choose $S_{1/2}$ and a set $S$ of kernel representatives. By the lemma on fibre data, and after applying $\iota$, we get fibre data over $\mathbb{C}_2$ for $\iota(e_1) + \iota(\kappa) w$ and $P_W$, with $c_Q = \iota \wp(Q) = x(P_Q) + b_2/12$. Here $\iota(e_1) = x_T + b_2/12$, and $\iota(\kappa) = 3\iota(e_1)^2 - g_2(W)/4$ since $W$ is uniformized by $L$. Since $\wp'(\omega_0/2) = 0$, the point $P_{\omega_0/2} = (x_T, y_T)$ has $2y_T + a_1 x_T + a_3 = 0$, so by the lemma on points of order two it is an integral point of order two. The lemma on integral models gives the Weierstrass parameter. Each $Q \in S_{1/2}$ lies in the fibre, so $|x(P_Q)| \leq 1$. The degree lemma gives $\iota(\alpha)\iota(\bar\alpha) = |\alpha|^2 = |S| + 1 = 2|S_{1/2}|$ and $\iota(\alpha)(\iota(\alpha) - \iota(\bar\alpha)) \iota(s_2(L)) = \iota(\sum_S \wp(P))$. The lemma on scalars from $\mathbb{Z}_2$ gives the conditions on $\alpha$ and $\bar\alpha$. So the [integrality theorem](/entry/th0-vanish/) applies and gives $\varphi_E \simeq 0$. Last, $\theta_{\omega_0/2}^{\iota} = \exp(-\varphi_E)$, and $\varphi_E \simeq 0$ means that this series has constant term $1$ and integral coefficients. $\square$

**Remark 8.4.9 (Formalization).** The identity $\theta_{\omega_0/2}^{\iota} = \exp(-\varphi_E)$ is `Formalism.L2.Th1.E.inWTh0`. Its proof, and the proofs of the lemmas on integral models, on the degree and quasi-period, and on fibre data, were not unfolded; the proofs above are the classical arguments. The hypothesis on $|x(P_z)|$ is used only at the points of $S_{1/2}$. The integral model is asked only for $|a_k| \leq 1$; good reduction is not needed here. The file [FinalJ.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/FinalJ.lean#L12) also proves a result on points at $2$ that no result of this chapter uses.
