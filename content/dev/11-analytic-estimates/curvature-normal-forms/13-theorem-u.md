---
title: Theorem U
decls:
  - Formalism.FourierDecayAlt.P.derivative_cost_bound
  - Formalism.FourierDecayAlt.P.phi_pointwise_bound
  - Formalism.FourierDecayAlt.P.compactly_supported_banach_model
  - Formalism.FourierDecayAlt.P.theorem_u
  - Formalism.FourierDecayAlt.P.corollary_u2_germ_hypothesis
status: drafted
drafted_by: writer@claude-opus-5-5
---

## Theorem U

The [germ expansion with a rate](/entry/germ-rate/) needs its input as a smooth function of a matrix variable $Z$ with values in a Banach space of functions of the lower variable $\gamma$, with bounds that decay in $Z$. The input is a partial unipotent integral of a function $F_1$ that decays with its derivatives. Theorem U says that this partial integral has such a lift into any Banach space that models the class of decaying functions. The proof estimates the cost of each derivative, integrates the estimate, and passes from weak to strong smoothness. A corollary puts the result in the form that the germ expansion uses. The results are used in the step [HypsAlt is nonempty](/step/nonempty-hyps/).

### The partial unipotent integral

Fix $k$ and three ranks $p, s, \rho$, with $s \ge 1$, and put $N = p + s + \rho$. Let $\sigma$ be a permutation of $p$ letters and let $d \in (\mathbb C^\times)^p$, so that $M(\sigma, d)$ is a monomial matrix. Let $z, z'$ be points of $\mathbb C^{2N + k + 1}$.

The parameter space $\Xi$ consists of two radical coordinates $\xi_{11}, \xi_{12}$ (with Lebesgue measure) and the head parameters $\eta = (a, b, u, v)$. For a matrix $Z$ of size $s$ with $\det Z \ne 0$ and the head matrix $H = w_\sigma\, \mathrm{low}(v)\, \mathrm{diag}(d)\, \mathrm{upper}(u)$, put
$$Z_j(\eta, Z) = \begin{pmatrix} 1 & 0 \\ a & 1 \end{pmatrix} \begin{pmatrix} H & 0 \\ 0 & Z \end{pmatrix} \begin{pmatrix} 1 & b \\ 0 & 1 \end{pmatrix}.$$
For $\gamma \in G_V(\rho)$ put
$$\gamma_\xi(Z, \gamma) = R(\xi_{11})^{-1}\, m\bigl(Z_j(\eta, Z), \gamma\bigr)\, R(\xi_{12}),$$
with the radical elements $R$ and the block map $m$. Let $\psi^*(\xi)$ be the product of the character $\psi$ of $z$ at $\xi_{11}$ and the conjugate character of $z'$ at $\xi_{12}$, together with the character of the head with the standard coefficient $\beta_U$.

**Definition 1.13.1 (Partial unipotent integral).** For a function $F_1$ on $G_V(N)$ with values in a Banach space $E$,
$$\Phi(Z, \gamma) = \int_\Xi \psi^*(\xi)\, F_1\bigl(\gamma_\xi(Z, \gamma)\bigr)\, d\xi.$$

### Decay classes

For lists $u = (X_1, \dots, X_a)$ and $v = (Y_1, \dots, Y_b)$ of Lie algebra elements let $D_{u, v} F$ be the function obtained by applying the left invariant derivatives $X_i$ and the right invariant derivatives $Y_i$. A *unit word* is a list of elements of the Lie algebra whose matrix entries have absolute value at most $1$. Let $\|g\|$ be the Frobenius norm.

**Definition 1.13.2 (Class $CC$).** Let $A \in \mathbb R$, $m \in \mathbb N$ and $c \ge 0$. A function $F$ on $G_V$ is in $CC(A, m)$ with constant $c$ if $F$ is of class $C^m$ on $G_V$ and $\|g\|^A \|D_{u, v} F(g)\| \le c$ for all unit words $u, v$ with $|u| + |v| \le m$ and all $g$. It is in $CC(A, m)$ if some constant works.

