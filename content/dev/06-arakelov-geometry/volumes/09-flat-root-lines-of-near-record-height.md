---
title: Flat root lines of near record height
decls:
  - RootFieldNumerics.RF.core
  - RootFieldNumerics.RF.rootFlatOnHodge_of
  - RootFieldNumerics.rootFlatOnHodge
  - RootFieldNumerics.global_model_tower_final_condition
  - GlobalTheory.T.good_tower_real_extra
  - GlobalTheory.CompanionTheory.Relay.good_tower_real_extra
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Flat root lines of near record height

Proposition F of [the tower conditions](/entry/full-intersection-tower-i8-identity/) bounds a combination of the shift coefficients of a tower by $C' N \Lambda_B$, with $\Lambda_B = \log(B\,\mathrm{rd}) + |L|$. Its input is a hermitian line on the base model whose metric is the product of the root lines of one CM type and which has a flat section of controlled height. This section builds such a line on every root model over a global integral model: for each CM type $\tau$ there is a flat root line whose height is near a record value fixed by the flat degree of [the previous section](/entry/flat-degree-st-of-res-k-gaga/), up to explicit corrections at the bad primes. The result is used in [the volume theorem](/entry/volume-theorem-x-of-inputs/), where it gives Proposition F with the constant $4$.

We keep the setting of [the section on height bounds](/entry/i5-and-i6-of-is-global-of-good-origin/). Let $M$ be a root model of type $(\Psi, N)$, with coordinates $y$ in a field $\Omega$, coordinate degrees $\deg x_{\tau, i}$ and twisted lines $x_t(\tau, i)$ for $t > 0$.

**Definition 9.9.1 (Flat hermitian structure).** Let $F$ be a number field with a map $\varphi \colon F \to \Omega$, and let $\overline{A}$ be a hermitian line on the coordinates of $M$. A flat structure on $\overline{A}$ over $\varphi$ consists of an integer $m \ge 1$, multihomogeneous polynomials $f$ and $g$ outside the coordinate ideal with $\deg f - \deg g = m \deg A$ that satisfy the unit condition of the development, and constants $\kappa_\sigma > 0$ for the embeddings $\sigma \colon F \to \mathbb{C}$, invariant under complex conjugation, such that

$$
|f(z)| = \big(\kappa_\sigma\, \|\cdot\|_A(z)\big)^m\, |g(z)|
$$

at every complex point $z$ over $\sigma$. Its height is

$$
h = -\frac{1}{[F : \mathbb{Q}]}\sum_\sigma \log \kappa_\sigma.
$$

So $f/g$ is a section of $A^{\otimes m}$ of constant norm $\kappa_\sigma^{-m}$ at each archimedean place, and the height is the arithmetic degree of $\overline{A}$ computed with it, if the unit condition makes its divisor zero at the finite places; this last point is our reading.

**Definition 9.9.2 (Flat root line).** A flat root line for $(M, \tau)$ consists of a number field $F$ with a map $\varphi \colon F \to \Omega$ that sends $\mathcal{O}_F$ into the integral charts of $M$, a smooth hermitian line $\overline{A}$ with $\deg A = \sum_i \deg x_{\tau, i}$, a flat structure on $\overline{A}$ over $\varphi$, and smooth functions $v_t$, invariant under scaling of each block of coordinates, with

$$
\prod_i \|\cdot\|_{x_t(\tau, i)} = \|\cdot\|_A\, e^{-v_t} \quad (t > 0)
$$

on the points of $M$, such that the integral of $v_t$ against every top monomial in the twisted lines of $M$ tends to $0$ as $t \to 0^+$. Its height is the height of the flat structure.

The line $\overline{A}$ is a smooth model of the product of the root lines of type $\tau$, and the functions $v_t$ measure how far the twisted metrics are from $\overline{A}$. The condition on the integrals says that this distance does not change the top intersection numbers in the limit.

**Definition 9.9.3 (Near record).** Let $N \ge 1$, let $\mathcal{B}$ be a finite set of primes and let $r > 0$, $L \in \mathbb{R}$. A real number $h$ is near the record for $(N, \mathcal{B}, r, L)$ if

$$
h = h_{\mathrm{rec}} + \sum_{\ell \in \mathcal{B}} d_\ell, \qquad |h_{\mathrm{rec}}| \le N\Big(\frac{3}{2}\log r + \frac{|L|}{2}\Big),
$$

and there are $v_\ell \ge 0$ with

$$
|d_\ell| \le \Big(\frac{N}{\ell - 1} + N v_\ell\Big)\log \ell, \qquad \sum_{\ell \in \mathcal{B}} v_\ell \log \ell \le \log r.
$$

A number near the record satisfies

