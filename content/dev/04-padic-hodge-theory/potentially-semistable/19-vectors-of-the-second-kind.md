---
title: Frobenius vectors with zero residues
decls:
  - GlobalTheory.T.exists_nonzero_frobVector_residue_zero
  - GlobalTheory.PMonII.exII
  - GlobalTheory.T.existsNonzeroFrobVectorResidueZero_proof
  - GlobalTheory.PMon.exII_holds
  - GlobalTheory.T.exists_secondKind_matrix_moore_det_ne_zero
  - GlobalTheory.SecondKind.exists_secondKind
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Frobenius vectors with zero residues

Let $\lambda_0, \dots, \lambda_{h-1}$ be elements of $\mathrm{Fil}^0$ that are linearly independent over $\mathbb{Q}_\ell$ modulo $\mathrm{Fil}^1$. This section constructs eigenvectors $a_0, \dots, a_{h-1}$ of $\varphi^h$ in $B^+$, with eigenvalue $\ell$, such that $\sum_j \lambda_j\, \iota(\varphi^i a_j) \in \mathrm{Fil}^1$ for $i < h$. First we find such a family that is not zero, from [the residue zeros](/entry/exists-orthogonal-family-residue-zeros/). Then we show that the Moore matrix of the family is invertible. These are the vectors of the second kind. They are used in [the lattice lemma in degree one](/entry/fundamental-lemma-lattice-degree-one/).

We keep the notation of [the section on Moore determinants](/entry/cris-plus-frob-eigenvector-ratio-padic/): the ring $B$ with Frobenius $\varphi$, the injective map $\iota : B \to B_{\mathrm{dR}}$, the filtration $\mathrm{Fil}^\bullet$, the element $t = \iota(t_B)$, the set $B^+$ of positive elements and the Moore matrix $M(a)$. For $j \geq 0$ and $x \in B$ put
$$\iota_j(x) = \iota(\varphi^j x).$$
Each $\iota_j$ is a ring homomorphism and is $\mathbb{Q}_\ell$-linear. We also keep the residue series $A_{h,j}$ of [the previous section](/entry/core-orth-core/).

We use the following facts, proved elsewhere in this development.

1. (Residues.) There is a ring homomorphism $\theta : \mathrm{Fil}^0 \to \mathbb{C}_\ell$ with kernel $\mathrm{Fil}^1$ and with $\theta(c) = c$ for $c \in \mathbb{Q}_\ell$. For every $h \geq 2$, every real $r < 1$ and every sequence $y = (y_k)_{k \geq 0}$ in $\mathcal{O}_C^\flat$ with $|y_k^\sharp| \leq r$ for all $k$, there is $b \in B^+$ with $\varphi^h(b) = \ell\, b$ and $\theta(\iota_j(b)) = A_{h,j}(y)$ for all $j \geq 0$.
2. (Orthogonal bases.) Let $\mu \in \mathbb{C}_\ell^h$ be linearly independent over $\mathbb{Q}_\ell$. Then there is a matrix $P \in M_h(\mathbb{Q}_\ell)$ with $\det P \neq 0$ such that $\mu' = P \mu$ satisfies the conditions of [the residue zeros theorem](/entry/core-orth-core/): $\mu'_i \neq 0$, $|\mu'_i| \leq 1$, $|\mu'_i|$ is decreasing, $|\mu'_i| < \ell\,|\mu'_j|$ for all $i, j$, and $|c_j|\,|\mu'_j| \leq |\sum_i c_i \mu'_i|$ for all $c \in \mathbb{Q}_\ell^h$ and all $j$.
3. (Independence from the first terms.) Let $h \geq 2$, $0 \leq r < 1$, and let $y_a = (y_{a,k})_k$ for $a < d$ be sequences in $\mathcal{O}_C^\flat$ with $|y_{a,k}^\sharp| \leq r$. Assume that for every $n \in \mathbb{N}^d$ with $|(\sum_a n_a y_{a,0})^\sharp| \leq r^{\ell^h}$, every $n_a$ is divisible by $\ell$. If $c \in \mathbb{Q}_\ell^d$ satisfies $\sum_a c_a A_{h,j}(y_a) = 0$ for $j = 0$ and $j = 1$, then $c = 0$.
4. (Periodic vectors.) Let $h > 0$, $e > 0$ and $c \in B$ with $\ell^e \varphi^h(c) = c$ and $\iota_j(c) \in \mathrm{Fil}^0$ for all $j < h$. Then $c = 0$.

