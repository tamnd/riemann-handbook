---
title: Cutting with lacunary jumps
decls:
  - UpperTheory.Gal.Int.Div.divSet_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Cutting with lacunary jumps

Section 24 used one fact without proof, fact 1 (cutting): a semisimple $\rho$ with a lacunary set of $a$ Hodge-Tate jumps, whose elements on a dense set are killed by monic polynomials of degree $a$, contains a representation $r$ of dimension $a$ that also covers $\rho$. This section proves it. There are two steps. A theorem of Sen type turns the lacunary jumps into an element of the Lie algebra of the Zariski closure of $\rho(G_E)$ with $a$ lacunary eigenvalues. Then [the small subrepresentation theorem](/entry/goal-holds/) of the chapter on Kummer and Chern classes cuts out $r$. The result is [the cutting theorem](/entry/div-set-holds/), an input of [Theorem 3.25.3](/entry/div-one-holds/).

We keep the notation of Sections 23 and 24. Here $E$ is any number field, $\Omega$ an algebraic closure, $G_E = \mathrm{Gal}(\Omega/E)$, and we fix a system of period rings over $\mathbb{Q}_\ell$. For a place $w \mid \ell$, a valuation ring $A$ of $\Omega$ over $w$ with a local bridge, and an embedding $\tau : E \to \overline{\mathbb{Q}}_\ell$, the *jumps* of a representation at $\tau$ are the Hodge-Tate jumps of its restriction to $D_A$ at $\tau$, a finite multiset of integers.

### Lacunary families

**Definition 3.28.1 (Lacunary family).** Let $k$ be a field of characteristic $0$. A family $e_1, \dots, e_n$ in $k$ is *lacunary* if for any two disjoint nonempty sets $A, B \subset \{1, \dots, n\}$,
$$|B| \sum_{i \in A} e_i \neq |A| \sum_{i \in B} e_i.$$
A finite set $J_0 \subset \mathbb{Z}$ is *lacunary* if the same holds for disjoint nonempty subsets of $J_0$, with the sums of their elements.

Lean: `PositivityTheory.AutomorphicGaloisHodgeTate.Div.IsLac` (also `GlobalTheory.RoadWGeo.Lacunary`).

So the averages over two disjoint nonempty sets are different. A lacunary family has distinct members: take $A = \{i\}$ and $B = \{j\}$. For example $\{1, 3, 9\}$ is lacunary, since the averages $1, 3, 9, 2, 5, 6$ of its nonempty subsets differ for each disjoint pair. The set $\{1, 2, 3\}$ is not, as $2$ is the average of $\{1, 3\}$. If the elements of a lacunary set $J_0$ of $n$ integers are listed in increasing order, the list is a lacunary family in $\mathbb{Q}$, and then in every field of characteristic $0$.

**Definition 3.28.2 (Lacunary jumps).** Let $\rho : G_E \to \mathrm{GL}_N(\overline{\mathbb{Q}}_\ell)$ and $n \geq 0$. Then $\rho$ has *$n$ lacunary jumps* if there are a place $w \mid \ell$, a valuation ring $A$ over $w$ with a local bridge, an embedding $\tau$ and a multiset $J$ such that $J$ is the multiset of jumps of $\rho$ at $\tau$, and $J$ contains a lacunary set $J_0$ of $n$ integers.

Lean: `UpperTheory.Gal.Int.Div.HTRichEx` (also `PositivityTheory.AutomorphicGaloisHodgeTate.Div.HTLac`, `UpperTheory.Gal.Int.Div.LacBridge`, `UpperTheory.Gal.Int.Div.lacBridge_of`).

By the remark after the first definition, this gives an injective family $k_1, \dots, k_n$ of elements of $J$ that is lacunary in $\mathbb{Q}$. The proofs below use the family.

**Definition 3.28.3 (Lie element).** Let $\Gamma$ be a group, $K \subset K'$ fields and $\rho : \Gamma \to \mathrm{GL}_N(K)$. A matrix $X \in M_N(K')$ is a *Lie element* of $\rho$ if
$$\sum_{p, q} \frac{\partial f}{\partial x_{pq}}(1)\, X_{pq} = 0$$
for every polynomial $f \in K[x_{pq} : 1 \leq p, q \leq N]$ that vanishes on $\rho(\Gamma)$.

Lean: `PositivityTheory.AutomorphicGaloisHodgeTate.Div.InLieZar`.

The polynomials that vanish on $\rho(\Gamma)$ define its Zariski closure $\overline{\rho(\Gamma)}$, and $1 \in \overline{\rho(\Gamma)}$. The condition says that $X$ is in the tangent space of $\overline{\rho(\Gamma)}$ at $1$, that is in its Lie algebra.

### A Lie element with lacunary eigenvalues

