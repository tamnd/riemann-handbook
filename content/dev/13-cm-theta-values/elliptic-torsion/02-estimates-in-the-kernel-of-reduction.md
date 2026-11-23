---
title: Estimates in the kernel of reduction
decls:
  - ReciprocityTheory.ChartRestriction.L1.formalGroup_add_estimate
  - ReciprocityTheory.ChartRestriction.L1.formalGroup_nsmul_estimate
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Estimates in the kernel of reduction

This section turns the formal group law of [the previous section](/entry/formal-group-points-hom/) into two inequalities. To first order, the parameter $u$ is additive on the kernel of reduction $E_1$, and the error is at most the square of the size of the points. By induction, $u(nD)$ is close to $n\,u(D)$. A corollary says that $u(M^k D) \to 0$ when $|M| < 1$. The proof that [torsion points are unramified](/entry/tor-x-mem/) uses this corollary to approximate a torsion point by points with coordinates in the unramified field.

We keep the notation of the previous section. The field $K$ is complete with an ultrametric absolute value, $W$ is an integral model over $K$, and $E_1$ is the set of the point $O$ and the nonsingular points $(x, y)$ with $|x| > 1$. The parameter is $u(O) = 0$ and $u(x, y) = -x/y$. For $n \in \mathbb{N}$, we write $n$ also for its image $n \cdot 1$ in $K$. The ultrametric inequality gives $|n| \le 1$.

### The size of a point

**Lemma 7.2.1 (Size of the parameter).** Let $W$ be an integral model and $P \in E_1$. Then $|u(P)| < 1$. If $P = (x, y)$, then $|u(P)|^2 = |x|^{-1}$.

Lean: `ReciprocityTheory.ChartRestriction.L1.formalGroup_param_norm_lt_one`

*Proof.* For $P = O$ this is clear. For $P = (x, y)$ with $|x| > 1$, the proof of [the parametrization theorem](/entry/formal-group-points-param/) shows $|y|^2 = |x|^3$. So $|u(P)|^2 = |x|^2/|y|^2 = |x|^{-1} < 1$. $\square$

So a point of $E_1$ is small when $|x|$ is large: the parameter measures how deep the point lies in the kernel of reduction.

### Addition

**Theorem 7.2.2 (Additivity to first order).** Let $W$ be an integral model over $K$ and let $P, Q \in E_1$. Then
$$\bigl|u(P + Q) - u(P) - u(Q)\bigr| \le \max\bigl(|u(P)|, |u(Q)|\bigr)^2 .$$

Lean: `ReciprocityTheory.ChartRestriction.L1.formalGroup_add_estimate`

*Proof.* Let $w$ be the solution of equation (1) of the previous section (Silverman, *The Arithmetic of Elliptic Curves*, Proposition IV.1.1). There is a chord series $F$ for $(W, w)$ whose coefficients lie in the ring $\mathbb{Z}[a_1, a_2, a_3, a_4, a_6]$, with $F(0, 0) = 0$ and with coefficient $1$ at $X$ and at $Y$. This is the formal group law of $W$ (Silverman, Chapter IV, §1). An element of $\mathbb{Z}[a_1, \dots, a_6]$ has absolute value at most $1$, because the $a_i$ do and the absolute value is ultrametric. So $F$ is integral. By [the homomorphism theorem](/entry/formal-group-points-hom/), with $a = u(P)$ and $b = u(Q)$,
$$u(P + Q) - u(P) - u(Q) = F(a, b) - a - b = G(a, b), \qquad G = F - X - Y .$$
The series $G$ is integral and has no terms of degree $0$ or $1$. Let $r = \max(|a|, |b|)$; then $r < 1$ by the lemma. Each term $G_{ij} a^i b^j$ with $i + j \ge 2$ has absolute value at most $r^{i + j} \le r^2$. The sum converges, and by the ultrametric inequality $|G(a, b)| \le r^2$. $\square$

The estimate needs no condition on the discriminant: it uses only the chord series and the integrality of $W$.

### Multiplication by $n$

