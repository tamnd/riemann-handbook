---
title: Jets of phase functions on formal groups
decls:
  - jets_phase_weights
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Jets of phase functions on formal groups

This section proves that a phase function on the formal group of a Weierstrass curve has integral jets, if the function is almost additive. Here "almost additive" means that the defect of additivity has an integral exponential. The result has three parts. Jets of order other than $1$ and $2$ are integral. The jet of order $1$ is integral when $p \neq 2$ and the function is even. The jet of order $2$ is integral after multiplication by $a - b$ when the defect is balanced between $a$ and $b$. The theorem is used in the proof that [all phase jets are integral](/entry/jets-ph-all/). The background on power series is in [polynomials and power series](/learn/algebra/#polynomials-and-power-series).

### Power series over the $p$-adic numbers

Let $p$ be a prime and let $\mathbb{C}_p$ be the completion of an algebraic closure of $\mathbb{Q}_p$. An element $x \in \mathbb{C}_p$ is *integral* if $|x|_p \leq 1$. A power series in any number of variables is *integral* if all its coefficients are integral.

For a power series $F$ in variables $x_\sigma$, put
$$\exp^{\flat}(F)_\alpha = \sum_{n=0}^{|\alpha|} \frac{\operatorname{coeff}_\alpha(F^n)}{n!},$$
where $|\alpha|$ is the total degree of the monomial $\alpha$. When the constant term of $F$ is $0$, this is the exponential of $F$, because $F^n$ has no terms of degree less than $n$.

**Definition 4.1.1 (Congruence of phases).** Two power series $f$ and $g$ are *congruent*, written $f \simeq g$, if the constant term of $f - g$ is $0$ and $\exp^{\flat}(f - g)$ is integral.

So $f \simeq g$ means that $f - g$ is a phase whose exponential has integral coefficients. For example $p x \simeq 0$, because the coefficient $p^n / n!$ of $\exp(p x)$ is integral for every $n$.

For a power series $f$ in one variable $X$, let $\partial f = \sum_{n \geq 0} (n+1) \operatorname{coeff}_{n+1}(f) X^n$ be its formal derivative.

### The formal logarithm of a Weierstrass curve

Let $W$ be a Weierstrass curve over $\mathbb{C}_p$ with coefficients $a_1, a_2, a_3, a_4, a_6$.

**Definition 4.1.2 (The series $w$).** A power series $w$ in $X$ is a *solution of the Weierstrass recursion* for $W$ if
$$w = 1 + a_1 X w + a_2 X^2 w + a_3 X^3 w^2 + a_4 X^4 w^2 + a_6 X^6 w^3.$$

**Definition 4.1.3 (Invariant differential and formal logarithm).** For such $w$ put
$$\omega = \frac{-2 w - X\, \partial w}{w\, (a_1 X + a_3 X^3 w - 2)},$$
where the quotient is the product with the inverse in the ring of power series. The *formal logarithm* is
$$\log_W(X) = \sum_{n \geq 1} \frac{\operatorname{coeff}_{n-1}(\omega)}{n} X^n.$$

This is the usual construction, as in Silverman, Chapter IV. The series $w$ there is $X^3$ times ours, and $\omega$ is the expansion of the invariant differential divided by $dX$.

Fix a power series $l$ in one variable and a power series $e$ with constant term $0$. For power series $a$ and $b$ in several variables, and $c \in \mathbb{C}_p$, define
$$a \oplus b = e(l(a) + l(b)), \qquad [c]\, a = e(c\, l(a)).$$
For a power series $\varphi$ in one variable put $\varphi(a) = \varphi \circ a$, and define the *bilinear defect*
$$\beta_\varphi(a, b) = \varphi(a \oplus b) - \varphi(a) - \varphi(b).$$
With three variables $x, y, z$, the *cubic defect* is
$$\begin{aligned} \kappa_\varphi = {} & \varphi((x \oplus y) \oplus z) - \varphi(x \oplus y) - \varphi(y \oplus z) - \varphi(z \oplus x) \\ & + \varphi(x) + \varphi(y) + \varphi(z). \end{aligned}$$
The *jet of order $i$* of $\varphi$ along $e$ is
$$j_i(\varphi) = i! \cdot \operatorname{coeff}_i(\varphi \circ e).$$

When $l = \log_W$ and $e$ is a compositional inverse with $l \circ e = X$, the operation $\oplus$ is the formal group law of $W$ read in the coordinate $e$, and $[c]$ is multiplication by $c$.

### The theorem

**Theorem 4.1.4 (Integral phase jets).** The following three statements hold for every prime $p$, every Weierstrass curve $W$ over $\mathbb{C}_p$ with integral coefficients, every solution $w$ of the Weierstrass recursion, and all power series $e$ and $\varphi$ in one variable such that $e$ has constant term $0$ and $\log_W \circ e = X$. All operations are formed with $l = \log_W$.

1. If $\kappa_\varphi \simeq 0$, then $j_i(\varphi)$ is integral for every $i \neq 1, 2$.
2. If $p \neq 2$ and $\varphi([-1] x) \simeq \varphi(x)$, then $j_1(\varphi)$ is integral.
3. If $a, b \in \mathbb{C}_p$ and $\beta_\varphi([a] x, y) \simeq \beta_\varphi(x, [b] y)$, then $(a - b)\, j_2(\varphi)$ is integral.

Lean: `jets_phase_weights`.

*Proof.* This is a reduction to the case of a general logarithm. Say that a pair $(l, e)$ is *admissible* if $e$ has constant term $0$, $l \circ e = X$, and $\partial l$ has an integral inverse $v$, that is $v\, \partial l = 1$ with $v$ integral. The proof applies a gluing lemma to four proved results.

First, $\partial \log_W$ has an integral inverse for every $W$ with integral coefficients and every solution $w$. Since $\partial \log_W = \omega$, this says that $\omega^{-1}$ is integral. Together with the hypotheses $e(0) = 0$ and $\log_W \circ e = X$, it shows that $(\log_W, e)$ is admissible.

Second, for every admissible pair $(l, e)$ and every $\varphi$ with $\kappa_\varphi \simeq 0$, the jets $j_i(\varphi)$ are integral for $i \neq 1, 2$. This general form is itself proved from eight lemmas on the cubic defect.

Third, for every admissible pair, $p \neq 2$ and $\varphi([-1]x) \simeq \varphi(x)$ give an integral $j_1(\varphi)$.

Fourth, for every admissible pair, $\beta_\varphi([a]x, y) \simeq \beta_\varphi(x, [b]y)$ gives an integral $(a - b) j_2(\varphi)$.

The gluing lemma says that the first result and the three general forms imply the three parts of the theorem. It instantiates each general form at $(\log_W, e)$, with the integral inverse from the first result. $\square$

The three parts can be used one at a time. Part 1 is the statement for the higher jets, part 2 for the jet of order $1$, and part 3 for the jet of order $2$.

**Remark 4.1.5.** The constant term of $\kappa_\varphi$ is $\varphi(0)$. Indeed, each of the seven terms has the constant term $\varphi(0)$, and the signs add up to $1$. So the hypothesis $\kappa_\varphi \simeq 0$ of part 1 forces $\varphi(0) = 0$. In parts 2 and 3 the constant terms cancel, so those parts make no claim on $\varphi(0)$. The jet $j_0(\varphi) = \varphi(e(0)) = \varphi(0)$ is then $0$ in part 1, which is integral.

**Remark 4.1.6.** Part 3 does not ask for $p \neq 2$. Its conclusion is empty when $a = b$, since then $(a - b) j_2(\varphi) = 0$.

**Example 4.1.7.** Take $\varphi = c\, l$ for a constant $c$. Then $\beta_\varphi(a, b) = c\,(l(a \oplus b) - l(a) - l(b)) = 0$, so $\kappa_\varphi = 0$. Part 1 then says that $i! \operatorname{coeff}_i(c\, l \circ e) = i!\, c\, \operatorname{coeff}_i(X)$ is integral for $i \neq 1, 2$. This is true, since $l \circ e = X$ has no coefficient of degree other than $1$.

**Remark 4.1.8 (Formalization).** The statement is the conjunction of the three parts. The three parts are also available as separate projections of it, in [JetsPhW.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/JetsPhW.lean#L13). The cubic defect has no term for $\varphi(0)$ of its own, so its constant term is $\varphi(0)$ and part 1 assumes $\varphi(0) = 0$, as the first remark says. The exponential in the congruence is the truncated sum of the second subsection; it agrees with the exponential only when the constant term is $0$, which the congruence also asks. The four proved results and the eight lemmas on the cubic defect were not unfolded beyond their statements. The definitions are in [JetsPhW.lean](lean:Formalism/PeriodIntegrals/JetsPhW.lean#L66).
