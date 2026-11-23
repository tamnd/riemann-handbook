---
title: Hironaka's theorem
decls:
  - FunctorialResolution.EmbeddedResolution.strongResolutionOfSingularitiesCharZero_of_principalizationAlgorithm
  - FunctorialResolution.EmbeddedResolution.strongResolutionOfSingularitiesCharZero_of_affineResolutionRule
  - FunctorialResolution.EmbeddedResolution.strongResolutionOfSingularitiesCharZero
  - FunctorialResolution.functorialResolutionCharZero
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Hironaka's theorem

This section proves the main theorem of the chapter: strong and functorial resolution of singularities for reduced schemes of finite type over a field of characteristic $0$. The affine resolutions of Section 8 are glued along étale covers. Their compatibility with open immersions, étale covers, field extensions and smooth maps, which rests on Section 9, makes the glued sequence well defined and functorial. The result is then copied into the form of the statement that the rest of the proof uses.

Throughout, $k$ is a field of characteristic $0$, and all schemes over $k$ are reduced, locally of finite type and quasi-compact over $k$.

**Definition 8.10.1 (Sequence of blow-ups).** A *sequence of blow-ups* of a scheme $X$ is a number $n$, the *length*, a tower of schemes $\cdots \to X_2 \to X_1 \to X_0$ with an isomorphism $X_0 \cong X$, and closed subschemes $Z_i \subseteq X_i$, the *centres*, such that $X_{i+1} \to X_i$ is the blow-up of $X_i$ along $Z_i$ for each $i < n$. A centre is *empty* if its ideal is the unit ideal. Then the blow-up is an isomorphism.

**Definition 8.10.2 (Pullbacks of sequences).** Let $\varphi \colon X' \to X$ be a map, $s$ a sequence of blow-ups of $X$ of length $n$, and $s'$ a sequence of blow-ups of $X'$ of length $n'$.

1. $s'$ is a *strict pullback* of $s$ along $\varphi$ if $n' = n$ and there are maps $X'_i \to X_i$, compatible with $\varphi$ at level $0$, such that each square formed by two consecutive levels is cartesian and each centre $Z'_i$ is the inverse image of $Z_i$.
2. $s'$ is a *pullback* of $s$ along $\varphi$ if there is a strictly increasing map $r \colon \{0, \dots, n'\} \to \{0, \dots, n\}$ with $r(n') = n$, such that $X'_i$ is isomorphic to $X' \times_X X_{r(i)}$ compatibly with the maps, each centre $Z'_i$ is the inverse image of $Z_{r(i)}$, and the levels $j < n$ whose centre has a nonempty inverse image in $X' \times_X X_j$ are exactly the levels $r(i)$ with $i < n'$.

So a pullback is a strict pullback with the blow-ups along empty centres removed.

**Definition 8.10.3 (Resolution rules).** A *resolution rule* $R$ assigns a sequence of blow-ups $R(X)$ to each field $k$ of characteristic $0$ and each scheme $X$ over $k$. It is a *strong resolution rule* if each $R(X)$ is a strong resolution of $X$ in the sense of Section 8. It is *compatible with smooth morphisms* if, for every map $\varphi \colon X' \to X$ over $k$ that is smooth of some relative dimension $r$, the sequence $R(X')$ is a pullback of $R(X)$ along $\varphi$. It is *compatible with field extensions* if, for every extension $K$ of $k$ of characteristic $0$ such that $X_K$ is reduced, the sequence $R(X_K)$ is a pullback of $R(X)$ along $X_K \to X$.

An *affine resolution rule* $B$ is the same for affine schemes only. We use four conditions on $B$:

1. *open immersions*: for an open immersion $V \to Y$ over $k$ of affine schemes, $B(V)$ is a pullback of $B(Y)$;
2. *étale covers*: for an étale surjective map $W \to Y$ over $k$ of affine schemes, $B(W)$ is a strict pullback of $B(Y)$;
3. *field base change*: for an extension $K$ of $k$ of characteristic $0$ with $Y_K$ reduced, $B(Y_K)$ is a strict pullback of $B(Y)$;
4. *smooth maps*: for a map $V \to Y$ over $k$ of affine schemes that is smooth of some relative dimension $r$, $B(V)$ is a pullback of $B(Y)$.

A sequence $s$ of blow-ups of a scheme $X$ is *induced by $B$* if, for every affine $W$ and every étale surjective map $W \to X$ over $k$, $B(W)$ is a strict pullback of $s$.

First, a general gluing theorem.

**Theorem 8.10.4 (Gluing of affine resolutions).** Let $B$ be an affine resolution rule that satisfies the four conditions above, such that $B(Y)$ is a strong resolution of $Y$ for every affine $Y$. Then there is a resolution rule that is a strong resolution rule, compatible with smooth morphisms and compatible with field extensions.

Lean: `FunctorialResolution.EmbeddedResolution.strongResolutionOfSingularitiesCharZero_of_affineResolutionRule`.

