---
title: Resolution of affine schemes
decls:
  - FunctorialResolution.EmbeddedResolution.centersLieOver_embeddedResolutionRuleOfPrincipalization
  - FunctorialResolution.EmbeddedResolution.toEmbeddedBlowupSequence_centersLieOver_smoothLocusComplement
  - FunctorialResolution.EmbeddedResolution.affineCentersLieOverSingularLocus_principalizationWithRadicalCenters
  - FunctorialResolution.EmbeddedResolution.isStrongResolution_canonicalAffineResolutionRule
  - FunctorialResolution.EmbeddedResolution.toEmbeddedBlowupSequence_center_eq_top_of_smooth
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Resolution of affine schemes

This section uses the canonical principalization to resolve a reduced affine scheme $Y$ of finite type over a field $k$ of characteristic $0$. We embed $Y$ as a closed subscheme of a smooth affine scheme $X$, principalize the ideal of $Y$ in $X$, and follow the strict transforms of $Y$. A component of a strict transform that lies in the centre would vanish under the next blow-up, so it is set aside as a *detached component* and kept. The main new result is that all centres of the induced sequence lie over the singular locus of $Y$. With it, the induced sequence is a strong resolution of $Y$. Section 10 glues these affine resolutions.

From this section on, $\mathcal{P}$ is the canonical principalization: the principalization of the canonical rules of Section 7, with $\mathrm{(ST)}$ and the radical property of smooth subschemes, both proved in the chapter. By Section 3 and Section 7 it is a functorial principalization algorithm.

**Definition 8.8.1 (Embedding datum).** Let $Y$ be a scheme over $k$ with structure map $p$. An *embedding datum* for $Y$ is a smooth, affine, quasi-compact scheme $X$ of finite type over $k$, with a closed immersion $e \colon Y \to X$ over $k$, such that the ideal of $Y$ in $X$ is nonzero on each component of $X$ and the empty list of divisors is in strict normal crossing position on $X$.

**Definition 8.8.2 (Induced sequence).** Let $(X, e)$ be an embedding datum and let $X_0 \leftarrow X_1 \leftarrow \cdots \leftarrow X_n$ be the principalization sequence $\mathcal{P}(X, \mathcal{I}_Y, ())$, with centres $Z_i$. Let $Y'_0 = Y$ in $X_0$ and let $Y'_{i+1}$ be the strict transform of $Y'_i$ in $X_{i+1}$.

1. A *detached component* at level $i$ is an irreducible component of $Y'_i$ whose image lies in $Z_i$. The detached scheme $D_i$ is the reduced closed subscheme on the closure of their union.
2. The *total space* at level $i$ is $Y_i = Y'_i \sqcup D_0 \sqcup \cdots \sqcup D_{i-1}$.
3. The map $Y_{i+1} \to Y_i$ is the strict transform map on $Y'_{i+1}$, the identity on $D_0, \dots, D_{i-1}$, and the inclusion $D_i \to Y'_i$ on $D_i$.
4. The centre on $Y_i$ is $Z_i \cap Y'_i$ with the detached locus removed, regarded as a closed subscheme of $Y_i$.

If every map $Y_{i+1} \to Y_i$ is the blow-up along this centre, these data form a sequence of blow-ups of $Y$, the *induced sequence*. The *resolution of $Y$ given by $(X, e)$* is the induced sequence with the blow-ups along empty centres removed.

Each $D_i$ lies in the centre $Z_i$, so it is smooth when the detached locus is open. The construction keeps $D_i$ because $Y'_{i+1}$ no longer contains it. The chapter proves that the transitions are blow-ups for $\mathcal{P}$ and every embedding datum, through the openness of the detached locus.

The first step is that a smooth $Y$ has nothing to resolve.

**Lemma 8.8.3 (Smooth case).** Let $(X, e)$ be an embedding datum for $Y$, and assume that $Y$ is affine, reduced and smooth over $k$. Assume that the transitions of the induced sequence are blow-ups. Then every centre of the induced sequence is empty, and the resolution of $Y$ given by $(X, e)$ has length $0$.

Lean: `FunctorialResolution.EmbeddedResolution.toEmbeddedBlowupSequence_center_eq_top_of_smooth`.

*Proof.* Let $y$ be a point of $Y'_t$ in $Z_t$. Since $Y$ is smooth, the proof shows that $y$ lies on a detached component. The detached locus is open, so the centre with the detached locus removed has empty support. So every centre of the induced sequence is empty, and the sequence without the blow-ups along empty centres has length $0$. $\square$

Now the general case. Let $\operatorname{Sing}(Y)$ be the complement of the smooth locus of $Y \to \operatorname{Spec} k$. It is closed, because the smooth locus is open.

**Theorem 8.8.4 (Centres over the singular locus, without trivial blow-ups).** Let $Y$ be affine, reduced, quasi-compact and of finite presentation over $k$, and let $(X, e)$ be an embedding datum for $Y$. Then every centre of the resolution of $Y$ given by $(X, e)$ maps into $\operatorname{Sing}(Y)$.

Lean: `FunctorialResolution.EmbeddedResolution.centersLieOver_embeddedResolutionRuleOfPrincipalization`.

*Proof.* Let $x$ be a point of the centre at level $i$, and assume that its image $y$ in $Y$ is a smooth point. The smooth locus is open, and the basic opens of the affine scheme $X$ form a basis. So there is $r \in \mathcal{O}(X)$ with $e(y) \in D(r)$ and $e^{-1}D(r)$ inside the smooth locus of $Y$. Put $V = e^{-1}D(r)$. Then $(D(r), e|_V)$ is an embedding datum for $V$: $D(r)$ is affine and smooth, and the empty list is in strict normal crossing position on a smooth scheme. The open immersion $D(r) \to X$ is smooth, and the square formed by $V \to Y$, $D(r) \to X$ and the two embeddings is cartesian.

