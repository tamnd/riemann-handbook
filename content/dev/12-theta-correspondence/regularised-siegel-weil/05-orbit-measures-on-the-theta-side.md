---
title: Orbit measures on the theta side
decls:
  - GlobalTheory.CompanionTheory.QKAvg.modular_stab
  - GlobalTheory.CompanionTheory.QKAvg.qk
  - GlobalTheory.CompanionTheory.ColumnSplitting.main
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Orbit measures on the theta side

The residue of the Siegel Eisenstein series at the edge will be written, in the next section, as an integral against a measure on a quadric of pairs of matrices. This section defines these measures, which we call orbit measures, and builds one from the theta side: an orbital integral over a unitary group, averaged over a compact subgroup and integrated along an isotropic subspace. The construction needs the modular character of the stabiliser of an isotropic subspace, and an averaging formula over a compact subgroup that follows from it. The theta-side measure is one of the two measures that the proof of [Theorem 5.7.3](/entry/res-core/) compares.

We keep the notation of the earlier sections. For a Hermitian space $V$ over $E$ of rank $m_V$ we write $U(V)(\mathbb{A})$ for the [adelic points](/learn/groups/#adelic-points-and-compact-open-subgroups) of its unitary group, and $\langle x, y \rangle = x^* V y$ for matrices $x, y$ with $m_V$ rows. We fix Hermitian spaces $B$ and $W$ with $r = m_W \ge 1$ and an integer $t \ge 1$, together with a *hyperbolic decomposition*: matrices $u, u'$ of size $m_B \times t$ and an isometry $i_0$ of $W$ into $B$ with
$$\langle u, u \rangle = 0, \quad \langle u', u' \rangle = 0, \quad \langle u', u \rangle = 1, \quad \langle i_0, u \rangle = \langle i_0, u' \rangle = 0, \quad m_B = r + 2t.$$
So $B$ is $W$ plus $t$ hyperbolic planes. Let $X$ be the isotropic subspace of rank $t$ in $B(\mathbb{A}_E)$ that the decomposition gives.

### The modular character of the stabiliser

Let $Q \subset U(B)(\mathbb{A})$ be the stabiliser of $X$. Each $q \in Q$ acts on $X$ by a matrix $\alpha_q \in GL_t(\mathbb{A}_E)$, and $q \mapsto |\det \alpha_q|$ is a continuous character of $Q$. The modular character $\Delta_Q$ of a locally compact group $Q$ measures how a left [[Haar measure|VY0HXD3GC4]] changes under right translation ([Haar measure](/learn/analysis/#haar-measure)).

**Proposition 5.5.1 (Modular character of the stabiliser).** Assume that $Q$ is locally compact. Then $\Delta_Q(q) = |\det \alpha_q|^{r+t}$ for all $q \in Q$.

Lean: `GlobalTheory.CompanionTheory.QKAvg.modular_stab`.

*Proof.* The group $Q$ is the semidirect product of its unipotent radical $N$ and a Levi subgroup $M$: both are closed, $Q = NM$ and $N \cap M = 1$. We take the following facts as given. There is a Haar measure $\nu_N$ on $N$ such that conjugation by $m \in M$ multiplies $\nu_N$ by $|\det \alpha_m|^{r+t}$. There is a right invariant Haar measure on $M$. For a semidirect product with these properties, the modular character is the given character, provided the character is trivial on $N$. Finally $|\det \alpha_q| = 1$ for $q \in N$, because $N$ acts trivially on $X$. These facts give the formula. $\square$

**Definition 5.5.2 (Good level).** A *good level* for $B$ is a pair of an $\mathcal{O}_E$-lattice $L \subset E^{m_B}$ that is self-dual at each finite place and a majorant of $B$ at the archimedean places. Its *level subgroup* $K_L \subset U(B)(\mathbb{A})$ is the stabiliser of these data. It is compact.

**Theorem 5.5.3 (Average over a good level).** Let $L$ be a good level for $B$ and $\nu_K$ a Haar measure on $K_L$. Let $s \colon U(B)(\mathbb{A}) \to [0, \infty]$ be measurable with $s(qh) = |\det \alpha_q|^{r+t} s(h)$ for $q \in Q$ and $h \in U(B)(\mathbb{A})$. Then for each $g \in U(B)(\mathbb{A})$
$$\int_{K_L} s(kg)\, d\nu_K(k) = \int_{K_L} s(k)\, d\nu_K(k).$$

Lean: `GlobalTheory.CompanionTheory.QKAvg.qk`.

*Proof.* We take as given that a good level gives an Iwasawa decomposition $U(B)(\mathbb{A}) = Q K_L$, and that $Q$ is closed, so that it is locally compact. The group $U(B)(\mathbb{A})$ is unimodular, so a Haar measure on it is also right invariant. We also take as given the general integration formula: if $G$ is unimodular, $G = QK$ with $Q$ closed and $K$ compact, and $s \ge 0$ is measurable with $s(qh) = \Delta_Q(q) s(h)$, then $g \mapsto \int_K s(kg)\, d\nu_K(k)$ is constant. By the [Proposition 5.5.1](/entry/modular-stab/), $\Delta_Q(q) = |\det \alpha_q|^{r+t}$, so the hypothesis on $s$ is the hypothesis of the formula. $\square$

### Idempotents and orbit measures

The orbit measures live on adelic matrices, and to compare them with functions of a fixed level we cut off the places outside a finite set. Fix a finite set $S$ of finite places of $F$. An *$S$-idempotent* is an $e \in \mathbb{A}_E$ with $e_w = 1$ at the archimedean places, $e_v = 1$ for $v \in S$ and $e_v = 0$ for finite $v \notin S$. Multiplication by $e$ keeps the components at $\infty$ and at $S$ and kills the others.

**Theorem 5.5.4 (Idempotents).** For each finite set $S$ of finite places there is an $S$-idempotent, and each $S$-idempotent $e$ satisfies $e^2 = e$ and $\bar e = e$.

Lean: `PositivityTheory.Rg.Rsw.L.idemEx`.

*Proof.* We take this result as given; we do not prove it in this chapter. $\square$

A matrix $x$ over $\mathbb{A}_E$ is *integral off $S$* if its entries are integral at each finite $v \notin S$. A function $\Phi$ on matrices is *good for $(S, e)$* if $\Phi(x) = \Phi(ex)$ when $x$ is integral off $S$, and $\Phi(x) = 0$ otherwise. So a good function is the product of its part at $\infty$ and $S$ with the characteristic function of the integral matrices off $S$.

Let $b_0 \in \mathrm{Herm}_r(E)$ with $\det b_0 \neq 0$. For a Hermitian space $V$ and a pair $z = (z_1, z_2)$ of matrices over $\mathbb{A}_E$ of sizes $m_V \times r$ and $m_V \times t$, put
$$y(z) = b_0^{-1} \langle z_1, z_2 \rangle, \qquad q(z) = \langle z_2, z_2 \rangle - y(z)^* b_0\, y(z).$$
Then $z_2 - z_1 y(z)$ is orthogonal to $z_1$ when $\langle z_1, z_1 \rangle = b_0$, and $q(z)$ is its Gram matrix.

**Definition 5.5.5 (Orbit measure).** Let $V$ be a Hermitian space, $b_0$ as above and $e \in \mathbb{A}_E$. An *orbit measure* for $(V, b_0, e)$ is a measure $\nu$ on pairs $z = (z_1, z_2)$ as above such that:

1. $\nu$ is finite on compact sets;
2. $\nu$-almost every $z$ has $e z_1 = z_1$, $e z_2 = z_2$, $\langle z_1, z_1 \rangle = e\, b_0$ and $q(z) = 0$;
3. $\nu$ is invariant under $z \mapsto (h z_1, h z_2)$ for $h \in U(V)(\mathbb{A})$ with $e(h - 1) = h - 1$;
4. $\nu$ is invariant under $z \mapsto (z_1, z_2 + z_1 y)$ for $y \in M_{r \times t}(\mathbb{A}_E)$ with $ey = y$;
5. the image of $\nu$ under $z \mapsto (z_1, z_2 g)$ is $|\det g|^{-(r+t)} \nu$ for $g \in GL_t(\mathbb{A}_E)$ with $e(g - 1) = g - 1$.

For $e = 1$ the support condition says that the columns of $z_1$ have Gram matrix $b_0$ and that the projection of $z_2$ orthogonal to $z_1$ spans an isotropic space. Conditions 3 to 5 are the symmetries of this set: the unitary group of $V$, the shift of $z_2$ by the columns of $z_1$, and a change of basis of the isotropic part.

### The theta-side measure

We fix the following data. Let $n = r + t$. Let $L$ be a good level for $B$, $\nu_K$ the Haar probability measure on $K_L$, $\mu_1$ a measure of covolume one on $M_{t \times n}(\mathbb{A}_E)$, and $m$ a Haar measure on $U(W)(\mathbb{A})$. For a function $\Phi$ on $M_{m_B \times n}(\mathbb{A}_E)$ let $\mathcal{I}\Phi$ be the function on $M_{r \times n}(\mathbb{A}_E)$ obtained in two steps: average $\Phi$ over $K_L$, then integrate against $\mu_1$ in the direction of $X$. For $x_0 \in M_r(E)$ and $y \in M_{r \times t}(\mathbb{A}_E)$ put
$$O_\Phi(y) = \int_{U(W)(\mathbb{A})} (\mathcal{I}\Phi_y)\big(h^{-1} (x_0 \mid 0)\big)\, dm(h), \qquad \Phi_y(x) = \Phi\Big(x \begin{pmatrix} 1 & y \\ 0 & 1 \end{pmatrix}\Big).$$
This is an orbital integral of a theta-type kernel over the unitary group of $W$, at the point $x_0$ extended by zero.

**Theorem 5.5.6 (Orbit measure on the theta side).** Assume the conclusion of the theorem on idempotents, and assume:

1. for each Hermitian space $V$, each $k$ and each Schwartz function $M$ on $M_{m_V \times k}(\mathbb{A}_E)$ there is $C$ with $\sum_x |M(h^{-1} x)| \le C$ for all $h \in U(V)(\mathbb{A})$, where $x$ runs over the matrices in $M_{m_V \times k}(E)$ of rank $m_V$;
2. the conclusion of the theorem on the average over a good level;
3. the average over $K_L$ and the map $\mathcal{I}$ take Schwartz functions to Schwartz functions.

Let $\mu$ be a Haar measure on $M_{r \times t}(\mathbb{A}_E)$, $b_0 \in \mathrm{Herm}_r(E)$ with $\det b_0 \neq 0$, and $x_0 \in M_r(E)$ with $x_0^* W x_0 = b_0$. Then there is an orbit measure $\nu$ for $(B, b_0, 1)$ such that:

1. there is a finite $S_0$ such that for each finite $S \supseteq S_0$ the set of $z$ with $z_1$ and $z_2$ integral off $S$ has nonzero $\nu$-measure;
2. for Schwartz functions $\Phi$ on $M_{m_B \times n}(\mathbb{A}_E)$ and $\eta$ on $M_{r \times t}(\mathbb{A}_E)$, the function $z \mapsto \Phi(z_1 \mid z_2)\, \overline{\eta(y(z))}$ is $\nu$-integrable, $O_\Phi$ is continuous, and
$$\int \Phi(z_1 \mid z_2)\, \overline{\eta(y(z))}\, d\nu(z) = \int O_\Phi(y)\, \overline{\eta(y)}\, d\mu(y).$$

Lean: `GlobalTheory.CompanionTheory.ColumnSplitting.main`.

*Proof.* We give the construction; the properties of the measure are lemmas that we take as given. The measure $\nu$ is the image of $\nu_K$ times a measure on a parameter space under $(k, p) \mapsto k^{-1} z(p)$, where $z(p)$ is a pair built from $x_0$ and the parameter $p$. Finiteness on compact sets, the support on the quadric, the invariance under the shifts $(z_1, z_2 + z_1 y)$, the scaling under $GL_t(\mathbb{A}_E)$ and the nonzero mass of the integral points are properties of this construction. The invariance under $U(B)(\mathbb{A})$ is where the [Theorem 5.5.3](/entry/qk/) on the average over a good level enters, together with a transformation law of the construction under $Q$. The integrability of $\Phi(z_1 \mid z_2)\, \overline{\eta(y(z))}$ and the continuity of $O_\Phi$ use the lattice bound of hypothesis 1 and the preservation of Schwartz functions of hypothesis 3, through a fundamental domain for $U(W)(F)$. The identity of the two integrals comes from an integration over the fibres of $z \mapsto y(z)$. $\square$

**Remark 5.5.7 (Formalization).** The theorem on the theta side takes the theorem on idempotents as a hypothesis but does not use it ([ImportsLast.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ImportsLast.lean#L43)). The proposition on the modular character assumes that the stabiliser is locally compact; the average over a good level gets this from the closedness of the stabiliser. We have not unfolded the Schwartz spaces nor the parameter measure in the construction of $\nu$, and we have not opened the analytic lemmas of the last proof; we state only what the proofs use from them.
