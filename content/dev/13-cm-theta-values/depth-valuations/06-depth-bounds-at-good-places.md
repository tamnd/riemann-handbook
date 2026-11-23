---
title: Depth bounds at good places
decls:
  - GlobalTheory.GoodDepth.nuGood
  - GlobalTheory.T.goodPlaceDepthBound_proof
  - GlobalTheory.GoodDepth.leafGood
  - GlobalTheory.T.depthTable_goodPrimeLeaf
  - GlobalTheory.GoodDepth.leafGood_run
  - GlobalTheory.T.depthLeaf_goodPrimes_of_point_data
  - GlobalTheory.leafDepthGood_of_chartForm
  - GlobalTheory.T.depthTable_goodPrimes_of_chartForm
  - GlobalTheory.RunDepth.leafDepth_all_run
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Depth bounds at good places

This section bounds the depth of a unitary moduli space at a place of good residue characteristic $\ell$, using the packages of the previous section. The bound has a main term, the content $F_j(\ell)$ of a numerical datum, and an error that decays in $\ell$. It vanishes when $\ell$ is larger than the total weight. We then transfer the bound to the normalized depths of a leaf object, and we add the bounds at the bad places. The result is the four depth bounds of a leaf object. They are used in the [depth bounds for the leaves of a record](/entry/leaf-depth-all-record/) in Volume 15, and through it in Branch 2 of [the unitary hypotheses](/proof/unitary-hypotheses/).

### The depth at a place

Let $X$ be a unitary moduli space over a CM field $E$, with level of modulus $M$ and coefficient field $F$. For a place $\lambda$ of $F$ over a prime $\ell$ let $e_\lambda$ be its ramification index. Fix a weight $a$ and an integer $n_W$.

**Definition 4.6.1.** The *depth* of $X$ at $\lambda$ is
$$\nu_W(\lambda) = \max\Big(0, \sup_{T, y} \inf_{C} \nu_C\Big),$$
where $T$ runs over the complete discrete valuation rings over $\lambda$, $y$ over the algebraic integral points of $X$ over $T$, $C$ over the integral charts at $y$, and $\nu_C$ is the local depth of $C$ of the previous section.

For integers $k$ and primes $\ell$ put $\theta(k, \ell) = \sup \ell^{-i}$, over the odd $i \geq 3$ with $\ell^i > k^{3/2}$. A numerical datum $N$ has ranks $k, m$, a number $f$ of places, sizes $S_c$ and $\eta$, weights $w_j$ and a content $F_j(\ell)$. Its total weight is $D_F$. A *good page* with constant $C_1$ is a list of inequalities between $a$, $n_W$, an integer $T$, real numbers $b, L$ and the ranks of $N$. We say that $\ell$ is *good* for $N$ if it is not one of the bad primes $q, d, g_0, g_1$ of the datum, does not lie in the set $s_m$ of small primes, and does not divide $M$.

**Theorem 4.6.2 (depth at a good place).** For each $C_1 \geq 0$ there is $C_c > 0$ with the following property. Assume that the involution of $\mathcal{O}_E$ is complex conjugation, that every algebraic integral point of $X$ has an integral chart, and that the package statement holds for $X$. Let $N$ be a numerical datum, let $1 \leq j \leq m$, and let $a, n_W, T, b, L, w$ form a good page with constant $C_1$, with an embedding datum tied to $N$, the signature of $N$, $\sum_z w_j(z) \leq w$ and $b \leq w$. Let $\lambda$ lie over a good prime $\ell$. Then $\nu_W(\lambda)$ is finite,
$$\begin{aligned}
\frac{T \nu_W(\lambda)}{e_\lambda} \leq F_j(\ell) + C_c \Big( &\frac{m w \log k}{\ell} + \frac{f k (S_c + \eta)}{\ell} \\
&+ k\,\theta(k, \ell)\, w + [\ell > X'']\, \frac{k w}{\ell^2} \Big),
\end{aligned}$$
and $\nu_W(\lambda) = 0$ if $D_F < \ell$. Here $X''$ is a threshold of $N$ and $[\ell > X'']$ is $1$ or $0$.

