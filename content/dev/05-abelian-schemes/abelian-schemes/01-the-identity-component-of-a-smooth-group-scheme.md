---
title: The identity component of a smooth group scheme
decls:
  - GlobalTheory.identityComponentOpen
  - GlobalTheory.T.isOpen_identityComponents_smooth_groupScheme
  - GlobalTheory.IdCompOpen.isOpen_identityComponent
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The identity component of a smooth group scheme

Let $G$ be a [[smooth|EXKGG9X6J0]] group scheme over a scheme $S$. In each fibre $G_s$ the connected component of the unit is a subgroup. This section proves that the union of these components is an open subscheme of $G$, and that it is a group scheme over $S$ (Theorem (Identity component)). The proof first shows that the union is open (Proposition (Openness)), and then applies a criterion for open subgroups. The result is an input of [EveryCharacter from Row0b](/step/every-character-of-row/), through two results on group schemes with geometrically connected fibres.

We work with group objects in the category of $S$-schemes. A *group* over $S$ is an $S$-scheme $G$ with a group structure on each set $G(Y)$ of $S$-morphisms $Y \to G$, natural in $Y$. Its unit is a section $e : S \to G$, its multiplication is $m : G \times_S G \to G$, and its inverse is $i : G \to G$. A *homomorphism* of groups is an $S$-morphism that is a group homomorphism on $Y$-points for each $Y$. We write $f : G \to S$ for the structure map. For a point $x$ of the underlying space of $G$, the fibre $f^{-1}(f(x))$ is a subspace of $G$, with the subspace topology. It is homeomorphic to the underlying space of the scheme fibre $G_{f(x)}$.

**Definition 1.1.1 (Identity component).** Let $f : X \to S$ be a morphism of schemes and $e : S \to X$ a section of $f$. The *component set of $e$* is
$$Z(f, e) = \{x \in X : x \text{ lies in the connected component of } e(f(x)) \text{ in } f^{-1}(f(x))\}.$$
For a group $G$ over $S$ with unit $e$, we write $G^0 = Z(f, e)$ and call it the *identity component* of $G$. Its intersection with the fibre over $s$ is the connected component of $e(s)$ in $f^{-1}(s)$.

For each $s \in S$ the point $e(s)$ lies in $G^0$, because $f(e(s)) = s$ and each point lies in its own connected component. If $G$ is an [[abelian scheme|JDDXZ89N33]], then the fibres are connected and $G^0 = G$. If $G = \mu_n$ over $\mathrm{Spec}\, \mathbb{Z}[1/n]$, the fibres are finite and discrete, and $G^0$ is the image of the unit section.

The classical statement is in SGA 3: if $G$ is smooth over $S$, the functor of the identity components of the fibres is represented by an open subgroup scheme of $G$ (M. Demazure and A. Grothendieck, *Schémas en groupes I*, Lecture Notes in Math. 151, Exposé VI_B, §3). We prove the form that follows.

**Theorem 1.1.2 (Identity component).** Let $S$ be a scheme and $G$ a group over $S$ with $f : G \to S$ smooth. Then there are a group $G_0$ over $S$ and a homomorphism $j : G_0 \to G$ such that $j$ is an open immersion and the image of $j$ is $G^0$.

Lean: `GlobalTheory.identityComponentOpen`.

We use eight facts. The first three are on a smooth morphism $f : X \to S$ with a section $e$, or on any scheme.

1. (Openness criterion.) Let $X$ be a scheme and $Z \subseteq X$ a set that is stable under generalization. Suppose that each $x \in Z$ has open sets $W \subseteq W'$ of $X$ and a finite set $J$ of sections of $\mathcal{O}_X$ over $W'$ such that $x \in W \cap V(J)$ and $W \cap V(J) \subseteq Z$. Here $V(J)$ is the set of points of $W'$ where all elements of $J$ vanish. Then $Z$ is open.
2. (Generalization.) If $f$ is smooth with a section $e$, then $Z(f, e)$ is stable under generalization.
3. (Irreducible neighbourhoods.) If $f$ is smooth with a section $e$, then for each $s \in S$ there are an open set $U$ of $X$, open sets $V_0 \subseteq V$ of $S$ and a finite set $I$ of sections of $\mathcal{O}_S$ over $V$, with $s \in V_0 \cap V(I)$ and $e(s) \in U$, such that $U \cap f^{-1}(t)$ is preirreducible for each $t \in V_0 \cap V(I)$.

The other five are on a group $G$ over $S$ with $f$ smooth. For an open set $U$ of $G$, let $O(U)$ be the set of points $y$ of $G$ for which there is a point $w$ of $G \times_S G$ with $p_1(w) \in U$, $m(w) \in U$ and $p_2(w) = y$. On the rational points of a fibre over an algebraically closed field, $O(U)$ is the set of $y$ such that $U$ meets $U y^{-1}$.

4. (Open translates.) For each open $U$, the set $O(U)$ is open.
5. If $e(f(y)) \in U$ and $y \in G^0$, then $y \in O(U)$.
6. If each $z \in U$ with $f(z) = f(y)$ lies in $G^0$, and $y \in O(U)$, then $y \in G^0$.
7. (Closure under products.) If $w$ is a point of $G \times_S G$ with $p_1(w), p_2(w) \in G^0$, then $m(w) \in G^0$. Inverses: if $y \in G^0$, then $i(y) \in G^0$. The second statement needs no smoothness.
8. (Open subgroups.) Let $Z \subseteq G$ be open, with $e(s) \in Z$ for each $s \in S$, with $m(w) \in Z$ for each point $w$ of $G \times_S G$ with $p_1(w), p_2(w) \in Z$, and with $i(Z) \subseteq Z$. Then there are a group $G_0$ over $S$ and a homomorphism $j : G_0 \to G$ that is an open immersion with image $Z$.

