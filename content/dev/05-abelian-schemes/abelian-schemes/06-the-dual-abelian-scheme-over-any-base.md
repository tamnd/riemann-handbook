---
title: The dual abelian scheme over any base
decls:
  - GlobalTheory.T.abelianScheme_dual_representable_affine_base
  - GlobalTheory.DualCon.hasRep_affine
  - GlobalTheory.DualExist.hasRep_affineOpen
  - GlobalTheory.T.exists_dual_abelianScheme_poincare
  - GlobalTheory.DualExist.exists_dual
  - GlobalTheory.dualAbelianScheme
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The dual abelian scheme over any base

This section completes the construction of the dual. A limit argument moves Theorem (Finite type) of the last section to an arbitrary ring (Theorem (Affine base)), and then to an affine open set of any base scheme (Proposition (Affine open set)). Representatives over affine open sets glue to a dual of $A$ over the whole base, which is an abelian scheme of the same relative dimension (Theorem (Existence)). With biduality, this gives the main theorem of the chapter (Theorem (Dual abelian scheme)). It is the field `dual` of [the CM and abelian variety inputs](/step/cm-abelian-inputs-from-literature/), and it is used at [EveryCharacter](/step/every-character/). For the dual of an abelian variety over a field, see [Volume 1](/learn/abelian-varieties/#duality-and-the-poincar-bundle).

Let $S$ be a scheme and $A$ an [[abelian scheme|JDDXZ89N33]] over $S$. We use the notation of the earlier sections: $\mathrm{Rep}_g(A, S')$, duals, and the condition that $B$ keeps the dimension of $A$. A base change $A \times_S S_1$ of $A$ along a morphism $S_1 \to S$ is again an abelian scheme, and it is smooth of relative dimension $g$ if $A$ is. We use seven more facts.

1. (Descent to a ring of finite type.) Let $R$ be a ring and $A$ an abelian scheme over $\mathrm{Spec}\, R$, smooth of relative dimension $g$. Then there are a subring $R_0 \subseteq R$ of finite type over $\mathbb{Z}$ and an abelian scheme $A_0$ over $\mathrm{Spec}\, R_0$, smooth of relative dimension $g$, such that $A \cong A_0 \times_{R_0} R$ as groups over $\mathrm{Spec}\, R$.
2. (Locally constant dimension.) Each $s \in S$ has an affine open neighbourhood $V$ such that $A_V \to V$ is smooth of relative dimension $g$ for some $g$.
3. (Zariski gluing.) Let $(V_i)$ be an open cover of $S$ and $g_i$ integers with $\mathrm{Rep}_{g_i}(A, V_i)$ for each $i$. Then there are an $S$-scheme $B$ and a line bundle $P$ on $A \times B$ such that $(B \to S, P)$ is a representative of the dual of $A$ over $S$, and $B_{V_i} \to V_i$ is proper, smooth of relative dimension $g_i$, with geometrically connected fibres.
4. (Group structure.) If $(B \to S, P)$ is a representative of the dual of $A$ over $S$, then $B$ has a commutative group structure such that $(B, P)$ is a dual of $A$.
5. (Dimension.) Let $B$ be an $S$-scheme, suppose $A \to S$ is surjective, and let $(V_i)$ be an open cover of $S$ such that $A_{V_i}$ and $B_{V_i}$ are both smooth of relative dimension $g_i$ over $V_i$. Then $B$ keeps the dimension of $A$.
6. (Local on the target.) A morphism $B \to S$ is smooth, proper or has geometrically connected fibres if its restriction over each set of an open cover of $S$ has this property.
7. (Biduality, [Theorem 1.10.2](/entry/is-dual-abelian-scheme-poincare-swap/).) Let $A$ and $B$ be abelian schemes over $S$, such that $B$ keeps the dimension of $A$, and let $(B, P)$ be a dual of $A$. Then $(A, s^* P)$ is a dual of $B$, where $s : B \times A \to A \times B$ is the swap of factors.

Fact 1 is an application of the limit methods of EGA (A. Grothendieck, *Éléments de géométrie algébrique IV*, Part 3, Publ. Math. IHÉS 28, §8): $R$ is the union of its subrings of finite type over $\mathbb{Z}$, and $A$, its group law, and the properties smooth, proper and geometrically connected descend to one of them. Fact 4 is the Yoneda lemma: $B$ represents the functor of additive families up to isomorphism, which takes values in commutative groups under the tensor product. Fact 7 is proved in a later section.

**Theorem 1.6.1 (Affine base).** Let $R$ be a ring and $A$ an abelian scheme over $\mathrm{Spec}\, R$, smooth of relative dimension $g$. Then $\mathrm{Rep}_g(A, \mathrm{Spec}\, R)$ holds.

Lean: `GlobalTheory.DualCon.hasRep_affine` (also `GlobalTheory.T.abelianScheme_dual_representable_affine_base`, a second name).

*Proof.* Take $R_0$ and $A_0$ from fact 1. As $R_0$ is of finite type over $\mathbb{Z}$, Theorem (Finite type) gives $\mathrm{Rep}_g(A_0, \mathrm{Spec}\, R_0)$. The inclusion $R_0 \to R$ gives a morphism $\mathrm{Spec}\, R \to \mathrm{Spec}\, R_0$, so $\mathrm{Rep}_g(A_0, \mathrm{Spec}\, R)$ holds by Lemma (Change of base), part (b). As $A$ is the base change of $A_0$ to $R$, part (a) gives $\mathrm{Rep}_g(A, \mathrm{Spec}\, R)$. $\square$

**Proposition 1.6.2 (Affine open set).** Let $V$ be an affine open set of $S$ such that $A_V \to V$ is smooth of relative dimension $g$. Then $\mathrm{Rep}_g(A, V)$ holds.

Lean: `GlobalTheory.DualExist.hasRep_affineOpen`.

*Proof.* Let $R = \Gamma(V, \mathcal{O}_S)$, so that there is an isomorphism $\iota : \mathrm{Spec}\, R \to V$, and let $A' = A \times_S \mathrm{Spec}\, R$, the base change along $\mathrm{Spec}\, R \to V \to S$. Then $A'$ is an abelian scheme over $\mathrm{Spec}\, R$. It is the base change of $A_V \to V$ along $\iota$, so it is smooth of relative dimension $g$. Theorem (Affine base) gives $\mathrm{Rep}_g(A', \mathrm{Spec}\, R)$, and Lemma (Change of base), part (a), gives $\mathrm{Rep}_g(A, \mathrm{Spec}\, R)$. Part (b), applied to $\iota^{-1} : V \to \mathrm{Spec}\, R$, which is a morphism of $S$-schemes, gives $\mathrm{Rep}_g(A, V)$. $\square$

**Theorem 1.6.3 (Existence).** Let $S$ be a scheme and $A$ an abelian scheme over $S$. Then there are a group $B$ over $S$ and a line bundle $P$ on $A \times B$ such that $B$ is an abelian scheme, $B$ keeps the dimension of $A$, and $(B, P)$ is a dual of $A$.

Lean: `GlobalTheory.DualExist.exists_dual` (also `GlobalTheory.T.exists_dual_abelianScheme_poincare`, a second name).

*Proof.* For each $s \in S$, fact 2 gives an affine open set $V_s \ni s$ and $g_s$ such that $A_{V_s}$ is smooth of relative dimension $g_s$. The sets $V_s$ cover $S$, and Proposition (Affine open set) gives $\mathrm{Rep}_{g_s}(A, V_s)$ for each $s$. Fact 3 gives $B$ and $P$, with $(B \to S, P)$ a representative over $S$. Fact 4 gives a commutative group structure on $B$ such that $(B, P)$ is a dual of $A$.

The morphism $B \to S$ is smooth, proper and has geometrically connected fibres over each $V_s$, by fact 3. By fact 6 it has these properties over $S$. So $B$ is an abelian scheme.

The fibres of $A \to S$ are geometrically connected, so they are not empty, and $A \to S$ is surjective. Over each $V_s$ both $A$ and $B$ are smooth of relative dimension $g_s$. So $B$ keeps the dimension of $A$, by fact 5. $\square$

**Theorem 1.6.4 (Dual abelian scheme).** Let $S$ be a scheme and $A$ an abelian scheme over $S$. Then there are a group $B$ over $S$ and a line bundle $P$ on $A \times B$ with these properties.

1. $B$ is an abelian scheme over $S$.
2. For each $g$, if $A \to S$ is smooth of relative dimension $g$, then so is $B \to S$.
3. $(B, P)$ is a dual of $A$.
4. $(A, s^* P)$ is a dual of $B$, where $s : B \times A \to A \times B$ is the swap of factors.

Lean: `GlobalTheory.dualAbelianScheme`.

*Proof.* Theorem (Existence) gives $B$ and $P$ with properties 1 and 3, such that $B$ keeps the dimension of $A$. Property 4 follows by fact 7. For property 2, apply the definition of preserved dimension to $T = S$ and $t = \mathrm{id}_S$. The projection $A \times_S S \to A$ is an isomorphism over $S$, so $A \times_S S \to S$ is smooth of relative dimension $g$ if and only if $A \to S$ is, and the same holds for $B$. $\square$

Property 3 says that $B$ represents the functor that sends an $S$-scheme $T$ to the group of line bundles on $A \times T$ that are additive in the first variable, and $P$ is the universal bundle. So $B$ is the dual abelian scheme $A^\vee$ and $P$ is the Poincaré bundle. Over a field this is the classical dual abelian variety (D. Mumford, *Abelian Varieties*, Chapter III, §13). Over a general base, the literature gives the dual as an algebraic space, and as a scheme under extra hypotheses, for example when $A$ is projective over $S$ (G. Faltings and C.-L. Chai, *Degeneration of Abelian Varieties*, Chapter I, §1). Raynaud gives abelian schemes that are not projective over their base (M. Raynaud, *Faisceaux amples sur les schémas en groupes et les espaces homogènes*, Lecture Notes in Math. 119). The theorem asks for a scheme over each base, with no noetherian or projectivity hypothesis, so it may ask for more than these results give.

**Remark 1.6.5 (Formalization).** Facts 1 to 7 are `GlobalTheory.AbelianLimit.abelianScheme_descends_to_fg_subring`, `GlobalTheory.T.abelianScheme_locally_constant_relDim`, `GlobalTheory.T.exists_additiveFamily_representative_zariski_glue`, `GlobalTheory.T.representing_additiveFamilies_isDual_comm`, `GlobalTheory.T.relDimPreserved_of_equal_local_relDims`, `GlobalTheory.CoverGlue.of_isPullback_cover` with Mathlib instances, and `GlobalTheory.T.isDualAbelianSchemePoincare_swap`. Facts 1 to 5 are cited by their statements; the remarks above on why facts 1 and 4 hold are not read from proofs. Fact 1 also takes a finite set $F \subseteq R$ that must lie in $R_0$; the proof of Theorem (Affine base) passes $F = \emptyset$ and drops this output ([AbelianSchemeDualRepresentableAffineBase.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/AbelianSchemeDualRepresentableAffineBase.lean#L19)). Fact 4 also says that $s^* P$ is an additive family; the proof of Theorem (Existence) drops this output ([ExistsDualAbelianSchemePoincare.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsDualAbelianSchemePoincare.lean#L69)). The cover in that proof is indexed by the points of $S$. The transport of a representative along $V \cong \mathrm{Spec}\, R$ is `GlobalTheory.DualExist.hasRep_of_iso`, and the two moves between $A$ and $A \times_S S$ in the last proof are `GlobalTheory.smoothOfRelDim_pullback_snd_identity` and `GlobalTheory.smoothOfRelDim_of_pullback_snd_identity`. The last theorem proves the statement `GlobalTheory.Published.DualAbelianScheme` ([ExistsCrystalPairing.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/ExistsCrystalPairing.lean#L25)), which has a further second name, `GlobalTheory.T.dualAbelianScheme_exists_biduality`. The second name of Theorem (Affine base) does not say that the representative is good. The second names of Theorem (Affine base) and Theorem (Existence) are closed by a `first` list under `set_option maxHeartbeats 1000000`. The statement does not say that $B$ is unique.