Lean: `GlobalTheory.T.goodPlaceDepthBound_proof` (also `GlobalTheory.GoodDepth.nuGood`, a second name).

*Proof.* Let $B$ be the right side. It is enough to show $\nu \leq B / T$ for every good point and every $\nu$ with $e_\lambda \nu \leq \nu_C$ for the chart $C$, since $\nu_W(\lambda)$ is built from such $\nu$. The package statement gives a package with this $T$ and $\nu$. Its kind depends on the class of $\ell$ for $N$.

Case 1 (zero packages). Assume $\ell \geq m b / (T f (k - 1)^3 L)$. If $b \geq 0$, the size bounds of the datum and the good page give $s$ with $a(\tau, 0) \leq s(\ell - 1)$ for each $\tau$ of positive multiplicity. If $b < 0$, the good page gives $T a(\tau, 0) \leq 3 b < 0$, so there is no such $\tau$ and $s = 0$ works. So a zero package exists, and the valuation of a zero package is at most $0$. So $\nu \leq 0 \leq B / T$.

Case 2 (small $\ell$). Now $\ell$ is inert or split for $N$. The content bound gives the main term of each inert case as at most $F_j(\ell) + 2 [\ell > X''] k w / \ell^2$. There are four subcases. If Frobenius acts as complex conjugation, we use the package of the previous section. If $\ell$ is in the conjugate class only, or inert in another way, or split, we use the corresponding package. In each subcase the depth content bound gives $T \nu$ at most a main term plus a constant times an error term. The size bounds give $T f (k - 1)^3 \log^2 k \leq m w \log k / \ell$, so this error term is at most twice the error in the statement. We take $C_c = 2 C_I + 2 C_P + 2 C_C + C_S + 2$, where $C_I, C_P, C_C, C_S$ are the constants of the four subcases.

Case 3 (vanishing). If $D_F < \ell$, then $a(\tau, 0) \leq D_F \leq \ell - 1$, and Case 1 with $s = 1$ gives $\nu \leq 0$ for every good point. So $\nu_W(\lambda) = 0$. $\square$

### Leaf objects

A *leaf object* $O$ over a number field $K$ with an involution has a finite set $T_w$ of finite places, an index set $J$, real constants $C, k, m, f, T, Y, b, b'$, weights $\theta(l), a(l) \geq 0$ on primes, and bad primes $g_1, g_2, q_1, d$ and a finite set $s_m$. At each place $w$ and index $j$ it has an exponent $E(w, j)$ and an element $\sigma(w, j)$. For a place $w$ let $\ell(w)$ be its residue characteristic and $\bar w$ the conjugate place. The *normalized depth* is
$$e_0(w, j) = \frac{E(w, j) - v_w(\sigma(w, j))}{e_w}, \qquad e_w = v_w(\ell(w)).$$
Let $N$ be a numerical datum with contents $F_0(w, j)$, and put
$$a_E(j, \ell) = \frac{A_1(j)}{\ell} + A_{kw}(j)\, \theta(\ell) + T a(\ell) + [\ell > X_2]\, \frac{A_{kw}(j)}{\ell^2}$$
for constants $A_1(j)$, $A_{kw}(j)$ and $X_2$ of $O$.

**Definition 4.6.3.** The *good-place bound* for $N$ and $O$ holds if $\theta \geq 0$ and $a \geq 0$; for every finite set $Q$ of primes $\sum_{p \in Q} \theta(p) \log p \leq C / k$ and $T \sum_{p \in Q} a(p) \log p \leq C m b$; and for each $w \in T_w$ whose residue characteristic $\ell$ is not bad, and each $j$, the following holds. If $\ell \leq Y$, then $e_0(w, j)$ and $e_0(\bar w, j)$ are at most $F_0(w, j) + a_E(j, \ell) + 1$. If $\ell > Y$, then $e_0(w, j) = e_0(\bar w, j) = 0 \leq F_0(w, j)$.

