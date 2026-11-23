---
title: A group scheme from a strict law
decls:
  - GlobalTheory.T.exists_union_translates'
  - GlobalTheory.SS.exists_union_translates
  - GlobalTheory.T.exists_grpObj_of_strictBirationalLaw
  - GlobalTheory.SS.exists_grpObj_of_strict
  - GlobalTheory.SS.exists_neutral_group_model
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A group scheme from a strict law

Let $R$ be a strictly Henselian discrete valuation ring with fraction field $K$, and let $A$ be a commutative abelian scheme over $K$. This section turns a model of $A$ with a strict birational group law into a smooth group scheme $G$ over $R$ with generic fibre $A$. The scheme $G$ is the union of finitely many translates of the model. This is Weil's theorem on birational group laws in the form of Bosch, Lütkebohmert and Raynaud. With [the birational group law](/entry/exists-weak-neron-model-birational-group-law/) it gives the neutral group model: a smooth connected group model of $A$ to which a fixed power of every rational point extends. The neutral group model enters the main proof at [the step on every character](/step/every-character/), through the results on semi-abelian reduction in the next sections. We keep the notation of the two previous sections.

### Strict laws and compatible models

**Definition 6.17.1 (Strict law).** A model $M$ of $A$ has a *strict* birational group law if it has a birational group law and, for each shear $\mathrm{sh}$ of $A \times A$ and each point $x$ of the special fibre of $M$, there are points $z$ and $z'$ of $M \times M$ with first coordinate $x$ and with second coordinate $x$, respectively, at which $\mathrm{sh}$ is an isomorphism from $M \times M$ to itself.

Lean: `GlobalTheory.SS.Strict`.

**Definition 6.17.2 (Compatible models).** Two models $M$ and $N$ of $A$ are *compatible* if there are a model $W$ of $A$ and open immersions $g : W \to M$ and $h : W \to N$, compatible with the maps $j$, such that $(g, h) : W \to M \times_R N$ is a closed immersion.

Lean: `GlobalTheory.SS.Compat`.

Compatible models can be glued along $W$, and the closed immersion makes the result separated.

### Inputs

We use these results. In each, $M$ is a model of $A$.

**Theorem 6.17.3 (Weak Néron models exist).** Let $R$ be a discrete valuation ring with perfect residue field and let $A$ be smooth, proper and projective over $K$. Then $A$ has a weak Néron model of finitely many irreducible models.

Lean: `GlobalTheory.T.exists_weak_neron_model`.

**Theorem 6.17.4 (Strict laws exist).** If $R$ is strictly Henselian and $M$ has a birational group law, then there is a model $N \leq M$ with a strict birational group law.

Lean: `GlobalTheory.T.exists_strict_model_of_birational`.

**Theorem 6.17.5 (The law at a point).** If $R$ is strictly Henselian and $M$ is strict, then for each point $z$ of $M \times M$ there is a $K$-point $a$ such that $\tau_a$ is a generic isomorphism from $M$ to $M$ and the multiplication of $A$ is defined at $z$ as a map from $M \times M$ to the twist of $M$ by $\tau_a$.

Lean: `GlobalTheory.T.modelGroupLaw_definedAt_translate`.

**Theorem 6.17.6 (Translates are compatible).** If $R$ is strictly Henselian, $M$ is strict, and $\tau_a$ and $\tau_b$ are generic isomorphisms from $M$ to $M$, then the twists of $M$ by $\tau_a$ and by $\tau_b$ are compatible.

Lean: `GlobalTheory.T.strictModel_translates_twist_compatible`.

**Theorem 6.17.7 (Gluing).** Let $R$ be a discrete valuation ring and let $M_0, \dots, M_n$ be pairwise compatible models of $A$. Then there is a model $G$ with $M_i \leq G$ for all $i$, such that every point of $G$ lies in the image of one of the open immersions $M_i \to G$, and such that every model compatible with all $M_i$ is compatible with $G$.

Lean: `GlobalTheory.T.exists_glue_finitely_many_compatible_smoothModels`.

