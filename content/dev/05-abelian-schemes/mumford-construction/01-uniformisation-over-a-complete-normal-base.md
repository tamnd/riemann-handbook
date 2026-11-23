---
title: Uniformisation over a complete normal base
decls:
  - GlobalTheory.Mum.has_of_base
  - GlobalTheory.T.hasSemiAbelianUniformisation_complete_normal_base
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Uniformisation over a complete normal base

This section states the main theorem of the chapter and gives the plan of its proof. Let $R$ be a noetherian, integrally closed local domain of characteristic $0$ that is complete for its maximal ideal. Then every set of degeneration data over $R$ comes from a semi-abelian scheme over $R$ whose generic fibre is a polarised abelian variety: the data has a uniformisation. This is Mumford's construction in the form of Faltings and Chai. The proof reduces the theorem, in several steps, to data of unitary PEL type, to a proper modification of $\operatorname{Spec} R$, and to a descent along that modification; each step is proved in a later section. The theorem is used in [the step on characters from the literature](/step/every-character-of-literature/). For the objects see [semi-abelian degenerations and Mumford's construction](/learn/abelian-varieties/#semi-abelian-degenerations-and-mumfords-construction) and [the theorem of the cube](/learn/abelian-varieties/#the-theorem-of-the-cube) in Volume 1.

### Bases and finite extensions

**Definition 4.1.1 (Admissible base, base).** Let $R$ be a local ring with maximal ideal $\mathfrak{m}$. We say that $R$ is an *admissible base* if $R$ is a noetherian, integrally closed domain that is complete and separated for the $\mathfrak{m}$-adic topology. We say that $R$ is a *base* if in addition $R$ has characteristic $0$.

Lean: `GlobalTheory.Mum.Base`.

For a base $R$ we write $K$ for its fraction field, $\bar K$ for an algebraic closure of $K$, $\kappa(R)$ for its residue field and $j_K : \operatorname{Spec} K \to \operatorname{Spec} R$ for the generic point. A complete discrete valuation ring of characteristic $0$ is a base. So is a ring of formal power series $W[[t_1, \dots, t_n]]$ over such a ring $W$.

**Definition 4.1.2 (Finite extension).** Let $R$ be a local domain. A ring map $\rho : R \to R'$ is a *finite extension* if $R'$ is an admissible base, $\rho$ is injective, and $R'$ is a finite $R$-module through $\rho$.

Lean: `GlobalTheory.Mum.FinExt`.

If $R$ is a base and $\rho : R \to R'$ is a finite extension, then $R'$ is again a base, because an injective ring map out of a ring of characteristic $0$ lands in a ring of characteristic $0$.

### Degeneration data and uniformisations

We use the degeneration data of Faltings and Chai in the form of Volume 1. Degeneration data $D$ over $R$ with respect to $\mathfrak{m}$ consist of an abelian scheme $B$ over $R$; an ample line bundle $L$ on $B$ that is rigidified along the zero section, with a cubical structure and a symmetric structure; a free abelian group $\mathsf{X}$ of finite rank, the character lattice; a homomorphism $c : \mathsf{X} \to B(R)$; and, for each $\chi \in \mathsf{X}$, a trivialisation $\psi(\chi)$ of the fibre $c(\chi)^* L^{-1}$ over $K$. We put
$$\tau(a, b) = \psi(a + b)\, \psi(a)^{-1} \psi(b)^{-1}, \qquad a, b \in \mathsf{X}.$$
The data are subject to these conditions: $\psi$ is even; $\tau$ is bimultiplicative; for $\chi \neq 0$ the trivialisation $\psi(\chi)$ extends over $R$ with values in $\mathfrak{m}$; and for each $e \geq 0$, $\psi(\chi)$ has values in $\mathfrak{m}^{e}$ for all but finitely many $\chi$. The last two conditions are the positivity of the data. The torus $T$ with character group $\mathsf{X}$ and the map $c$ give an extension $\tilde G$ of $B$ by $T$, the Raynaud extension, and $L$ pulls back to a line bundle on $\tilde G$.

Let $\rho : R \to R'$ be a ring map and $D'$ degeneration data over $R'$. We say that $D'$ is a *pullback* of $D$ along $\rho$ if we are given an isomorphism of groups $B' \cong B \otimes_R R'$, an isomorphism of $L'$ with the pullback of $L$ which respects the rigidifications, and an isomorphism $\mathsf{X}' \cong \mathsf{X}$ under which $c'$ is the base change of $c$ and $\psi'$ is the base change of $\psi$.

A *polarised abelian variety* over $K$ is an abelian variety $A$ over $K$ with an ample line bundle $L_A$ that is rigidified along the zero section.

**Definition 4.1.3 (Uniformisation).** Let $D$ be degeneration data over $R$, let $A$ be a polarised abelian variety over $K$, and let $G$ be a smooth, separated, commutative group scheme over $R$. A *uniformisation* of $(A, G)$ by $D$ consists of the following data.

1. An isomorphism of group schemes $A \cong G_K$ between $A$ and the generic fibre of $G$.
2. A line bundle $L_G$ on $G$, rigidified along the zero section, with a cubical structure and a symmetric structure that is compatible with the rigidification; and an isomorphism $L_A \cong L_G|_{G_K}$ that respects the rigidifications.
3. For each $e \geq 0$, an isomorphism of group schemes between $G \otimes_R R/\mathfrak{m}^{e+1}$ and the Raynaud extension $\tilde G \otimes_R R/\mathfrak{m}^{e+1}$, and an isomorphism of the restriction of $L_G$ with the restriction of the pullback of $L$.

The isomorphisms in 3 are compatible as $e$ grows. They respect the rigidifications, the cubical structures and the symmetric structures, and they carry the trivialisations $\psi(\chi)$ to the values of $L_G$ at the periods of $G$.

So a uniformisation says that $G$ is a formal model of the Raynaud extension along the closed fibre, and that its generic fibre is $A$. This is the output of Mumford's construction.

**Definition 4.1.4 (Realised data).** Let $R$ be a local domain and $D$ degeneration data over $R$ with respect to $\mathfrak{m}$. We say that $D$ is *realised* if there are a commutative semi-abelian group scheme $G$ over $\operatorname{Spec} R$, a polarised abelian variety $A$ over $K$, and a uniformisation of $(A, G)$ by $D$. We say that $D$ is *realised after a finite extension* if there are a finite extension $\rho : R \to R'$ and a pullback $D'$ of $D$ along $\rho$ such that $D'$ is realised.

Lean: `GlobalTheory.Mum.Has` (also `GlobalTheory.Mum.HasFin`, the second notion).

### The main theorem

The classical statement is due to Mumford and, for data with a non-trivial abelian part, to Faltings and Chai. Let $R$ be an excellent normal noetherian domain that is complete for the $I$-adic topology of a radical ideal $I$. Then Mumford's construction is an inverse of the functor that sends a semi-abelian scheme over $R$ with a principally polarised abelian generic fibre, split over $R/I$, to its degeneration data; so every set of principally polarised degeneration data over $(R, I)$ comes from such a scheme. (D. Mumford, *An analytic construction of degenerating abelian varieties over complete rings*, Compositio Math. 24, 1972; G. Faltings and C.-L. Chai, *Degeneration of Abelian Varieties*, Chapter III. See [the statement in Volume 1](/learn/abelian-varieties/#semi-abelian-degenerations-and-mumfords-construction).) The theorem below is the existence half of this statement in the local case $I = \mathfrak{m}$, in characteristic $0$, for data with the trivialisations $\psi$ of a line bundle in place of a principal polarisation. A complete noetherian local ring is excellent, so no condition of excellence is needed. The theorem does not claim that the semi-abelian scheme is unique, nor that the construction is a functor.

**Theorem 4.1.5 (Mumford's construction).** Let $R$ be a base. Then every set of degeneration data over $R$ with respect to its maximal ideal is realised.

Lean: `GlobalTheory.Mum.has_of_base` (also `GlobalTheory.T.hasSemiAbelianUniformisation_complete_normal_base`, a second name).

*Proof.* Let $D$ be degeneration data over $R$ with character lattice $\mathsf{X}$.

If $\mathsf{X} = 0$, then the torus is trivial and $D$ is realised by the abelian scheme $B$ itself, with $A = B_K$ and $L_G = L$. This case holds over any admissible base.

Let $\mathsf{X} \neq 0$. By [the theorem on unitary factors](/entry/exists-unitary-peltype-factor-deg-data/), there are a CM field $E$ with host data, a unitary datum, degeneration data $D'$ over $R$ with an action of $\mathcal{O}_E$ on its character lattice $\mathsf{X}'$ of unitary PEL type, and an algebraic factor $F$ of $D'$ onto $D$. The factor gives a map $\xi : \mathsf{X} \to \mathsf{X}'$ with a left inverse, so $\mathsf{X}' \neq 0$.

By [the theorem on labelled covers](/entry/exists-labelled-cover-unitary-peltype-finite-ext/), there are a finite extension $\rho : R \to R'$ and a pullback $D''$ of $D'$ along $\rho$ such that $D''$ has a labelled cover. The ring $R'$ is again a base. By [the theorem on labelled covers and realisation](/entry/has-semi-abelian-uniformisation-of-labelled-cover/), $D''$ is realised after a finite extension. A pullback of $D'$ along $\rho$ which is realised after a finite extension shows that $D'$ itself is realised after a finite extension, since a composite of finite extensions is a finite extension. By [the descent theorem for finite extensions](/entry/has-semi-abelian-uniformisation-of-finite-ext/), $D'$ is realised: there are $G'$, $A'$ and a uniformisation $U'$ of $(A', G')$ by $D'$.

The ring $\mathcal{O}$ of the factor $F$ acts on $D'$. By the result on extension of ring actions to uniformised semi-abelian schemes, this action extends to actions on $A'$ and on $G'$ for which $U'$ is linear. The factor contains an idempotent $e \in \mathcal{O}$, so the endomorphism $[e]$ of $G'$ is idempotent. The image of an idempotent endomorphism of a commutative semi-abelian scheme is a semi-abelian scheme $G$, with a monomorphism $i : G \to G'$ and a homomorphism $p : G' \to G$ such that $p \circ i = 1$ and $i \circ p = [e]$. By [the theorem on idempotent factors](/entry/idempotent-factor-uniformised-of-deg-data-factor/), there are a finite extension $\rho_1 : R \to R_1$, a pullback $D_1$ of $D$ along $\rho_1$, and a group scheme $G_1$ over $R_1$ with a uniformisation by $D_1$, such that $G_1$ is the base change of $G$ along $\rho_1$. A group scheme that is a base change of a semi-abelian scheme is semi-abelian, so $D$ is realised after a finite extension. By [the descent theorem for finite extensions](/entry/has-semi-abelian-uniformisation-of-finite-ext/) again, $D$ is realised. $\square$

The proof has three parts of different kinds. The first part is lattice theory: it embeds $D$ as a direct factor of data with a large ring of endomorphisms. The second part is geometry over a modification: data with these endomorphisms have a labelled cover, and a labelled cover gives a semi-abelian scheme over a proper modification of $\operatorname{Spec} R$, which descends to $\operatorname{Spec} R$ after a finite extension. The third part is Galois descent and the passage to the factor. Sections 2 to 7 of this chapter prove the second part and the lattice step that starts the first. The later sections prove the rest.

**Remark 4.1.6 (Formalization).** The second name is a wrapper: its proof is a `first | exact` tactic that applies the first ([HasSemiAbelianUniformisationCompleteNormalBaseStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasSemiAbelianUniformisationCompleteNormalBaseStatement.lean#L13)). The case $\mathsf{X} = 0$ is `GlobalTheory.Mum.has_of_subsingleton`, which needs only an admissible base. The step from the pullback $D''$ to $D'$ is `GlobalTheory.Mum.hasFin_of_finExt`. The extension of ring actions is `GlobalTheory.T.exists_ringAction_extension_to_uniformised_semiAbelian` and the image of the idempotent is `GlobalTheory.Mum.IdemImage.isSemiAbelian_image`. The fact that a group pullback of a semi-abelian scheme is semi-abelian is proved twice, as `GlobalTheory.Mum.isSemiAbelian_of_isGrpPullback'` ([HasSemiAbelianUniformisationCompleteNormalBase.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasSemiAbelianUniformisationCompleteNormalBase.lean#L27)) and as `GlobalTheory.Mum.CoverFin.semiAbelian_of_pull` ([HasSemiAbelianUniformisationOfLabelledCover.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasSemiAbelianUniformisationOfLabelledCover.lean#L26)), with the same proof. Of the conclusion of the theorem on idempotent factors, the proof uses only the finite extension, the pullback of $D$, the uniformisation and the group pullback square; the compatibility of the line bundles is discarded. Degeneration data, their pullbacks and uniformisations are the structures `DegData`, `IsPullDeg` and `Unif`.
