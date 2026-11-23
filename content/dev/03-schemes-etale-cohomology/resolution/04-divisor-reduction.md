---
title: Divisor reduction
decls:
  - FunctorialResolution.EmbeddedResolution.divisorReductionProperties_of_blowupPreservesNoetherian
  - FunctorialResolution.EmbeddedResolution.divisorReductionStepProperties_canonicalAlgorithmRules
  - FunctorialResolution.EmbeddedResolution.divisorReductionHypotheses_canonicalAlgorithmRules
  - FunctorialResolution.EmbeddedResolution.isBoundaryDivisorReduction_divisorFamily_canonicalAlgorithmRules
  - FunctorialResolution.EmbeddedResolution.isBoundaryPositionInvariant_divisorFamily_canonicalAlgorithmRules
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Divisor reduction

This section constructs the canonical divisor reduction and proves that it meets the third and fourth specifications. Let $T = (k, X, I, m, E)$ be admissible, bounded by its mark and balanced, and let $D = V(E_j)$ be the boundary divisor in position $j$. The sequence restricts $T$ to $D$, takes the sequence that the input level gives to the restriction, and pushes it forward to $X$. Since $D$ has smaller dimension, this is the step where the induction on dimension uses a smaller case. The results give conditions 1 and 2 of the Definition (Reduces inductively on dimension) for the canonical rules, and Section 7 uses them in the proof of correctness.

Two facts about blow-ups enter as hypotheses. The first, $\mathrm{(ST)}$, says that strict transforms are blow-ups: let $X$ be locally noetherian, $j \colon S \to X$ a closed immersion, $\pi \colon X_1 \to X$ a blow-up along $Z$, and assume that no irreducible component of $S$ maps into $Z$. Then there is $\psi$ from the strict transform $S'$ of $S$ to $S$ with $\psi \circ j = \pi$ on $S'$, and $\psi$ is a blow-up of $S$ along $j^{-1}Z$. This is [Hartshorne, II.7.15]. The second, $\mathrm{(N)}$, says that a blow-up of a noetherian scheme is noetherian. The chapter proves both. The proof of $\mathrm{(N)}$ is short, and the proof of $\mathrm{(ST)}$ is a computation in the charts of the blow-up. The results of this section keep $\mathrm{(ST)}$ as a hypothesis, and Section 8 inserts its proof.

**Definition 8.4.1 (Contained components).** Let $T$ be as above and $j$ less than the length of $E$, and write $\iota \colon D \to X$ for the inclusion of $D = V(E_j)$. Let $U \subseteq D$ be the set of points $x$ whose connected component lies in $\iota^{-1}\operatorname{cosupp}(I, m)$. If $U$ is open, the *contained components ideal* $\mathcal{Z}_j$ is the ideal of the image of $U$ in $X$. If $U$ is not open, then $\mathcal{Z}_j$ is the unit ideal.

So $V(\mathcal{Z}_j)$ is the union of the connected components of $D$ on which $I$ has order at least $m$ everywhere. It is empty exactly when $\mathcal{Z}_j$ is the unit ideal and $U$ is open. On an admissible $T$ the scheme $D$ is smooth and noetherian, so its connected components are open, $U$ is open, and $V(\mathcal{Z}_j)$ is a union of components of a smooth divisor. In particular the identity of $X$ is a blow-up along $\mathcal{Z}_j$, with exceptional ideal $\mathcal{Z}_j$ itself.

**Definition 8.4.2 (Restriction to a boundary divisor).** Let $I_0$ be an ideal sheaf on $X$ and $E^0$ a list of ideal sheaves on $X$. The *restriction* of $T$ to $D$ with data $(I_0, E^0)$ is the marked ideal
$$\bigl(k,\ D,\ \iota^{-1}I_0,\ m,\ \iota^{-1}F\bigr),$$
where $F$ is the list $E^0$ with the entry in position $j$ deleted and then cut to its first $|E| - 1$ entries, and $\iota^{-1}F$ restricts each entry to $D$.

If $E^0 = E$, the cut does nothing. If $E^0$ is $E$ followed by one more entry, the cut deletes that last entry. Both cases occur below.