**Definition 1.13.3 (Condition (Star)).** Let $A_1, B_1 \in \mathbb R$, $Q \in \mathbb N$ and $K \subseteq (0, \infty)$. A function $F_1$ on $G_V(N)$ satisfies (Star) if $F_1$ is of class $C^Q$ on $G_V$, $|\det Z_h(g)| \in K$ whenever $F_1(g) \ne 0$ (where $Z_h(g)$ is the head block of size $p + s$), and $\|g\|^{A_1} \|D_{u, v} F_1(g)\| \le B_1$ for all unit words $u, v$ in a fixed Lie subalgebra $\mathfrak p$ attached to the head block, with $|u| + |v| \le Q$.

Put
$$a_1 = a_1(N, A_1, m, mm) = \frac{A_1 - 5N(m + 1) - 2N\, mm}{8(2N + 1)}.$$
This is the decay rate that survives the integration over $\Xi$, after $m + 1$ derivatives in $Z$ and $mm$ derivatives in $\gamma$.

### The cost of a derivative

**Theorem 1.13.4 (Derivative cost).** Let $d$ have nonzero entries, let $s \ge 1$, let $K \subseteq (0, \infty)$ be compact and let $Q \in \mathbb N$. Then there is $C$ such that for every $F_1$ that satisfies (Star), every $\xi \in \Xi$, all unit words $u, v$ in the Lie algebra of $G_V(\rho)$ and $q$ with $q + |u| + |v| \le Q$, every $Z$ with $\det Z \ne 0$ and every $\gamma \in G_V(\rho)$, the function $Z \mapsto D_{u, v}(F_1 \circ \gamma_\xi)(Z, \gamma)$ is $C^q$ at $Z$ and
$$\bigl\| D^q_Z\, D_{u, v}(F_1 \circ \gamma_\xi)(Z, \gamma) \bigr\| \le C\, B_1\, \|\gamma_\xi(Z, \gamma)\|^{-A_1 + 5Nq + 2N(|u| + |v|)}.$$

Lean: `Formalism.FourierDecayAlt.P.derivative_cost_bound`

*Proof.* A derivative in $\gamma$ is a derivative of $F_1$ at $\gamma_\xi$ in a direction $\mathrm{Ad}(R(\xi_{12})^{-1}) Y$, by the definition of $\gamma_\xi$. Write this direction in the Lie algebra of the parabolic of the head: the slice of $G_V(N)$ along the block map, the radical parameter, the right and left slice rules and the slice rule in $Z$ express it as a combination of unit words. The coefficients are polynomials in the coordinates of $\gamma_\xi$, and a bound on the coordinate sizes gives a factor at most $C\|\gamma_\xi\|^{2N}$ for each derivative in $\gamma$. In the same way a derivative in $Z$ gives a factor at most $C\|\gamma_\xi\|^{5N}$. Each derivative of $F_1$ in a unit direction is bounded by (Star). $\square$

### The pointwise bound

**Theorem 1.13.5 (Pointwise bound).** Let $d$, $s$, $K$ be as above, let $m, mm, Q \in \mathbb N$ with $m + 1 + mm \le Q$, and let $A_1$ satisfy $2N(2N + k + 1) < a_1$. Then there is $C$ such that for all $z, z'$, every Banach space $E$, every $F_1$ that satisfies (Star) with constant $B_1$:

1. for every $Z$ with $\det Z \ne 0$ and every $\gamma$, the integrand of $\Phi(Z, \gamma)$ is integrable on $\Xi$;
2. for every $Z$ with $\det Z \ne 0$, the function $\Phi(Z, \cdot)$ is in $CC(a_1, mm)$ with constant $C B_1 (1 + \|Z\|)^{-a_1}$;
3. for all unit words $u, v$ with $|u| + |v| \le mm$ and every $\gamma$, the function $Z \mapsto D_{u, v} \Phi(Z, \gamma)$ is $C^{m+1}$ on $\{\det Z \ne 0\}$, and for $q \le m + 1$,
$$\|\gamma\|^{a_1}\, \bigl\| D^q_Z\, D_{u, v} \Phi(Z, \gamma) \bigr\| \le C B_1 (1 + \|Z\|)^{-a_1}.$$

Lean: `Formalism.FourierDecayAlt.P.phi_pointwise_bound`

