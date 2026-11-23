---
title: The lattice lemma
decls:
  - GlobalTheory.T.fundamentalLemmaLattice_degreeOne
  - GlobalTheory.PMon.FLOne.flAt_one
  - GlobalTheory.T.fundamentalLemmaLatticeFrobFixed_forall_degree
  - GlobalTheory.PMon.flAt_all
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The lattice lemma

A de Rham representation with weights is described by $r$ lattices $U_m (\mathrm{Fil}^0)^n$ in $B_{\mathrm{dR}}^n$, one for each power $\sigma^m$ of Frobenius. The weight modification of the next section changes two weights by $\mp 1$. On the lattices, this means that one column of one $U_m$ is divided by $t$, and another column is multiplied by $t$. The lattice lemma says that, under a condition of linear independence, the modified lattices are spanned by the images of one matrix $A$ over $B$ that is fixed by $\varphi^r$. We prove it first for $r = 1$, with the Frobenius vectors of the previous sections, and then for all $r$ by restriction of scalars. The lemma is used in [the weight modification](/entry/monodromy-irreducible-elementary-weight-modification/).

We keep the notation of the previous sections: $B$, $\varphi$, $\iota$, $\mathrm{Fil}^\bullet$, $t = \iota(t_B)$, $t^a = \iota(t_B^a)$, $B^+$, the Moore matrix $M(a)$ and $\iota_j = \iota \circ \varphi^j$. The field $\mathbb{Q}_\ell^{\mathrm{ur}}$ with its Frobenius $\sigma$ maps into $B$ and into $B_{\mathrm{dR}}$, compatibly with $\iota$; we write $c$ for the image of $c \in \mathbb{Q}_\ell^{\mathrm{ur}}$. Maps act on matrices entry by entry. For a finite set $n$ write $\mathrm{GL}_n(\mathrm{Fil}^0)$ for the set of $U \in \mathrm{GL}_n(B_{\mathrm{dR}})$ such that $U$ and $U^{-1}$ have all entries in $\mathrm{Fil}^0$.

**Definition 6.20.1 (Elementary exponents).** Let $Z$ be a set and $x, y \in Z$. For $z \in Z$ put $\varepsilon_{x,y}(z) = -1$ if $z = x$, $\varepsilon_{x,y}(z) = 1$ if $z = y$ and $z \neq x$, and $\varepsilon_{x,y}(z) = 0$ otherwise.

Lean: `GlobalTheory.PMon.eps`.

**Definition 6.20.2 (Lattice lemma in degree $r$).** Let $r \geq 0$. We say that the *lattice lemma holds in degree $r$* if the following is true for every prime $\ell$, all tied local period data and every finite set $n$. Let $U_0, \dots, U_{r-1} \in \mathrm{GL}_n(\mathrm{Fil}^0)$ and $x = (x_1, x_2)$, $y = (y_1, y_2)$ in $\{0, \dots, r-1\} \times n$ with $x \neq y$. Assume that for every $c \in (\mathbb{Q}_\ell^{\mathrm{ur}})^n$ with $\sigma^r(c_i) = c_i$ for all $i$,
$$\sum_{i \in n} c_i\, (U_{x_1})_{i, x_2} \in \mathrm{Fil}^1 \implies c = 0.$$
Then there is $A \in \mathrm{GL}_n(B)$ with $\varphi^r(A_{ij}) = A_{ij}$ for all $i, j$, such that for every $m < r$ there is $W_m \in \mathrm{GL}_n(\mathrm{Fil}^0)$ with
$$\iota_m(A) = U_m \cdot \operatorname{diag}\big( t^{\varepsilon_{x,y}(m,j)} \big)_{j \in n} \cdot W_m.$$

Lean: `GlobalTheory.PMon.FLAt`.

The hypothesis says that the column $x_2$ of $U_{x_1}$ is linearly independent modulo $\mathrm{Fil}^1$ over the field of $\sigma^r$-fixed elements. In the conclusion, the columns of $\iota_m(A)$ span the lattice $U_m D_m (\mathrm{Fil}^0)^n$, where $D_m = \operatorname{diag}(t^{\varepsilon_{x,y}(m,j)})$. This lattice differs from $U_m (\mathrm{Fil}^0)^n$ only at the level $m = x_1$, where column $x_2$ is divided by $t$, and at the level $m = y_1$, where column $y_2$ is multiplied by $t$.

