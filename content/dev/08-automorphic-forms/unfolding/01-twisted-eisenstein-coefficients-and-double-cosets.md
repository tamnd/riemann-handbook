---
title: Twisted Eisenstein coefficients and double cosets
decls:
  - PI.TwistedEisensteinNonvanishing.W.twisted_eisenstein_of_remaining
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Twisted Eisenstein coefficients and double cosets

This section proves that the local coefficient of a twisted Eisenstein series at a prime $P$ of degree one is nonzero at large depth for one element $h$ if and only if it is nonzero for every element of the double coset $R_1 h J$. Here $R_1$ is a unipotent group of the first unfolding and $J$ is a parahoric level group. The proof reduces the statement to three properties of the test function: its support, its periodicity, and a bound on the entries of bounded matrices. This reduction is the main theorem of the section. With the three properties, it gives [the nonvanishing theorem for twisted Eisenstein coefficients](/entry/twisted-eisenstein-nonvanishing/) of Volume 10, which Section 2 applies to the column data of the proof.

### Ranks, lattices and groups

**Definition 5.1.1 (Ranks).** *Ranks* are integers $o, k, m, t \geq 0$ such that $k$ and $m$ are even, $t$ is odd, and
$$\begin{aligned} 2 &\leq m, & m + 3 &\leq k, & k + m - 1 + 5 &\leq t, \\ 3m &< t, & m \leq 2o &\leq k, & m^2 &\leq k + m(t+1). \end{aligned}$$
For $j \geq 0$ put $N_j = k + j(t+1)$, $c_j = m - 1 - j$ (with $c_j = 0$ when $j \geq m - 1$) and $r = k + m - 1$. The space of step $j$ is $V_j = E^{N_j + c_j}$, with coordinates numbered from $0$.