The objects $O$ in this section come from *depth data*: the exponents $E(w, j)$ are rounded depths $\nu_W$ of moduli spaces $X_{\iota(j)}$ at the places below $w$, for a map $\iota : J \to \mathbb{N}$.

**Theorem 4.6.4 (good-place bound from depth data).** For each $C_1 \geq 0$ there is $C_0$ with the following property. Let $O$ be a leaf object whose exponents and elements are built from depth data $D$ with moduli spaces $X_i$, and whose bad primes are those of $D$ and of $N$. Assume $C_0 \leq C$, that $g_1 g_2 = M$ with $\pi_i \bar\pi_i = g_{i+1}$, that the involution is complex conjugation, and, for each $j$, that every algebraic integral point of $X_{\iota(j)}$ has an integral chart, that the package statement holds for $X_{\iota(j)}$, and that there is a good page with constant $C_1$. Assume that the constants of $O$ match those of $N$, with $a = 0$ and with $T$ equal to the integer $T_D$ of $D$, and that $F_0$ is the content of $N$. Then the good-place bound holds for $N$ and $O$.

Lean: `GlobalTheory.T.depthTable_goodPrimeLeaf` (also `GlobalTheory.GoodDepth.leafGood`, a second name).

*Proof.* Let $C_c$ be the constant of the theorem on the depth at a good place for $C_1$, and put $C_0 = \max(C_c, 20)$.

The weights. Each $\theta(l)$ is a supremum of positive numbers, so $\theta \geq 0$, and $a = 0$. So the sum with $a$ vanishes, and a bound for the tail of a prime sum gives $\sum_{p \in Q} \theta(p) \log p \leq 20 / k \leq C / k$.

The good places. Let $w$ be a place with good residue characteristic $\ell$, let $v$ be $w$ or $\bar w$, and let $\lambda$ be the place of $F$ below $v$. The exponent is a rounded depth, so $e_0(v, j) \leq T_D \nu_W(\lambda) / e_\lambda + 1$, and $e_0(v, j) = 0$ if $\nu_W(\lambda) = 0$. Since $M = g_1 g_2$ and $\ell$ is neither $g_1$ nor $g_2$, $\ell \nmid M$. So the depth bound applies and gives $T_D \nu_W(\lambda) / e_\lambda \leq F_0(w, j) + C_c\, \mathrm{err}(\ell)$, where $\mathrm{err}(\ell)$ is its error term. Since $C_c \leq C$, a monotonicity argument gives $C_c\, \mathrm{err}(\ell) \leq a_E(j, \ell)$.

Large $\ell$. The ties give $D_F \leq Y$. If $\ell > Y$, then $D_F < \ell$, so $\nu_W(\lambda) = 0$ and $e_0 = 0$. The content satisfies $F_0(w, j) \geq 0$ at good primes. $\square$

**Corollary 4.6.5 (good-place bound for a run).** There is $C_0$ such that the following holds. Let $D$ be a datum with a core $T$ that satisfies the laws of the run, and let $O$, $N$ and $\iota$ be tied to $D$. Assume that the package statement holds for every $X_{\iota(j)}$ of the core, that $C_0 \leq C$, that the leaf object has its page and size conditions, and that $10 \leq C_{n_W}$, $3 \leq x^{e_z / 5}$, $x \geq 3$, $k b' \leq b$ and $F_0$ is the content of $D$. Then the good-place bound holds for $N$ and $O$.

Lean: `GlobalTheory.T.depthLeaf_goodPrimes_of_point_data` (also `GlobalTheory.GoodDepth.leafGood_run`, a second name).