The map $\theta$ in fact 1 plays the role of Fontaine's map $\theta$ on $B_{\mathrm{dR}}^+$. Fact 1 says that the residues of the $\iota_j(b)$ are exactly the series of the previous section.

**Theorem 6.19.1 (Nonzero Frobenius vector with zero residues).** Let $h \geq 2$, and let $\lambda_0, \dots, \lambda_{h-1} \in \mathrm{Fil}^0$. Assume that for every $c \in \mathbb{Q}_\ell^h$ with $\sum_j c_j \lambda_j \in \mathrm{Fil}^1$ we have $c = 0$. Then there is $a = (a_0, \dots, a_{h-1}) \in B^h$ with $a \neq 0$ such that:

1. $a_j \in B^+$ and $\varphi^h(a_j) = \ell\, a_j$ for all $j$;
2. $\sum_j \lambda_j\, \iota_i(a_j) \in \mathrm{Fil}^1$ for every $i < h$.

Lean: `GlobalTheory.T.exists_nonzero_frobVector_residue_zero` (also `GlobalTheory.PMonII.exII`, `GlobalTheory.T.existsNonzeroFrobVectorResidueZero_proof` and `GlobalTheory.PMon.exII_holds`, second names).

*Proof.* Step 1: residues of $\lambda$. Put $\mu_j = \theta(\lambda_j) \in \mathbb{C}_\ell$. The $\mu_j$ are linearly independent over $\mathbb{Q}_\ell$: if $\sum_j c_j \mu_j = 0$ with $c \in \mathbb{Q}_\ell^h$, then $\theta(\sum_j c_j \lambda_j) = 0$, so $\sum_j c_j \lambda_j \in \mathrm{Fil}^1$ and $c = 0$. Fact 2 gives $P$ with $\det P \neq 0$ such that $\mu' = P\mu$ satisfies the conditions of the residue zeros theorem.

Step 2: the sequences. [The residue zeros theorem](/entry/exists-orthogonal-family-residue-zeros/) for $\mu'$ gives sequences $y_0, \dots, y_{h-1}$ in $\mathcal{O}_C^\flat$, an index $j_0$ and reals $r, R$ with $0 \leq r < 1$, $R < 1$, $|y_{k,n}^\sharp| \leq R$, $|y_{j_0,n}^\sharp| \leq r$, $r^{\ell^h} < |y_{j_0,0}^\sharp|$, and $\sum_k \mu'_k A_{h,i}(y_k) = 0$ for every $i < h$. For each $k < h$, fact 1 with the bound $R$ gives $b_k \in B^+$ with $\varphi^h(b_k) = \ell\, b_k$ and $\theta(\iota_j(b_k)) = A_{h,j}(y_k)$ for all $j$.

Step 3: $b_{j_0} \neq 0$. Suppose $b_{j_0} = 0$. Then $A_{h,j}(y_{j_0}) = \theta(0) = 0$ for all $j$. We apply fact 3 with $d = 1$, the sequence $y_{j_0}$ and the bound $r$. Its hypothesis holds: let $n \in \mathbb{N}$ with $\ell \nmid n$. In the ring $\mathcal{O}_C^\flat$ of characteristic $\ell$, there is an integer $m$ with $m n = 1$, so $y = m \cdot (n y)$ and $|y^\sharp| = |m^\sharp|\,|(ny)^\sharp| \leq |(ny)^\sharp|$ for every $y$. For $y = y_{j_0,0}$ this gives $|(n y_{j_0,0})^\sharp| \geq |y_{j_0,0}^\sharp| > r^{\ell^h}$. So $|(n y_{j_0,0})^\sharp| \leq r^{\ell^h}$ forces $\ell \mid n$. Fact 3 with $c = 1$ now gives $1 = 0$, a contradiction.

