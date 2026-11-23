---
title: Labelled covers
decls:
  - GlobalTheory.Mum.hasFin_of_labCover
  - GlobalTheory.T.hasSemiAbelianUniformisation_of_labelledCover
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Labelled covers

This section reduces [Mumford's construction](/entry/has-of-base/) to the construction of a labelled cover. A labelled cover of degeneration data $D$ is a semi-abelian scheme over a proper modification of $\operatorname{Spec} R$, which is uniformised by pullbacks of $D$ at every complete trait. The theorem of this section says that a labelled cover gives a uniformisation of $D$ after a finite extension of $R$. The first section uses it in the step that goes from data of unitary PEL type to a uniformisation. The proof uses the [[valuative criterion|QZN6P7AG33]] of properness and two results that come later in this chapter: [the embedding of a labelled cover near its closed fibre](/entry/exists-labelled-cover-embedding-closed-fibre/) and [the descent of a semi-abelian scheme from a modification](/entry/semi-abelian-descends-of-closed-fibre-embedding/).

Throughout, $R$ is a base, with maximal ideal $\mathfrak{m}$, fraction field $K$ and the map $j_K : \operatorname{Spec} K \to \operatorname{Spec} R$. As in the first section, a *complete trait* is a complete [[discrete valuation ring|MGM3CNJW9V]] of characteristic $0$.

### Modifications

**Definition 4.3.1 (Modification).** Let $R$ be a domain with fraction field $K$. A *modification* of $\operatorname{Spec} R$ is an integral scheme $S$ with a proper morphism $\pi : S \to \operatorname{Spec} R$ and a morphism $\gamma : \operatorname{Spec} K \to S$ with dominant image, such that $\pi \circ \gamma = j_K$. The *trivial modification* is $S = \operatorname{Spec} R$ with $\pi$ the identity and $\gamma = j_K$.

Lean: `GlobalTheory.Mum.Modif` (also `GlobalTheory.Mum.Modif.self`, the trivial modification).

So $\gamma$ is a generic point of $S$, and $\pi$ is an isomorphism at the generic point. A blow-up of $\operatorname{Spec} R$ along an ideal that is not zero is a modification. If $V$ is a complete trait, $\varphi : R \to V$ is an injective local map and $\xi : \operatorname{Spec} V \to S$ satisfies $\pi \circ \xi = \operatorname{Spec} \varphi$, we say that $\xi$ is a *trait of $S$ over $\varphi$*. By the valuative criterion for the proper map $\pi$, every $\varphi$ has such a trait: the map $\operatorname{Spec} \operatorname{Frac} V \to \operatorname{Spec} K \to S$ extends over $\operatorname{Spec} V$.

### Labelled covers

**Definition 4.3.2 (Labelled cover).** Let $R$ be a local domain and let $D$ be degeneration data over $R$. A *labelled cover* of $D$ consists of the following data.

1. A modification $(S, \pi, \gamma)$ of $\operatorname{Spec} R$.
2. A commutative semi-abelian group scheme $G$ over $S$, with a rigidified line bundle $P$ on $G$ that has a cubical structure and a symmetric structure.
3. A polarised [[abelian variety|R7W03TXRS9]] $A$ over $K$, with a morphism $\alpha : A \to G$ that makes $A$ the group pullback of $G$ along $\gamma$, and an isomorphism of the polarisation bundle of $A$ with $\alpha^* P$.
4. An odd prime $n$ that is a unit in $R$.
5. For each $j \geq 0$, a map $\ell_j$ from the torsion classes $Q_{n^j}(D)(\bar K)$ to the points $A(\bar K)$. These are the *labels*.
6. The trait condition. Let $V$ be a complete trait, $\varphi : R \to V$ an injective local map and $\xi$ a trait of $S$ over $\varphi$. Then there are a complete trait $V'$ with a finite injective map $\iota : V \to V'$; degeneration data $D'$ over $V'$ which are a pullback of $D$ along $\iota \circ \varphi$; a commutative group scheme $G'$ over $V'$ with a morphism $\beta : G' \to G$ that makes $G'$ the group pullback of $G$ along $\xi \circ \operatorname{Spec} \iota$; and a uniformisation $U'$ of $G'$ by $D'$, with generic fibre a polarised abelian variety $A'$, whose line bundle is isomorphic to $\beta^* P$. The labels are compatible with $U'$: let $F$ be an algebraically closed field over $\operatorname{Frac} V'$, with a $K$-embedding of $\bar K$ into $F$ that agrees with $\iota \circ \varphi$ on $R$. If $p \in Q_{n^j}(D)(\bar K)$ has image $p'$ in $Q_{n^j}(D')(F)$, and $x' \in A'(F)$ lies over the image of $\ell_j(p)$ in $G$, then $U'$ carries $p'$ to $x'$.

