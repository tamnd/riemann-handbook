---
title: Weak Néron models and members of maximal order
decls:
  - GlobalTheory.T.exists_automorphism_permutation_maxOrder_members
  - GlobalTheory.SS.exists_permuted_members
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Weak Néron models and members of maximal order

This section starts the third part of the chapter, on smooth group models of abelian varieties over a strictly Henselian discrete valuation ring. A weak Néron model is a finite family of smooth models such that every unramified point extends to one of them. We attach to each member an integer, its Jacobian order, and we prove that the members of maximal order are permuted by all automorphisms of the abelian variety and of its square. This result is the basis of the birational group law in the next section, which is the first step of [the neutral group model](/entry/exists-neutral-group-model/), which enters the main proof at [the step on every character](/step/every-character/). We follow the method of Bosch, Lütkebohmert and Raynaud; for the background see [Néron models and good reduction](/learn/abelian-varieties/#neron-models-and-good-reduction) in Volume 1.

### Models

Let $R$ be a local domain with fraction field $K$. We say that $R$ is *strictly Henselian* if it is a discrete valuation ring, it is Henselian, and its residue field is algebraically closed. Let $A$ be a scheme over $K$.

**Definition 6.15.1 (Model).** A *model* $M$ of $A$ over $R$ is a scheme $Y$ over $\operatorname{Spec} R$ that is smooth, separated and quasi-compact, with an isomorphism $e : Y_K \cong A$. We write $j : A \to Y$ for the composite of $e^{-1}$ and the inclusion of the generic fibre. The *special fibre* of $M$ is the set of points of $Y$ over the closed point of $R$, and $M$ is *irreducible* if its special fibre is irreducible. For an isomorphism $f : A \cong A'$, the *twist* of $M$ by $f$ is the model of $A'$ with the same $Y$ and the isomorphism $f \circ e$. The *product* of models of $A$ and $A'$ is the model of $A \times A'$ on $Y \times_R Y'$.

Lean: `GlobalTheory.SS.Model` (also `GlobalTheory.SS.Model.twist`, twists; `GlobalTheory.SS.Model.prod`, products; `GlobalTheory.SS.Model.Irr`, irreducible).

**Definition 6.15.2 (Generic isomorphism).** Let $M$ and $N$ be models of $A$ and $A'$ and let $f : A \to A'$. A map $g : U \to N$ from an open set $U \subset M$ *extends* $f$ if it is a map over $R$ and $g \circ j = j \circ f$ on the generic fibre of $U$. The map $f$ is *defined at* a point $y$ of $M$ if some $g$ on a neighbourhood of $y$ extends $f$. It is an *isomorphism at* $y$ if $g$ can be taken to be an open immersion. It is a *generic isomorphism* from $M$ to $N$ if it is an isomorphism at some point of the special fibre of $M$. For two models $M$ and $N$ of $A$, we write $M \leq N$ if there is an open immersion $M \to N$ over $R$ compatible with the maps $j$.

Lean: `GlobalTheory.SS.GenIso` (also `GlobalTheory.SS.DefAt`, defined at; `GlobalTheory.SS.IsoAt`, isomorphism at; `GlobalTheory.SS.Model.Le`, open immersions).

**Definition 6.15.3 (Weak Néron model).** A family $(M_i)_{i \in I}$ of models of $A$ is a *weak Néron model* if this holds: for every discrete valuation ring $R'$ over $R$ with $\mathfrak{m}_R R' = \mathfrak{m}_{R'}$ and fraction field $K'$, every $K'$-point of $A$ extends to an $R'$-point of some $M_i$.

Lean: `GlobalTheory.SS.WeakNeron`.

**Lemma 6.15.4 (Weak Néron models are not empty).** If $R$ is strictly Henselian and $(M_i)_{i \in I}$ is a weak Néron model of a group scheme $A$, then $I$ is not empty.

Lean: `GlobalTheory.SS.WeakNeron.nonempty`.

*Proof.* Apply the definition with $R' = R$ to the unit point of $A$. $\square$

### Jacobian orders

Let $A$ be smooth over $K$. A *vector field* on $A$ is a family of derivations $D_U$ of $\Gamma(U, \mathcal{O})$ over $K$, for $U \subset A$ open, that commute with restriction. For vector fields $D_1, \dots, D_g$ and functions $t_1, \dots, t_g$ on $U$, the *Jacobian* is $\det(D_i t_k)$. The family $(D_i)$ is a *frame* if $A$ is smooth of relative dimension $g$ and each point has functions $t_1, \dots, t_g$ on a neighbourhood whose Jacobian is a unit. Let $\pi$ be a uniformiser of $R$.

**Definition 6.15.5 (Jacobian order).** A model $M$ of $A$ has *Jacobian order* $n \in \mathbb{Z}$ for a frame $D$ if two conditions hold. First, for every open set $U \subset Y$ and functions $t_1, \dots, t_g$ on $U$, the Jacobian of the $t_k \circ j$ equals $\pi^n s \circ j$ for a function $s$ on $U$. Second, for some $U$ that meets the special fibre and some $t_k$, this holds with $s$ a unit.

Lean: `GlobalTheory.SS.HasOrd` (also `GlobalTheory.SS.VF`, vector fields; `GlobalTheory.SS.IsFrame`, frames).

### Inputs

In the next five theorems $R$ is a discrete valuation ring with fraction field $K$ and uniformiser $\pi$, $A$ is an integral scheme over $K$ and $D$ is a frame on $A$.

**Theorem 6.15.6 (Frames exist).** If $A$ is a commutative group scheme over $K$, smooth of relative dimension $g$, then $A$ has a frame of $g$ vector fields.

Lean: `GlobalTheory.T.exists_vectorFieldFrame_smooth_commGrpScheme`.

**Theorem 6.15.7 (Orders exist).** Every irreducible model has exactly one Jacobian order.

Lean: `GlobalTheory.T.existsUnique_modelHasJacobianOrder`.

**Theorem 6.15.8 (Maps into the family).** If $(M_i)$ is a weak Néron model and $N$ is an irreducible model, then for some $i$ the identity of $A$ is defined at a point of the special fibre of $N$ as a map from $N$ to $M_i$.

Lean: `GlobalTheory.T.exists_modelMapDefined_weakNeronFamily`.

**Theorem 6.15.9 (Orders grow).** Let $M$ and $N$ be irreducible models with orders $m$ and $n$. If the identity of $A$ is defined at a point of the special fibre of $M$ as a map from $M$ to $N$, then $m \leq n$, and if $m = n$ it is a generic isomorphism from $M$ to $N$.

Lean: `GlobalTheory.T.jacobian_order_monotone_semistableModel`.

**Theorem 6.15.10 (Automorphisms shift orders).** If $A$ is an abelian scheme and $f$ is an automorphism of $A$, there is $c \in \mathbb{Z}$ such that the twist by $f$ of every model of order $n$ has order $n + c$.

Lean: `GlobalTheory.T.abelianVariety_automorphism_shifts_jacobianOrder`.

In the remaining inputs $R$ is strictly Henselian.

**Theorem 6.15.11 (Products).** Products of irreducible models are irreducible, and products of weak Néron models are weak Néron models. For frames $D$ and $D'$ on $A$ and $A'$ there is a frame on $A \times A'$ for which the product of models of orders $m$ and $n$ has order $m + n$.

Lean: `GlobalTheory.T.prod_irr_and_weakNeron'` (also `GlobalTheory.T.vectorFieldOrder_add_of_prod_strictHenselian`, orders of products).

**Theorem 6.15.12 (Calculus of generic isomorphisms).** For models over a strictly Henselian $R$:

1. if $M$ is irreducible and $M \leq N$, then the identity is a generic isomorphism from $M$ to $N$;
2. if $N$ is irreducible, $f$ is a generic isomorphism from $M$ to $N$ and $g$ one from $N$ to $P$, then $g \circ f$ is one from $M$ to $P$;
3. if an isomorphism $f$ is a generic isomorphism from $M$ to $N$, then $f^{-1}$ is one from $N$ to $M$; $f$ is one from $M$ to $N$ if and only if the identity is one from the twist of $M$ by $f$ to $N$; twists of irreducible models are irreducible;
4. products of generic isomorphisms are generic isomorphisms of the products;
5. for irreducible models, the associativity and the swap of products are generic isomorphisms.

Lean: `GlobalTheory.T.modelMapGenericallyOpenImmersion_calculus`.

### Members of maximal order

**Lemma 6.15.13 (Members of maximal order).** Let $R$ be strictly Henselian, $A$ an abelian scheme over $K$ with a frame $D$, and $(M_j)$ a weak Néron model of irreducible models with orders $o_j \leq \rho$ for all $j$. If $o_i = \rho$ and $f$ is an automorphism of $A$, then there is $i'$ with $o_{i'} = \rho$ such that $f$ is a generic isomorphism from $M_i$ to $M_{i'}$.

Lean: `GlobalTheory.SS.exists_genIso_of_max_ord`.

*Proof.* Every irreducible model $N$ of order $m$ has $m \leq \rho$, and if $m = \rho$ then the identity is a generic isomorphism from $N$ to some $M_{i'}$ of order $\rho$. Indeed, the identity is defined at a special point from $N$ to some $M_j$, so $m \leq o_j \leq \rho$, and if $m = \rho$ then $m = o_j$ and the theorem on growing orders applies.

Let $c$ and $c'$ be the shifts of $f$ and $f^{-1}$. The twist of $M_i$ by $f$ has order $\rho + c$, and twisting it back by $f^{-1}$ gives $M_i$ with order $\rho + c + c'$. By uniqueness of orders, $c + c' = 0$. The twists of $M_i$ by $f$ and $f^{-1}$ are irreducible, so $\rho + c \leq \rho$ and $\rho + c' \leq \rho$. Hence $c = 0$. So the twist of $M_i$ by $f$ has order $\rho$, and the identity is a generic isomorphism from it to some $M_{i'}$ of order $\rho$. By the calculus, $f$ is a generic isomorphism from $M_i$ to $M_{i'}$. $\square$

**Theorem 6.15.14 (Permuted members).** Let $R$ be strictly Henselian with fraction field $K$, let $A$ be a commutative abelian scheme over $K$, and let $(M_i)_{i \leq n}$ be a weak Néron model of irreducible models. Then there is a nonempty set $S$ of indices with these properties.

1. For every automorphism $f$ of $A$ and every $i \in S$ there is $i' \in S$ such that $f$ is a generic isomorphism from $M_i$ to $M_{i'}$.
2. For every automorphism $\Theta$ of $A \times A$ and all $i, j \in S$ there are $i', j' \in S$ such that $\Theta$ is a generic isomorphism from $M_i \times M_j$ to $M_{i'} \times M_{j'}$.

Lean: `GlobalTheory.T.exists_automorphism_permutation_maxOrder_members` (also `GlobalTheory.SS.exists_permuted_members`, a second name).

*Proof.* The index set is not empty. Choose a uniformiser $\pi$, let $g$ be the relative dimension of $A$, and choose a frame $D$ of $g$ vector fields. Each $M_i$ has a unique order $o_i$. Let $\rho$ be the largest order and let $S$ be the set of $i$ with $o_i = \rho$. Property 1 is the lemma on members of maximal order.

For property 2, the products $M_i \times M_j$ form a weak Néron model of $A \times A$ of irreducible models. With the product frame, $M_i \times M_j$ has order $o_i + o_j \leq 2\rho$. The lemma on members of maximal order for $A \times A$, at a pair $(i, j)$ in $S \times S$, gives $(i', j')$ with $o_{i'} + o_{j'} = 2\rho$ such that $\Theta$ is a generic isomorphism from $M_i \times M_j$ to $M_{i'} \times M_{j'}$. Since $o_{i'}, o_{j'} \leq \rho$, both are equal to $\rho$. $\square$

**Remark 6.15.15 (Formalization).** The theorem is proved in [ExistsAutomorphismPermutationMaxOrderMembers.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ExistsAutomorphismPermutationMaxOrderMembers.lean#L76), and the lemma on members of maximal order is at line 37 of that file. The first name is a `first | exact ...` wrapper in the file with the suffix `Statement`. The definitions are in [OfDerivationFnOn.lean](lean:Development/AbelianVarietyTheory/Definitions/Degenerations/OfDerivationFnOn.lean#L11). The theorem asks for the index set to be $\{1, \dots, n\}$, though only finiteness is used. The second condition of a Jacobian order asks for one open set and one family of functions with a unit quotient; it does not ask for coordinates. We did not unfold the inputs listed above.
