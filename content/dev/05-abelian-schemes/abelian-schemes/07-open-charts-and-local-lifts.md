---
title: Open charts and local lifts
decls:
  - GlobalTheory.T.openChart_of_smoothFamily_geomFibreInjective
  - GlobalTheory.ChartCrit.openChart
  - GlobalTheory.T.representingScheme_of_finite_surjective_lift
  - GlobalTheory.DualCon.hasRep_of_liftAt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Open charts and local lifts

The pinching theorem ([Theorem 1.4.2](/entry/has-rep-pinched/)) builds a good representative over $\mathrm{Spec}\, R$ from a representative over a finite cover $\mathrm{Spec}\, R'$. This section gives the criterion that the pinching proof checks. Suppose that $S' \to \mathrm{Spec}\, R$ is finite and surjective, that a good representative $(b : B \to S', P)$ exists, and that near each point of $B$ the bundle $P$ comes from an additive family over a smooth $R$-scheme $U$. Then a good representative exists over $\mathrm{Spec}\, R$ (Theorem (Descent from a finite cover)). The tool is the notion of a chart: a family $M$ on $A \times U$ such that $U$ is an open piece of the dual functor. Theorem (Open chart) says that a smooth family of the right dimension that is injective on geometric fibres is a chart.

Throughout, $R$ is a noetherian ring, $S = \mathrm{Spec}\, R$, and $A$ is an [[abelian scheme|JDDXZ89N33]] over $S$, smooth of relative dimension $g$. Products are fibre products over $S$. We use additive families, agreement and representatives as defined in the second section of this chapter.

**Definition 1.7.1 (Injective on geometric fibres).** Let $U$ be an $S$-scheme and $M$ a line bundle on $A \times U$. We say that $M$ is *injective on geometric fibres* if the following holds for each algebraically closed field $K$ and each $s : \mathrm{Spec}\, K \to S$. Let $Y$ be an $S$-scheme with an $S$-morphism $Y \to \mathrm{Spec}\, K$, and let $u, u' \in U(Y)$. If $M$ at $u$ agrees with $M$ at $u'$, then $u = u'$.

So $M$ is injective on geometric fibres if it is injective after restriction to the $S$-schemes that lie over a geometric point of $S$. This is the condition that one can check from the universal property of a representative over a cover, as in Lemma (Injectivity from a lift) below.

**Definition 1.7.2 (Chart).** Let $U$ be an $S$-scheme and $M$ an additive family on $A \times U$. We say that $M$ is a *chart* if $M$ is injective and the following holds for each $S$-scheme $T$ and each additive family $N$ on $A \times T$. There is an open set $W \subseteq T$ such that for each $S$-scheme $Y$ and each $y \in T(Y)$,
$$\text{there is } u \in U(Y) \text{ such that } N \text{ at } y \text{ agrees with } M \text{ at } u \iff y(Y) \subseteq W.$$

Let $D$ be the functor that sends $T$ to the set of additive families on $A \times T$ up to isomorphism. The family $M$ gives a map of functors $U \to D$, and $M$ is injective if and only if this map is injective. The second condition says that for each $N \in D(T)$ the fibre product $U \times_D T$ is the open subscheme $W$ of $T$. So $M$ is a chart if and only if $U \to D$ is representable by open immersions. If $D$ is represented by $B$, a chart is the same as an open immersion $U \to B$ with $M$ the pullback of the universal bundle.

We use six facts.

1. (Injectivity.) Let $U$ be locally of finite type over $S$ and $M$ an additive family on $A \times U$ that is injective on geometric fibres. Then $M$ is injective.
2. (Affine test schemes.) Let $M$ be an injective additive family on $A \times U$. If the condition of a chart holds for each affine $T$, it holds for each $T$.
3. (Test schemes of finite type.) Let $M$ be an additive family on $A \times U$. If the condition of a chart holds for each affine $T$ that is locally of finite type over $S$, it holds for each affine $T$.
4. (Charts from lifts.) Let $U$ be locally of finite type over $S$, $M$ an injective additive family on $A \times U$, and $T$ an affine $S$-scheme, locally of finite type. Let $N$ be an additive family on $A \times T$. Suppose that fact 5 holds, and that the following lifting property holds. For each local Artinian ring $B$ with maximal ideal $\mathfrak{m}$, each ideal $I \subseteq \mathfrak{m}$ with $\mathfrak{m} I = 0$, each $y : \mathrm{Spec}\, B \to T$ and each $u_0 : \mathrm{Spec}\, B/I \to U$ over $S$ such that $N$ at $y|_{B/I}$ agrees with $M$ at $u_0$, there is $u : \mathrm{Spec}\, B \to U$ such that $N$ at $y$ agrees with $M$ at $u$. Then the condition of a chart holds for $T$ and $N$.
5. (Open immersions.) Let $f : X \to Y$ be a monomorphism of schemes, locally of finite type, with $Y$ locally noetherian. Suppose that for each $B$, $\mathfrak{m}$ and $I$ as in fact 4, each $a : \mathrm{Spec}\, B/I \to X$ and $b : \mathrm{Spec}\, B \to Y$ with $f \circ a = b|_{B/I}$, there is $l : \mathrm{Spec}\, B \to X$ with $l|_{B/I} = a$ and $f \circ l = b$. Then $f$ is an open immersion.
6. (Smooth families lift.) Let $U$ be smooth of relative dimension $g$ over $S$ and $M$ an injective additive family on $A \times U$. Then for each $S$-scheme $T$ and each additive family $N$ on $A \times T$, the lifting property of fact 4 holds.

Fact 5 says that a monomorphism that satisfies the infinitesimal lifting criterion for small extensions of Artinian rings is étale, and an étale monomorphism is an open immersion. In fact 4 the map $U \times_D T \to T$ is a monomorphism, and the lifting property is the lifting criterion for it. Fact 6 is where the dimensions enter: the tangent space of the dual of a geometric fibre $A_s$ is $H^1(A_s, \mathcal{O})$, of dimension $g$, so an injective smooth family of relative dimension $g$ cannot miss a first-order deformation. Note that in fact 6 the lift $u$ need not restrict to $u_0$; by injectivity it does so after the fact.

**Theorem 1.7.3 (Open chart).** Let $U$ be an $S$-scheme, smooth of relative dimension $g$, and let $M$ be an additive family on $A \times U$ that is injective on geometric fibres. Then $M$ is a chart.

Lean: `GlobalTheory.ChartCrit.openChart` (also `GlobalTheory.T.openChart_of_smoothFamily_geomFibreInjective`, a second name).

*Proof.* A smooth morphism is locally of finite type, so $U$ is locally of finite type over $S$. By fact 1, $M$ is injective. Let $T$ be an $S$-scheme and $N$ an additive family on $A \times T$. By fact 2 we may assume that $T$ is affine, and by fact 3 that $T$ is also locally of finite type over $S$. Fact 5 holds, and by fact 6 the lifting property of fact 4 holds for $T$ and $N$. So fact 4 gives the open set $W$. $\square$

Now let $S'$ be an $S$-scheme and $(b : B \to S', P)$ a representative of the dual of $A$ over $S'$.