*Proof.* Differentiate under the integral sign. By the [derivative cost](/entry/derivative-cost-bound/), the derivative of the integrand is bounded by $C B_1 \|\gamma_\xi\|^{-A_1 + 5N(m+1) + 2N\, mm}$. A decay statement in the coordinates gives a lower bound for $\|\gamma_\xi(Z, \gamma)\|$ by powers of $\|\xi\|$, $\|Z\|$ and $\|\gamma\|$. Split the remaining power of $\|\gamma_\xi\|$ into three parts. One part gives the weight $(1 + \|Z\|)^{-a_1}$, one gives $\|\gamma\|^{-a_1}$, and the third is integrable on $\Xi$ by an integrability lemma for the weight, which is where the condition $2N(2N + k + 1) < a_1$ is used. $\square$

### Banach models of the decay class

**Definition 1.13.6 (Banach model).** Let $a \in \mathbb R$, $mm \in \mathbb N$ and $S \subseteq G_V(\rho)$. A *Banach model* of $CC(a, mm)$ on $S$ is a Banach space $V$ with a linear map $\operatorname{ev}$ from $V$ to the functions on $G_V(\rho)$ with values in $E$ such that:

1. $\operatorname{ev}(v)$ is in $CC(a, mm)$ with constant $\|v\|$;
2. if $\operatorname{ev}(v)$ is in $CC(a, mm)$ with constant $c$, then $\|v\| \le c$;
3. $\operatorname{ev}(v)$ vanishes on $G_V \setminus S$;
4. every $F$ in $CC(a, mm)$ that vanishes on $G_V \setminus S$ agrees on $G_V$ with $\operatorname{ev}(v)$ for some $v$.

So $\|v\|$ is the best constant of $\operatorname{ev}(v)$, and $V$ is the space of functions of the class that are supported in $S$.

**Proposition 1.13.7 (Banach models exist).** For every $k$, $\rho$, every Banach space $E$, every $a$, $mm$ and $S$, there is a Banach model of $CC(a, mm)$ on $S$.

Lean: `Formalism.FourierDecayAlt.P.compactly_supported_banach_model`

*Proof.* Let $\mathrm{Idx}$ be the set of pairs $(g, (u, v))$ with $g \in G_V$ and unit words with $|u| + |v| \le mm$. To $F$ assign the bounded family $T(F) = (\|g\|^a D_{u, v} F(g))$ in $\ell^\infty(\mathrm{Idx}, E)$. Let $V$ be the set of $T(F)$ for $F$ in $CC(a, mm)$ vanishing off $S$. The sup norm of $T(F)$ is the best constant of $F$, which gives 1 and 2, and $\operatorname{ev}(T(F)) = F$ gives 3 and 4. It remains to show that $V$ is closed, so that it is complete. Let $T(F_n)$ converge. The components with $u = v = \emptyset$ converge uniformly on compact sets, so $F_n$ converges to a function $F$. The derivatives $D_{u,v} F_n$ converge uniformly on compact sets too, so $F$ is of class $C^{mm}$ and its derivatives are the limits. Hence the limit is $T(F)$, and $F$ vanishes off $S$. $\square$

### Theorem U

**Theorem 1.13.8 (Theorem U).** Let $d$, $s$, $K$, $m$, $mm$, $Q$ and $A_1$ be as in the pointwise bound. Then there is $C$ such that for all $z, z'$, every Banach space $E$ and every $F_1$ that satisfies (Star) with constant $B_1$:

1. the integrand of $\Phi(Z, \gamma)$ is integrable on $\Xi$ when $\det Z \ne 0$;
2. $\Phi(Z, \gamma) = 0$ when $\det Z \ne 0$ and $|\det M(\sigma, d)\, \det Z| \notin K$;
3. for every $S$ and every Banach model $V$ of $CC(a_1, mm)$ on $S$ such that $\Phi(Z, \cdot)$ vanishes off $S$ for all $Z$ with $\det Z \ne 0$, there is a map $\Phi^\sharp : Z \mapsto V$ with $\operatorname{ev}(\Phi^\sharp(Z)) = \Phi(Z, \cdot)$ on $G_V$, such that $\Phi^\sharp$ is $C^m$ at each $Z$ with $\det Z \ne 0$ and
$$\| D^q \Phi^\sharp(Z) \| \le C B_1 (1 + \|Z\|)^{-a_1}, \qquad q \le m.$$