$$
|h| \le N\Big(\frac{5}{2}\log r + \frac{|L|}{2} + \sum_{\ell \in \mathcal{B}} \frac{\log \ell}{\ell - 1}\Big),
$$

since the terms $N v_\ell \log \ell$ add up to at most $N \log r$. We use the root discriminant $r = \mathrm{rd}_E$ and $L = \operatorname{Re} L'(1, \chi)/L(1, \chi)$ for the Kronecker character $\chi$ of the host.

The proof uses six statements, each proved in the development:

1. the component statement: a root origin over $Y$ gives a clopen irreducible component $U$ of the generic fibre and a component $Z$ over $U$ whose generic point is that of the Hodge component;
2. the period statement: the points of $U$ are periods of a uniformization;
3. the smooth line statement;
4. the local comparison: the local norms of the flat line agree with valuations at the primes outside $\mathcal{B}$, and differ by at most $N(c_\ell \log \ell - \log\|\cdot\|)$ at the primes of $\mathcal{B}$, with $c_2 = 2$ and $c_\ell = 1/(\ell - 1)$ otherwise; it is built from statements on points, on values, on integral frames and on the fibre sandwich;
5. the character statement: there is a Kronecker character $\chi$ modulo $d_H$;
6. the numerics statement, which turns the comparisons and the degree into the near record bound.

**Theorem 9.9.4 (Core construction).** Assume the smooth line, local comparison and numerics statements and the Fargues comparison. Let $Z$ be a component over $U$, let $\varphi$ be a frame function with a flat line of type $\tau$ on the model, and let $N_{\log}$ be adelic log norms whose archimedean and finite parts are the norms of the flat line, invariant under conjugation, with degree

$$
\deg N_{\log} = \frac{p - q}{2}\big(\gamma + \log 2\pi - \log \mathrm{rd}_E - L\big).
$$

Let $\mathfrak{M}$ be a Hodge component over $S$ with the generic point of $Z$, birational coordinates and a flag with root lines and Hodge lines. Assume that $2 \in S$, that $S$ contains the primes dividing the discriminant of $E$, that $\mathfrak{M}$ is Hodge-Tate free at every prime of $S$, that $p + q > 0$, and that the lattices of the Hodge lines are trivial modulo every prime outside $S$. Then there is a number field $F'$ with a map to $\Omega$, integral on the charts, and a smooth hermitian line $\overline{A}$ with $\deg A = \sum_i \deg x_{\tau, i}$, whose metric at the interior points is the product of the metrics of the Hodge lines of type $\tau$, with a flat structure whose height is near the record for $(p + q, S, \mathrm{rd}_E, L)$.

Lean: `RootFieldNumerics.RF.core`

*Proof.* The constants of the Hodge component give a number field $F'$ with a map to $\Omega$. The Hodge component matches a component of the model, and the flat line of type $\tau$ gives, by a comparison of CM type lattices, two lattices $a'$ and $b'$ of the Hodge lines of type $\tau$ on its two sides. The flag degree of the Hodge component is nonzero on the root constants. The line $\overline{A}$ is the smooth line built from the Hodge lines of type $\tau$, and its flat structure comes from the flat line through the lattices.

The height of the flat structure is computed place by place. At the archimedean places it is the degree of $N_{\log}$, which gives $h_{\mathrm{rec}}$ with the bound $|h_{\mathrm{rec}}| \le N(\frac32 \log \mathrm{rd}_E + |L|/2)$ from the degree formula. At a prime outside $S$ the local comparison is exact, by the triviality modulo $\ell$, so there is no correction. At a prime $\ell \in S$ the Fargues comparison gives a sandwich, since $\mathfrak{M}$ is Hodge-Tate free at $\ell$, and the local comparison gives the correction $d_\ell$ with the bound $(N c_\ell + N v_\ell)\log \ell$. The numerics statement collects these bounds into the near record condition. $\square$

**Theorem 9.9.5 (Assembly).** Assume the six statements above, the flat degree statement and the top level inputs. Let $E$ be a CM field, abelian over $\mathbb{Q}$, let $Y$ be a global integral model, let $M$ be a root model of type $(\Psi, p + q)$ with a root origin $o$ over $Y$ for a set $\mathcal{B}$ of primes, and assume that $p, q \ge 1$, that $\mathcal{B}$ is the set of primes dividing $2\, d_E\, M'_l$, where $M'_l$ is a positive integer attached to the level, and that the Hodge component of $o$ is Hodge-Tate free at the primes of $\mathcal{B}$. Then for every CM type $\tau$ there is a flat root line for $(M, \tau)$ whose height is near the record for $(p + q, \mathcal{B}, \mathrm{rd}_E, L)$.

Lean: `RootFieldNumerics.RF.rootFlatOnHodge_of`

