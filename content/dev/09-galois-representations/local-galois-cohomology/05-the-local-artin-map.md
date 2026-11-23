---
title: The local Artin map
decls:
  - ReciprocityTheory.DiscreteGroups.LocalClassField.isArtinK_of_isRecip
  - ReciprocityTheory.DiscreteGroups.LocalClassField.exists_isArtinK
  - ReciprocityTheory.DiscreteGroups.LocalClassField.artin_reciprocity_char_zero
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The local Artin map

This section proves the local reciprocity law for nonarchimedean local fields of characteristic $0$: there is a continuous injective homomorphism $\operatorname{Art}_K : K^\times \to G_K^{\mathrm{ab}}$ with dense image, which sends uniformizers to Frobenius elements and induces $K^\times/N_{L/K}(L^\times) \cong \operatorname{Gal}(L/K)$ for each finite abelian $L$ ([local class field theory](/learn/class-field-theory/#local-class-field-theory)). We first build the map for a finite extension of $\mathbb{Q}_p$ inside $\overline{\mathbb{Q}}_p$, from the reciprocity elements of Section 3, and then move it to an abstract local field. The result is used by the theorem that the product of two non-norms from a quadratic extension of a local field is a norm, [Theorem 1.15 of Volume 12](/entry/mul-mem-range-norm/).

### The Artin map of a subfield of $\overline{\mathbb{Q}}_p$

We keep the setting of Section 3: $K \subseteq \overline{\mathbb{Q}}_p$ is finite over $\mathbb{Q}_p$, $G_K = \operatorname{Gal}(\overline{\mathbb{Q}}_p/K)$, and $N_L = N_{L/K}(L^\times)$. Let $G_K^{\mathrm{ab}}$ be the quotient of $G_K$ by the closure of its commutator subgroup, and write $g \mapsto \bar g$ for the quotient map. An element $g \in G_K$ is a *lift* of $\bar g$.

**Definition 1.5.1 (Frobenius lift).** An element $\sigma \in G_K$ is a *Frobenius lift* if $|\sigma(x) - x^{q_K}| < 1$ for each $x \in \overline{\mathbb{Q}}_p$ with $|x| \leq 1$.

Lean: `ReciprocityTheory.DiscreteGroups.LocalClassField.IsFrob`.

So $\sigma$ induces the Frobenius $x \mapsto x^{q_K}$ on the residue field of $\overline{\mathbb{Q}}_p$. An element $\sigma$ is a Frobenius lift if and only if $\sigma(\zeta) = \zeta^{q_K}$ for each root of unity $\zeta$ of order prime to $p$. These roots of unity generate $K^{\mathrm{nr}}$, so a Frobenius lift is the same as an element that restricts to $\operatorname{Frob}$ on $K^{\mathrm{nr}}$ ([decomposition groups](/learn/galois-representations/#decomposition-groups-inertia-and-frobenius)).

**Definition 1.5.2 (Artin map).** A homomorphism $\operatorname{Art} : K^\times \to G_K^{\mathrm{ab}}$ is an *Artin map* for $K$ if:

1. $\operatorname{Art}$ is continuous and injective, and its image is dense;
2. for each $\pi \in K^\times$ with $v_K(\pi) = 1$, each lift of $\operatorname{Art}(\pi)$ is a Frobenius lift;
3. for each finite abelian extension $L$ of $K$: each $g \in G_K$ is congruent modulo $G_L$ to a lift of some $\operatorname{Art}(x)$, and for each $x \in K^\times$ and each lift $g$ of $\operatorname{Art}(x)$, we have $g \in G_L$ if and only if $x \in N_L$.

Lean: `ReciprocityTheory.DiscreteGroups.LocalClassField.IsArtinK`.

Condition 3 says that $K^\times \to G_K^{\mathrm{ab}} \to \operatorname{Gal}(L/K)$ is surjective with kernel $N_L$.

We use two facts on the topology of $G_K^{\mathrm{ab}}$. The groups $G_L/\overline{[G_K, G_K]}$, for $L$ finite abelian, form a basis of open neighbourhoods of $1$, and $G_K^{\mathrm{ab}}$ is the inverse limit of the finite groups $\operatorname{Gal}(L/K)$. Hence:

- a map $f$ from a topological space $X$ to $G_K^{\mathrm{ab}}$ is continuous if and only if for each finite abelian $L$ and each $x \in X$, all $y$ near $x$ satisfy $g^{-1}g' \in G_L$ for all lifts $g$ of $f(x)$ and $g'$ of $f(y)$;
- a map $f : X \to G_K^{\mathrm{ab}}$ has dense image if and only if for each finite abelian $L$, each $g \in G_K$ is congruent modulo $G_L$ to a lift of some $f(x)$;
- given, for each finite abelian $L$, a map $\gamma_L : K^\times \to G_K$ that is a homomorphism modulo $G_L$ and with $\gamma_{L'}(a) \equiv \gamma_L(a) \bmod G_L$ for $L \subseteq L'$, there is a homomorphism $f : K^\times \to G_K^{\mathrm{ab}}$ with $g \equiv \gamma_L(a) \bmod G_L$ for each lift $g$ of $f(a)$ and each $L$.

**Theorem 1.5.3 (Artin map from reciprocity elements).** Let $\operatorname{Art} : K^\times \to G_K^{\mathrm{ab}}$ be a homomorphism such that, for each $a \in K^\times$, each lift $g$ of $\operatorname{Art}(a)$ and each finite abelian extension $L$ of $K$, the element $g$ is a reciprocity element for $a$ on $L$. Then $\operatorname{Art}$ is an Artin map for $K$.

Lean: `ReciprocityTheory.DiscreteGroups.LocalClassField.isArtinK_of_isRecip`.

*Proof.* We check the conditions. Let $L$ be finite abelian.

The first half of condition 3. Let $g \in G_K$. By the reciprocity isomorphism of Section 3, $g$ is a reciprocity element on $L$ for some $a$. A lift $g'$ of $\operatorname{Art}(a)$ is another one, so $g'^{-1} g \in G_L$ by uniqueness. This also gives the density of the image, by the second fact on the topology.

The second half of condition 3. If $g$ lifts $\operatorname{Art}(x)$, it is a reciprocity element for $x$, and the reciprocity isomorphism says $g \in G_L$ if and only if $x \in N_L$.

Continuity. Let $x \in K^\times$. The set $x N_L$ is open, since $N_L$ contains the open subgroup $(K^\times)^{[L:K]}$. Let $y \in x N_L$, and let $g, g'$ be lifts of $\operatorname{Art}(x), \operatorname{Art}(y)$. Let $k$ be a reciprocity element for $x^{-1}y$; then $gk$ is one for $y$, so $g' \equiv gk \bmod G_L$. Since $x^{-1}y \in N_L$, $k \in G_L$, and so $g^{-1}g' \in G_L$. The first fact on the topology gives continuity.

Injectivity. Let $\operatorname{Art}(a) = 1$. Then $1$ is a lift of $\operatorname{Art}(a)$, hence a reciprocity element for $a$ on each $L$. Since $1 \in G_L$, the reciprocity isomorphism gives $a \in N_L$ for every finite abelian $L$. By the [Corollary 1.4.7](/entry/eq-one-of-forall-mem-norm-grp/) on universal norms, $a = 1$.

Condition 2. Let $v_K(\pi) = 1$ and let $g$ lift $\operatorname{Art}(\pi)$. For $n \geq 1$ let $K_n$ be the unramified extension of $K$ of degree $n$, generated by the roots of unity of order $q_K^n - 1$. It is finite abelian. Fix one Frobenius lift $\phi$. Each character $\chi$ trivial on $K_n$ is trivial on $K^{\mathrm{nr}}$, so $(\pi, \chi) = \chi(\phi)$ by part 2 of the properties of the local symbol. So $\phi$ is a reciprocity element for $\pi$ on $K_n$, and so is $g$. By uniqueness $\phi^{-1} g \in G_{K_n}$ for all $n$. Each root of unity of order prime to $p$ lies in some $K_n$, so $g(\zeta) = \phi(\zeta) = \zeta^{q_K}$ for all such $\zeta$, and $g$ is a Frobenius lift. $\square$

**Theorem 1.5.4 (existence of the Artin map).** Each finite extension $K$ of $\mathbb{Q}_p$ in $\overline{\mathbb{Q}}_p$ has an Artin map.

Lean: `ReciprocityTheory.DiscreteGroups.LocalClassField.exists_isArtinK` (also `ReciprocityTheory.DiscreteGroups.LocalClassField.exists_artin_hom`).

*Proof.* For each finite abelian $L$ and each $a \in K^\times$, choose a reciprocity element $\gamma_L(a)$ for $a$ on $L$. By uniqueness modulo $G_L$, $\gamma_L$ is a homomorphism modulo $G_L$: both $\gamma_L(ab)$ and $\gamma_L(a)\gamma_L(b)$ are reciprocity elements for $ab$. For $L \subseteq L'$, a reciprocity element on $L'$ is one on $L$, so $\gamma_{L'}(a) \equiv \gamma_L(a) \bmod G_L$. The third fact on the topology gives a homomorphism $\operatorname{Art} : K^\times \to G_K^{\mathrm{ab}}$ such that each lift of $\operatorname{Art}(a)$ is congruent to $\gamma_L(a)$ modulo $G_L$, hence is a reciprocity element for $a$ on $L$. The [Theorem 1.5.3](/entry/is-artin-k-of-is-recip/) on the Artin map from reciprocity elements applies. $\square$

### Local reciprocity for an abstract local field

Now let $K$ be any nonarchimedean local field, with ring of integers $\mathcal{O}_K$, residue field of $q$ elements, and an algebraic closure $\overline{K}$. Let $\mathcal{O}_{\overline{K}}$ be the integral closure of $\mathcal{O}_K$ in $\overline{K}$ and $\mathfrak{m}_{\overline{K}}$ the set of $y \in \mathcal{O}_{\overline{K}}$ with $y = 0$ or $y^{-1} \notin \mathcal{O}_{\overline{K}}$. Let $G_K^{\mathrm{ab}}$ be the quotient of $\operatorname{Gal}(\overline{K}/K)$ by the closure of its commutator subgroup. A finite abelian extension is a finite Galois extension $L \subseteq \overline{K}$ of $K$ with abelian group, and $N_{L/K}(L^\times)$ is the image of the field norm.

**Definition 1.5.5 (local Artin map).** A homomorphism $\operatorname{Art} : K^\times \to G_K^{\mathrm{ab}}$ is a *local Artin map* if:

1. $\operatorname{Art}$ is continuous and injective, and its image is dense;
2. for each uniformizer $\pi$ of $K$, each lift $g$ of $\operatorname{Art}(\pi)$ satisfies $g(x) - x^q \in \mathfrak{m}_{\overline{K}}$ for all $x \in \mathcal{O}_{\overline{K}}$;
3. for each finite abelian extension $L$, the composite $K^\times \to G_K^{\mathrm{ab}} \to \operatorname{Gal}(L/K)$ is surjective with kernel $N_{L/K}(L^\times)$.

We say that *local reciprocity holds for $K$* if a local Artin map exists.

Lean: `Neutral.B1.IsLocalArtinMap` (also `Neutral.B1.LocalReciprocity`).

The classical local reciprocity law (Neukirch, *Algebraic Number Theory*, Chapter V, §1; Serre, *Local Fields*, Chapter XIII, §4) says that local reciprocity holds for every nonarchimedean local field.

**Theorem 1.5.6 (local reciprocity in characteristic zero).** Let $K$ be a nonarchimedean local field of characteristic $0$. Then local reciprocity holds for $K$.

Lean: `ReciprocityTheory.DiscreteGroups.LocalClassField.artin_reciprocity_char_zero`.

*Proof.* Let $p$ be the residue characteristic. Since $K$ has characteristic $0$, $\mathbb{Q}$ and then $\mathbb{Q}_p$ embed continuously in $K$, and $K$ is a finite extension of $\mathbb{Q}_p$. So there is a field $K' \subseteq \overline{\mathbb{Q}}_p$, finite over $\mathbb{Q}_p$, with a homeomorphic isomorphism $e : K \to K'$ that matches $\mathcal{O}_K$ with $\{x : |e(x)| \leq 1\}$, and an isomorphism $\overline{K} \to \overline{\mathbb{Q}}_p$ that extends $e$. These maps identify $\operatorname{Gal}(\overline{K}/K)$ with $G_{K'}$, the abelianizations, the finite abelian extensions, the norm groups and the Frobenius conditions. The [Theorem 1.5.4](/entry/exists-is-artin-k/) on the existence of the Artin map gives an Artin map for $K'$, and its transport is a local Artin map for $K$. $\square$

**Remark 1.5.7 (Formalization).** The theorem covers only characteristic $0$; the hypothesis is used to embed $\mathbb{Q}_p$ in $K$ ([TransportC.lean](lean:ReciprocityTheory/ClassFieldTheory/LocalClassField/TransportC.lean#L155)). The two definitions of the norm group differ: the abstract one is the image of the norm of Mathlib, the one for subfields of $\overline{\mathbb{Q}}_p$ is the product over cosets of Section 3. The transport shows they match (`ReciprocityTheory.DiscreteGroups.LocalClassField.Model.mem_normGroup_iff`). The Artin map is built from choices of reciprocity elements, and the statement $\operatorname{Art}_K(\pi) = $ Frobenius is in the arithmetic normalization, in agreement with the Lubin-Tate law of Section 2. The existence theorem for an abstract local field is a separate statement (`Neutral.B1.LocalExistence`, with $H$ open and of finite index); this chapter does not prove it in that form. Uniqueness of the Artin map is proved as well ([RecArtin.lean](lean:ReciprocityTheory/ClassFieldTheory/LocalClassField/RecArtin.lean#L144)), but the proof of reciprocity does not use it.