**Theorem 7.2.3 (Multiplication by $n$ to first order).** Let $W$ be an integral model over $K$ with $|\Delta| = 1$, let $D \in E_1$ and $n \in \mathbb{N}$. Then $nD \in E_1$ and
$$\bigl|u(nD) - n\,u(D)\bigr| \le |u(D)|^2 .$$

Lean: `ReciprocityTheory.ChartRestriction.L1.formalGroup_nsmul_estimate`

*Proof.* We use induction on $n$. For $n = 0$, $0 \cdot D = O$ lies in $E_1$ and both sides are $0$. Assume the claim for $n$. Since $|\Delta| = 1$, the set $E_1$ is closed under addition (this is the subgroup property of the kernel of reduction, Silverman, Proposition VII.2.1). So $(n + 1)D = nD + D \in E_1$. Put $r = |u(D)| < 1$. By the induction hypothesis and $|n| \le 1$,
$$|u(nD)| \le \max\bigl(|u(nD) - n\,u(D)|,\ |n\,u(D)|\bigr) \le \max(r^2, r) = r .$$
By the additivity theorem applied to $nD$ and $D$,
$$|u(nD + D) - u(nD) - u(D)| \le \max(|u(nD)|, r)^2 = r^2 .$$
Now
$$u((n + 1)D) - (n + 1)u(D) = \bigl(u(nD + D) - u(nD) - u(D)\bigr) + \bigl(u(nD) - n\,u(D)\bigr),$$
and both terms have absolute value at most $r^2$. $\square$

### Contraction

**Corollary 7.2.4 (Contraction).** Let $W$ be an integral model over $K$ with $|\Delta| = 1$, let $D \in E_1$, and let $M \in \mathbb{N}$ with $|M| < 1$. Put $c = \max(|M|, |u(D)|)$. Then for every $k \ge 0$,
$$|u(M^k D)| \le c^k\, |u(D)| ,$$
and so $|u(M^k D)| \to 0$ as $k \to \infty$.

Lean: `ReciprocityTheory.ChartRestriction.L1.formalGroup_pow_tendsto_zero`

*Proof.* Induction on $k$; the case $k = 0$ is clear. Let $D_k = M^k D$. It lies in $E_1$ by the previous theorem, and $|u(D_k)| \le c^k |u(D)| \le |u(D)|$ because $c < 1$. Apply the previous theorem to $D_k$ and $n = M$:
$$|u(M D_k)| \le \max\bigl(|u(M D_k) - M u(D_k)|,\ |M|\,|u(D_k)|\bigr) \le \max\bigl(|u(D_k)|^2,\ |M|\,|u(D_k)|\bigr).$$
Both terms are at most $c\,|u(D_k)|$, since $|u(D_k)| \le |u(D)| \le c$. So $|u(D_{k+1})| \le c^{k+1}|u(D)|$. Since $0 \le c < 1$, the bound tends to $0$. $\square$

**Example 7.2.5.** Let $K = \mathbb{C}_l$ and $M = l$. Then $|M| = l^{-1}$. For $D = (x, y) \in E_1$ with $|x| = l^2$, the lemma gives $|u(D)| = l^{-1}$, so $c = l^{-1}$ and the corollary gives $|u(l^k D)| \le l^{-k-1}$. If instead $|x| = l$, then $c = l^{-1/2}$ and the bound is $l^{-(k+1)/2}$. In the language of formal groups, multiplication by $l$ is $[l](T) = lT + (\text{higher terms})$, and on the open disc it contracts towards $0$.

**Remark 7.2.6 (Formalization).** The additivity theorem has no hypothesis on the discriminant: [TorChord.lean](lean:ReciprocityTheory/ReductiveGroups/UnramifiedIntegrals/TorChord.lean#L147). The theorem on multiplication by $n$ uses $|\Delta| = 1$ only to keep the multiples of $D$ in $E_1$, through the subgroup property of $E_1$: [TorContr.lean](lean:ReciprocityTheory/ReductiveGroups/UnramifiedIntegrals/TorContr.lean#L15). In both theorems the field is any complete normed field with an ultrametric absolute value; it need not be $\mathbb{C}_l$.
