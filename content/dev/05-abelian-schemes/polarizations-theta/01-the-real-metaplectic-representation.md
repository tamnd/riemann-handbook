---
title: The real metaplectic representation
decls:
  - PositivityTheory.Stage1.PM.realMetaplecticRepresentation
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The real metaplectic representation

This section states the existence of the metaplectic double cover of the real symplectic group together with its Weil representation on $L^2(\mathbb{R}^l)$ and on the Schwartz space. The statement is one of the published results that the proof uses at the infinite places of the theta correspondence: it is the content of [the real metaplectic representation from the literature](/entry/real-metaplectic-representation-of-literature/), and through it it enters [EveryCharacter from the literature](/step/every-character-of-literature/). The background is in [the Weil representation](/learn/theta/#the-weil-representation) and in [topological groups and covering maps](/learn/analysis/#topological-groups-and-covering-maps).

**Definition 2.1.1 (Phase space and the symplectic group).** Let $l$ be a finite nonempty set. Write a vector of $V = \mathbb{R}^l \oplus \mathbb{R}^l$ as $w = (p, q)$ with $p, q \in \mathbb{R}^l$, and let
$$J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$$
in this decomposition. The *real symplectic group* $\mathrm{Sp}(l, \mathbb{R})$ is the group of real matrices $g$ indexed by $l \sqcup l$ with $g J g^{T} = J$. Its Lie algebra $\mathfrak{sp}(l, \mathbb{R})$ is the space of real matrices $X$ with $X^{T} J + J X = 0$. We give $\mathrm{Sp}(l, \mathbb{R})$ the topology of a subspace of the matrices.

**Definition 2.1.2 (Heisenberg operators).** For $w = (p, q) \in V$ and a function $f$ on $\mathbb{R}^l$ put
$$\rho(w) f(x) = e^{2\pi i \langle q, x \rangle + \pi i \langle p, q \rangle} f(x + p).$$
Each $\rho(w)$ is a unitary operator of $L^2(\mathbb{R}^l)$, and $\rho(w)\rho(w') = e^{\pi i \sigma(w, w')}\rho(w + w')$ with $\sigma(w, w') = \langle p, q' \rangle - \langle q, p' \rangle$, so $\rho$ is a projective representation of $V$ whose cocycle is given by the symplectic form. Let $\mathcal{S}(\mathbb{R}^l)$ be the Schwartz space. The infinitesimal operators
$$d\rho(w) f(x) = \partial_p f(x) + 2\pi i \langle q, x \rangle f(x)$$
are continuous on $\mathcal{S}(\mathbb{R}^l)$; here $\partial_p$ is the derivative in the direction $p$. For $X \in \mathfrak{sp}(l, \mathbb{R})$ let
$$Q(X) = \frac{1}{4\pi i} \sum_{a, b \in l \sqcup l} \frac{(XJ)_{ab}}{2}\bigl(d\rho(e_a) d\rho(e_b) + d\rho(e_b) d\rho(e_a)\bigr),$$
where $e_a$ is the standard basis of $V$. This is the operator of the Lie algebra of the metaplectic group: a symmetrized quadratic expression in the generators of the Heisenberg Lie algebra.

Lean: `GlobalTheory.RealWeil.rho`, `GlobalTheory.RealWeil.dRho`, `GlobalTheory.RealWeil.quad`.

**Example 2.1.3.** Write $X = \begin{pmatrix} A & B \\ C & D \end{pmatrix}$ in blocks, so $XJ = \begin{pmatrix} B & -A \\ D & -C \end{pmatrix}$. Then
$$\begin{aligned} Q(X) f(x) = {} & \frac{1}{4\pi i} \sum_{j,k} B_{jk}\, \partial_j \partial_k f(x) - \sum_{j,k} A_{jk}\, x_k\, \partial_j f(x) \\ & - \frac{\operatorname{tr} A}{2} f(x) - \pi i \sum_{j,k} C_{jk}\, x_j x_k\, f(x). \end{aligned}$$
For $A = B = D = 0$ and $C$ symmetric, $\exp(tX)$ sends $(p, q)$ to $(p, q + tCp)$, and $Q(X)$ is multiplication by $-\pi i\, x^{T} C x$. The operator $U_t$ of multiplication by $\phi_t(x) = e^{-\pi i t\, x^{T} C x}$ satisfies $U_t \rho(p, q) U_t^{-1} = \rho(p, q + tCp)$. Indeed $\phi_t(x)/\phi_t(x + p) = e^{2\pi i t \langle Cp, x\rangle + \pi i t\, p^{T} C p}$, and this is exactly the change of phase from $q$ to $q + tCp$. So $t \mapsto U_t$ is a one-parameter group with derivative $Q(X)$ that intertwines $\rho$ with its transport by $\exp(tX)$. The theorem below says that this works for every $X$, after one passes to a double cover.

