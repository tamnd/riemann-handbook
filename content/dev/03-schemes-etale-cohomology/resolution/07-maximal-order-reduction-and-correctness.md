---
title: Maximal order reduction and correctness of the canonical rules
decls:
  - FunctorialResolution.EmbeddedResolution.geometricHypotheses_of_orderReductionHypotheses
  - FunctorialResolution.EmbeddedResolution.principalizationGeometryHypotheses
  - FunctorialResolution.EmbeddedResolution.MaxOrderReduction.isMaxOrderReduction_orderReductionSeq
  - FunctorialResolution.EmbeddedResolution.MaxOrderReduction.isMaxOrderReduction_canonicalAlgorithmRules
  - FunctorialResolution.EmbeddedResolution.isCorrect_canonicalAlgorithmRules_of_hypotheses
  - FunctorialResolution.EmbeddedResolution.isCorrect_canonicalAlgorithmRules
  - FunctorialResolution.EmbeddedResolution.canonicalAlgorithmRules_isCorrect
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Maximal order reduction and correctness of the canonical rules

This section constructs the third canonical rule, maximal order reduction, and proves that the canonical rules reduce inductively on dimension. Maximal order reduction removes the condition "bounded by the mark" from order reduction. It writes $I = M \cdot N$, with $M$ monomial in the boundary and $N$ without monomial factors. It first reduces the order of $N$, then it uses a companion ideal to move the order locus of $N$ off the locus of order $m$ of $I$, and at the end it principalizes the monomial part. With Sections 4 and 6 this gives all four conditions of the Definition (Reduces inductively on dimension). The Theorem (Functorial principalization) of Section 3 then applies, and Sections 8 to 10 use the result.

Fix a marked ideal $T = (k, X, I, m, E)$.

**Definition 8.7.1 (Monomial splitting).** Let $E$ be a list of ideal sheaves on $X$ and $I$ an ideal sheaf. A *monomial splitting* of $I$ along $E$ is a pair $(M, N)$ of ideal sheaves such that:

1. $I = M \cdot N$;
2. the support of $V(M)$ lies in the union of the supports of the $V(E_i)$;
3. near each point, $M = \prod_i E_i^{a_i}$ for some exponents $a_i \geq 0$;
4. no irreducible component of any $V(E_i)$ lies in $V(N)$.

On an admissible marked ideal a monomial splitting exists and is unique; these are two of the facts below. We write $M(E, I)$ and $N(E, I)$ for the chosen pair, with the fallback $(\mathcal{O}_X, I)$ if no splitting exists.

**Definition 8.7.2 (Monomial principalization).** Let $T$ be a marked ideal. For a subset $J$ of the positions of $E$, let $E_J$ be the intersection of the $V(E_j)$ with $j \in J$. A component $C$ of $E_J$ is a *candidate* if $\operatorname{ord}_C I \geq m$, where the order is taken at the generic point of $C$. Let $r \geq 1$ be the smallest size of a $J$ with a candidate. Among the candidates for sets of size $r$, take those of largest order, and among their index sets take the one $J$ whose binary code $\sum_{j \in J} 2^{|E| - 1 - j}$ is largest. The *monomial centre* is the union of the candidates for $J$ of largest order, if it is open in $E_J$, and the empty centre otherwise. The *monomial principalization* blows up the monomial centre of the last level as long as the centre is nonempty, smooth, has strict normal crossings with the boundary, lies in the order locus and gives a controlled transform. It stops at the first step where the sequence does not grow.

**Definition 8.7.3 (Maximal order reduction by companion ideals).** Let $\mathcal{O}$ be an assignment. The sequence $R_{\max}(T, \mathcal{O})$ is built as follows. If $\operatorname{cosupp}(I, m)$ is empty, it is the empty sequence. Otherwise:

1. *Non-monomial part.* Start with the empty sequence. At each step, let $N$ be the non-monomial part of the ideal at the last level, along the current boundary, and let $b$ be the maximal order of $N$. If $b \geq m$ and the locus where $N$ has order $b$ is nonempty, append $\mathcal{O}$ applied to the marked ideal $(N, b)$ with the current boundary. Repeat this $b_0 + 1$ times, where $b_0$ is the maximal order of $N(E, I)$.
2. *Companion ideal.* At each step, let $N$ be as before and let $b$ be the maximal order of $N$ on $\operatorname{cosupp}(I_t, m)$, where $I_t$ is the ideal at the last level. If $b \geq 1$, append $\mathcal{O}$ applied to the marked ideal
$$\bigl(N^m + I_t^{\,b},\ m b\bigr)$$
with the current boundary. Repeat this $b_1 + 1$ times, where $b_1$ is the value of $b$ after step 1.
3. *Monomial part.* Append the monomial principalization of $(I_t, m)$ at the last level.

A sequence from $\mathcal{O}$ is appended only if its marked ideal has $\delta$ at most $\delta(T)$ and the sequence is a marked sequence for $(I, m)$ at that level. Otherwise the step leaves the sequence unchanged.

