---
title: A Künneth formula for the multiplicative group
decls:
  - UpperTheory.injectiveComplex_productSection_map_quasiIso
  - UpperTheory.bijective_cohomology_gm_product_kummer_cup
  - UpperTheory.Kun.main
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A Künneth formula for the multiplicative group

The next two sections prove the projective bundle formula in étale cohomology for the projective line and then for all projective spaces. The projective line is covered by two affine lines, and the two lines meet in the multiplicative group $\mathbb{G}_m$. So the first input is a formula for the cohomology of $\mathbb{G}_m \times E$: it is the cohomology of $E$ plus a copy of the cohomology of $E$ shifted by one, multiplied by the Kummer class of the coordinate. This section proves that formula. It first proves a general comparison theorem for complexes of injective sheaves, and then applies it to $\mathbb{G}_m$. The induction on the rank in [Theorem 3.5.3](/entry/pbf-all/) uses both.

### Spaces and their cohomology

The proof works with simplicial objects, not only with schemes, so that the cover of a scheme by two open sets and its fibre products can be handled in one formalism.

**Definition 5.2.1 (Space).** A *space* is a simplicial presheaf of sets on the category of schemes. So a space $E$ gives, for each $p \ge 0$ and each scheme $T$, a set $E_p(T)$ of $p$-simplices of $E$ over $T$, with face and degeneracy maps, all natural in $T$. A scheme $X$ gives the space $hX$ with $(hX)_p(T) = \operatorname{Hom}(T, X)$ for all $p$. We write $X$ for $hX$.

Let $R$ be a commutative ring. A *sheaf* in this chapter is a sheaf of $R$-modules on the big étale site of schemes. For a space $E$, let $R[E]$ be the complex of sheaves whose term in degree $-p$ is the sheaf of free $R$-modules on $E_p$, with the alternating sum of the faces as differential.

**Definition 5.2.2 (Cohomology of a space).** Let $I$ be a complex of sheaves. The group $H^n(E, I)$ is the degree $n$ cohomology of the complex $\operatorname{Hom}^\bullet(R[E], I)$. For a sheaf $F$, put $H^n(E, F) = H^n(E, I)$, where $I$ is a fixed injective resolution of $F$.