**Theorem 2.1.4 (Real metaplectic representation).** Let $l$ be a finite nonempty set. There are a topological group $G$ and group homomorphisms
$$p : G \to \mathrm{Sp}(l, \mathbb{R}), \qquad \omega : G \to \mathrm{U}(L^2(\mathbb{R}^l)), \qquad \omega_{\mathcal{S}} : G \to \mathcal{L}(\mathcal{S}(\mathbb{R}^l))$$
into the symplectic group, the unitary group of $L^2(\mathbb{R}^l)$ and the group of continuous linear operators of the Schwartz space, with the following properties.

1. $p$ is a surjective covering map, and there is $\varepsilon \in G$ with $\varepsilon \neq 1$, $\ker p = \{1, \varepsilon\}$ and $\omega(\varepsilon) = -1$.
2. For each $f \in L^2(\mathbb{R}^l)$ the map $g \mapsto \omega(g) f$ is continuous.
3. $\omega(g)\, \rho(w) = \rho(p(g) w)\, \omega(g)$ for all $g \in G$ and $w \in V$.
4. $\omega(g) f = \omega_{\mathcal{S}}(g) f$ for each Schwartz function $f$.
5. If $\gamma : \mathbb{R}^k \to G$ is continuous and the entries of $p \circ \gamma$ are smooth, then $t \mapsto \omega(\gamma(t)) f$ is a smooth map into $L^2(\mathbb{R}^l)$ for each Schwartz function $f$.
6. For each $X \in \mathfrak{sp}(l, \mathbb{R})$ there is a continuous one-parameter subgroup $\gamma : \mathbb{R} \to G$ with $p(\gamma(t)) = \exp(tX)$ for all $t$ and
$$\frac{d}{dt}\Big|_{t = 0} \omega(\gamma(t)) f = Q(X) f$$
in $L^2(\mathbb{R}^l)$ for each Schwartz function $f$.

Lean: `PositivityTheory.Stage1.PM.realMetaplecticRepresentation`.

*Proof.* This is [the theorem on the real metaplectic representation](/entry/real-metaplectic-representation-holds/) of Volume 10, with no change. We recall the idea. By the Stone-von Neumann theorem ([the Stone-von Neumann theorem](/learn/theta/#the-stone-von-neumann-theorem)), for each $s \in \mathrm{Sp}(l, \mathbb{R})$ the representation $w \mapsto \rho(sw)$ is unitarily equivalent to $\rho$, and the intertwining unitary operator $U$ is unique up to a scalar of absolute value $1$. So the pairs $(s, U)$ form a central extension of $\mathrm{Sp}(l, \mathbb{R})$ by the circle. Each such $U$ preserves the Schwartz space. A normalization of the scalar, through a square root of $\det(A - iB)$ for $s = \begin{pmatrix} A & B \\ C & D\end{pmatrix}$, cuts the circle down to $\{\pm 1\}$ and gives the double cover $G$. Continuity and smoothness come from explicit formulas for $U$ on the generators of the example above and on the Fourier transform, and property 6 is the computation of the example for general $X$. $\square$

**Remark 2.1.5.** The classical statement is due to Weil: the metaplectic group $\mathrm{Mp}(l, \mathbb{R})$, the unique connected double cover of $\mathrm{Sp}(l, \mathbb{R})$ ([[metaplectic group|8B0JM2YDE2]]), has a faithful unitary representation $\omega$ on $L^2(\mathbb{R}^l)$ with $\omega(g)\rho(w)\omega(g)^{-1} = \rho(p(g)w)$ (A. Weil, Sur certains groupes d'opérateurs unitaires; G. B. Folland, *Harmonic Analysis in Phase Space*, Chapter 4). The statement above is that result in the coordinates of this section. It does not say that $G$ is connected, and it does not name $G$ as $\mathrm{Mp}(l, \mathbb{R})$: it only asks for a double covering with $\omega(\varepsilon) = -1$, which rules out a split cover on which $\omega$ factors through $\mathrm{Sp}(l, \mathbb{R})$. In exchange it adds the action on Schwartz space, the smoothness in families and the formula for the derivative, which the proof uses at the archimedean places.

**Remark 2.1.6 (Formalization).** The theorem is a pure second name: [RealMetaplecticRepresentation.lean](lean:Development/WeilBound/CoreStatements/StandardPublishedResults/StandardTheoremStatements/RealMetaplecticRepresentation.lean#L5) proves it by the term `PositivityTheory.ThKR.realMetaplecticRepresentation_holds`. The statement `GlobalTheory.Published.RealMetaplecticRepresentation` is in [RealMetaplecticRepresentation.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/RealMetaplecticRepresentation.lean#L351), with $\rho$ (`rho`), $d\rho$ (`dRho`, line 121) and $Q$ (`quad`, line 191). The block formula of the example is `quad_fromBlocks` (line 282). The sketch of the proof above is a summary of the proof in Volume 10; the group there is built in `realMetaplectic_of_forall` from triples $(s, U, U_{\mathcal{S}})$.
