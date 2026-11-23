---
title: Coefficient identities and host fields
decls:
  - Formalism.L2.FormalSeriesBounds.coeffIdentity_selfConj_of_two
  - Formalism.L2.FormalSeriesBounds.coeffIdentity_selfConj_holds
  - Formalism.L2.FormalSeriesBounds.independence_bound_self_conjugate
  - Formalism.HC.D7.hostDer
  - Formalism.HC.D7.hostAx
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Coefficient identities and host fields

This section has two parts. The first part proves that in a self-conjugate raw chart, a family of good vectors that is independent modulo the maximal ideal has at most $j'$ members. The proof uses a coefficient identity that comes from two congruences for power series. The bound feeds [Theorem 6.6.3 of Volume 13](/entry/label-set-geo-of-even-of-rank-ok-of-not-dvd-discr/). The second part builds the CM host field $E = \mathbb{Q}(\sqrt{-q}, \sqrt{-d}, \zeta + \zeta^{-1})$ and proves its derived properties. This feeds the host field example in [Theorem](/entry/host-ax0/).

### Valued fields and raw charts

**Definition 8.7.1 (Valued field).** A valued field is a field $C$ with an additive valuation $v : C \to \mathbb{R} \cup \{\infty\}$ and a prime $l$ with $v(l) = 1$. We write $x \equiv 0$ when $v(x) > 0$, and we say that $x$ is integral when $v(x) \ge 0$. A power series over $C$ is integral when all its coefficients are integral. A curve is a family $\gamma = (\gamma_i)_{i \in \kappa}$ of power series in one variable with constant term $0$ and integral coefficients.

**Definition 8.7.2 (Raw chart).** Let $C$ be a field, $d \ge 1$ an integer, $I_0, I_1$ finite sets and $\kappa$ a finite set. A raw chart $X$ consists of:

- power series $\mathrm{lg}_i$ and $\mathrm{ex}_i$ ($i \in \kappa$) in the variables $\kappa$, the logarithm and the exponential of the chart;
- a power series $h(x, z)$ in two blocks $x = (x_i)$ and $z = (z_i)$ of variables, indexed by $\kappa$;
- a vector $u_g(c) \in C^\kappa$ and a type $\mathrm{ty}_g(c) \in \mathbb{Z}/d$ for each $g \in \{0, 1\}$ and $c \in I_g$;
- integers $k$, $n$, $j$, $j'$ and a predicate $\mathrm{big}(g, a)$ on $\{0,1\} \times \mathbb{Z}/d$.

For $v \in C^\kappa$ the gauge series of $v$ is the series in the variables $x$ given by
$$\mathrm{sg}(v)(x) = -\sum_{i \in \kappa} v_i \, [z_i]\, h(x, z),$$
where $[z_i]\,h$ is the part of $h$ that is linear in $z_i$ and has no other $z$ variable.

**Definition 8.7.3 (Rank condition and alternation).** The rank condition on $X$ says: $\mathrm{big}(1-g, a)$ holds if and only if $\mathrm{big}(g, a)$ fails, and the number of elements of $I_g$ of type $a$ is $n + j$ if $\mathrm{big}(g, a)$ holds and $j'$ if it fails. The chart is alternating when $d$ is even and, for all $a \in \mathbb{Z}/d$, $\mathrm{big}(0, a)$ holds if and only if the residue of $a$ in $\{0, \dots, d-1\}$ is even.

**Definition 8.7.4 (Coefficient identity).** Let $X$ be a raw chart over a valued field, and let $H$ be a pair of Cartier hypotheses for $X$, one for each $g$. Each $H_g$ gives a goodness relation on pairs $(w, x)$, with $w \in C^{I_g}$ and $x$ a sequence of vectors on $I_g \sqcup I_{1-g}$, and two forms $V_2(x, c)$ and $c_0'(x, q)$. The coefficient identity for $(X, H)$ is the statement: if $X$ is alternating and $\mathrm{big}(g, a)$ holds, then there is a matrix $M$ indexed by $I_{1-g} \times I_{1-g}$ such that for each good pair $(w, x)$ of type $a$ with $V_2(x, c) \equiv 0$ for all $c$, there is a vector $c_1$, supported on the $q$ with $\mathrm{ty}_{1-g}(q) = a + 2$, with
$$c_0'(x, q)^l \equiv \sum_{q'} c_1(q') \, M(q', q) \quad \text{for all } q.$$

