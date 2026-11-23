---
title: Certificates and the four specifications
decls:
  - FunctorialResolution.EmbeddedResolution.PrincipalizationCertificate
  - FunctorialResolution.EmbeddedResolution.IsMaxOrderReduction
  - FunctorialResolution.EmbeddedResolution.IsOrderReduction
  - FunctorialResolution.EmbeddedResolution.IsBoundaryDivisorReduction
  - FunctorialResolution.EmbeddedResolution.IsBoundaryPositionInvariant
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Certificates and the four specifications

The construction of the chapter builds sequences of blow-ups in dimension $d$ from sequences in smaller dimension. It has three kinds of steps: reduction of the maximal order, reduction of the order with a hypersurface of maximal contact, and reduction along one boundary divisor. This section states what each kind of step must achieve. There are four specifications. The next section shows that rules which meet them in each dimension give a functorial principalization. Sections 4 to 7 check the specifications for the canonical rules. All notions refer to the marked ideals and marked sequences of the [first section](/entry/deriv-ideal-sheaf-iterate-le-bi-sup-log-deriv-ideal-sheaf-iterate-of-blowup/).

Fix a marked sequence for $T = (k, X, I, m, E)$, with schemes $X_i$, ideals $I_i$, lists $E_i$ and centres $Z_i$. Let $B_i \subseteq X_i$ be the boundary locus at level $i$, the union of the supports of the entries of $E_i$. For $j \geq 0$ let $B_i^{(j)}$ be the union of the supports of the entries of $E_i$ other than the entry in position $j$.

**Definition 8.2.1 (Certified centre).** Let $W$ be a scheme over $k$, $I$ an ideal sheaf on $W$, $m \geq 0$, $B \subseteq W$ a subset and $Z \subseteq W$ a closed subscheme. The two notions "$Z$ is *certified* for $(I, m)$ relative to $B$" and "$Z$ is *order-certified* for $(N, \mu)$ relative to $B$" are defined together, as the smallest notions with the following closure rules. The centre $Z$ is certified for $(I, m)$ if one of these holds:

1. $\operatorname{supp} Z \subseteq B$;
2. $m \geq 2$;
3. $I = M \cdot N$ for ideal sheaves $M$ and $N$ with $\operatorname{supp} V(M) \subseteq B$, and there is $\mu \geq m$ with $\operatorname{supp} Z \subseteq \operatorname{cosupp}(N, \mu)$ and $Z$ order-certified for $(N, \mu)$;
4. each point $z \in Z$ has an open neighbourhood $U$ such that $Z \cap U$ is certified for $(I|_U, m)$ relative to $B \cap U$.

The centre $Z$ is order-certified for $(N, \mu)$ if one of these holds:

1. $\operatorname{supp} Z \subseteq B$;
2. $\mu \geq 2$;
3. the local rule 4 above, with order-certified in place of certified;
4. each point $z \in Z$ has an open neighbourhood $U$ and a smooth divisor $H \subseteq U$ with $\operatorname{supp} V(N|_U) \subseteq H$ and $Z \cap U \subseteq H$, such that either $Z \cap U$ is open in $H$, or there is an ideal sheaf $J$ on $H$, nonzero on each component of $H$, which agrees with $N|_H$ near each point of $H$ outside $B$, and $Z \cap U$ is certified for $(J, \mu)$ relative to $B \cap H$.

Lean: `FunctorialResolution.EmbeddedResolution.PrincipalizationCertificate` (also `FunctorialResolution.EmbeddedResolution.OrderCertificate`).

A certificate records where a centre comes from in the induction: from the boundary, from a monomial factor, or from a smooth hypersurface in smaller dimension. Rule 2 makes each centre certified as soon as the mark is at least $2$. So the notion has content only for the mark $1$. This is the mark of principalization, and it is the case in which a sequence is pushed forward from a hypersurface.

Next come the four specifications. In each of them, $P$ is a property of natural numbers. It is the range of dimensions for which the specification is claimed: we apply the specifications with $P(d)$ equal to $d < n$ or $d \leq n$, and $d$ is the number $\delta(T) = \dim X + 1$. Recall that an *assignment* $A$ gives a marked sequence $A(T)$ to each marked ideal $T$.

For a smooth morphism $h \colon Y \to X$ and a marked ideal $T$ on $X$, we write $T_Y = (k, Y, h^{-1} I \cdot \mathcal{O}_Y, m, h^{*} E)$, where $h^{*} E$ is the list of the pullbacks of the entries of $E$. For a field homomorphism $k \to L$ we write $X_L = X \times_k L$ and $T_L$ for the pullback of $T$ to $X_L$, a marked ideal over $L$. For a list $E'$ on $Y$ we write $(T_Y, E')$ for $T_Y$ with its boundary replaced by $E'$.