Since $\mathcal{P}$ is functorial, the resolution of $V$ given by $(D(r), e|_V)$ is a pullback of the resolution of $Y$ given by $(X, e)$ along $V \to Y$. In a pullback, the centre at a level $i$ has a point over $V$ only if level $i$ corresponds to a level $j$ of the pulled-back sequence with $j$ less than its length. The point $x$ lies over $y \in V$, so such a $j$ exists. But $V$ is smooth, so by the Lemma (Smooth case) the pulled-back sequence has length $0$. This is a contradiction. $\square$

**Theorem 8.8.5 (Centres over the singular locus).** Let $Y$ and $(X, e)$ be as in the previous theorem, and assume that the transitions of the induced sequence are blow-ups. Then every centre of the induced sequence maps into $\operatorname{Sing}(Y)$.

Lean: `FunctorialResolution.EmbeddedResolution.toEmbeddedBlowupSequence_centersLieOver_smoothLocusComplement`.

*Proof.* A blow-up along an empty centre has an empty centre, so it adds no point. Every nonempty centre of a sequence of blow-ups is a centre of the sequence with the empty centres removed, at the same level of the base. Apply the previous theorem. $\square$

**Corollary 8.8.6 (Affine centres over the singular locus).** Let $Y$ be affine and reduced, of finite type and quasi-compact over $k$, with $\operatorname{char} k = 0$. Let $Y \to \mathbb{A}^n_k$ be the chosen closed immersion over $k$ whose ideal is nonzero on each component. Then every centre of the induced sequence for this embedding maps into $\operatorname{Sing}(Y)$.

Lean: `FunctorialResolution.EmbeddedResolution.affineCentersLieOverSingularLocus_principalizationWithRadicalCenters`.

*Proof.* Such an embedding exists for every affine $Y$ of finite type over $k$, and $\mathbb{A}^n_k$ is smooth, so it gives an embedding datum. The transitions are blow-ups. Apply the previous theorem. The canonical principalization is functorial by Section 3, with the closed immersion condition proved from the correctness of the canonical rules. $\square$

The induced sequence for the embedding into affine space is the *canonical affine resolution* of $Y$.

**Definition 8.8.7 (Strong resolution).** Let $Y$ be of finite type over $k$, and let $Y_n \to \cdots \to Y_0 = Y$ be a sequence of blow-ups with composite $\pi \colon Y_n \to Y$. It is a *strong resolution* of $Y$ if:

1. $Y_n$ is smooth over $k$;
2. $\pi$ is proper;
3. $\pi$ is an isomorphism over the smooth locus of $Y$;
4. the inverse image of the smooth locus is dense in $Y_n$;
5. every centre maps into $\operatorname{Sing}(Y)$;
6. the reduced inverse image of $\operatorname{Sing}(Y)$ in $Y_n$ is a strict normal crossings divisor.

**Theorem 8.8.8 (Strong resolution of affine schemes).** Let $k$ be a field of characteristic $0$ and let $Y$ be affine and reduced, of finite type and quasi-compact over $k$. Then the canonical affine resolution of $Y$, with the blow-ups along empty centres removed, is a strong resolution of $Y$.

Lean: `FunctorialResolution.EmbeddedResolution.isStrongResolution_canonicalAffineResolutionRule`.

*Proof.* The proof combines eleven conditions on the induced sequence for $\mathcal{P}$, which we group in six items:

1. the strict transform of $Y$ is empty at the last level, by the principalization of $\mathcal{I}_Y$;
2. the detached schemes are smooth, and the smooth locus of $Y$ has dense inverse image in each of them;
3. the centres map into $\operatorname{Sing}(Y)$, by the previous corollary;
4. each detached scheme is open and closed in the centre, and none of its components lies in the boundary;
5. the inverse image of $\operatorname{Sing}(Y)$ is the boundary;
6. the centres have strict normal crossings with the boundary, all levels are smooth, and the boundary is in strict normal crossing position.

By item 1, $Y_n$ is the disjoint union of the detached schemes, so it is smooth by item 2. Blow-ups are proper, so $\pi$ is proper. By item 3, no blow-up changes the part over the smooth locus, so $\pi$ is an isomorphism there. Item 2 gives density. Items 5 and 6, restricted to the open and closed pieces $D_i$, give the divisor condition. $\square$

**Remark 8.8.9 (Formalization).** The induced sequence is `EmbeddedBlowupSequence.inducedBlowups` in [EmbeddedBlowupSequence.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/StrongResolution/EmbeddedBlowupSequence.lean#L302), with `detachedComponents` and `totalSpace` in the same file. The definition takes the fact that the transitions are blow-ups as an argument, and the strict transform map is chosen by choice. The first theorem is private ([AffineCentersOverSingularLocus.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/StrongResolution/AffineCentersOverSingularLocus.lean#L413)), and the public results use it. The corollary uses `embeddedInducedBlowups_eq`, which says that the two ways to build the sequence for the affine space embedding agree by definition. The embedding into affine space comes from `AffineEmbedsIntoAffineSpace` by choice. `IsStrongResolution` ([StrongResolution.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/StrongResolution/StrongResolution.lean#L12)) asks for the six conditions above and no separatedness. The proof of the strong resolution theorem is an assembly of eleven named conditions in [HironakaTheorem.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/HironakaTheorem.lean#L26); we read their names but not their statements or proofs, so the proof sketch above follows the names.