**Definition 8.7.5 (Independence bound).** For $(X, H)$ as above, the rank maximal condition says: if $X$ is alternating, $\mathrm{big}(g, a)$ holds, $(w, x)$ is good of type $a$ and $c_0'(x, q) \equiv 0$ for all $q$, then $w(c) \equiv 0$ for all $c$. The independence bound condition says: if $X$ is alternating, $\mathrm{big}(g, a)$ holds, and $(w_\nu, x_\nu)_{\nu < N}$ are good pairs of type $a$ with $V_2(x_\nu, c) \equiv 0$ for all $\nu$ and $c$, and the vectors $w_\nu$ are independent modulo the maximal ideal, then $N \le j'$. Independence means: if integral $c_\nu$ satisfy $\sum_\nu c_\nu w_\nu \equiv 0$ in each coordinate, then all $c_\nu \equiv 0$.

**Definition 8.7.6 (Self-conjugate charts).** A statement holds for all self-conjugate charts when it holds for the raw chart of every field chart $Y$ over a valued field of characteristic $0$ and every self-conjugate datum on $Y$. In such a chart $I_0 = I_1$.

The four properties of raw charts below are about the two-variable series
$$H_X(x, z)(Y, Z) = h\big(x(Y), z(Z)\big),$$
where $x$ and $z$ are families of power series in one variable, $x$ is put in the variable $Y$ and $z$ in the variable $Z$. For $c \in C$ let $c \cdot \gamma$ be the curve $\gamma_i(cT)$, and let $\gamma^{[n]}$ be the curve $\gamma_i(T^n)$. A chart is basic when $\mathrm{lg}_i$ has constant term $0$ and linear part $x_i$, $\mathrm{ex}$ inverts $\mathrm{lg}$, every monomial of $h$ uses both blocks of variables, the $u_g(c)$ are integral, and $u_g(c)$ and $u_{1-g}(q)$ pair integrally through the gauge series when their types differ. The norm relation for $(l, n, \zeta, \gamma, \delta)$ says $\mathrm{lg}_i(\delta)(T^n) = \sum_{k < l} \mathrm{lg}_i(\gamma)(\zeta^k T)$ for each $i$.

**Definition 8.7.7 (Gauge axioms).** The four gauge axioms are these statements, for every raw chart $X$.

1. Leading term. Suppose $h$ has no monomial without a $z$ variable, $x$ has constant term $0$, $m \ge 1$, and each series $c_i$ vanishes in degrees below $m$. Then the coefficients of $Y^n Z^{j}$ in $H_X(x, c)$ vanish for $j < m$, and the coefficient of $Y^n Z^m$ is minus the coefficient of $T^n$ in $\mathrm{sg}(c^{(m)})(x(T))$, where $c^{(m)}_i$ is the coefficient of $T^m$ in $c_i$.
2. Rescaling. If $x$ and $z$ have constant term $0$, then $H_X(c \cdot x, z)$ is $H_X(x, z)$ with $Y$ replaced by $cY$, and $H_X(x, c \cdot z)$ is $H_X(x, z)$ with $Z$ replaced by $cZ$.
3. Integral unit families. Let $X$ be basic and integral in both variables, $\zeta^l = 1$, $n > 0$, and let $\gamma, \delta, c$ be curves with the norm relation for $(l, n, \zeta, \gamma, \delta)$. Then the exponentials of the series
$$\sum_{k < l} H_X(\zeta^k \cdot \gamma, c) - H_X(\delta^{[n]}, c) \quad \text{and} \quad \sum_{k < l} H_X(c, \zeta^k \cdot \gamma) - H_X(c, \delta^{[n]})$$
are integral.
4. Generic point congruence. Let $X$ be basic and integral in both variables, $\zeta^l = 1$, $n > 0$, and let $z, \varepsilon, \delta$ be curves with the norm relation for $(l, n, \zeta, z, \varepsilon)$ and with $\delta_i'(0) \equiv 0$ for all $i$. Then for $N > 0$ and $i \le N$, every coefficient of $Y^i Z^j$ in
$$\exp\Big(\sum_{k < l} H_X(\delta^{[N]}, \zeta^k \cdot z) - H_X(\delta^{[N]}, \varepsilon^{[n]})\Big) - 1$$
is $\equiv 0$.