**Theorem 6.17.8 (Extension of maps).** Let $R$ be a discrete valuation ring, let $M$ and $N$ be models of $A$ and $A'$, and let $f : A \to A'$. If $f$ is defined at every point of $M$, then $f$ extends to a unique map $M \to N$.

Lean: `GlobalTheory.T.existsUnique_model_extension_of_definedAtPoints` (also `GlobalTheory.SS.existsUnique_extension_of_forall_defAt`, the same statement).

**Theorem 6.17.9 (Translation by a section).** Let $R$ be strictly Henselian and $M$ strict, and let $s$ be an $R$-point of $M$. Then there is a $K$-point $a$ of $A$ with $j \circ a = s$ on the generic fibre, such that $\tau_a$ is a generic isomorphism from $M$ to $M$. If a shear is an isomorphism at $(s, y)$, then $\tau_a$ or $\tau_a^{-1}$, respectively, is an isomorphism at $y$.

Lean: `GlobalTheory.SS.SectionTranslation.translation_by_section`.

**Theorem 6.17.10 (Groups from a dense open set).** Let $Z$ be an integral scheme, $j : U \to Z$ an open immersion with $U$ nonempty, $G$ smooth and separated over $Z$, and $A$ a commutative group scheme over $U$ that is the pullback of $G$. If the multiplication, the inverse and the unit of $A$ extend to maps $m$, $i$ and $e$ for $G$, then they make $G$ a commutative group scheme over $Z$ with pullback $A$.

Lean: `GlobalTheory.grpObj_of_dense_open`.

### Lemmas

**Lemma 6.17.11 (Sections through a set).** Let $R$ be strictly Henselian and let $S$ be a locally closed set of points of $M$ that meets the special fibre. Then $M$ has an $R$-point whose closed point lies in $S$.

Lean: `GlobalTheory.SS.exists_section`.

*Proof.* The special fibre of $M$ is of finite type over the algebraically closed residue field, so it is a Jacobson scheme, and the nonempty locally closed set $S$ meets it in a closed point $x$. The residue field at $x$ is the residue field of $R$. Since $M$ is smooth and $R$ is Henselian, the rational point $x$ of the special fibre lifts to an $R$-point. $\square$

**Lemma 6.17.12 (Sections agree).** If $Y$ is separated over $R$, two $R$-points of $Y$ that agree on the generic point are equal.

Lean: `GlobalTheory.SS.ext_section`.

**Lemma 6.17.13 (Irreducible unions).** Let $S \subset X$ and let $(U_i)$ be open sets that cover $S$, with each $S \cap U_i$ preirreducible. If $S \cap U_i \cap U_{i_0}$ is not empty for every $i$, then $S$ is irreducible.

Lean: `GlobalTheory.SS.FinUnion.irr_union`.

*Proof.* Each $S \cap U_i$ is preirreducible and meets the open set $U_{i_0}$, so it lies in the closure of $S \cap U_i \cap U_{i_0}$. Hence $S$ lies in the closure of the irreducible set $S \cap U_{i_0}$. $\square$

**Lemma 6.17.14 (Translates inside the union).** Let $R$ be a discrete valuation ring, let $M$ be strict, and let $m : M \times M \to G$ extend the multiplication. If $\tau_a$ is a generic isomorphism from $M$ to $M$ and the twist $M_a$ of $M$ by $\tau_a$ is compatible with $G$, then $M_a \leq G$.

Lean: `GlobalTheory.SS.FinUnion.le_of_law`.

*Proof.* Let $W$, $g : W \to M_a$ and $h : W \to G$ give the compatibility. It suffices to show that $g$ is surjective. Points of the generic fibre lie in the image of $j$. Let $y$ be in the special fibre. Strictness gives a point $z$ of $M \times M$ with second coordinate $y$ where the second shear is an isomorphism, and we may move $z$ so that its first coordinate lies where $\tau_a$ is an isomorphism. Near $z$, the map $(u, v) \mapsto m(\tau_a(u), u^{-1} v)$ is defined, and on the generic fibre it equals $\tau_a(v)$, since $a u \cdot u^{-1} v = a v$. So the map from $M_a$ to $G$ given by $j$ extends near $y$. Its graph and the closed graph of $(g, h)$ agree on a dense open set, so $y$ lies in the image of $g$. $\square$

