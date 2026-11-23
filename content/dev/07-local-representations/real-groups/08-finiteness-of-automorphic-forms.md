---
title: Finiteness of automorphic forms with discrete series at infinity
decls:
  - CompanionTheory.D.gk.RF.automorphic_forms_finite_dimensional
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Finiteness of automorphic forms with discrete series at infinity

Harish-Chandra proved that the automorphic forms of a fixed level, a fixed $K$-type and a fixed infinitesimal character form a finite-dimensional space. This section proves the form of this theorem that the later counting arguments need, for a unitary group over a CM field: the image of $L^2(G(F) \backslash G(\mathbb{A}))$ under the projection given by a level at the finite places and a discrete series coefficient at the infinite places is finite-dimensional. The result is used in the step [the nonemptiness hypotheses](/step/nonempty-hyps/), where the multiplicity of a discrete series with given level is a dimension.

Background: [finiteness of automorphic forms](/learn/trace-formula/#finiteness-of-automorphic-forms), [automorphic forms on adelic groups](/learn/automorphic-forms/#automorphic-forms-on-adelic-groups), [quotients of finite volume](/learn/groups/#quotients-of-finite-volume), [discrete series](/learn/representations/#discrete-series).

### The setting

Let $E/F$ be a CM extension of number fields and $J$ a nondegenerate Hermitian $n \times n$ matrix over $E$, with unitary group $G = U(J)$. Fix an $\mathcal{O}_E$-lattice $L \subseteq E^n$ that spans $E^n$ and is self-dual for the Hermitian form: $x \in L$ exactly when the form pairs $x$ integrally with all of $L$. For each infinite place $v$ of $F$ fix an embedding of $E$ into $\mathbb{C}$ above $v$ and a matrix $P_v$ that carries $J$ to a diagonal sign matrix $J_{\varepsilon_v}$, so that $G(F_v) \cong U(J_{\varepsilon_v})$, a group $U(p_v, q_v)$.

Write $G_\infty = \prod_{v \mid \infty} U(J_{\varepsilon_v})$ and $G_f = G(\mathbb{A}_f)$, so that $G(\mathbb{A}) = G_\infty \times G_f$. Let $K \subseteq G_f$ be the stabiliser of the adelic lattice $\widehat{L}$; the principal congruence subgroups of $K$ form a basis of neighbourhoods of $1$ in $G_f$. Let $\mu_\infty$ be the product of fixed Haar measures on the groups $U(J_{\varepsilon_v})$, $\mu_f$ a Haar measure on $G_f$, and $\mu = \mu_\infty \times \mu_f$.

Let $D \subseteq G(\mathbb{A})$ be a measurable fundamental domain for $G(F)$ acting on the left: every $y$ has a translate $\gamma y \in D$ with $\gamma \in G(F)$, and $\gamma D \cap D$ is $\mu$-null for $\gamma \neq 1$. Then $L^2(G(F) \backslash G(\mathbb{A}))$ is $L^2(D, \mu)$, and the right regular representation $R$ acts by $R(g) f(x) = f(\overline{x g})$, where $\overline{y}$ is the representative of $y$ in $D$.

**Definition 2.8.1 (Convolution operators).** For an integrable function $\phi$ on $G(\mathbb{A})$, the operator $R(\phi)$ on $L^2(D)$ is defined by $\langle x, R(\phi) y \rangle = \int \phi(g) \langle x, R(g) y \rangle\, d\mu(g)$. The same formula, with $G_\infty$ or $G_f$ in place of $G(\mathbb{A})$, defines $R(\phi_\infty)$ and $R(e)$ for functions on the factors.

**Definition 2.8.2 (Discrete series data at infinity).** For each infinite place $v$, let $\sigma_v$ be an irreducible unitary representation of $U(J_{\varepsilon_v})$ on a Hilbert space $H_v$, square integrable with formal degree $d_v$ for the measure above, and $w_v \in H_v$ a unit vector whose matrix coefficient $g \mapsto \langle w_v, \sigma_v(g) w_v \rangle$ is integrable. Put
$$\phi_\infty(g) = \prod_v d_v\, \overline{\langle w_v, \sigma_v(g_v) w_v \rangle}.$$

By Schur orthogonality, $\phi_\infty * \phi_\infty = \phi_\infty$, and $R(\phi_\infty)$ is the orthogonal projection on the vectors of $L^2$ that transform at infinity like $w = \otimes_v w_v$ in a copy of $\sigma = \otimes_v \sigma_v$.

### The theorem

The classical statement is the following (Harish-Chandra, *Automorphic forms on semisimple Lie groups*, Lecture Notes in Math. 62 (1968), Chapter I, Theorem 1). Let $G$ be a reductive group over $\mathbb{Q}$, $\Gamma$ an arithmetic subgroup, $K_\infty$ a maximal compact subgroup of $G(\mathbb{R})$, $\tau$ a finite-dimensional representation of $K_\infty$, and $\mathfrak{J}$ an ideal of finite codimension in the centre of the universal enveloping algebra. Then the space of automorphic forms on $\Gamma \backslash G(\mathbb{R})$ of type $\tau$ annihilated by $\mathfrak{J}$ is finite-dimensional.

**Theorem 2.8.3 (Finiteness of automorphic forms).** In the setting above, let $e$ be a locally constant integrable function on $G_f$ with support in $K$, and $\sigma_v, w_v, d_v$ discrete series data at the infinite places. Then the range of $R(e) R(\phi_\infty)$ on $L^2(G(F) \backslash G(\mathbb{A}))$ is finite-dimensional.

Lean: `CompanionTheory.D.gk.RF.automorphic_forms_finite_dimensional`.

**Remark 2.8.4 (How the Lean form differs).** The Lean statement is adelic and replaces "$K$-type and infinitesimal character" by a projection: a vector in the range of $R(e) R(\phi_\infty)$ is fixed under right translation by a compact open subgroup and lies in the $w$-line of the $\sigma$-isotypic part at infinity, so it is an automorphic form with discrete series at infinity, of a fixed level. The function $e$ need not be idempotent or bi-invariant; the theorem holds for each such $e$. The operator $R(\phi_\infty)$ is described only through its matrix coefficients, as an operator-valued integral, and so is $R(e)$.

### The proof

*Proof.* Call a function $h$ on $G(\mathbb{A})$ *representable* for an integrable function $\phi$ if $h$ is continuous, bounded, left $G(F)$-invariant, and $h(x) = \int \phi(y) h(x y)\, d\mu(y)$ for all $x$. There are four steps.

*Step 1: a level.* Since $e$ is locally constant with support in the compact open group $K$, there is a compact open subgroup $K' \subseteq K$ with $e(k x) = e(x)$ for $k \in K'$ and all $x$: take the $k \in K$ that fix $e$ under left translation; this group is open because $e$ is locally constant on the compact set $K$. Put
$$\phi_{K'}(g_\infty, g_f) = \phi_\infty(g_\infty) \cdot \frac{\mathbf{1}_{K'}(g_f)}{\mu_f(K')}.$$
The operator $R(e) R(\phi_\infty)$ is convolution by $\phi_\infty \otimes e$, and $\phi_{K'} * (\phi_\infty \otimes e) = \phi_\infty \otimes e$, by $\phi_\infty * \phi_\infty = \phi_\infty$ at infinity and the left $K'$-invariance of $e$ at the finite places. Hence, for bounded $F_0$, the vector $R(e) R(\phi_\infty) F_0$ is represented by a function that is representable for $\phi_{K'}$. Bounded functions are dense in $L^2$, so the range of $R(e) R(\phi_\infty)$ lies in the closure of the representable functions for $\phi_{K'}$.

*Step 2: integrable idempotents have no constant terms.* Let $H$ be a locally compact group with Haar measure, $\phi$ an integrable function with $\phi * \phi = \phi$, $N \subseteq H$ a subgroup, $a : \mathbb{R} \to H$ a continuous one-parameter group normalising $N$, and $\mathrm{ht}$ a continuous height with $\mathrm{ht}(m g) = \mathrm{ht}(g)$ for $m \in N$, $\mathrm{ht}(a(t) g) = t + \mathrm{ht}(g)$, bounded change under right translation, and with $N a(t)$ close to $1$ after conjugation for small $t$. These are the data of the unipotent radical $N$ of a proper parabolic subgroup of $U(J_{\varepsilon_v})$ with a split one-parameter torus. Then for every bounded continuous left $N$-invariant $F$,
$$\int \phi(y) F(x y)\, dy = 0 \quad \text{for all } x.$$
The proof is Fourier analysis along $a$: on the bounded continuous functions invariant under $N$ and under $a$, convolution by $\phi$ twisted by $e^{i s (\mathrm{ht}(x y) - \mathrm{ht}(x))}$ is a continuous family $Q(s)$ of idempotent operators that tends to $0$ as $s \to \infty$, an oscillatory integral estimate; a continuous family of idempotents tending to $0$ is identically $0$, since an idempotent of norm less than $1$ is $0$. Fourier inversion in $s$ then removes the invariance under $a$ and gives the display. This is Harish-Chandra's argument that integrable eigenfunctions are cuspidal (LNM 62, Chapter I).

*Step 3: reduction theory.* Let $\Gamma_M \subseteq G_\infty$ be the arithmetic group of level $M$; it is discrete. By reduction theory (transport to a standard form at each infinite place, successive minima of the lattices $y L$, Mahler compactness, and a covering of the unipotent quotients $\Gamma_M \cap N \backslash N$ by compact sets), for every neighbourhood $U$ of $1$ in $G_\infty$ there is a compact $C$ such that every $y \in G_\infty$ either has a $\Gamma_M$-translate in $C$, or there is a nonzero isotropic subspace $W$ of $E^n$ whose unipotent radical $N_W$ satisfies: for every $m \in N_W$ there is $\gamma \in \Gamma_M \cap N_W$ with $y^{-1} \gamma m y \in U$. In the second case, averaging over a fundamental set of $\Gamma_M \cap N_W$ in $N_W$ gives a probability measure $\nu$ carried by elements $m$ with $y^{-1} m y \in U$, such that $x \mapsto \int u(m x)\, d\nu(m)$ is left $N_W$-invariant for every bounded continuous $\Gamma_M$-invariant $u$. By step 2 applied to this average, $\int u(m y)\, d\nu(m) = 0$ whenever $u$ is representable for $\phi_\infty$. The congruence subgroups at the finite places transfer this to $G(\mathbb{A})$ and $\phi_{K'}$: away from a compact set modulo $G(F)$, a representable function averages to $0$ over a probability measure carried by elements conjugate into $U$. The rational points form a discrete subgroup: they meet each compact set in a finite set.

*Step 4: finitely many linear forms.* With step 3 and the discreteness, a general argument on locally compact groups with a lattice gives a continuous compactly supported $\alpha$ and finitely many points $p_1, \dots, p_m$ such that a representable $h$ of finite $L^2$ norm on $D$ with $\int \alpha(y) h(p_i y)\, dy = 0$ for all $i$ is $0$. Near the compact part, $\alpha$ approximates $\phi_{K'}$ in $L^1$ and the values of $h$ are bounded by its $L^2$ norm, uniformly; in the cusps the averages of step 3 make $h$ small. So the map $h \mapsto (\int \alpha(y) h(p_i y)\, dy)_i$ is injective on representable functions and bounded for the $L^2$ norm, and a subspace of the closure of the representable functions is finite-dimensional. By step 1, this applies to the range of $R(e) R(\phi_\infty)$. $\square$

**Remark 2.8.5 (Formalization).** The topology on $G(\mathbb{A}_f)$ is not derived from the adeles: it is part of the data of the instance, through the two conditions that the principal congruence subgroups are open and form a basis at $1$ ([GlobAut.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/GlobAut.lean#L32)). The fundamental domain is only measure-theoretic, and the right regular representation is any family of operators that acts by right translation almost everywhere. The steps are separate proved statements joined in [RowsFinDimOf.lean](lean:CompanionTheory/HarishChandraModules/KFiniteAnalyticVectors/FundamentalDomainCusps/RowsFinDimOf.lean#L25); the reduction theory inputs are assembled in the same module as the theorem.