**Lemma 3.28.4 (Derivative of a cocharacter).** Let $K \subset K'$ be fields with $K'$ algebraically closed, $P \in \mathrm{GL}_N(K')$ and $k_1, \dots, k_N \in \mathbb{Z}$. Let $f \in K[x_{pq}]$ vanish at $P \operatorname{diag}(t^{k_1}, \dots, t^{k_N}) P^{-1}$ for all $t \in K'^\times$. Then $X = P \operatorname{diag}(k_1, \dots, k_N) P^{-1}$ satisfies $\sum_{p, q} \partial_{pq} f(1)\, X_{pq} = 0$.

Lean: `PositivityTheory.AutomorphicGaloisHodgeTate.Div.CochLie.inLie_of_cochar`.

*Proof.* The entries of $P \operatorname{diag}(T^{k_j}) P^{-1}$ are Laurent polynomials in $T$. So $L(T) = f(P \operatorname{diag}(T^{k_j}) P^{-1})$ is a Laurent polynomial over $K'$, and $T^m L(T)$ is a polynomial for some $m$. It vanishes at every $t \neq 0$, and $K'$ is infinite, so $L = 0$. Now evaluate $L$ in the ring of dual numbers $K'[\varepsilon]$, $\varepsilon^2 = 0$, at the unit $T = 1 + \varepsilon$, with inverse $1 - \varepsilon$. Here $(1 + \varepsilon)^m = 1 + m \varepsilon$ for all $m \in \mathbb{Z}$, so $P \operatorname{diag}((1 + \varepsilon)^{k_j}) P^{-1} = 1 + \varepsilon X$. Hence $f(1 + \varepsilon X) = 0$. By Taylor expansion, $f(1 + \varepsilon X) = f(1) + \varepsilon \sum_{p, q} \partial_{pq} f(1)\, X_{pq}$, and the coefficient of $\varepsilon$ is the claim. $\square$

The next theorem is the input from $p$-adic Hodge theory. It says that the Hodge-Tate cocharacter, after a conjugation over $\mathbb{C}_\ell$, takes values in the Zariski closure of the image.

**Theorem 3.28.5 (Hodge-Tate cocharacter).** Let $\rho : G_E \to \mathrm{GL}_N(\overline{\mathbb{Q}}_\ell)$ be continuous with $n$ lacunary jumps, given by $w$, $A$, $\tau$, $J$ and an injective lacunary family $k'_1, \dots, k'_n$ in $J$. Then there are $P \in \mathrm{GL}_N(\mathbb{C}_\ell)$ and $k_1, \dots, k_N \in \mathbb{Z}$ such that each $k'_i$ is some $k_j$, and every polynomial $f$ over $\overline{\mathbb{Q}}_\ell$ that vanishes on $\rho(G_E)$ vanishes at $P \operatorname{diag}(t^{k_1}, \dots, t^{k_N}) P^{-1}$ for every $t \in \mathbb{C}_\ell^\times$.

Lean: `UpperTheory.Gal.Int.Div.htCochar_of` (also `PositivityTheory.AutomorphicGaloisHodgeTate.Div.HTCochar`, `GlobalTheory.HodgeTateCochar.mem_closure_of_jumps`, `UpperTheory.Gal.Int.Div.jumpCard_of`).

*Proof.* A representation with jumps at $\tau$ is de Rham at $w$, and a representation of dimension $N$ that is de Rham at $w$ has, at each $\tau$, a multiset of jumps with exactly $N$ elements, counted with multiplicity. Given this count, the theorem of Sen on the Lie algebra of the image of a Hodge-Tate representation gives $P$ and a list $k_1, \dots, k_N$ of the elements of $J$, such that every $f$ that vanishes on $\rho(D_A)$ vanishes on the torus $P \operatorname{diag}(t^{k_j}) P^{-1}$, $t \in \mathbb{C}_\ell^\times$. A polynomial that vanishes on $\rho(G_E)$ vanishes on $\rho(D_A)$. Each $k'_i$ is in $J$, so it is some $k_j$. $\square$

**Theorem 3.28.6 (Lacunary Lie element).** Let $\rho : G_E \to \mathrm{GL}_N(\overline{\mathbb{Q}}_\ell)$ be continuous with $n$ lacunary jumps. Then there are an algebraically closed field $K' \supset \overline{\mathbb{Q}}_\ell$, a Lie element $X \in M_N(K')$ of $\rho$, and an injective lacunary family $e_1, \dots, e_n$ in $K'$ of roots of the characteristic polynomial of $X$.

Lean: `UpperTheory.Gal.Int.Div.senWLac_holds` (also `UpperTheory.Gal.Int.Div.senWLac_of`, `PositivityTheory.AutomorphicGaloisHodgeTate.Div.cocharToLie_holds`, `PositivityTheory.AutomorphicGaloisHodgeTate.Div.SenWLac`).