Step 4: the vector $a$. Put
$$a_j = \sum_{k} P_{kj}\, b_k.$$
Then $a \neq 0$, since $b_{j_0} = \sum_j (P^{-1})_{j j_0}\, a_j$ and $b_{j_0} \neq 0$. Each $a_j$ lies in $B^+$, since $B^+$ contains $\mathbb{Q}_\ell$ and is closed under sums and products. Since $\varphi^h$ is $\mathbb{Q}_\ell$-linear, $\varphi^h(a_j) = \ell\, a_j$. Let $i < h$. The element $X = \sum_j \lambda_j\, \iota_i(a_j)$ lies in $\mathrm{Fil}^0$, since $\iota_i(b_k) \in \mathrm{Fil}^0$ for $b_k \in B^+$. Its residue is
$$\begin{aligned} \theta(X) &= \sum_j \sum_k \mu_j\, P_{kj}\, A_{h,i}(y_k) \\ &= \sum_k \mu'_k\, A_{h,i}(y_k) = 0. \end{aligned}$$
Since the kernel of $\theta$ is $\mathrm{Fil}^1$, $X \in \mathrm{Fil}^1$. $\square$

**Theorem 6.19.2 (Vectors of the second kind).** Let $h \geq 2$ and $\lambda_0, \dots, \lambda_{h-1} \in \mathrm{Fil}^0$ be as in the previous [Theorem 6.19.1](/entry/exists-nonzero-frob-vector-residue-zero/): if $c \in \mathbb{Q}_\ell^h$ and $\sum_j c_j \lambda_j \in \mathrm{Fil}^1$, then $c = 0$. Then there is $a \in B^h$ such that:

1. $\varphi^h(a_j) = \ell\, a_j$ for all $j$;
2. $\iota_i(a_j) \in \mathrm{Fil}^0$ for all $i \geq 0$ and all $j$;
3. $\sum_j \lambda_j\, \iota_i(a_j) \in \mathrm{Fil}^1$ for every $i < h$;
4. $\det M(a) \neq 0$, where $M(a) = (\varphi^i a_j)_{0 \leq i, j < h}$.

Lean: `GlobalTheory.T.exists_secondKind_matrix_moore_det_ne_zero` (also `GlobalTheory.SecondKind.exists_secondKind`, a second name).

*Proof.* The previous Theorem gives $a \neq 0$ with entries in $B^+$, with $\varphi^h(a_j) = \ell\, a_j$, and with property 3. Property 2 holds since $a_j \in B^+$. If the $a_j$ are linearly independent over $\mathbb{Q}_\ell$, then [the Moore determinant theorem](/entry/moore-determinant-cris-plus-ne-zero/) with $k = h$ gives property 4. We show that the other case is impossible.

Suppose that the $a_j$ are linearly dependent. Let $V \subseteq B$ be their $\mathbb{Q}_\ell$-span, and $k = \dim V$. Then $k < h$, since the family is dependent, and $k > 0$, since $a \neq 0$. Choose a basis $b_0, \dots, b_{k-1}$ of $V$. Every element of $V$ lies in $B^+$ and is an eigenvector of $\varphi^h$ with eigenvalue $\ell$, since both properties are stable under $\mathbb{Q}_\ell$-linear combinations. By the Moore determinant theorem with $k \leq h$, $\det M(b) \neq 0$, where $M(b) = (\varphi^i b_m)_{0 \leq i, m < k}$. We show that $\det M(b) = 0$.

Step 1: new coefficients. Write $a_j = \sum_m c_{jm} b_m$ with $c_{jm} \in \mathbb{Q}_\ell$, and put $\lambda'_m = \sum_j c_{jm} \lambda_j \in \mathrm{Fil}^0$. Then $\lambda'_0 \notin \mathrm{Fil}^1$. Otherwise the hypothesis gives $c_{j0} = 0$ for all $j$. Then every $a_j$ has $0$-th coordinate $0$ in the basis $b$, so every element of $V$ does, but $b_0$ has $0$-th coordinate $1$.