**Definition 1.7.4 (Local lift).** Let $x \in B$. A *local lift at $x$* consists of an $S$-scheme $U$, smooth of relative dimension $g$, an additive family $M$ on $A \times U$, and a morphism $j : U \times S' \to B$ with these properties: $b \circ j$ is the projection to $S'$, $j$ is an open immersion, $x$ lies in the image of $j$, and $M$ at the projection $\mathrm{pr}_U$ agrees with $P$ at $j$, as points of $U(U \times S')$ and $B(U \times S')$.

So near $x$ the representative over $S'$ is the base change to $S'$ of a smooth family $U$ over $S$. The pinching proof of the next section constructs such lifts.

**Lemma 1.7.5 (Injectivity from a lift).** Suppose that $S' \to S$ is finite and surjective. Let $(U, M, j)$ be a local lift at some point of $B$. Then $M$ is injective on geometric fibres.

Lean: `GlobalTheory.DualCon.fibInj`.

*Proof.* Let $K$, $s$, $Y \to \mathrm{Spec}\, K$ and $u, u' \in U(Y)$ be as in the definition, with $M$ at $u$ agreeing with $M$ at $u'$. Since $S' \to S$ is finite and surjective, $s$ lifts to $t : \mathrm{Spec}\, K \to S'$: the residue field at a point of $S'$ over the image of $s$ is a finite extension of the residue field below, so it embeds in $K$. Let $y' \in S'(Y)$ be the composite $Y \to \mathrm{Spec}\, K \to S'$. The points $j(u, y')$ and $j(u', y')$ of $B(Y)$ both lie over $y'$. Pulling back the agreement of $M$ and $P$ along $(u, y')$ shows that $P$ at $j(u, y')$ agrees with $M$ at $u$, and the same holds for $u'$. So $P$ at $j(u, y')$ agrees with $P$ at $j(u', y')$. By the uniqueness in the definition of a representative, $j(u, y') = j(u', y')$. An open immersion is a monomorphism, so $(u, y') = (u', y')$ and $u = u'$. $\square$

We use four more facts.

