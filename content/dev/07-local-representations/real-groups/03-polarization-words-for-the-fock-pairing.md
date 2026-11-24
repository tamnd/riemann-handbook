---
title: Polarization words for the Fock pairing
decls:
  - Formalism.MainNotions.TestSideWords.operator_weight_bound_holds
  - Formalism.MainNotions.TestSideWords.onePos_of_OB
  - Formalism.MainNotions.TestSideWords.tenOp_of_OB
  - Formalism.MainNotions.TestSideWords.tensor_operators_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Polarization words for the Fock pairing

Let $s$ and $\beta$ be two vectors of a dual Weyl module, realised as polynomials on matrices. Multiply a test polynomial by $s$, pair the product with another test polynomial multiplied by $\beta$, and view the result as a bilinear form in the two test polynomials. This section proves that the form is given by a polynomial differential operator of a bounded order: a combination of words of length at most $c$ in the polarization operators $y_a\, \partial/\partial y_b$, where $c$ bounds the first entry of the highest weight. The result, for a tensor product of several blocks, is used in [Theorem 5.5.5 of Volume 11](/entry/stmt-e-of-mp/) of the volume on growth bounds, where the length of the words controls the growth of a twisted test vector.

Background: [polynomials on matrices](/learn/combinatorics/#polynomials-on-matrices), [highest weights and branching](/learn/representations/#highest-weights-and-branching).

### Words in polarization operators

Let $K$ be a field of characteristic $0$, let $k, d \geq 0$, and let $V_d$ be the space of homogeneous polynomials of degree $d$ in $y_0, \dots, y_{k-1}$ over $K$. For $a, b < k$ the *polarization operator* $E_{ab}$ on $V_d$ is $E_{ab} F = y_a\, \partial F / \partial y_b$. A *word of length $r$* is a product $E_{a_1 b_1} \cdots E_{a_r b_r}$; the empty word is the identity.

The operators $E_{ab}$ span a copy of $\mathfrak{gl}_k$ acting on $V_d = \mathrm{Sym}^d(K^k)$. An operator $A$ on $V_d$ has *weight* $\omega \in \mathbb{Z}^k$ if $[E_{aa}, A] = \omega_a A$ for every $a$. For example, $E_{ab}$ with $a \neq b$ has weight $e_a - e_b$, and a word of length $r$ has weight with all entries at most $r$. The next theorem is a converse: a $\mathfrak{gl}_k$-stable space of operators whose weights have entries at most $c$ consists of combinations of words of length at most $c$.

**Theorem 2.3.1 (Operator bound).** Let $K$ be a field of characteristic $0$ and $k, d, c \geq 0$. Let $W$ be a subspace of $\mathrm{End}_K(V_d)$ and $S \subseteq \mathrm{End}_K(V_d)$ a set with these properties: $W$ is the span of $S$; $[E_{ab}, A] \in W$ for all $A \in W$ and all $a, b$; and every $A \in S$ has a weight $\omega$ with $\omega_a \leq c$ for all $a$. Then every element of $W$ is a linear combination of words of length at most $c$.

Lean: `Formalism.MainNotions.TestSideWords.operator_weight_bound_holds` (also `operator_words_bound`).

*Proof.* We pass to symbols. Let $x_0, \dots, x_{k-1}, \xi_0, \dots, \xi_{k-1}$ be new variables and $t = \sum_i x_i \xi_i$. For an operator $A$ on $V_d$ put
$$\kappa(A) = \sum_{|g| = d} \frac{1}{g!}\, A(y^g)(x)\, \xi^g,$$
a polynomial of degree $d$ in $x$ and degree $d$ in $\xi$. The map $\kappa$ is injective. It turns composition with $E_{ab}$ on the left into $x_a\, \partial/\partial x_b$ and composition on the right into $\xi_b\, \partial/\partial \xi_a$, and $\kappa(1) = t^d / d!$. So $\kappa(W)$ is stable under the operators $x_a \partial_{x_b} - \xi_b \partial_{\xi_a}$, and a weight vector of weight $\omega$ has only monomials with $\deg_{x_a} - \deg_{\xi_a} = \omega_a$.

If $c < d$, every element of $\kappa(W)$ vanishes on the quadric $t = 0$. This is the main step, and it uses only the stability under the operators above and the bound $\omega_a \leq c < d$ on the weights. A bihomogeneous polynomial that vanishes on the quadric is divisible by $t$, and dividing by $t$ keeps the stability and the bound. Repeating, $\kappa(A) = t^{d - c} g$ with $g$ of bidegree $(c, c)$. Conversely, for $c \leq d$ every polynomial $t^{d-c} g$ with $g$ of bidegree $(c, c)$ is the symbol of a combination of words of length at most $c$; this follows from the two rules for $\kappa$ and $\kappa(1) = t^d/d!$. Injectivity of $\kappa$ gives the claim. If $c \geq d$, the same last step with $c$ replaced by $d$ shows that every operator is a combination of words of length at most $d \leq c$. $\square$

### One block

Fix $m \geq 1$ and let $x = (x_{ij})_{0 \leq i, j \leq m}$ be a square matrix of variables. On $K[x]$ we use the *Fock pairing without conjugation*,
$$(f, g) = \sum_\mu f_\mu\, g_\mu\, \mu!,$$
where $f_\mu$ is the coefficient of the monomial $x^\mu$ and $\mu! = \prod_{ij} \mu_{ij}!$. It is symmetric and bilinear over any field, and $x_{ij}$ is adjoint to $\partial / \partial x_{ij}$. Let $\nu \in \mathbb{N}^{m+1}$ be antitone. The *dual Weyl module* $\nabla(\nu)_K \subseteq K[x]$ is defined as in [the previous section](/entry/branching-interlacing-pairs/): the polynomials of degree $\nu_j$ in column $j$ that are invariant under adding $t$ times column $l$ to column $j$ for $l < j$.

**Definition 2.3.2 (The substitutions $\theta$).** For a sign $\mathrm{vec} \in \{\mathrm{true}, \mathrm{false}\}$, let $\theta_{\mathrm{vec}} : K[y_0, \dots, y_m] \to K[x]$ be the algebra map with
$$\theta_{\mathrm{true}}(y_c) = x_{c0}, \qquad \theta_{\mathrm{false}}(y_c) = \mathrm{adj}(x)_{mc},$$
where $\mathrm{adj}(x)$ is the adjugate matrix.

So $\theta_{\mathrm{true}}$ sends $y$ to the first column of $x$, and $\theta_{\mathrm{false}}$ sends $y$ to the last row of the adjugate, a row of cofactors. Both images transform under $\mathrm{GL}_{m+1}$ acting on the rows of $x$: the first as the standard representation, the second as its dual twisted by the determinant. The row operators $R_{ab} = \sum_t x_{at}\, \partial / \partial x_{bt}$ act on $K[x]$.

**Lemma 2.3.3 (Row operators).** Let $K$ be a field of characteristic $0$.

1. $(R_{ab} f, g) = (f, R_{ba} g)$ for all $f, g \in K[x]$, and $R_{ab}$ preserves $\nabla(\nu)_K$.
2. For $P$ homogeneous of degree $d$ in $y$: $R_{ab}\, \theta_{\mathrm{true}}(P) = \theta_{\mathrm{true}}(y_a \partial_b P)$ and $R_{ab}\, \theta_{\mathrm{false}}(P) = \theta_{\mathrm{false}}(d\, \delta_{ab} P - y_b \partial_a P)$.
3. $\nabla(\nu)_K$ is spanned by vectors $b$ with $R_{aa} b = \mu_a b$ for all $a$, where $\mu \in \mathbb{N}^{m+1}$ and $\mu_a \leq \nu_0$.
4. On $V_d$, the bilinear form $(P, Q) \mapsto (\theta_{\mathrm{vec}} P, \theta_{\mathrm{vec}} Q)$ is nondegenerate, and every linear form on $V_d$ is $Q \mapsto (\theta_{\mathrm{vec}} P, \theta_{\mathrm{vec}} Q)$ for some $P \in V_d$.

Lean: `Formalism.MainNotions.TestSideWords.letter_operators_holds` (part 2), `Formalism.MainNotions.TestSideWords.dual_weyl_weights_bounded` (part 3).

*Proof.* Part 1: the adjunction follows from that of $x_{ij}$ and $\partial / \partial x_{ij}$; the row operators commute with the column operations, so they preserve $\nabla(\nu)_K$. Part 2 is the chain rule: $R_{ab}$ moves row $b$ to row $a$, which for the first column is $y_b \mapsto y_a$, and for the cofactors of the last row gives the dual action plus the trace term $d\,\delta_{ab}$. Part 3: $\nabla(\nu)_K$ is spanned by bideterminants, products of minors on the first columns with rows in increasing order (the standard monomial theory of C. De Concini, D. Eisenbud and C. Procesi, Invent. Math. 56 (1980)). A product of minors is a weight vector for the $R_{aa}$, and there are $\nu_0$ minors, each using row $a$ at most once, so $\mu_a \leq \nu_0$. Part 4: $\theta_{\mathrm{vec}}$ maps $V_d$ injectively onto a dual Weyl module $\nabla(\nu')_K$, for a weight $\nu'$ that depends on $d$ and the sign; injectivity holds because composing $\theta_{\mathrm{vec}}$ with a suitable substitution multiplies $P$ by a nonzero power of a fixed polynomial (here $m \geq 1$ is used). The Fock pairing without conjugation is nondegenerate on every dual Weyl module. So the form is nondegenerate on the finite-dimensional space $V_d$, and every linear form is represented. $\square$

**Theorem 2.3.4 (Polarization words for one block).** Let $K$ be a field of characteristic $0$, $m \geq 1$, $\mathrm{vec}$ a sign, $d, c \geq 0$ and $\nu \in \mathbb{N}^{m+1}$ antitone with $\nu_0 \leq c$. Let $\beta, s \in \nabla(\nu)_K$. Then there are a finite set $L$ of words in letters $(a, b)$, each of length at most $c$, and scalars $a_l \in K$, such that for all $P, Q \in V_d$:
$$\big(\theta_{\mathrm{vec}}(P)\, s,\ \theta_{\mathrm{vec}}(Q)\, \beta\big) = \Big(\theta_{\mathrm{vec}}\Big(\sum_{l \in L} a_l\, E_l P\Big),\ \theta_{\mathrm{vec}}(Q)\Big),$$
where $E_l$ is the word of the letters of $l$.

Lean: `Formalism.MainNotions.TestSideWords.onePos_of_OB`.

*Proof.* By part 4 of the lemma, for $x, y \in \nabla(\nu)_K$ there is a unique operator $A(x, y)$ on $V_d$ with $(\theta P \cdot x, \theta Q \cdot y) = (\theta A(x,y) P, \theta Q)$ for all $P, Q$, and $A$ is bilinear. Let $W$ be the span of all $A(x, y)$ with $x, y \in \nabla(\nu)_K$. By parts 1 and 2, the commutator $[E_{ab}, A(x, y)]$ is a combination of $A(x, R y)$ and $A(R x, y)$ for row operators $R$: move $R_{ab}$ across the pairing and across the product with the Leibniz rule. So $W$ is stable under all $[E_{ab}, \cdot]$. Take the spanning set $S$ of all $A(b_i, b_j)$, where $(b_i)$ are the weight vectors of part 3, of weights $\mu^{(i)}$. Then $A(b_i, b_j)$ has weight $\mu^{(j)} - \mu^{(i)}$ when $\mathrm{vec}$ is true and $\mu^{(i)} - \mu^{(j)}$ when it is false. In both cases each entry is at most $\nu_0 \leq c$, since the $\mu$ have entries in $[0, \nu_0]$. Theorem (Operator bound) shows that $A(s, \beta)$ is a combination of words of length at most $c$. $\square$

### Several blocks

Let $n' \geq 0$ and consider $n'$ copies of the matrix variables, $x^{(t)}$ for $t < n'$, and $n'$ copies of the variables $y^{(t)}_0, \dots, y^{(t)}_m$. For $d \in \mathbb{N}^{n'}$ let $\mathrm{Pol}_d$ be the polynomials in all the $y^{(t)}$ of degree $d_t$ in the block $y^{(t)}$, for each $t$. For a sign vector $\mathrm{vec} \in \{\mathrm{true}, \mathrm{false}\}^{n'}$ let $\Theta_{\mathrm{vec}}$ be the substitution that applies $\theta_{\mathrm{vec}_t}$ in block $t$. For antitone $\nu_t \in \mathbb{N}^{m+1}$, the *tensor lattice* $\bigotimes_t \nabla(\nu_t)_K$ is the span of the products $\prod_t f_t(x^{(t)})$ with $f_t \in \nabla(\nu_t)_K$. A letter is now a triple $(t, a, b)$, acting by $y^{(t)}_a\, \partial / \partial y^{(t)}_b$.

**Theorem 2.3.5 (Polarization words for several blocks).** Let $K$ be a field of characteristic $0$, $n' \geq 0$, $m \geq 1$, $\mathrm{vec} \in \{\mathrm{true}, \mathrm{false}\}^{n'}$, $T$ a set of blocks, $d \in \mathbb{N}^{n'}$ and $c \geq 0$. Let $\nu_t \in \mathbb{N}^{m+1}$ be antitone for every $t$, with $(\nu_t)_0 \leq c$ for $t \in T$ and $\nu_t = 0$ for $t \notin T$. Let $\beta, s \in \bigotimes_t \nabla(\nu_t)_K$. Then there are a finite set $L$ of words and scalars $a_l$ such that: every letter of every word lies in a block of $T$; every word has at most $c$ letters in each block; and for every $G \in \mathrm{Pol}_d$, the polynomial $G' = \sum_{l \in L} a_l E_l G$ lies in $\mathrm{Pol}_d$ and
$$\big(\Theta_{\mathrm{vec}}(G)\, s,\ \Theta_{\mathrm{vec}}(H)\, \beta\big) = \big(\Theta_{\mathrm{vec}}(G'),\ \Theta_{\mathrm{vec}}(H)\big) \quad \text{for all } H \in \mathrm{Pol}_d.$$

Lean: `Formalism.MainNotions.TestSideWords.tensor_operators_holds` (also `tenOp_of_OB`, the same statement derived from Theorem (Operator bound)).

*Proof.* The Fock pairing is multiplicative across blocks of disjoint variables: $(\prod_t F_t, \prod_t G_t) = \prod_t (F_t, G_t)$. Both sides of the identity are linear in $s$, in $\beta$, in $G$ and in $H$, so it suffices to treat products $s = \prod_t s_t$, $\beta = \prod_t \beta_t$, $G = \prod_t G_t$ and $H = \prod_t H_t$. The pairing then factors into one pairing for each block. For $t \notin T$, $\nabla(0)_K$ is the constants and the factor needs no word. For $t \in T$, Theorem (Polarization words for one block) gives an operator $A_t$ of words of length at most $c$ in block $t$. The product of the operators $A_t$ for $t \in T$ is a combination of words with at most $c$ letters in each block of $T$; it preserves the multidegree, because every letter does. By bilinearity, the operator for general $s, \beta$ is a combination of these products. $\square$

**Remark 2.3.6 (Formalization).** The pairing used here, [FockR.lean](lean:Formalism/LocalToGlobal/GroupLattices/FockModels/TransposeWords/FockR.lean#L11), has no complex conjugation, unlike the normalised Fock pairing of the previous section. The theorem for several blocks is proved for a second copy of the definitions, in [FockRBlock.lean](lean:Formalism/PeriodIntegrals/FockRBlock.lean#L99), as an implication from the multiplicativity of the pairing and the one-block statement; the copies agree by definition. On the right side of each identity, $\beta$ and $s$ do not appear: they are absorbed into the scalars $a_l$, which depend on them. Two of the four declarations are implications whose hypothesis is Theorem (Operator bound), which is itself proved.