Let $E$ be a number field with an involution, let $K$ be a field, and let $P$ be a nonzero prime of $\mathcal{O}_E$ with norm $q = |\mathcal{O}_E / P|$. An element $a \in E$ is *integral at $P$* if it lies in the [local ring](/learn/commutative-algebra/#regular-local-rings-and-discrete-valuation-rings) $\mathcal{O}_{(P)}$. We say that $P$ is *of degree one and unramified* if $q$ is a prime number and $q \notin P^2$. Then $q \in P \setminus P^2$, so $q$ is a uniformizer of $\mathcal{O}_{(P)}$, and $\mathcal{O}_E / P = \mathbb{Z}/q$.

**Definition 5.1.2 (Lattices and level group).** Let $\Lambda_j = \mathcal{O}_{(P)}^{N_j + c_j} \subset V_j$ be the standard lattice. For integers $e_0, e_1, \dots$ let $\Lambda(e)$ be the set of $x \in E^N$ with $q^{-e_l} x_l$ integral at $P$ for all $l$. For $\kappa_0 \leq n$ let $\Lambda'(\kappa_0, n, c) \subset E^{n+c}$ be $\Lambda(e)$ with $e_l = 1$ for $\kappa_0 \leq l < n$ and $e_l = 0$ otherwise. The *level group* of step $j$ is
$$J_j = \operatorname{Stab}(\Lambda_j) \cap \operatorname{Stab}(\Lambda'(k + j, N_j, c_j)) \subset \mathrm{GL}(V_j).$$

**Definition 5.1.3 (The group $R_1$).** Let $n, c \geq 0$, and let $e_0, \dots, e_{n+c-1}$ be the standard basis of $E^{n+c}$. For $i \geq 0$ let $U_i$ be the span of the $e_l$ with $l < n + i$. An automorphism $g$ of $E^{n+c}$ satisfies the *$R_1$ condition* if $g(U_i) \subseteq U_i$ for all $i$, $g(e_n) = e_n$, and $g(e_{n+i}) - e_{n+i} \in U_i$ for all $i$. The group $R_1(n, c)$ is the set of $g$ such that $g$ and $g^{-1}$ both satisfy the $R_1$ condition.

So an element of $R_1$ is block upper triangular with respect to $E^n \oplus E^c$, fixes $e_n$, and is unipotent upper triangular on the last $c$ coordinates modulo $E^n$. It is the unipotent radical of the first unfolding, together with the automorphisms of $E^n$ that it carries along.

**Definition 5.1.4 (Bounded element, double coset).** An automorphism $h$ of $V_j$ is *bounded* at step $j$ if $h^{-1} x \in \Lambda_j$ and $q^j h x \in \Lambda_j$ for all $x \in \Lambda_j$. Two automorphisms $h$, $h'$ of $V_j$ are in the *same double coset* if $h' = g h \kappa$ with $g \in R_1(N_j, c_j)$ and $\kappa \in J_j$.

### The first unfolding sum

Let $a, b \geq 0$ and let $\mathcal{S}(a, b)$ be the set of functions from $\operatorname{Hom}_E(E^a, E^b)$ to $K$.

**Definition 5.1.5 (Transform by a pair).** Let $\mu \colon E^\times \to K$ and $v \colon E^\times \to \mathbb{Z}$ be maps and let $s \in K$. For $g_0 \in \mathrm{GL}_a(E)$, $h \in \mathrm{GL}_b(E)$ and $\Phi \in \mathcal{S}(a, b)$ put
$$(\omega(g_0, h)\Phi)(x) = \mu(\det g_0)\, \mu(\det h)^{-1}\, s^{-v(\det g_0)\, b}\, s^{v(\det h)\, a}\, \Phi(h^{-1} x g_0).$$

Now fix $n', c', n, c$ with $c' = c + 1$, and index the entries $x_{l s}$ of $x \in \operatorname{Hom}(E^{n'+c'}, E^{n+c})$ by rows $l < n + c$ and columns $s < n' + c'$. The entry $(l, s)$ is *free* if $s \geq n'$ and either $s - n' = c$, or $s - n' \geq 1$ and ($l < n$ or $l - n < s - n'$). Let $F$ be the finite set of free entries.

**Definition 5.1.6 (Unfolding matrix).** For $x_0 \in \operatorname{Hom}(E^{n'}, E^n)$ and $t \in E^F$, the matrix $X(x_0, t)$ has the entry $t_{ls}$ at a free entry $(l, s)$. Off the free entries it has the entries of $x_0$ in the block $l < n$, $s < n'$, the entry $1$ at $(n + (s - n'), s)$ for $s \geq n'$, and $0$ elsewhere.

So column $n'$ of $X(x_0, t)$ is $e_n$; for $1 \leq j < c$, column $n' + j$ is $e_{n+j}$ plus free entries in the rows $l < n$ and $n \leq l < n + j$; the last column is free. The *character argument* of $x$ is the sum of the entries just above the diagonal of the last block,
$$\operatorname{ch}(x) = \sum_{i < c} x_{n+i,\; n'+i+1}.$$

**Definition 5.1.7 (First unfolding sum).** Let $\psi \colon E \to K$, let $\mathcal{V} \subset E$ be a finite set, let $w \in K$ and $\Phi \in \mathcal{S}(n'+c', n+c)$. The *first unfolding sum* is the function on $\operatorname{Hom}(E^{n'}, E^n)$
$$E_1(\psi, \mathcal{V}, w, \Phi)(x_0) = w^{|F|} \sum_{t \in \mathcal{V}^F} \Phi(X(x_0, t))\, \psi\big(-\operatorname{ch}(X(x_0, t))\big).$$

For integers $A, B \geq 0$ put $\mathcal{V}_{A,B} = \{ i / q^A : 0 \leq i < q^{A+B} \}$. When $P$ is of degree one and unramified, $\mathcal{V}_{A,B}$ is a set of representatives of $q^{-A}\mathcal{O}_{(P)} / q^B \mathcal{O}_{(P)}$. With the weight $w = q^{-B}$, the sum is then a Riemann sum for the integral over $(q^{-A}\mathcal{O}_{(P)})^F$ with the Haar measure that gives $\mathcal{O}_{(P)}$ volume one. This is the local integral of the first unfolding of the twisted Eisenstein series.

### The test function and the coefficient

**Definition 5.1.8 (Valuation and local character).** For $a \in E$ let $v_P(a)$ be an integer $z$ such that the reduction of $a / q^z$ modulo $P$ is a unit, chosen once and for all. For a character $\chi$ of $(\mathcal{O}_E/P)^\times$ with values in $K^\times$, put $\chi^\circ(a) = \chi(\bar a)$ if the reduction $\bar a$ of $a$ is a unit, and $\chi^\circ(a) = 0$ otherwise. For $c_q \in K$ put
$$\mu_{c_q, \chi}(a) = c_q^{\,v_P(a)}\, \chi^\circ\big(a / q^{v_P(a)}\big).$$

If $P$ is of degree one and unramified, $v_P$ is the $P$-adic valuation on $E^\times$ and $\mu_{c_q,\chi}$ is the tamely ramified character of $E^\times$ with $\mu(q) = c_q$ and restriction $\chi$ to the units, as in the theory of [Hecke characters](/learn/class-field-theory/#hecke-characters).

**Definition 5.1.9 (Test function).** Let $\kappa_0, r, c', n', c, n \geq 0$. For $s < n + c$ let $\sigma(s) = s$ if $s < \kappa_0$, $\sigma(s) = n + (s - \kappa_0)$ if $\kappa_0 \leq s < \kappa_0 + c$, and $\sigma(s) = s - c$ otherwise; define $\sigma'$ in the same way with $c', n'$. For $x \in \operatorname{Hom}(E^{n'+c'}, E^{n+c})$ let $y_{pp'} = x_{\sigma(p)\sigma'(p')}$ be the matrix with the last coordinates moved to the positions after $\kappa_0$. Then $\Phi_\xi(x) = \xi^\circ\big(\det (y_{pp'})_{p, p' < r}\big)$ if all $y_{pp'}$ are integral at $P$ and $y_{pp'}/q$ is integral at $P$ for $p \geq r$ and $p' < r$. Otherwise $\Phi_\xi(x) = 0$.

So $\Phi_\xi$ is $\xi$ of the determinant of the top left block on an Iwahori type set of integral matrices. In the coefficients below, $\kappa_0 = k$ and $r = k + m - 1$.

**Definition 5.1.10 (Twisted Eisenstein coefficient).** Fix ranks, a prime $P$, a function $\psi \colon E \to K$, elements $s, c_q \in K$, and a character $\xi$ of $(\mathcal{O}_E/P)^\times$. For $i \geq 0$, $A, B \geq 0$, $g_0 \in \mathrm{GL}(V_i)$ and $h \in \mathrm{GL}(V_{i+1})$, the *twisted Eisenstein coefficient* is
$$\begin{aligned} \mathcal{E}_{A,B}(g_0, h) = E_1\Big(\psi,\; \mathcal{V}_{A,B},\; q^{-B},\; \omega(g_0, h)\, \Phi_\xi\Big), \end{aligned}$$
where $\omega$ is formed with $\mu = \mu_{c_q, \xi^{-1}}$, $v = v_P$ and $s$, and $\Phi_\xi$ has the parameters $(k, r, c_i, N_i, c_{i+1}, N_{i+1})$. It is a function on $\operatorname{Hom}(E^{N_i}, E^{N_{i+1}})$. It is *nonzero at large depth* if there are $A_0$, $B_0$ such that $\mathcal{E}_{A,B}(g_0, h)$ is not the zero function for all $A \geq A_0$ and $B \geq B_0$.

**Definition 5.1.11 (Admissible additive character).** Let $D \geq 0$. A function $\psi \colon E \to K$ is *admissible of depth $D$* at $P$ if $\psi(x + y) = \psi(x)\psi(y)$ whenever $q^D x$ and $q^D y$ are integral at $P$, $\psi(x) = 1$ for $x$ integral at $P$, and $\psi(x) = 1$ whenever $q^D x$ is not integral at $P$.

So $\psi$ is an [additive character](/learn/class-field-theory/#additive-characters) of $q^{-D}\mathcal{O}_{(P)} / \mathcal{O}_{(P)}$, extended by $1$.

### The reduction to the test function

**Theorem 5.1.12 (Double coset invariance from the test function).** Assume the following three statements, for all number fields $E$ with an involution, all fields $K$, all nonzero primes $P$ of $\mathcal{O}_E$ and all characters $\xi$ of $(\mathcal{O}_E/P)^\times$.

1. (Support.) For every integer $q \geq 0$ and all $\kappa_0, r, c', n', c, n$ with $\kappa_0 \leq n$ and $\kappa_0 \leq n'$: if the test function, formed with $q$ in place of the norm, is nonzero at $y$, then every entry of $y$ is integral at $P$.
2. (Periodicity.) If $P$ is of degree one and unramified, then $\Phi_\xi(y + \varepsilon) = \Phi_\xi(y)$ for all parameters and all $y$, $\varepsilon$ such that every entry of $\varepsilon$ lies in $q\mathcal{O}_{(P)}$.
3. (Bounded entries.) For all ranks and $j \geq 0$, if $h$ is bounded at step $j$, then all entries of $q^j h$ and of $h^{-1}$ are integral at $P$.

Then the following holds. Let $E$, $K$, ranks and $P$ be given, with $P$ of degree one and unramified. Let $\psi$ be admissible of depth $2m$, let $s \neq 0$ and $c_q \neq 0$ in $K$, and let $\xi$ be a character of $(\mathcal{O}_E/P)^\times$. Let $i + 3 \leq m$, let $g_0 \in \mathrm{GL}(V_i)$ be bounded at step $i$, and let $h, h' \in \mathrm{GL}(V_{i+1})$ be bounded at step $i+1$ and in the same double coset. If $\mathcal{E}(g_0, h)$ is nonzero at large depth, then $\mathcal{E}(g_0, h')$ is nonzero at large depth.

Lean: `PI.TwistedEisensteinNonvanishing.W.twisted_eisenstein_of_remaining`.

*Proof.* Write $h' = g h \kappa$ with $g \in R_1$ and $\kappa \in J_{i+1}$, and put $\rho = g$. Let $n' = N_i$, $c' = c_i$, $n = N_{i+1}$, $c = c_{i+1}$, so $c' = c + 1$.

First let $q = 0$ in $K$. Then $q^{-B} = 0$ in $K$, read as the inverse of $0$. The set $F$ of free entries is not empty, since the last column is free. So the weight $q^{-B|F|}$ is $0$ and $\mathcal{E}_{A,B}(g_0, h) = 0$ for all $A$, $B$. The hypothesis fails, and there is nothing to prove.

Now let $q \neq 0$ in $K$. We use five facts on $\mathcal{O}_{(P)}$, which hold because $q$ is a prime number and a uniformizer: an integer is integral at $P$ with $q \mid$ it in $\mathcal{O}_{(P)}$ if and only if $q$ divides it in $\mathbb{Z}$; every element integral at $P$ is congruent to an integer modulo $q^N$; every $a \neq 0$ is $q^z u$ with $u$ a unit at $P$; the exponent $z$ is unique; and every unit is congruent to an integer modulo $P$. They give that $v_P$ is the valuation, that $\mu_{c_q, \xi^{-1}}(a) \neq 0$ for $a \neq 0$, and that $\mathcal{V}_{A,B}$ represents $q^{-A}\mathcal{O}_{(P)}/q^B\mathcal{O}_{(P)}$.

Step 1 (the level group). There is $C \neq 0$ in $K$ with
$$\omega(g_0, \rho h \kappa)\Phi_\xi(x) = C\, \omega(g_0, h)\Phi_\xi(\rho^{-1} x)$$
for all $x$. This is a transformation law of $\Phi_\xi$ under $\kappa \in J_{i+1}$: the determinant of $\kappa$ is a unit at $P$, and right translation by $\kappa^{-1}$ changes the top left block of size $r = k + (i+1) + c$ by a matrix whose determinant is a unit, so $\Phi_\xi$ changes by the nonzero factor $\xi^\circ$ of that determinant. The factor $C$ collects this value and the values of $\mu$ and $s$ at $\det \rho$ and $\det \kappa$, which are nonzero.

Step 2 (the unfolding matrix). For $\rho \in R_1(n, c)$ and every $x_0$, $t$,
$$\rho^{-1} X(x_0, t) = X\big(\rho_X^{-1} x_0,\; \tau(t)\big),$$
where $\rho_X^{-1}$ is the restriction of $\rho^{-1}$ to $E^n$ and $\tau$ is an affine map of $E^F$ whose linear part is invertible. Indeed $\rho^{-1}$ preserves the flag $U_i$, fixes $e_n$ and moves $e_{n+i}$ only by vectors of $U_i$, so it preserves the shape of the unfolding matrix and acts on the free entries by an affine bijection. The map $x_0 \mapsto \rho_X^{-1} x_0$ is surjective, and $\operatorname{ch}(X(\rho_X^{-1}x_0, \tau(t))) - \operatorname{ch}(X(x_0,t))$ does not depend on $t$.

Step 3 (good integrands). By the support property and the bounded entries of $h$ and $g_0$, the function $t \mapsto \omega(g_0, h)\Phi_\xi(X(x_0, t))\,\psi(-\operatorname{ch}(X(x_0, t)))$ vanishes unless $t \in (q^{-a}\mathcal{O}_{(P)})^F$, for some $a$ that depends only on $i$. By the periodicity property, the bounded entries, and the admissibility of $\psi$ at depth $2m$, it is invariant under translation by $(q^{b}\mathcal{O}_{(P)})^F$ for some $b$. Here $i + 3 \leq m$ makes the depth $2m$ of $\psi$ large enough for the character argument of bounded matrices.

Step 4 (stability and change of variables). For a function $H$ on $E^F$ with support in $(q^{-a}\mathcal{O}_{(P)})^F$ and invariant under $(q^b\mathcal{O}_{(P)})^F$, the sum $q^{-B|F|}\sum_{t \in \mathcal{V}_{A,B}^F} H(t)$ does not depend on $(A, B)$ for $A \geq a$ and $B \geq b$, since it is then the integral of $H$. An affine change of variables $t \mapsto \tau(t)$ with invertible linear part multiplies this stable value by a nonzero constant, the absolute value of the determinant of the linear part. Since $\psi$ is a character on the relevant domain, its values are nonzero, and the constant shift of the character argument multiplies the sum by a nonzero value of $\psi$.

Combining the four steps, for $A$ and $B$ large there is $c \neq 0$ with
$$\mathcal{E}_{A,B}(g_0, h')(x_0) = c\, \mathcal{E}_{A,B}(g_0, h)(\rho_X^{-1} x_0)$$
for all $x_0$. If $\mathcal{E}_{A,B}(g_0, h)$ is nonzero at $y_0$, choose $x_0$ with $\rho_X^{-1} x_0 = y_0$; then $\mathcal{E}_{A,B}(g_0, h')(x_0) \neq 0$. $\square$

**Remark 5.1.13 (Formalization).** The three statements of the theorem are hypotheses; at the top level they are supplied by three proved results on the test function and on bounded matrices. The support statement asks for nothing about $q$, and it holds for every $q$ because the reindexing is a bijection. The valuation $v_P$ is chosen with Hilbert's choice operator, so $v_P(0)$ is an arbitrary integer; only $v_P$ on $E^\times$ matters. The case $q = 0$ in $K$ is vacuous because the inverse of $0$ is $0$. We did not unfold the proofs of the transformation law of Step 1, of the stability and change of variables lemmas of Step 4, or of the affine bijection of Step 2; they are proved results that the proof cites. See [TwistedEisensteinOfRemaining.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/TwistedEisensteinCoset/TwistedEisensteinOfRemaining.lean#L12).
