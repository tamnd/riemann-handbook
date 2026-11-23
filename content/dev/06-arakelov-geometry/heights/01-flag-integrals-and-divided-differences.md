---
title: Flag integrals and divided differences
decls:
  - GroundTheory.Heights₂.Heights.RestTerms.LemmaA.full
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Flag integrals and divided differences

This section sets up the algebra of the rest terms. We work in a polynomial ring with $f$ blocks of $N$ variables each. A linear form on this ring, the flag integral, pairs a polynomial with the product of the Vandermonde polynomials of the blocks. The main result, Lemma A below, says two things. First, on polynomials of the top degree the flag integral is a fixed nonzero multiple of the divided difference (the alternating sum over the block permutations, divided by the Vandermonde product). Second, if a polynomial $F$ is written as a combination of power sums, then the flag integral of $G \cdot Q_{k,\tau}$, where $Q_{k,\tau}$ is the coefficient of the $k$-th power sum of block $\tau$, can be read off from one coefficient of the divided difference of $GF$. The rest terms of the next two sections are flag integrals of this form. Lemma A is the tool that turns them into coefficients of Schur polynomials, which [the bound at one prime](/entry/rest-prime-bound-full/) then estimates.

### The ring of roots

Fix integers $f, N \ge 0$. Let
$$R_{f,N} = \mathbb{Q}[X_{\tau,i} : 0 \le \tau < f,\ 0 \le i < N].$$
We call the variables $X_{\tau,0}, \dots, X_{\tau,N-1}$ the roots of block $\tau$. The group $W = S_N^f$ acts on $R_{f,N}$: an element $w = (w_\tau)_\tau$ sends $X_{\tau,i}$ to $X_{\tau,w_\tau(i)}$. Its sign is $\operatorname{sgn}(w) = \prod_\tau \operatorname{sgn}(w_\tau)$. A polynomial is block-symmetric if $W$ fixes it.

**Definition 4.1.1 (Power sums, Vandermonde product).** For $k \ge 0$ and a block $\tau$, the $k$-th power sum of block $\tau$ is $p_k(\tau) = \sum_{i<N} X_{\tau,i}^k$. For a family $v_0, \dots, v_{m-1}$ in a commutative ring, its Vandermonde product is $V(v) = \prod_{i<j}(v_i - v_j)$. The block Vandermonde product is
$$\Delta = \prod_{\tau<f} V(X_{\tau,0}, \dots, X_{\tau,N-1}).$$
It is homogeneous of degree $t = f \cdot N(N-1)/2$, the top degree.

The power sums $p_k(\tau)$ are block-symmetric. The polynomial $\Delta$ is alternating: $w(\Delta) = \operatorname{sgn}(w)\Delta$ for $w \in W$.

**Definition 4.1.2 (Antisymmetrization, divided difference).** For $H \in R_{f,N}$ put
$$A(H) = \sum_{w \in W} \operatorname{sgn}(w)\, w(H).$$
The divided difference of $H$ is the element $\partial(H) = A(H)/\Delta$ of the fraction field of $R_{f,N}$.

The polynomial $A(H)$ is alternating. Each factor $X_{\tau,i} - X_{\tau,j}$ divides an alternating polynomial, since the transposition of $i$ and $j$ in block $\tau$ changes its sign, so the polynomial vanishes when $X_{\tau,i} = X_{\tau,j}$. These factors are pairwise coprime primes of the factorial ring $R_{f,N}$. So $\Delta$ divides $A(H)$, and $\partial(H)$ is a polynomial. It is block-symmetric, because $A(H)$ and $\Delta$ are both alternating. If $H$ is homogeneous of degree $d$, then $\partial(H)$ is homogeneous of degree $d - t$, or zero.

**Example 4.1.3.** Let $f = 1$ and $N = 2$, with roots $x, y$. Then $\Delta = x - y$ and $\partial(H) = (H(x,y) - H(y,x))/(x - y)$. For $H = x$ we get $\partial(H) = 1$. For $H = x^2$ we get $\partial(H) = x + y = p_1$.