We use the following facts, proved elsewhere in this development.

1. (Moore determinants that vanish modulo $\mathrm{Fil}^1$.) Let $h > 0$ and $a \in B^h$ with $\varphi^h(a_j) = \ell\, a_j$, $\iota_i(a_j) \in \mathrm{Fil}^0$ for all $i \geq 0$ and all $j$, $\det M(a) \neq 0$ and $\iota(\det M(a)) \in \mathrm{Fil}^1$. Then $\det M(a) = \kappa\, t_B$ for some $\kappa \in \mathbb{Q}_\ell^{\mathrm{ur}}$ with $\kappa \neq 0$.
2. (Vectors of the first kind.) Let $h \geq 2$ and $\mu \in (\mathrm{Fil}^0)^h$ with $\mu_i \notin \mathrm{Fil}^1$ for some $i$. Then there is $b \in (B^+)^h$, linearly independent over $\mathbb{Q}_\ell$, with $\varphi^h(b_j) = \ell\, b_j$ and $\sum_i \mu_i\, \iota_i(b_j) \in \mathrm{Fil}^1$ for every $j$.

We also use the determinant argument of [the previous section](/entry/exists-second-kind-matrix-moore-det-ne-zero/), in this form. Let $N$ be a square matrix with entries in $\mathrm{Fil}^0$, and $v$ a vector with entries in $\mathrm{Fil}^0$ and some $v_k \notin \mathrm{Fil}^1$. If all entries of $N v$ lie in $\mathrm{Fil}^1$, or all entries of $v^{T} N$ do, then $\det N \in \mathrm{Fil}^1$. Indeed $\det(N) v_k$ is a combination of the entries of $Nv$ (or of $v^T N$) with coefficients in the adjugate, and $v_k$ has an inverse in $\mathrm{Fil}^0$.

**Theorem 6.20.3 (Lattice lemma in degree one).** The lattice lemma holds in degree $1$.

Lean: `GlobalTheory.T.fundamentalLemmaLattice_degreeOne` (also `GlobalTheory.PMon.FLOne.flAt_one`, a second name).

*Proof.* Here $x = (0, x_2)$ and $y = (0, y_2)$ with $x_2 \neq y_2$. So $h = |n| \geq 2$. We number the elements of $n$ as $0, \dots, h-1$. Write $U = U_0$.

Step 1: the column. Let $\lambda_k = U_{k, x_2}$, the column $x_2$ of $U$. Its entries lie in $\mathrm{Fil}^0$. For $c \in \mathbb{Q}_\ell^h$ we have $\sigma(c_i) = c_i$, so the hypothesis gives: if $\sum_k c_k \lambda_k \in \mathrm{Fil}^1$, then $c = 0$. In particular some $\lambda_k \notin \mathrm{Fil}^1$.

Step 2: the first Moore matrix. [The theorem on vectors of the second kind](/entry/exists-second-kind-matrix-moore-det-ne-zero/) gives $a \in B^h$ with $\varphi^h(a_j) = \ell\, a_j$, $\iota_i(a_j) \in \mathrm{Fil}^0$, $\sum_j \lambda_j\, \iota_i(a_j) \in \mathrm{Fil}^1$ for $i < h$, and $\det M(a) \neq 0$. Let $A_1 = M(a)$. Then every entry of $\iota(A_1) \lambda$ lies in $\mathrm{Fil}^1$, so $\iota(\det A_1) \in \mathrm{Fil}^1$ by the determinant argument. Fact 1 gives $\det A_1 = \kappa\, t_B$ with $\kappa \in \mathbb{Q}_\ell^{\mathrm{ur}}$ nonzero. So $\det A_1$ is a unit of $B$.