### The independence bound

**Theorem 8.7.8 (Coefficient identity from two axioms).** Assume the leading term axiom and the generic point congruence. Then the coefficient identity holds for all self-conjugate charts that satisfy the rank condition, for every pair of Cartier hypotheses.

Lean: `Formalism.L2.FormalSeriesBounds.coeffIdentity_selfConj_of_two`

*Proof (outline).* A general theorem derives the coefficient identity from all four gauge axioms, with proved results on good curves, restriction steps, the Frobenius congruence, roots of unity and the low order terms of the exponential. The rescaling axiom and the integral unit families axiom are proved, so only the leading term axiom and the generic point congruence stay as hypotheses. $\square$

**Theorem 8.7.9 (Coefficient identity).** The coefficient identity holds for all self-conjugate charts that satisfy the rank condition, for every pair of Cartier hypotheses.

Lean: `Formalism.L2.FormalSeriesBounds.coeffIdentity_selfConj_holds`

*Proof.* This is Theorem (Coefficient identity from two axioms) applied to the proofs of the leading term axiom and the generic point congruence. $\square$

**Theorem 8.7.10 (Independence bound for self-conjugate charts).** Let $X$ be a self-conjugate chart with the rank condition, and let $H$ be a pair of Cartier hypotheses for $X$. If the rank maximal condition holds for $(X, H)$, then so does the independence bound condition.

Lean: `Formalism.L2.FormalSeriesBounds.independence_bound_self_conjugate`

*Proof (outline).* The field of a self-conjugate chart is algebraically closed. Fix $g$ and $a$ with $\mathrm{big}(g, a)$. Since $X$ is alternating, the condition $\mathrm{big}(g, a)$ implies $\mathrm{big}(g, a+2)$. Then $\mathrm{big}(1-g, a+2)$ fails, so by the rank condition exactly $j'$ elements $q$ of $I_{1-g}$ have type $a+2$. Since $c_1$ is supported on these $q$, the identity says that for each good pair the vector $c_0'(x, \cdot)^l$ is congruent to a combination of $j'$ fixed rows of $M$. Over an algebraically closed field, a general lemma shows that under the rank maximal condition such a span property bounds an independent family by the number of spanning rows. So $N \le j'$. The coefficient identity is Theorem (Coefficient identity). $\square$

### The host field

**Definition 8.7.11 (Host primes and layers).** A pair $(q, d)$ of integers satisfies the host hypothesis when $q$ and $d$ are prime, $q \equiv 3 \pmod 8$, $d \equiv 7 \pmod{16}$, and the Jacobi symbol $\left(\frac{-d}{q}\right)$ is $1$. A layer of level $m$ for $(q, d)$ in a number field $L$ is a triple $(\zeta, a, b)$ in $L$ where $\zeta$ is a primitive $2^m$-th root of unity, $a^2 = -q$, $b^2 = -d$, and $L = \mathbb{Q}(\zeta, a, b)$. The host field of the layer is the compositum
$$E = \mathbb{Q}(a, b) \cdot \mathbb{Q}(\zeta + \zeta^{-1}) \subseteq L.$$