*Proof.* Since $Y$ is global, the level is good, there are local systems with split fibres at every prime, and $Y$ descends. The component statement gives $U$ and $Z$. From the top level inputs, the flat degree statement, the period statement and the character statement we get a frame function $\varphi$ with a flat line of type $\tau$ and adelic log norms $N_{\log}$ that satisfy the hypotheses of the core construction, with the degree formula; here the flat degree statement gives the degree $\frac{p-q}{2}\operatorname{Re}\log\Omega(E, \chi)$ of [the previous section](/entry/exists-const-sec/).

Every prime dividing $d_E$ divides $2 d_E M'_l$, so it lies in $\mathcal{B}$, and so does $2$. At the primes outside $\mathcal{B}$ the local systems with split fibres give the triviality of the Hodge lattices modulo $\ell$. The core construction, with the Fargues comparison from the top level inputs, gives $F'$, $\overline{A}$ and a flat structure of near record height.

It remains to make a flat root line. Let $i_0 = p + q - 1$ be the last index. The fundamental reference line at $(\tau, i_0)$ has degree $-\sum_{k \le i_0} \deg x_{\tau, k}$, and the difference of two consecutive fundamental lines is a single root line. A telescoping sum shows that the degree of $A$ is right and that the product of the metrics of the twisted lines $x_t(\tau, i)$ is the metric of $\overline{A}$ times $e^{-v_t}$, with $v_t$ given by the logarithmic metrics of the fundamental lines. The statement on flat hermitian root lines, with the inputs of the proof theory, gives the flat root line with the same flat structure, and so with the same height. $\square$

**Theorem 9.9.6 (Flat root lines on Hodge components).** Assume the flat degree statement and the top level inputs. Then the conclusion of the assembly theorem holds for every global model $Y$, every root model $M$ with a root origin as there, and every CM type.

Lean: `RootFieldNumerics.rootFlatOnHodge`

*Proof.* The six statements are proved in the development; apply the assembly theorem. $\square$

**Theorem 9.9.7 (Flat root lines on good towers).** Assume the flat degree statement and the top level inputs. Let $E$ be a CM field, abelian over $\mathbb{Q}$, let $Y$ be an integral model of $X_o(l)$, let $T$ be a root tower of type $(\Psi, p + q)$ with a good origin $o$ over $Y$, and let $\mathrm{II}$ be an intersection system. Assume that $Y$ is global, that $o$ satisfies the extra conditions, that $\mathrm{II}$ is full and that $p, q \ge 1$. Then for each component $a$ and each CM type $\tau$ the root model $M_{2, a}$ has a flat root line for $\tau$ whose height is near the record for $(p + q, \mathcal{B}_T, \mathrm{rd}_E, L)$, where $\mathcal{B}_T$ is the set of bad primes of $T$.

Lean: `RootFieldNumerics.global_model_tower_final_condition` (also `GlobalTheory.T.good_tower_real_extra` and `GlobalTheory.CompanionTheory.Relay.good_tower_real_extra`, second names)

*Proof.* The good origin gives a root origin of $M_{2, a}$ over the prime set $S_2$, which is the set of bad primes of $T$, and its Hodge component is Hodge-Tate free at these primes. The index of the tower is $p$, with $1 \le p < p + q$. Apply the theorem on flat root lines on Hodge components. $\square$

Only the base level $B = 2$ is needed, since Proposition F concerns the base model. The near record bound gives the term $|L|$ and the term $\log \mathrm{rd}_E$ in $\Lambda_B$.

**Remark 9.9.8 (Formalization).** The theorem on good towers has four hypotheses that are not used: the extra conditions, the fullness of $\mathrm{II}$, and $p, q \ge 1$; the intersection system plays no part in the conclusion ([GlobalModelTowerFinalCondition.lean](lean:Development/WeilBound/CoreStatements/FlagImmersions/GlobalModelTowerFinalCondition.lean#L32)). The name speaks of a final condition, and the two other names speak of a real extra condition; the conclusion is a height bound for flat lines. In the assembly theorem the Fargues comparison and the inputs of the proof theory are taken from the top level inputs by position, as the seventh and tenth parts ([RootFlatOnHodgeOf.lean](lean:Development/WeilBound/CoreStatements/FlagImmersions/RootFlatOnHodgeOf.lean#L30)). The core construction is in a file named after an injectivity lemma ([TauInInjective.lean](lean:Development/WeilBound/CoreStatements/FlagImmersions/TauInInjective.lean#L26)). We have not unfolded the six statements, the unit condition of a flat structure, the integral of the functions $v_t$, or the integer $M'_l$; the description of the core proof is a summary of the steps it calls, not of their proofs, and the reading of $h_{\mathrm{rec}}$ as a record value is ours.
