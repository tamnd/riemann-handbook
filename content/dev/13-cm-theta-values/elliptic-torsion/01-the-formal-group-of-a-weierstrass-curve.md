---
title: The formal group of a Weierstrass curve
decls:
  - Formalism.ELL.formal_group_points_param
  - Formalism.ELL.formal_group_points_hom
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The formal group of a Weierstrass curve

This section describes the points of a Weierstrass curve over a complete non-archimedean field that reduce to the point at infinity. It proves two facts. First, the parameter $u = -x/y$ is a bijection from these points onto the open unit disc, and the series $w$ of the [formal group](/learn/formal-groups/#formal-group-laws) of the curve gives the inverse map. Second, the group law on these points becomes a formal group law $F$ in the parameter. The estimates of the next section rest on these two facts, and through them the torsion results of this chapter.

Throughout, $K$ is a field with an absolute value $|\cdot|$ that satisfies the ultrametric inequality $|a + b| \le \max(|a|, |b|)$, and $K$ is complete. Let $W$ be a [[Weierstrass curve|427N6S6QQW]] over $K$,
$$y^2 + a_1 xy + a_3 y = x^3 + a_2 x^2 + a_4 x + a_6 .$$
We write $W(K)$ for the group of its nonsingular points: the point $O$ at infinity and the nonsingular solutions $(x, y) \in K^2$, with the chord and tangent law ([elliptic curves](/learn/elliptic-curves/#elliptic-curves-and-the-j-invariant)).

### Integral models and the kernel of reduction

**Definition 7.1.1 (Integral model).** The curve $W$ is an *integral model* if $|a_i| \le 1$ for $i = 1, 2, 3, 4, 6$.

On an integral model, a point with $|x| > 1$ also has $|y| > 1$, and these are the points whose reduction modulo the maximal ideal is the point at infinity ([reduction](/learn/elliptic-curves/#reduction-and-minimal-models)).

**Definition 7.1.2 (Kernel of reduction).** Let $W$ be an integral model. The set $E_1$ consists of $O$ and of the nonsingular points $(x, y)$ of $W$ with $|x| > 1$. The *parameter* of a point is $u(O) = 0$ and $u(x, y) = -x/y$.

If $|\Delta| = 1$, then $E_1$ is a subgroup of $W(K)$, and it has no nonzero torsion of order $n$ with $|n| = 1$. The next sections use these two facts.

### The series $w$

The parameter $u = -x/y$ and the function $v = -1/y$ are local coordinates at $O$. In these coordinates $x = u/v$ and $y = -1/v$. Multiply the Weierstrass equation by $v^3$. The result is the equation
$$v = u^3 + a_1 u v + a_2 u^2 v + a_3 v^2 + a_4 u v^2 + a_6 v^3 . \tag{1}$$

**Definition 7.1.3 (The series $w$).** Let $R$ be a commutative ring and $W$ a Weierstrass curve over $R$. A power series $w \in R[[X]]$ is a *solution of (1)* if $w(0) = 0$ and
$$w = X^3 + a_1 X w + a_2 X^2 w + a_3 w^2 + a_4 X w^2 + a_6 w^3 .$$

Equation (1) has exactly one solution in $R[[X]]$, and $w = X^3 + a_1 X^4 + \cdots$ (Silverman, *The Arithmetic of Elliptic Curves*, Proposition IV.1.1). The two theorems below assume a solution $w$ over $K$; by uniqueness it is the series of Silverman.

**Definition 7.1.4 (Value of a series).** For $f = \sum_n f_n X^n \in K[[X]]$ and $t \in K$, put $f(t) = \sum_n f_n t^n$. For $F = \sum_{i, j} F_{ij} X^i Y^j \in K[[X, Y]]$ and $a, b \in K$, put $F(a, b) = \sum_{i, j} F_{ij} a^i b^j$. A series is *integral* if all its coefficients have absolute value at most $1$.

If $f$ is integral and $|t| < 1$, then $|f_n t^n| \to 0$ and the sum converges, because $K$ is complete. The same holds for an integral $F$ and $|a|, |b| < 1$. On the ring of integral series in $X, Y$, the map $F \mapsto F(a, b)$ is then a ring homomorphism.

### The parameter is a bijection onto the disc

**Theorem 7.1.5 (Parametrization of the kernel of reduction).** Let $W$ be an integral model over $K$ and let $w \in K[[X]]$ be a solution of (1).

1. Let $t \in K$ with $0 < |t| < 1$. Then $w(t) \ne 0$, the pair $\bigl(t/w(t), -1/w(t)\bigr)$ is a nonsingular point of $W$, $|t/w(t)| > 1$, and the parameter of this point is $t$.
2. Let $(x, y)$ be a nonsingular point of $W$ with $|x| > 1$, and let $u = -x/y$. Then $0 < |u| < 1$, $x = u/w(u)$ and $y = -1/w(u)$.

Lean: `Formalism.ELL.formal_group_points_param`

*Proof.* Let $\mathcal{O} = \{a \in K : |a| \le 1\}$, a subring of $K$ because $K$ is ultrametric. Equation (1) for the coefficients $a_i \in \mathcal{O}$ has a solution in $\mathcal{O}[[X]]$. Viewed in $K[[X]]$, it is a solution over $K$, so it equals $w$ by uniqueness. Hence $w$ is integral.

Let $|t| < 1$. Then $w(t)$ converges, $|w(t)| \le |t| < 1$, and $w(t)$ satisfies (1) with $u = t$, because evaluation at $t$ is a ring homomorphism on integral series. Write (1) as
$$w(t)\,(1 - E) = t^3, \qquad E = a_1 t + a_2 t^2 + a_3 w(t) + a_4 t\, w(t) + a_6 w(t)^2 .$$
Each term of $E$ has absolute value less than $1$, so $|E| < 1$ and $|1 - E| = 1$. Thus $|w(t)| = |t|^3$. If $t \ne 0$, then $w(t) \ne 0$. Put $x = t/w(t)$ and $y = -1/w(t)$. Equation (1) divided by $w(t)^3$ is the Weierstrass equation at $(x, y)$, so $(x, y)$ lies on $W$. Also $|x| = |t|^{-2} > 1$ and $-x/y = t$. For nonsingularity, suppose that both partial derivatives of the Weierstrass equation vanish at $(x, y)$. Multiply them by powers of $w(t)$. A linear combination, together with (1), gives $w(t)(1 - Q) = 0$ for an element $Q$ with $|Q| < 1$, built from $t$, $w(t)$ and the $a_i$. So $w(t) = 0$, a contradiction. This proves part 1.

Let $(x, y)$ be as in part 2. In the Weierstrass equation, $|x^3|$ is larger than the absolute value of each other term on the right, so the right side has absolute value $|x|^3$. On the left, if $|y| \le |x|$, each term has absolute value at most $|x|^2 < |x|^3$, which is impossible. So $|y| > |x| > 1$, the term $y^2$ dominates the left side, and $|y|^2 = |x|^3$. Hence $u = -x/y$ satisfies $|u| = |x|^{-1/2}$, and $0 < |u| < 1$. The element $v = -1/y$ satisfies (1) at $u$, and so does $v' = w(u)$, by the first paragraph. Subtract the two equations. The difference factors as $(v - v')(1 - E') = 0$, where $E'$ is a polynomial in $u$, $v$ and $v'$ with coefficients in $\mathcal{O}$ and no constant term, so $|E'| < 1$. Thus $v = w(u)$, which gives $y = -1/w(u)$ and $x = -uy = u/w(u)$. $\square$

### The group law in the parameter

Let $L$ be the field of fractions of $K[[X, Y]]$. For a series $s$ with $s(0) = 0$, put $x(s) = s/w(s)$ and $y(s) = -1/w(s)$ in $L$, where $w(s)$ is the substitution of $s$ into $w$. These are the coordinates of the "generic point" with parameter $s$.

**Definition 7.1.6 (Chord series).** A series $F \in K[[X, Y]]$ with $F(0, 0) = 0$ is a *chord series* for $(W, w)$ if the point $\bigl(x(F), y(F)\bigr)$ is the sum of $\bigl(x(X), y(X)\bigr)$ and $\bigl(x(Y), y(Y)\bigr)$ by the chord formulas of $W$ over $L$:
$$\begin{aligned}
\lambda &= \frac{y(X) - y(Y)}{x(X) - x(Y)}, \qquad x(F) = \lambda^2 + a_1 \lambda - a_2 - x(X) - x(Y),\\
y(F) &= -\bigl(\lambda (x(F) - x(X)) + y(X)\bigr) - a_1 x(F) - a_3 .
\end{aligned}$$

The formal group law of $W$ in Silverman, Chapter IV, §1, is a chord series with coefficients in $\mathbb{Z}[a_1, \dots, a_6]$. It has the form $F(X, Y) = X + Y + (\text{terms of degree at least } 2)$.

**Theorem 7.1.7 (The parameter is a homomorphism).** Let $W$ be an integral model over $K$, let $w$ be a solution of (1), and let $F \in K[[X, Y]]$ be an integral chord series for $(W, w)$. Then for all $P, Q \in E_1$,
$$u(P + Q) = F\bigl(u(P), u(Q)\bigr).$$

Lean: `Formalism.ELL.formal_group_points_hom`

*Proof.* The parameters $a = u(P)$ and $b = u(Q)$ have $|a|, |b| < 1$ by [the parametrization theorem](/entry/formal-group-points-param/), so $F(a, b)$ converges. A chord series is unique: its $x$-coordinate $x(F)$ is fixed by the chord formulas, and $x(F)$ determines $F$. So $F$ is the formal group law of $W$, which also has an inverse series $i(X) = -X\psi(X)$ with $F(X, i(X)) = 0$, where $\psi = 1/(1 - a_1 X - a_3 w(X))$. There are four cases.

1. If $P = O$ or $Q = O$, the claim is $F(0, b) = b$ or $F(a, 0) = a$, which holds for a formal group law.
2. If $P = -Q$, then $u(Q) = i(u(P))$ and both sides are $0$.
3. If $x(P) \ne x(Q)$, clear the denominators of the chord formulas. They become polynomial identities in $X$, $Y$, $w(X)$, $w(Y)$, $F$ and $w(F)$ with coefficients in $\mathbb{Z}[a_1, \dots, a_6]$. All these series are integral, and evaluation at $(a, b)$ is a ring homomorphism on integral series. So the same identities hold for $a$, $b$, $w(a)$, $w(b)$, $c = F(a, b)$ and $w(c)$. By the parametrization theorem, $P = (a/w(a), -1/w(a))$ and $Q = (b/w(b), -1/w(b))$. The identities say that $(c/w(c), -1/w(c))$ is the third point on the chord through $P$ and $Q$, reflected, that is $P + Q$. Its parameter is $c$.
4. If $P = Q \ne -Q$, the same argument with the tangent formulas, which hold for the series $F(X, X)$, gives the claim.

In each case $u(P + Q) = F(u(P), u(Q))$. $\square$

The two theorems together say that $u$ is an isomorphism from $E_1$ to the group of the open unit disc with the law $F$. This is Proposition VII.2.2 of Silverman, *The Arithmetic of Elliptic Curves*.

**Remark 7.1.8 (Formalization).** The value $f(t)$ of a series is an unconditional sum in Lean (`tsum`), so it is $0$ when the sum does not converge. The theorems apply it only to integral series on the open disc, where it converges. Both theorems are proved from a list of other results, and the proof term tries each of 22 (for the parametrization) or 6 (for the homomorphism) candidate results on each open goal in turn: [FormalGroupPointsNoTorsion.lean](lean:Formalism/EllipticTorsion/FormalGroupPointsNoTorsion.lean#L85). The parametrization is proved at [FormalGroupPointsParamDef.lean](lean:Formalism/EllipticTorsion/EllipticTorsionProofs/FormalGroupPointsParamDef.lean#L200), and the case analysis of the homomorphism at [FormalGroupPointsHomDef.lean](lean:Formalism/EllipticTorsion/EllipticTorsionProofs/FormalGroupPointsHomDef.lean#L1151).
