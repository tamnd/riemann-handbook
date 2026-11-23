---
title: Induction on dimension and principalization
decls:
  - FunctorialResolution.EmbeddedResolution.PrincipalizationRules.isMaxOrderReduction_outputLevelData
  - FunctorialResolution.EmbeddedResolution.PrincipalizationRules.isOrderReduction_outputLevelData
  - FunctorialResolution.EmbeddedResolution.PrincipalizationRules.outputLevelData_maxOrderReduction_eq_at_dim
  - FunctorialResolution.EmbeddedResolution.PrincipalizationRules.isFunctorialPrincipalization_principalization
  - FunctorialResolution.EmbeddedResolution.PrincipalizationRules.ReducesInductivelyOnDimension
  - FunctorialResolution.EmbeddedResolution.IsFunctorialPrincipalization
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Induction on dimension and principalization

This section turns the four specifications of the previous section into a construction. A set of rules says how to build each kind of sequence in dimension $d$ from sequences in smaller dimension. We iterate the rules, starting from the empty sequences, and prove by induction on the dimension that the result is a maximal order reduction in every dimension. With mark $1$ this gives a principalization of ideal sheaves on smooth schemes that is compatible with closed immersions, smooth maps and field extensions. Section 7 shows that the canonical rules satisfy the hypothesis of the induction, and Section 8 uses the principalization to resolve affine schemes.

**Definition 8.3.1 (Rules).** A set of *principalization rules* $R$ consists of three operations.

1. Divisor reduction: for a marked ideal $T$, a position $j$, and a marked sequence $L(S)$ for each marked ideal $S$ with $\delta(S) < \delta(T)$, it gives a marked sequence $R_{\mathrm{div}}(T, L, j)$ for $T$.
2. Maximal order reduction: for $T$ and a marked sequence $O(S)$ for each $S$ with $\delta(S) \leq \delta(T)$, it gives $R_{\max}(T, O)$.
3. Order reduction: for $T$ and a marked sequence $D_j(S)$ for each $S$ with $\delta(S) \leq \delta(T)$ and each $j \geq 0$, it gives $R_{\mathrm{ord}}(T, D)$.

For assignments $L$, $A$ and a family $D = (D_j)$ we get assignments
$$\operatorname{Div}_j(L) \colon T \mapsto R_{\mathrm{div}}(T, L, j), \qquad \operatorname{Max}(A) \colon T \mapsto R_{\max}(T, A), \qquad \operatorname{Ord}(D) \colon T \mapsto R_{\mathrm{ord}}(T, D).$$

Divisor reduction only looks at smaller dimension, because it works on a boundary divisor. The other two may call sequences in the same dimension: maximal order reduction calls order reduction of a companion marked ideal, and order reduction calls divisor reduction along the boundary.

**Definition 8.3.2 (Levels).** A *level* is a pair $\Lambda = (\Lambda_{\max}, \Lambda_{\mathrm{ord}})$ of assignments. The *next level* of $\Lambda$ is
$$\begin{aligned} \operatorname{next}(\Lambda)_{\mathrm{ord}} &= \operatorname{Ord}\bigl((\operatorname{Div}_j(\Lambda_{\max}))_{j \geq 0}\bigr), \\ \operatorname{next}(\Lambda)_{\max} &= \operatorname{Max}\bigl(\operatorname{next}(\Lambda)_{\mathrm{ord}}\bigr). \end{aligned}$$
Let $\mathrm{In}_0$ be the level whose two assignments give the empty sequence of length $0$ to every marked ideal. Let $\mathrm{In}_{n+1} = \operatorname{next}(\mathrm{In}_n)$ and $\mathrm{Out}_n = \operatorname{next}(\mathrm{In}_n)$, so $\mathrm{Out}_n = \mathrm{In}_{n+1}$.