**Definition 8.2.2 (Maximal order reduction).** Let $A$ and $B$ be assignments. Then $A$ is a *maximal order reduction for $P$ relative to $B$* if, for each admissible marked ideal $T = (k, X, I, m, E)$ with $P(\delta(T))$:

1. for each $i$ below the length of $A(T)$, the centre $Z_i$ of $A(T)$ is certified for $(I_i, m)$ relative to $B_i$;
2. if $E = ()$ and $T$ is bounded by its mark, then $A(T)$ and $B(T)$ are isomorphic sequences of blow-ups;
3. for each field homomorphism $k \to L$ with $\operatorname{char} L = 0$ and each list $E'$ on $X_L$ with the same nontrivial part as the boundary of $T_L$, if $(T_L, E')$ is admissible and $P(\delta(T_L, E'))$ holds, then $A(T_L, E')$ is a pullback and a strict pullback of $A(T)$ along the projection $X_L \to X$;
4. each centre of $A(T)$ is nonempty;
5. $A(T)$ resolves $T$;
6. for each smooth $h \colon Y \to X$ and each list $E'$ on $Y$ with the same nontrivial part as $h^{*}E$, if $(T_Y, E')$ is admissible and $P(\delta(T_Y, E'))$ holds, then $A(T_Y, E')$ is a pullback of $A(T)$ along $h$, and a strict pullback if $h$ is also surjective;
7. if $\operatorname{cosupp}(I, m) = \varnothing$, then $A(T)$ has length $0$.

Lean: `FunctorialResolution.EmbeddedResolution.IsMaxOrderReduction`.

Two remarks on this definition. If $P$ holds for no number, the conditions are empty, and every pair $(A, B)$ satisfies them. If $P$ implies $P'$ and $A$ is a maximal order reduction for $P'$, then it is one for $P$. Both facts are used in the next section.

The second specification asks less in two ways: it only applies to marked ideals that are bounded by their mark, and its centres only need an order certificate. It asks more in two ways: the order stays bounded along the sequence, and the sequence is compatible with a hypersurface that carries the whole ideal.

**Definition 8.2.3 (Order reduction).** Let $A$ and $B$ be assignments. Then $A$ is an *order reduction for $P$ relative to $B$* if, for each admissible $T = (k, X, I, m, E)$ with $P(\delta(T))$ that is bounded by its mark:

1. each centre $Z_i$ of $A(T)$ is order-certified for $(I_i, m)$ relative to $B_i$;
2. conditions 3 to 7 of a maximal order reduction hold, where in 3 and 6 the new marked ideal is also asked to be bounded by its mark;
3. $\operatorname{ord}_x I_i \leq m$ for each level $i$ up to the length and each point $x$ of $X_i$;
4. assume $E = ()$ and $m = 1$. Let $e \colon Y \to X$ be a closed immersion whose ideal is a smooth divisor on $X$, and let $J$ be an ideal sheaf on $Y$ such that $(k, Y, J, 1, ())$ is admissible, $\delta(k, Y, J, 1, ()) < \delta(T)$, and $I$ is the ideal of $V(J)$ regarded as a closed subscheme of $X$. Then the sequence $B(k, Y, J, 1, ())$ pushes forward along $e$ to $A(T)$.

Lean: `FunctorialResolution.EmbeddedResolution.IsOrderReduction`.

Here a sequence $Y_0 \leftarrow \cdots \leftarrow Y_n$ *pushes forward* along $e$ to $X_0 \leftarrow \cdots \leftarrow X_n$ if both have the same length $n$ and there are closed immersions $e_i \colon Y_i \to X_i$ with $e_0 = e$ that commute with the blow-up maps, such that the centre of $X_i$ is the image of the centre of $Y_i$ and $Y_{i+1}$ is the strict transform of $Y_i$. So the hypersurface $Y$ and its strict transforms carry the whole sequence.

The third specification is about one boundary divisor $E_j$. It asks for a sequence that moves the locus of maximal order off the strict transforms of $E_j$, and whose centres come from a sequence on $E_j$ itself.

**Definition 8.2.4 (Divisor reduction).** Let $j \geq 0$ and let $A$ and $B$ be assignments. Then $A$ is a *divisor reduction at position $j$ for $P$ relative to $B$* if, for each admissible $T = (k, X, I, m, E)$ with $P(\delta(T))$ that is bounded by its mark, balanced, and has $j$ less than the length of $E$:

1. conditions 3, 4, 6 and 7 of a maximal order reduction hold, where in 3 and 6 the new list $E'$ must also agree with the pulled-back list in the positions $0$ to $j$, and the new marked ideal must be bounded by its mark, balanced, and have a boundary of length more than $j$;
2. $\operatorname{ord}_x I_i \leq m$ at each level $i$ and each point $x$;
3. if $m = 1$, $J$ is an ideal sheaf on the divisor $D = V(E_j)$, the marked ideal $(k, D, J, 1, E|_D)$ is admissible with $\delta$ less than $\delta(T)$, where $E|_D$ is $E$ with the entry $j$ deleted and the others restricted to $D$, and $I$ is the ideal of $V(J)$ in $X$, then $B(k, D, J, 1, E|_D)$ pushes forward to $A(T)$ along the inclusion of $D$;
4. there are smooth divisors $D_t \subseteq X_t$ for $t$ up to the length $n$ of $A(T)$, and a boolean $b$, with the following properties. First, $D_0 = V(E_j)$ and each centre $Z_t$ lies in $D_t$. If $b$ is true, then $n > 0$, $Z_0$ is open in $D_0$, and $D_1$ is the full inverse image of $D_0$. For every other $t < n$, $D_{t+1}$ is the strict transform of $D_t$. The last level satisfies $\operatorname{cosupp}(I_n, m) \cap D_n = \varnothing$. Finally, for each $t < n$ other than $t = 0$ when $b$ is true, there is an ideal $J_t$ on $D_t$, nonzero on each component, which agrees with $I_t|_{D_t}$ near each point outside $B_t^{(j)}$, and $Z_t$ is certified for $(J_t, m)$ relative to $B_t^{(j)} \cap D_t$.

Lean: `FunctorialResolution.EmbeddedResolution.IsBoundaryDivisorReduction`.

Condition 4 is the content of divisor reduction. Away from the other boundary divisors, the restriction of $I_t$ to the strict transform of $E_j$ is a marked ideal in one dimension less, and the centres come from it. At the end, no point of maximal order lies on the strict transform of $E_j$.

The last specification concerns a family $A_0, A_1, \dots$ of assignments, where $A_j$ works along the boundary divisor in position $j$. It says that $A_j$ sees only the divisor $D$ in position $j$ and the nontrivial entries before and after it, not their exact positions.

**Definition 8.2.5 (Position invariance).** A family $(A_j)_{j \geq 0}$ of assignments is *position invariant for $P$* if the following holds. Let $T$ be a marked ideal with $P(\delta(T))$, with $X$ locally of finite type over $k$, bounded by its mark and balanced. Let $E_1, E_1', E_2, E_2'$ be lists of ideal sheaves on $X$ and $D$ an ideal sheaf, such that $E_1$ and $E_1'$ have the same nontrivial part, and so do $E_2$ and $E_2'$. If $T$ with boundary $E_1 \mathbin{+\!\!+} (D) \mathbin{+\!\!+} E_2$ and $T$ with boundary $E_1' \mathbin{+\!\!+} (D) \mathbin{+\!\!+} E_2'$ are both admissible, then the sequences
$$A_{|E_1|}\bigl(T, E_1 \mathbin{+\!\!+} (D) \mathbin{+\!\!+} E_2\bigr) \quad\text{and}\quad A_{|E_1'|}\bigl(T, E_1' \mathbin{+\!\!+} (D) \mathbin{+\!\!+} E_2'\bigr)$$
are isomorphic.

Lean: `FunctorialResolution.EmbeddedResolution.IsBoundaryPositionInvariant`.

Here $|E_1|$ is the length of $E_1$, so $D$ sits in position $|E_1|$ of the first list and in position $|E_1'|$ of the second. Position invariance is what makes order reduction compatible with pullbacks: a pullback can make an earlier boundary divisor empty, and this shifts the position of $D$.

**Remark 8.2.6 (Formalization).** Certificates are the two mutually inductive families `PrincipalizationCertificate` and `OrderCertificate` ([PrincipalizationCertificate.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/PrincipalizationCertificate.lean#L12)). The constructors `large` (lines 19 and 48) certify every centre once the mark is at least $2$, so the certificate fields of the specifications say nothing for $m \geq 2$. The four specifications are in [OrderReductionProperties.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/OrderReductionProperties.lean#L299). The text lists their fields in a different order and joins a field with its strict version. Order reduction has no field that compares $A(T)$ with $B(T)$, while maximal order reduction has one. Position invariance does not ask $T$ to be admissible, only that the two marked ideals with the new boundaries are. We did not unfold the isomorphism of sequences of blow-ups.