Lean: `GlobalTheory.Mum.LabCover`.

Over the generic point, a labelled cover is a polarised abelian variety with an extension to a semi-abelian scheme over $S$. The labels name its torsion points of order a power of $n$ by torsion classes of $D$. The trait condition says that at each complete trait the cover is uniformised by $D$, after a finite extension of the trait, in a way that matches the labels with the torsion classes. If $S = \operatorname{Spec} R$ and $R$ is a complete trait, the trait condition at the identity map of $R$ already gives a uniformisation of $D$ after a finite extension.

The main difficulty is that $S$ is not $\operatorname{Spec} R$. The proof below first replaces the modification by one on which the cover has a projective embedding near the closed fibre, then descends the group scheme to $\operatorname{Spec} R'$ for a finite extension $R'$ of $R$, and last uses one complete trait to compare the descended group with the data.

### The theorem

**Theorem 4.3.3 (Uniformisation from a labelled cover).** Let $R$ be a base and let $D$ be degeneration data over $R$. If $D$ has a labelled cover, then $D$ is realised after a finite extension: there are a finite extension $\rho : R \to R'$, degeneration data $D'$ over $R'$ that are a pullback of $D$ along $\rho$, and a commutative semi-abelian scheme over $\operatorname{Spec} R'$ which is uniformised by $D'$.

Lean: `GlobalTheory.Mum.hasFin_of_labCover` (also `GlobalTheory.T.hasSemiAbelianUniformisation_of_labelledCover`, a second name).

*Proof.* Let $C$ be a labelled cover of $D$.

*Step 1: an embedding near the closed fibre.* By [the embedding theorem for labelled covers](/entry/exists-labelled-cover-embedding-closed-fibre/), there are a finite extension $\rho : R \to R'$, degeneration data $D'$ over $R'$ that are a pullback of $D$ along $\rho$, and a labelled cover $C'$ of $D'$ with modification $(S', \pi', \gamma')$ and semi-abelian scheme $G'$, together with a projective embedding of a neighbourhood of the closed fibre of $G'$ that has a theta section for the line bundle of $C'$. The ring $R'$ is an admissible base, noetherian and of characteristic $0$, since $R$ has characteristic $0$ and $\rho$ is injective.

*Step 2: descent.* By [the descent theorem](/entry/semi-abelian-descends-of-closed-fibre-embedding/) applied over $R'$, there are a commutative semi-abelian scheme $G$ over $\operatorname{Spec} R'$, a rigidified line bundle $P$ on $G$ with a cubical structure and a symmetric structure, and a morphism $\beta : G' \to G$ that makes $G'$ the group pullback of $G$ along $\pi'$, such that the line bundle of $C'$ is isomorphic to $\beta^* P$.

