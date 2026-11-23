---
title: A smooth quotient and the descent datum
decls:
  - GlobalTheory.Mum.exists_near_galois_quotient
  - GlobalTheory.Mum.descend_of_near
  - GlobalTheory.T.exists_descentDatum_of_descendedMultiplication
  - GlobalTheory.Mum.Desc.exists_datum
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A smooth quotient and the descent datum

This section proves two results on smooth models near the closed fibre, in the sense of [the section on descent to the base](/entry/mum-exists-near/). The first result says that a semi-abelian scheme with a model of this kind over a proper surjective cover of $\operatorname{Spec} R$ descends to a semi-abelian scheme over $R$. It is used in [Mumford's construction](/entry/has-of-base/) and in [the Galois descent theorem](/entry/has-of-galois-action/). The second result builds such a model from a Galois action, by a quotient of an invariant open subset; the Galois descent theorem uses it as its first step. The heart of the first result is a descent datum for the group scheme, which we build from the model with an argument on effective epimorphisms.

### The descent datum

Throughout, $R$ is a local domain, $\pi : S \to \operatorname{Spec} R$ is a morphism and $G'$ is a group scheme over $S$. Let $p_1, p_2 : S \times_R S \to S$ be the two projections, and let $p_1^* G'$ and $p_2^* G'$ be the base changes of $G'$ along them. A point of $p_i^* G'$ with values in $T$ is a pair of a point $t$ of $S \times_R S$ and a point of $G'$ over $p_i(t)$.

**Definition 4.14.1 (Descent datum for a smooth model).** Let $(U, u)$ be a smooth model of $G'$ near the closed fibre. A *descent datum* for $(U, u)$ is an isomorphism $\varphi : p_1^* G' \cong p_2^* G'$ of schemes over $S \times_R S$ with these two properties.

1. $\varphi$ is a homomorphism of group schemes.
2. Let $T$ be a scheme, $a : T \to U$ a morphism and $x$ a $T$-point of $p_1^* G'$, with image $t$ in $S \times_R S$. If $u$ carries $(a, p_1(t))$ to the point $x$ of $G'$, then $u$ carries $(a, p_2(t))$ to the point $\varphi(x)$ of $G'$.

Lean: `GlobalTheory.Mum.Near.Datum`.

Here "$u$ carries $(a, s)$ to $x$" means that $(a, s)$ is a point of $U \times_R S$ and $u(a, s) = x$. So condition 2 says that $\varphi$ is the identity on the model: a point $u(a, s_1)$ goes to $u(a, s_2)$. Since the model is defined over $R$, it has a canonical descent datum, and $\varphi$ extends it. The cocycle condition on triple products is not part of the definition.

We use two schemes built from the model. Let
$$
U_T = U \times_R (S \times_R S),
$$
a scheme over $S \times_R S$. For $i = 1, 2$, let $e_i : U_T \to p_i^* G'$ send $(a, t)$ to $u(a, p_i(t))$, and let
$$
\Sigma_i : U_T \times_{S \times_R S} U_T \to p_i^* G', \qquad (a, b, t) \mapsto e_i(a, t) \cdot e_i(b, t).
$$
So $\Sigma_i$ is the product of two points of the model, read in $G'$ over $p_i(t)$.

**Theorem 4.14.2 (Descent datum from the multiplication).** Let $R$ be an admissible base, $S$ an integral scheme and $\pi : S \to \operatorname{Spec} R$ a proper surjective morphism. Let $G'$ be a commutative semi-abelian scheme over $S$ and $(U, u)$ a smooth model of $G'$ near the closed fibre to which the multiplication descends. Then $(U, u)$ has a descent datum.

Lean: `GlobalTheory.Mum.Desc.exists_datum` (also `GlobalTheory.T.exists_descentDatum_of_descendedMultiplication`, a second name).

*Proof.* *Step 1: the sum maps are covers.* For $i = 1, 2$ the map $\Sigma_i$ is flat, surjective and quasi-compact. This is an input that we did not open. Its idea is that $u$ is an open immersion onto a neighbourhood of the closed fibre, and every point of a fibre of a semi-abelian scheme over a proper base is a product of two points of such a neighbourhood. Hence $\Sigma_1$ and $\Sigma_2$ are effective epimorphisms in the category of schemes, since a faithfully flat quasi-compact morphism is one.

*Step 2: equal kernel pairs.* Let $g, g' : T \to U_T \times U_T$ be two morphisms with $\Sigma_1 \circ g = \Sigma_1 \circ g'$. Then $\Sigma_2 \circ g = \Sigma_2 \circ g'$. The same holds with $1$ and $2$ exchanged. This is a second input, which uses the descended multiplication: the products $e_1(a) e_1(b)$ and $e_2(a) e_2(b)$ are both $u$ of the descended product $m(a, b)$ when $(a, b)$ lies in its domain.

*Step 3: the maps.* By Steps 1 and 2 and the universal property of effective epimorphisms, there are unique morphisms $f : p_1^* G' \to p_2^* G'$ and $h : p_2^* G' \to p_1^* G'$ with $f \circ \Sigma_1 = \Sigma_2$ and $h \circ \Sigma_2 = \Sigma_1$.

*Step 4: isomorphism over the base.* Since $\Sigma_1$ is an epimorphism, two morphisms out of $p_1^* G'$ that agree after composition with $\Sigma_1$ are equal. Now $(h \circ f) \circ \Sigma_1 = h \circ \Sigma_2 = \Sigma_1$, so $h \circ f = 1$. In the same way $f \circ h = 1$, and $f$ commutes with the maps to $S \times_R S$. So $f$ is an isomorphism over $S \times_R S$.

*Step 5: $f$ fixes the model.* From $f \circ \Sigma_1 = \Sigma_2$, a third input gives $f \circ e_1 = e_2$.

*Step 6: homomorphism.* A fourth input shows that a morphism with $f \circ \Sigma_1 = \Sigma_2$ and $f \circ e_1 = e_2$ is a homomorphism of group schemes.

*Step 7: condition 2.* Let $a$ and $x$ be as in condition 2, and let $(a, t)$ be the point of $U_T$ with $t$ the image of $x$. The hypothesis says $e_1(a, t) = x$. By Step 5, $f(x) = f(e_1(a, t)) = e_2(a, t) = u(a, p_2(t))$. So $f$ is a descent datum. $\square$

Step 7 is a formal computation with pullbacks. The real content of the proof is in the four inputs. Steps 3 and 4 are the standard construction of a morphism out of an effective epimorphism.

### Descent from a smooth model

**Theorem 4.14.3 (Descent from a smooth model).** Let $R$ be an admissible base, $S$ an integral scheme and $\pi : S \to \operatorname{Spec} R$ a proper surjective morphism. Let $G'$ be a commutative semi-abelian scheme over $S$ and $(U, u)$ a smooth model of $G'$ near the closed fibre to which the multiplication descends. Then there are a commutative group scheme $G$ over $\operatorname{Spec} R$, a morphism $\beta : G' \to G$ and a morphism $i : U \to G$ over $\operatorname{Spec} R$ with these properties.

1. $G$ is semi-abelian.
2. $\beta$ makes $G'$ the group pullback of $G$ along $\pi$.
3. $i$ is an open immersion.
4. $\beta \circ u = i \circ \mathrm{pr}_1$ as morphisms $U \times_R S \to G$.

Lean: `GlobalTheory.Mum.descend_of_near` (also `GlobalTheory.T.semiAbelian_descends_of_descends_near_closedFibre`, a second name).

*Proof.* *Step 1: the descent datum.* The previous theorem gives a descent datum $\varphi$ for $(U, u)$.

*Step 2: the scheme.* By an input on descent near the closed fibre, there are a scheme $G$ smooth over $R$, a morphism $\beta : G' \to G$ and a morphism $i : U \to G$ over $R$ with these properties: the square formed by $\beta$, $\pi$ and the structure maps is a pullback square; $i$ is an open immersion; $\beta \circ u = i \circ \mathrm{pr}_1$; and $\beta \circ \mathrm{pr} = \beta \circ \mathrm{pr} \circ \varphi$ as maps $p_1^* G' \to G$, where $\mathrm{pr} : p_i^* G' \to G'$ are the projections. In words, $G$ is obtained by gluing the image of $U$ with the descent of $G'$ along $\varphi$, and $\beta$ is invariant under $\varphi$.

*Step 3: the group structure.* By an input on descent along proper surjective morphisms, a smooth scheme $G$ with these properties carries a commutative group structure that makes $G$ semi-abelian and makes $\beta$ a group pullback along $\pi$. This input uses that $\varphi$ is a homomorphism.

The morphisms $\beta$ and $i$ of Step 2, with the group structure of Step 3, have properties 1 to 4. $\square$

In the theorem the group $G$ is not built from the multiplication on the model directly. The model gives only the neighbourhood of the closed fibre; the descent datum gives all of $G$, and the group law comes from the group law of $G'$ through the descent.

### A smooth quotient by a Galois action

In the next theorem we are in the situation of [the section on Galois descent](/entry/has-of-galois-action/), without the group $G$. So $R$ is a base, $\rho : R \to R'$ is a finite Galois extension, $D'$ is a pullback of degeneration data $D$ over $R$, $G'$ is a commutative semi-abelian scheme over $R'$, $U'$ is a uniformisation of $(A', G')$ by $D'$, and $(a_\sigma)$ is a Galois action on $U'$.

**Theorem 4.14.4 (Smooth quotient near the closed fibre).** In this situation there is a smooth model $(U, u)$ of $G'$ near the closed fibre, over $\operatorname{Spec} \rho : \operatorname{Spec} R' \to \operatorname{Spec} R$, with these properties.

1. The multiplication of $G'$ descends to the model.
2. Let $\sigma \in \operatorname{Gal}(\rho)$, let $T$ be a scheme, $s : T \to \operatorname{Spec} R'$, $v : T \to U$ and $x$ a $T$-point of $G'$. If $u$ carries $(v, s)$ to $x$, then $u$ carries $(v, \operatorname{Spec} \sigma \circ s)$ to $a_\sigma(x)$.

Lean: `GlobalTheory.Mum.exists_near_galois_quotient`.

*Proof.* *Step 1: an invariant neighbourhood.* By an input, there is an open subset $H \subseteq G'$ that contains every point over the closed point of $\operatorname{Spec} R$, with $a_\sigma(H) = H$ for all $\sigma$, such that every orbit of the Galois group in $H$ lies in an affine open subset.

*Step 2: the quotient.* By a second input, there are a scheme $X$ over $R$ and a morphism $q : H \to X$ over $\operatorname{Spec} \rho$ with these properties. The map $q$ is affine and surjective, and $q \circ a_\sigma = q$ on $H$ for all $\sigma$. Two points of $H$ with the same image are in one orbit. For every open $V \subseteq X$, the pullback of functions $q^*$ on $V$ is injective, and its image is the set of functions on $q^{-1}(V)$ fixed by every $a_\sigma$. So $X$ is the quotient $H / \operatorname{Gal}(\rho)$.

*Step 3: smoothness near the closed fibre.* By a third input, every point $x \in H$ over the closed point of $\operatorname{Spec} R$ has an affine open neighbourhood $V$ of $q(x)$ in $X$ such that $V$ is smooth over $R$ and the map $q^{-1}(V) \to V \times_R \operatorname{Spec} R'$ is an isomorphism. Here one uses that the Galois group acts on $\operatorname{Spec} R'$ through $\rho$, so the quotient of a base change is the original scheme.

*Step 4: gluing.* By a fourth input, the opens $V$ of Step 3 glue to a smooth model $(U, u)$ of $G'$ near the closed fibre with property 2. The model $U$ is the union of these opens in $X$, and $u$ is the inverse of the isomorphisms of Step 3.

*Step 5: the multiplication.* By a fifth input, the multiplication of $G'$ descends to this model. Its idea is that the multiplication is equivariant, so it induces a morphism on invariant functions near the closed fibre. $\square$

**Remark 4.14.5 (Formalization).** In the descent datum theorem ([ExistsDescentDatumOfDescendedMultiplication.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsDescentDatumOfDescendedMultiplication.lean#L50)), the schemes $U_T$ and the maps $e_i$, $\Sigma_i$ are `GlobalTheory.Mum.Desc.UT`, `GlobalTheory.Mum.Desc.emb` and `GlobalTheory.Mum.Desc.sum`, and Step 7 is `GlobalTheory.Mum.Desc.pt_of_fix`. The inputs of Steps 1, 2, 5 and 6 are `GlobalTheory.T.nearOpen_sumMap_flat_surjective_quasiCompact`, `GlobalTheory.T.kernelPair_sum_eq_of_sum_eq_other_pullback`, `GlobalTheory.T.nearOpenEmbedding_comp_of_sumMap_comp` and `GlobalTheory.T.isMonHom_of_sumMap_comp_fixing_nearOpen`, and Step 3 uses `EffectiveEpi.desc`. In the theorem on descent from a smooth model ([SemiAbelianDescendsOfDescendsNearClosedFibre.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SemiAbelianDescendsOfDescendsNearClosedFibre.lean#L14)), Steps 2 and 3 are `GlobalTheory.T.semiAbelian_descends_near_closedFibre` and `GlobalTheory.T.exists_semiAbelian_descent_along_proper_surjective`; the facts that $R$ is noetherian and integrally closed are extracted at lines 20 and 21 and not used. The second name of this theorem is a wrapper that is not in the outline of the chapter. In the last theorem ([ExistsNearGaloisQuotient.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsNearGaloisQuotient.lean#L19)), Steps 1 to 5 are `GlobalTheory.T.exists_galois_invariant_nbhd_closedFibre`, `GlobalTheory.T.exists_galois_quotient_invariant_open`, `GlobalTheory.T.galoisQuotient_smooth_baseChange_iso_closedFibre`, `GlobalTheory.T.glue_local_descents_near_closedFibre_galois` and `GlobalTheory.T.groupLaw_descends_galois_invariant_open`. We did not open the proofs of any of these inputs, and the reasons given for them are sketches. A smooth model is the structure `GlobalTheory.Mum.Near`, and "$u$ carries $(a, s)$ to $x$" is `GlobalTheory.Mum.Near.Pt`.
