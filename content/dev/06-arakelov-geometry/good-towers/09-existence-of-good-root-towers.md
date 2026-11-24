---
title: Existence of good root towers
decls:
  - GlobalTheory.CompanionTheory.Ar.TopTower.exists_good_tower
  - GlobalTheory.T.exists_good_root_tower
  - GlobalTheory.CompanionTheory.Ar.TopTower.comp_data
  - GlobalTheory.CompanionTheory.Ar.exists_refGeo
  - GlobalTheory.T.exists_reference_geometry_same_generic
  - GlobalTheory.T.exists_holomorphic_section_of_analytic
  - GlobalTheory.CompanionTheory.Ar.TopTower.level_data
  - GlobalTheory.CompanionTheory.Relay.intersection_degree_lower
status: drafted
drafted_by: writer@claude-opus-5-5
---

## Existence of good root towers

The volume theorem of the last section is a statement about a good root tower. This section proves that such a tower exists. Let $Y$ be a global model with split components. Then there are a root tower $T$ and a good origin of $Y$ over $T$ with the extra conditions: local holomorphic lifts of the reference points, and the value $R(p) = 4$ at every prime of every level. The construction has three steps. First, at the generic point of each irreducible component of $Y$ we build a reference geometry and a reference origin with an empty set of primes. Second, for each finite set $S$ of primes that contains the primes of the discriminant, we move the reference origin to a root origin over $S$. Third, we put these origins into one tower. The result feeds [the final assembly](/entry/good-tower-volume-of-reduced/) and through it [the good tower theorem](/entry/good-tower-and-volume/).

We keep the setting of the earlier sections. $E$ is a CM field with host $H$, $D$ is a datum of signature $(p, q)$ with $N = p + q$, $l$ is a level, $X_o$ is a moduli space for $D$ and $l$, $c$ is a coefficient datum with field $F$, and $Y$ is a model of $X_o$ over the ring of integers of $F$. We use the notions of a global model, of split components, of a reference geometry, of an analytic system with fixed data, of a root model and of a root origin over a set of primes. We do not unfold these. A point $x$ of $Y$ is a generic point of a component if every generization $x' \rightsquigarrow x$ has $x' = x$.

### The reference geometry of a component

**Theorem 8.9.1 (Reference geometry with a given generic point).** Assume the residue field statement. Let $\Omega_0$ be a field and let $\xi_0 \colon \operatorname{Spec} \Omega_0 \to Y$ be a point that is a compact generic point of a component. Then there is a reference geometry $G$ of $Y$ whose generic point is the generic point of $\xi_0$.

Lean: `GlobalTheory.CompanionTheory.Ar.exists_refGeo` (also `GlobalTheory.T.exists_reference_geometry_same_generic`, a second name).

*Proof.* First, the field $\Omega_0$ has characteristic $0$; this is a lemma on generic points of components of $Y$ that we do not unfold. The residue field statement gives coordinates for the component. These coordinates map to coordinates with constants over $\Omega_0$, and the generic coordinates descend to a subfield. We add one more block of coordinates, indexed by a set with one element, by a Segre embedding. This does not change the generic point. We reindex the normal crossings model and the complex coordinates by the new index set. In characteristic $0$ the new coordinates embed the generic fibre. The reference geometry has these coordinates. Its generic point is the generic point of $\xi_0$, since we replaced only the coordinates. $\square$

**Theorem 8.9.2 (Holomorphic inverse on the reference geometry).** Assume the top level inputs and the two flat line generator statements. Let $Y$ be global with split components and let $p, q \ge 1$. Then for every reference geometry $G$ of $Y$ there is an analytic datum $A$ for $G$ and a holomorphic map $\iota$ from the analytic space of $A$ to the complex space of the reference realization such that
$$
\iota(\pi(x)) = x
$$
for every point $x$ of the reference realization, where $\pi$ is the map of the realization to the analytic space.

