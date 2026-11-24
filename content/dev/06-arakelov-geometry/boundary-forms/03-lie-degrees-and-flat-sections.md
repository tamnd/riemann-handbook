---
title: Lie degrees and flat sections at the last level
decls:
  - GlobalTheory.DefCoreLie.degLie_core_alt
  - GlobalTheory.T.degLie_eq_neg_flatDegVal_at_last_index
  - GlobalTheory.DefFlat.flatExistsAt_core_alt
  - GlobalTheory.T.flatExistsAt_last_index_of_fnAlgClosed
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Lie degrees and flat sections at the last level

At the last level of the tower the datum is definite: its signature is $(p, 0)$. This section computes two degrees there. The first is the Arakelov degree of the Lie determinant at a rational point. The second is the degree of a flat section on a component. Both are given by one number, built from a logarithmic period of the CM field and its root discriminant. The two results are the input of the low defect bound of the next section, which bounds the slope of the core lattice from below.

We use the language of [the first section](/entry/to-classical-theorems/). Fix a family, a point $p$ with the row condition, and a level $i$ with $i + 1 = m$. Let $X$ be the moduli space at level $i + 1$ over the coefficient field $F$, with signature $(p_i, q_i)$, and let $U$ be its family of uniformizations. Let $\Psi$ be the CM type of the host field $E$, one complex embedding $\tau$ from each conjugate pair, let $\mathrm{rd}(E)$ be the root discriminant of $E$, and let $d_E$ be the integer of the host that is the modulus of its Kronecker character. Let $\log \Omega$ be the logarithmic period of the record of the point. We assume the Gram condition at level $i$ and two lists of numerical conditions.

**Definition 2.3.1 (Weight numerics and host numerics).** The *weight numerics* at $(p, i)$ with parameter $P$ say, among other conditions: the signature is the one of the family and $p_i + q_i = r$; the number of CM types is $f$; the flag dimension is $f \binom{r}{2}$; the unit of error is $E = f\, m\, b\, L \log\log x$; $|\log \Omega| \le 3L$; the weights are bounded by $4b$; and $P^2 r m k d^3 \le b$. The *host numerics* with parameters $P$, $A$ and $M$ say, among other conditions: $M \le L$, $10 \le L \le x$, $1 \le \log\log x$; $f \ge 8$ and $[E : \mathbb{Q}] = 2f$; $\log |\mathrm{disc}(E)| \le 4 f L$; $\log d_E \le L$; $15$ is prime to the two host primes $g_0 g_1$; $P \le x^A$ and $(x^A)^M \le b$.

These conditions make all the error terms below at most a constant times $E$. In this section they are only carried along.

**Definition 2.3.2 (Flat degree value).** For a datum of signature $(p_i, q_i)$ put
$$\phi = \frac{p_i - q_i}{2} \log \Omega + q_i \bigl(\log d_E - \log \mathrm{rd}(E)\bigr).$$

At the last level $q_i = 0$, so $\phi = \frac{p_i}{2} \log \Omega$. For a component $Z$ of $X$ and $\tau \in \Psi$ there is a set of *flat sections* on $Z$ at $\tau$, and each flat section $s$ has a degree $\deg s \in \mathbb{R}$. We do not unfold the flat sections or their degree.

**Definition 2.3.3 (Point datum and Lie degree).** A *point datum* on a component $Z$ is an $F$-rational point $y_0$ that lies only on $Z$, with a frame matrix $B_w(\tau)$ at each finite place $w$ of $F$, equal to $1$ at almost all $w$, and a matrix $X_\sigma(\tau)$ at each complex embedding $\sigma$ of $F$. Its *Lie degree* at $\tau$ is
$$\deg_{\mathrm{Lie}}(\tau) = \sum_w v_w\bigl(\det B_w(\tau)\bigr)\, \ell_w - \frac{1}{[F : \mathbb{Q}]} \sum_\sigma \log \bigl| \det X_\sigma(\tau) \bigr|,$$
where the weights $\ell_w$ satisfy $\sum_w v_w(n) \ell_w = \log n$ for each integer $n \ge 1$.

