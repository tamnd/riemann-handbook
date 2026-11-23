---
title: Honda theory at inert primes
decls:
  - ReciprocityTheory.ChartRestriction.L1.hon_main
  - ReciprocityTheory.ChartRestriction.L1.cm3
  - ReciprocityTheory.ChartRestriction.L1.cmIntegralityThree
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Honda theory at inert primes

This section proves that at a prime $l$ that is inert in $K = \mathbb{Q}(\sqrt{-d})$, the formal group of a good model of a lattice with complex multiplication is isomorphic over the integers of $\breve{\mathbb{Q}}_l$ to the Lubin-Tate formal group of height $2$, by an explicit series. The proof has two parts. The first is an abstract criterion in the style of Honda: a [formal group law](/learn/formal-groups/#formal-group-laws) with an endomorphism that is not defined over the fixed field of Frobenius, and with height at most $2$, has a logarithm of a fixed functional type. The second checks the hypotheses for the curve and then compares the two logarithms. The result is one of the statements on complex multiplication that [the service row from Artin reciprocity](/entry/serv-h-row-of-artin/) depends on.

### The abstract setting

All series below have coefficients in a field $K$ with an absolute value. A series is *integral* if all its coefficients have absolute value at most $1$. For a ring map $\tau$ of $K$ and a series $f$, $f^{\tau}$ is the series with $\tau$ applied to each coefficient.

**Definition 7.6.1 (Frobenius data).** Let $K$ be a complete field of characteristic $0$ with an ultrametric absolute value, $l$ a prime and $\sigma : K \to K$ a ring map. The pair $(K, \sigma)$ is *Frobenius data at $l$* if $|l| < 1$, $|\sigma x| = |x|$ for all $x$, $|\sigma x - x^l| \le |l|$ for all $x$ with $|x| \le 1$, and every $x$ with $|x| < 1$ has $|x| \le |l|$.

The last condition says that $l$ is a uniformizer: the field is absolutely unramified. The third says that $\sigma$ lifts the Frobenius map $x \mapsto x^l$ of the residue field.

**Definition 7.6.2 (Law with logarithm).** A pair $(f, \Phi)$ with $f \in K[[X]]$ and $\Phi \in K[[X, Y]]$ is a *law with logarithm* if $f(0) = 0$, the coefficient of $X$ in $f$ is $1$, $\Phi(0, 0) = 0$, $\Phi$ is integral, and $f(\Phi(X, Y)) = f(X) + f(Y)$.

**Definition 7.6.3 (Honda data).** Let $(K, \sigma)$ be Frobenius data. A *Honda datum* is a law with logarithm $(f, \Phi)$ together with $A \in K[[X]]$ and $a \in K$ such that $A(0) = 0$, $A$ is integral, $f(A(X)) = a f(X)$, $|\sigma a - a| = 1$ and $\sigma(\sigma a) = a$.

So $A$ is an integral endomorphism of the law $\Phi$ with multiplier $a$, and $a$ reduces to an element of the residue field that is not fixed by Frobenius but is fixed by its square.

**Theorem 7.6.4 (Honda type of height two).** Let $(K, \sigma)$ be Frobenius data at $l$ and let $(f, \Phi, A, a)$ be a Honda datum. Let $e \in K[[X]]$ be integral with $e(0) = 0$ and $f(e(X)) = l f(X)$, and suppose that some coefficient of $X^i$ in $e$ with $i \le l^2$ has absolute value $1$. Then there is $c \in K$ with $|c| = 1$ such that
$$f(X) - \frac{c}{l}\, f^{\sigma^2}\bigl(X^{l^2}\bigr)$$
is integral.

Lean: `ReciprocityTheory.ChartRestriction.L1.hon_main`

The series $e$ is the endomorphism "multiplication by $l$" of the law, and the condition on its coefficients says that the law has height at most $2$. The conclusion says that $f$ satisfies the functional equation of Honda for the operator $l - c\,\sigma^2 \circ (X \mapsto X^{l^2})$.

*Proof.* We write $f \equiv g$ if $f - g$ has all coefficients in $l \cdot \{|x| \le 1\}$. There are three steps.

Step 1. Since $A$ commutes with $e$ and $a$ is not fixed by $\sigma$ modulo $l$, the coefficients of $e$ at indices prime to $l^2$ vanish modulo $l$. More precisely, there is an integral series $h$ with $h(0) = 0$, which is a homomorphism modulo $l$ from the law $\Phi^{\sigma^2}$ with endomorphism $A^{\sigma^2}$ to the law $\Phi$ with endomorphism $A$, such that $e \equiv h(X^{l^2})$, and the coefficient of $X$ in $h$ equals the coefficient of $X^{l^2}$ in $e$.

Lean: `ReciprocityTheory.ChartRestriction.L1.hon_shape`

Step 2. Iterating Step 1 with the height condition, there are $c_0, c_1, \ldots \in K$ with $|c_0| = 1$ and $|c_i| \le 1$ such that for each $N$ there is a series $R$ with $R(0) = 0$ and
$$l f \equiv \sum_{i < N} c_i\, f^{\sigma^{2(i+1)}}\bigl(X^{l^{2(i+1)}}\bigr) + R\bigl(X^{l^{2(N+1)}}\bigr).$$

Lean: `ReciprocityTheory.ChartRestriction.L1.hon_series`

Step 3. Put $\tau = \sigma^2$. Since $|c_0| = 1$ and $|l| < 1$, a recursion gives $t_0 = 1, t_1, t_2, \ldots$ with $|t_n| \le 1$ and
$$l\, t_n = \sum_{i < n} t_i\, \tau^i(c_{n - 1 - i}) \qquad (n \ge 2).$$
At each step one divides by the unit $\tau^{n-1}(c_0)$ and absorbs the factor $l$.

Lean: `ReciprocityTheory.ChartRestriction.L1.twisted_division`

Put $c = c_0 - l t_1$. Then $|c| = 1$, because $|l t_1| < 1 = |c_0|$. Fix $n$. Regroup the sum of Step 2 with the weights $t_i$: the identity of Step 3 makes all terms with $i \ge 1$ cancel up to multiples of $l$, and the bound $|t_i| \le 1$ controls the rest. The result is
$$\bigl| l f_n - c\, \sigma^2\bigl(f_{n/l^2}\bigr) \bigr| \le |l|,$$
where $f_m$ is the coefficient of $X^m$ in $f$ and $f_{n/l^2} = 0$ when $l^2 \nmid n$. Dividing by $l$ gives the claim. $\square$

### The curve at an inert prime

Now return to the notation of the previous sections: $d$ is squarefree with $d \equiv 3 \pmod 4$, $\omega_K = (1 + i\sqrt d)/2$, $L$ has complex multiplication by $\mathcal{O}_K$, and $\iota : \mathbb{C} \to \mathbb{C}_l$ is a field isomorphism. Let $(g_2, g_3)$ be a [good model](/entry/good-reduction-of-integral-unramified/) of $L$ at $(l, \iota)$.

Let $c_2 = g_2/20$, $c_3 = g_3/28$ and, for $k \ge 4$,
$$c_k = \frac{3}{(2k+1)(k-3)} \sum_{m=2}^{k-2} c_m c_{k-m}.$$
Put
$$u(X) = X \cdot \frac{1 + \sum_{k \ge 2} c_k X^{2k}}{1 - \sum_{k \ge 2} (k - 1) c_k X^{2k}}, \qquad \ell(X) = \sum_{j \ge 0} \frac{X^{l^{2j}}}{l^j}.$$
Over $\mathbb{C}$, with $g_2, g_3$ the invariants of a lattice, the Laurent series of the Weierstrass function is $\wp(z) = z^{-2}\bigl(1 + \sum_{k \ge 2} c_k z^{2k}\bigr)$, and $u(z) = -2\wp(z)/\wp'(z)$ is the parameter $-x/y$ of the point $(\wp(z), \wp'(z)/2)$. So $u$ is the inverse of the logarithm $f$ of the formal group of the curve $y^2 = x^3 - \frac{g_2}{4}x - \frac{g_3}{4}$ in this parameter. The series $\ell$ is the logarithm of the Lubin-Tate formal group of height $2$ for the uniformizer $l$.

