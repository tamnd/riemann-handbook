---
title: Hermitian forms on derivatives and the exponent bound
decls:
  - PositivityTheory.RgUd.Form.U.Lift2.uLift
  - PositivityTheory.RgUd.Form.U.Lift2.absLift
  - PositivityTheory.RgUd.Form.U.Lift2.lift_form
  - PositivityTheory.RgUd.expBound
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Hermitian forms on derivatives and the exponent bound

An invariant inner product on a representation of $\mathrm{GL}_N(k)$ does not pass to its derivatives directly, since the derivatives are quotients. Bernstein's method moves the form down the mirabolic tower one column at a time. At each step the form splits into a part at the trivial character of the column, called the atom, and a part at a nontrivial character, called the density. This section proves the lifting theorem at the heart of the method, states the two consequences used by the [irreducibility theorem](/entry/bern-at/), and proves a bound on the central exponents of a unitary generic product. All of these feed the step [EveryCharacter](/step/every-character/).

Background: [smooth representations of $p$-adic groups](/learn/representations/#smooth-representations-of-p-adic-groups), [generic representations](/learn/representations/#generic-representations-and-local-factors), [[unitary representation|74BPYJNZTM]].

### Forms with a column action

Let $k$ be a nonarchimedean local field with absolute value $|\cdot|$, and let $\psi$ be a nontrivial continuous additive character of $k$. Fix $m \ge 0$ and write $X = k^{m+1}$, with the standard pairing $\xi \cdot x$. Let $e = (0, \dots, 0, 1) \in X$.

A *column setup* on a complex vector space $V$ is a pair of actions: an action $x \mapsto c(x)$ of the additive group $X$ and an action $g \mapsto \gamma(g)$ of $\mathrm{GL}_{m+1}(k)$, both smooth, with $\gamma(g)\, c(x) = c(g x)\, \gamma(g)$. For $\pi$ a smooth representation of $\mathrm{GL}_N(k)$ with $N \ge m + 2$, the column $x$ placed above the diagonal in column $m + 2$ and the block $\mathrm{GL}_{m+1}(k)$ in the upper left corner give a column setup on the space of $\pi$.

A sesquilinear form $B$ on $V$ is *positive* if $B(w, v) = \overline{B(v, w)}$ and $B(v, v) \ge 0$ for all $v, w$. A *lattice* is a compact open subgroup $A \subseteq X$. For a lattice $A$ and $\xi \in X$, let $\mathrm{av}^\xi_A$ be the averaging operator
$$\mathrm{av}^\xi_A(v) = \frac{1}{[A : A']} \sum_{t \in A / A'} \overline{\psi(\xi \cdot t)}\, c(t)\, v,$$
where $A' \subseteq A$ is any lattice small enough that it fixes $v$ and lies in the kernel of $t \mapsto \psi(\xi \cdot t)$. It projects $v$ onto the part on which $A$ acts by the character $t \mapsto \psi(\xi \cdot t)$.

**Definition 7.6.1 (Density and atom).** Let $B$ and $B'$ be sesquilinear forms on $V$ and $A_0$ a lattice. The form $B'$ is the *density* of $B$ at $e$ relative to $A_0$ if for all $v, w$ there is a lattice $A_1 \supseteq A_0$ such that
$$B'(v, w) = [A : A_0]\; B(\mathrm{av}^e_A v, w) \quad \text{for every lattice } A \supseteq A_1.$$
The *atom* of $B$ is the limit of $B(\mathrm{av}^0_A v, w)$ as $A$ grows.

Lean: `PositivityTheory.RgUd.Form.U.Lift2.IsD` (also `PositivityTheory.RgUd.Form.U.Lift2.IsA`).

The density measures how much of $B$ sits at the character $\psi(e \cdot\,)$ of the column. The factor $[A : A_0]$ makes it independent of $A$, since the projection shrinks as $A$ grows.

### The lifting theorem

**Theorem 7.6.2 (Abstract lift).** Let $(c, \gamma)$ be a column setup on $V$, let $s \in \mathbb{R}$, and let $A_0$ be a lattice. Let $B$ be a positive form with $B(c(x) v, c(x) w) = B(v, w)$ and $B(\gamma(g) v, \gamma(g) w) = |\det g|^s B(v, w)$. Let $B'$ be the density of $B$ at $e$ relative to $A_0$. Let $C$ be a positive form such that

1. $C(c(x) v, w) = \psi(e \cdot x)\, C(v, w)$ for all $x \in X$,
2. $C(\gamma(p) v, \gamma(p) w) = |\det p|^{s+1} C(v, w)$ for all $p$ in the mirabolic subgroup $P_{m+1}$,
3. $C(v, v) \le B'(v, v)$ for all $v$.

Then there is a positive form $I$ on $V$ with the following properties.

1. $I$ is invariant under $c$, and $I(\gamma(g) v, \gamma(g) w) = |\det g|^s I(v, w)$.
2. $I(v, v) \le B(v, v)$ for all $v$.
3. The density of $I$ at $e$ relative to $A_0$ is $C$, and the atom of $I$ is $0$.
4. If a subspace $Y$ is stable under $\gamma$ and $C(y, w) = 0$ for all $y \in Y$, then $I(y, w) = 0$ for all $y \in Y$.

Lean: `PositivityTheory.RgUd.Form.U.Lift2.absLift` (also `PositivityTheory.RgUd.Form.U.Lift2.lift_form`).

*Proof.* The group $\mathrm{GL}_{m+1}(k)$ acts on row vectors, and the orbit of $e$ is $X \setminus \{0\}$. The stabilizer of $e$ is $P_{m+1}$. For $\xi \neq 0$ choose $g_\xi$ with $e\, g_\xi^{-1} = \xi$, and put
$$C_\xi(v, w) = |\det g_\xi|^{s+1}\; C\big(\gamma(g_\xi)^{-1} v, \gamma(g_\xi)^{-1} w\big), \qquad C_0 = 0.$$
Two choices of $g_\xi$ differ by an element of $P_{m+1}$, so condition 2 shows that $C_\xi$ does not depend on the choice. Each $C_\xi$ is positive, and condition 1 with the relation between $\gamma$ and $c$ gives $C_\xi(c(x) v, w) = \psi(\xi \cdot x)\, C_\xi(v, w)$. The map $\xi \mapsto C_\xi(v, w)$ is locally constant on $X \setminus \{0\}$.

Let $\nu$ be the [[Haar measure|VY0HXD3GC4]] on $X$ with $\nu(A_0^\perp) = 1$, where $A_0^\perp$ is the set of $\xi$ with $\psi(\xi \cdot a) = 1$ for all $a \in A_0$. Define
$$I(v, w) = \int_X C_\xi(v, w)\, d\nu(\xi).$$

*Bound and integrability.* Translate condition 3 by $g_\xi$: the form $C_\xi$ is bounded by the density of $B$ at $\xi$, by the equivariance of $B$. For a lattice $A$ and a smaller lattice $A'$ that fixes $v$, the operators $\mathrm{av}^\xi_A$, for $\xi$ in a set of representatives of the characters of $A/A'$, are orthogonal projections for $B$ with sum the identity on $v$. So the sum of $B(\mathrm{av}^\xi_A v, v)$ over these $\xi$ equals $B(v, v)$. Each term is $\nu(A^\perp)$ times the density of $B$ at $\xi$, for $A$ large. So the integral of the densities, and with it the integral of $C_\xi(v, v)$, is at most $B(v, v)$. The function $\xi \mapsto C_\xi(v, w)$ is then integrable, by the inequality $|C_\xi(v, w)| \le \frac12 (C_\xi(v, v) + C_\xi(w, w))$. This gives property 2, and $I$ is positive.

*Equivariance.* Since $|\psi(\xi \cdot x)| = 1$, each $C_\xi$ is invariant under $c$, and so is $I$. For $g \in \mathrm{GL}_{m+1}(k)$, the forms satisfy $C_\xi(\gamma(g) v, \gamma(g) w) = |\det g|^{s+1} C_{\xi g}(v, w)$. The substitution $\xi \mapsto \xi g^{-1}$ in the integral contributes $|\det g|^{-1}$, which gives property 1.

*Density and atom.* Near $e$ the function $\xi \mapsto C_\xi(v, w)$ is constant and equal to $C(v, w)$. The averaging $\mathrm{av}^e_A$ picks out the integral of $C_\xi$ over $e + A^\perp$, which has measure $\nu(A^\perp) = [A : A_0]^{-1}$. So the density of $I$ is $C$. In the same way the atom of $I$ is the limit of the integral over $A^\perp$, a neighbourhood of $0$ that shrinks to $\{0\}$. The measure of $\{0\}$ is zero, so the atom vanishes.

*Kernels.* If $Y$ is stable under $\gamma$ and killed by $C$, then $\gamma(g_\xi)^{-1} Y = Y$ is killed by $C$, so $Y$ is killed by every $C_\xi$ and by $I$. $\square$

**Corollary 7.6.3 (Lift for derivatives).** Let $\pi$ be a smooth representation of $\mathrm{GL}_N(k)$ and $m + 2 \le N$. Let $B$ be a positive form on $\pi$ of level $m$: it kills the twisted kernel of the unipotent group of level $m + 2$, and it is equivariant with exponent $s$ under the mirabolic group of level $m + 1$. Let $C$ be a positive form of level $m + 1$ with exponent $s + 1$, bounded by the density of $B$. Then there is a form $I$ of level $m$ with exponent $s$, bounded by $B$, with density $C$ and atom $0$.

Lean: `PositivityTheory.RgUd.Form.U.Lift2.uLift`.

*Proof.* Apply the abstract lift to the column setup of $\pi$ at level $m$. The invariance of $B$ under the column comes from its equivariance under the mirabolic group, since a unipotent matrix has determinant $1$. $\square$

### Unitary derivatives

The lift is one of seven steps in Bernstein's analysis of forms on derivatives. The others split a form of level $m$ into its atom and its density, show that the atom is a form of the derivative at that level, and bound the eigenvalues of scalar matrices when the atom is zero. Starting from the invariant inner product of an irreducible unitarisable $\pi$, and using [Theorem B](/entry/thm-b/) to fix each form up to a scalar, one gets the following two statements. Let $\pi^{(h)}$ be the highest nonzero derivative of $\pi$.

**Theorem 7.6.4 (Top derivative).** Let $\pi$ be an irreducible unitarisable representation of $\mathrm{GL}_{n+h}(k)$ with $h \ge 1$ and $\pi^{(h)}$ its highest nonzero derivative. Then $\pi^{(h)} \nu^{(1-h)/2}$ is irreducible and unitarisable.

Lean: `PositivityTheory.RgUd.Form.U.Final.derivTop`.

**Theorem 7.6.5 (Lower derivatives).** Let $\pi$ be as above, $1 \le i$, and assume that a derivative of order larger than $i$ is nonzero. Let $\sigma$ be a nonzero subquotient of $\pi^{(i)} \nu^{(1-i)/2}$ with central character $\omega$. Then $|\omega(z)| < 1$ for every $z \in k^\times$ with $|z| < 1$.

Lean: `PositivityTheory.RgUd.Form.U.Final.derivPos`.

### The exponent bound

Let $\pi = \pi_1 \times \dots \times \pi_h$ be a product of irreducible representations $\pi_j$ of $\mathrm{GL}_{n_j}(k)$. For a character $\omega$ of $k^\times$ with $|\omega(z)| = |z|^{n_j s}$, call $s$ the *central exponent* of $\pi_j$.

**Theorem 7.6.6 (Exponent bound).** Assume that $\pi$ is irreducible, unitarisable and generic. Then every factor $\pi_j$ with $n_j \ge 1$ has central exponent $s$ with $|s| < \tfrac12$.

Lean: `PositivityTheory.RgUd.expBound`.

The lower bound comes from a growth estimate on the Whittaker form.

**Proposition 7.6.7 (Lower bound).** Let $A$ and $x$ be smooth generic representations of $\mathrm{GL}_r(k)$ and $\mathrm{GL}_m(k)$, with $r, m \ge 1$. Let $x$ have central character $\omega$ with $|\omega(z)| = |z|^{m s}$. If $A \times x$ is generic and unitarisable, then $s > -\tfrac12$.

Lean: `PositivityTheory.RgUd.Cell.expLow`.

*Proof.* Let $N = r + m$ and let $a(z)$ be the diagonal matrix with $z$ in the first $m$ entries and $1$ in the others. Two facts are used.

First, a unitarisable $\Pi$ of $\mathrm{GL}_N(k)$ carries a positive form $Q$ whose null vectors are exactly the kernel of the Whittaker functional, and for $|z| < 1$ the series
$$\sum_{i \ge 0} |z|^{-i m (N - m - 1)}\; Q\big(\Pi(a(z^i)) v, \Pi(a(z^i)) v\big)$$
converges for every $v$. The form $Q$ is the norm of the Kirillov model restricted to the torus, and the series is a Bessel inequality for it.

Second, on the open cell of the flag variety of $A \times x$, there are vectors $f$ and $f_0$, with $f_0$ outside the Whittaker kernel, such that for all large $i$
$$\Pi(a(z^i)) f \equiv |z|^{i m r / 2}\, \omega(z)^i\, f_0$$
modulo the Whittaker kernel.

Put these together. The $i$-th term of the series for $v = f$ is
$$|z|^{-i m (r - 1)}\, |z|^{i m r}\, |z|^{2 i m s}\, Q(f_0, f_0) = |z|^{i m (1 + 2s)}\, Q(f_0, f_0),$$
with $Q(f_0, f_0) > 0$. The series converges only if $|z|^{m(1+2s)} < 1$, that is, $s > -\tfrac12$. $\square$

*Proof of the theorem.* Since $\pi$ is irreducible, its factors can be permuted without changing $\pi$. Move $\pi_j$ to the last place and group the other factors into one representation $A$. Then $\pi \cong A \times \pi_j$, and the lower bound gives $s > -\tfrac12$. Now let $\theta(g) = w\, {}^t g^{-1} w$, with $w$ the antidiagonal permutation matrix. The representation $\pi \circ \theta$ is again irreducible, unitarisable and generic, and it is the product of the $\pi_l \circ \theta$ in the reverse order. The factor $\pi_j \circ \theta$ has central character $\omega^{-1}$, with central exponent $-s$. The same argument gives $-s > -\tfrac12$. $\square$

**Remark 7.6.8 (Formalization).** The abstract lift is stated in [SmoothCol.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/HermitianForms/UnitaryLattices/SmoothColumnLifts/SmoothCol.lean#L70) and proved in [MeasurableSpaceFourthLift.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/HermitianForms/UnitaryLattices/LatticeIndexLifts/MeasurableSpaceFourthLift.lean#L239). The name of that file comes from a local instance of the Borel structure on $k$ that it declares at line 15, not from its content; the same holds for the second and third files of the series. The forms $C_\xi$ are built with a choice function $\xi \mapsto g_\xi$ that is not continuous; only its independence of the choice is used. The averaging operator depends on a chosen pair of a small lattice and a set of representatives, and it is $0$ when no such pair exists. The corollary is derived in [ULiftOfAbs.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/HermitianForms/UnitaryLattices/SmoothColumnLifts/ULiftOfAbs.lean#L25), and the seven steps are combined with Theorem B in [DerivPos.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/HermitianForms/UnitaryLattices/DerivPos.lean). The two theorems on derivatives are obtained as the two parts of one assembled statement, which is evaluated twice. The exponent bound is assembled in [ExpBound.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/BernsteinExponentBounds/ExpBound.lean) from [ExpBoundOf.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/GenericIrreducibility/ExpBoundOf.lean#L15), and the lower bound is in [ExpLow.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/OpenCellDecomposition/PiTensorNontriviality/ExpLow.lean#L125). The convergence statement uses the natural number $N - m - 1$, which is safe because $m < N$ is assumed ([IsInvForm.lean](lean:Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof/BernsteinExponentBounds/IsInvForm.lean#L25)).
