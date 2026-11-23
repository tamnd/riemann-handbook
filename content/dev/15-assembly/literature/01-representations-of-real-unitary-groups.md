---
title: Representations of real unitary groups
decls:
  - UpperTheory.LiteratureTheorems.casselman_wallach_of_literature
  - UpperTheory.LiteratureTheorems.harish_chandra_analyticity_of_literature
  - UpperTheory.LiteratureTheorems.gk_globalisation_of_literature
  - UpperTheory.LiteratureTheorems.formal_degree_compact_dual_of_literature
  - UpperTheory.LiteratureTheorems.real_metaplectic_representation_of_literature
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Representations of real unitary groups

This section states five results on representations of real Lie groups: the analyticity of matrix coefficients and a density theorem of Harish-Chandra, the passage between unitary representations and their Harish-Chandra modules, the Casselman-Wallach extension theorem, the formal degree of a discrete series representation, and the existence of the metaplectic representation of the real symplectic group. The proof takes all five from the literature. The first four are fields of the bundles of the [unitary group hypotheses](/step/published-results-eigen/) and of the [local theta inputs](/step/published-results-first/), which feed the step [EveryCharacter from the literature](/step/every-character-of-literature/). The metaplectic representation is a field of the second bundle. Background is in [real reductive groups](/learn/real-groups/#real-reductive-groups), [discrete series and formal degrees](/learn/real-groups/#discrete-series-and-formal-degrees) and [the Heisenberg and metaplectic groups](/learn/groups/#the-heisenberg-and-metaplectic-groups).

**Definition 1.1.1 (The groups $U(J_\varepsilon)$).** Let $n \geq 0$ and $\varepsilon = (\varepsilon_1, \dots, \varepsilon_n)$ a sequence of signs. Let $J_\varepsilon$ be the diagonal matrix with entries $\varepsilon_i \in \{\pm 1\}$. The [[unitary group|0R9R0Y1HDK]] of $J_\varepsilon$ is

$$U(J_\varepsilon) = \{ g \in M_n(\mathbb{C}) : g^* J_\varepsilon g = J_\varepsilon \}.$$

If $p$ signs are $+1$ and $q$ signs are $-1$, then $U(J_\varepsilon)$ is isomorphic to $U(p, q)$. Let $K_\varepsilon$ be its maximal compact subgroup, isomorphic to $U(p) \times U(q)$, and let $\mathfrak{g}_\varepsilon$ be its Lie algebra.

All the representations of this section act on a Hilbert space $H$. A vector $v \in H$ is $K$-*finite* if $\pi(K_\varepsilon) v$ spans a finite-dimensional space, and *smooth* if $g \mapsto \pi(g) v$ is smooth. The $K$-finite vectors of a unitary representation form a $(\mathfrak{g}_\varepsilon, K_\varepsilon)$-module, its [[Harish-Chandra module|2MKHH636C3]]. A representation is *admissible* if each irreducible representation of $K_\varepsilon$ occurs in it with finite multiplicity.

**Theorem 1.1.2 (Harish-Chandra: analyticity and density).** Let $G = U(J_\varepsilon)$.

1. Let $\pi$ be a continuous admissible representation of $G$ on a Hilbert space $H$ on which $K_\varepsilon$ acts by isometries. Then for all $K$-finite $v, w \in H$ the matrix coefficient $g \mapsto \langle w, \pi(g) v \rangle$ is real analytic on $G$.
2. Let $P$ be the parabolic subgroup of $G$ that stabilises an isotropic flag, with each step of dimension at least $1$, and let $M$ be its Levi factor. Let $\sigma$ be an irreducible unitary representation of $M$ on a Hilbert space $V$. Let $S \subseteq V$ be a nonzero subspace of $K_M$-finite vectors such that, for each $X$ in the Lie algebra of $M$ and each $v \in S$, the derivative of $t \mapsto \sigma(\exp tX) v$ at $t = 0$ exists and lies in $S$. Then $S$ is dense in $V$.

Lean: `UpperTheory.LiteratureTheorems.harish_chandra_analyticity_of_literature`.

The two parts are the analyticity theorem and the density theorem of Harish-Chandra (Trans. Amer. Math. Soc. 75, 1953). They do not depend on each other.

*Proof.* We take both parts from Harish-Chandra. In the development they are [Theorem 1.1.6 of Volume 8](/entry/harish-chandra-analyticity-density/). $\square$

**Theorem 1.1.3 (Harish-Chandra modules determine unitary representations).** Let $G = U(J_\varepsilon)$.

1. (Admissible closure.) Let $\sigma$ be a unitary representation of $G$ on a Hilbert space $H$, and let $V \subseteq H$ be an admissible $(\mathfrak{g}_\varepsilon, K_\varepsilon)$-submodule of smooth $K$-finite vectors. Then the closure $\overline{V}$ is stable under $G$, and every $K$-finite vector of $\overline{V}$ lies in $V$.
2. (Infinitesimal equivalence.) Let $\sigma_1, \sigma_2$ be irreducible unitary representations of $G$ on nonzero Hilbert spaces $H_1, H_2$, and let $e$ be an isomorphism of $(\mathfrak{g}_\varepsilon, K_\varepsilon)$-modules from the $K$-finite vectors of $H_1$ to those of $H_2$. Then there are a unitary $G$-isomorphism $U : H_1 \to H_2$ and a constant $c > 0$ with $U v = c \, e(v)$ for every $K$-finite $v$.

Lean: `UpperTheory.LiteratureTheorems.gk_globalisation_of_literature`.

*Proof.* Both parts are due to Harish-Chandra; see Wallach, *Real Reductive Groups I*, Chapter 3. In the development this is [Theorem 1.1.5 of Volume 8](/entry/gk-globalisation-holds/). $\square$

The next theorem goes from Harish-Chandra modules to smooth representations on more general spaces. A *smooth Fréchet representation* here is a representation $\pi$ of $G$ on a complete Hausdorff locally convex space $E$, whose topology is given by a sequence of seminorms, with a derived action $d\pi$ of $\mathfrak{g}_\varepsilon$.

**Theorem 1.1.4 (Casselman-Wallach).** Let $\sigma$ be an irreducible unitary representation of $G = U(J_\varepsilon)$ on a Hilbert space $H$, and let $(\pi, E)$ be a smooth Fréchet representation of $G$. Let $T_0 : H \to E$ be a linear map that is a map of $(\mathfrak{g}_\varepsilon, K_\varepsilon)$-modules on the $K$-finite vectors. Then there is a linear map $T : H \to E$ such that:

1. $T = T_0$ on the $K$-finite vectors;
2. $T$ is $G$-equivariant and continuous on smooth vectors;
3. every other $T'$ with properties 1 and 2 agrees with $T$ on the smooth vectors;
4. the image under $T$ of the smooth vectors is closed in $E$;
5. if $T_0$ is nonzero on some $K$-finite vector, then each Sobolev norm of a smooth vector $w$, built from a finite list of words in $\mathfrak{g}_\varepsilon$, is bounded by a continuous seminorm of $T w$.

Lean: `UpperTheory.LiteratureTheorems.casselman_wallach_of_literature`.

In its standard form (Casselman, Canad. J. Math. 41, 1989; Wallach, *Real Reductive Groups II*, Chapter 11) the theorem says that every map of Harish-Chandra modules extends uniquely to a continuous map of their smooth globalisations of moderate growth, with closed image. Parts 1 to 4 are this statement for the smooth vectors of a unitary representation. Part 5 is the topological isomorphism onto the image.

*Proof.* We take the result from the sources above. In the development it is [Theorem 9.8.3 of Volume 3](/entry/casselman-wallach/). $\square$

**Theorem 1.1.5 (Formal degree of the discrete series).** Fix Haar measures on the groups $U(p, q)$ such that $U(N)$ has total mass one and such that, near the identity, $U(p, q)$ and its compact dual $U(p + q)$ have the same density with respect to one Lebesgue measure on the Lie algebra, pulled back through the exponential map. Let $N \geq 1$, a sign vector $\varepsilon$ of length $N$, and $\lambda = (\lambda_1 > \dots > \lambda_N)$ real numbers with $\lambda_a - \tfrac{N-1}{2} \in \mathbb{Z}$ for all $a$. Let $\sigma$ be a discrete series representation of $U(J_\varepsilon)$ with Harish-Chandra parameter $\lambda$ on a Hilbert space $H$. Then for every nonzero $w \in H$,

$$\frac{\|w\|^4}{\displaystyle\int_{U(J_\varepsilon)} |\langle w, \sigma(g) w \rangle|^2 \, dg} = \prod_{a < b} \frac{|\lambda_a - \lambda_b|}{b - a}.$$

Lean: `UpperTheory.LiteratureTheorems.formal_degree_compact_dual_of_literature`.

By the Schur orthogonality relations the left side is the formal degree $d_\sigma$. The right side is $\prod_{\alpha > 0} |\langle \lambda, \alpha \rangle| / \langle \rho, \alpha \rangle$, Harish-Chandra's formula, with the measure normalised through the compact dual as above.

*Proof.* This is Harish-Chandra's formula for the formal degree (Acta Math. 116, 1966). In the development it is [Theorem 7.9.4 of Volume 7](/entry/formal-degree-compact-dual/). $\square$

**Definition 1.1.6 (Schrödinger representation).** Let $l$ be a nonempty finite set and $\mathbb{R}^{2l} = \mathbb{R}^l \times \mathbb{R}^l$ with coordinates $w = (p, q)$. For $f \in L^2(\mathbb{R}^l)$ let

$$\rho(w) f (x) = \exp\big(2 \pi i \langle q, x \rangle + \pi i \langle p, q \rangle\big) \, f(x + p).$$

Then $\rho(w)$ is unitary. This is the Schrödinger model of the [[Heisenberg group|ZZYCV5EX9J]], restricted to $\mathbb{R}^{2l}$. Let $\mathcal{S}(\mathbb{R}^l)$ be the Schwartz space. For $X \in \mathfrak{sp}_{2l}(\mathbb{R})$ let $Q(X)$ be the second-order operator on $\mathcal{S}(\mathbb{R}^l)$ obtained from the quadratic form $X J$ through the derived action of $\rho$: in terms of the derived operators $D_a$ of $\rho$ at the unit vectors, $Q(X) = (4 \pi i)^{-1} \sum_{a, b} \tfrac12 (XJ)_{ab} (D_a D_b + D_b D_a)$.

**Theorem 1.1.7 (Metaplectic representation).** For every nonempty finite set $l$ there are a topological group $G$, a homomorphism $\mathrm{pr} : G \to \mathrm{Sp}_{2l}(\mathbb{R})$, a unitary representation $\omega$ of $G$ on $L^2(\mathbb{R}^l)$ and a representation $\omega_S$ of $G$ on $\mathcal{S}(\mathbb{R}^l)$ by continuous operators with these properties.

1. $\mathrm{pr}$ is a surjective covering map with kernel $\{1, \epsilon\}$, $\epsilon \neq 1$, and $\omega(\epsilon) = -1$.
2. $\omega$ is strongly continuous.
3. $\omega(g) \rho(w) = \rho(\mathrm{pr}(g) w) \omega(g)$ for all $g$ and $w$.
4. $\omega(g)$ restricted to Schwartz functions is $\omega_S(g)$.
5. For each smooth family $\gamma : \mathbb{R}^k \to G$ and each Schwartz $f$, the map $t \mapsto \omega(\gamma(t)) f$ is smooth.
6. For each $X \in \mathfrak{sp}_{2l}(\mathbb{R})$ there is a continuous one-parameter subgroup $\gamma$ of $G$ with $\mathrm{pr}(\gamma(t)) = \exp(tX)$ and $\frac{d}{dt}\big|_{t=0} \omega(\gamma(t)) f = Q(X) f$ for each Schwartz $f$.

Lean: `UpperTheory.LiteratureTheorems.real_metaplectic_representation_of_literature`.

This is the [[Weil representation|H3Q2703KKV]] of the metaplectic double cover $G = \mathrm{Mp}_{2l}(\mathbb{R})$ (Weil, Acta Math. 111, 1964; Folland, *Harmonic Analysis in Phase Space*, Chapter 4). Property 3 is the intertwining relation that, by the Stone-von Neumann theorem, defines $\omega(g)$ up to a scalar. Property 6 says that the infinitesimal action is given by the quadratic operators. See [the Schrödinger model](/learn/theta/#the-schrdinger-model).

*Proof.* We take the construction from the sources above. In the development it is [Theorem 2.1.4 of Volume 5](/entry/real-metaplectic-representation/). $\square$

**Remark 1.1.8 (Formalization).** All five theorems take the record of open statements as an argument and do not use it. Each proof is one term: `GlobalTheory.CompanionTheory.Hypotheses₂.harishChandra_analyticity_density`, `GlobalTheory.gkGlobalisation_holds`, `PositivityTheory.CWB.casselmanWallach`, `PositivityTheory.RgFd.B.formalDegreeCompactDual` and `PositivityTheory.Stage1.PM.realMetaplecticRepresentation` ([EveryCharacterOfLiteratureOfVWin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L321), lines 321, 383, 385, 411, 491). A representation of $U(J_\varepsilon)$ is a function on all of $M_n(\mathbb{C})$ with values in bounded operators, with the group laws asked only on the subset $U(J_\varepsilon)$. We did not unfold this subset, the compact $K_\varepsilon$, the predicates for unitary, irreducible, $K$-finite and smooth, the discrete series predicate `IsDS`, the measures in the formal degree statement, or the seminorm conditions of Casselman-Wallach. We read them through their names. Each statement is the conjunction of named parts: `HarishChandraAnalyticity` is `AdmissibleCoefficientsAnalytic ∧ LeviSubmoduleDense` ([AdmissibleCoefficientsAnalytic.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/AdmissibleCoefficientsAnalytic.lean#L26)) and `GKGlobalisation` is `AdmissibleClosure ∧ InfinitesimalEquivalence` ([IsAdmissibleSubOfFiniteDimensional.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/IsAdmissibleSubOfFiniteDimensional.lean#L161)). In density, the subspace $S$ is stable under the Lie algebra but is not asked to be stable under $K_M$. The formal degree statement quantifies over all normalisations `cd`, `sc` that satisfy the compatibility condition ([FormalDegreeCompactDualIff.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/FormalDegreeCompactDualIff.lean#L8)). In Casselman-Wallach, the map $T_0$ is defined on all of $H$, and uniqueness holds only on smooth vectors ([HasDRepIffHasDerivAt.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/HasDRepIffHasDerivAt.lean#L98)). The metaplectic statement is at [RealMetaplecticRepresentation.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/RealMetaplecticRepresentation.lean#L351).
