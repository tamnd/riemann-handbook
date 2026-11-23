---
title: Descent to the base
decls:
  - GlobalTheory.Mum.descend_of_emb
  - GlobalTheory.T.semiAbelian_descends_of_closedFibre_embedding
  - GlobalTheory.Mum.exists_near
  - GlobalTheory.T.exists_smooth_model_near_closedFibre_embedding
  - GlobalTheory.Mum.closedFibre_chart
  - GlobalTheory.T.closedFibre_projectiveEmbedding_factors_proper
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Descent to the base

This section proves the descent step of [the theorem on labelled covers](/entry/has-semi-abelian-uniformisation-of-labelled-cover/). We have a modification $(S, \pi, \gamma)$ of $\operatorname{Spec} R$ and a commutative semi-abelian scheme $G'$ over $S$, with an [embedding near the closed fibre](/entry/exists-labelled-cover-embedding-closed-fibre/) that has a theta section for a line bundle $P'$. The result is a commutative semi-abelian scheme $G$ over $\operatorname{Spec} R$ whose pullback along $\pi$ is $G'$, with a line bundle $P$ whose pullback is $P'$. The proof has three parts. First, a chart: the projective embedding factors through a proper map onto a noetherian scheme over $\mathbb{P}^N_R$. Second, a smooth model: an open part of that scheme is a smooth scheme $U$ over $R$ whose pullback to $S$ is an open neighbourhood of the closed fibre of $G'$. Third, the multiplication of $G'$ descends to $U$, and $U$ with this multiplication gives $G$.

Throughout, $R$ is an admissible base with maximal ideal $\mathfrak{m}$, residue field $\kappa(R)$ and fraction field $K$. Let $(S, \pi, \gamma)$ be a modification of $\operatorname{Spec} R$, let $G'$ be a commutative semi-abelian scheme over $S$, and let $(N, \mathcal{H}, f, Y, j)$ be an embedding of $G'$ near the closed fibre, as in the previous section. So $\mathcal{H}$ is an open subset of $G'$ that contains every point over the closed point of $\operatorname{Spec} R$, and $f : \mathcal{H} \to \mathbb{P}^N_R$ is a morphism over $\operatorname{Spec} R$. A point of $G'$ *over the closed point* is a point whose image in $\operatorname{Spec} R$ is the closed point; these points make the *closed fibre* of $G'$.

### Smooth models near the closed fibre

**Definition 4.7.1 (Smooth model near the closed fibre).** Let $R$ be a local ring, $\pi : S \to \operatorname{Spec} R$ a morphism and $G'$ a scheme over $S$. A *smooth model of $G'$ near the closed fibre* consists of a scheme $U$ over $\operatorname{Spec} R$ that is smooth, separated and quasi-compact, and an open immersion $u : U \times_R S \to G'$ over $S$, such that every point of $G'$ over the closed point of $\operatorname{Spec} R$ is in the image of $u$. If $G'$ is a group scheme over $S$, we say that the multiplication of $G'$ *descends to the model* if there are an open subset $V \subseteq U \times_R U$ that contains every point over the closed point and a morphism $m : V \to U$ over $\operatorname{Spec} R$ with this property: for every scheme $T$, every $s : T \to S$, every $v : T \to V$ and all points $x, y$ of $G'$ over $s$, if $u$ carries $(\mathrm{pr}_1 v, s)$ to $x$ and $(\mathrm{pr}_2 v, s)$ to $y$, then $u$ carries $(m v, s)$ to $x y$.

Lean: `GlobalTheory.Mum.Near` (also `GlobalTheory.Mum.Near.Law`, the descent of the multiplication).

If $S = \operatorname{Spec} R$ and $G'$ is smooth, separated and quasi-compact over $R$, then $G'$ itself with $u$ the identity is a smooth model near the closed fibre. So the definition asks for a scheme over $R$ that becomes, after the base change to $S$, an open neighbourhood of the closed fibre of $G'$. The model is not a group, since $V$ need not be all of $U \times_R U$. The condition on $m$ says that $m$ is the multiplication of $G'$ on points of $V$, read through $u$.

### A chart for the embedding

The first step replaces the map $f$ by a map that is proper over its image near the closed fibre.