So the maximal order reduction of the input level is used for divisor reduction, the divisor reductions feed order reduction, and order reduction feeds maximal order reduction. The level $\mathrm{Out}_n$ is meant for marked ideals with $\delta(T) \leq n$, that is, of dimension less than $n$.

**Definition 8.3.3 (Reduces inductively on dimension).** The rules $R$ *reduce inductively on dimension* if, for each $n \geq 0$, all assignments $L$, $O$, $A$ and every family $D = (D_j)$:

1. if $L$ is a maximal order reduction for $\delta < n$ relative to $O$, then $\operatorname{Div}_j(L)$ is a divisor reduction at position $j$ for $\delta \leq n$ relative to $L$, for each $j$;
2. under the same hypothesis, the family $(\operatorname{Div}_j(L))_j$ is position invariant for $\delta \leq n$;
3. if $A$ is an order reduction for $\delta \leq n$ relative to $L$, then $\operatorname{Max}(A)$ is a maximal order reduction for $\delta \leq n$ relative to $A$;
4. if $L$ is a maximal order reduction for $\delta < n$ relative to $O$, each $D_j$ is a divisor reduction at position $j$ for $\delta \leq n$ relative to $L$, and $D$ is position invariant for $\delta \leq n$, then $\operatorname{Ord}(D)$ is an order reduction for $\delta \leq n$ relative to $L$.

Lean: `FunctorialResolution.EmbeddedResolution.PrincipalizationRules.ReducesInductivelyOnDimension`.

Each condition raises the range of dimensions by one step or keeps it. Conditions 1, 2 and 4 pass from $\delta < n$ to $\delta \leq n$; condition 3 stays at $\delta \leq n$.

**Theorem 8.3.4 (Induction on dimension).** Let $R$ be rules that reduce inductively on dimension. Then for each $n \geq 0$:

1. $(\mathrm{Out}_n)_{\mathrm{ord}}$ is an order reduction for $\delta \leq n$ relative to $(\mathrm{In}_n)_{\max}$;
2. $(\mathrm{Out}_n)_{\max}$ is a maximal order reduction for $\delta \leq n$ relative to $(\mathrm{Out}_n)_{\mathrm{ord}}$;
3. if $\delta(T) \leq N$, then $(\mathrm{Out}_N)_{\max}(T) = (\mathrm{Out}_{\delta(T)})_{\max}(T)$.

Lean: `FunctorialResolution.EmbeddedResolution.PrincipalizationRules.isMaxOrderReduction_outputLevelData` (also `FunctorialResolution.EmbeddedResolution.PrincipalizationRules.isOrderReduction_outputLevelData`, `FunctorialResolution.EmbeddedResolution.PrincipalizationRules.outputLevelData_maxOrderReduction_eq_at_dim`).

*Proof.* First we show by induction on $n$ that $(\mathrm{In}_n)_{\max}$ is a maximal order reduction for $\delta < n$ relative to $(\mathrm{In}_n)_{\mathrm{ord}}$. For $n = 0$ no number $d$ satisfies $d < 0$, so the conditions are empty. Assume the claim for $n$ and put $L = (\mathrm{In}_n)_{\max}$. By conditions 1 and 2 of the definition, each $\operatorname{Div}_j(L)$ is a divisor reduction at $j$ for $\delta \leq n$ relative to $L$, and the family is position invariant for $\delta \leq n$. By condition 4, $(\mathrm{Out}_n)_{\mathrm{ord}} = \operatorname{Ord}((\operatorname{Div}_j(L))_j)$ is an order reduction for $\delta \leq n$ relative to $L$. This is part 1 for $n$. By condition 3, $(\mathrm{Out}_n)_{\max}$ is a maximal order reduction for $\delta \leq n$ relative to $(\mathrm{Out}_n)_{\mathrm{ord}}$. This is part 2 for $n$. Since $d < n + 1$ means $d \leq n$ and $\mathrm{Out}_n = \mathrm{In}_{n+1}$, this is the claim for $n + 1$.