**Theorem 7.6.5 (Formal groups at inert primes).** Let $d$ be squarefree with $d \equiv 3 \pmod 4$, and let $L$ have complex multiplication by $\mathcal{O}_K$. Let $l \ge 5$ be a prime with $l \nmid d$ such that $-d$ is not a square modulo $l$. Let $\iota : \mathbb{C} \to \mathbb{C}_l$ be a field isomorphism, and let $(g_2, g_3)$ be a good model of $L$ at $(l, \iota)$. Then there is $\varepsilon \in \breve{\mathbb{Q}}_l$ with $|\varepsilon| = 1$ such that every coefficient of $u(\varepsilon\, \ell(X))$ lies in $\breve{\mathbb{Q}}_l$ and has absolute value at most $1$.

Lean: `ReciprocityTheory.ChartRestriction.L1.cm3` (also `ReciprocityTheory.ChartRestriction.L1.cmIntegralityThree`)

The condition on $-d$ says that $l$ is inert in $K$. Classically, the curve then has supersingular reduction, and the theorem gives the isomorphism of its formal group with the Lubin-Tate group explicitly.

*Proof.* We work in $\breve{\mathbb{Q}}_l$, which is complete. It has a ring map $\sigma$ such that $(\breve{\mathbb{Q}}_l, \sigma)$ is Frobenius data at $l$, and every monic integral polynomial of positive degree has an integral root modulo $l$.

Lean: `ReciprocityTheory.ChartRestriction.L1.kurFrob` (also `ReciprocityTheory.ChartRestriction.L1.kur_resClosed`)