*Proof.* Take $C_0$ from the theorem with $C_1 = 100$. Apply it to the field, host, level, data and moduli spaces of the core, to the depth data of the core, to the numerical datum of $D$, and to the map of places to embeddings given by the CM type of $D$. We check the hypotheses. The depths, the constants and the bad primes of $O$ come from the tie with $D$. The relations $\pi_i \bar\pi_i = g_{i+1}$ and $M = g_1 g_2$ hold for the depth data of a datum. Integral charts exist at integral points. The real places match the CM type and its Frobenius. For each $j$, the index lies in $[1, m]$, the signature comes from the core, the weight is dominant, and the good page comes from the depth parameters, with $\log k \leq L$ from the size conditions. Finally, $S_c + \eta$ is at most the size of $O$, $\sum_z w_j(z) \leq 2 f b$ by the bounds on the first rows, and $D_F \leq Y$ by the degree of the weight exponents. $\square$

**Theorem 4.6.6 (good-place bound from the character statement).** Assume the character statement at every prime. Then there is $C_0$ such that the conclusion of the corollary holds without the hypothesis on packages.

Lean: `GlobalTheory.T.depthTable_goodPrimes_of_chartForm` (also `GlobalTheory.leafDepthGood_of_chartForm`, a second name).

*Proof.* Take $C_0$ from the corollary. For each $j$, the [theorem on packages at good primes](/entry/all-good-prime-depth-data-exist-proof/) applied to $X_{\iota(j)}$ and its coefficient field gives the package statement. The corollary applies. $\square$

### All places of a leaf

The bad places need three local statements on formal groups. The character statement is the one of the previous section. The *height statement* at $p$ says that the linear terms of finitely many characters of a formal group with a chart span the tangent module up to a factor $c$ with $|c|^{p - 1} \leq |p|$. The *abelian statement* at $p$ bounds the cokernel of the character map on eigenspaces of an order, like the character statement.

**Theorem 4.6.7 (depth bounds at a leaf).** Assume the abelian, height and character statements at every prime. Then there is $C_0$ such that, under the hypotheses of the corollary without the package hypothesis, the following four bounds hold.
1. The good-place bound holds for $N$ and $O$.
2. If $\ell(w) \in \{q_1, d\}$, then $e_0(w, j)$ and $e_0(\bar w, j)$ are at most $s_B(j) + T + 1$. Also $F_0(w, j) = 0$ if $\ell(w) = q_1$, and $-2 f k b' \leq F_0(w, j) \leq 0$ if $\ell(w) = d$.
3. If $\ell(w) \in s_m$, then both depths are at most $s_C(j) + T + 1$, and $F_0(w, j) = 0$.
4. If $\ell(w) \in \{g_1, g_2\}$, then $e_0(w, j) \leq 2T - n(w, j)$, $e_0(\bar w, j) \leq 2T - n(\bar w, j)$, and $n(w, j) + n(\bar w, j) = -2 F_0(w, j)$.

Here $s_B$, $s_C$ and $n$ are constants of $O$.

Lean: `GlobalTheory.RunDepth.leafDepth_all_run`.

*Proof.* Part 1 and the constant $C_0$ come from the previous theorem, which uses only the character statement. Parts 2, 3 and 4 are the bounds at the ramified places, at the small primes and at the level primes. They have separate proofs, which we do not repeat here. Only part 3 uses the abelian and height statements. Parts 2 and 4 use no statement on formal groups. $\square$

**Remark 4.6.8 (Formalization).** All second names here are proved by `first | exact @…` under `maxHeartbeats 1000000`. The words "depth table" in two names match no defined object. The depth bound does not use the zero statement for primes where Frobenius acts as complex conjugation ([GoodPlaceDepthBoundProof.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/GoodPlaceDepthBoundProof.lean#L56)). In the theorem from depth data the hypothesis $T = T_D$ is not used, because $a = 0$.