Lean: `GlobalTheory.T.exists_holomorphic_section_of_analytic` (a second name of `AnalyticReference.reference_geometry_holomorphic_inverse`).

*Proof.* This result is proved outside this chapter, and we take it as given here. $\square$

### Component data

**Theorem 8.9.3 (Component data).** Assume the top level inputs and the two flat line generator statements. Let $Y$ be global with split components, let $p, q \ge 1$, and let $x$ be a generic point of a component of $Y$. Then there are an analytic system $\mathcal{S}$ of dimension the flag dimension of $(\Phi, N)$, with index set the root indices together with one more index, fixed data $F_x$ of $Y$ on $\mathcal{S}$, a root model $R$ and a root origin $o$ of $Y$ for $R$ and $F_x$ over the empty set of primes, with these properties.

1. The generic point of $F_x$ is $x$.
2. For each root index $r = (\tau, i)$, the weight of $F_x$ is $n_r = -k_A q' i$, where $k_A$ and $q'$ are positive integers of $F_x$.
3. The flag of $o$ has degree $1$, the realization of $o$ has $J = \top$, the line of $R$ is ample over $\mathbb{Q}$, the realization is embedded and the map $\pi$ of the realization is bijective.
4. For each $\tau$ and each $i$ with $i + 1 = N$ and for each $t$, the potential of $\mathcal{S}$ at $(\tau, i)$ and $t$ and its negative are plurisubharmonic.
5. Every point $y$ of the analytic space has an open neighbourhood $U$ and holomorphic functions $\lambda_0, \dots, \lambda_m$ on $U$ such that $\lambda(z) = a_0(z)\, \mathrm{pt}(z)$ with $a_0(z) \ne 0$ for every $z \in U$. If $\lambda_k(y) \ne 0$, then in every chart at $y$ the map $z \mapsto (\lambda_j(z)/\lambda_k(z))_j$ has an injective differential at $y$.

Lean: `GlobalTheory.CompanionTheory.Ar.TopTower.comp_data`.

*Proof.* The stalks of $Y$ are domains, since $Y$ is normal. So the residue field point at $x$ is a compact generic point. The [reference geometry theorem](/entry/exists-ref-geo/) gives a reference geometry $G$ with generic point $x$, and the [holomorphic inverse theorem](/entry/exists-holomorphic-section-of-analytic/) gives an analytic datum $A$ for $G$ with a holomorphic inverse $\iota$ of $\pi$. We take the weight $\nu(\tau, i) = -i$. It is antitone in $i$. A lemma on effective weight sections gives integers $k_A, q' \ge 1$ and an effective section $s$ of the weight $\nu$ on $A$. A second lemma uses the retraction $\iota$ of $\pi$ and the split components. It turns $s$ into fixed data $F_x$ with weight $k_A q' \nu$, a root model $R$ and an origin $o$ with property 1, property 3 and the lifts of property 5. Property 2 is the formula $n_r = k_A q' \nu(r)$. Property 4 is the flatness condition of the analytic datum $A$, since the system of $F_x$ is the system of $A$. $\square$

### Change of the set of primes

**Theorem 8.9.4 (Level data).** Assume the top level inputs and the Weil pairing statement. Let $\mathcal{S}$, $F_x$, $R$ and $o$ be as in the last theorem: $o$ is a root origin over the empty set of primes with a flag of degree $1$, an embedded realization and a bijective map $\pi$. Let $S$ be a finite set of primes that contains every prime that divides the discriminant of $E$. Then there are a root model $R'$ and a root origin $o'$ of $Y$ for $R'$ and $F_x$ over $S$ such that the Hodge component of $o'$ satisfies the condition on the Lie lattices, $R(p) = 4$ for every $p \in S$, the realization of $o'$ has $J = \top$, and the field of $R'$ is an algebra over $\mathbb{Q}$ on which the model $R'$ has a smooth generic fibre.

Lean: `GlobalTheory.CompanionTheory.Ar.TopTower.level_data`.