**Definition 4.1.4 (Flag integral).** For a polynomial $\Phi \in R_{f,N}$, the flag integral of $\Phi$ is
$$\int \Phi = \sum_{\alpha} [X^\alpha]\Phi \cdot [X^\alpha]\Delta \cdot \alpha!,$$
where $\alpha$ runs over the exponents of the monomials of $\Delta$, $[X^\alpha]$ denotes the coefficient of $X^\alpha$, and $\alpha! = \prod_{\tau,i} \alpha_{\tau,i}!$.

In other words, $\int \Phi = (\Delta(\partial)\Phi)(0)$, where $\Delta(\partial)$ is the differential operator obtained by putting $\partial/\partial X_{\tau,i}$ in place of $X_{\tau,i}$. Only the homogeneous part of degree $t$ of $\Phi$ contributes. The name comes from geometry. On a product of $f$ full flag varieties of $\mathbb{C}^N$, the integral of a polynomial in the Chern roots of the tautological line bundles is, up to a constant, the divided difference of the polynomial (Brion's lectures, in the Notes). We do not use this fact. In this chapter the flag integral is the linear form above.

We record three properties of the flag integral.

1. For $w \in W$, $\int w(\Phi) = \operatorname{sgn}(w) \int \Phi$. Indeed $\Delta(\partial)$ applied to $w(\Phi)$ is $w$ applied to $(w^{-1}\Delta)(\partial)\Phi = \operatorname{sgn}(w)\Delta(\partial)\Phi$, and evaluation at $0$ does not see $w$. So $\int A(\Phi) = |W| \int \Phi = (N!)^f \int \Phi$.
2. $\int \Delta = \sum_\alpha ([X^\alpha]\Delta)^2 \alpha! > 0$, since $\Delta \ne 0$.
3. If $\Phi = \Delta \cdot R$, then $\int \Phi = R(0) \int \Delta$, where $R(0)$ is the constant term of $R$. Indeed $\Delta \cdot (R - R(0))$ has no monomial of degree $t$.

### Power sum decompositions and Lemma A

**Definition 4.1.5 (Power sum decomposition).** Let $F \in R_{f,N}$. A power sum decomposition of $F$ is a family $Q_{k,\tau} \in R_{f,N}$, for $1 \le k \le N$ and $\tau < f$, such that
$$F = \sum_{k=1}^{N} \sum_{\tau<f} p_k(\tau)\, Q_{k,\tau}.$$

A decomposition exists if and only if $F$ lies in the ideal generated by the power sums; it is far from unique. We also need two maps to the polynomial ring $\mathbb{Q}[X_0, \dots, X_{N-1}]$ in one block of variables. The restriction to block $\tau$, written $P \mapsto P|_\tau$, sends $X_{\tau,i}$ to $X_i$ and $X_{\sigma,i}$ to $0$ for $\sigma \ne \tau$. The power sum map $\pi$ is the algebra map with $\pi(X_i) = p_{i+1} = \sum_j X_j^{i+1}$. Since $p_1, \dots, p_N$ are algebraically independent over $\mathbb{Q}$, the map $\pi$ is injective, and its image is the ring of symmetric polynomials. For a symmetric $U$, the unique $S$ with $\pi(S) = U$ writes $U$ as a polynomial in $p_1, \dots, p_N$; the coefficient of the monomial $X_{k-1}$ in $S$ is the coefficient of $p_k$ in this expression.

**Theorem 4.1.6 (Lemma A).** Let $f, N \ge 0$. There is a rational number $c \ne 0$ with the following two properties.

1. For every $H \in R_{f,N}$, homogeneous of degree $t = f \cdot N(N-1)/2$, we have $\int H = c \cdot \partial(H)$ in the fraction field of $R_{f,N}$.
2. Let $F \in R_{f,N}$ and let $(Q_{k,\tau})$ be a power sum decomposition of $F$. Let $1 \le k \le N$, let $\tau < f$, and let $G \in R_{f,N}$ be homogeneous of degree $k - 1$. Then there is a polynomial $P \in R_{f,N}$ with the following properties: $P = \partial(GF)$; if $F$ is homogeneous of degree $t + 1$, then $P|_\tau$ is homogeneous of degree $k$; and there is $S \in \mathbb{Q}[X_0, \dots, X_{N-1}]$ with $\pi(S) = P|_\tau$ and
$$\int G\, Q_{k,\tau} = c \cdot [X_{k-1}] S.$$

Lean: `GroundTheory.Heights₂.Heights.RestTerms.LemmaA.full`

So the flag integral of $G Q_{k,\tau}$ does not depend on the decomposition: it is $c$ times the coefficient of $p_k$ in the block $\tau$ part of $\partial(GF)$.

*Proof.* Put $c = \int \Delta / (N!)^f$. It is positive by property 2, so $c \ne 0$.

First we show: if $A(H) = \Delta \cdot R$, then $\int H = c \cdot R(0)$. By property 1, $(N!)^f \int H = \int A(H) = \int \Delta R$, and by property 3 this is $R(0) \int \Delta$. Divide by $(N!)^f$.

Part 1. Let $H$ be homogeneous of degree $t$. By the discussion after the definition, $A(H) = \Delta \cdot R$ with $R = \partial(H)$ a polynomial, homogeneous of degree $0$, so $R$ is a constant and $R = R(0)$. Hence $\int H = c\, R(0) = c\, \partial(H)$.

Part 2. For each pair $(l, \sigma)$ with $1 \le l \le N$ and $\sigma < f$, write $A(G Q_{l,\sigma}) = \Delta \cdot R_{l,\sigma}$ with $R_{l,\sigma}$ a block-symmetric polynomial. Put
$$P = \sum_{l=1}^{N} \sum_{\sigma<f} p_l(\sigma)\, R_{l,\sigma}.$$
Since $p_l(\sigma)$ is block-symmetric, $A(p_l(\sigma) G Q_{l,\sigma}) = p_l(\sigma) A(G Q_{l,\sigma})$. Sum over $(l, \sigma)$: $A(GF) = \Delta \cdot P$, that is, $P = \partial(GF)$.

If $F$ is homogeneous of degree $t + 1$, then $GF$ is homogeneous of degree $t + k$, so $A(GF)$ is homogeneous of degree $t + k$ and the quotient $P$ is homogeneous of degree $k$. Restriction to a block sends each variable to a variable or to $0$, so it keeps homogeneity: $P|_\tau$ is homogeneous of degree $k$.

Now restrict to block $\tau$. For $\sigma \ne \tau$ and $l \ge 1$, $p_l(\sigma)|_\tau = 0$. So $P|_\tau = \sum_l p_l \cdot R_{l,\tau}|_\tau$. Each $R_{l,\tau}|_\tau$ is symmetric in $X_0, \dots, X_{N-1}$, so $R_{l,\tau}|_\tau = \pi(T_l)$ for a polynomial $T_l$. Put $S = \sum_{l} X_{l-1} T_l$. Then $\pi(S) = P|_\tau$. The coefficient of $X_{k-1}$ in $X_{l-1} T_l$ is the constant term of $T_k$ if $l = k$ and $0$ otherwise. So $[X_{k-1}]S = T_k(0)$. The map $\pi$ and the restriction both keep constant terms, so $T_k(0) = R_{k,\tau}(0)$. By the first step, applied to $H = G Q_{k,\tau}$, we get $\int G Q_{k,\tau} = c\, R_{k,\tau}(0) = c\, [X_{k-1}] S$. $\square$

**Remark 4.1.7.** The hypothesis that $G$ is homogeneous of degree $k - 1$ is used only for the homogeneity of $P|_\tau$. The identity $\int G Q_{k,\tau} = c\,[X_{k-1}]S$ holds for every $G$.

**Remark 4.1.8 (Formalization).** The constant is $\int\Delta/(N!)^f$, and the proof is assembled from separate lemmas: divisibility of an alternating polynomial by $\Delta$, the decomposition of $A(GF)$, three homogeneity lemmas, the preimage under $\pi$, and the formula $\int H = c\,R(0)$ ([PLemmaA.lean](lean:GroundTheory/HeightsAndTheta/Heights/RemainderTerms/PLemmaA.lean#L1)). The flag integral is defined as the pairing with $\Delta$ above; no flag variety appears. In [Imports.lean](lean:GroundTheory/HeightsAndTheta/Heights/RemainderTerms/Imports.lean#L575), two facts of this section, that $\int$ kills $p_k(\tau) G$ for $1 \le k \le N$ and that $\partial(\Delta) = (N!)^f$, are proved by lemmas whose names end in `intersectionNumber_baseChange`. The names say nothing about the content.
