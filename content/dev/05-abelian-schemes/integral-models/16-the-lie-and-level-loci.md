---
title: The Lie and level loci
decls:
  - GlobalTheory.UPel.HT.lieHer_closed
  - GlobalTheory.UPel.HT.lieGeom_locus_closed
  - GlobalTheory.T.harrisTaylor_lie_tate_loci_closed_siegelPullback
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Lie and level loci

An object of level $N$ (Definition 8.1.3) has two conditions that are not stable under every operation we use: the condition on the Lie algebra, and the condition that the level map comes from an isomorphism of Tate modules at each geometric point. This section proves that both conditions cut out a closed subscheme. The first theorem does this for the Lie condition on any smooth commutative group scheme with an action of $O$. The second theorem does it for both conditions together on a group scheme that is a pullback of a Siegel object. The next section uses the second theorem to show that objects of level $N$ are relatively representable over the Siegel moduli scheme.

Throughout, $D$ is a datum for $p$ (Definition 8.1.1), $b$ is a base for $D$ over a ring $R$ (Definition 8.1.2) and $s : S \to \operatorname{Spec} R$ is a scheme over $R$. For a ring $R'$ we write $R'[\varepsilon] = R'[\varepsilon]/(\varepsilon^2)$.

### The conditions

Let $A$ be a commutative group scheme over $S$ with an action of $O$. Let $x : \operatorname{Spec} R' \to S$. A *tangent vector* at $x$ is a map $v : \operatorname{Spec} R'[\varepsilon] \to A$ over $S$, where $\operatorname{Spec} R'[\varepsilon]$ maps to $S$ through $x$, whose restriction to $\operatorname{Spec} R'$ is the zero section. An element $c \in O$ *acts on $v$ by* $r \in R'$ if $c \circ v$ is $v$ composed with the map of $\operatorname{Spec} R'[\varepsilon]$ given by $\varepsilon \mapsto r\varepsilon$.

**Definition 8.16.1 (The Hermitian Lie condition).** Let $\beta : R \to R'$ and $x : \operatorname{Spec} R' \to S$. The *Lie condition* at $(\beta, x)$ holds if every tangent vector $v$ at $x$ on which $\omega$ acts by $\beta(\rho)$ is a sum $v = w_1 + \dots + w_a$ of tangent vectors such that each $c \in \mathcal{O}_F$ acts on $w_i$ by $\beta(t_i(c))$. The *rank condition* at $(\beta, x)$ holds if for every algebraically closed field $k$, every $g : R' \to k$ and every $i$, the tangent vectors at $x \circ \operatorname{Spec} g$ on which every $c \in \mathcal{O}_F$ acts by $g(\beta(t_i(c)))$ have a basis of $m$ vectors over $k$. That is, there are $v_1, \dots, v_m$ such that each such tangent vector is $\sum_j c_j v_j$ for unique $c_j \in k$. The *Hermitian Lie condition* at $(\beta, x)$ holds if, for every ring map $g : R' \to R''$, the Lie condition and the rank condition hold at $(g\beta, x \circ \operatorname{Spec} g)$.

Lean: `GlobalTheory.UPel.HT.LieHer` (also `GlobalTheory.UPel.HT.LieAt`, the Lie condition).

**Definition 8.16.2 (The Rosati, level and Tate conditions).** Let $A$ be a commutative group scheme over $S$ with an action of $O$ and let $P$ be a line bundle on $A \times_S A$. The *Rosati condition* holds if $(c \times 1)^* P \cong (1 \times c^*)^* P$ for every $c \in O$. Let $N \geq 0$. A map $\eta : \Lambda \to A(S)$ *is a level map of level $N$* if it is additive, satisfies $\eta(cx) = c\,\eta(x)$ for $c \in O$, and satisfies $\eta(Nx) = 0$. Let $k$ be a field and $x : \operatorname{Spec} k \to S$. The *Tate condition* holds at $x$ if there are primitive roots of unity $\zeta_n \in k$ and maps $I_n : \Lambda \to A_x(k)$, for $n > 0$ prime to $p$, with these properties. Each $I_n$ is additive and $O$-linear, its kernel is $n\Lambda$, and its image is the $n$-torsion of $A_x(k)$. The maps are compatible: $\zeta_{nm}^m = \zeta_n$ and $m\,I_{nm}(y) = I_n(y)$. The Weil pairing of $\Delta^* P$ satisfies $e_n(I_n(y), I_n(z)) = \zeta_n^{2E(y, z)}$. Finally $\eta(y)$ restricted to $x$ is $I_N(y)$ for every $y \in \Lambda$.