*Step 3: a complete trait.* Since $R'$ is a noetherian domain of characteristic $0$, there are a complete trait $V$ and an injective map $\varphi : R' \to V$ with $\varphi^{-1}(\mathfrak{m}_V) = \mathfrak{m}_{R'}$. So $\varphi$ is local. The map $\varphi$ extends to the fraction fields. By the valuative criterion for the proper map $\pi'$, the composite $\operatorname{Spec} \operatorname{Frac} V \to \operatorname{Spec} \operatorname{Frac} R' \to S'$ (the second map is $\gamma'$) extends to a trait $\xi : \operatorname{Spec} V \to S'$ over $\varphi$.

*Step 4: the trait condition.* The trait condition of $C'$ at $(V, \varphi, \xi)$ gives a complete trait $V'$ with a finite injective map $\iota : V \to V'$, degeneration data $D''$ over $V'$ that are a pullback of $D'$, a commutative group scheme $G''$ over $V'$ with $\beta' : G'' \to G'$ that makes $G''$ the group pullback of $G'$ along $\xi \circ \operatorname{Spec} \iota$, and a uniformisation $U''$ of $G''$ by $D''$ whose line bundle is isomorphic to $\beta'^* $ of the line bundle of $C'$. We use only this part of the trait condition, and not the labels.

*Step 5: comparison with $G$.* Since $\pi' \circ \xi \circ \operatorname{Spec} \iota = \operatorname{Spec}(\iota \circ \varphi)$, the composite $\beta \circ \beta'$ makes $G''$ the group pullback of $G$ along $\operatorname{Spec}(\iota \circ \varphi)$. The isomorphisms of Steps 2 and 4 compose to an isomorphism of the line bundle of $U''$ with $(\beta \circ \beta')^* P$. Now $\iota \circ \varphi$ is an injective local map from $R'$ to a complete trait, and $G$ is semi-abelian over $R'$ with a uniformisation of its pullback to $V'$ by a pullback of $D'$, with matching line bundles. A result on uniformisations at one trait then gives a finite extension $\rho_1 : R' \to R_1$, degeneration data $D_1$ over $R_1$ that are a pullback of $D'$, a group scheme $G_1$ over $R_1$ with a morphism $\beta_1 : G_1 \to G$ that makes $G_1$ the group pullback of $G$, and a uniformisation of $G_1$ by $D_1$. Since $G$ is semi-abelian, its pullback $G_1$ is semi-abelian. So $D'$ is realised after the finite extension $\rho_1$.

*Step 6: transitivity.* Since $D'$ is a pullback of $D$ along the finite extension $\rho$, and $D'$ is realised after a finite extension, $D$ is realised after a finite extension. $\square$

The labels of a labelled cover are not used in this proof. They are used in the construction of the cover from data of unitary PEL type, which is in a later part of this chapter, and there they serve to recognise the degeneration data of the cover at each trait.

**Remark 4.3.4 (Formalization).** The second name is a wrapper ([HasSemiAbelianUniformisationOfLabelledCoverStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasSemiAbelianUniformisationOfLabelledCoverStatement.lean#L12)), proved by a `first | exact` tactic. In the proof ([HasSemiAbelianUniformisationOfLabelledCover.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasSemiAbelianUniformisationOfLabelledCover.lean#L43)), Step 3 is `GlobalTheory.PrimeUnif.exists_cdvr` with the local lemma `GlobalTheory.Mum.CoverFin.isLocalHom_of_comap`, and the extension over the trait is `val_exists`. In Step 4, the label clause of `LabCover.trait` is discarded with a `-` pattern (line 65). The result on one trait in Step 5 is `GlobalTheory.T.exists_finiteExtension_uniformisation_of_trait_unif`; its last output, the line bundle isomorphism, is also discarded (line 73). The semi-abelian pullback is the local lemma `GlobalTheory.Mum.CoverFin.semiAbelian_of_pull` (line 26), which repeats a lemma of the file of the first section. Step 6 is `GlobalTheory.T.hasSemiAbelianUniformisation_of_finiteExt_trans`. A labelled cover of the Lean code is `LabCover`, which extends `Modif`; the polarised abelian variety is a `PolAV`, the line bundle with its cubical and symmetric structures a `GlobalTheory.UU.CP`, and the label compatibility the predicate `QkToAkU`.
