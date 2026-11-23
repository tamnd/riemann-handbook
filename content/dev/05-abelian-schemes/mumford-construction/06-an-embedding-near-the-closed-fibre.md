---
title: An embedding near the closed fibre
decls:
  - GlobalTheory.Mum.exists_emb_of_labCover
  - GlobalTheory.T.exists_labelledCover_embedding_closedFibre
  - GlobalTheory.Mum.SecEmb.emb_of_secs
  - GlobalTheory.T.exists_closedFibre_theta_embedding_of_sections
  - GlobalTheory.Mum.extend_finiteModif
status: drafted
drafted_by: writer@claude-opus-5-5
---
## An embedding near the closed fibre

The sections of [the previous section](/entry/secs-exists/) live on the abelian variety $A$ over $K$, and they extend over every complete trait. This section makes them extend over the modification itself, after a finite modification, and so gives a map from an open neighbourhood of the closed fibre of the labelled cover to a projective space over $R$. On the closed fibre this map is the fixed immersion of a smooth group, up to an isomorphism at every field point, and a theta section does not vanish on a dense part of it. This is the first step of [the theorem on labelled covers](/entry/has-fin-of-lab-cover/); the second step, [the descent](/entry/semi-abelian-descends-of-closed-fibre-embedding/), starts from this embedding. The proof uses [discrete valuation rings](/learn/commutative-algebra/#regular-local-rings-and-discrete-valuation-rings) and the [[valuative criterion|QZN6P7AG33]] from Volume 1.

Throughout, $R$ is a base with maximal ideal $\mathfrak{m}$, residue field $\kappa(R)$ and fraction field $K$, and $\mathbb{P}^N_R$ is projective space over $R$. For a modification $M = (S, \pi, \gamma)$ of $\operatorname{Spec} R$, a group scheme $G$ over $S$, a line bundle $\mathcal{L}$ on $G$ and $\alpha : A \to G$, we use sections of $\alpha^* \mathcal{L}^k$ and the relation "agree" of [the previous section](/entry/secs-exists/).

### Sections regular at traits

**Definition 4.6.1 (Section regular at all traits).** A section $s$ of $\alpha^* \mathcal{L}^k$ is *regular at all traits* if for every complete trait $V$, every injective local map $\varphi : R \to V$ and every trait $\xi : \operatorname{Spec} V \to S$ over $\varphi$, there are a complete trait $V'$ with a finite injective map $\iota : V \to V'$ and a section $\sigma$ of the pullback of $\mathcal{L}^k$ to $G \times_S \operatorname{Spec} V'$ (along $\xi \circ \operatorname{Spec} \iota$) that agrees with $s$.

Lean: `GlobalTheory.Mum.TraitReg`.

A section in a system with prescribed reduction is regular at all traits: the trait condition gives the section $\sigma_i$ on a group $G'$ which is a group pullback of $G$, and this pullback is isomorphic to the fibre product.

**Theorem 4.6.2 (Extension over a finite modification).** Let $R$ be a noetherian local domain of characteristic $0$, let $M = (S, \pi, \gamma)$ be a modification of $\operatorname{Spec} R$, and let $G$ be a scheme over $S$ which is smooth, quasi-compact and geometrically irreducible, with a line bundle $\mathcal{L}$. Let $\alpha : A \to G$ and $t : A \to \operatorname{Spec} K$ make $A$ the fibre product of $G$ and $\operatorname{Spec} K$ over $S$ (along $\gamma$). Let $I$ be a finite set, $k : I \to \mathbb{N}$, and let $s_i$ be sections of $\alpha^* \mathcal{L}^{k(i)}$ that are regular at all traits. Then there are a modification $M' = (S', \pi', \gamma')$ of $\operatorname{Spec} R$ and a finite morphism $h : S' \to S$ with $h \circ \gamma' = \gamma$ and $\pi \circ h = \pi'$, such that for each $i$ there is a section of the pullback of $\mathcal{L}^{k(i)}$ to $G \times_S S'$ that agrees with $s_i$.

Lean: `GlobalTheory.Mum.extend_finiteModif`.

A section that is regular at all traits need not be regular on $G$ itself, since its constants may be integral over $S$ without being functions on $S$. The finite modification adjoins these constants. In this sense the theorem is a form of the Hartogs property: a rational section that is regular at all traits becomes regular after a finite modification.

