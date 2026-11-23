---
title: Order reduction by maximal contact
decls:
  - FunctorialResolution.EmbeddedResolution.OrderReductionProperties.orderReductionHypotheses
  - FunctorialResolution.EmbeddedResolution.OrderReductionProperties.coverSequenceProperties_of_isBoundaryDivisorReduction
  - FunctorialResolution.EmbeddedResolution.OrderReductionProperties.isStrictPullbackBlowupSeq_maxContact_baseChange
  - FunctorialResolution.EmbeddedResolution.OrderReductionProperties.maxContact_isPullback_of_smooth_of_orderAt_le_mult
  - FunctorialResolution.EmbeddedResolution.OrderReductionProperties.descentProperties_of_isBoundaryDivisorReduction
  - FunctorialResolution.EmbeddedResolution.OrderReductionProperties.isOrderReduction_maxContact_of_isBoundaryPositionInvariant
  - FunctorialResolution.EmbeddedResolution.OrderReductionProperties.isOrderReduction_orderFamily_of_strictTransformIsBlowup
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Order reduction by maximal contact

This section constructs the canonical order reduction and proves that it meets the second specification. The input is a family $(A_j)_{j \geq 0}$ of divisor reductions, as built in [Section 8.4.4](/entry/divisor-reduction-properties-of-blowup-preserves-noetherian/). The construction replaces $I$ by its balanced tuned ideal, chooses hypersurfaces of maximal contact on a finite open cover, separates the order locus from the old boundary with $A_0, \dots, A_{r-1}$, and then applies $A_0$ along the strict transform of the hypersurface. The result on the cover descends to $X$ by the étale equivalence of Section 5. The main theorem gives condition 4 of the Definition (Reduces inductively on dimension) for the canonical rules. Section 7 uses it.

Fix a marked ideal $T = (k, X, I, m, E)$ with $E = (E_0, \dots, E_{r-1})$.

**Definition 8.6.1 (Maximal contact cover).** Let $W$ be an ideal sheaf on $X$ and $\mu \geq 1$. A *maximal contact cover* for $(W, \mu)$ is a finite family of affine opens $U_i$ that cover $X$, with an ideal sheaf $H_i$ on each $U_i$, such that for each $i$ one of these holds:

1. $U_i$ does not meet $\operatorname{cosupp}(W, \mu)$ and $H_i$ is the unit ideal;
2. there is an étale map $c \colon U_i \to \mathbb{A}^n_k$ over $k$ and a coordinate $x_j$ with $H_i = (c^{*}x_j)$ and $c^{*}x_j \in \operatorname{MC}(W, \mu)(U_i)$.

So $H_i$ is a hypersurface of maximal contact on $U_i$. If $T$ is admissible and the balanced tuned ideal $W$ has order at most $N_m$ at every point, a maximal contact cover for $(W, N_m)$ exists.

**Definition 8.6.2 (Order reduction by maximal contact).** Let $(A_j)_{j \geq 0}$ be assignments. The sequence $R_{\mathrm{ord}}(T, A)$ is built as follows.

