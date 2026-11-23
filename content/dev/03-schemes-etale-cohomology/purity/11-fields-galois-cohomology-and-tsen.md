---
title: Fields, Galois cohomology and Tsen's theorem
decls:
  - GlobalTheory.T.etaleCohomology_field_eq_galoisCohomology
  - GlobalTheory.EtC.FieldTw.field_tw_coh_eq_galois
  - GlobalTheory.T.nonempty_cohomology_addEquiv_galois_cohomology
  - GlobalTheory.EtC.GalFld.cohomology_field_addEquiv_galois
  - GlobalTheory.T.etale_cohomology_vanishing_algebraic_over_ratFunc
  - GlobalTheory.EtC.gaugeSplitting_holds
  - GlobalTheory.T.cdp_galois_le_one_of_isAlgebraic_ratFunc
  - GlobalTheory.TsenCD.cdp_galois_le_one_of_algebraic_ratFunc
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Fields, Galois cohomology and Tsen's theorem

This section proves two results on the cohomology of a field $K$. The first says that the cohomology of $\mathrm{sp}(K)$ with coefficients in a sheaf $F$ is the Galois cohomology of the module of sections of $F$ over a separable closure. The second says that if $K$ is algebraic over $k(t)$ with $k$ algebraically closed, then $H^n(K, \mathbb{Z}/q(i)) = 0$ for $n \geq 2$. Both are inputs of [the local steps](/entry/steps-holds/) of the chapter on Galois representations. The second result follows from the first and from Tsen's theorem.

We keep the notation of the earlier sections. For a ring $A$ we write $H^n(A, F)$ for the cohomology of $\mathrm{sp}(A)$. Throughout, $K$ is a field, $\Omega$ is a separable closure of $K$, and $G = \operatorname{Aut}_K(\Omega)$ with the Krull topology, a profinite group.

### Galois cohomology

**Definition 2.11.1 (Discrete module and its cohomology).** Let $R$ be a commutative ring. A *discrete $G$-module over $R$* is an $R$-module $M$ with a linear action of $G$ such that the stabilizer of each $m \in M$ is open. For $m \geq 0$ let $C^m(G, M)$ be the group of locally constant maps $\varphi : G^{m+1} \to M$ such that $\varphi(\tau\sigma_0, \ldots, \tau\sigma_m) = \tau \varphi(\sigma_0, \ldots, \sigma_m)$ for all $\tau \in G$. The differential $d : C^m \to C^{m+1}$ is $(d\varphi)(\sigma_0, \ldots, \sigma_{m+1}) = \sum_j (-1)^j \varphi(\sigma_0, \ldots, \widehat{\sigma_j}, \ldots, \sigma_{m+1})$. The *Galois cohomology* $H^n(G, M)$ is the cohomology of this complex.

This complex computes the cohomology of the continuous cochains of J.-P. Serre, *Galois Cohomology*, Chapter I, §2.2. A map $G^{m+1} \to M$ is locally constant if and only if it is continuous for the discrete topology on $M$.

**Definition 2.11.2 (Cohomological dimension at a prime).** Let $p$ be a prime. The *$p$-cohomological dimension* $\mathrm{cd}_p(G) \in \{0, 1, 2, \ldots, \infty\}$ is the least $n$ such that for every discrete torsion $G$-module $A$ over $\mathbb{Z}$ and every $m > n$, the $p$-primary component of $H^m(G, A)$ is zero.

This is the definition of Serre, *Galois Cohomology*, Chapter I, §3.1.

### Inputs

We use the following results and take them as given.

**Lemma 2.11.3 (The Čech nerve of a separable closure).** Let $R$ be a commutative ring and let $F$ be a sheaf of $R$-modules whose functor of sections on rings commutes with filtered colimits. Let $f : \operatorname{Spec} \Omega \to \operatorname{Spec} K$ and let $\check{C}(f)$ be its Čech nerve, with $\check{C}(f)_m = \operatorname{Spec}(\Omega \otimes_K \cdots \otimes_K \Omega)$, with $m + 1$ factors. For $\sigma = (\sigma_0, \ldots, \sigma_m) \in G^{m+1}$ let $P_\sigma$ be the $\Omega$-point of $\check{C}(f)_m$ given by $x_0 \otimes \cdots \otimes x_m \mapsto \sigma_0(x_0) \cdots \sigma_m(x_m)$.

