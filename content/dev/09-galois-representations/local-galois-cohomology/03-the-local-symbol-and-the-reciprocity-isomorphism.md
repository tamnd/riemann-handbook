---
title: The local symbol and the reciprocity isomorphism
decls:
  - ReciprocityTheory.DiscreteGroups.LocalClassField.pairK
  - ReciprocityTheory.DiscreteGroups.LocalClassField.exists_recipHom
  - ReciprocityTheory.DiscreteGroups.LocalClassField.exists_normGrp_eq_of_le
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The local symbol and the reciprocity isomorphism

Sections 3 to 5 build the local Artin map of a finite extension $K$ of $\mathbb{Q}_p$ by the cohomological method of Serre. This section defines the local symbol $(a, \chi) = \operatorname{inv}_K(a \cup \delta\chi)$ and uses it to identify $K^\times / N_{L/K}(L^\times)$ with $\operatorname{Gal}(L/K)$ for each finite abelian extension $L$. The next section proves the existence theorem from this identification, and Section 5 glues the identifications over all $L$ into the Artin map.

### The setting

Fix a prime $p$ and an algebraic closure $\overline{\mathbb{Q}}_p$ of $\mathbb{Q}_p$, with the absolute value $|\cdot|$ that extends the one of $\mathbb{Q}_p$, so $|p| = p^{-1}$. In this section and the next, $K$ is a subfield of $\overline{\mathbb{Q}}_p$ of finite degree over $\mathbb{Q}_p$. Let $G_K = \operatorname{Gal}(\overline{\mathbb{Q}}_p/K)$ with its Krull topology. For a field $L$ between $K$ and $\overline{\mathbb{Q}}_p$, $G_L \leq G_K$ is the subgroup that fixes $L$. Let $v_K$ be the normalized valuation of $K$, $e_K$ its ramification index over $\mathbb{Q}_p$, $q_K$ the number of elements of its residue field, and $U_K = \ker v_K$. This is the setting of the first section with $\Omega = \overline{\mathbb{Q}}_p$ and $G = G_K$.

**Definition 1.3.1 (finite abelian extension).** A field $L$ with $K \subseteq L \subseteq \overline{\mathbb{Q}}_p$ is a *finite abelian extension* of $K$ if $[L : \mathbb{Q}_p]$ is finite and the commutator subgroup $[G_K, G_K]$ lies in $G_L$. Then $G_L$ is normal, $L/K$ is Galois with abelian group $\operatorname{Gal}(L/K) = G_K/G_L$, and $[L : K] = [G_K : G_L]$.

Lean: `ReciprocityTheory.DiscreteGroups.LocalClassField.IsAbLK` (also `ReciprocityTheory.DiscreteGroups.LocalClassField.degLK`, `ReciprocityTheory.DiscreteGroups.LocalClassField.GalLK`).

**Definition 1.3.2 (norm group).** Let $L \supseteq K$ be finite over $\mathbb{Q}_p$. For $y \in L^\times$ put
$$N_{L/K}(y) = \prod_{c \in G_K/G_L} \sigma_c(y),$$
where $\sigma_c \in G_K$ is a representative of the left coset $c$. This is the field norm: the cosets correspond to the $K$-embeddings of $L$. The *norm group* of $L$ is $N_L = N_{L/K}(L^\times) \leq K^\times$.

Lean: `ReciprocityTheory.DiscreteGroups.LocalClassField.normGrp` (also `ReciprocityTheory.DiscreteGroups.LocalClassField.normHom`).

For $x \in K^\times$ the norm is $x^{[L:K]}$, so $N_L$ contains $(K^\times)^{[L:K]}$. This subgroup is open and of finite index, so $N_L$ is open and of finite index.

**Definition 1.3.3 (characters).** Let $X(G_K)$ be the group of continuous homomorphisms $\chi : G_K \to \mathbb{Q}/\mathbb{Z}$, with the discrete topology on $\mathbb{Q}/\mathbb{Z}$. We say that $\chi$ is *trivial on* $L$ if $\chi(G_L) = 0$.