**Theorem 4.7.2 (Chart for the closed fibre embedding).** Let $R$ be an admissible base, $(S, \pi, \gamma)$ a modification of $\operatorname{Spec} R$, $G'$ a commutative semi-abelian scheme over $S$, and $(N, \mathcal{H}, f, Y, j)$ an embedding of $G'$ near the closed fibre. Then there are a scheme $P'$, a morphism $b : P' \to \mathbb{P}^N_R$, an open subset $X \subseteq \mathcal{H}$ and a morphism $a : X \to P'$ with these properties.

1. $P'$ is noetherian, and $b$ is separated and locally of finite type.
2. $a$ is proper and surjective, and for every open $W \subseteq P'$ the map $a^\sharp : \mathcal{O}_{P'}(W) \to \mathcal{O}_X(a^{-1} W)$ is bijective.
3. $b \circ a$ is the restriction of $f$ to $X$.
4. Every point of $\mathcal{H}$ over the closed point of $\operatorname{Spec} R$ is in $X$.
5. Let $x$ be a closed point of $P'$ over the closed point of $\operatorname{Spec} R$, let $\Omega$ be an algebraically closed field, let $\xi : \operatorname{Spec} \Omega \to P'$ have image $\{x\}$, and let $s : \operatorname{Spec} \Omega \to S$ have the same image in $\operatorname{Spec} R$ as $\xi$. Then there is a point $p : \operatorname{Spec} \Omega \to X$ with $a \circ p = \xi$ whose image in $S$ is $s$.

Lean: `GlobalTheory.Mum.closedFibre_chart` (also `GlobalTheory.T.closedFibre_projectiveEmbedding_factors_proper`, a second name).

*Proof.* The scheme $\mathbb{P}^N_R$ is noetherian, since $R$ is noetherian, and its pullback $\mathbb{P}^N_S \to S$ is proper. The map $\mathcal{H} \to \mathbb{P}^N_S$ given by $f$ and the structure map of $\mathcal{H}$ is separated, locally of finite type and quasi-compact. On the closed fibre this map is injective on points: two points of $\mathcal{H}$ over the closed point with the same image in $\mathbb{P}^N_S$ are equal. So every point of the closed fibre is isolated in its fibre. A result in the style of the Zariski main theorem then gives an open neighbourhood $\mathcal{H}_0 \subseteq \mathcal{H}$ of the closed fibre, a scheme $X''$ that is finite over $\mathbb{P}^N_S$, and an open immersion $\mathcal{H}_0 \to X''$ over $\mathbb{P}^N_S$.

The composite $X'' \to \mathbb{P}^N_S \to \mathbb{P}^N_R$ is proper. Its Stein factorisation is a proper surjective map $a'' : X'' \to P''$ with connected fibres and with $a''^\sharp$ bijective on every open, followed by a map $b'' : P'' \to \mathbb{P}^N_R$. A further result on the Stein factorisation gives an open subset $X$ of $\mathcal{H}_0$, a scheme $P'$ with a map $c : P' \to P''$, and a proper surjective map $a : X \to P'$ with $a^\sharp$ bijective on every open, such that $a$ followed by $c$ is $a''$ on $X$ and $X$ is saturated for $a''$ in the open part. Put $b = b'' \circ c$. Then $b \circ a = f$ on $X$, by the construction of $X''$ over $\mathbb{P}^N_S$.

For property 4, let $z$ be a point of $\mathcal{H}$ over the closed point. Then $z \in \mathcal{H}_0$. The fibre of $a''$ through the image of $z$ is connected, and its points over the closed point lie in the open part $\mathcal{H}_0$. So $z$ is in the saturated open $X$. Property 5 follows from a lifting result for geometric points over the closed fibre, which uses the surjectivity of $a$ and properties 3 and 4. $\square$

### A smooth model

**Theorem 4.7.3 (Smooth model near the closed fibre).** Let $R$, $(S, \pi, \gamma)$, $G'$ and $(N, \mathcal{H}, f, Y, j)$ be as in the previous theorem. Then there are a smooth model $(U, u)$ of $G'$ near the closed fibre, a morphism $f_U : U \to \mathbb{P}^N_R$ and a morphism $l : U \times_R S \to \mathcal{H}$, such that $l$ followed by the inclusion $\mathcal{H} \subseteq G'$ is $u$, and $f \circ l = f_U \circ \mathrm{pr}_1$.

Lean: `GlobalTheory.Mum.exists_near` (also `GlobalTheory.T.exists_smooth_model_near_closedFibre_embedding`, a second name).