*Proof.* Take $K' = \mathbb{C}_\ell$, and $P$ and $k$ from the Hodge-Tate cocharacter theorem. Put $X = P \operatorname{diag}(k_1, \dots, k_N) P^{-1}$. By the lemma, $X$ is a Lie element of $\rho$. The characteristic polynomial of $X$ is $\prod_j (T - k_j)$, so each $e_i = k'_i$ is a root. The family $(k'_i)$ is injective and lacunary in $\mathbb{Q}$, and $\mathbb{Q} \to K'$ is injective, so $(e_i)$ is injective and lacunary in $K'$. $\square$

### The cutting theorem

We use [the small subrepresentation theorem](/entry/goal-holds/) with $\Gamma = G_E$, $K = \overline{\mathbb{Q}}_\ell$ and $n = a$. Its hypotheses are: $\Gamma$ compact; $K$ algebraically closed of characteristic $0$, with a Hausdorff topology that makes it a topological ring; $K' \supset K$ algebraically closed; $\rho$ continuous and semisimple; a dense set $S$ and monic $P_s$ of degree $a$ with $P_s(\rho(s)) = 0$ for $s \in S$; a Lie element $X$ whose characteristic polynomial has an injective lacunary family of $a$ roots; and a continuous character $\psi$ with $\psi(s) = (-1)^a P_s(0)$ on $S$. It gives a continuous semisimple $r : \Gamma \to \mathrm{GL}_a(K)$ with six properties. We use three of them: $r$ is inside $\rho$, $r$ covers $\rho$, and the set of $g$ where the characteristic polynomial of $r(g)$ is separable is open and dense.

**Theorem 3.28.7 (Cutting).** Let $E$ be a number field, $\rho : G_E \to \mathrm{GL}_N(\overline{\mathbb{Q}}_\ell)$ continuous and semisimple with $a$ lacunary jumps, and $\psi : G_E \to \overline{\mathbb{Q}}_\ell^\times$ a continuous character. Assume that the set of $g \in G_E$ for which there is a monic $Q \in \overline{\mathbb{Q}}_\ell[T]$ of degree $a$ with
$$Q(\rho(g)) = 0, \qquad \psi(g) = (-1)^a Q(0)$$
is dense in $G_E$. Then there is a continuous semisimple $r : G_E \to \mathrm{GL}_a(\overline{\mathbb{Q}}_\ell)$, inside $\rho$ and covering $\rho$, such that the set of $g$ where the characteristic polynomial of $r(g)$ is separable is open and dense in $G_E$.

Lean: `UpperTheory.Gal.Int.Div.divSet_holds` (also `UpperTheory.Gal.Int.Div.divSet_of`, `UpperTheory.Gal.Int.Div.DivSet`).

*Proof.* The group $G_E$ is profinite, hence compact. The field $\overline{\mathbb{Q}}_\ell$ is algebraically closed of characteristic $0$, and its $\ell$-adic topology is Hausdorff and makes it a topological ring. Let $S$ be the dense set of the hypothesis, and for $s \in S$ choose $Q_s$ as there. By the lacunary Lie element theorem there are $K'$, a Lie element $X$ of $\rho$ and an injective lacunary family of $a$ roots of its characteristic polynomial. All hypotheses of the small subrepresentation theorem hold with $P_s = Q_s$, and it gives $r$, continuous and semisimple, inside $\rho$, covering $\rho$, with an open dense set of separable elements. The map $g \mapsto r(g)^{-1} = r(g^{-1})$ is continuous too, so $r$ is continuous as a map to the group $\mathrm{GL}_a(\overline{\mathbb{Q}}_\ell)$. $\square$

The small subrepresentation theorem also gives $\det r = \psi$, $Q_s(r(s)) = 0$ on $S$, and equal characteristic polynomials in good cases. The cutting theorem does not keep them. Section 24 gets the characteristic polynomials again from fact 5 (separable pinning).

**Remark 3.28.8 (Formalization).** `divSet_holds` is in [DivisionOneGeometricRepresentation.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/ZetaCharacterDivisibility/DivisionOneGeometricRepresentation.lean#L52) and `divSet_of` in [PDivSet.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/ZetaCharacterDivisibility/PDivSet.lean#L16). We read `divSet_of`, `lacBridge_of`, `htCochar_of`, `inLie_of_cochar` and `cocharToLie_holds` in full. We read only the statements of `jumpCard_of`, of `GlobalTheory.HodgeTateCochar.mem_closure_of_jumps` ([MemClosureOfJumps.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/MemClosureOfJumps.lean#L69)), which is the Sen type input over $\mathbb{C}_\ell$, and of `LateralTheory.DivDb.goal_holds`. Odd points. `divSet_of` takes `InFacts` as an argument and does not use it (PDivSet.lean line 18). It drops four of the conclusions of `DivWCoreLac`, among them $\det r = \psi$ (line 37). `DivSet` asks no CM condition on $E$ ([PhiOfDivOf.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/ZetaCharacterDivisibility/PhiOfDivOf.lean#L121)). There are two lacunary predicates, `Lacunary` on finite sets of integers and `IsLac` on families in a field, and `LacBridge` passes from one to the other by listing the set in order. The thirteen inputs of `goal_holds` all carry the name `intersectionNumber_baseChange` ([GoalHolds.lean](lean:Development/EtaleCohomology/DivisorCycles/GoalHolds.lean#L19)), which does not describe them.