*Proof.* Let $Y$ be affine. By condition 1 for the identity of $Y$, $B(Y)$ is a pullback of itself. In such a pullback the map $r$ is strictly increasing from $\{0, \dots, n\}$ to itself, so it is the identity. So every centre of $B(Y)$ has a nonempty inverse image, and no centre of $B(Y)$ is empty.

Let $X$ be a scheme over $k$. With nonempty centres and condition 2, the project proves that there is a sequence of blow-ups of $X$ with nonempty centres that is induced by $B$. The proof covers $X$ by finitely many affine opens, since $X$ is quasi-compact, and works with an affine étale cover of their disjoint union. We read the start of this construction but not all of it. Choose such a sequence $R(X)$ for each $X$. This gives a resolution rule $R$.

Compatibility of $R$ with smooth morphisms follows from condition 4, and compatibility with field extensions follows from conditions 1 and 3. The project proves both for every rule induced by $B$.

Now let $X$ be affine. Take an affine étale surjective cover $g \colon W \to X$. Then $B(W)$ is a strict pullback of $R(X)$ because $R(X)$ is induced by $B$, and a strict pullback of $B(X)$ by condition 2. Since $g$ is flat and surjective, a strict pullback along $g$ determines the sequence up to isomorphism. So $R(X)$ is isomorphic to $B(X)$. A sequence isomorphic to a strong resolution is a strong resolution, so $R(X)$ is a strong resolution of $X$.

Let $X$ be arbitrary, and cover it by the affine opens $U_i$ of its standard affine cover. Each open immersion $U_i \to X$ is smooth of relative dimension $0$. So $R(U_i)$ is a pullback of $R(X)$ along $U_i \to X$, by the compatibility with smooth morphisms. Each $R(U_i)$ is a strong resolution of $U_i$ by the affine case. The project proves that a sequence with such an open cover, whose restrictions are pullbacks and strong resolutions, is a strong resolution. So $R(X)$ is a strong resolution of $X$. $\square$

The next theorem builds such a rule $B$ from a principalization algorithm.

**Theorem 8.10.5 (Resolution from principalization).** Let $\mathcal{A}$ be a principalization algorithm. Assume:

1. every affine scheme $Y$ locally of finite type over $k$ has a closed immersion $e \colon Y \to \mathbb{A}^n_k$ over $k$ whose ideal is nonzero on each component;
2. the empty list of divisors is in strict normal crossing position on $\mathbb{A}^n_k$, and $\mathbb{A}^n_k$ is smooth over $k$;
3. $\mathcal{A}$ is a functorial principalization algorithm;
4. for every embedding datum, the transitions of the induced sequence of Section 8 are blow-ups, and the same holds for the embedding into affine space of item 1;
5. two closed immersions $e_1 \colon Y \to \mathbb{A}^n_k$ and $e_2 \colon Y \to \mathbb{A}^m_k$ over $k$ are related by an automorphism of $\mathbb{A}^{n+m}_k$ over $k$, which carries the map $(e_1, 0)$ to the map $(0, e_2)$;
6. for every affine $Y$, the induced sequence for the embedding of item 1, with the blow-ups along empty centres removed, is a strong resolution of $Y$.

Then there is a resolution rule that is a strong resolution rule, compatible with smooth morphisms and compatible with field extensions.

Lean: `FunctorialResolution.EmbeddedResolution.strongResolutionOfSingularitiesCharZero_of_principalizationAlgorithm`.

*Proof.* Let $B(Y)$ be the induced sequence for the embedding of item 1, with the blow-ups along empty centres removed. Item 6 says that each $B(Y)$ is a strong resolution. The project proves the four conditions for $B$ from items 1 to 5, in four lemmas. The lemma for smooth maps applies the smooth pullback theorem of Section 9, and the lemmas for open immersions and étale covers use the local ambient embedding of Section 9. Item 5 is an argument of all four lemmas. Apply the gluing theorem. $\square$

**Theorem 8.10.6 (Strong resolution of singularities).** There is a resolution rule $R$ such that, for every field $k$ of characteristic $0$ and every reduced scheme $X$, locally of finite type and quasi-compact over $k$, with composite $\pi \colon X_n \to X$:

1. $X_n$ is smooth over $k$, and $\pi$ is proper;
2. $\pi$ is an isomorphism over the smooth locus of $X$, and the inverse image of the smooth locus is dense in $X_n$;
3. every centre maps into $\operatorname{Sing}(X)$, and the reduced inverse image of $\operatorname{Sing}(X)$ in $X_n$ is a strict normal crossings divisor;
4. $R$ is compatible with smooth morphisms and with field extensions.

Lean: `FunctorialResolution.EmbeddedResolution.strongResolutionOfSingularitiesCharZero`.