1. The augmentation $\check{C}(f) \to \mathrm{sp}(K)$ induces a bijection $H^n(K, F) \to H^n(\check{C}(f), F)$ for every $n$.
2. $H^s(\check{C}(f)_m, F) = 0$ for all $m \geq 0$ and $s > 0$.
3. Let $e : M \to F(\Omega)$ be an additive bijection with $e(\sigma m) = (\operatorname{Spec} \sigma)^* e(m)$. The map that sends $c \in F(\check{C}(f)_m)$ to the function $\sigma \mapsto e^{-1}(c(P_\sigma))$ is injective, and its image is $C^m(G, M)$.

Lean: `GlobalTheory.T.etaleCechAugmentation_sepClosure_isEquivalence`, `GlobalTheory.T.cohomology_cech_level_eq_zero_of_pos` and `GlobalTheory.T.galoisDescent_freeSheaf_cechLevel_sepClosure`.

The reason is that for a finite Galois extension $L/K$ the ring $\Omega \otimes_K L$ is a product of copies of $\Omega$ indexed by $\operatorname{Gal}(L/K)$, and $\Omega \otimes_K \Omega$ is the filtered colimit of these rings. So $F$ on the levels of $\check{C}(f)$ is described by locally constant functions on powers of $G$, and the levels are acyclic because $\Omega$ is separably closed. This is the description of étale sheaves on $\operatorname{Spec} K$ as discrete $G$-modules in SGA 4, Exposé VIII, §2.

**Lemma 2.11.4 (Acyclic levels).** Let $E$ be a space and $F$ a sheaf of $R$-modules with $H^s(E_m, F) = 0$ for all $m \geq 0$ and $s > 0$. Then $H^n(E, F)$ is isomorphic to the $n$-th cohomology of the complex $F(E_0) \to F(E_1) \to \cdots$ whose differential is the alternating sum of the pullbacks along the faces.

Lean: `GlobalTheory.EtC.GalFld.bridge`.

This is the degenerate case of the spectral sequence $E_1^{p,s} = H^s(E_p, F) \Rightarrow H^{p+s}(E, F)$.

**Lemma 2.11.5 (Homogeneous cochains).** Let $C^\bullet$ be a cosimplicial abelian group, $M$ a discrete $G$-module over $R$, and $e_m : C^m \to \operatorname{Map}(G^{m+1}, M)$ injective homomorphisms with image $C^m(G, M)$, such that $e_{m+1}(\delta_j c)(\sigma) = e_m(c)(\sigma_0, \ldots, \widehat{\sigma_j}, \ldots, \sigma_{m+1})$. Then the $n$-th cohomology of the alternating complex of $C^\bullet$ is isomorphic to $H^n(G, M)$ for every $n$.

Lean: `GlobalTheory.T.homogeneousCochains_homology_addEquiv_alt`.

The maps $e_m$ identify the alternating complex of $C^\bullet$ with the complex of the definition.

### Étale and Galois cohomology

**Theorem 2.11.6 (Cohomology of a field).** Let $R$ be a commutative ring and let $F$ be a sheaf of $R$-modules whose functor of sections on rings commutes with filtered colimits. Let $M$ be a discrete $G$-module over $R$ and let $e : M \to F(\Omega)$ be an additive bijection such that $e(\sigma m) = (\operatorname{Spec} \sigma)^* e(m)$ for all $\sigma \in G$ and $m \in M$. Then $H^n(K, F) \cong H^n(G, M)$ as groups, for every $n \geq 0$.

Lean: `GlobalTheory.T.nonempty_cohomology_addEquiv_galois_cohomology` (also `GlobalTheory.EtC.GalFld.cohomology_field_addEquiv_galois`).