*Proof.* *Step 1: the modification.* Since $R$ is a normal domain and $\pi$ is a modification, the map $R \to \mathcal{O}_S(S)$ is bijective and $\pi$ is surjective.

*Step 2: the chart.* The previous theorem gives $P'$, $b$, $X$ and $a$. Let $q : P' \to \operatorname{Spec} R$ be $b$ followed by the structure map of $\mathbb{P}^N_R$. Since $b \circ a = f$ on $X$ and $f$ is a map over $\operatorname{Spec} R$, the square with sides $a : X \to P'$, $X \to S$, $q$ and $\pi$ commutes. For every point $w$ of $X$, the image of $a(w)$ in $\operatorname{Spec} R$ is the image of $w$.

*Step 3: local models.* Let $x$ be a closed point of $P'$ over the closed point of $\operatorname{Spec} R$. A local result gives an open neighbourhood $V_x$ of $x$ in $P'$ such that $q$ is smooth on $V_x$ and the square
$$\begin{array}{ccc} a^{-1}(V_x) & \longrightarrow & S \\ \downarrow & & \downarrow \pi \\ V_x & \xrightarrow{\ q\ } & \operatorname{Spec} R \end{array}$$
is a pullback square. This result needs property 5 of the chart, and also the following fact. Let $\Omega$ be a field and let $p, p' : \operatorname{Spec} \Omega \to X$ be two points over the closed point, with $a \circ p = a \circ p'$ of image $\{x\}$ and with the same image in $S$. Then $f \circ p = f \circ p'$, since $b \circ a = f$. Two field points of the closed fibre of $G'$ over the same point of $S$ with the same image under $f$ are equal. So $p = p'$.

*Step 4: the union.* Let $U \subseteq P'$ be the union of the open sets $V_x$, for all closed points $x$ of $P'$ over the closed point. The pullback squares on the $V_x$ glue to a pullback square on $U$, so $a^{-1}(U)$ is isomorphic to $U \times_R S$. The map $q$ is smooth on $U$, since it is smooth on each $V_x$. Since $q$ is locally of finite type, every point of $P'$ over the closed point has a closed point of $P'$ over the closed point in its closure; so every point of $P'$ over the closed point is in $U$. The map $q$ is separated on $U$, since $b$ is separated and $\mathbb{P}^N_R$ is proper over $R$. It is quasi-compact on $U$, since $P'$ is noetherian and so every open subset of $P'$ is quasi-compact.

*Step 5: the model.* Let $u$ be the inverse of the isomorphism of Step 4, followed by the inclusions $a^{-1}(U) \subseteq X \subseteq \mathcal{H} \subseteq G'$. It is an open immersion over $S$. Let $g$ be a point of $G'$ over the closed point. Then $g \in \mathcal{H}$, and $g \in X$ by property 4 of the chart. The image of $a(g)$ in $\operatorname{Spec} R$ is the closed point, so $a(g) \in U$ by Step 4. So $g$ is in the image of $u$. Put $f_U = b$ on $U$, and let $l$ be the inverse isomorphism followed by $a^{-1}(U) \subseteq X \subseteq \mathcal{H}$. The two equations hold by construction. $\square$

### The descent

**Theorem 4.7.4 (Descent of a semi-abelian scheme from a modification).** Let $R$ be an admissible base, $(S, \pi, \gamma)$ a modification of $\operatorname{Spec} R$, $G'$ a commutative semi-abelian scheme over $S$ and $P'$ a rigidified line bundle on $G'$ with a cubical structure and a symmetric structure. Let $(N, \mathcal{H}, f, Y, j)$ be an embedding of $G'$ near the closed fibre with a theta section for the line bundle of $P'$. Then there are a commutative group scheme $G$ over $\operatorname{Spec} R$, a rigidified line bundle $P$ on $G$ with a cubical structure and a symmetric structure, and a morphism $\beta : G' \to G$, such that:

1. $G$ is semi-abelian;
2. $\beta$ makes $G'$ the group pullback of $G$ along $\pi$;
3. the line bundle of $P'$ is isomorphic to $\beta^*$ of the line bundle of $P$.

Lean: `GlobalTheory.Mum.descend_of_emb` (also `GlobalTheory.T.semiAbelian_descends_of_closedFibre_embedding`, a second name).

*Proof.* *Step 1: surjectivity.* Since $R$ is a normal noetherian domain, the map $\pi$ of the modification is surjective.