The ideal $N^m + I_t^{\,b}$ with mark $mb$ is the companion ideal. Its order locus is the set of points where $N$ has order at least $b$ and $I_t$ has order at least $m$. So order reduction of the companion ideal moves the points of maximal order of $N$ off the order locus of $I$. On $\operatorname{cosupp}(I_t, m)$ the order of $N$ is at most $b$, and off it $I_t$ has order less than $m$. So the companion ideal has order at most $m b$ everywhere. It is bounded by its mark, and order reduction applies to it. When step 2 reaches $b = 0$, $N$ is a unit on the order locus of $I$, so $I$ is monomial there and step 3 finishes.

The proofs need ten geometric facts. We state them as one theorem.

**Theorem 8.7.4 (Geometric facts for principalization).** Let $T$ be admissible. Then:

1. order certificates are invariant under isomorphisms when they come from hypersurfaces of maximal contact (the precise statement uses local hypersurfaces $H$, local ideals $J$ on them with certificates, and an isomorphism $W' \cong W$);
2. let $Z$ be smooth with strict normal crossings with $E$, let $\pi$ be the blow-up along $Z$, let $J$ have order exactly $c$ at each point of $Z$, and let $\mathcal{E}_\pi^c \cdot J' = \pi^{-1} J$; then no irreducible component of the exceptional divisor lies in $V(J')$;
3. orders are invariant under field base change $X_L \to X$, for $\operatorname{char} L = 0$;
4. in the situation of part 2, $\operatorname{ord}_{x'} J' \leq c$ at each point $x'$ of the exceptional divisor;
5. monomial splittings pull back along field base change;
6. monomial splittings pull back along smooth maps;
7. a monomial splitting of $I$ along $E$ exists;
8. it is unique;
9. in the situation of part 2, each irreducible component of the strict transform of a boundary divisor $D$ is the closure of a point outside the exceptional divisor whose image has closure a component of $V(D)$ not contained in $Z$;
10. a list of facts on the monomial case: if the divisors $E_j$ with $j \in J$ have a common point, then $|J| < \delta$; the monomial centre is smooth and has strict normal crossings with the boundary, the blow-up gives a controlled transform, and the components of intersections of boundary divisors behave well under blow-ups, flat maps and smooth maps.

Lean: `FunctorialResolution.EmbeddedResolution.principalizationGeometryHypotheses`.

*Proof.* Parts 1, 2, 3, 5, 6, 7 and 8 are proved directly from admissibility, as described in the next theorem. Parts 4, 9 and 10 come from a short list of facts on strict transforms and the monomial case. The proof goes through three reductions: the strict transform facts give the facts on residual ideals, these give the three facts of the next theorem, and these give the ten facts. $\square$

**Theorem 8.7.5 (Reduction to three facts).** Assume the following three facts:

1. part 4 of the previous theorem;
2. part 9 of the previous theorem;
3. a list of monomial case facts: if the divisors $E_j$ with $j \in J$ have a common point, then $|J| < \delta$; the monomial centre is smooth with strict normal crossings with the boundary, the total transform of the blow-up, and the behaviour of components of intersections of boundary divisors.

Then the ten geometric facts hold.

Lean: `FunctorialResolution.EmbeddedResolution.geometricHypotheses_of_orderReductionHypotheses`.

*Proof.* Part 1 is the descent of order certificates under isomorphisms. Part 2 holds because the controlled transform does not contain a component of the exceptional divisor; this uses that the blow-up of a noetherian scheme is locally noetherian. Part 3 is the invariance of order under flat base change by a field extension. Parts 5 and 6 hold because monomial splittings pull back along flat maps, and smooth maps are flat. Parts 7 and 8 use that $E$ has strict normal crossings and $I$ is nonzero on each component. The other parts of the monomial list are derived from the three given facts. $\square$

Now the main theorem. Recall that $\mathcal{O}$ only receives marked ideals $S$ with $\delta(S) \leq \delta(T)$.

**Theorem 8.7.6 (Maximal order reduction by companion ideals).** Assume the ten geometric facts and the invariance of order loci, strict normal crossings and smoothness under isomorphisms. Let $n \geq 0$, and let $A$ be an order reduction for $\delta \leq n$ relative to some assignment $B$. Then the assignment $T \mapsto R_{\max}(T, A)$ is a maximal order reduction for $\delta \leq n$ relative to $A$.

Lean: `FunctorialResolution.EmbeddedResolution.MaxOrderReduction.isMaxOrderReduction_orderReductionSeq` (also `FunctorialResolution.EmbeddedResolution.MaxOrderReduction.isMaxOrderReduction_canonicalAlgorithmRules`, the same statement for $\operatorname{Max}(A)$ of the canonical rules).

*Proof.* First, the monomial principalization satisfies four conditions on monomial marked ideals: its centres are certified, nonempty, it resolves, and it is empty if the order locus is empty. This uses parts 10 and 3 of the facts. Now take $T$ admissible with $\delta(T) \leq n$.

*Certificates.* Each centre of $R_{\max}(T, A)$ comes from one of the three steps. In steps 1 and 2 it is a centre of a value of $A$, which carries an order certificate by condition 1 of the order reduction specification, and the certificate passes to $(I, m)$. In step 3 it is a centre of the monomial principalization.

*Comparison.* If $E = ()$ and $T$ is bounded by its mark, then $M = \mathcal{O}_X$ and $N = I$. The first pass of step 1 applies $A$ to $(I, m)$ and makes the order locus empty. After that, $b$ in step 2 is $0$ and step 3 has an empty order locus, so nothing more is added. So $R_{\max}(T, A)$ is isomorphic to $A(T)$.

*Nonempty centres and resolution.* The centres are nonempty by the same conditions for $A$ and for the monomial step. After step 2 the order locus lies where $I$ is monomial, and step 3 resolves it.

*Pullbacks.* The monomial splitting commutes with field base change and smooth pullback by parts 5, 6 and 8. Orders are invariant by part 3. So every step for the pulled-back marked ideal is the pullback of the same step for $T$, by conditions 3 and 6 of the order reduction specification. If the map is surjective, the pullback is strict because all centres are nonempty.

*Empty order locus.* If $\operatorname{cosupp}(I, m) = \varnothing$, the definition gives the empty sequence. $\square$

The remaining condition, the passage from $\delta < n$ to $\delta \leq n$, is now complete. The theorem below collects the four conditions.

**Theorem 8.7.7 (Correctness from hypotheses).** Assume $\mathrm{(ST)}$, the divisor reduction facts of Section 4 and the ten geometric facts. Then the canonical rules reduce inductively on dimension.

Lean: `FunctorialResolution.EmbeddedResolution.isCorrect_canonicalAlgorithmRules_of_hypotheses`.

*Proof.* Condition 1 is the Theorem (Divisor reduction meets its specifications), first part. Condition 2 is the second part of that theorem. Condition 3 is the previous theorem. Condition 4 is the [Theorem (Order reduction by maximal contact)](/entry/is-order-reduction-order-family-of-strict-transform-is-blowup/). $\square$

**Theorem 8.7.8 (Correctness of the canonical rules).** Assume $\mathrm{(ST)}$. Then the canonical rules reduce inductively on dimension.

Lean: `FunctorialResolution.EmbeddedResolution.isCorrect_canonicalAlgorithmRules`.

*Proof.* The divisor reduction facts are the Theorem (The divisor reduction facts hold) of Section 4, and the geometric facts are the Theorem (Geometric facts for principalization). Apply the previous theorem. $\square$

**Corollary 8.7.9 (Correctness).** The canonical rules, built with the proof of $\mathrm{(ST)}$, reduce inductively on dimension.

Lean: `FunctorialResolution.EmbeddedResolution.canonicalAlgorithmRules_isCorrect`.

*Proof.* The chapter proves $\mathrm{(ST)}$: the strict transform of a closed subscheme under a blow-up is the blow-up of that subscheme along the inverse image of the centre. Apply the previous theorem to this proof. $\square$

**Remark 8.7.10 (Formalization).** The construction is `orderReductionSeq` in [OrderReductionAlgorithm.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/MarkedOrderReduction/OrderReductionAlgorithm.lean#L186), with `nonMonomialOrderReductionIter`, `companionIdealReductionIter` and `monomialPrincipalization`. In `canonicalAlgorithmRules` ([CanonicalPrincipalization.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/CanonicalPrincipalization.lean#L26)) the field `maxOrderRed` is `orderReductionSeq` and the field `orderRed` is `MaxContactReduction.reduceOrder`, so the Lean names of the two rules cross. The function `monomialSplitting` (line 26) falls back to $(\mathcal{O}_X, I)$ by choice, and `lexMaxIndices` and `monomialCenter` fall back to $\varnothing$ and the unit ideal. The argument `principalizationOfDimLe` ([NonMonomialOrderReduction.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/MarkedOrderReduction/NonMonomialOrderReduction.lean#L84)) ignores its proof of the bound on $\delta$, so the bound is only checked by `appendRecursivePrincipalization`. The ten facts are `PrincipalizationGeometryHypotheses` in GeometryHypotheses.lean. The three facts are the structure `OrderReductionHypotheses` at line 196 of MarkedOrderReduction/OrderReductionHypotheses.lean, one of three structures with that name in the project. Both structures are proved, so the word "Hypotheses" does not mean an assumption. In `isMaxOrderReduction_canonicalAlgorithmRules` ([MaxOrderReduction.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/MarkedOrderReduction/MaxOrderReduction.lean#L123)) the argument `hres` is not used. The name `isCorrect_canonicalAlgorithmRules` refers to the proposition `ReducesInductivelyOnDimension`; there is no separate predicate called correctness. We did not open the proofs of the four monomial conditions or of the bound on the number of iterations in steps 1 and 2.
