---
title: A one-coset lemma for an unfolding over a finite field
decls:
  - Formalism.L2.Col.residueFieldUnfolding_claims_hold
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A one-coset lemma for an unfolding over a finite field

At a prime of depth one, the local unfolding integrals of the column argument reduce to finite sums over the residue field: a test function on rectangular matrices, built from an additive character and determinants of diagonal blocks, is integrated against a character over a unipotent group of free coordinates. This section proves two facts about that finite sum. First, the unfolded sum of a left translate by $h$ vanishes unless $h$ lies in one explicit double coset, the product of a flag unipotent group and a set of matrices with a fixed support pattern. Second, the unfolded sum of the untranslated function is not zero. Both are used in the step [the nonemptiness hypotheses](/step/nonempty-hyps/), where the first reduces a sum over a group to a single coset and the second shows that the surviving term is nonzero.

Background: [smooth representations of $p$-adic groups](/learn/representations/#smooth-representations-of-p-adic-groups), [minors and determinant identities](/learn/combinatorics/#minors-and-determinant-identities).

### The data

Throughout, $k$ is a finite field, $\psi_0 : k \to \mathbb{C}^\times$ an additive character and $\chi_0, \chi_1, \dots$ multiplicative characters of $k^\times$, each extended to $k$ by $\chi_i(0) = 0$. Indices of rows and columns start at $0$. Fix integers $k_0, m, t, j, n', c, n \geq 0$ with
$$\begin{aligned} &k_0 \geq 1, \quad m \text{ even}, \quad m \geq 4, \quad 1 \leq j \leq m - 2, \quad c = m - 1 - j, \\ &n' + c + 1 = r + (j - 1) t, \quad n + c = r + j t, \quad \text{where } r = k_0 + m - 1. \end{aligned}$$
Put $A = n' + c + 1$ and $B = n + c$. The objects below are functions on the space of $B \times A$ matrices over $k$, which we view as linear maps $k^A \to k^B$.

**Definition 2.9.1 (Reindexing).** For integers $c, n$ let $f_{c,n}(s) = s$ if $s < k_0$, $f_{c,n}(s) = n + (s - k_0)$ if $k_0 \leq s < k_0 + c$, and $f_{c,n}(s) = s - c$ otherwise. On $\{0, \dots, n + c - 1\}$ this is the permutation that moves the last $c$ positions into the slots $k_0, \dots, k_0 + c - 1$. For a $B \times A$ matrix $x$ let $M(x)$ be the matrix with entries $M(x)_{p, p'} = x_{f_{c,n}(p),\, f_{c+1,n'}(p')}$.

**Definition 2.9.2 (Allowed positions).** For a bound $N$, the position $(p, p')$ with $p \neq p'$ is *allowed* when:
1. $p' < k_0$, and $p < p'$ or $k_0 \leq p < k_0 + m/2 - 1$;
2. $k_0 \leq p' < r$, and $k_0 \leq p < p'$, or $p' + 1 - k_0 > m/2$ and $p < k_0$;
3. $p' \geq r$, and $p < r$, or $p < N$ and $\lfloor (p - r)/t \rfloor \leq \lfloor (p' - r)/t \rfloor$.

So on the first $r$ indices the allowed positions are strictly upper triangular for an order that puts the block $[k_0, k_0 + m/2 - 1)$ first, then $[0, k_0)$, then the rest; beyond $r$ the pattern is block upper triangular with blocks of length $t$.

**Definition 2.9.3 (The test function).** Let $a = r + (j - 1) t = A$. For a $B \times A$ matrix $x$ with $M = M(x)$, put $\Phi(x) = 0$ unless $M_{p', p'} = 1$ for all $p' < r$ and every nonzero off-diagonal entry $M_{p, p'}$ with $p < B$ and $p' < a$ sits at an allowed position for the bound $a$. Otherwise
$$\Phi(x) = \psi_0\Bigl(\sum_{i < r - 1} M_{i, i+1}\Bigr) \prod_{i < j - 1} \chi_i\bigl(\det M^{(i)}\bigr) \cdot \chi_{j-1}\bigl(\det M_{[0,a) \times [0,a)}\bigr)^{-1},$$
where $M^{(i)}$ is the $t \times t$ diagonal block of $M$ on the indices $r + i t, \dots, r + (i + 1) t - 1$, and the inverse of $0$ is read as $0$.

**Definition 2.9.4 (The unfolded sum).** Call a position $(l, s)$ of a $B \times A$ matrix *free* if $s \geq n'$ and either $s - n' = c$, or $s - n' \geq 1$ and ($l < n$ or $l - n < s - n'$). For an $n \times n'$ matrix $x_j$ and a vector $\tau$ of values indexed by the free positions, let $X(x_j, \tau)$ be the $B \times A$ matrix whose free entries are given by $\tau$, whose first $n'$ columns are $x_j$ on top of a zero block, and whose other entries in column $s \geq n'$ are $1$ in row $n + (s - n')$ and $0$ elsewhere. Then
$$E(\Phi)(x_j) = \sum_{\tau} \Phi\bigl(X(x_j, \tau)\bigr)\, \psi_0\Bigl(-\sum_{i < c} X(x_j, \tau)_{n + i,\, n' + i + 1}\Bigr),$$
the sum over all $\tau$ with values in $k$. This is the finite-field form of an integral over a unipotent group against a generic character. For $h \in GL_B(k)$, write $(h \cdot \Phi)(x) = \Phi(h^{-1} x)$.

**Definition 2.9.5 (The two groups).** Let $U_i \subseteq k^B$ be the span of the first $n + i$ basis vectors $e_0, \dots, e_{n+i-1}$. Let $R_1$ be the set of $\rho \in GL_B(k)$ such that $\rho$ and $\rho^{-1}$ map each $U_i$ into itself, fix $e_n$, and move each $e_{n+i}$ by an element of $U_i$; this is a subgroup. Let $\mathcal{K}$ be the set of $\kappa \in GL_B(k)$ such that $M = M(\kappa)$, formed with $f_{c,n}$ on both sides, has $M_{p', p'} = 1$ for $p' < r$ and has every nonzero off-diagonal entry at an allowed position for the bound $B$.

### The statement

**Theorem 2.9.6 (One coset).** With the data above:
1. if $E(h \cdot \Phi)(x_j) \neq 0$ for some $h \in GL_B(k)$ and some $x_j$, then $h = \rho \kappa$ with $\rho \in R_1$ and $\kappa \in \mathcal{K}$;
2. there is an $x_j$ with $E(\Phi)(x_j) \neq 0$.

Lean: `Formalism.L2.Col.residueFieldUnfolding_claims_hold`.

The Lean statement also assumes that $\psi_0$ is not the trivial character, but the proof never uses this assumption. Part 2 holds for every $\psi_0$: the proof below shows that $E(\Phi)(x_j^0)$ is a positive integer for an explicit $x_j^0$.

### The proof

The first part rests on four lemmas.

**Lemma 2.9.7 (Pattern closure).** $\mathcal{K}$ is closed under products and inverses.

*Proof.* Let $S$ be the relation "$p = q$ or $(p, q)$ is allowed". On indices below $r$, an allowed pair $(p, q)$ strictly increases the weight $\varphi(p)$ that is $m + p$ for $p < k_0$, $p - k_0$ for $k_0 \leq p < k_0 + m/2 - 1$, and $p + 2m + k_0$ otherwise. Hence $S$ is transitive and, on these indices, antisymmetric. Matrices with nonzero entries only on $S$ then form an algebra that contains the inverses of its invertible elements, and the diagonal entries below $r$ of a product are the products of the diagonal entries. After the permutation $f_{c,n}$ these are exactly the conditions defining $\mathcal{K}$. $\square$

**Lemma 2.9.8 (Support of the test function).** If $\Phi(y) \neq 0$, there is $\kappa \in \mathcal{K}$ whose column $f_{c,n}(p)$ equals the column $f_{c+1,n'}(p)$ of $y$ for every $p < A$.

*Proof.* The nonvanishing of $\Phi(y)$ says that the reindexed $y$ has unit diagonal below $r$ and allowed support in its $A$ columns. Complete it by the basis vectors in the remaining $B - A$ columns. An allowed position $(p, p')$ with $p' < a$ has $p < a$, so after reindexing the completed matrix is block diagonal, with the leading $A \times A$ block of $M(y)$ and an identity block. It is invertible: $\Phi(y) \neq 0$ forces $\chi_{j-1}(\det M_{[0,a) \times [0,a)})^{-1} \neq 0$, so this determinant is not $0$. Allowed for the bound $a$ implies allowed for the bound $B$, so the completed matrix lies in $\mathcal{K}$. $\square$

**Lemma 2.9.9 (The unipotent coordinates).** For every $x_j$ and $\tau$ there is $\nu \in R_1$ that fixes the first $n$ basis vectors and maps $e_{n+i}$ to column $n' + i$ of $X(x_j, \tau)$ for each $i < c$.

*Proof.* By the definition of the free positions, column $n' + i$ of $X(x_j, \tau)$ is $e_{n+i}$ plus a vector in $U_i$. Take $\nu$ with these columns and the identity elsewhere. $\square$

**Lemma 2.9.10 (Factoring).** Let $g \in GL_B(k)$ fix $e_{n+i}$ for $i < c$, and map $e_{f_{c,n}(p)}$ into $U_0$ for each $p < A$ with $p < k_0$ or $p > k_0 + c$. Then $g = \gamma \kappa$ with $\gamma \in R_1$ and $\kappa \in \mathcal{K}$.

*Proof.* Let $X$ be the projection onto the first $n$ coordinates and $Y = 1 - X$. Put $\beta = Y g X$, so $\beta^2 = 0$, and let $\kappa = 1 + \beta$, with inverse $1 - \beta$. After reindexing, the rows of $\beta$ that can be nonzero are $k_0, \dots, k_0 + c - 1$, and by the hypotheses on $g$ its nonzero columns are among $k_0 + c$ and the indices $\geq A$. These positions are allowed (by the second and third cases, since $k_0 + c < r$), so $\kappa \in \mathcal{K}$. The element $\gamma = g \kappa^{-1}$ fixes each $e_{n+i}$ and maps $U_0$ into itself, so it lies in $R_1$. $\square$

*Proof of the theorem.* Part 1. Suppose $E(h \cdot \Phi)(x_j) \neq 0$. Some term of the sum is nonzero: there is $\tau$ with $\Phi(h^{-1} X) \neq 0$, where $X = X(x_j, \tau)$. By the support lemma there is $\kappa \in \mathcal{K}$ whose columns $f_{c,n}(p)$ agree with the columns $f_{c+1,n'}(p)$ of $h^{-1} X$. Take $\nu$ from the lemma on unipotent coordinates and put $g = \nu^{-1} h \kappa$. For $i < c$, the index $p = k_0 + i$ gives $h \kappa e_{n+i} = X e_{n'+i} = \nu e_{n+i}$, so $g$ fixes $e_{n+i}$. For $p < k_0$ or $p > k_0 + c$, the column $f_{c+1,n'}(p)$ of $X$ lies among the first $n'$ columns, so it lies in $U_0$, and $\nu^{-1}$ maps $U_0$ to itself identically; hence $g e_{f_{c,n}(p)} \in U_0$. The factoring lemma gives $g = \gamma \kappa'$, and
$$h = \nu g \kappa^{-1} = (\nu \gamma)(\kappa' \kappa^{-1}),$$
with $\nu \gamma \in R_1$ and $\kappa' \kappa^{-1} \in \mathcal{K}$ by pattern closure.

Part 2. Let $x_j^0$ be the $n \times n'$ matrix with a $1$ in position $(s, s)$ for $s < k_0$, a $1$ in position $(s + 1, s)$ for $s \geq k_0$, and $0$ elsewhere: it skips row $k_0$. For every $\tau$, the term of $E(\Phi)(x_j^0)$ at $\tau$ is $1$ or $0$. When the support condition holds, the diagonal blocks $M^{(i)}$ and the leading block have determinant $1$, so the characters give $1$, and the superdiagonal sum in $\psi_0$ is exactly the sum $\sum_{i < c} X_{n+i,\, n'+i+1}$, so the two values of $\psi_0$ cancel. Hence $E(\Phi)(x_j^0)$ is the number of $\tau$ for which the support condition holds. This number is at least $1$: take $\tau^0$ equal to $1$ at the position (row $k_0$, column $n' + c$) and $0$ at the other free positions. Then the reindexed matrix is the identity on its first $A$ columns, and the support condition holds. $\square$

**Remark 2.9.11 (Formalization).** The five definitions behind the statement, from the character extended by zero to the pattern set, are written twice with identical bodies: once in [ChainOneB.lean](lean:Formalism/LocalToGlobal/Columns/ChainOneB.lean#L16) and once in [OneCosetSharp.lean](lean:Formalism/PeriodIntegrals/OneCosetSharp.lean#L152), and the theorem is the second copy restated through the first. The unfolded sum in Lean also carries a weight, a set of values and a translation by a pair of group elements with a character and a valuation; here they are $1$, all of $k$, and the translation by $h$ alone. Floor division by $t = 0$ is read as $0$; the case $t = 0$ is allowed, and then $A = B = r$ and there are no indices beyond $r$.