*Proof.* By part 1 of the lemma on the Čech nerve, $H^n(K, F) \cong H^n(\check{C}(f), F)$. By part 2 and the lemma on acyclic levels, $H^n(\check{C}(f), F)$ is the cohomology of the complex $m \mapsto F(\check{C}(f)_m)$. Part 3 gives injective maps $e_m$ from this complex into the maps $G^{m+1} \to M$, with image $C^m(G, M)$. The $j$-th face $\check{C}(f)_{m+1} \to \check{C}(f)_m$ forgets the $j$-th factor, so it sends $P_\sigma$ to $P_{\sigma'}$ with $\sigma' = (\sigma_0, \ldots, \widehat{\sigma_j}, \ldots, \sigma_{m+1})$. This is the face condition of the lemma on homogeneous cochains, which gives $H^n(\check{C}(f), F) \cong H^n(G, M)$. $\square$

**Lemma 2.11.7 (Tate twists over a field).** Let $q \geq 1$ and $i, j \in \mathbb{Z}$.

1. The functor of sections of $\mathbb{Z}/q(i)$ on rings commutes with filtered colimits.
2. If $\zeta \in \mathrm{Prim}_q(\Omega)$, then $c \mapsto c\,[\zeta]$ is a bijection $\mathbb{Z}/q \to \mathbb{Z}/q(i)(\Omega)$.
3. If $A$ is a ring in which $q$ is a unit and $\Phi_q$ has a root, then $H^n(A, \mathbb{Z}/q(i)) \cong H^n(A, \mathbb{Z}/q(j))$ for every $n$.

Lean: `GlobalTheory.T.tateTwist_finitary`, `GlobalTheory.T.freeRankOne_etaleSheaf_equiv_locallyConstant` and `GlobalTheory.T.tateTwistCohomology_spec_twist_independent`.

Part 2 holds because $\mathbb{Z}/q(i)$ is free of rank one with basis $[\zeta]$ over $\operatorname{Spec} \Omega$, and the locally constant functions on the one point of $\operatorname{Spec} \Omega$ are the constants. Part 3 holds because the choice of a root $\zeta$ makes $\mathbb{Z}/q(i)$ and $\mathbb{Z}/q(j)$ both isomorphic to the constant sheaf $\mathbb{Z}/q$ over $\operatorname{Spec} A$.

**Theorem 2.11.8 (Tate twists of a field and Galois cohomology).** Let $q \geq 1$ be a unit in $K$, let $i \geq 0$ be an integer, and let $\zeta \in \Omega$ be a primitive $q$-th root of unity. Let $M$ be a discrete $G$-module over $\mathbb{Z}/q$ that is free of rank one with basis $b$, such that $\sigma b = a^i b$ whenever $\sigma \in G$, $a \geq 0$ and $\sigma(\zeta) = \zeta^a$. Then $H^n(K, \mathbb{Z}/q(i)) \cong H^n(G, M)$ as groups, for every $n \geq 0$.

Lean: `GlobalTheory.T.etaleCohomology_field_eq_galoisCohomology` (also `GlobalTheory.EtC.FieldTw.field_tw_coh_eq_galois`).

*Proof.* Since $q$ is a unit in $\Omega$, the root $\zeta$ lies in $\mathrm{Prim}_q(\Omega)$. Let $e : M \to \mathbb{Z}/q(i)(\Omega)$ send $c\,b$ to $c\,[\zeta]$. By part 2 of the lemma on Tate twists, $e$ is bijective. Let $\sigma \in G$ and write $\sigma(\zeta) = \zeta^a$ with $a \geq 0$. The pullback along $\operatorname{Spec} \sigma$ sends $[\zeta]$ to $[\sigma(\zeta)] = [\zeta^a] = a^i [\zeta]$, by the relation in the definition of $\mathbb{Z}/q(i)$. So
$$
(\operatorname{Spec} \sigma)^* e(c\,b) = c\,a^i [\zeta] = e(c\,a^i b) = e(\sigma(c\,b)).
$$
By part 1 of the lemma on Tate twists, [Theorem 2.11.6](/entry/nonempty-cohomology-add-equiv-galois-cohomology/) applies to $F = \mathbb{Z}/q(i)$ and gives the claim. $\square$

### Tsen's theorem

Recall that a field $K$ is *$C_1$* if every homogeneous polynomial over $K$ of degree $d > 0$ in $n > d$ variables has a nonzero zero in $K^n$.

**Theorem 2.11.9 (Tsen).** Let $k$ be an algebraically closed field and $K$ an algebraic extension of $k(t)$. Then $K$ is $C_1$, and $\mathrm{cd}(G) \leq 1$.

This is J.-P. Serre, *Galois Cohomology*, Chapter II, §3.3, with §3.2 for the passage from $C_1$ to the bound on the dimension. We state the form that we use, and prove it from the following inputs, which we take as given.

**Lemma 2.11.10 (Inputs on Galois cohomology).**

1. Let $H$ be a profinite group, $\ell$ a prime, $n \geq 0$, and $A$ a discrete $H$-module over $\mathbb{Z}$ that is isomorphic to $\mathbb{Z}/\ell$ as a group. If $H^{n+1}(U, A) = 0$ for every open subgroup $U$ of $H$, then $\mathrm{cd}_\ell(H) \leq n$.
2. Every field algebraic over $k(t)$, with $k$ algebraically closed, is $C_1$.
3. If $E$ is a $C_1$ field and $L/E$ is a finite Galois extension, then $H^2(\operatorname{Gal}(L/E), L^\times) = 0$.

Lean: `GroundTheory.ProfCoh.cdp_le_of_forall_openSubgroup`, `GlobalTheory.tsen_algebraic_extension_ratFunc` and `GlobalTheory.c_one_h2_units_subsingleton`.

For part 1 see Serre, *Galois Cohomology*, Chapter I, §3 and §4: the bound for a pro-$\ell$ Sylow subgroup gives the bound for $H$. Parts 2 and 3 are in Chapter II, §3.2 and §3.3 of the same book.

**Theorem 2.11.11 (Dimension of the Galois group).** Let $k$ be an algebraically closed field and let $K$ be an algebraic extension of $k(t)$. Then $\mathrm{cd}_p(G) \leq 1$ for every prime $p$.

Lean: `GlobalTheory.T.cdp_galois_le_one_of_isAlgebraic_ratFunc` (also `GlobalTheory.TsenCD.cdp_galois_le_one_of_algebraic_ratFunc`).

*Proof.* Let $U$ be an open subgroup of $G$ and let $E = \Omega^U$ be its fixed field. Then $E$ is finite over $K$, so it is algebraic over $k(t)$, and $U = \operatorname{Gal}(\Omega/E)$. By part 1 of the inputs with $n = 1$, it is enough to find a discrete $G$-module $A \cong \mathbb{Z}/p$ with $H^2(U, A) = 0$ for every such $U$.

Case $p \neq 0$ in $K$. Let $A = \mu_p(\Omega)$, which is cyclic of order $p$. The Kummer sequence
$$
1 \to \mu_p \to \Omega^\times \xrightarrow{x \mapsto x^p} \Omega^\times \to 1
$$
is exact, because $X^p - c$ is separable for $c \neq 0$. Its long exact sequence contains $H^1(U, \Omega^\times) \to H^2(U, \mu_p) \to H^2(U, \Omega^\times)$. The left group is zero by Hilbert's Theorem 90. The right group is the union of the images of the inflation maps from $H^2(\operatorname{Gal}(L/E), L^\times)$, for $L/E$ finite Galois in $\Omega$. These groups are zero by parts 2 and 3 of the inputs. So $H^2(U, \mu_p) = 0$.

Case $p = 0$ in $K$. Let $A = \mathbb{Z}/p$ with the trivial action. The Artin-Schreier sequence
$$
0 \to \mathbb{Z}/p \to \Omega \xrightarrow{x \mapsto x^p - x} \Omega \to 0
$$
is exact, because $X^p - X - c$ is separable and $\Omega$ is separably closed. Its long exact sequence contains $H^1(U, \Omega) \to H^2(U, \mathbb{Z}/p) \to H^2(U, \Omega)$. The additive group $\Omega$ has $H^n(U, \Omega) = 0$ for $n \geq 1$, by the normal basis theorem at each finite level. So $H^2(U, \mathbb{Z}/p) = 0$. This is the argument of Serre, *Galois Cohomology*, Chapter II, §2.2. $\square$

### Vanishing over a function field of a curve

**Lemma 2.11.12 (From dimension to vanishing).** Let $H$ be a topological group and $q \geq 1$, with $\mathrm{cd}_\ell(H) \leq 1$ for every prime $\ell$ dividing $q$. Then $H^n(H, \mathbb{Z}/q) = 0$ for every $n \geq 2$, where $H$ acts trivially on $\mathbb{Z}/q$.

Lean: `GlobalTheory.EtC.CdOne.subsingleton_cohomology_trivial_zmod`.

*Proof.* Every element of $H^n(H, \mathbb{Z}/q)$ is killed by $q$, so the group is the sum of its $\ell$-primary components for the primes $\ell$ dividing $q$. Since $\mathbb{Z}/q$ is torsion and $n > 1 \geq \mathrm{cd}_\ell(H)$, each component is zero. $\square$

**Theorem 2.11.13 (Vanishing for fields algebraic over $k(t)$).** Let $q \geq 1$, let $k$ be an algebraically closed field, and let $K$ be a field with an algebraic map $k(t) \to K$, such that $q$ is a unit in $K$. Then $H^n(K, \mathbb{Z}/q(i)) = 0$ for all integers $n \geq 2$ and $i$.

Lean: `GlobalTheory.T.etale_cohomology_vanishing_algebraic_over_ratFunc` (also `GlobalTheory.EtC.gaugeSplitting_holds`).

*Proof.* Since $q$ is a unit in $K$ and $k \to K$ is injective, $q$ is a unit in $k$. As $k$ is algebraically closed, $\Phi_q$ has a root $\zeta \in k$, a primitive $q$-th root of unity, and its image in $K$ is a root of $\Phi_q$. Part 3 of the lemma on Tate twists gives $H^n(K, \mathbb{Z}/q(i)) \cong H^n(K, \mathbb{Z}/q(0))$. Take $\Omega$ a separable closure of $K$ and $M = \mathbb{Z}/q$ with the trivial action and basis $1$. The condition $\sigma b = a^0 b$ holds, so [Theorem 2.11.8](/entry/etale-cohomology-field-eq-galois-cohomology/) with $i = 0$ gives $H^n(K, \mathbb{Z}/q(0)) \cong H^n(G, \mathbb{Z}/q)$. By [Theorem 2.11.11](/entry/cdp-galois-le-one-of-is-algebraic-rat-func/), $\mathrm{cd}_\ell(G) \leq 1$ for every prime $\ell$, and the lemma from dimension to vanishing gives $H^n(G, \mathbb{Z}/q) = 0$. $\square$

**Remark 2.11.14 (Formalization).** The comparison for Tate twists is the condition $B_7$ and the vanishing is the condition $C_1$ of the package of axioms in [DivisorSupportCondition.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/DivisorSupportCondition.lean#L97). The condition $B_7$ allows only twists $i \geq 0$, so the proof of $C_1$ moves the twist to $0$ first. The name of the proof of $C_1$ speaks of a splitting of gauges, and its module is named after the statement: [EtaleCohomologyVanishingAlgebraicOverRatFunc.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/EtaleCohomologyVanishingAlgebraicOverRatFunc.lean#L43). The file [CohomologyFieldAddEquivGalois.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CohomologyFieldAddEquivGalois.lean#L277) ends with an unnamed copy of its theorem. In [EtaleCohomologyFieldEqGaloisCohomology.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/EtaleCohomologyFieldEqGaloisCohomology.lean#L113) one step is a tactic that is tried and may do nothing. The wrapper [CdpGaloisLeOneOfAlgebraicRatFuncStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CdpGaloisLeOneOfAlgebraicRatFuncStatement.lean#L3) imports Mathlib twice, and [CdpGaloisLeOneOfAlgebraicRatFunc.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CdpGaloisLeOneOfAlgebraicRatFunc.lean#L12) lowers a limit of instance search. We opened the statements of the inputs but not their proofs; the reasons we give after them are ours.