**Lemma 6.17.15 (Translates meet).** If $\tau_a$ is a generic isomorphism from $M$ to $M$, and $M$ and its twist by $\tau_a$ map to $G$ by maps compatible with $j$, then the images of the two maps meet in the special fibre of $G$.

Lean: `GlobalTheory.SS.FinUnion.meet`.

*Proof.* Let $\tau_a$ be an isomorphism on an open set $V$ that meets the special fibre. The two maps $V \to G$, one through the twist and one through $\tau_a$ and $M$, agree on the generic fibre of $V$, which is dense in $V$. Since $G$ is separated, they agree on $V$. So a special point of $V$ has the same image under both. $\square$

### The union of translates

**Theorem 6.17.16 (Union of translates).** Let $R$ be strictly Henselian with fraction field $K$, let $A$ be a commutative abelian scheme over $K$, and let $M$ be a model of $A$ with a strict birational group law. Then there is a model $G$ of $A$ with these properties.

1. $G$ is irreducible.
2. For each $K$-point $a$ such that $\tau_a$ is a generic isomorphism from $M$ to $M$, the twist of $M$ by $\tau_a$ satisfies $M_a \leq G$.
3. Each point of $G$ lies in the image of an open immersion $M_a \to G$, compatible with $j$, for such an $a$.
4. The multiplication of $A$ is defined at every point of $M \times M$ as a map to $G$.

Lean: `GlobalTheory.T.exists_union_translates'` (also `GlobalTheory.SS.exists_union_translates`, a second name).

*Proof.* For each point $z$ of $M \times M$, the theorem on the law at a point gives $a_z$ such that the multiplication is defined at $z$ into $M_{a_z}$, on an open set $U_z$. The model $M \times M$ is quasi-compact, so finitely many $U_z$ cover it. Let $b_0 = 1$ and let $b_1, \dots, b_n$ be the corresponding $a_z$. All $\tau_{b_i}$ are generic isomorphisms of $M$; for $b_0$ this holds because the special fibre is not empty. The twists $M_{b_i}$ are pairwise compatible, and the gluing theorem gives $G$.

Property 4 holds because the multiplication is defined into $M_{b_i}$ on $U_z$, and $M_{b_i} \leq G$. The theorem on extension of maps gives $m : M \times M \to G$ that extends the multiplication. For property 2, the twist $M_a$ is compatible with each $M_{b_i}$, hence with $G$, and the lemma on translates inside the union gives $M_a \leq G$. Property 3 follows from the covering property of the gluing.

For property 1, the special fibre of $G$ is covered by the open images of the special fibres of the $M_{b_i}$. Each image is irreducible, since $M$ is irreducible. By the lemma on translates that meet, each image meets the image of $M_{b_0} = M$. The lemma on irreducible unions gives property 1. $\square$

### The group scheme

**Theorem 6.17.17 (Group scheme from a strict law).** Let $R$ be strictly Henselian with fraction field $K$, let $A$ be a commutative abelian scheme over $K$, and let $M$ be a model of $A$ with a strict birational group law. Then there is a model $G$ of $A$ with a group structure such that $G$ is commutative, smooth, separated, quasi-compact and geometrically connected, the isomorphism of the generic fibre with $A$ is a homomorphism, and every $K$-point $a$ such that $\tau_a$ is a generic isomorphism from $M$ to $M$ extends to an $R$-point of $G$.

Lean: `GlobalTheory.T.exists_grpObj_of_strictBirationalLaw` (also `GlobalTheory.SS.exists_grpObj_of_strict`, a second name).

*Proof.* Let $G$ be the union of translates. Let $H$ be the set of $K$-points $a$ such that $\tau_a$ is a generic isomorphism from $M$ to $M$. By the calculus of generic isomorphisms, $H$ is a subgroup. For $a \in H$ there is an open immersion $g_a : M \to G$ with $g_a \circ j = j \circ \tau_a$.