The element $a = \iota(\omega_K)$ is a root of $X^2 - X + (d+1)/4$. Its discriminant is $-d$, which is a unit and not a square modulo $l$. So $a \in \breve{\mathbb{Q}}_l$, $|a| \le 1$, $|1 - 2a| = 1$, and $\sigma a = 1 - a$, because $\sigma$ must exchange the two roots. Hence $|\sigma a - a| = |1 - 2a| = 1$ and $\sigma(\sigma a) = a$.

Lean: `ReciprocityTheory.ChartRestriction.L1.kur_quad`

Since $|g_2|, |g_3| \le 1$ and $|2| = 1$, the logarithm $f$ and the formal group law $\Phi$ of the curve form a law with logarithm.

Lean: `ReciprocityTheory.ChartRestriction.L1.curve_law`

The series $A = u(a f(X))$ satisfies $f(A) = a f$ and $A(0) = 0$. It is the endomorphism of complex multiplication by $\omega_K$, and it is integral. The proof of integrality writes $A$ through the values of the Weierstrass function of the scaled lattice at the points killed by $\omega_K$. These points are killed by $\omega_K \bar\omega_K = (d+1)/4$, which is prime to $l$ because $-d$ is not a square modulo $l$, so their values are integral as in [the section on torsion points](/entry/tor-kur/). So $(f, \Phi, A, a)$ is a Honda datum.

Lean: `ReciprocityTheory.ChartRestriction.L1.end_integral`

The series $e = u(l f(X))$ is integral, since multiplication by $l$ is an integral endomorphism of any integral law, and the series $e$ with $e(0) = 0$ and $f(e) = l f$ is unique.

Lean: `ReciprocityTheory.ChartRestriction.L1.mulN_integral` (also `ReciprocityTheory.ChartRestriction.L1.mult_unique`)

Some coefficient of $X^i$ in $e$ with $i \le l^2$ has absolute value $1$. To see this, let $S$ be a set of representatives of the $l^2 - 1$ nonzero points of $l^{-1}L'/L'$, where $L'$ is the lattice scaled so that its invariants map to $(g_2, g_3)$. Then $e^2$ is $X^2 U$ times $l^2 \prod_{P \in S}\bigl(x - \iota(\wp(P)) X^2\bigr)$, with $U$ integral and $U(0) = 1$, where $x$ is the series $X^2 x(X)$ of the $x$-coordinate, with constant term $1$. A Gauss norm bound, together with the value $|l^2 \prod_{P \in S}(e_1 - \iota\wp(P))| = 1$ at a $2$-torsion value $e_1$, shows that this product has a unit coefficient at a low index.

Lean: `ReciprocityTheory.ChartRestriction.L1.level_le`

The theorem on Honda type now gives $c$ with $|c| = 1$ such that $f - \frac{c}{l} f^{\sigma^2}(X^{l^2})$ is integral. Since every monic integral polynomial has a root modulo $l$, successive approximation gives $\varepsilon$ with $|\varepsilon| = 1$ and $\varepsilon = c\, \sigma^2(\varepsilon)$.

Lean: `ReciprocityTheory.ChartRestriction.L1.lang_semilinear`

The series $\varepsilon \ell$ has the same type as $f$:
$$\varepsilon \ell(X) - \frac{c}{l}\,\sigma^2(\varepsilon)\, \ell\bigl(X^{l^2}\bigr) = \varepsilon\Bigl(\ell(X) - \frac{1}{l}\ell\bigl(X^{l^2}\bigr)\Bigr) = \varepsilon X,$$
which is integral. By the functional equation lemma for two logarithms of the same type, $u(\varepsilon \ell(X))$ is integral.

Lean: `ReciprocityTheory.ChartRestriction.L1.fin_integral`

Finally the coefficients of this series, computed in $\breve{\mathbb{Q}}_l$, are the coefficients of the same series computed in $\mathbb{C}_l$, because the inclusion is a ring map. $\square$

**Remark 7.6.6.** The theorem on Honda type follows the method of Honda's theory of commutative formal groups, and the comparison of two logarithms of the same type is the functional equation lemma of Hazewinkel. The Lubin-Tate group with logarithm $\ell$ is the formal group of the uniformizer $l$ over the unramified quadratic extension of $\mathbb{Q}_l$.

**Remark 7.6.7 (Formalization).** The hypothesis that $d$ is squarefree is not used: it is the unused binder at [FgClose.lean](lean:ReciprocityTheory/ReductiveGroups/UnramifiedIntegrals/FgClose.lean#L26). The statement for the rest of the development is a bare alias of the theorem on formal groups at inert primes: [FgStatus.lean](lean:ReciprocityTheory/ReductiveGroups/UnramifiedIntegrals/FgStatus.lean#L5). The theorem on Honda type is proved for any complete ultrametric field of characteristic $0$ with Frobenius data: [FgHonH.lean](lean:ReciprocityTheory/ReductiveGroups/UnramifiedIntegrals/FgHonH.lean#L220). The logarithm $f$ is defined as a chosen compositional inverse of $u$, with the value $0$ when no inverse exists: [FgDefs.lean](lean:ReciprocityTheory/ReductiveGroups/UnramifiedIntegrals/FgDefs.lean#L53).