*Proof.* Apply the previous theorem to the canonical principalization $\mathcal{P}$ of Section 8. The project proves each hypothesis. Items 1 and 2 are facts on affine space. Item 3 is the functoriality of $\mathcal{P}$, from Section 3 and the correctness of the canonical rules in Section 7. Item 4 is proved for $\mathcal{P}$ and every embedding datum. Item 5 is the comparison of two closed immersions into affine space; we read its statement only. Item 6 is the [strong resolution of affine schemes](/entry/is-strong-resolution-canonical-affine-resolution-rule/). $\square$

The rest of the proof uses the theorem in a second form, with other names for the same notions.

**Theorem 8.10.7 (Functorial resolution in characteristic zero).** There is a rule that assigns to each field $k$ of characteristic $0$ and each reduced scheme $X$, locally of finite type and quasi-compact over $k$, a sequence of blow-ups of $X$ with the properties 1 to 4 of the previous theorem.

Lean: `FunctorialResolution.functorialResolutionCharZero`.

*Proof.* Take the rule $R$ of the previous theorem. Copy each sequence $R(X)$ field by field into a sequence of blow-ups of the second form: length, tower, isomorphism at level $0$, centres and blow-up property. The definitions of the six conditions and of the two compatibilities in the second form agree with the first form by definition, so the three properties of $R$ hold with no change. $\square$

**Remark 8.10.8 (Formalization).** The theorem `strongResolutionOfSingularitiesCharZero` is in [HironakaTheorem.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/HironakaTheorem.lean#L69). It applies `strongResolutionOfSingularitiesCharZero_of_principalizationAlgorithm` ([GlobalResolutionFromAffine.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/StrongResolution/GlobalResolutionFromAffine.lean#L390)) to `principalizationWithRadicalCenters` and to proved facts. The facts `AffineEmbedsIntoAffineSpace`, `NilIsStrictNormalCrossingsOnAffineSpace` and `AffineSpaceIsSmooth` are theorems, but the general theorem takes them as arguments, and the affine rule `affineResolutionRuleOfPrincipalization` depends on them as data. The four compatibility lemmas are `isCompatibleWithEtaleCovers_…`, `isCompatibleWithOpenImmersions_…`, `isCompatibleWithFieldBaseChange_…` and `isCompatibleWithSmoothOfRelativeDimension_affineResolutionRule`; we read their names and statements only. `ExistsGluedBlowupSequence` and `InducedRuleCompatibleWithFieldExtension` are propositions, proved by `existsGluedBlowupSequence_of_center_ne_top` and `inducedRuleCompatibleWithFieldExtension`. The glued rule is chosen with `Exists.choose`, so it is not computed. `IsCompatibleWithFieldBaseChange` also asks that $Y_K$ be affine, as an instance argument, though this always holds. The statement used downstream, `FunctorialResolutionCharZero`, is in [Statements.lean](lean:Development/ResolutionOfSingularities/Statements.lean#L150), and `StrongResolutionOfSingularitiesCharZero` is in [ResolutionOfSingularities.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/ResolutionOfSingularities.lean#L151). They are two parallel families of definitions, such as `BlowupSequence` and `SequenceOfBlowups`, or `nonSmoothLocus` and `smoothLocusComplement`. The proof of `functorialResolutionCharZero` ([HasSimpleNormalCrossingsOfInStrictNormalCrossing.lean](lean:Development/ResolutionOfSingularities/HasSimpleNormalCrossingsOfInStrictNormalCrossing.lean#L15)) works because the two families agree by definition. The file name refers to other lemmas in the file, not to this theorem. Neither statement asks for separatedness.

## Notes and references

This chapter feeds the step [EveryCharacter from the literature and VWin](/step/every-character-of-literature/) of [the Weil bound](/proof/weil-bound/). There functorial resolution and the principalization of ideals in characteristic $0$ are inputs of the bound on covolumes, through the theorems `resolutionCharZero` and `resW` of the Lean folder `WeilBound/CoreStatements/ResolutionCharZero`. The background is in Volume 1, in [resolution and principalisation](/learn/geometry/#resolution-of-singularities). The top results are the [correctness of the canonical rules](/entry/is-correct-canonical-algorithm-rules/) and the theorem of this section.

The proof follows the route of Włodarczyk and of Kollár: principalization of marked ideals by induction on the dimension, through hypersurfaces of maximal contact, and resolution by the strict transforms of an embedded scheme.

- R. Hartshorne, *Algebraic Geometry*, Springer, 1977, Proposition II.7.15 (strict transforms under blow-ups).
- J. Kollár, *Lectures on Resolution of Singularities*, Annals of Mathematics Studies 166, Princeton University Press, 2007, Chapter 3, and §3.5 for maximal contact and the order reduction.
- J. Włodarczyk, Simple Hironaka resolution in characteristic zero, *J. Amer. Math. Soc.* 18 (2005), 779 to 822.
- H. Hironaka, Resolution of singularities of an algebraic variety over a field of characteristic zero I, II, *Ann. of Math.* 79 (1964), 109 to 326.
- E. Bierstone and P. Milman, Canonical desingularization in characteristic zero by blowing up the maximum strata of a local invariant, *Invent. Math.* 128 (1997), 207 to 302.