*Translations.* For $c \in H$, the translation $\tau_c$ is defined at each point $y = g_a(x)$ of $G$, through $g_{ac} \circ g_a^{-1}$. So $\tau_c$ extends to $G$.

*Multiplication.* A point of $G \times G$ has the form $(g_a(x), g_b(x'))$. Near it, the multiplication is $g_{ab} \circ \mu \circ (g_a \times g_b)^{-1}$ followed by the translation, and $\mu$ is defined on $M \times M$ into $G$. So the multiplication extends to $m : G \times G \to G$.

*Points.* Let $a \in H$. The lemma on sections through a set gives an $R$-point $s$ of $M$. The theorem on translation by a section gives $c \in H$ with $j \circ c = s$ generically. Then $g_{ac^{-1}} \circ s$ is an $R$-point of $G$ that extends $a$.

*Inverse.* Assume that the inverse is not defined at a point $y$ of $G$. Then $y$ is in the special fibre, and $y = g_a(x)$ with $x$ special. The set of points where the inverse is defined is open. The lemma on sections through a set gives an $R$-point $s$ of $M$ through the closed set where the inverse is not defined after $g_a$, and an $R$-point $u$ through the open set where the inverse is defined on $M$, which meets the special fibre by the birational group law. Let $c$ and $d$ be the points of the theorem on translation by a section for $s$ and $u$, and let $e = a c d^{-1}$. Then $g_e \circ u = g_a \circ s$, by the lemma on sections that agree. So the inverse is defined at the closed point of $g_a \circ s$, since it is defined at the closed point of $u$ and the translations extend. This is a contradiction.

*Group.* The point $1$ is in $H$, so the unit extends. The generic fibre is a dense open set of $G$, and the theorem on groups from a dense open set gives a commutative group structure. The special fibre of $G$ is irreducible and $A$ is geometrically connected, so $G$ is geometrically connected. The isomorphism of the generic fibre with $A$ is a homomorphism because the structure is the one of $A$ there. $\square$

### The neutral group model

**Theorem 6.17.18 (Neutral group model).** Let $R$ be strictly Henselian with fraction field $K$, and let $A$ be a commutative abelian scheme over $K$ that is projective. Then there are a model $G$ of $A$ with a group structure and an integer $c \geq 1$ such that $G$ is commutative, smooth, separated, quasi-compact and geometrically connected, the isomorphism of the generic fibre with $A$ is a homomorphism, and $a^c$ extends to an $R$-point of $G$ for every $K$-point $a$ of $A$.

Lean: `GlobalTheory.SS.exists_neutral_group_model`.

*Proof.* The residue field is algebraically closed, hence perfect. So $A$ has a weak Néron model of irreducible models. The theorem on a birational group law gives a model $N$ with a birational group law and $c \geq 1$ such that $\tau_{a^c}$ is a generic isomorphism of $N$ for all $a$. The theorem on strict laws gives $N' \leq N$ with a strict law. The theorem on groups from a strict law gives $G$.

It remains to show that $\tau_{a^c}$ is a generic isomorphism of $N'$. Since $N'$ is irreducible and $N' \leq N$, the identity is a generic isomorphism from $N'$ to $N$, and by the calculus also from $N$ to $N'$. Composing, $\tau_{a^c}$ is a generic isomorphism from $N'$ to $N'$. So $a^c$ extends to an $R$-point of $G$. $\square$

**Remark 6.17.19 (Formalization).** The theorems are in [ExistsUnionTranslates.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ExistsUnionTranslates.lean#L302), [ExistsGrpObjOfStrictBirationalLaw.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ExistsGrpObjOfStrictBirationalLaw.lean#L247) and [ExistsNeutralGroupModel.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ExistsNeutralGroupModel.lean#L18). The first names of the first two are `first | exact ...` wrappers in the files with the suffix `Statement`. The wrapper for the union of translates carries a prime, and there is no version of that name without it. The name of the last theorem says "neutral", but the statement has no neutral component: $G$ itself is geometrically connected.