Facts 5 and 6 have a simple meaning on a fibre over an algebraically closed field. The identity component $G^0_t$ is then irreducible. If $e \in U$ and $y \in G^0_t$, the open sets $U \cap G^0_t$ and $U y^{-1} \cap G^0_t$ are not empty, since they contain $e$ and $y^{-1}$, so they meet. If $u$ and $u y$ lie in $U \cap G_t \subseteq G^0_t$, then $y = u^{-1}(u y)$ lies in $G^0_t$.

**Lemma 1.1.3 (Components along a section).** Let $f : X \to S$ be smooth and $e$ a section of $f$. Let $O$ assign to each open set $U$ of $X$ an open set $O(U)$, with these two properties. (a) If $e(f(y)) \in U$ and $y \in Z(f, e)$, then $y \in O(U)$. (b) If each $z \in U$ with $f(z) = f(y)$ lies in $Z(f, e)$, and $y \in O(U)$, then $y \in Z(f, e)$. Then $Z(f, e)$ is open in $X$.

Lean: `GlobalTheory.IdCompOpen.isOpen_sectionComponents_of_family`.

*Proof.* Put $Z = Z(f, e)$. By fact 2, $Z$ is stable under generalization, so by fact 1 it is enough to find, for each $x \in Z$, the sets $W$, $W'$ and $J$. Let $s = f(x)$ and take $U$, $V_0$, $V$, $I$ from fact 3. Put
$$W = O(U) \cap f^{-1}(V_0 \cap e^{-1}(U)), \qquad W' = f^{-1}(V),$$
and let $J$ be the set of pullbacks $f^*c$ for $c \in I$. Then $W \subseteq W'$. The point $x$ lies in $O(U)$ by property (a), since $e(s) \in U$ and $x \in Z$. It lies in $f^{-1}(V_0 \cap e^{-1}(U))$, since $s \in V_0$ and $e(s) \in U$. It lies in $V(J)$, since $s \in V(I)$. Now let $y \in W \cap V(J)$ and $t = f(y)$. Then $t \in V_0 \cap V(I)$, so $U \cap f^{-1}(t)$ is preirreducible, hence preconnected. It contains $e(t)$, since $t \in e^{-1}(U)$. So $U \cap f^{-1}(t)$ lies in the connected component of $e(t)$ in $f^{-1}(t)$, that is, each $z \in U$ with $f(z) = t$ lies in $Z$. As $y \in O(U)$, property (b) gives $y \in Z$. So $W \cap V(J) \subseteq Z$. $\square$

**Proposition 1.1.4 (Openness).** Let $S$ be a scheme and $G$ a group over $S$ with $f : G \to S$ smooth. Then $G^0$ is open in $G$.

Lean: `GlobalTheory.IdCompOpen.isOpen_identityComponent` (also `GlobalTheory.T.isOpen_identityComponents_smooth_groupScheme`, a second name).

*Proof.* Apply the lemma to $f$, the unit section $e$ and the sets $O(U)$ defined above. They are open by fact 4. Property (a) is fact 5 and property (b) is fact 6. $\square$

*Proof of the theorem.* Apply fact 8 to $Z = G^0$. It is open by the proposition. It contains $e(s)$ for each $s$, as we saw after the definition. It is closed under products and inverses by fact 7. Fact 8 gives $G_0$ and $j$, with image $G^0$. $\square$

**Remark 1.1.5 (Formalization).** The eight facts are proved elsewhere in the development and are cited here by their statements: `GlobalTheory.T.isOpen_of_stableUnderGeneralization_of_local_pieces`, `GlobalTheory.T.stableUnderGeneralization_section_connectedComponentIn`, `GlobalTheory.T.exists_open_nbhd_section_fiber_isPreirreducible`, `GlobalTheory.T.isOpen_snd_image_mul_mem_open_groupScheme`, `GlobalTheory.T.mem_mul_preimage_of_mem_unitComponent`, `GlobalTheory.T.mem_unitComponent_of_mul_mem`, `GlobalTheory.T.identityComponents_smooth_groupScheme_mul_mem`, `GlobalTheory.T.inv_mem_identity_component_fibre` and `GlobalTheory.T.exists_openSubgroupScheme_of_isOpen_stable`. The statement that is proved is `GlobalTheory.Published.IdentityComponentOpen`; it asks that $j$ be a monoid homomorphism and an open immersion with the given image, and it is stated with `connectedComponentIn` of the preimage $f^{-1}\{f(x)\}$ in $G$, not with the scheme fibre. The second name is closed by a `first` list of three tactics under `set_option maxHeartbeats 1000000` ([IsOpenIdentityComponentsSmoothGroupSchemeStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsOpenIdentityComponentsSmoothGroupSchemeStatement.lean#L5)). The theorem is used in ExistsBasicOpenGeometricallyConnectedFibresOfGen.lean, line 73, and ExistsLocalGroupRangeUnionClosedFibres.lean, line 109.