Step 3: the first new lattice. Let $D_x$ be the diagonal matrix with $t^{-1}$ at $x_2$ and $1$ elsewhere, and put $U' = \iota(A_1)\, U\, D_x$. The entries of $\iota(A_1) U$ lie in $\mathrm{Fil}^0$, and its column $x_2$ is $\iota(A_1)\lambda$, which lies in $\mathrm{Fil}^1$. Since $t^{-1}\mathrm{Fil}^1 = \mathrm{Fil}^0$, all entries of $U'$ lie in $\mathrm{Fil}^0$. Also
$$\det U' = \kappa\, t \cdot \det U \cdot t^{-1} = \kappa \det U,$$
whose inverse $\kappa^{-1} \det(U^{-1})$ lies in $\mathrm{Fil}^0$. So $U' \in \mathrm{GL}_n(\mathrm{Fil}^0)$, since the inverse is the adjugate divided by the determinant.

Step 4: the row. Let $V = U'^{-1}$ and $\mu_k = V_{y_2, k}$, the row $y_2$ of $V$. Its entries lie in $\mathrm{Fil}^0$. Some $\mu_k \notin \mathrm{Fil}^1$, since $\sum_k \mu_k U'_{k, y_2} = (VU')_{y_2,y_2} = 1$ and $1 \notin \mathrm{Fil}^1$.

Step 5: the second Moore matrix. Fact 2 gives $b \in (B^+)^h$, linearly independent over $\mathbb{Q}_\ell$, with $\varphi^h(b_j) = \ell\, b_j$ and $\sum_k \mu_k\, \iota_k(b_j) \in \mathrm{Fil}^1$ for every $j$. Let $B_1 = M(b)$. By [the Moore determinant theorem](/entry/moore-determinant-cris-plus-ne-zero/), $\det B_1 \neq 0$. The entries $\iota_i(b_j)$ lie in $\mathrm{Fil}^0$ since $b_j \in B^+$, and every entry of $\mu^T \iota(B_1)$ lies in $\mathrm{Fil}^1$. The determinant argument and fact 1 give $\det B_1 = \kappa' t_B$ with $\kappa' \in \mathbb{Q}_\ell^{\mathrm{ur}}$ nonzero.

Step 6: the matrix $W$. Let $X = V \iota(B_1)$. Its entries lie in $\mathrm{Fil}^0$, and its row $y_2$ is $\mu^T \iota(B_1)$, which lies in $\mathrm{Fil}^1$. Let $D_y$ be the diagonal matrix with $t^{-1}$ at $y_2$ and $1$ elsewhere, and $W = D_y X$. Then $W$ has entries in $\mathrm{Fil}^0$, and $\det W = \kappa' \det V$, whose inverse $\kappa'^{-1} \det U'$ lies in $\mathrm{Fil}^0$. So $W \in \mathrm{GL}_n(\mathrm{Fil}^0)$.

Step 7: the matrix $A$. Let $A = A_1^{-1} B_1$. It is invertible over $B$, with determinant $\kappa^{-1}\kappa'$. Let $C$ be the $h \times h$ matrix with $C_{i,i+1} = 1$ for $i + 1 < h$, $C_{h-1,0} = \ell$, and all other entries $0$. Since $\varphi^h(a_j) = \ell\, a_j$, the rows of $\varphi(M(a))$ are the rows $1, \dots, h-1$ of $M(a)$ followed by $\ell$ times row $0$. So $\varphi(A_1) = C A_1$, and in the same way $\varphi(B_1) = C B_1$. Hence
$$\varphi(A) = (C A_1)^{-1} C B_1 = A_1^{-1} B_1 = A.$$
Finally, since $U' V = 1$,
$$\begin{aligned} \iota_0(A) &= \iota(A_1)^{-1}\, U' V\, \iota(B_1) \\ &= U D_x\, X = U\, \operatorname{diag}\big(t^{\varepsilon_{x,y}(0,j)}\big)\, D_y X = U\, \operatorname{diag}\big(t^{\varepsilon_{x,y}(0,j)}\big)\, W. \end{aligned}$$
Here $\operatorname{diag}(t^{\varepsilon_{x,y}(0,j)})\, D_y = D_x$: at $x_2$ both sides are $t^{-1}$, at $y_2$ the left side is $t \cdot t^{-1} = 1$, and elsewhere both sides are $1$. $\square$

To pass to degree $r$ we use restriction of scalars from the field of $\sigma^r$-fixed elements to $\mathbb{Q}_\ell$. The following facts are proved elsewhere in this development. Let $r > 0$.

3. (A basis of the fixed field.) There are $\omega_0, \dots, \omega_{r-1} \in \mathbb{Q}_\ell^{\mathrm{ur}}$, fixed by $\sigma^r$ and linearly independent over $\mathbb{Q}_\ell$, such that every $\sigma^r$-fixed element of $\mathbb{Q}_\ell^{\mathrm{ur}}$ is a $\mathbb{Q}_\ell$-linear combination of them, and such that the matrix $\Omega = (\sigma^m(\omega_k))_{0 \leq m, k < r}$ has $\det \Omega \neq 0$.

Let $\omega$ be as in fact 3. Index the rows and columns of matrices of size $nr$ by $n \times \{0, \dots, r-1\}$. Let $R$ be the matrix with $R_{(i,m),(i',k)} = \sigma^m(\omega_k)$ if $i = i'$ and $0$ otherwise; it is invertible since $\det \Omega \neq 0$. Given $U_0, \dots, U_{r-1}$, let $\tilde U = R^{-1} \cdot \operatorname{blockdiag}(U_0, \dots, U_{r-1})$, where the block diagonal matrix has entry $(U_m)_{i,i'}$ at $((i,m),(i',m))$. For $a \in B^n$, say that $a$ satisfies the *lattice condition* if $\varphi^r(a_i) = a_i$ for all $i$ and, for every $m < r$, there is $w \in (\mathrm{Fil}^0)^n$ with $\iota_m(a) = U_m\, \operatorname{diag}(t^{\varepsilon_{x,y}(m,j)})\, w$. For a matrix $A_0$ of size $nr$ over $B$ and a column index $c$, let $v_c \in B^n$ be the vector with entries $(v_c)_i = \sum_k \omega_k\, (A_0)_{(i,k), c}$.

4. If all $U_m \in \mathrm{GL}_n(\mathrm{Fil}^0)$, then $\tilde U \in \mathrm{GL}_{nr}(\mathrm{Fil}^0)$.
5. If the hypothesis of the lattice lemma in degree $r$ holds at $x$, then for every $c \in (\mathbb{Q}_\ell^{\mathrm{ur}})^{n \times r}$ with $\sigma(c) = c$, $\sum_{(i,m)} c_{(i,m)}\, \tilde U_{(i,m),(x_2,x_1)} \in \mathrm{Fil}^1$ implies $c = 0$.
6. Let $A_0 \in \mathrm{GL}_{nr}(B)$ be fixed by $\varphi$, and let $W_0 \in \mathrm{GL}_{nr}(\mathrm{Fil}^0)$ with $\iota(A_0) = \tilde U\, \operatorname{diag}(t^{\varepsilon_{x,y}(m,j)})_{(j,m)}\, W_0$. Then every $v_c$ satisfies the lattice condition, and the $v_c$ are linearly independent over $\mathbb{Q}_\ell$.
7. Under the hypotheses of 6, every $a \in B^n$ that satisfies the lattice condition is a $\mathbb{Q}_\ell$-linear combination of the $v_c$.
8. If $a$ satisfies the lattice condition and $e \in \mathbb{Q}_\ell^{\mathrm{ur}}$ is fixed by $\sigma^r$, then $e a$ satisfies the lattice condition.
9. Let $M$ be a $\mathbb{Q}_\ell^{\mathrm{ur}}$-module, and let $(v_c)_{c \in n \times r}$ be a family in $M$, linearly independent over $\mathbb{Q}_\ell$, whose $\mathbb{Q}_\ell$-span is stable under multiplication by $\sigma^r$-fixed elements. Then there are $a_j \in M$, $j \in n$, in this span, such that the family $(\omega_k a_j)_{(j,k)}$ is linearly independent over $\mathbb{Q}_\ell$ and has the same $\mathbb{Q}_\ell$-span as $(v_c)$.
10. Under the hypotheses of 6 and with all $U_m \in \mathrm{GL}_n(\mathrm{Fil}^0)$, if $a_j \in B^n$ ($j \in n$) are such that $(\omega_k a_j)_{(j,k)}$ has the same $\mathbb{Q}_\ell$-span as $(v_c)$, then the conclusion of the lattice lemma in degree $r$ holds for $U$, $x$ and $y$.

In fact 9, the span of the $v_c$ is a vector space over the field $E$ of $\sigma^r$-fixed elements, and the $a_j$ form an $E$-basis of it. In fact 10, they become the columns of the matrix $A$.

**Theorem 6.20.4 (Lattice lemma).** The lattice lemma holds in every degree $r \geq 0$.

Lean: `GlobalTheory.T.fundamentalLemmaLatticeFrobFixed_forall_degree` (also `GlobalTheory.PMon.flAt_all`, a second name).

*Proof.* If $r = 0$, the set $\{0, \dots, r-1\} \times n$ is empty, so there is no $x$ and nothing to prove. Let $r > 0$, and let $U$, $x$, $y$ satisfy the hypotheses. Take $\omega$ by fact 3 and form $\tilde U$. By fact 4, $\tilde U \in \mathrm{GL}_{nr}(\mathrm{Fil}^0)$. By fact 5, the hypothesis of the lattice lemma in degree one holds for $\tilde U$ at the index $(0, (x_2, x_1))$. The indices $x' = (0, (x_2, x_1))$ and $y' = (0, (y_2, y_1))$ are distinct since $x \neq y$, and $\varepsilon_{x',y'}(0, (j, m)) = \varepsilon_{x,y}(m, j)$. So [the lattice lemma in degree one](/entry/fundamental-lemma-lattice-degree-one/) gives $A_0 \in \mathrm{GL}_{nr}(B)$ fixed by $\varphi$ and $W_0 \in \mathrm{GL}_{nr}(\mathrm{Fil}^0)$ as in fact 6.

By fact 6, the vectors $v_c$ satisfy the lattice condition and are linearly independent over $\mathbb{Q}_\ell$. Their span is stable under multiplication by a $\sigma^r$-fixed $e$: for each $c$, $e v_c$ satisfies the lattice condition by fact 8, so it lies in the span by fact 7. Fact 9, with $M = B^n$, gives $a_j$ such that $(\omega_k a_j)$ has the same span as $(v_c)$. Fact 10 gives the matrix $A$ and the matrices $W_m$. $\square$

**Remark 6.20.5 (Formalization).** The proof in degree one applies its hypothesis only to coefficients in $\mathbb{Q}_\ell$ ([FundamentalLemmaLatticeDegreeOne.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/FundamentalLemmaLatticeDegreeOne.lean#L179), lines 179 to 189), which is all the hypothesis gives when $r = 1$. The condition $x \neq y$ is used only to get $|n| \geq 2$. In the proof for all degrees, the case $r = 0$ is closed by `x.1.elim0` ([FundamentalLemmaLatticeFrobFixedForallDegree.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/FundamentalLemmaLatticeFrobFixedForallDegree.lean#L24)). The fact behind fact 3 also gives a finite extension $E$ of $\mathbb{Q}_\ell$ of degree $r$ inside $\mathbb{Q}_\ell^{\mathrm{ur}}$ whose elements are the $\sigma^r$-fixed ones; these three clauses are discarded at line 25. Facts 1 and 2 are `GlobalTheory.T.mooreDeterminant_eq_unramified_mul_period` and `GlobalTheory.T.existsIndependentFrobSolutionsCris_proof`, and facts 4 to 10 are wrappers of lemmas in `GlobalTheory.PMon.ResR`, `GlobalTheory.PMon.Extract` and `GlobalTheory`. The matrices $R$, $\tilde U$ and the vectors $v_c$ are `GlobalTheory.PMon.ResR.resMat`, `GlobalTheory.PMon.ResR.U0` and `GlobalTheory.PMon.ResR.colv`.