For part 3 we show a stronger statement by induction on $d$: if $\delta(T) \leq d < m \leq M$, then $\mathrm{In}_m$ and $\mathrm{In}_M$ agree on $T$, in both components. Write $m = m' + 1$ and $M = M' + 1$. The rules compute $\mathrm{In}_m(T) = \operatorname{next}(\mathrm{In}_{m'})(T)$ from the values of $(\mathrm{In}_{m'})_{\max}$ on marked ideals $S$ with $\delta(S) < \delta(T)$ only: order reduction of $T$ calls divisor reduction of marked ideals $S$ with $\delta(S) \leq \delta(T)$, and divisor reduction of $S$ calls the input level on marked ideals of $\delta$ less than $\delta(S)$. For $d = 0$ there are no such $S$. For $d > 0$ such $S$ have $\delta(S) \leq d - 1 < m' \leq M'$, and the induction hypothesis gives $(\mathrm{In}_{m'})_{\max}(S) = (\mathrm{In}_{M'})_{\max}(S)$. So the two levels agree on $T$. Part 3 is the case $d = \delta(T)$, $m = \delta(T) + 1$ and $M = N + 1$. $\square$

Next we pass from marked ideals to ideal sheaves. Let $k$ have characteristic $0$, let $X$ be smooth and of finite type over $k$, let $I$ be an ideal sheaf on $X$ that is nonzero on each component, and let $E$ be a list in strict normal crossing position.

**Definition 8.3.5 (Principalization).** A *principalization sequence* for $(X, I, E)$ is a sequence of blow-ups $X_0 = X \leftarrow X_1 \leftarrow \cdots \leftarrow X_n$ with ideal sheaves $I_i$ and lists $E_i$, such that $I_0 = I$, $E_0 = E$, each centre $Z_i$ is smooth over $k$ and has strict normal crossings with $E_i$, $I_i \subseteq \mathcal{I}_{Z_i}$, $\mathcal{E}_{\pi_i} \cdot I_{i+1} = \pi_i^{-1} I_i \cdot \mathcal{O}_{X_{i+1}}$, and $E_{i+1}$ is the list of strict transforms of $E_i$ followed by $\mathcal{E}_{\pi_i}$. A *principalization algorithm* gives such a sequence to each $(X, I, E)$ as above. It is *functorial* if:

1. its last ideal $I_n$ is the unit ideal;
2. for each field homomorphism $k \to K$ with $\operatorname{char} K = 0$ such that $X_K$ is smooth and of finite type over $K$, $I_K$ is nonzero on components and $E_K$ is in strict normal crossing position, the sequence for $(X_K, I_K, E_K)$ is a pullback and a strict pullback of the sequence for $(X, I, E)$;
3. for each smooth $\varphi \colon X' \to X$ over $k$ with $X'$ of finite type and $(X', \varphi^{-1} I, \varphi^{*} E)$ again admissible, the sequence for $X'$ is a pullback of the sequence for $X$, and a strict pullback when $\varphi$ is surjective;
4. for each closed immersion $j \colon S \to X$ over $k$ of smooth schemes of finite type such that, locally on $X$, the ideal of $S$ is generated by $c \geq 1$ coordinates of an étale chart, and each $I$ on $S$ with $I$ and its image in $X$ nonzero on components, the sequence for $(S, I, ())$ pushes forward along $j$ to the sequence for $(X, \mathcal{I}_{V(I)}, ())$, where $\mathcal{I}_{V(I)}$ is the ideal of $V(I)$ in $X$.

Lean: `FunctorialResolution.EmbeddedResolution.IsFunctorialPrincipalization`.

Condition 1 says that $\pi^{-1} I \cdot \mathcal{O}_{X_n}$ is a product of powers of the exceptional ideals, which are locally principal. Given rules $R$, the *principalization of $R$* takes the marked ideal $(k, X, I, 1, E)$ of mark $1$ and the sequence $(\mathrm{Out}_{\delta(X)})_{\max}(k, X, I, 1, E)$. With mark $1$ the order locus of $I_i$ is the support of $V(I_i)$, so the centre $Z_i$ lies in $V(I_i)$. To get $I_i \subseteq \mathcal{I}_{Z_i}$ we use that a smooth subscheme is reduced: if $Z$ is smooth and $\operatorname{supp} Z \subseteq \operatorname{supp} V(J)$, then $J \subseteq \mathcal{I}_Z$.

The rules *commute with closed immersions* if the sequences $(\mathrm{Out}_{\delta})_{\max}$ of mark $1$ and empty boundary satisfy condition 4 above.

**Theorem 8.3.6 (Functorial principalization).** Let $R$ be rules that reduce inductively on dimension and commute with closed immersions, and assume that $J \subseteq \mathcal{I}_Z$ whenever $Z$ is a smooth closed subscheme of a scheme over $k$ and $\operatorname{supp} Z \subseteq \operatorname{supp} V(J)$. Then the principalization of $R$ is a functorial principalization algorithm.

Lean: `FunctorialResolution.EmbeddedResolution.PrincipalizationRules.isFunctorialPrincipalization_principalization` (also `FunctorialResolution.EmbeddedResolution.commutesWithClosedImmersion_of_isCorrect`, which shows that rules that reduce inductively on dimension commute with closed immersions).

*Proof.* The sequence is a marked sequence of mark $1$, so its centres are smooth, have strict normal crossings with the boundary and satisfy $\mathcal{E} \cdot I_{i+1} = \pi^{-1} I_i$. The assumption on smooth subschemes gives $I_i \subseteq \mathcal{I}_{Z_i}$. So it is a principalization sequence. Condition 4 is the assumption that $R$ commutes with closed immersions. For condition 1, part 2 of the Theorem (Induction on dimension) says that $(\mathrm{Out}_{\delta(X)})_{\max}$ resolves $(k, X, I, 1, E)$, so the order locus $\operatorname{cosupp}(I_n, 1) = \operatorname{supp} V(I_n)$ is empty and $I_n$ is the unit ideal. For condition 3, let $N = \max(\delta(X), \delta(X'))$. By part 3 of the same theorem, the sequences for $X$ and $X'$ are the values of $(\mathrm{Out}_N)_{\max}$, and this assignment is a maximal order reduction for $\delta \leq N$ by part 2. Its smooth pullback condition, with $E' = \varphi^{*}E$, gives condition 3. Condition 2 follows in the same way from the base change condition, with $N = \max(\delta(X), \delta(X_K))$. $\square$

The fact that rules which reduce inductively on dimension commute with closed immersions is proved by induction on the codimension $c$. For $c \geq 1$ one takes a smooth surjective cover of $X$ on which the pullback of $S$ lies in a smooth hypersurface, so that the codimension in the hypersurface is $c - 1$. The image ideal has order at most $1$, so the pushforward condition of order reduction applies to the hypersurface. The sequences are then compared on the cover and descended to $X$.

**Remark 8.3.7 (Formalization).** The rules are `PrincipalizationRules` and the levels are `inputLevelData` and `outputLevelData` in [DimensionRecursion.lean](lean:Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization/DimensionRecursion.lean#L10). The induction for the input levels is a private theorem there. The families `divisorFamily`, `orderFamily` and `maxOrderFamily` (lines 20 to 38) throw away the bound on $\delta$ that the rules receive, so a rule gets its argument on all marked ideals and the bound only constrains which values it may use. The radical hypothesis is the proposition `SmoothSubschemeIdealIsRadical`, proved later in the chapter. The closed immersion case uses the local codimension condition `HasEtaleCoordCodim`, which we did not unfold beyond its definition by étale charts. We read the statement of the closed immersion result and the outline of its proof, not every step.