This is the Arakelov degree of the determinant line of the Lie algebra at $y_0$, computed from local frames: the finite part counts the valuations of the frames and the infinite part their archimedean norms ([hermitian lattices and slopes](/learn/arakelov/#hermitian-lattices-and-slopes)).

**Theorem 2.3.4 (Lie degree at the last level).** Let $p$ satisfy the row condition and let $i + 1 = m$. Assume the Gram condition, the weight numerics with parameter $P$ and the host numerics with parameters $P$, $A$ and $M$ at $(p, i)$, and assume that $F$ is algebraically closed in the function field of each component of $X$. Then for each component $Z$, each point datum on $Z$ and each $\tau \in \Psi$,
$$\deg_{\mathrm{Lie}}(\tau) = -\phi.$$

Lean: `GlobalTheory.DefCoreLie.degLie_core_alt` (also `GlobalTheory.T.degLie_eq_neg_flatDegVal_at_last_index`, a second name).

*Proof.* At the last level the moduli space has finitely many components, at least one, and the datum is in the definite case: $q_i = 0$, $p_i \ge 1$, the uniformizations have good reduction at all primes and satisfy the laws of the core. The host numerics give a Kronecker character $\chi$ modulo $d_E$ with
$$\operatorname{Re} \log \Omega(E, \chi) = \log \Omega,$$
where $\log \Omega(E, \chi) = \gamma + \log\bigl(2\pi / \mathrm{rd}(E)\bigr) - L'(1, \chi)/L(1, \chi)$ and $\gamma$ is the Euler constant. Next we compute the degree of a flat section. Pick a CM point of good reduction on $Z$ and compare the degrees of two eigenlattices of the Lie algebra of its CM abelian variety. The difference is the period $\operatorname{Re} \log \Omega(E, \chi)$ times $\frac{p_i - q_i}{2}$. So each flat section $s$ on $Z$ at $\tau$ has $\deg s = \frac{p_i - q_i}{2} \log \Omega = \phi$, since $q_i = 0$. A flat section exists in the definite case. Finally, a lemma on the dual of the Lie determinant compares the point datum with a flat section $s$ on $Z$ at $\tau$: $\deg_{\mathrm{Lie}}(\tau) = -\deg s$. So $\deg_{\mathrm{Lie}}(\tau) = -\phi$. $\square$

The value $\frac{p_i}{2} \log \Omega$ has the shape of the Chowla-Selberg formula, which writes the Faltings height of a CM abelian variety through logarithmic derivatives of $L$-functions at $s = 1$. We use only the statement above.

**Theorem 2.3.5 (Flat sections at the last level).** Under the hypotheses of the previous theorem, for each component $Z$ of $X$ and each $\tau \in \Psi$ there is a flat section on $Z$ at $\tau$, and every flat section $s$ on $Z$ at $\tau$ has
$$\deg s = \phi.$$

Lean: `GlobalTheory.DefFlat.flatExistsAt_core_alt` (also `GlobalTheory.T.flatExistsAt_last_index_of_fnAlgClosed`, a second name).

*Proof.* The datum is in the definite case, as in the previous proof. Existence: a flat section exists on $Z$ at $\tau$, because $q_i = 0$, $p_i \ge 1$, the uniformizations have good reduction and are unfolded, and $F$ is algebraically closed in the function field. Degree: the component $Z$ has a point datum, a rational point with local frames. For a flat section $s$, the lemma on the dual of the Lie determinant gives $\deg_{\mathrm{Lie}}(\tau) = -\deg s$. By [Theorem 2.3.4](/entry/deg-lie-core-alt/), $\deg_{\mathrm{Lie}}(\tau) = -\phi$. So $\deg s = \phi$. $\square$

The degree of a flat section is the same on every component and for every $\tau$. This is the form in which the next section uses it: in the slope of the core lattice, the flat sections contribute $\phi$ for each $\tau$, and the defect bound compares the slope with $\phi$.

**Remark 2.3.6 (Formalization).** The second theorem states `FlatExistsAt U ξ (-flatDegVal …)`, and `FlatExistsAt a` asks for degree $-a$, so the degree is $\phi$ ([ExistsFlatSecRankZero.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/ExistsFlatSecRankZero.lean#L746)). Its proof at [FlatExistsAtCore.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FlatExistsAtCore.lean#L14) passes through a point datum and the first theorem, whose proof at [DegLieCore.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/DegLieCore.lean#L16) computes the degree of a flat section and moves it back to the point datum by the same lemma. So the detour only moves the result back and forth. The first theorem is a copy of `degLie_core` in [ComponentPointLastIndex.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ComponentPointLastIndex.lean#L47). We have not unfolded the flat sections, their degree, the laws of the core, or the lemma that compares eigenlattices of a CM object; the comparison with the Chowla-Selberg formula is by the shape of the formula only. The weight and host numerics are structures with more fields than we list.