*Proof.* First, each $s_i$ is *locally integral*: on every affine open $W$ of $G$ on which $\mathcal{L}$ is trivial and which lies over an affine open $U$ of $S$, the section $s_i$ is a finite sum $\sum_m c_m b_m$ with $c_m$ regular functions on $W$ and $b_m$ elements of $K$ that are integral over $\mathcal{O}(U)$. This step uses that $G$ is smooth, quasi-compact and geometrically irreducible over $S$, and that $R$ is noetherian of characteristic $0$. Second, finitely many locally integral sections extend over a finite modification: there are $M'$ and a finite map $h$ as in the statement such that each $s_i$ agrees with a section on $G \times_S S'$. $\square$

### Embeddings near the closed fibre

**Definition 4.6.3 (Embedding near the closed fibre).** Let $\pi : S \to \operatorname{Spec} R$ be a morphism and $G$ a group scheme over $S$. An *embedding of $G$ near the closed fibre* consists of: an integer $N$; an open subset $\mathcal{H} \subseteq G$ that contains every point of $G$ over the closed point of $\operatorname{Spec} R$; a morphism $f : \mathcal{H} \to \mathbb{P}^N_R$ over $\operatorname{Spec} R$; a smooth group scheme $Y$ over $\kappa(R)$; and an immersion $j : Y \to \mathbb{P}^N_R$ over $\operatorname{Spec} \kappa(R)$. We require the following fibre condition. For every field $\Omega$, every point $x : \operatorname{Spec} \Omega \to S$ and every map $\kappa : \kappa(R) \to \Omega$ with $\pi(x)$ the closed point through $\kappa$, there are a field extension $\Omega \to \Omega'$, a group isomorphism $e : G_x \otimes \Omega' \cong Y \otimes \Omega'$, and a morphism $l : G_x \otimes \Omega' \to \mathcal{H}$ over the inclusion into $G$, with $f \circ l = j \circ e$.

The embedding *has a theta section* for a line bundle $\mathcal{L}$ on $G$ if there are a global section $\theta$ of $\mathcal{L}$ and a nonempty open subset $O \subseteq Y$ such that every point $g \in \mathcal{H}$ over the closed point with $f(g) = j(y)$ for some $y \in O$ lies in the set where $\theta$ does not vanish.

Lean: `GlobalTheory.Mum.Emb` (also `GlobalTheory.Mum.Emb.Theta`, the theta section).

So $f$ maps every geometric fibre of $G$ over the closed point isomorphically, as a group, onto the same subscheme $j(Y)$ of $\mathbb{P}^N$. Over $\operatorname{Spec} R$ itself, with $S = \operatorname{Spec} R$, this says that $f$ restricted to the closed fibre is an immersion with image $j(Y)$.

**Theorem 4.6.4 (Embedding from sections).** Let $R$ be a base, $D$ degeneration data over $R$ and $C$ a labelled cover of $D$ that has a system of sections with prescribed reduction. Then there is a labelled cover $C'$ of $D$ whose group has an embedding near the closed fibre with a theta section for the line bundle of $C'$.

Lean: `GlobalTheory.Mum.SecEmb.emb_of_secs` (also `GlobalTheory.T.exists_closedFibre_theta_embedding_of_sections`, a second name).

*Proof.* Let $(s_0, \dots, s_N, \theta, Y, j, O)$ be the system, with sections $s_i$ of degree $k$, on the cover $C$ with modification $M = (S, \pi, \gamma)$ and group $G$.

*Step 1: regularity.* By the remark after the definition, the $s_i$ and $\theta$ are regular at all traits.

*Step 2: a finite modification.* The group $G$ is semi-abelian, so it is smooth and quasi-compact over $S$ with geometrically connected fibres; a smooth scheme with geometrically connected fibres is geometrically irreducible. The ring $R$ is noetherian of characteristic $0$, and $A$ is the fibre product of $G$ and $\operatorname{Spec} K$. Apply the extension theorem to the $N + 2$ sections $\theta, s_0, \dots, s_N$. It gives a modification $M' = (S', \pi', \gamma')$ and $h : S' \to S$ with sections on $G \times_S S'$ that agree with $\theta$ and with the $s_i$.