**Definition 8.4.3 (Divisor reduction sequence).** Let $T$ be a marked ideal and $L$ a marked sequence for each $S$ with $\delta(S) < \delta(T)$. The *divisor reduction sequence* $R_{\mathrm{div}}(T, L, j)$ is defined as follows.

1. If $j$ is at least the length of $E$, or $\operatorname{cosupp}(I, m)$ is empty, it is the empty sequence.
2. If $\mathcal{Z}_j$ is the unit ideal, let $S$ be the restriction of $T$ to $D$ with data $(I, E)$. The sequence is the pushforward of $L(S)$ along $\iota$.
3. Otherwise, if the identity of $X$ is a blow-up along $\mathcal{Z}_j$, let $I^{\flat}$ be the ideal with $\mathcal{Z}_j^m \cdot I^{\flat} = I$, and let $S$ be the restriction of $T$ to $D$ with data $(I^{\flat}, E')$, where $E'$ is the list of strict transforms of $E$ along the identity followed by $\mathcal{Z}_j$. The sequence starts with the blow-up of $X$ along $\mathcal{Z}_j$ and continues with the pushforward of $L(S)$.
4. In all other cases it is the empty sequence.

In cases 2 and 3 the pushforward is the result only if $\delta(S) < \delta(T)$, $X$ is noetherian, no centre of $L(S)$ contains an irreducible component of its level, and the pushed sequence is a marked sequence for $T$. If one of these fails, the result is again the empty sequence.

The *pushforward* of a sequence $D = D_0 \leftarrow D_1 \leftarrow \cdots$ along $\iota$ blows up $X$ along the image of the centre of $D_0$, then the new ambient scheme along the image of the centre of $D_1$ in the strict transform of $D$, and so on. By $\mathrm{(ST)}$ the strict transform of $D_t$ is the blow-up of $D_t$ along the centre, so it is $D_{t+1}$, and the construction continues. In case 3 the first step does not change $X$. It replaces $I$ by the residual ideal $I^{\flat}$ and adds $\mathcal{Z}_j$ to the boundary as an exceptional divisor. On the restriction the new divisor is cut away again, so that $S$ has a boundary of length $|E| - 1$, as in case 2.

The next theorem lists what the construction gives. It has fourteen parts, which we group.

**Theorem 8.4.4 (Properties of divisor reduction).** Assume $\mathrm{(ST)}$ and $\mathrm{(N)}$. Let $T$ be admissible, bounded by its mark and balanced, and let $j$ be less than the length of $E$. Let $S$ be the restriction of case 2 if $\mathcal{Z}_j$ is the unit ideal, and of case 3 otherwise.

1. $S$ is admissible.
2. Let $X$ be noetherian and let $s$ be a marked sequence for $S$ whose centres contain no irreducible component. Then the pushforward of $s$, preceded in case 3 by the blow-up along $\mathcal{Z}_j$, is a marked sequence for $T$. Along it, $\operatorname{ord}_x I_t \leq m$ at each level $t$ and each point $x$.
3. In the same situation, the controlled transform $I_t$ restricted to the $t$-th strict transform of $D$ is the ideal of $s$ at level $t$. If $s$ resolves $S$, then $\operatorname{cosupp}(I_n, m)$ at the last level $n$ misses the last strict transform of $D$.
4. The pushed sequences are compatible with flat pullback: for a flat map of noetherian schemes, the pushforward of the pulled back sequence on $D$ is a pullback of the pushed sequence, and a strict pullback if the sequence on $D$ is a strict pullback.
5. $\mathcal{Z}_j$ commutes with base change along a field extension and with pullback along smooth maps.
6. If $m = 1$ and $I$ is the ideal of $V(J)$ for an ideal $J$ on $D$, then $\mathcal{Z}_j$ is the unit ideal.

Lean: `FunctorialResolution.EmbeddedResolution.divisorReductionProperties_of_blowupPreservesNoetherian`.

*Proof.* Part 1. In case 2, no connected component of $D$ lies in $\operatorname{cosupp}(I, m)$. A component on which $\iota^{-1}I$ vanishes has infinite order, so $\iota^{-1}I$ is nonzero on each component. The restricted boundary keeps strict normal crossings on $D$, because $E$ has them on $X$. In case 3, write $I = \mathcal{Z}_j^m I^{\flat}$. The order of a product of ideals on a smooth scheme is the sum of the orders, and $\mathcal{Z}_j^m$ has order $m$ at each point of $V(\mathcal{Z}_j)$. Since $\operatorname{ord}_x I \leq m$, the residual $I^{\flat}$ is the unit ideal near $V(\mathcal{Z}_j)$. Near the other components of $D$ it equals $I$. So $\iota^{-1}I^{\flat}$ is again nonzero on each component.

Part 2. The pushed sequence is built one blow-up at a time. Along it the proof carries an invariant at each level $t$. Write $I_t$ for the controlled transform of $I_0$ with exponent $m$ and $K_{l,t}$ for the controlled transform of $\mathcal{D}^l I_0$ with exponent $m - l$, where $I_0 = I$ in case 2 and $I_0 = I^{\flat}$ in case 3. Let $D_t$ be the $t$-th strict transform of $D$. The invariant says that $X_t$ is smooth, that the boundary is in strict normal crossing position with $D_t$ in position $j$, that the restriction of the boundary without position $j$ is the boundary of $s$ at level $t$, and that
$$\mathcal{D}^n I_t \subseteq \sum_{l \leq n} \mathcal{D}_{D_t}^{\,n-l} K_{l,t} \qquad \text{for all } n < m.$$
At $t = 0$ the inclusion holds because the summand $l = n$ is $\mathcal{D}^n I_0 = K_{n,0}$. The step from $t$ to $t + 1$ is the [Theorem (Derivative estimate after a blow-up)](/entry/deriv-ideal-sheaf-iterate-le-bi-sup-log-deriv-ideal-sheaf-iterate-of-blowup/) with $H = D_t$, $K_0 = I_t$ and $K_l = K_{l,t}$. Its hypothesis $K_{l,t} \subseteq \mathcal{I}_{Z_t}^{m-l}$ comes from balance. The strict normal crossings at level $t + 1$ come from a lemma that lifts strict normal crossings with a divisor from the divisor to the ambient scheme. The logarithmic derivatives along $D_t$ are tangent to $D_t$, so the invariant compares the order of $I_t$ at points of $D_t$ with the order of its restriction. This shows that each centre of $s$, which lies in the order locus of the restricted ideal, lies in $\operatorname{cosupp}(I_t, m)$. So the pushed sequence is marked. A controlled transform along a marked sequence keeps the order at most $m$, which gives the bound.

Part 3 follows from the invariant at the last level and the fact that the restriction of a controlled transform to the strict transform is the controlled transform of the restriction. Part 4 uses that blow-up commutes with flat base change. Part 5 holds because connected components and the order locus are compatible with field extension and with smooth pullback. Part 6 holds because the image ideal of $V(J)$ has order $1$ only on $V(J)$, which contains no component of $D$ when $J$ is nonzero on components. $\square$

We read the statement, the invariant and its use of the derivative estimate. For the other parts we read the names and statements of the lemmas, not their proofs.

The input level only sees a part of this theorem. The step properties are the parts that concern the sequence for one $T$, with $\mathrm{(N)}$ replaced by its proof.

**Theorem 8.4.5 (Step properties of divisor reduction).** Assume $\mathrm{(ST)}$. For $T$ as above, $I = \mathcal{Z}_j^m \cdot J$ for some ideal $J$, the identity of $X$ is a blow-up along $\mathcal{Z}_j$, and parts 1, 2 and 3 of the Theorem (Properties of divisor reduction) hold.

Lean: `FunctorialResolution.EmbeddedResolution.divisorReductionStepProperties_canonicalAlgorithmRules`.

*Proof.* Apply the previous theorem with the proof of $\mathrm{(N)}$, and forget the parts that are not needed. The factorization $I = \mathcal{Z}_j^m J$ holds because $V(\mathcal{Z}_j)$ is a union of components of a smooth divisor inside $\operatorname{cosupp}(I, m)$. $\square$

The proof of correctness reads these facts through one collection, which also contains the compatibilities of divisor reduction with pullbacks.

**Theorem 8.4.6 (The divisor reduction facts hold).** Assume $\mathrm{(ST)}$. Then the following hold.

1. If $L$ is any assignment, $T$ is admissible with $j$ less than the length of $E$ and $\operatorname{cosupp}(I, m)$ nonempty, and $h \colon Y \to X$ is smooth with $\operatorname{cosupp}$ of the pulled back ideal empty, then the empty sequence on $Y$ is a pullback of $R_{\mathrm{div}}(T, L, j)$ along $h$.
2. Pushed sequences are compatible with smooth pullback and with base change along field extensions.
3. Smooth morphisms are flat.
4. A pullback with an empty centre is compatible with the deletion of that step.
5. The restriction to $D$ is unchanged if trivial entries are added to or deleted from the boundary.
6. The restriction to $D$ commutes with field base change.
7. The step properties above and the properties of pushed sequences hold.

Lean: `FunctorialResolution.EmbeddedResolution.divisorReductionHypotheses_canonicalAlgorithmRules`.

*Proof.* Each part is a separate lemma of the formalization, and the theorem collects them. Part 1 is the case where the sequence on $X$ is a pullback of an empty sequence on the order locus. Part 7 is the previous theorem. $\square$

With these facts the specifications follow. The key point is that, for $T$ bounded by its mark, balanced and with a nonempty order locus, none of the failure cases in the Definition (Divisor reduction sequence) occurs, so $R_{\mathrm{div}}(T, L, j)$ is the pushed sequence.

**Theorem 8.4.7 (Divisor reduction meets its specifications).** Assume $\mathrm{(ST)}$. Let $n \geq 0$ and let $L$ be a maximal order reduction for $\delta < n$ relative to some assignment $O$. Then for each $j$, the assignment $\operatorname{Div}_j(L)$ of the canonical rules is a divisor reduction at position $j$ for $\delta \leq n$ relative to $L$, and the family $(\operatorname{Div}_j(L))_j$ is position invariant for $\delta \leq n$.

Lean: `FunctorialResolution.EmbeddedResolution.isBoundaryDivisorReduction_divisorFamily_canonicalAlgorithmRules` (also `FunctorialResolution.EmbeddedResolution.isBoundaryPositionInvariant_divisorFamily_canonicalAlgorithmRules`).

*Proof.* Let $T$ satisfy the hypotheses of the specification, with $\delta(T) \leq n$. If $\operatorname{cosupp}(I, m)$ is empty, the sequence is empty, and part 1 of the previous theorem handles pullbacks. Otherwise the sequence is the pushforward of $L(S)$, preceded in case 3 by one blow-up. Since $\delta(S) < \delta(T) \leq n$, the sequence $L(S)$ resolves $S$ and has nonempty centres. The properties of divisor reduction then give condition 2 of the divisor reduction specification, and condition 4 with $b$ true exactly in case 3. The pushforward condition 3 is part 6 of that theorem together with the pushforward condition for $L$. The pullback conditions come from those of $L$, from part 5 and from part 4. For position invariance, the restriction $S$ depends only on $D$ and the nontrivial entries of $E$, so $L(S)$ is the same for both lists, up to isomorphism. $\square$

**Remark 8.4.8 (Formalization).** The construction is `divisorReductionSeq` in [DivisorReductionSequence.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/DivisorReduction/DivisorReductionSequence.lean#L173). It returns the empty marked sequence in five different places (lines 173 to 196 and in `liftSeqFromDivisor`), so the definition is total and the content is in the proofs that these branches do not occur. Case 3 is a "blow-up" along $\mathcal{Z}_j$ by the identity morphism, and the twisted boundary is cut back by `take` at line 125, which removes the new exceptional entry only because it is last. The definition also pulls $I$ and $E$ back along the identity of $X$ several times. The fourteen parts of the first theorem are the fields of `DivisorReductionProperties`; the text groups them. The step properties theorem is private ([CanonicalDivisorReduction.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/DivisorReduction/CanonicalDivisorReduction.lean#L151)) and is a projection of the first theorem. The structure `DivisorReductionHypotheses` is a list of proved facts, not of assumptions. In `DivisorReductionHypotheses.divisorReductionSeqEqAmbient` the hypotheses `_hL` and `_hdim` are unused. The invariant of the proof of part 2 is `GoingUpInvariant`, whose field `deriv_le` is the inclusion of the text.