Step 2: all shifts. For every $i \geq 0$,
$$\sum_m \lambda'_m\, \iota_i(b_m) = \sum_j \lambda_j\, \iota_i(a_j) \in \mathrm{Fil}^1.$$
The equality holds since $\iota_i$ is linear. For $i < h$ the membership is property 3. For $i \geq h$ it follows by induction, since $\iota_{i}(x) = \ell\, \iota_{i-h}(x)$ for every $x$ with $\varphi^h(x) = \ell x$.

Step 3: the determinant lies in $\mathrm{Fil}^1$ at every level. Fix $j \geq 0$, and let $N$ be the $k \times k$ matrix with entries $N_{im} = \iota_{j+i}(b_m)$. Its entries lie in $\mathrm{Fil}^0$, and by step 2 every entry of $N\lambda'$ lies in $\mathrm{Fil}^1$. The adjugate of $N$ has entries in $\mathrm{Fil}^0$, so
$$\det(N)\, \lambda'_0 = \sum_i (\operatorname{adj} N)_{0i}\, (N\lambda')_i \in \mathrm{Fil}^1.$$
Since $\lambda'_0 \in \mathrm{Fil}^0 \setminus \mathrm{Fil}^1$, it has an inverse in $\mathrm{Fil}^0$. So $\det N \in \mathrm{Fil}^1$. Since $\iota_j$ is a ring homomorphism, $\det N = \iota_j(\det M(b))$. So $\iota_j(\det M(b)) \in \mathrm{Fil}^1$ for every $j \geq 0$.

Step 4: the eigenvalue of the determinant. The map $\varphi^h$ multiplies every column of $M(b)$ by $\ell$, so $\varphi^h(\det M(b)) = \ell^k \det M(b)$.

Step 5: vanishing. Let $d = \det M(b)$, and let $c = d\, t_B^{-1}$; here $t_B$ is a unit of $B$. Since $\varphi(t_B) = \ell\, t_B$, we have $\varphi^h(t_B^{-1}) = \ell^{-h} t_B^{-1}$, so $\ell^{h-k} \varphi^h(c) = c$ with $h - k > 0$. For $j < h$, $\iota_j(t_B^{-1}) = \ell^{-j} t^{-1}$, so $t\, \iota_j(c) = \ell^{-j} \iota_j(d) \in \mathrm{Fil}^1$. Multiplication by $t$ maps $x$ into $\mathrm{Fil}^1$ exactly when $x \in \mathrm{Fil}^0$, so $\iota_j(c) \in \mathrm{Fil}^0$. Fact 4, with $e = h - k$, gives $c = 0$. So $d = c\, t_B = 0$, a contradiction. $\square$

**Remark 6.19.3 (Formalization).** The chain of names for the first theorem is long: `GlobalTheory.T.existsNonzeroFrobVectorResidueZero_proof` is a wrapper of `GlobalTheory.PMon.exII_holds`, which is the term `GlobalTheory.T.exists_nonzero_frobVector_residue_zero` ([ExistsNonzeroFrobVectorResidueZeroProof.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsNonzeroFrobVectorResidueZeroProof.lean#L9)), which is in turn a wrapper of `GlobalTheory.PMonII.exII`. In the first theorem, condition 2 is asked only for $i < h$. The second theorem uses the wrapper `GlobalTheory.T.existsNonzeroFrobVectorResidueZero_proof`. Its conclusion drops positivity and linear independence of $a$, although the proof shows that $a$ is linearly independent ([ExistsSecondKindMatrixMooreDetNeZero.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsSecondKindMatrixMooreDetNeZero.lean#L335)). Step 5 is the lemma `GlobalTheory.SecondKind.eq_zero_of_frobeniusImages_mem_filOne` (line 122 of the same file). In fact 1 the bound $r < 1$ comes without $r \geq 0$; for $r < 0$ the hypothesis on $y$ is empty.
