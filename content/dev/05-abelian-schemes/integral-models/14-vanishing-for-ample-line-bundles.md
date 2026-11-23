---
title: Vanishing for ample line bundles
decls:
  - GlobalTheory.AmpleGen.ampleVanishing
  - GlobalTheory.AmpleSecBC.fieldVanishing
  - GlobalTheory.AmpleSecBC.geomVanishing
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Vanishing for ample line bundles

Let $A$ be an abelian variety over an algebraically closed field $K$ and $L$ an [[ample|RRK8P6TXG2]] line bundle on $A$. Then $H^i(A, L) = 0$ for all $i > 0$ (Mumford, *Abelian Varieties*, Chapter III, the vanishing theorem; see also [the theorem of the cube](/learn/abelian-varieties/#the-theorem-of-the-cube) in Volume 1). This section proves this vanishing for Čech cohomology on finite affine covers, and deduces that $H^1$ of every positive power of a relatively ample line bundle vanishes on every geometric fibre of an abelian scheme. The next section uses the fibrewise vanishing to find bases of sections that are stable under base change, which the construction of the scheme of homomorphisms in Section 8.9 needs.

### Čech cohomology on affine covers

**Definition 8.14.1 (Čech nonvanishing and acyclicity).** Let $X$ be a scheme, $P$ a line bundle on $X$ and $j \geq 0$.

1. $P$ has *nonzero Čech cohomology in degree $j$* if there are a finite totally ordered set $I$ and affine open sets $W_i \subseteq X$, $i \in I$, that cover $X$, such that the Čech complex of $P$ for the cover $(W_i)$ is not exact in degree $j$. We write $\operatorname{NV}(P, j)$.
2. Let $f : X \to Y$. Then $P$ is *relatively acyclic* over $Y$ if for every affine open $U \subseteq Y$ and every finite cover of $f^{-1}(U)$ by affine open sets $W_i$ with $I$ totally ordered, the Čech complex of $P$ for $(W_i)$ is exact in every degree $n \geq 1$.
3. The *first cohomology of $P$ vanishes* if for every open cover $(V_a)$ of $X$ in which $P$ is trivial on each $V_a$, every Čech $1$-cocycle of $P$ on $(V_a)$ is a coboundary.

Lean: `GlobalTheory.AmpleGen.NV` (also `GlobalTheory.CxForm.IsRelAcyclic` and `GlobalTheory.AbLaw.FirstCohomologyVanishes`).

An abelian variety is noetherian and separated. For such a scheme the Čech complex of a quasi-coherent sheaf on an affine open cover computes sheaf cohomology (Hartshorne, *Algebraic Geometry*, III.4.5). So for an abelian variety, $\operatorname{NV}(P, j)$ says $H^j(A, P) \neq 0$, and $P$ is relatively acyclic over $\operatorname{Spec} K$ if and only if $H^n(A, P) = 0$ for all $n \geq 1$.

For a line bundle $L$ on a group scheme $A$ and integers $a, b$ put
$$L(a, b) = L^{a} \otimes [-1]^* L^{b}, \qquad \operatorname{tri}(n) = \frac{n^2 + n}{2}.$$
By the theorem of the cube, $[n]^* L \cong L(\operatorname{tri}(n), \operatorname{tri}(-n))$ on an abelian variety. This is why the numbers $\operatorname{tri}(n)$ occur below.

We use the following results. In results 2 to 5, $K$ is algebraically closed and $A$ is an abelian variety over $K$.

1. (Acyclicity from covers.) Let $A$ be a group scheme over a field $K$ and $P$ a line bundle on $A$. If $\operatorname{NV}(P, j + 1)$ fails for every $j \geq 0$, then $P$ is relatively acyclic over $\operatorname{Spec} K$.
2. (The bundle $L(1, 0)$.) For every line bundle $L$ and every $j$, $\operatorname{NV}(L, j)$ implies $\operatorname{NV}(L(1, 0), j)$.
3. (Vanishing in high degree.) There is $c \geq 0$ such that $\operatorname{NV}(P, j)$ fails for every line bundle $P$ on $A$ and every $j \geq c$.
4. (Künneth and an isogeny.) Let $\alpha, \beta, \gamma, \delta \in \mathbb{Z}$ with $\alpha\beta + \gamma\delta = 0$ and $\alpha\delta - \beta\gamma \neq 0$ in $K$. Let $L$ be a line bundle on $A$, $a, b \geq 0$ and $j \geq 0$ with $\operatorname{NV}(L(a, b), j)$. Then there are $j_1 + j_2 = 2j$ with $\operatorname{NV}(L(a_1, b_1), j_1)$ and $\operatorname{NV}(L(a_2, b_2), j_2)$, where
$$\begin{aligned} a_1 &= a\operatorname{tri}(\alpha) + b\operatorname{tri}(-\alpha) + a\operatorname{tri}(\gamma) + b\operatorname{tri}(-\gamma), \\ b_1 &= a\operatorname{tri}(-\alpha) + b\operatorname{tri}(\alpha) + a\operatorname{tri}(-\gamma) + b\operatorname{tri}(\gamma), \\ a_2 &= a\operatorname{tri}(\beta) + b\operatorname{tri}(-\beta) + a\operatorname{tri}(\delta) + b\operatorname{tri}(-\delta), \\ b_2 &= a\operatorname{tri}(-\beta) + b\operatorname{tri}(\beta) + a\operatorname{tri}(-\delta) + b\operatorname{tri}(\delta). \end{aligned}$$
5. (Serre vanishing along a line.) Let $L$ be relatively ample and $d \in \mathbb{Z}$. There is $N$ such that $\operatorname{NV}(L(a, b), j + 1)$ fails for all $a, b \geq 0$ with $a + b \geq N$ and $a - b = d$, and all $j \geq 0$.

By the comparison above, result 3 follows from Grothendieck's vanishing theorem (Hartshorne, III.2.7), with $c = \dim A + 1$. Result 4 has the shape of the Künneth formula on $A \times A$ for $L(a, b) \boxtimes L(a, b)$, pulled back along the isogeny $(x, y) \mapsto (\alpha x + \beta y, \gamma x + \delta y)$. Result 5 has the shape of Serre's vanishing theorem for the ample bundles $L(a, b)$, $a + b$ large, on a line $a - b = d$.

### The vanishing theorem

**Lemma 8.14.2 (The growth step).** Let $K$ be algebraically closed, $A$ an abelian variety over $K$, $L$ a line bundle on $A$, and $a, b, i \geq 0$ with $\operatorname{NV}(L(a, b), i)$. Then there are $i_1 + i_2 = 2i$ and $a_1, b_1, a_2, b_2 \geq 0$ with $\operatorname{NV}(L(a_1, b_1), i_1)$ and $\operatorname{NV}(L(a_2, b_2), i_2)$, such that $a_1 + b_1 \geq a + b$, $a_2 + b_2 \geq 2(a + b)$, and either $a_2 - b_2 = a - b$ or $a_2 = b_2$.

Lean: `GlobalTheory.AmpleGen.step` (also `GlobalTheory.AmpleGen.stepTwo` and `GlobalTheory.AmpleGen.stepFive`, the two cases).

*Proof.* We use result 4 and the values $\operatorname{tri}(1) = 1$, $\operatorname{tri}(-1) = 0$, $\operatorname{tri}(2) = 3$ and $\operatorname{tri}(-2) = 1$. If $2 \neq 0$ in $K$, take $(\alpha, \beta, \gamma, \delta) = (1, 1, 1, -1)$. Then $\alpha\beta + \gamma\delta = 0$ and $\alpha\delta - \beta\gamma = -2 \neq 0$. Result 4 gives $(a_1, b_1) = (2a, 2b)$ and $(a_2, b_2) = (a + b, a + b)$. If $2 = 0$ in $K$, then $5 = 1 \neq 0$. Take $(\alpha, \beta, \gamma, \delta) = (1, 2, 2, -1)$. Then $\alpha\beta + \gamma\delta = 0$ and $\alpha\delta - \beta\gamma = -5 \neq 0$. Result 4 gives $(a_1, b_1) = (4a + b, a + 4b)$ and $(a_2, b_2) = (3a + 2b, 2a + 3b)$. Both sums are $5(a + b)$, and $a_2 - b_2 = a - b$. $\square$

**Theorem 8.14.3 (Vanishing for ample line bundles).** Let $K$ be an algebraically closed field, $A$ an abelian variety over $K$ and $L$ a relatively ample line bundle on $A$. Then $L$ is relatively acyclic over $\operatorname{Spec} K$.

Lean: `GlobalTheory.AmpleGen.ampleVanishing`.

*Proof.* By result 1 we must show that $\operatorname{NV}(L, j + 1)$ fails for every $j$. Suppose that $\operatorname{NV}(L, j + 1)$ holds. By result 2, $\operatorname{NV}(L(1, 0), j + 1)$ holds. Let $\Sigma$ be the set of degrees $i \geq 1$ such that $\operatorname{NV}(L(a, b), i)$ holds for some $a, b \geq 0$ with $a + b \geq 1$. Then $j + 1 \in \Sigma$, and $\Sigma \subseteq [1, c]$ by result 3. Let $T$ be the largest element of $\Sigma$, with $(a, b)$ such that $a + b \geq 1$ and $\operatorname{NV}(L(a, b), T)$.

We claim the following. If $a' + b' \geq 1$ and $\operatorname{NV}(L(a', b'), T)$, then there is $(a_2, b_2)$ with $\operatorname{NV}(L(a_2, b_2), T)$, $a_2 + b_2 \geq 2(a' + b')$, and $a_2 - b_2 \in \{a' - b', 0\}$. Apply the growth step to $(a', b')$ and $T$. It gives $i_1 + i_2 = 2T$. If $i_1 \geq 1$, then $i_1 \in \Sigma$, since $a_1 + b_1 \geq a' + b' \geq 1$, so $i_1 \leq T$. The same holds for $i_2$. So $i_1 \leq T$ and $i_2 \leq T$, and $i_1 + i_2 = 2T$ forces $i_2 = T$. The pair $(a_2, b_2)$ proves the claim.

Start from $(a, b)$ and apply the claim $n$ times. We get pairs $(a', b')$ with $\operatorname{NV}(L(a', b'), T)$ and $a' + b' \geq n$. The difference $a' - b'$ stays $a - b$ until it becomes $0$, and then it stays $0$. Result 5 for $d = a - b$ and for $d = 0$ gives bounds $N_1$ and $N_2$. Take $n = N_1 + N_2$. As $T \geq 1$, the pair $(a', b')$ contradicts result 5 for the value of $a' - b'$. $\square$

The argument does not compute any cohomology group. It plays the Künneth formula, which doubles degrees, against the bound of result 3 and Serre vanishing, which kills high powers.

### Positive powers and geometric fibres

**Corollary 8.14.4 (Vanishing of $H^1$ over a field).** Let $K$ be an algebraically closed field, $B$ an abelian variety over $K$, $M$ a relatively ample line bundle on $B$ and $a \geq 1$. Then the first cohomology of $M^a$ vanishes.

Lean: `GlobalTheory.AmpleSecBC.fieldVanishing`.

*Proof.* We use two more results. (6) If $X$ is a scheme over a ring $R$ and $M$ is relatively ample on $X$, then $M^a$ is relatively ample for every $a \geq 1$. (7) If $X$ is a quasi-compact scheme over $\operatorname{Spec} R$ and the line bundle $P$ on $X$ is relatively acyclic over $\operatorname{Spec} R$, then the first cohomology of $P$ vanishes. By (6), $M^a$ is relatively ample. By the theorem, $M^a$ is relatively acyclic over $\operatorname{Spec} K$. The abelian variety $B$ is proper over $K$, so it is quasi-compact, and (7) gives the claim. $\square$

**Corollary 8.14.5 (Vanishing of $H^1$ on geometric fibres).** Let $S$ be a scheme, $A$ an [[abelian scheme|JDDXZ89N33]] over $S$, $L$ a relatively ample line bundle on $A$ and $a \geq 1$. Let $T$ be a scheme over $S$, $K$ an algebraically closed field and $q : \operatorname{Spec} K \to T$. Then there is a fibre product $X' = A_T \times_T \operatorname{Spec} K$, with projection $\pi : X' \to A_T$, such that the first cohomology of $\pi^* L_T^a$ vanishes.

Lean: `GlobalTheory.AmpleSecBC.geomVanishing`.

*Proof.* We use one more result. (8) If the conclusion of the previous corollary holds for every algebraically closed $K$, every abelian variety $B$ over $K$, every relatively ample $M$ and every $a \geq 1$, then the conclusion of the present corollary holds. The previous corollary gives the hypothesis of (8). $\square$

**Remark 8.14.6 (Formalization).** The vanishing theorem is the statement of a published result, kept with the published theorems: [IsL2OnDiagonalOfIsL2Metric.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/IsL2OnDiagonalOfIsL2Metric.lean#L297). Here it is proved, not assumed: [AmpleVanishing.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/AmpleVanishing.lean#L66). The case split on the characteristic is at [AmpleVanishing.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/AmpleVanishing.lean#L57). The bundles $L(a, b)$, the numbers $\operatorname{tri}(n)$ and the condition $\operatorname{NV}$ are defined in [Tri.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/Tri.lean#L16); $\operatorname{tri}(n)$ is defined with integer division, which is exact. Relative acyclicity is stated for Čech complexes on finite, totally ordered affine covers: [CharChPartZero.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/CharChPartZero.lean#L167). The comparison with sheaf cohomology and the readings of results 3 to 5 above are ours. We read the statements of results 1 to 8, not their proofs.
