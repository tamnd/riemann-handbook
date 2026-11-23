---
title: Unfolding the theta integral over a vector of length one
decls:
  - GlobalTheory.UnfoldingObj.unfolding
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Unfolding the theta integral over a vector of length one

Let $W$ be a [[Hermitian form|8NJ7XY6F1S]] space over a CM field and $W'$ the orthogonal complement of a vector $x$ of length $\pm 1$. This section proves the unfolding identity that relates the integral of a theta series of $W$ over $U(W)(F)\backslash U(W)(\mathbb{A})$ to the volume of $U(W')(F)\backslash U(W')(\mathbb{A})$. The sum runs over all vectors of length $h(x, x)$, and the test function is the characteristic function of the self-dual lattice at the finite places times an arbitrary function at the infinite places. Then the integral is $\mathrm{vol}(W')$ times an archimedean orbit integral. The finite places contribute nothing, because the stabilizer of the lattice acts transitively on the lattice vectors of length $\pm 1$. The identity is used in Section 9, in the proof of [the volume ratio](/entry/volume-ratio/), together with [the measures at the real places](/entry/real-place-measures/) of Section 7. For background see [the mass formula for unitary groups](/learn/hermitian-lattices/#the-mass-formula-for-unitary-groups).

### The setting

Let $F$ be a totally real field of degree $f$, and $E/F$ a CM extension that is unramified at all finite places, with complex conjugation $z \mapsto \bar{z}$. Fix a CM type $\Psi$, that is, a set of $f$ embeddings $\tau : E \to \mathbb{C}$, one above each real place of $F$. Let $\mathbb{A}$ be the adeles of $F$, $\mathbb{A}_f$ the finite adeles and $F_\infty = F \otimes \mathbb{R}$.

A *hermitian space* $W$ is a finite-dimensional $E$-vector space with a nondegenerate hermitian form $h$, a basis, and a self-dual $\mathcal{O}_E$-lattice $L_0$. Its rank is $M$, and it has signature $(P, Q)$ at $\tau$ if the matrix of $h$ under $\tau$ has $P$ positive and $Q$ negative eigenvalues. Let $G = U(W)$ and $\widehat{L}_0 = L_0 \otimes \widehat{\mathcal{O}}$. For each $\tau \in \Psi$ choose a matrix $A_\tau$ with $A_\tau^* J_{P,Q} A_\tau = \tau(\mathrm{Gram})$, where $J_{P,Q} = \mathrm{diag}(1_P, -1_Q)$. Then $A_\tau$ identifies $G(F_\infty)$ with $\prod_{\tau \in \Psi} U(P, Q)$, and the vector $x \in W$ with the point $x_\infty = (A_\tau\tau(x))_\tau$.

We fix a compact dual normalization $(\mu_{P,Q})$ of Haar measures on the groups $U(P, Q)$, as in Section 7.

**Definition 2.8.1 (Normalized Haar measure).** A Haar measure $\mu$ on $G(\mathbb{A})$ is *normalized* if for every choice of the matrices $A_\tau$ and all measurable sets $B_\tau \subseteq U(P, Q)$,
$$\mu\bigl(\{h : h_f\widehat{L}_0 = \widehat{L}_0,\ h_\infty \in \textstyle\prod_\tau B_\tau\}\bigr) = \prod_{\tau \in \Psi} \mu_{P,Q}(B_\tau).$$

So the stabilizer $K$ of $\widehat{L}_0$ in $G(\mathbb{A}_f)$ has measure $1$, and the archimedean factor is the compact dual measure.

**Definition 2.8.2 (Quotient measure).** Let $j : G' \to G$ be an injective homomorphism of groups, and $m$, $m'$ measures on $G$ and $G'$. A measure $\nu$ on the space of right cosets $j(G')\backslash G$ is a *quotient measure* for $m$ and $m'$ if for every measurable $f \geq 0$ on $G$,
$$\int_G f\, dm = \int_{j(G')\backslash G} \int_{G'} f\bigl(j(g')\tilde{c}\bigr)\, dm'(g')\, d\nu(c),$$
where $\tilde{c}$ is a fixed representative of the coset $c$.

**Definition 2.8.3 (Archimedean orbit integral).** Let $x \in W$ with $h(x, x) = \beta \neq 0$, and let $(P', Q')$ be the signature of $x^\perp$. Let $\Phi_\infty \geq 0$ be a measurable function on $W \otimes F_\infty$. A number $I$ is *the archimedean orbit integral of $\Phi_\infty$ at $x$* if for all choices of the following data, and for at least one choice:

1. matrices $A_\tau$ as above;
2. matrices $C_\tau$ with $C_\tau^* J_{P,Q} C_\tau = J_{P',Q'}$ and $C_\tau^* J_{P,Q}\, x_\tau = 0$, where $x_\tau = A_\tau\tau(x)$;
3. a homomorphism $j : \prod_\tau U(P', Q') \to \prod_\tau U(P, Q)$ with $j(b)_\tau C_\tau = C_\tau b_\tau$ and $j(b)_\tau x_\tau = x_\tau$;
4. a map $o$ from $\prod_\tau U(P, Q)$ to $W \otimes F_\infty$ with $A_\tau\tau(o(g)) = g_\tau^{-1}x_\tau$ for all $\tau$;
5. a quotient measure $\nu$ on $j(\prod U(P', Q'))\backslash\prod U(P, Q)$ for $\prod_\tau \mu_{P,Q}$ and $\prod_\tau \mu_{P',Q'}$;

we have $\int \Phi_\infty(o(\tilde{c}))\, d\nu(c) = I$.

### The inputs

**Theorem 2.8.4 (Witt's theorem over $E$).** Let $x \in W$ with $h(x, x) \neq 0$. Then $G(F)$ acts transitively on $\{x' \in W : h(x', x') = h(x, x)\}$.

Lean: `GlobalTheory.T.rational_vectors_same_length_one_unitary_orbit`.

**Theorem 2.8.5 (Lattice orbits at the finite places).** Let $E/F$ be unramified at all finite places, let $L$ be a self-dual lattice, $\beta = \pm 1$ and $x \in L$ with $h(x, x) = \beta$. Let $K$ be the stabilizer of $\widehat{L}$ in $G(\mathbb{A}_f)$ and $H$ the stabilizer of $x$. Then:

1. $K$ acts transitively on $\{y \in \widehat{L} : h(y, y) = \beta\}$;
2. $\{g \in G(\mathbb{A}_f) : g^{-1}x \in \widehat{L}\} = H(\mathbb{A}_f)K$;
3. $K \cap H(\mathbb{A}_f)$ is the stabilizer of $\widehat{L} \cap x^\perp$ in $H(\mathbb{A}_f)$.

Lean: `GlobalTheory.T.stabSelfDualLattice_transitive_on_length`.

Item 1 is a local statement at each finite place. Since $h(x, x)$ is a unit and $L_v$ is self-dual, $L_v = \mathcal{O}_{E,v}x \oplus (L_v \cap x^\perp)$, and the complement is again self-dual. Then Witt's theorem for unimodular lattices over the unramified extension gives the transitivity. Items 2 and 3 follow from item 1.

### The theorem

**Theorem 2.8.6 (Unfolding).** Let $W$ be a hermitian space of rank $M \geq 3$, with signature $(P, Q)$ at every $\tau \in \Psi$. Let $\beta = 1$ and $P \geq 1$, or $\beta = -1$ and $Q \geq 1$. Let $x \in L_0$ with $h(x, x) = \beta$. Let $W'$ be a hermitian space and $\iota : W' \to W$ an isometric embedding with image $x^\perp$ and lattice $L_0' = \iota^{-1}(L_0)$, with signature $(P', Q') = (P - 1, Q)$ if $\beta = 1$ and $(P, Q - 1)$ if $\beta = -1$. Let $\mu$ and $\mu'$ be normalized Haar measures on $G(\mathbb{A})$ and $G'(\mathbb{A})$, where $G' = U(W')$, and let $\mathcal{F}$ and $\mathcal{F}'$ be fundamental domains for $G(F)$ and $G'(F)$ of finite measure. Let $\Phi_\infty \geq 0$ be measurable. Then there is $I$, the archimedean orbit integral of $\Phi_\infty$ at $x$, such that
$$\int_{\mathcal{F}} \sum_{\substack{x' \in W \\ h(x', x') = \beta}} \mathbf{1}_{\widehat{L}_0}(h_f^{-1}x')\,\Phi_\infty(h_\infty^{-1}x')\, d\mu(h) = \mu'(\mathcal{F}') \cdot I.$$

Lean: `GlobalTheory.UnfoldingObj.unfolding`.

*Proof.* Let $H \subseteq G$ be the stabilizer of $x$. An element $g' \in G'$ extends to an element of $G$ that is $\iota g'\iota^{-1}$ on $x^\perp$ and the identity on $Ex$. This gives an isomorphism $\varphi : G' \to H$, over $F$ and over every completion. Put $\phi(y) = \mathbf{1}_{\widehat{L}_0}(y_f)\Phi_\infty(y_\infty)$.

Step 1 (the orbit). By Witt's theorem over $E$, the map $\gamma \mapsto \gamma x$ is a bijection from $G(F)/H(F)$ onto the set of $x' \in W$ with $h(x', x') = \beta$. So the integrand is
$$\sum_{\gamma \in G(F)/H(F)} \phi(h^{-1}\gamma x).$$

Step 2 (unfolding). The function $h \mapsto \phi(h^{-1}x)$ is invariant under left multiplication by $H(\mathbb{A})$. We integrate over $\mathcal{F}$, which is a fundamental domain for $G(F)$. The sum over $G(F)/H(F)$ and the integral over $G(F)\backslash G(\mathbb{A})$ combine to an integral over $H(F)\backslash G(\mathbb{A})$. Then we integrate first over $H(F)\backslash H(\mathbb{A})$, with the measure $\varphi_*\mu'$, and the result is $\mu'(\mathcal{F}')$ times an integral over $H(\mathbb{A})\backslash G(\mathbb{A})$ for a quotient measure. All terms are nonnegative, so the exchange of sum and integral is justified.

Step 3 (the finite places). The quotient $H(\mathbb{A})\backslash G(\mathbb{A})$ is the product of the finite part $H(\mathbb{A}_f)\backslash G(\mathbb{A}_f)$ and the archimedean part. By item 2 of the theorem on lattice orbits, $\mathbf{1}_{\widehat{L}_0}(g_f^{-1}x) = 1$ exactly on the image of $K$ in $H(\mathbb{A}_f)\backslash G(\mathbb{A}_f)$. By item 3, $K \cap H(\mathbb{A}_f) = \varphi(K')$, where $K'$ is the stabilizer of $\widehat{L}_0'$. So the finite part of the integral is the ratio of the measure of $K$ to the measure of $K'$. Both are $1$, because $\mu$ and $\mu'$ are normalized.

Step 4 (the infinite places). The matrices $A_\tau$ exist because $W$ has signature $(P, Q)$ at $\tau$. Since $x_\tau$ has length $\beta$, its orthogonal complement in $\mathbb{C}^{P+Q}$ has signature $(P', Q')$. A basis of it adapted to the signs gives $C_\tau$, and $j$ is the corresponding embedding, as in Section 7. The map $o$ exists because $g \mapsto g^{-1}x_\infty$ takes values in the image of $W \otimes F_\infty$. A quotient measure $\nu$ exists because $j$ is a closed embedding of unimodular groups: one constructs it from a Bruhat function. For every such choice, the normalization of $\mu$ and $\mu'$ at the infinite places says that the archimedean part of the quotient measure of Step 2 is $\nu$. So the archimedean part of the integral is $\int\Phi_\infty(o(\tilde{c}))\, d\nu(c)$, and this does not depend on the choice. $\square$

The identity is a form of the Siegel-Weil unfolding for the orbit of one vector. The hypothesis that $E/F$ is unramified at all finite places enters only through the theorem on lattice orbits. At a ramified place, the stabilizer of a self-dual lattice need not act transitively on the lattice vectors of length $\pm 1$, and the finite factor would be a local density instead of $1$; see [local densities](/learn/hermitian-lattices/#local-densities).

**Remark 2.8.7 (Formalization).** The theorem is obtained through the equivalence `GlobalTheory.UnfoldingCompare.unfolding_iff` ([FundamentalDomainNeZero.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/FundamentalDomainNeZero.lean#L312)) from a second formal version, `GlobalTheory.T.unitaryUnfolding_volume_vectorStabilizer`, whose statement uses the parallel definitions of [InfiniteCoordinateUnfold.lean](lean:Development/AbelianVarietyTheory/BlockTheory/GlobalSignature/InfiniteCoordinateUnfold.lean#L79). That version takes three hypotheses: `QuotientMeasures` (seven clauses on invariant measures on quotients), `AdelicUnitaryHaar` (unimodularity and fundamental domains for the adelic unitary groups) and `StabTransitive` (the theorem on lattice orbits). They are supplied by `GlobalTheory.T.quotientMeasure_integration_formulas_unimodular`, `GlobalTheory.T.adelicUnitaryGroupHaarProperties_proof` and `GlobalTheory.T.stabSelfDualLattice_transitive_on_length`. The proof `GlobalTheory.VolumeUnfolding.unfolding` discards the first two hypotheses and uses only `StabTransitive` ([UnitaryUnfoldingVolumeVectorStabilizer.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/UnitaryUnfoldingVolumeVectorStabilizer.lean#L271)). The unramified hypothesis is derived from the data of the setting, in `GlobalTheory.VolumeUnfolding.unramified_host`. The orbit sum is unfolded by `GlobalTheory.T.lintegral_tsum_orbit_unfold_alt`, and the measures are compared with the compact dual by `GlobalTheory.T.map_restrict_latticeStabiliser_measure_eq_compactDual`. The archimedean orbit integral is stated as a chain of `AllSome` conditions, which ask that a choice exists and that the value is the same for all choices.