Lean: `GlobalTheory.UPel.HT.GeomAt` (also `GlobalTheory.UPel.HT.RosatiFor`, the Rosati condition, and `GlobalTheory.UPel.HT.EtaOK`, the level map).

The Tate condition is the condition at geometric points in Definition 8.1.3, written out.

### Inputs

We use the following results.

1. (A criterion for closed subschemes.) Let $Q$ be a property of maps $x : \operatorname{Spec} R' \to S$ with three properties. (a) If $Q(x)$ holds, then $Q(x \circ \operatorname{Spec} g)$ holds for every $g : R' \to R''$. (b) If $t \subseteq R'$ is finite, generates the unit ideal, and $Q$ holds for the composite $\operatorname{Spec} R'_r \to \operatorname{Spec} R' \to S$ for each $r \in t$, then $Q(x)$ holds. (c) Every point of $S$ has an affine open neighbourhood $U$ and an ideal $K \subseteq \mathcal{O}(U)$ such that for every $f : \mathcal{O}(U) \to R'$, $Q$ holds for $\operatorname{Spec} R' \to U \to S$ if and only if $K \subseteq \ker f$. Then there is a [[closed immersion|WWRWYSJDET]] $i : Z \to S$ such that $Q(x)$ holds if and only if $x$ factors through $i$.
2. (The Lie condition is local.) Let $A$ be a commutative group scheme over $S$ with an action of $O$, $\beta : R \to R'$, $x : \operatorname{Spec} R' \to S$, and $t \subseteq R'$ finite generating the unit ideal. If the Lie condition holds at the composite of $\beta$ and $x$ with $R' \to R'_r$ for each $r \in t$, then it holds at $(\beta, x)$.
3. (The Kottwitz ideal.) Let $A$ be a [[smooth|EXKGG9X6J0]] commutative group scheme over $S$ with an action of $O$. Every point of $S$ has an affine open neighbourhood $U$ and an ideal $K \subseteq \mathcal{O}(U)$ with this property. For every $f : \mathcal{O}(U) \to R'$ and every $\beta : R \to R'$ such that $\operatorname{Spec} R' \to U \to S \to \operatorname{Spec} R$ is $\operatorname{Spec} \beta$, the Hermitian Lie condition holds at $\beta$ and $\operatorname{Spec} R' \to U$ if and only if $K \subseteq \ker f$.
4. (Pullbacks of abelian schemes.) A group pullback (Definition 8.2.5) of an [[abelian scheme|JDDXZ89N33]] is an abelian scheme.
5. (A pre-object.) Let $c$ be a Siegel object over $s_1 : S \to \operatorname{Spec} B$ whose kernel is killed by $e$ prime to $p$, and let $t : S \to \operatorname{Spec} R$. Let $\pi_X : X \to S$ and $(A_X, \varphi_X, \varphi_{2X}, \eta_X)$ be as in the second theorem below. Then there is a *pre-object* $o$ of level $N$ over $t \pi_X$, that is, all data and conditions of Definition 8.1.3 except the Lie condition and the Tate condition, such that for every field $k$ and every $x : \operatorname{Spec} k \to X$, the Tate condition for $o$ at $x$ holds if and only if it holds for $(A_X, \varphi_{2X}^* P_c, \eta_X)$ at $x$.
6. (The Tate locus is open and closed.) Let $N \geq 3$ be prime to $p$, let $X$ be locally noetherian and let $o$ be a pre-object of level $N$ over $X$. Then there is an open and closed set $U \subseteq X$ such that a geometric point $x : \operatorname{Spec} k \to X$ lands in $U$ if and only if the Tate condition for $o$ holds at $x$.
7. (Restriction to an open and closed set.) Let $i : Z_1 \to X$ be a closed immersion and $U \subseteq X$ open and closed. Then there is a closed immersion $j : Z \to X$ such that $g : T \to X$ factors through $j$ if and only if $g$ factors through $i$ and the image of $g$ lies in $U$.
8. (Factoring through a closed immersion.) Let $i : Z \to X$ be a closed immersion and $g : T \to X$. If $g x$ factors through $i$ for every $x : \operatorname{Spec} R' \to T$, then $g$ factors through $i$.
9. (Geometric points.) For every point $\tau$ of a scheme $T$ there are an algebraically closed field $k$ and $x : \operatorname{Spec} k \to T$ with image $\{\tau\}$.