1. If $T$ is not admissible or $\operatorname{cosupp}(I, m)$ is empty, it is the empty sequence.
2. Delete the entries of $E$ that are the unit ideal. Let $W = W(I, m)$ be the balanced tuned ideal and $\mu = N_m$ its mark.
3. Choose a maximal contact cover $(U_i, H_i)$ for $(W, \mu)$. Let $U = \coprod_i U_i$ with the map $\rho \colon U \to X$, and let $S = (k, U, \rho^{-1}W, \mu, \rho^{*}E)$. Let $H$ be the ideal on $U$ that is $H_i$ on $U_i$.
4. *Separation.* Starting from the empty sequence on $S$, for $j = 0, 1, \dots, r - 1$ in turn, take the last level of the current sequence, form the marked ideal with the balanced tuned ideal of the controlled transform and its full boundary, and append the value of $A_j$ on it.
5. *Hypersurface step.* At the last level, form the marked ideal with the balanced tuned ideal of the controlled transform and the boundary $(H') \mathbin{+\!\!+} F$. Here $H'$ is the strict transform of $H$ and $F$ is the list of exceptional divisors made in step 4. Append the value of $A_0$ on it.
6. *Descent.* Choose a sequence of blow-ups of $X$ whose strict pullback along $\rho$ is the sequence on $U$. If it is a marked sequence for $T$, it is $R_{\mathrm{ord}}(T, A)$.

In steps 4 and 5 a sequence is appended only if its dimension is at most $\delta(T)$ and it is a marked sequence for $S$. If a choice in step 3 or step 6 does not exist, or the result of step 6 is not marked, the result is the empty sequence.

The idea is as follows. Each $A_j$ is a divisor reduction, so after step $j$ the order locus misses the strict transform of $E_j$. After step 4 it misses all old boundary divisors. Then the old boundary can be forgotten, and $H'$ is in strict normal crossing position with the new divisors. The order locus lies in $H'$, because $H'$ stays a hypersurface of maximal contact. Step 5 moves the order locus off $H'$, so the order locus becomes empty. Divisor reduction along $H'$ calls the input level on $H'$, which has smaller dimension.

The proofs use ten facts about blow-ups and pullbacks, collected in one theorem.

**Theorem 8.6.3 (Facts for order reduction).** The following hold.

1. Let $u$ be a marked sequence for $(V, A', \mu, E')$ with $V$ smooth over $k$ of characteristic $0$ and $\mu \geq 1$. Assume that its levels are locally noetherian and that every ideal whose support contains the support of a centre lies in that centre. Then there are ideals $c_i$ with $c_0 = \operatorname{MC}(A', \mu)$, $\mathcal{E}_{\pi_i} \cdot c_{i+1} = \pi_i^{-1} c_i$, and $c_i \subseteq \mathcal{I}_{Z_i}$.
2. The centres of a marked sequence map into $\operatorname{cosupp}(I, m)$.
3. Balance is preserved by smooth pullback.
4. An étale map to a locally noetherian scheme of finite dimension does not raise $\delta$.
5. The levels of a marked sequence on an admissible $T$ are locally noetherian.
6. Let $\pi$ be a blow-up along $Z$, let $f, g \colon S \to X$ with $f^{-1}Z = g^{-1}Z$, let $\rho$ be the blow-up of $S$ along $f^{-1}Z$, and let $f', g'$ be lifts of $f\rho$ and $g\rho$. If $f$ and $g$ agree on $V(a)$, and $\mathcal{E}_\rho \cdot c = \rho^{-1}a$, then $f'$ and $g'$ agree on $V(c)$.
7. If $Z$ is smooth over $k$ and $\operatorname{supp} Z \subseteq \operatorname{supp} V(J)$, then $J \subseteq \mathcal{I}_Z$.
8. The Theorem (Étale equivalence of hypersurfaces of maximal contact).
9. A pullback along $\varphi$ whose centres are nonempty and map into the image of $\varphi$ is a strict pullback.
10. Smooth pullback along a quasi-compact structure map preserves admissibility.

Lean: `FunctorialResolution.EmbeddedResolution.OrderReductionProperties.orderReductionHypotheses`.

*Proof.* Each part is a separate lemma and the theorem collects them. Part 1 says that the maximal contact ideal transforms with exponent $1$; it holds because $\operatorname{MC}(A', \mu)$ has order $1$ along each centre. Part 6 is the step that carries the agreement of two étale maps on the maximal contact locus up one blow-up. $\square$

Part 7 is the reducedness of smooth schemes. It is proved here as one of the facts, and it is the same statement as the radical hypothesis of the Theorem (Functorial principalization).

**Theorem 8.6.4 (Properties of the cover sequence).** Let $n \geq 0$ and let each $A_j$ be a divisor reduction at position $j$ for $\delta \leq n$ relative to $L$. Let $T$ be admissible with $\delta(T) \leq n$, bounded by its mark, with $\operatorname{cosupp}(I, m)$ nonempty. Let $s$ be the sequence on $U$ after step 5. Then:

1. every centre of $s$ is nonempty;
2. if $m = 1$, every centre of $s$ has an order certificate;
3. there is a sequence of blow-ups of $X$ whose strict pullback along $\rho$ is $s$;
4. if $E = ()$, $m = 1$, $e \colon Y \to X$ is a closed immersion whose ideal is a smooth divisor, $J$ is an ideal on $Y$ with $(k, Y, J, 1, ())$ admissible, and $I$ is the image ideal of $J$, then $s$ is the strict pullback along $\rho$ of $A_0(T, (\mathcal{I}_Y))$;
5. $s$ resolves the tuned marked ideal: $\operatorname{cosupp}(W_n, \mu) = \varnothing$ at its last level.

Lean: `FunctorialResolution.EmbeddedResolution.OrderReductionProperties.coverSequenceProperties_of_isBoundaryDivisorReduction`.

*Proof.* Parts 1, 2 and 5 follow the idea above. Condition 4 of each divisor reduction moves the order locus off one boundary divisor, part 1 of the facts keeps the order locus inside $H'$, and the last step empties it. Part 4 holds because with $m = 1$ the tuned ideal is $I$ itself and $V(I) \subseteq Y$, so $\mathcal{I}_Y$ is a hypersurface of maximal contact. Part 3 uses two facts: the balanced tuned ideal is MC-invariant, and the strict transform of a hypersurface of maximal contact stays one under smooth pullback. With the étale equivalence, these show that the sequences on two pieces $U_i$ and $U_{i'}$ agree over the overlap, so they come from one sequence on $X$. $\square$

Next come the two compatibilities with pullbacks. They are conditions of the order reduction specification for $R_{\mathrm{ord}}(-, A)$.

**Theorem 8.6.5 (Field base change).** Let $n$, $(A_j)$ and $L$ be as in the previous theorem, and let $T$ be admissible with $\delta(T) \leq n$ and bounded by its mark. Let $k \to K$ be a field homomorphism with $\operatorname{char} K = 0$, and let $E'$ be a list on $X_K$ with the same nontrivial part as $E_K$, such that $(T_K, E')$ is admissible with $\delta \leq n$. Then $R_{\mathrm{ord}}((T_K, E'), A)$ is a strict pullback of $R_{\mathrm{ord}}(T, A)$ along the projection $X_K \to X$.

Lean: `FunctorialResolution.EmbeddedResolution.OrderReductionProperties.isStrictPullbackBlowupSeq_maxContact_baseChange`.

*Proof.* The projection is flat and surjective. Orders and order loci are compatible with field extension, so $\operatorname{cosupp}$ for $T_K$ is the inverse image of $\operatorname{cosupp}$ for $T$. If it is empty, both sequences are empty. Otherwise the tuned ideal, a maximal contact cover and the divisor reductions pull back, the last by condition 1 of the divisor reduction specification. So the cover sequence for $T_K$ is a pullback of the one for $T$. Every centre is nonempty, so the pullback is strict. $\square$

**Theorem 8.6.6 (Smooth pullback).** Let $n$, $(A_j)$ and $L$ be as above, and assume also that $(A_j)$ is position invariant for $\delta \leq n$. Let $T$ be admissible with $\delta(T) \leq n$ and bounded by its mark. Let $h \colon Y \to X$ be smooth, and let $E'$ be a list on $Y$ with the same nontrivial part as $h^{*}E$, such that $(T_Y, E')$ is admissible with $\delta \leq n$ and bounded by $m$. Then $R_{\mathrm{ord}}((T_Y, E'), A)$ is a pullback of $R_{\mathrm{ord}}(T, A)$ along $h$.

Lean: `FunctorialResolution.EmbeddedResolution.OrderReductionProperties.maxContact_isPullback_of_smooth_of_orderAt_le_mult`.

*Proof.* The argument is the same as for field base change, with one change. A smooth pullback can make some entries of $E$ trivial. These are deleted in step 2, so the remaining divisors move to smaller positions. Position invariance says that $A_j$ does not see this shift. $\square$

These two theorems and twelve more facts form the descent properties.

**Theorem 8.6.7 (Descent properties).** Let $n$, $(A_j)$ and $L$ be as above, with $(A_j)$ position invariant for $\delta \leq n$. Then the following hold for $R_{\mathrm{ord}}(-, A)$ and $\delta \leq n$: the tuning properties; order certificates descend along surjective local isomorphisms; field base change gives a pullback and a strict pullback; smooth pullback gives a pullback, and a strict pullback when $h$ is surjective; the maps of a descended sequence to the cover sequence are local isomorphisms; all levels are locally noetherian; the descended sequence is marked for the tuned ideal; marking for the list without trivial entries implies marking for $E$; the order stays at most $m$; $\rho$ is flat and surjective; a hypersurface $Y$ with an admissible $J$ gives an admissible image ideal on $V(\mathcal{I}_Y)$ of the same $\delta$; with $m = 1$ the tuned ideal is $I$; and deleting trivial entries keeps admissibility.

Lean: `FunctorialResolution.EmbeddedResolution.OrderReductionProperties.descentProperties_of_isBoundaryDivisorReduction`.

*Proof.* The pullback parts are the two previous theorems. For a strict smooth pullback with $h$ surjective, a pullback whose centres are nonempty is strict. The centres are nonempty by part 1 of the Theorem (Properties of the cover sequence). Each other part is a separate lemma. $\square$

**Theorem 8.6.8 (Order reduction by maximal contact).** Let $n \geq 0$. Let $L$ be a maximal order reduction for $\delta < n$ relative to some $L'$. Let each $A_j$ be a divisor reduction at position $j$ for $\delta \leq n$ relative to $L$, and let $(A_j)$ be position invariant for $\delta \leq n$. Then $R_{\mathrm{ord}}(-, A)$ is an order reduction for $\delta \leq n$ relative to $L$.

Lean: `FunctorialResolution.EmbeddedResolution.OrderReductionProperties.isOrderReduction_maxContact_of_isBoundaryPositionInvariant` (also `FunctorialResolution.EmbeddedResolution.OrderReductionProperties.isOrderReduction_orderFamily_of_strictTransformIsBlowup`, the same statement for $\operatorname{Ord}(A)$ of the canonical rules).

*Proof.* Let $T$ satisfy the hypotheses of the specification. If $\operatorname{cosupp}(I, m)$ is empty, the sequence is empty, and each condition is checked directly for the empty sequence. Otherwise let $d$ be the descended sequence. It is a marked sequence for the tuned ideal $(W, \mu)$, so by the tuning properties it is a marked sequence for $(I, m)$ with the same order loci. Its last order locus pulls back to the last order locus of $s$, which is empty, and $\rho$ is surjective, so $d$ resolves $T$. Its centres pull back to nonempty centres, so they are nonempty. The order bound and the pullback conditions are among the descent properties. For $m = 1$ the order certificates of $s$ descend along the local isomorphism $\rho$. For the pushforward condition, part 4 of the cover sequence theorem identifies $d$ with $A_0(T, (\mathcal{I}_Y))$, and condition 3 of the divisor reduction specification says that $L(k, Y, J, 1, ())$ pushes forward to it. For the canonical rules, $\operatorname{Ord}(A)$ is $R_{\mathrm{ord}}(-, A)$ by definition. $\square$

**Remark 8.6.9 (Formalization).** The construction is `MaxContactReduction.reduceOrder` in [MaxContactReduction.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/OrderReduction/MaxContactReduction.lean#L220), with `separateBoundary`, `reduceAlongHypersurface` and `descendStrictPullback`. Steps 3 and 6 use choice, and five branches return the unchanged or the empty sequence, so the definition is total and the proofs show that these branches do not occur. The ten facts are `OrderReduction.OrderReductionHypotheses` in MaxContactGeometryHypotheses.lean (line 64). Two other structures in the same project have the name `OrderReductionHypotheses` (DescentHypotheses.lean line 39 and MarkedOrderReduction/OrderReductionHypotheses.lean line 196), with different contents. The descent properties are `MaxContactFunctoriality.DescentHypotheses` with sixteen fields; the text lists them in a shorter form. All these "hypotheses" structures are proved. In the descent theorem the binder `_hO'` at line 934 of OrderReductionCompatibility.lean is unused. The canonical version takes $\mathrm{(ST)}$ as an argument and does not use it ([OrderReductionCompatibility.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/OrderReduction/OrderReductionCompatibility.lean#L1011)). The proofs supply `ComapIsoInvariance`, which says that order loci, strict normal crossings and smoothness are invariant under isomorphisms; it is needed to append sequences.