*Step 3: the pulled back cover.* A labelled cover pulls back along such a map $h$: there are a labelled cover $C'$ of $D$ with modification isomorphic to $M'$ and group $G'$, and a morphism $\beta : G' \to G$ that makes $G'$ the group pullback of $G$ along $S' \to S$, with the line bundle of $C'$ isomorphic to $\beta^* P$. The sections of Step 2 pull back along $G' \to G \times_S S'$ to sections $\sigma_i$ and $\theta_0$ of $\beta^* P^k$ and $\beta^* P$ on $G'$, and they still agree with $s_i$ and $\theta$.

*Step 4: reduction at traits.* Since the $\sigma_i$ agree with the $s_i$, the trait condition of the system passes to $C'$: at every trait of $S'$, after a finite extension, there is a group isomorphism $e$ of the closed fibre of the pulled back group with $Y$ such that $[\sigma_0 : \dots : \sigma_N] = j \circ e$ at field points, and a section $\theta$ of the line bundle of $C'$ that does not vanish over $O$.

*Step 5: the embedding.* Let $\mathcal{H}$ be the union of the open sets where some $\sigma_i$ does not vanish, and $f = [\sigma_0 : \dots : \sigma_N] : \mathcal{H} \to \mathbb{P}^N_R$. From Step 4 one gets that every point of $G'$ over the closed point lies in $\mathcal{H}$, since at the traits the $\sigma_i$ have no common zero on the closed fibre. The fibre condition at a field point $x$ of $S'$ over the closed point follows from Step 4 at a trait through $x$, and the theta condition follows from the last clause of Step 4. $\square$

**Theorem 4.6.5 (Embedding of a labelled cover).** Let $R$ be a base, $D$ degeneration data over $R$ and $C$ a labelled cover of $D$. Then there are a finite extension $\rho : R \to R'$, degeneration data $D'$ over $R'$ that are a pullback of $D$ along $\rho$, and a labelled cover $C'$ of $D'$ whose group has an embedding near the closed fibre with a theta section for the line bundle of $C'$.

Lean: `GlobalTheory.Mum.exists_emb_of_labCover` (also `GlobalTheory.T.exists_labelledCover_embedding_closedFibre`, a second name).

*Proof.* By [the theorem on sections after a finite extension](/entry/exists-secs-fin-ext/) there are a finite extension $\rho : R \to R_1$, data $D_1$ that are a pullback of $D$, and a labelled cover $C_1$ of $D_1$ with a system of sections with prescribed reduction. The ring $R_1$ is a base: it is an admissible base by the definition of a finite extension, and it has characteristic $0$ since $\rho$ is injective and $R$ has characteristic $0$. The previous theorem, applied to $C_1$ over $R_1$, gives $C'$ and the embedding. $\square$

**Remark 4.6.6 (Formalization).** Both second names are wrappers, proved by a `first | exact` tactic. Since the finite extension in the theorem on sections is the identity, the extension $\rho$ in the last theorem is also the identity in the Lean proof. The extension theorem is the composite of `GlobalTheory.T.locallyIntegral_of_regular_at_all_traits` and `GlobalTheory.T.locallyIntegralSections_extend_over_finiteModification` ([ExtendFiniteModif.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExtendFiniteModif.lean#L16)); the reading as a Hartogs property is ours, and the predicate "locally integral" is `GlobalTheory.Mum.LocInt`. In the proof of the embedding theorem ([ExistsClosedFibreThetaEmbeddingOfSections.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsClosedFibreThetaEmbeddingOfSections.lean#L85)), Step 1 is `traitReg_of_secs`, which discards most components of the trait condition with `-` patterns (lines 63 and 68); Step 2 discards the finiteness of $h$ (line 92), which is not needed after it; the irreducibility is the local lemma `geometricallyIrreducible_of_smooth`; Step 3 is `GlobalTheory.Mum.LabCover.exists_pull` and `agree_pull`; Step 4 is `GlobalTheory.Mum.SecEmb.traitRed_cover` with the predicate `TraitRed`; and Step 5 is `emb_of_traitRed`, with $\mathcal{H}$ the open `embH` and $f$ the map `embF`. The $N + 2$ sections are indexed by `Option (Fin (N + 1))`, with `none` for $\theta$.
