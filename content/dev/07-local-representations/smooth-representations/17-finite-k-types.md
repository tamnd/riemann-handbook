---
title: Finite K-types
decls:
  - GlobalTheory.T.unitary_K_type_finite
  - GlobalTheory.CompanionTheory.IsoTypes.finiteDimensional_isotypic
  - GlobalTheory.T.cuspidal_K_type_finite
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Finite K-types

A unitary irreducible representation of a real reductive group is admissible: each type of the maximal compact subgroup occurs in it with finite multiplicity. This section proves two forms of this fact for $\mathrm{GL}_a$ over a totally complex number field. The first form is local at the archimedean places. The second form is global: in an irreducible cuspidal representation in $L^2$, the vectors of a fixed $K_\infty$-type that are invariant under an open subgroup of the finite adelic group form a finite-dimensional space. The second form is the input that makes $K$-finite cusp forms smooth in Section 18, and through it the cuspidal spectrum enters the base change argument of the step [EveryCharacter](/step/every-character/). For background see [representations of real groups](/learn/representations/#representations-of-real-groups) and [compact groups](/learn/representations/#compact-groups).

### Setting

Let $E$ be a totally complex number field with $r$ complex places, and let $\mathbb{A} = E_\infty \times \mathbb{A}_f$ be its adele ring, with $E_\infty \cong \mathbb{C}^r$. Put
$$G = \mathrm{GL}_a(\mathbb{A}), \qquad G_\infty = \mathrm{GL}_a(E_\infty) \cong \mathrm{GL}_a(\mathbb{C})^r, \qquad G_f = \mathrm{GL}_a(\mathbb{A}_f),$$
so that $G = G_\infty \times G_f$ and the two factors commute. Let $K_\infty = \mathrm{U}(a)^r$ be the group of unitary matrices in $G_\infty$. For $t \in \mathbb{R}$ let $z(t) \in G_\infty$ be the scalar matrix $e^t$ at every complex place, and put
$$\Gamma = \mathrm{GL}_a(E)\cdot z(1)^{\mathbb{Z}}.$$
Let $\mu$ be a right invariant Haar measure on $G$, let $L^2 = L^2(\Gamma \backslash G)$ for the measure that $\mu$ induces, and let $R$ be the right regular representation of $G$ on $L^2$. It is unitary. Let $L^2_{\mathrm{cusp}} \subseteq L^2$ be the closed subspace of cusp forms.

**Definition 1.17.1 (Type space).** Let $C$ be a group, let $\sigma$ be a representation of a group containing $C$ on a Hilbert space $V$, and let $\rho$ be a representation of $C$ on a finite-dimensional space $W$. The *$\rho$-type space* $V[\rho]$ is the sum, over all linear maps $T : W \to V$ with $T\rho(k) = \sigma(k)T$ for all $k \in C$, of the images $T(W)$.

The maps $T$ need not be continuous, and $\rho$ need not be continuous or irreducible. When $\rho$ is irreducible and continuous, $V[\rho]$ is the $\rho$-isotypic subspace.

### The archimedean form

**Theorem 1.17.2 (Admissibility of unitary representations).** Let $G_0 \subseteq \mathrm{GL}_n(\mathbb{C})$ be a linear reductive group and $K_0 = G_0 \cap \mathrm{U}(n)$. Let $\sigma$ be a unitary representation of $G_0$ on a Hilbert space $V$ that is topologically irreducible. For every finite-dimensional $K_0$-stable subspace $S \subseteq V$ that is irreducible under $K_0$, the sum of the spaces $T(S)$, over linear maps $T : V \to V$ that commute with $K_0$ on $S$, is finite-dimensional. The group $\mathrm{GL}_a(\mathbb{C})^r$, embedded block diagonally in $\mathrm{GL}_{ar}(\mathbb{C})$, is linear reductive, and its intersection with $\mathrm{U}(ar)$ is $K_\infty$.

Lean: `GlobalTheory.CompanionTheory.admitted.isAdmissible_of_unitary_irreducible` (also `GlobalTheory.CompanionTheory.AdmIwa.RamifiedPrimeLengthBound`).

This is the theorem of Harish-Chandra, in the proof by Godement's polynomial identity; see Knapp, *Representation Theory of Semisimple Groups*, Chapter VIII, Section 1.

**Theorem 1.17.3 (Finite K-types for GL over E).** Let $\sigma$ be a unitary representation of $G_\infty$ on a Hilbert space $V$ that is topologically irreducible. For every representation $\rho$ of $K_\infty$ on a finite-dimensional complex vector space $W$, the type space $V[\rho]$ is finite-dimensional.

Lean: `GlobalTheory.T.unitary_K_type_finite`.

*Proof.* By the input, every finite-dimensional irreducible $K_\infty$-stable subspace $S$ of $V$ has finitely many independent copies in $V$, in the sense that the sum $V\langle S \rangle$ of the images of $S$ under $K_\infty$-maps is finite-dimensional. Let $T : W \to V$ be a $K_\infty$-map. Its image $T(W)$ is a finite-dimensional $K_\infty$-stable subspace. Since $\sigma$ is unitary, the orthogonal complement in $T(W)$ of a stable subspace is stable, so $T(W) = S_1 \oplus \dots \oplus S_l$ with each $S_i$ stable and irreducible. The orthogonal projection onto $S_i$ composed with $T$ maps $W$ onto $S_i$, so $S_i$ is an irreducible quotient of $W$. By the Jordan-Hölder theorem, $W$ has finitely many irreducible quotients up to isomorphism; choose one subspace $S^\tau \subseteq V$ in each class $\tau$ that occurs in $V$. Each $S_i$ is isomorphic to some $S^\tau$, so $S_i \subseteq V\langle S^\tau\rangle$. Hence $T(W) \subseteq \sum_\tau V\langle S^\tau \rangle$, which is a finite sum of finite-dimensional spaces and does not depend on $T$. $\square$

### The cuspidal form

**Theorem 1.17.4 (Inputs on cusp forms and compact operators).**

1. $G_f$ has a compact open subgroup.
2. For every continuous compactly supported $f$ on $G$, the operator $R(f) = \int_G f(g)R(g)\,d\mu(g)$ restricted to $L^2_{\mathrm{cusp}}$ is compact.
3. Let $\pi$ be a unitary representation of a group on a Hilbert space $V$ with *enough compact operators*: for each $v \neq 0$ there is a compact operator $A$ that commutes with every bounded operator commuting with $\pi$, such that $Av \neq 0$. Then $V$ is a Hilbert direct sum of closed irreducible subrepresentations. Each irreducible $\pi'$ has finite multiplicity, and this multiplicity is the number of summands isomorphic to $\pi'$.

Lean: `GlobalTheory.GLIntegral.exists_isOpen_isCompact` (also `GlobalTheory.T.cuspidal_convolution_compact`, `GlobalTheory.DiscreteSum.exists_isHilbertSum`, `GlobalTheory.DiscreteSum.EnoughCompact.multIn_lt`, `GlobalTheory.DiscreteSum.multIn_eq_ncard`).

Item 2 is the compactness theorem of Gelfand and Piatetski-Shapiro; for the adelic form see Godement (1966). Item 3 is the spectral theorem for compact self-adjoint operators, applied as in Godement (1966).

**Theorem 1.17.5 (Finite K-types in cuspidal representations).** Let $H \subseteq L^2_{\mathrm{cusp}}$ be a closed $G$-stable subspace on which $R$ is irreducible. Let $U$ be an open subgroup of $G_f$ and let $\rho$ be a representation of $K_\infty$ on a finite-dimensional space $W$. Then the sum of the images $T(W)$, over linear maps $T : W \to L^2$ with
$$T\rho(k) = R(k)T \ (k \in K_\infty), \qquad T(W) \subseteq H, \qquad R(u)T(w) = T(w) \ (u \in U,\ w \in W),$$
is finite-dimensional.

Lean: `GlobalTheory.CompanionTheory.IsoTypes.finiteDimensional_isotypic` (also `GlobalTheory.T.cuspidal_K_type_finite`).

*Proof.* Step 1: reduction to a compact level. By input 1 choose a compact open $K_0 \subseteq G_f$ and put $U' = U \cap K_0$, a compact open subgroup. Vectors fixed by $U$ are fixed by $U'$, so it is enough to prove the claim for $U'$. Let $X = H^{U'}$ be the space of vectors of $H$ fixed by $R(U')$. It is closed, and it is $G_\infty$-stable since $G_\infty$ commutes with $G_f$. So $X$ is a unitary representation of $G_\infty$, and every $T$ in the claim maps $W$ into $X$.

Step 2: enough compact operators. Let $v \in X$ be nonzero. The function $g \mapsto \mathrm{Re}\langle v, R(g)v \rangle$ is continuous on $G_\infty$ and positive at $1$. Choose a continuous $\varphi \geq 0$ on $G_\infty$ with compact support in the set where it is positive and $\varphi(1) \neq 0$, and put $f(g) = \varphi(g_\infty)\mathbf{1}_{U'}(g_f)$. This $f$ is continuous with compact support, since $U'$ is open and compact. Let $A$ be the compression of $R(f)$ to $X$. By input 2, $A$ is compact. For $x \in X$ and $g_f \in U'$ we have $R(g)x = R(g_\infty)x$, so
$$\langle y, Ax\rangle = \int_G f(g)\,\langle y, R(g_\infty)x\rangle\,d\mu(g) \qquad (x, y \in X).$$
So $A$ commutes with every bounded operator on $X$ that commutes with $G_\infty$, and $\mathrm{Re}\langle v, Av \rangle > 0$. So $X$ has enough compact operators.

Step 3: $X$ is isotypic. Let $\pi$ be an irreducible unitary representation of $G_\infty$ with a nonzero map into $X$, and let $Y \subseteq X$ be the closed $\pi$-isotypic subspace. For $b \in G_f$ the compression $P_X R(b) P_X$ of $R(b)$ to $X$ commutes with $G_\infty$, so it maps $Y$ into $Y$. Let $Z$ be the closed span of the translates $R(g)Y$, $g \in G$. It is $G$-stable, nonzero and contained in $H$, so $Z = H$ by irreducibility. Write $g = g_\infty g_f$. For $y \in Y$, $P_X R(g)y = P_X R(g_f)R(g_\infty)y$ lies in $Y$ because $R(g_\infty)y \in Y$. So $P_X(H) \subseteq Y$, and since $X \subseteq H$ this gives $X = Y$.

Step 4: finiteness. By Step 2 and input 3, $X$ is a Hilbert sum of irreducible representations of $G_\infty$, and by Step 3 they are all isomorphic to one $\pi$. Since the multiplicity of $\pi$ is finite, the sum has finitely many terms $V_1, \dots, V_l$. Let $T$ be as in the claim, and let $p_i$ be the orthogonal projection onto $V_i$. Each $p_i T$ is a $K_\infty$-map into $V_i$, so its image lies in the type space $V_i[\rho]$, which is finite-dimensional by the archimedean form. Since $T(w) = \sum_i p_i T(w)$, every $T(W)$ lies in $V_1[\rho] + \dots + V_l[\rho]$. $\square$

The multiplicity one theorem for $\mathrm{GL}_a$ is not used. The proof uses only that $H$ is irreducible under the whole group $G$, so that its $U'$-fixed part is isotypic under $G_\infty$.

**Remark 1.17.6 (Formalization).** The archimedean theorem is proved as `admissible_GL_Cinf` in [UnitaryKTypeFinite.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/UnitaryKTypeFinite.lean#L145), from `finiteDimensional_isoPart_gl` (L104), which embeds $G_\infty$ in $\mathrm{GL}_{ar}(\mathbb{C})$ by the map `blk` and then argues by induction on $\dim W$ instead of by quotients. The admissibility input is `isAdmissible_of_unitary_irreducible`, fed by a theorem named `RamifiedPrimeLengthBound` in [AdmissibleOfLinearReductive.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/AdmissibleOfLinearReductive.lean#L196); that name does not describe its content, which is the admissibility property `AdmG` derived from the four inputs `finite_rank_of_irreducible_unitary`, `small_irreducible_representation`, `transfer_holds` and `exists_averaging_operator`. The cuspidal theorem is in [CuspidalKTypeFinite.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/CuspidalKTypeFinite.lean#L358); Steps 2, 3 and 4 are `enoughCompact_fixedPart` (L341), `isoPart_eq_top` (L72) and `finiteDimensional_types` (L21), joined by `finiteDimensional_types_of_irred` (L169). The group $\Gamma$ is `latticeGL`, which contains $z(1)^{\mathbb{Z}}$ only, not all $z(t)$. Both statements take $\rho$ as a representation of $K_\infty$ as an abstract group and allow all linear maps $T$, with no continuity. Both wrappers set `maxHeartbeats 1000000`. The definitions of `L2cusp` and `IsIrredSubrep` were not unfolded.