Lean: `ReciprocityTheory.DiscreteGroups.LocalClassField.charGrp` (also `ReciprocityTheory.DiscreteGroups.LocalClassField.TrivOn`).

If $L/K$ is finite abelian, the characters trivial on $L$ are the characters of the finite abelian group $\operatorname{Gal}(L/K)$. So there are $[L : K]$ of them, and they separate the elements of $\operatorname{Gal}(L/K)$.

### The local symbol

Let $\operatorname{Br}(K) = H^2(G_K, \overline{\mathbb{Q}}_p^\times)$, computed with continuous cochains ([continuous cohomology](/learn/galois-cohomology/#continuous-cohomology)). Let $K^{\mathrm{nr}} \subseteq \overline{\mathbb{Q}}_p$ be the maximal unramified extension and $\operatorname{Frob} \in \operatorname{Gal}(K^{\mathrm{nr}}/K)$ the arithmetic Frobenius. We use two facts on the Brauer group, proved in Serre, *Local Fields*, Chapter XII.

- The inflation map $H^2(\operatorname{Gal}(K^{\mathrm{nr}}/K), (K^{\mathrm{nr}})^\times) \to \operatorname{Br}(K)$ is bijective.
- There is an isomorphism $\operatorname{inv} : H^2(\operatorname{Gal}(K^{\mathrm{nr}}/K), (K^{\mathrm{nr}})^\times) \to \mathbb{Q}/\mathbb{Z}$ with the following property. Let $\pi$ be a uniformizer of $K$ and $t : \operatorname{Gal}(K^{\mathrm{nr}}/K) \to \mathbb{Q}$ a locally constant function such that $\delta t(g, h) = t(g) + t(h) - t(gh)$ lies in $\mathbb{Z}$ for all $g, h$. Then the class of the cocycle $(g, h) \mapsto \pi^{\delta t(g, h)}$ has invariant $t(\operatorname{Frob}) \bmod \mathbb{Z}$.

**Definition 1.3.4 (invariant map).** The *invariant map* $\operatorname{inv}_K : \operatorname{Br}(K) \to \mathbb{Q}/\mathbb{Z}$ is the map $\operatorname{inv}$ composed with the inverse of the inflation map.

Lean: `ReciprocityTheory.DiscreteGroups.LocalClassField.invBr` (also `ReciprocityTheory.DiscreteGroups.LocalClassField.invUr`, `ReciprocityTheory.DiscreteGroups.LocalClassField.inflation_unramified_closure_h2_bijective`).

**Definition 1.3.5 (local symbol).** Let $a \in K^\times$ and $\chi \in X(G_K)$. Choose a locally constant lift $t : G_K \to \mathbb{Q}$ of $\chi$. Then $\delta t$ takes values in $\mathbb{Z}$, and $(g, h) \mapsto a^{\delta t(g, h)}$ is a continuous $2$-cocycle with values in $\overline{\mathbb{Q}}_p^\times$. Its class is the cup product $a \cup \delta\chi \in \operatorname{Br}(K)$ of $a \in H^0(G_K, \overline{\mathbb{Q}}_p^\times)$ with the image $\delta\chi \in H^2(G_K, \mathbb{Z})$ of $\chi$ under the coboundary of $0 \to \mathbb{Z} \to \mathbb{Q} \to \mathbb{Q}/\mathbb{Z} \to 0$. The *local symbol* is
$$(a, \chi) = \operatorname{inv}_K(a \cup \delta\chi) \in \mathbb{Q}/\mathbb{Z}.$$

Lean: `ReciprocityTheory.DiscreteGroups.LocalClassField.pairK` (also `ReciprocityTheory.DiscreteGroups.LocalClassField.pairBr`).

**Proposition 1.3.6 (properties of the local symbol).** Let $a, b \in K^\times$ and $\chi, \psi \in X(G_K)$.

1. $(ab, \chi) = (a, \chi) + (b, \chi)$ and $(a, \chi + \psi) = (a, \chi) + (a, \psi)$.
2. If $\chi$ is trivial on $K^{\mathrm{nr}}$, then $(a, \chi) = v_K(a)\, \chi(\phi)$ for any $\phi \in G_K$ that restricts to $\operatorname{Frob}$ on $K^{\mathrm{nr}}$.
3. If $L \supseteq K$ is finite over $\mathbb{Q}_p$, $a \in N_L$ and $\chi$ is trivial on $L$, then $(a, \chi) = 0$.
4. If $(a, \chi) = 0$ for all $a \in K^\times$, then $\chi = 0$.

Lean: `ReciprocityTheory.DiscreteGroups.LocalClassField.pairK_mul` (also `ReciprocityTheory.DiscreteGroups.LocalClassField.pairK_add`, `ReciprocityTheory.DiscreteGroups.LocalClassField.pairK_unr`, `ReciprocityTheory.DiscreteGroups.LocalClassField.pairK_eq_zero_of_mem_normGrp`, `ReciprocityTheory.DiscreteGroups.LocalClassField.eq_zero_of_pairK_eq_zero`).

*Proof.* Part 1 holds because the cocycle is bilinear in $a$ and in the lift $t$. For part 2, $\chi$ comes from a character of $\operatorname{Gal}(K^{\mathrm{nr}}/K)$, so $a \cup \delta\chi$ is inflated from the unramified Brauer group. By part 1 it is enough to treat a uniformizer $\pi$ and the units. For $\pi$ the defining property of $\operatorname{inv}$ gives $\chi(\operatorname{Frob})$. A unit $u$ gives $0$, because $u$ is a norm from each finite unramified extension (Serre, *Local Fields*, Chapter V, §2). For part 3, write $a = N_{L/K}(b)$. The corestriction from $L$ to $K$ sends $b \cup \delta(\chi|_{G_L})$ to $N_{L/K}(b) \cup \delta\chi$ and is compatible with the invariant maps, so $(a, \chi) = (b, \chi|_{G_L})_L = 0$. For part 4, let $M$ be the fixed field of $\ker \chi$. Then $M/K$ is cyclic of degree the order of $\chi$. For a cyclic extension, $(a, \chi) = 0$ holds exactly when $a \in N_M$, and $[K^\times : N_M] = [M : K]$ (the class field axiom for cyclic extensions, Serre, *Local Fields*, Chapter XIII). So $N_M = K^\times$, $M = K$ and $\chi = 0$. $\square$

### Reciprocity elements

**Definition 1.3.7 (reciprocity element).** Let $L/K$ be finite abelian and $a \in K^\times$. An element $g \in G_K$ is a *reciprocity element for $a$ on $L$* if $\chi(g) = (a, \chi)$ for each $\chi \in X(G_K)$ trivial on $L$.

Lean: `ReciprocityTheory.DiscreteGroups.LocalClassField.IsRecip`.

**Proposition 1.3.8 (the reciprocity isomorphism).** Let $L/K$ be finite abelian.

1. Each $a \in K^\times$ has a reciprocity element $g_a$ on $L$, and it is unique modulo $G_L$.
2. Each $g \in G_K$ is a reciprocity element on $L$ for some $a \in K^\times$.
3. The map $\rho_L : K^\times \to \operatorname{Gal}(L/K)$, $a \mapsto g_a G_L$, is a surjective homomorphism with kernel $N_L$. So $[K^\times : N_L] = [L : K]$, and for a reciprocity element $g$ of $a$ we have $g \in G_L$ if and only if $a \in N_L$.

Lean: `ReciprocityTheory.DiscreteGroups.LocalClassField.exists_recipHom` (also `ReciprocityTheory.DiscreteGroups.LocalClassField.exists_isRecip`, `ReciprocityTheory.DiscreteGroups.LocalClassField.IsRecip.unique`, `ReciprocityTheory.DiscreteGroups.LocalClassField.exists_isRecip_of_gal`, `ReciprocityTheory.DiscreteGroups.LocalClassField.recipHom_ker`, `ReciprocityTheory.DiscreteGroups.LocalClassField.index_normGrp`, `ReciprocityTheory.DiscreteGroups.LocalClassField.IsRecip.mem_subG_iff`).

*Proof.* Part 1. By part 1 of the properties, $\chi \mapsto (a, \chi)$ is a homomorphism on the dual group of $\operatorname{Gal}(L/K)$. By Pontryagin duality for finite abelian groups it is evaluation at a unique element of $\operatorname{Gal}(L/K)$.

Part 2. The reciprocity elements of all $a \in K^\times$ form a subgroup $S$ of $G_K$ that contains $G_L$. So $S$ is open, and $S = G_{L_0}$ for a field $K \subseteq L_0 \subseteq L$. If $g \notin S$, there is a character $\chi$ trivial on $L_0$ with $\chi(g) \neq 0$. For each $a$, $(a, \chi) = \chi(g_a) = 0$, since $g_a \in G_{L_0}$. By part 4 of the properties $\chi = 0$, a contradiction.

Part 3. The map $\rho_L$ is a homomorphism by uniqueness, and it is onto by part 2. If $a \in N_L$, then $\chi(g_a) = (a, \chi) = 0$ for all $\chi$ trivial on $L$ by part 3 of the properties, so $g_a \in G_L$. Hence $N_L \subseteq \ker \rho_L$, and $[K^\times : N_L] \geq [L : K]$. For the other inequality we use induction on $[L : K]$. If $L \neq K$, choose a nonzero character $\chi$ trivial on $L$, and let $M$ be the fixed field of its kernel. Then $M/K$ is cyclic and $M \neq K$. By the transitivity of the norm and the cyclic case $[K^\times : N_M] = [M : K]$,
$$[K^\times : N_{L/K}(L^\times)] \leq [M^\times : N_{L/M}(L^\times)]\,[M : K] \leq [L : M]\,[M : K] = [L : K],$$
where the middle step is the induction hypothesis for $L/M$. So $N_L = \ker \rho_L$. $\square$

**Lemma 1.3.9 (subgroups above a norm group).** Let $L/K$ be finite abelian, and $H \leq K^\times$ a subgroup with $N_L \subseteq H$. Then there is a finite abelian extension $L_0 \subseteq L$ of $K$ with $N_{L_0} = H$.

Lean: `ReciprocityTheory.DiscreteGroups.LocalClassField.exists_normGrp_eq_of_le` (also `ReciprocityTheory.DiscreteGroups.LocalClassField.exists_field_recipImage`).

*Proof.* The reciprocity elements on $L$ of the elements of $H$ form a subgroup of $G_K$ that contains $G_L$. Let $L_0 \subseteq L$ be its fixed field. Let $a \in K^\times$ with reciprocity element $g_a$. By the proposition, $a \in N_{L_0}$ if and only if $g_a \in G_{L_0}$, that is, $g_a \equiv g_{a'} \bmod G_L$ for some $a' \in H$. This holds if and only if $a a'^{-1} \in N_L \subseteq H$ for some $a' \in H$, that is, $a \in H$. $\square$

**Remark 1.3.10 (Formalization).** The norm $N_{L/K}$ is defined as the product over coset representatives on all of $\overline{\mathbb{Q}}_p^\times$ ([RecDefs.lean](lean:ReciprocityTheory/ClassFieldTheory/LocalClassField/RecDefs.lean#L21)), not as the norm of Mathlib. The class $a \cup \delta\chi$ is chosen among the classes with the stated cocycle, with the value $0$ if there is none ([RecPairDefs.lean](lean:ReciprocityTheory/ClassFieldTheory/LocalClassField/RecPairDefs.lean#L22)). So are $\operatorname{inv}_K$ and $\operatorname{inv}$ ([Brauer.lean](lean:ReciprocityTheory/ClassFieldTheory/LocalClassField/Brauer.lean#L62)); their defining properties are proved. The Frobenius element $\phi$ of part 2 of the properties is one fixed lift `ReciprocityTheory.DiscreteGroups.LocalClassField.frobK`, chosen by `Classical.epsilon` ([ExistsIntEKMulVbar.lean](lean:ReciprocityTheory/ClassFieldTheory/LocalClassField/ExistsIntEKMulVbar.lean#L192)). The condition on a finite abelian extension uses the commutator subgroup, not its closure; since $G_L$ is closed this makes no difference.