*Step 2: a smooth model.* The previous theorem gives a smooth model $(U, u)$ of $G'$ near the closed fibre, with $f_U : U \to \mathbb{P}^N_R$ and $l : U \times_R S \to \mathcal{H}$.

*Step 3: the multiplication.* A result on embeddings near the closed fibre, applied to $f_U$ and $l$, shows that the multiplication of $G'$ descends to the model $U$.

*Step 4: the group.* Since $\pi$ is proper and surjective, $S$ is integral, $G'$ is semi-abelian and the multiplication descends to $U$, a descent result gives a commutative group scheme $G$ over $\operatorname{Spec} R$, a morphism $\beta : G' \to G$ and an open immersion $i : U \to G$ over $\operatorname{Spec} R$ with these properties: $G$ is semi-abelian; $\beta$ makes $G'$ the group pullback of $G$ along $\pi$; and $\beta \circ u = i \circ \mathrm{pr}_1$ on $U \times_R S$.

*Step 5: a theta section on $G$.* From the theta section for the line bundle of $P'$ on $\mathcal{H}$, the maps $f_U$ and $l$, and the open immersion $i$, there are a section $\theta$ and an open subset $O \subseteq G$ that contains a point over the closed point, such that every point $g$ of $G'$ over the closed point with $\beta(g) \in O$ lies in the open set where $\theta$ is not zero.

*Step 6: the line bundle.* With $\theta$ and $O$, a descent result for cubical line bundles gives a line bundle $L$ on $G$ with an isomorphism of the line bundle of $P'$ with $\beta^* L$.

*Step 7: the structures.* Last, a result on the descent of cubical and symmetric structures gives a rigidified line bundle $P$ on $G$ with a cubical structure and a symmetric structure whose line bundle is $L$. With Step 6, this gives property 3. $\square$

The theorem gives the semi-abelian scheme $G$ over $\operatorname{Spec} R$ and the line bundle, but it says nothing about a uniformisation of $G$. In the theorem on labelled covers, the comparison with the degeneration data comes after the descent, at one complete trait.

**Remark 4.7.5 (Formalization).** All three second names are wrappers, proved by a `first | exact` tactic. In the proof of the descent theorem ([SemiAbelianDescendsOfClosedFibreEmbedding.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SemiAbelianDescendsOfClosedFibreEmbedding.lean#L24)), Step 1 is `GlobalTheory.Mum.Modif.appTop_bijective_surjective`, Step 3 is `GlobalTheory.T.mul_descends_near_closed_fibre_of_embedding`, Step 4 is `GlobalTheory.T.semiAbelian_descends_of_descends_near_closedFibre`, Step 5 is `GlobalTheory.T.exists_open_thetaNonvanishing_descendedGroup`, Step 6 is `GlobalTheory.T.cubicalBundle_modification_descends_to_group`, and Step 7 is `GlobalTheory.T.exists_cp_descent'`. The theorem assumes an admissible base, and the characteristic is not used. Its conclusion compares only the line bundles, not the cubical and symmetric structures. The smooth model ([ExistsSmoothModelNearClosedFibreEmbedding.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsSmoothModelNearClosedFibreEmbedding.lean#L19)) uses `GlobalTheory.T.appTop_bijective_and_surjective_normalDomain`, `exists_smooth_open_nbhd_isPullback_at_closedPoint`, `eq_of_fieldPoints_closedFibre_same_projective_image`, `isPullback_restrict_iSup_of_forall_restrict` and `mem_of_closedPoints_closedFibre_mem'`, and discards one output of the chart with a `-` pattern. The chart ([ClosedFibreProjectiveEmbeddingFactorsProper.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ClosedFibreProjectiveEmbeddingFactorsProper.lean#L20)) uses `isNoetherian_projectiveSpace_and_pullback_proper`, `closedFibreEmbedding_lift_separated_finiteType_quasiCompact`, `exists_finite_openImmersion_nbhd_isolatedFibrePoints`, `stein_factorisation_connected_fibres`, `exists_proper_surjective_sections_bijective_over_fibre_open`, `steinFibre_closedFibre_point_subset_open_part` and `lift_geometricPoint_over_closed_fibre`; two outputs of the Zariski step and one output of the Stein step are discarded. The smooth model is the structure `Near`, its multiplication `Near.Law`, and the trivial model `Near.self`. The properness of $\mathbb{P}^N_R$ is `ReciprocityTheory.ChartRestriction.G.Geo.Tor.isProper_str`, a lemma from another part of the library.
