---
title: Lattices with a symmetric pairing
decls:
  - Formalism.MainNotions.G.SymmetricFormBlocks.orthSplit_of_min
  - Formalism.MainNotions.G.SymmetricFormBlocks.orthBasisLat_of
  - Formalism.MainNotions.G.SymmetricFormBlocks.goodLeSmall_of
  - Formalism.MainNotions.G.SymmetricFormBlocks.orthLat_of'
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Lattices with a symmetric pairing

This section is about one lattice $L$ over $\mathbb{Z}_p$ with a pairing $B$ that is symmetric on $L$. We count how many pairs of vectors of $L$ are dual to each other up to the factor $p^D$ (the good count), and we prove that for $p \neq 2$ an orthogonal family of vectors of $L$ with small norms comes close to this count. The rest of the chapter applies this to lattices of polynomials, with $B$ built from the Fock pairing of Section 2. The orthogonal family theorem at the end of the section is the first input of the closed form of Theorem A in Section 7.

We use [lattices over discrete valuation rings](/learn/commutative-algebra/#regular-local-rings-and-discrete-valuation-rings) and [lattices with a symmetric form](/learn/hermitian-lattices/#lattices-in-quadratic-and-hermitian-spaces). Throughout, $p$ is a prime, $v_p$ is the $p$-adic valuation on $\mathbb{Q}_p$ (with the convention $v_p(0) = 0$), and $\sigma$ is a set of variables. All lattices live in the polynomial ring $\mathbb{Q}_p[\sigma]$.

**Definition 7.1.1 (Setting).** A *lattice setting* is a finite-dimensional $\mathbb{Q}_p$-subspace $W \subseteq \mathbb{Q}_p[\sigma]$, a finitely generated $\mathbb{Z}_p$-submodule $L \subseteq W$, and a map $B : \mathbb{Q}_p[\sigma] \times \mathbb{Q}_p[\sigma] \to \mathbb{Q}_p$ that is $\mathbb{Q}_p$-linear in the first variable, $B(cu, v) = c B(u, v)$ and $B(u + u', v) = B(u, v) + B(u', v)$, and symmetric on $L$: $B(u, v) = B(v, u)$ for $u, v \in L$.

We ask nothing of $B$ in the second variable. Symmetry on $L$ gives linearity in the second variable for vectors of $L$, and this is all that the proofs use. Since $L$ sits in the finite-dimensional space $W$, it is torsion free, so it is free of finite rank $\operatorname{rk} L$ over $\mathbb{Z}_p$.

**Definition 7.1.2 (Good count and bad count).** Let $B$ be a pairing on $L$ and $D \in \mathbb{Z}$. The *good count* $g(B, L, D)$ is the supremum of the integers $n$ for which there are $x_1, \dots, x_n, y_1, \dots, y_n \in L$ with
$$B(x_i, y_j) = p^D \delta_{ij} \quad \text{for all } i, j.$$
The *bad count* is $\operatorname{bad}(B, L, D) = \operatorname{rk} L - g(B, L, D)$, a difference of natural numbers truncated at $0$.

The $x_i$ are linearly independent over $\mathbb{Q}_p$ when $D$ is fixed, so $g \leq \operatorname{rk} L$ in the setting above, and the bad count measures how far $B$ is from being unimodular up to $p^D$. For example, let $L = \mathbb{Z}_p e_1 \oplus \mathbb{Z}_p e_2$ with $B(e_1, e_1) = 1$, $B(e_2, e_2) = p^3$ and $B(e_1, e_2) = 0$. For $D = 2$ the pair $x_1 = p^2 e_1$, $y_1 = e_1$ gives $g \geq 1$; the next result shows $g = 1$, so the bad count is $1$. For $D = 3$ both basis vectors can be used and the bad count is $0$.

**Theorem 7.1.3 (Minimal vector).** Let $p \neq 2$ and let $(W, L, B)$ be a lattice setting with $B(u, v) \neq 0$ for some $u, v \in L$. Then there is $x \in L$ with $B(x, x) \neq 0$ such that for every $u \in L$ there is $c \in \mathbb{Z}_p$ with $B(u, x) = c B(x, x)$.

*Proof.* This is the first step in the construction of a Jordan splitting of a lattice over a non-dyadic local field, see O'Meara, *Introduction to Quadratic Forms*, §91 and §92. We take it as given: it is supplied with the other inputs of [Theorem 5.11.3](/entry/theorem-a-closed-form-holds/). The argument is short. Choose $a, b \in L$ for which $|B(a, b)|_p$ is the largest value of $|B|_p$ on $L \times L$; it exists since $B$ takes the values $\sum_{k,l} c_k c_l B(f_k, f_l)$ on a finite basis $(f_k)$. If $|B(a, a)|_p$ or $|B(b, b)|_p$ equals this maximum, take $x = a$ or $x = b$. Otherwise $B(a + b, a + b) = 2 B(a, b) + B(a, a) + B(b, b)$ has the same absolute value as $2 B(a, b)$, which is $|B(a, b)|_p$ because $|2|_p = 1$. Take $x = a + b$. In each case $|B(u, x)|_p \leq |B(x, x)|_p$ for all $u$, which is the claim. $\square$

**Lemma 7.1.4 (Diagonal count).** Let $X, Y$ be $n \times m$ matrices over $\mathbb{Z}_p$, $c \in \mathbb{Q}_p^m$ and $D \in \mathbb{Z}$, with
$$\sum_{a=1}^{m} X_{ia} c_a Y_{ja} = p^D \delta_{ij} \quad (1 \leq i, j \leq n).$$
Then $n$ is at most the number of indices $a$ with $c_a \neq 0$ and $v_p(c_a) \leq D$.

*Proof.* We take this as given, as the second input of [Theorem 5.11.3](/entry/theorem-a-closed-form-holds/); here is the argument. Let $S$ be the set of indices $a$ with $c_a \neq 0$ and $v_p(c_a) \leq D$. For $a \notin S$ the number $p^{-D} c_a$ lies in $p \mathbb{Z}_p$. Divide the identity by $p^D$ and split the sum over $S$ and its complement:
$$X_S \operatorname{diag}(p^{-D} c_S) Y_S^{T} = I_n - pN,$$
with $N$ an $n \times n$ matrix over $\mathbb{Z}_p$. The determinant of $I_n - pN$ is $1$ modulo $p$, so it is not zero. The left side factors through $\mathbb{Q}_p^{S}$, so $n \leq |S|$. $\square$

**Proposition 7.1.5 (Orthogonal basis).** Let $p \neq 2$ and let $(W, L, B)$ be a lattice setting. Then $L$ has a $\mathbb{Z}_p$-basis $f_1, \dots, f_m$ with $B(f_a, f_b) = 0$ for $a \neq b$.

Lean: `Formalism.MainNotions.G.SymmetricFormBlocks.orthBasisLat_of` (also `Formalism.MainNotions.G.SymmetricFormBlocks.orthSplit_of_min`, the splitting step).

*Proof.* We argue by strong induction on $\operatorname{rk} L$. First, $L$ is free with a finite basis, because it is finitely generated and torsion free over the principal ideal domain $\mathbb{Z}_p$. If $B$ vanishes on $L \times L$, every basis works. Otherwise the Theorem (Minimal vector) gives $x \in L$. Put $L' = \{u - c_u x : u \in L\}$, where $c_u \in \mathbb{Z}_p$ is the unique element with $B(u, x) = c_u B(x, x)$. Then $L'$ is a submodule of $L$, $B(x, L') = 0$ by symmetry, $L = \mathbb{Z}_p x + L'$, and $cx + y = 0$ with $y \in L'$ forces $c = 0$ (pair with $x$). So $L = \mathbb{Z}_p x \oplus L'$ and $\operatorname{rk} L' < \operatorname{rk} L$. The induction hypothesis gives an orthogonal basis of $L'$, and adding $x$ gives one of $L$. $\square$

**Lemma 7.1.6 (Good count and an orthogonal basis).** Let $(W, L, B)$ be a lattice setting (any $p$), $D \in \mathbb{Z}$, and let $f_1, \dots, f_m$ be a $\mathbb{Z}_p$-basis of $L$ with $B(f_a, f_b) = 0$ for $a \neq b$. Then
$$g(B, L, D) \leq \#\{a : B(f_a, f_a) \neq 0,\ v_p(B(f_a, f_a)) \leq D\}.$$

Lean: `Formalism.MainNotions.G.SymmetricFormBlocks.goodLeSmall_of`.

*Proof.* Let $x_i, y_j \in L$ be as in the definition of the good count. Write $x_i = \sum_a X_{ia} f_a$ and $y_j = \sum_a Y_{ja} f_a$ with $X, Y$ over $\mathbb{Z}_p$. By linearity in the first variable, symmetry on $L$ and orthogonality, $B(x_i, y_j) = \sum_a X_{ia} B(f_a, f_a) Y_{ja}$. The Lemma (Diagonal count) with $c_a = B(f_a, f_a)$ bounds $n$. Every such $n$ is bounded by the same number, so the supremum is too. $\square$

**Theorem 7.1.7 (Orthogonal family).** Let $p \neq 2$, let $(W, L, B)$ be a lattice setting and $D \in \mathbb{Z}$. Then there are $n_1 \geq 0$ and vectors $e_1, \dots, e_{n_1} \in L$, linearly independent over $\mathbb{Z}_p$, such that $B(e_a, e_b) = 0$ for $a \neq b$, $B(e_a, e_a) \neq 0$ and $v_p(B(e_a, e_a)) \leq D$ for all $a$, and
$$n_1 \leq \operatorname{rk} L \leq n_1 + \operatorname{bad}(B, L, D).$$

Lean: `Formalism.MainNotions.G.SymmetricFormBlocks.orthLat_of'`.

*Proof.* Take the orthogonal basis $f_1, \dots, f_m$ of the Proposition (Orthogonal basis), and let $e_1, \dots, e_{n_1}$ be the $f_a$ with $B(f_a, f_a) \neq 0$ and $v_p(B(f_a, f_a)) \leq D$. They are part of a basis, so they are independent, and $n_1 \leq m = \operatorname{rk} L$. The previous lemma gives $g(B, L, D) \leq n_1$, so $\operatorname{rk} L = g + \operatorname{bad} \leq n_1 + \operatorname{bad}$. $\square$

The theorem says that, up to the bad count, the good count is realized by a diagonal family. In the later sections the bad count is the quantity to bound, and an orthogonal family of this kind is what the window counts of Section 7 take as input.

**Remark 7.1.8 (Formalization).** The minimal vector theorem (`OrthMin`) and the diagonal count (`GoodLeSmallMat`) are hypotheses of the theorems of this chapter. They are supplied by `PI.exists_minimalNormVector` and `diagonal_rank_bound` in the proof of `theorem_A_closed_form_holds`; we did not open those proofs, and the arguments above are ours. The freeness step `freeLat_proved` ([OrthBasisLatOf.lean](lean:Formalism/SharpRestriction/GrowthBounds/MonomialFactorials/OrthBasisLatOf.lean#L28)) is closed by a tactic that tries six alternatives in turn. The splitting `orthSplit_of_min` combines `OrthMin` with the rank drop `splitRank_proved`. The count step goes through `orthCount_of` and `orthLat_of`. `GoodLeSmall` does not ask for $p \neq 2$, while the orthogonal basis and the orthogonal family theorem do.