We also use two standard facts. Every map $\operatorname{Spec} R' \to \operatorname{Spec} R$ is $\operatorname{Spec} \beta$ for a unique $\beta : R \to R'$, and $\operatorname{Spec}$ carries composites of ring maps to composites in the reverse order.

### The Lie locus

**Theorem 8.16.3 (The Lie locus is closed).** Let $A$ be a smooth commutative group scheme over $S$ with an action of $O$. Then there is a closed immersion $i : Z \to S$ with this property. For every ring $R'$, every $\beta : R \to R'$ and every $x : \operatorname{Spec} R' \to S$ with $s x = \operatorname{Spec} \beta$, the map $x$ factors through $i$ if and only if the Hermitian Lie condition holds at $(\beta, x)$.

Lean: `GlobalTheory.UPel.HT.lieHer_closed`.

*Proof.* For $x : \operatorname{Spec} R' \to S$ let $Q(x)$ be the statement that the Hermitian Lie condition holds at $(\beta, x)$ for every $\beta$ with $s x = \operatorname{Spec} \beta$. Such a $\beta$ exists and is unique. So, for $s x = \operatorname{Spec} \beta$, $Q(x)$ holds if and only if the Hermitian Lie condition holds at $(\beta, x)$. We check the three properties of result 1.

(a) Let $g : R' \to R''$ and let $s x = \operatorname{Spec} \beta$. Then $s x \operatorname{Spec} g = \operatorname{Spec}(g\beta)$. For $g' : R'' \to R'''$, the Lie and rank conditions at $(g' g \beta, x \operatorname{Spec}(g' g))$ are part of the Hermitian Lie condition at $(\beta, x)$, applied to $g' g$. So $Q(x \operatorname{Spec} g)$ holds.

(b) Let $t \subseteq R'$ be finite, generating the unit ideal, with $Q$ on each $R'_r$. Let $s x = \operatorname{Spec} \beta$ and $g : R' \to R''$. The set $g(t)$ generates the unit ideal of $R''$. For $r \in t$, the map $R' \to R'_r \to R''_{g(r)}$ equals $R' \to R'' \to R''_{g(r)}$. So $Q$ on $R'_r$, applied to $R'_r \to R''_{g(r)}$, gives the Lie condition on each $R''_{g(r)}$. Result 2 then gives the Lie condition at $(g\beta, x \operatorname{Spec} g)$. For the rank condition, let $g' : R'' \to k$ with $k$ algebraically closed. Some $r \in t$ has $g'(g(r)) \neq 0$, since otherwise the kernel of $g' g$ contains the ideal generated by $t$, which contains $1$. So $g' g$ factors through $R'_r$, and the rank condition at this geometric point is part of $Q$ on $R'_r$.

(c) This is result 3, since $A$ is smooth, together with the uniqueness of $\beta$.

Result 1 gives $i : Z \to S$ such that $x$ factors through $i$ if and only if $Q(x)$ holds. $\square$

### The Lie and Tate loci over a Siegel family

**Theorem 8.16.4 (The Lie and Tate loci are closed).** Let $N \geq 3$ be prime to $p$. Let $c$ be a Siegel object of genus $h$ and level $M$ over $s_1 : S \to \operatorname{Spec} B$, with $\zeta \in B$, whose kernel is killed by an integer $e$ prime to $p$, and let $t : S \to \operatorname{Spec} R$. Let $X$ be a locally [[noetherian|0670T59HGE]] scheme with $\pi_X : X \to S$. Let $A_X$ be a commutative group scheme over $X$ with an action of $O$ and a level map $\eta_X$ of level $N$. Let $\varphi_X : A_X \to A_c$ be a group pullback along $\pi_X$ and $\varphi_{2X} : A_X \times_X A_X \to A_c \times_S A_c$ a map that is $\varphi_X$ on each factor. Suppose that the Rosati condition holds for $\varphi_{2X}^* P_c$. Then there is a closed immersion $j : Z \to X$ such that a map $g : T \to X$ factors through $j$ if and only if both of the following hold:

1. the Hermitian Lie condition holds at $(\beta, g x)$ for every ring $R'$, every $\beta : R \to R'$ and every $x : \operatorname{Spec} R' \to T$ with $t \pi_X g x = \operatorname{Spec} \beta$;
2. the Tate condition for $(A_X, \varphi_{2X}^* P_c, \eta_X)$ holds at $g x$ for every algebraically closed field $k$ and every $x : \operatorname{Spec} k \to T$.

Lean: `GlobalTheory.UPel.HT.lieGeom_locus_closed` (also `GlobalTheory.T.harrisTaylor_lie_tate_loci_closed_siegelPullback`, a second name).

*Proof.* By result 4, $A_X$ is an abelian scheme, so it is smooth. The theorem on the Lie locus, for $A_X$ over $t \pi_X : X \to \operatorname{Spec} R$, gives a closed immersion $i_1 : Z_1 \to X$. Result 5 gives a pre-object $o$ of level $N$ over $t \pi_X$ with the same Tate condition as $(A_X, \varphi_{2X}^* P_c, \eta_X)$. As $N \geq 3$ is prime to $p$ and $X$ is locally noetherian, result 6 gives an open and closed set $U \subseteq X$. Result 7, for $i_1$ and $U$, gives $j : Z \to X$. So $g$ factors through $j$ if and only if $g$ factors through $i_1$ and the image of $g$ lies in $U$. We show that the first statement is condition 1 and the second is condition 2.

Suppose that $g = i_1 y$. For $x$ and $\beta$ as in condition 1, the map $g x = i_1 (y x)$ factors through $i_1$, so the Hermitian Lie condition holds at $(\beta, g x)$. Conversely, suppose condition 1. Let $x : \operatorname{Spec} R' \to T$, and let $\beta$ be the ring map with $t \pi_X g x = \operatorname{Spec} \beta$. By condition 1 and the choice of $i_1$, the map $g x$ factors through $i_1$. Result 8 shows that $g$ factors through $i_1$.

Suppose that the image of $g$ lies in $U$, and let $x : \operatorname{Spec} k \to T$ be a geometric point. The image of $g x$ lies in $U$, so the Tate condition for $o$ holds at $g x$ by result 6, and the condition for $(A_X, \varphi_{2X}^* P_c, \eta_X)$ holds by result 5. Conversely, suppose condition 2 and let $\tau \in T$. Result 9 gives a geometric point $x$ of $T$ with image $\{\tau\}$. By condition 2 and result 5, the Tate condition for $o$ holds at $g x$. By result 6, the image of $g x$ lies in $U$, so $g(\tau) \in U$. $\square$

The Lie part of the proof needs no hypothesis on $N$ and no noetherian hypothesis. Both are used only through result 6, for the Tate part.

**Remark 8.16.5 (Formalization).** The first theorem is [LieOcExistsSpMap.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LieOcExistsSpMap.lean#L27), with the two standard facts as helpers at L16 to L25. The conditions are defined in [LieRankAt.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LieRankAt.lean#L13) and [RosatiFor.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/RosatiFor.lean#L16). The rank condition uses the predicate of [TwoWeightEqOneAddRoot.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/TwoWeightEqOneAddRoot.lean#L113), and the Tate isomorphism is the structure of [NotCompactOfMEqOne.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/NotCompactOfMEqOne.lean#L141). The second theorem is [HarrisTaylorLieTateLociClosedSiegelPullback.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HarrisTaylorLieTateLociClosedSiegelPullback.lean#L17). In it, the bounds $N \geq 3$ and $\gcd(N, p) = 1$ are used only by result 6, and the genus $h$, the level $M$, the ring $B$ and $\zeta \in B$ are arbitrary. The Lean statement also asks that $\varphi_{2X}$ be the square of $\varphi_X$ and that $\eta_X$ be a level map, which we have put into the hypotheses. Result 6 is [GeomAtIffOfSpecializes.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/GeomAtIffOfSpecializes.lean#L171); its set $U$ is open and the statement asks that it be closed. Its proof shows that the set is closed under specialization and generization, and it uses $N \geq 3$ only to get $N > 0$: [GeomAtIffOfSpecializes.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/GeomAtIffOfSpecializes.lean#L176). The second name is a wrapper that tries three forms of one proof term under a raised heartbeat limit: [HarrisTaylorLieTateLociClosedSiegelPullbackStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HarrisTaylorLieTateLociClosedSiegelPullbackStatement.lean#L7). We read the statements of results 1 to 9, not their proofs.