**Definition 8.7.12 (Frame).** A frame $\varphi$ is a finite abelian group $A$ of order $\mathrm{ord}$ with a surjective homomorphism $h : A \to H_e$, where $H_e = (\mathbb{Z}/2^{e+2})^\times / \{\pm 1\}$, and a generator condition on a chosen element of $A$. Its group is $G = \{\pm 1\}^2 \times A$, where complex conjugation is $c = ((-1, -1), 1)$, the inertia element at $d$ is $\iota_d = ((1, -1), 1)$, and $\Psi$ is the kernel of the second sign. When $h$ is injective, $\mathrm{ord} = 2^e$.

**Definition 8.7.13 (Host data).** Raw host data on a frame $\varphi$ consist of primes $q, d$ with the host hypothesis, $e \ge 2$, an integer $Q > 0$ with $2^{e+2} \mid Q$, $\gcd(Q, qd) = 1$ and $\left(\frac{-d}{l}\right) = 1$ for each odd prime $l \mid Q$, a Galois number field $E$ with $\mathrm{Gal}(E/\mathbb{Q}) \cong G$, an element $\sqrt{-d} \in E$ on which the Galois group acts by the second sign, an embedding of $E$ in the cyclotomic field of conductor $N = Qqd$, and an Artin map $(\mathbb{Z}/N)^\times \to G$ that is compatible with the cyclotomic action and sends $-1$ to $c$, with three more conditions on its values. Host axioms are raw host data with the derived properties of the next theorem.

Let $F$ be the maximal real subfield of $E$ and $K = \mathbb{Q}(\sqrt{-d})$. The root discriminant of $E$ is $\mathrm{rd} = |\mathrm{disc}\, E|^{1/[E:\mathbb{Q}]}$.

**Theorem 8.7.14 (Derived properties of the host field).** Let $\varphi$ be a frame with $h$ injective and $e \ge 2$. Let $(q, d)$ satisfy the host hypothesis, and let $(\zeta, a, b)$ be a layer of level $e + 2$ for $(q, d)$ in a number field $L$. Put $Q = 2^{e+2}$ and let $E$ be the host field of the layer. Then the raw host data built from $E$ have these properties.

1. The Artin map is surjective. $E$ is a CM field, and for each complex embedding $\psi$, an automorphism $\sigma$ satisfies $\psi \circ \sigma = \bar{\psi}$ if and only if $\sigma$ maps to $c$.
2. $[E : \mathbb{Q}] = 4\,\mathrm{ord}$ and $[F : \mathbb{Q}] = 2\,\mathrm{ord}$, and $F$ is the fixed field of $c$.
3. The embeddings $\psi$ with $\psi(\sqrt{-d}) = i\sqrt{d}$ form a CM type with $2\,\mathrm{ord}$ elements that is stable under $\Psi$ and under no other automorphism.
4. There is an element $s \ne 0$ on which the Galois group acts by the first sign. The second sign of the Artin map is the Jacobi symbol $\left(\frac{\cdot}{d}\right)$, and the first sign is $-1$ on the units that are $d$ mod $Qq$.
5. At a prime $p \nmid N$, the Frobenius elements are the Artin images of $p$, with second sign $\left(\frac{-d}{p}\right)$, and inertia is trivial. At every prime $l$, Frobenius, inertia and decomposition groups are given by the Artin map. The inertia group at $d$ is $\{1, \iota_d\}$.
6. At primes dividing $Qq$ the decomposition group lies in $\Psi$, and at primes dividing $N$ it does not contain $c$.
7. $E/F$ is unramified at all finite primes. A prime $p$ splits in $K$ if and only if $p = 2$ or $\left(\frac{-d}{p}\right) = 1$, and this happens if and only if $\sigma\tau \in \Psi \Leftrightarrow \sigma \in \Psi$ for all $\sigma$ and all $\tau$ in the decomposition group of a prime over $p$.
8. Each prime of $F$ splits or is inert in $E$, and it splits if it lies over a prime dividing $N$.
9. The relative different of $E/K$ is supported on primes over $Qq$, and it equals $\mathfrak{b} \cdot c(\mathfrak{b})$ for an ideal $\mathfrak{b}$ that is coprime to $c(\mathfrak{b})$ and stable under $\Psi$. For every $\mathfrak{b}$ with this product formula, the dual of $\mathfrak{b}^{-1}$ for the trace form $\mathrm{Tr}_{E/K}(x \bar{y})$ is $\mathfrak{b}^{-1}$.
10. $\mathrm{disc}\, E = (\mathrm{disc}\, F)^2$, the primes that divide $\mathrm{disc}\, E$ divide $N$, and $2$ and $d$ divide $\mathrm{disc}\, E$.
11. The root discriminant satisfies
$$\begin{aligned} 2^{e + 1 - 2^{-e}} \sqrt{d} &\le \mathrm{rd} \le \tfrac{Q}{2} \sqrt{qd}, \\ 4\,\mathrm{ord} &\le \mathrm{rd}^2. \end{aligned}$$
12. Every root of unity in $E$ has norm $1$ to $K$.