*Proof.* The Weil pairing statement shows that the primes at which the origin $o$ is not good form a finite set, and it gives a field $\Omega$, a Hodge component with $R(p) = 4$ for $p \in S$, a flag of degree $1$ and the lines of the flag over $S$. Then the coordinates of the origin descend to a field. This gives the root model $R'$ and the origin $o'$ over $S$ with the condition on the Lie lattices, $J = \top$ and a smooth generic fibre. The value of $R(p)$ is not changed by the descent. $\square$

### The tower

**Theorem 8.9.5 (Existence of good root towers).** Assume the top level inputs, the Weil pairing statement and the two flat line generator statements. For each level $l$ let $X_o(l)$ be a moduli space for $D$ and $l$. Let $Y$ be a global model of $X_o(l)$ with split components and let $p, q \ge 1$. Then there are a root tower $T$ of type $(\Phi, N)$ and a good origin $o$ of $Y$ over $T$ with these properties.

1. For each component $a$ of $T$, every point of the analytic space of the system of $o$ at $a$ has local holomorphic lifts as in property 5 of the theorem on component data.
2. For every level $B$, every component $a$ and every prime $p \in S_B$, the Hodge component of the origin at $(B, a)$ has $R(p) = 4$.

Lean: `GlobalTheory.CompanionTheory.Ar.TopTower.exists_good_tower` (also `GlobalTheory.T.exists_good_root_tower`, a second name).

*Proof.* Let $C$ be the set of generic points of the irreducible components of $Y$. It is finite and not empty. For each $x \in C$ the [theorem on component data](/entry/comp-data/) gives a system, fixed data, a reference root model $R_x$ and a reference origin $o_x$ over the empty set of primes. Let $M'$ be the least common multiple of the two integers of the level $l$. Then $M' \ne 0$. Let the bad primes be the primes that divide $2\,|d_E|\,M'$. For each $B$ let $S_B$ be the set of primes $p \le B$ together with the bad primes. It is finite and contains every prime that divides $d_E$. For each $B$ and $x$ the [level data theorem](/entry/level-data/) moves $o_x$ to a root origin over $S_B$ with $R(p) = 4$ on $S_B$, the condition on the Lie lattices and a smooth generic fibre. The tower $T$ has index $j = p$, components $C$, the bad primes above, the weight $\nu(\tau, i) = -i$ and the models of the level data. Since $q \ge 1$, $j < N$. The good origin takes the origins over $S_B$ and the reference data of the component data. Property 1 is property 5 of the component data, and property 2 is the value of $R(p)$ in the level data. $\square$

The weight $\nu(\tau, i) = -i$ is the same for every CM type $\tau$, and the reference origin at a component does not depend on $B$. Only the origins over $S_B$ depend on $B$.

**Remark 8.9.6 (Formalization).** The residue field statement enters the proof of `comp_data` by position, as the component `hG.2.2.2.2.1` of `Top.Given` (ExistsGoodRootTower.lean:42). The holomorphic inverse `T.exists_holomorphic_section_of_analytic` is a second name of a result outside this chapter, and the second names in this section are proved by `first | exact @...`. The Segre block in the proof of `exists_refGeo` is indexed by `Unit` (ExistsReferenceGeometrySameGeneric.lean:24 to 86), and the final step only replaces the coordinates (lines 123 to 166). The steps of the proofs are named results such as `T.exists_effective_weight_section`, `T.effective_scaled_weight_of_retraction`, `T.root_origin_good_primes_finite` and `T.root_origin_coords_over_field`, which we do not unfold. The statement files import `Mathlib` twice (ExistsGoodRootTowerStatement.lean:1 and 3). The list of declarations of this section also contains `Relay.intersection_degree_lower`, whose second name is stated as [Theorem 8.6.4](/entry/t-intersection-degree-lower/). It has no hypothesis on a cusp weight, and it takes its input on point integrals from `Top.Given` by position (IntersectionDegreeLower.lean:24).