For a scheme $X$ this is the [étale cohomology](/learn/geometry/#tale-cohomology) of $X$ ([[étale cohomology|7YX76G0838]]) for the big étale site. A map of spaces $f : E' \to E$ gives a pullback $f^* : H^n(E, F) \to H^n(E', F)$.

Fix an integer $q \ge 1$. We write $\mathbb{Z}/q(i)$ for the twisted sheaf of $\mathbb{Z}/q$-modules that the Lean code builds from the primitive $q$-th roots of unity ([roots of unity](/learn/algebra/#roots-of-unity)), and $H^n(E, \mathbb{Z}/q(i))$ for its cohomology. There is a cup product $H^n(E, \mathbb{Z}/q(i)) \times H^m(E, \mathbb{Z}/q(j)) \to H^{n+m}(E, \mathbb{Z}/q(i+j))$.

**Definition 5.2.3.** The integer $q$ is *invertible on $E$* if $q$ is a unit in $\Gamma(T, \mathcal{O}_T)$ for each scheme $T$ with $E_0(T) \neq \emptyset$.

**Definition 5.2.4 (Kummer class).** Let $\mathbb{G}_m = \operatorname{Spec} \mathbb{Z}[1/q][t, t^{-1}]$. The *Kummer class* $\kappa \in H^1(\mathbb{G}_m, \mathbb{Z}/q(1))$ is the class of the torsor of $q$-th roots of the unit $t$.

For a map $f : E' \to E$ we say that $f$ is a *cohomological equivalence* for a sheaf $F$ if $f^*$ is bijective on $H^n(-, F)$ for all $n$.

### A comparison theorem

Let $W$ be a scheme. A property holds *locally on* a scheme $T$ if there is a covering sieve of $T$ in the étale topology such that it holds for each morphism $V \to T$ of the sieve.

**Theorem 5.2.5 (Comparison of injective complexes).** Let $R$ be a commutative ring, $W$ a scheme, and $L$, $I$ complexes of injective sheaves of $R$-modules that vanish in negative degrees. Let maps of groups
$$\psi_T : L^s(T) \to I^s(W \times T)$$
be given for all schemes $T$ and all $s$, natural in $T$ and compatible with the differentials. Let $\mathcal{Z}$ be a class of schemes such that $T \in \mathcal{Z}$ and $T' \to T$ imply $T' \in \mathcal{Z}$. Assume for each $T \in \mathcal{Z}$ and each $n$:

1. (local surjectivity) for each cocycle $b \in I^n(W \times T)$, locally on $T$ there are a cocycle $a \in L^n(V)$ and $c \in I^{n-1}(W \times V)$ with $\psi_V(a) = b|_{W \times V} + dc$;
2. (local injectivity) if $a \in L^n(T)$ is a cocycle and $\psi_T(a)$ is a coboundary, then $a$ is a coboundary locally on $T$.

Let $E$ be a space such that $T \in \mathcal{Z}$ whenever $E_0(T) \neq \emptyset$. Then for each $n$ there is a bijective homomorphism
$$\Phi_n : H^n(E, L) \to H^n(W \times E, I).$$
On cocycles it is given by $\psi$: if $\alpha$ is a cocycle, then $\Phi_n[\alpha]$ is the class of a cocycle $\beta$ whose value at a $p$-simplex $y = (w, e)$ of $W \times E$ over $T$ is $(w, 1)^* \psi_T(\alpha(e))$, where $(w, 1) : T \to W \times T$.

Lean: `UpperTheory.injectiveComplex_productSection_map_quasiIso`.

*Proof.* Let $B$ be the complex of sheaves $T \mapsto I(W \times T)$, the pushforward of $I$ along the products with $W$. Each $B^s$ is injective, since pushforward along a product has an exact left adjoint. The maps $\psi_T$ form a morphism of complexes $\rho : L \to B$. Let $C$ be its mapping cone. It is a complex of injective sheaves that vanishes below degree $-1$.

Hypotheses 1 and 2 say that $\rho$ induces isomorphisms on cohomology sheaves, at least over the schemes of $\mathcal{Z}$. So the cone $C$ is exact locally on each scheme $T$ that carries a $0$-simplex of $E$. A bounded below complex of injectives that is exact in this local sense has zero cohomology on $E$: we get $H^m(E, C) = 0$ for all $m$. The long exact sequence of the cone in the second variable,
$$\cdots \to H^{m-1}(E, C) \to H^m(E, L) \xrightarrow{\rho_*} H^m(E, B) \to H^m(E, C) \to \cdots,$$
then shows that $\rho_*$ is bijective. Last, the adjunction between products with $W$ and pushforward identifies $H^n(E, B)$ with $H^n(W \times E, I)$. On cocycles the identification sends a cocycle $\gamma$ to the cocycle $y = (w, e) \mapsto (w, 1)^* \gamma(e)$. Composing gives $\Phi_n$ and its formula on cocycles. $\square$

### The Künneth formula

The local input for $\mathbb{G}_m$ is a statement about schemes.

**Lemma 5.2.6 (Local Künneth for $\mathbb{G}_m$).** Let $T$ be a scheme on which $q$ is a unit, and let $m, j \in \mathbb{Z}$. Write $\mathrm{pr}_1, \mathrm{pr}_2$ for the projections of $\mathbb{G}_m \times T$.

1. Each class $y \in H^{m+1}(\mathbb{G}_m \times T, \mathbb{Z}/q(j+1))$ is, locally on $T$, of the form $\mathrm{pr}_2^* a + \mathrm{pr}_2^* b \cup \mathrm{pr}_1^* \kappa$ with $a \in H^{m+1}(V, \mathbb{Z}/q(j+1))$ and $b \in H^m(V, \mathbb{Z}/q(j))$.
2. If $\mathrm{pr}_2^* a + \mathrm{pr}_2^* b \cup \mathrm{pr}_1^* \kappa = 0$ on $\mathbb{G}_m \times T$, then $a$ and $b$ vanish locally on $T$.

Lean: `UpperTheory.locally_surjective_multiplicativeGroupKunnethMap`.

We did not open the proof of this Lemma. Its statement is local on $T$, so only the strict henselizations of $T$ matter; over such a base it is the computation of the cohomology of $\mathbb{G}_m$ by the Kummer sequence.

**Theorem 5.2.7 (Künneth formula for $\mathbb{G}_m$).** Let $E$ be a space on which $q$ is invertible. For all $n, i \in \mathbb{Z}$ the map
$$\begin{aligned} H^n(E, \mathbb{Z}/q(i)) \oplus H^{n-1}(E, \mathbb{Z}/q(i-1)) &\to H^n(\mathbb{G}_m \times E, \mathbb{Z}/q(i)), \\ (a, b) &\mapsto \mathrm{pr}_2^* a + \mathrm{pr}_2^* b \cup \mathrm{pr}_1^* \kappa \end{aligned}$$
is bijective.

Lean: `UpperTheory.bijective_cohomology_gm_product_kummer_cup` (also `UpperTheory.Kun.main`, the same statement with $n = m + 1$ and $i = j + 1$).

*Proof.* Write $n = m + 1$ and $i = j + 1$. Let $I$, $Q$ and $P$ be the chosen injective resolutions of $\mathbb{Z}/q(j+1)$, $\mathbb{Z}/q(j)$ and $\mathbb{Z}/q(1)$, and let $\mu : Q \otimes P \to I$ be the pairing that gives the cup product. Choose a cocycle $k \in P^1(\mathbb{G}_m)$ that represents $\kappa$. Let $L$ be the complex with $L^s = I^s \oplus Q^{s-1}$ and the differential of a direct sum, up to the sign on the second factor. Define
$$\psi_T(a_1, a_2) = \mathrm{pr}_2^* a_1 \pm \mu(\mathrm{pr}_2^* a_2, \mathrm{pr}_1^* k) \in I^s(\mathbb{G}_m \times T),$$
with the sign $(-1)^s$ that makes $\psi$ commute with the differentials. Let $\mathcal{Z}$ be the class of schemes on which $q$ is a unit; it is closed under maps into its members. On cohomology, $\psi$ is the map $(a, b) \mapsto \mathrm{pr}_2^* a + \mathrm{pr}_2^* b \cup \mathrm{pr}_1^* \kappa$. So the two parts of the Lemma are hypotheses 1 and 2 of [Theorem 5.2.5](/entry/injective-complex-product-section-map-quasi-iso/) (comparison of injective complexes), with $W = \mathbb{G}_m$. Since $q$ is invertible on $E$, the comparison theorem applies to $E$. It gives a bijection $H^n(E, L) \to H^n(\mathbb{G}_m \times E, I)$ that is given by $\psi$ on cocycles. Finally $H^n(E, L) = H^n(E, \mathbb{Z}/q(j+1)) \oplus H^{n-1}(E, \mathbb{Z}/q(j))$, and the bijection becomes the map of the theorem. $\square$

Over a field, the theorem is the familiar computation $H^*(\mathbb{G}_m) = H^*(\mathrm{pt}) \oplus H^{*-1}(\mathrm{pt}) \cdot \kappa$, the étale analogue of the cohomology of the punctured plane $\mathbb{C}^\times$, which has the homotopy type of a circle.

**Remark 5.2.8.** In the Lean code the general form of the proof is a private theorem in the namespace of the Künneth formula. It takes the scheme $W$, the complexes $I$, $Q$, $P$, the pairing, the cocycle and the class $\mathcal{Z}$ as data, and applies the comparison theorem to $W$ and the complex `LL I Q`. The theorem `UpperTheory.Kun.main` is private too. It is the case $W = \mathbb{G}_m$, in the indices $(m + 1, j + 1)$, and the public theorem only changes the indices to $(n, i)$. [Lemma 5.3.4](/entry/kun/) in the next section changes them back.