Lean: `Formalism.HC.D7.hostDer`

*Proof (outline).* The Galois group of $E$ is identified with $\{\pm 1\}^2 \times H_e$ through the signs on $\sqrt{-q}$ and $\sqrt{-d}$ and the action on $\zeta + \zeta^{-1}$, and then with $G$ through $h$. The Artin map comes from the cyclotomic field of conductor $2^{e+2} q d$. Each property is proved from this description; the discriminant statements also use the discriminant of the maximal real subfield of a $2$-power cyclotomic field. $\square$

**Corollary 8.7.15 (Host axioms).** Under the hypotheses of the theorem, the raw host data built from $E$ and their derived properties form host axioms on $\varphi$.

Lean: `Formalism.HC.D7.hostAx`

*Proof.* This is Theorem (Derived properties of the host field) attached to the raw host data. $\square$

**Example 8.7.16.** Take $q = 11$, $d = 7$ and $e = 2$. Then $11 \equiv 3 \pmod 8$, $7 \equiv 7 \pmod{16}$, and $-7 \equiv 4 = 2^2 \pmod{11}$, so the host hypothesis holds. A layer of level $4$ exists, and the corollary gives $E = \mathbb{Q}(\sqrt{-11}, \sqrt{-7}, \zeta_{16} + \zeta_{16}^{-1})$, of degree $16$ over $\mathbb{Q}$. This is the host field of [Theorem](/entry/host-ax0/).

For background see [splitting of primes](/learn/number-fields/#the-splitting-of-primes) and [global class field theory](/learn/class-field-theory/#global-class-field-theory).

**Remark 8.7.17 (Formalization).** The gauge axioms are in [PowerSeriesFrobeniusCongruence.lean](lean:Formalism/SharpRestriction/GrowthBounds/PowerSeriesFrobeniusCongruence.lean#L50). The two open axioms are proved in [CoeffGaugeSquareLowDegree.lean](lean:Formalism/SharpRestriction/GrowthBounds/CoeffGaugeSquareLowDegree.lean#L238) and [GenIntSPsubst.lean](lean:Formalism/SharpRestriction/GrowthBounds/GenIntSPsubst.lean#L194) and combined in [CoeffIdentitySelfConjHolds.lean](lean:Formalism/SharpRestriction/GrowthBounds/CoeffIdentitySelfConjHolds.lean#L8). The two-variable series has four separate definitions, and the rescalings, integrality in both variables, the norm relation, integral series and the exponential have two or three each. We do not unfold the Cartier hypotheses, the goodness relation, the forms $V_2$ and $c_0'$, field charts, self-conjugate data, or the proofs of the gauge axioms. The host axioms are a definition, not a theorem ([NonemptyFieldAxiomsCyclicPow.lean](lean:Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/NonemptyFieldAxiomsCyclicPow.lean#L651)), and the derived properties are a structure in [ConjEMemHostFIff.lean](lean:Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/ConjEMemHostFIff.lean#L87). The same file states, as a proposition and without proof, that every raw host datum has the derived properties.