Lean: `Formalism.FourierDecayAlt.P.theorem_u`

*Proof.* Claim 1 is part of the [pointwise bound](/entry/phi-pointwise-bound/). For claim 2, the determinant of the head block of $\gamma_\xi(Z, \gamma)$ is $\det M(\sigma, d) \det Z$, since the unipotent factors do not change it; by (Star) the integrand vanishes if its absolute value is not in $K$. For claim 3, the pointwise bound puts $\Phi(Z, \cdot)$ in the class with the right constant, so it is $\operatorname{ev}$ of a unique $\Phi^\sharp(Z) \in V$. The evaluations $v \mapsto \|g\|^{a_1} D_{u, v}\operatorname{ev}(v)(g)$ are bounded linear functionals on $V$, and they determine the norm, by property 2 of a model. The pointwise bound says that each evaluation of $\Phi^\sharp$ is $C^{m + 1}$ with the bound $C B_1 (1 + \|Z\|)^{-a_1}$. A weak to strong principle finishes: if a family of functionals determines the norm and every functional of the family applied to $\Phi^\sharp$ is $C^{m+1}$ with derivatives up to order $m + 1$ bounded by a continuous function $b$, then $\Phi^\sharp$ is $C^m$ with derivatives up to order $m$ bounded by $b$. One order of smoothness is lost because the difference quotients of order $m$ converge uniformly only thanks to the bound on order $m + 1$. $\square$

### The form used by the germ expansion

**Corollary 1.13.9 (Corollary U2).** For all $C_1, C_2 \in \mathbb N$ there is $C_c$ with the following property. Let $U$ be germ data of sizes $p, s, \rho$ (a permutation, a diagonal, points $z, z'$, a finite family of operators, cutoffs, and the derived numbers $A_s$, $A_B$, $mm_B$ and the support $S$) that satisfy the conditions of order $C_2$, and let $A_0 \ge C_c (N + 1)^4 A_s$. Then the decay rate $a = a(C_2, A_0)$ of the data satisfies
$$(C_1 + 1)(N + 1)^3 A_s \le a, \qquad C_1 s^2 \le a, \qquad A_B \le a,$$
and there is $C$ such that for every $f$ in $CC(A_0, 3A_s)$ with constant $c$ and every Banach model $V$ of $CC(a, mm_B)$ on $S$, there is $\Phi^\sharp : Z \mapsto V$ with $\operatorname{ev}(\Phi^\sharp(Z)) = \Phi_U f(Z, \cdot)$ on $G_V$, which is $C^{C_2 s^2}$ at each $Z$ with $\det Z \ne 0$ and has $\|D^q \Phi^\sharp(Z)\| \le C c (1 + \|Z\|)^{-a}$ for $q \le C_2 s^2$.

Lean: `Formalism.FourierDecayAlt.P.corollary_u2_germ_hypothesis`

*Proof.* The operators of the data and the two cutoffs turn $f$ into a function $F_1$ that satisfies (Star) with $B_1$ a multiple of $c$, by a star bound for the cutoff operators and the projection of the head. A count of the derivative budget chooses $m = C_2 s^2$ and $mm = mm_B$ with $m + 1 + mm \le Q$, and the thresholds give the three inequalities for $a$ and the condition $2N(2N + k + 1) < a_1$. A support lemma shows that $\Phi_U f(Z, \cdot)$ vanishes off $S$. Then [Theorem U](/entry/theorem-u/) gives $\Phi^\sharp$. $\square$

**Remark 1.13.10 (Formalization).** The derivative cost is declared with its full name outside any namespace, in a file whose name refers to a truncated Corollary U1. Its proof takes seven inputs about slices and coordinate sizes; the pointwise bound takes four; Theorem U takes three (the pointwise bound, the support statement and the weak to strong principle); Corollary U2 takes six. We did not unfold the subalgebra $\mathfrak p$ of condition (Star), the germ data, their conditions of order $C_2$, or the rate $a(C_2, A_0)$; the statement above gives them by their role. The points $z, z'$ in Theorem U are arbitrary vectors; no condition on them is assumed.
