---
title: The Bessel integral of a discrete series
decls:
  - ReciprocityTheory.ChartRestriction.DS.Mult1.thmM
  - ReciprocityTheory.ChartRestriction.DS.Mult1.thmM_of_xi
  - ReciprocityTheory.ChartRestriction.DS.Mult1.theoremM_of
  - ReciprocityTheory.ChartRestriction.DS.Mult1.stSym
  - ReciprocityTheory.ChartRestriction.DS.Mult1.stInvCC
  - ReciprocityTheory.ChartRestriction.DS.Mult1.InvCC.main
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Bessel integral of a discrete series

This section moves from $\mathrm{GL}_n$ to a real unitary group. Sections 1 and 2 proved that a generic representation has at most one Whittaker functional. Here the role of the Whittaker functional is played by a Bessel functional, and the representation is a discrete series with fast decay. We prove that the local Bessel integral of such a representation factors through one equivariant map (Theorem M). This is an input of the step [HypsAlt is nonempty](/step/nonempty-hyps/), and the [uniqueness of Bessel maps](/entry/bessel-map-uniq-gap/) uses it. On the way we prove two facts about an anti-involution $\theta$ of the group: it preserves the classes of smooth functions with polynomial decay, and the Bessel distribution is invariant under it. For the background on Bessel periods and on multiplicity one, see [Bessel and Fourier-Jacobi periods](/learn/periods/#bessel-and-fourier-jacobi-periods) and [local multiplicity one](/learn/periods/#local-multiplicity-one).

### The setting

Fix integers $k, r \geq 0$ and put $n = 2r + k + 1$. Let $H = H_{k,r}$ be the Hermitian matrix on $\mathbb{C}^n$ that pairs the first $r$ coordinates with the last $r$ coordinates by an antidiagonal block and is diagonal $(1, \ldots, 1, -1)$ on the middle $k + 1$ coordinates. Let $G = \mathrm{U}(H) = \{g : g^* H g = H\}$. On matrices we use the Frobenius norm $\|g\|$.

**Definition 4.5.1 (Bessel data).** A *Bessel datum* $D$ on $G$ consists of the following objects.

1. The unipotent subgroup $N \subset G$ attached to the isotropic flag of the first $r$ coordinates, and a vector $z$ in the middle block with $T_z = \langle z, z \rangle_H > 0$.
2. The character $\psi(m) = \exp(i \operatorname{Re}(c\,\ell_z(m)))$ of $N$, with $c = -2i$ and $\ell_z$ a linear form in the entries of $m$ that depends on $z$.
3. The stabilizer $W \subset G$ of $z$ and of the two isotropic basis vectors that are fixed by the flag. It is compact and it normalizes $N$ and fixes $\psi$.
4. A unitary representation $\pi$ of $W$ on a finite-dimensional Hilbert space $V$, and Haar measures $dh$ on $W$ and $dm$ on $N$.

The datum is *diagonal* if the second copy of the data that enters the two-sided integrals below is equal to the first, $dh$ has total mass $1$, and $\pi$ is irreducible.

**Definition 4.5.2 (Bessel integral).** Let $\sigma$ be an irreducible unitary representation of $G$ on a Hilbert space $\mathcal{H}$, let $w \in \mathcal{H}$ be a unit vector, and let $a > 0$ with $|\langle w, \sigma(x) w \rangle| \leq C_w \|x\|^{-a}$ for $x \in G$. Let $\mathcal{V}_a$ be the set of $u \in \mathcal{H}$ such that $|\langle w, \sigma(x) u\rangle| \leq C \|x\|^{-a}$ for some $C$. For $u, u' \in \mathcal{V}_a$ put
$$\beta(u, u') = \int_W \int_N \langle u', \sigma(mh) u \rangle\, \overline{\psi(m)}\, \pi(h)^{-1} \, dm\, dh \in \mathrm{End}(V).$$

The integral converges when $a$ is large; this is the first step of the proof below. The vector $w$ plays the role of a $K$-finite vector with the decay of a discrete series. The space $\mathcal{V}_a$ is the space on which the decay estimate holds.

**Definition 4.5.3 (Multiplicity one map).** A map $l \colon \mathcal{H} \to V$ is a *multiplicity one map* for $(D, \sigma)$ if $l$ is additive and $\mathbb{C}$-homogeneous on $\mathcal{V}_a$, if $l(\sigma(mh)u) = \psi(m)\pi(h)\, l(u)$ for $u \in \mathcal{V}_a$, $m \in N$, $h \in W$, and if
$$\beta(u, u')\,\xi = \langle l(u'), \xi \rangle\, l(u) \qquad (u, u' \in \mathcal{V}_a,\ \xi \in V).$$

So $\beta$ is of rank one and determined by $l$. The map $l$ may be $0$; then the statement says that $\beta = 0$.

### The anti-involution

A *frame* for $z$ is a matrix $\gamma \in \mathrm{GL}_{k+1}(\mathbb{C})$ with $\gamma^* H_b \gamma = H_b$, $H_b = \mathrm{diag}(1, \ldots, 1, -1)$, whose embedding $E = E_\gamma \in G$ maps the first middle basis vector to $z / \sqrt{T_z}$. For $g \in G$ put
$$\bar g = E\, \overline{E^{-1} g E}\, E^{-1}, \qquad \theta(g) = \bar g^{-1}.$$
Complex conjugation of a matrix in $G$ is in $\mathrm{U}(\bar H) = \mathrm{U}(H)$, so $\bar g \in G$, and $\theta$ is an anti-automorphism of $G$ with $\theta^2 = 1$. It is the archimedean analogue of the anti-involution of Section 1.

For a real number $A$ and an integer $m \geq 0$, let $C^m_A$ be the class of functions $F$ on $n \times n$ matrices that are $C^m$ on $G$ with
$$\|g\|^{A}\, \|\partial_L^{u} \partial_R^{v} F(g)\| \leq c \qquad (g \in G)$$
for all words $u, v$ of total length at most $m$ in elements of norm at most $1$ of the Lie algebra of $G$. Here $\partial_L$ and $\partial_R$ are the derivatives along left and right translation.

**Lemma 4.5.4 (θ preserves decay classes).** Let $D$ be diagonal, let $\sigma$ be square integrable with the decay above, and let $\gamma$ be a frame for $z$. Then there is $C$ with $\|\theta(g)\| \leq C \|g\|$ for $g \in G$, and $F \in C^m_A$ implies $F \circ \theta \in C^m_A$.

Lean: `ReciprocityTheory.ChartRestriction.DS.Mult1.InvCC.main` (also `ReciprocityTheory.ChartRestriction.DS.Mult1.stInvCC`, a second name).

*Proof.* The map $g \mapsto \bar g$ is conjugation by the fixed matrix $E$ composed with entrywise conjugation, so $\|\bar g\| \leq B \|g\|$ with $B = \|E\|\,\|E^{-1}\|$. For $g \in G$ we have $g^{-1} = H^{-1} g^* H$, so $\|\theta(g)\| = \|\bar g^{-1}\| \leq C \|g\|$. Now let $F \in C^m_A$. The chain rule gives $\partial_L^X (F \circ \theta) = (\partial_R^{X'} F) \circ \theta$ with $X' = -\bar X$, and the same with $L$ and $R$ exchanged: $\theta$ exchanges left and right derivatives and transforms the Lie element by $X \mapsto -\bar X$. The norm of $\bar X$ is at most $M \|X\|$ with $M = \max(B, 1)$, so a word of unit elements goes to $M^{\ell}$ times a word of unit elements, where $\ell$ is its length. Left and right derivatives commute, so the transformed word can be put back in the form $\partial_L^{u'} \partial_R^{v'}$. Last, $\|g\|^A$ and $\|\theta(g)\|^A$ differ by at most $C^{|A|}$, by the first part applied to $g$ and to $\theta(g)$. So $F \circ \theta \in C^m_A$ with constant $M^m C^{|A|} \max(c, 0)$. $\square$

### Symmetry of the Bessel distribution

For a function $F$ on matrices with values in $\mathrm{End}(V)$, the *Bessel distribution* is
$$J(F)(g) = \int \psi(m_1)\overline{\psi(m_2)}\, \pi(h_1)\, F(h_1^{-1} m_1^{-1}\, g\, m_2 h_2)\, \pi(h_2)^{-1},$$
where the integral is over $(h_1, m_1, h_2, m_2) \in W \times N \times W \times N$. Let $\mu_d$ be the explicit matrix in $\mathrm{U}(H_b)$ that sends the first middle basis vector to $-\bar d$ times itself plus a multiple $\sqrt{|d|^2 - 1}$ of the last one. For $q = (c, d) \in \mathbb{C}^r \times \mathbb{C}$ let $g_q$ be the element of the big cell with unipotent part given by $c$ and middle part given by a section $\mu(d)$. Let $Q$ be the set of $q$ at which a fixed explicit weight is positive, and let $E_f(q) = \int \|{\text{integrand of } J(f)(g_q)}\|$.

**Theorem 4.5.5 (θ-symmetry).** Let $D$ be diagonal, let $\sigma$ be square integrable with the decay above, and let $\gamma$ be a frame for $z$. Let $f$ be a scalar function on matrices, viewed as $f \cdot \mathrm{id}_V$. Assume that $f$ is integrable on $G$, that $q \in Q$, $T_z^2 < |q_2|^2$ and $E_f(q) < \infty$. Then
$$J(f \circ \theta)(g_q) = J(f)(g_q).$$

Lean: `ReciprocityTheory.ChartRestriction.DS.Mult1.stSym`.

*Proof.* Put $d = -q_2/T_z$. Then $|d| > 1$, and the positivity of the weight at $q$ forces each entry of $q_1$ to be nonzero. Under these conditions $g_q = h^{-1} g_0 h'$ with $h, h' \in W$, where $g_0$ is an explicit element of the big cell built from $q_1$ and $\gamma \mu_d \gamma^{-1}$, and $\theta(g_0) = g_0$. By the equivariance of $J$ under $W$ on both sides, it is enough to prove the claim at $g_0$. Let $Y = J(f \circ \theta)(g_0) - J(f)(g_0) \in \mathrm{End}(V)$. Let $U \subset W$ be the subgroup that also fixes the first vector of the frame. By the equivariance of $J$, $Y$ commutes with $\pi(u)$ for $u \in U$. For each $y \in W$ there is $u_0 \in U$ with $\theta(y) = u_0 y u_0^{-1}$, and $U$ is closed under inverses. With this, the integrands of $J(f \circ\theta)(g_0)$ and $J(f)(g_0)$ are conjugate by $\pi(u_0)$, and their pairings against $Y$ under the trace form $\langle Y, X \rangle = \operatorname{tr}(Y^* X)$ agree. So $\operatorname{tr}(Y^* Y) = 0$ and $Y = 0$. The case where the integrand is not measurable is treated apart. $\square$

### Theorem M

**Theorem 4.5.6 (Theorem M).** Let $D$ be a diagonal Bessel datum, let $\sigma$ be an irreducible unitary representation of $G$ with square integrable matrix coefficients, and let $w$ be a unit vector with the decay above for an exponent $a \geq 4n^3$. Then there is a multiplicity one map $l \colon \mathcal{H} \to V$ for $(D, \sigma)$.

Lean: `ReciprocityTheory.ChartRestriction.DS.Mult1.thmM` (also `ReciprocityTheory.ChartRestriction.DS.Mult1.thmM_of_xi` and `ReciprocityTheory.ChartRestriction.DS.Mult1.theoremM_of`, the forms with the inputs as hypotheses).

*Proof.* The proof uses a list of structural facts on $G$ and one analytic input, a majorant $\Xi$ of the matrix coefficients of $\sigma$ ([the majorant](/entry/xi-exists/)). The main steps are as follows.

1. Let $d$ be the formal degree of $\sigma$: $\int_G |\langle w, \sigma(g)w\rangle|^2\, dg = d^{-1}$ ([Schur orthogonality](/learn/real-groups/#discrete-series-and-formal-degrees)).
2. For $a \geq 4n^3$ the integral $\beta(u, u')$ converges absolutely on $\mathcal{V}_a$.
3. $\beta(u', u) = \beta(u, u')^*$, and $\beta(u, u)$ is positive semidefinite.
4. $\beta$ is bounded by the decay of $u$ and $u'$ with the exponent $a - n^2 - 1$.
5. A reproducing formula writes $u$ as $d$ times an integral of $\sigma(g)w$ against $\langle w, \sigma(g) u \rangle$. It expresses $\beta$ through the Bessel distribution $J$ of matrix coefficients.
6. The $2 \times 2$ minors of the kernel $\beta$ vanish on $\mathcal{V}_a$. This is the deep step. It uses the majorant $\Xi$, the cut-off estimates, the invariance of the decay classes under $\theta$ (Lemma above) and the $\theta$-symmetry (Theorem above, in the form for $\beta$).
7. A positive semidefinite, equivariant kernel with vanishing $2 \times 2$ minors has the form $\beta(u, u')\xi = \langle l(u'), \xi\rangle\, l(u)$ for an equivariant $l$. $\square$

The vanishing of the minors in step 6 is the analogue of the Gelfand-Kazhdan argument of Section 1: the anti-involution $\theta$ fixes the Bessel distribution, and this forces the rank to be at most one.

**Remark 4.5.7 (Formalization).** The general form `theoremM_of` in [TheoremMOf.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/MultiplicityOne/TheoremMOf.lean#L16) takes about twenty-five step statements as hypotheses. Five of them are not used in its proof: the character identity under $\theta$, the transport of $g_q$ to $g_0$, the conjugation of $W$ under $\theta$, the $\theta$-symmetry and the rank one statement for minors. The $\theta$-symmetry is still used, inside the symmetry statement for $\beta$ (JSymBeta.lean, line 15). In the $\theta$-symmetry theorem the integrability of $f$ on $G$ is not used (UuInv.lean, line 154). The subgroup $N$, the linear form $\ell_z$, the weight that defines $Q$ and the section $\mu$ are not unfolded here. Theorem M itself is `thmM_of_xi` applied to the structural facts and to the majorant.