7. (Gluing charts.) Let $(U_i, M_i)_{i \in I}$ be charts. Suppose that for each algebraically closed field $K$, each $s : \mathrm{Spec}\, K \to S$ and each additive family $N$ on $A \times \mathrm{Spec}\, K$ there are $i$ and $u \in U_i(K)$ such that $N$ agrees with $M_i$ at $u$. Then there are an $S$-scheme $B_0$, a line bundle $P_0$ on $A \times B_0$ and open immersions $j_i : U_i \to B_0$ that cover $B_0$, such that $(B_0 \to S, P_0)$ is a representative over $S$ and $M_i$ agrees with $P_0$ at $j_i$.
8. (Base change.) Let $(b : B \to S', P)$ be a representative over $S'$, and let $B'' = B \times_{S'} S''$ for a morphism $S'' \to S'$, with $k : B'' \to B$. Then $(B'' \to S'', k^* P)$ is a representative over $S''$.
9. (Uniqueness.) Two representatives $(b, P)$ and $(b', P')$ over $S'$ are isomorphic: there is an isomorphism $e : B \to B'$ over $S'$ such that $P$ agrees with $P'$ at $e$.
10. (Descent of good morphisms.) Let $f : X \to Y$ be smooth of relative dimension $g$, let $q : Y' \to Y$ be finite and surjective, and let $f' : X \times_Y Y' \to Y'$ be the base change. If $f'$ is proper with geometrically connected fibres, so is $f$.

Fact 7 is the gluing of the open pieces $U_i$ of the functor $D$ along their overlaps; the hypothesis says that the pieces cover $D$ on geometric points. Facts 8 and 9 are formal consequences of the universal property. In fact 10, a closed set of $X$ has the same image in $Y$ as its preimage in $X \times_Y Y'$ has under the finite map to $Y$, so the [[proper|9537RKBZPP]] property descends, and each geometric fibre of $f$ is a geometric fibre of $f'$.

**Theorem 1.7.6 (Descent from a finite cover).** Let $S' \to S$ be finite and surjective, and let $(b : B \to S', P)$ be a good representative of dimension $g$ over $S'$. Suppose that there is a local lift at each point of $B$. Then $\mathrm{Rep}_g(A, S)$ holds.

Lean: `GlobalTheory.DualCon.hasRep_of_liftAt` (also `GlobalTheory.T.representingScheme_of_finite_surjective_lift`, a second name).

*Proof.* For each $x \in B$ choose a local lift $(U_x, M_x, j_x)$ at $x$. By Lemma (Injectivity from a lift), $M_x$ is injective on geometric fibres, and by Theorem (Open chart) it is a chart.

We check the hypothesis of fact 7 for the family $(U_x, M_x)_{x \in B}$. Let $K$, $s$ and $N$ be given. Lift $s$ to $t : \mathrm{Spec}\, K \to S'$, as in the proof of the lemma. The universal property of $(b, P)$ gives $z \in B(K)$ over $t$ with $N \cong P_z$. Let $x$ be the image of the point of $\mathrm{Spec}\, K$ under $z$. Since $x$ lies in the open image of $j_x$, the point $z$ factors through $j_x$ as $z = j_x(u, t)$ with $u \in U_x(K)$. Then $N \cong P_z \cong (M_x)_u$, so $N$ agrees with $M_x$ at $u$.

Fact 7 gives $B_0$, $P_0$ and $j_x : U_x \to B_0$. The $j_x$ form an open cover of $B_0$, and $j_x$ followed by $B_0 \to S$ is $U_x \to S$, which is smooth of relative dimension $g$. This property is local on the source, so $B_0 \to S$ is smooth of relative dimension $g$.

By fact 8, $B_0 \times S' \to S'$ with the pullback of $P_0$ is a representative over $S'$. By fact 9 it is isomorphic over $S'$ to $(b, P)$. So $B_0 \times S' \to S'$ is proper, smooth of relative dimension $g$, with geometrically connected fibres. By fact 10, applied to the square of $B_0 \to S$ and $S' \to S$, the morphism $B_0 \to S$ is proper with geometrically connected fibres. So $(B_0 \to S, P_0)$ is a good representative of dimension $g$ over $S$. $\square$

**Remark 1.7.7 (Formalization).** Facts 1 to 6 are `GlobalTheory.T.lineBundleFamilyParamInjective_of_geomFiberInjective`, `GlobalTheory.T.lineBundleFamilyChart_of_affine_parameters`, `GlobalTheory.T.additiveFamily_chart_affine_of_chart_finiteType`, `GlobalTheory.T.lineBundleFamily_openChart_affine_finiteType`, `GlobalTheory.T.isOpenImmersion_of_mono_lift_smallArtinExtensions` and `GlobalTheory.T.smoothInjectiveFamily_lifts_small_artinian`. Facts 7 to 10 are `GlobalTheory.T.glue_openCharts_additiveFamilies_representing`, `GlobalTheory.T.rep_ev_of_isPullback`, `GlobalTheory.DualCon.rep_unique` and `GlobalTheory.T.properSmoothGeomConnected_descend_finite_surjective`. Facts 1 to 10 are cited by their statements; the sentences on why they hold are not read from proofs. Fact 4 takes fact 5 as a hypothesis, and the proof of Theorem (Open chart) passes fact 5 to it ([OpenChartOfSmoothFamilyGeomFibreInjective.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/OpenChartOfSmoothFamilyGeomFibreInjective.lean#L35)). The relative dimension $g$ of $A$ enters only through fact 6. The lift of a geometric point is `GlobalTheory.DualCon.exists_lift`, and the factorization through $j_x$ is `GlobalTheory.DualCon.exists_point`. The proof drops the last output of fact 7, the agreement of $M_i$ with $P_0$ at $j_i$. The family of charts is indexed by all points of $B$. The second names are closed by a `first` list under `set_option maxHeartbeats 1000000`.
