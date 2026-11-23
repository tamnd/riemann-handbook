---
title: Symplectic reduction of positive definite forms
decls:
  - GroundTheory.Heights₂.Heights.SymplStep.full
  - GroundTheory.Heights₂.Heights.SymplecticReduction.full
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Symplectic reduction of positive definite forms

This section proves a reduction theorem for positive definite symplectic matrices. Let $G$ be a real symmetric positive definite matrix of size $2g$ that is also symplectic. We find an integral symplectic matrix $P$ such that, after the change of basis by $P$, the first basis vector is a shortest nonzero vector of the lattice $\mathbb{Z}^{2g}$ for the form $G$, and the upper left $g \times g$ block of the new matrix has determinant at most $\rho^2 (2g)^{g-1}$, where $\rho^2$ is the length of a shortest vector. The proof is an induction on $g$: one reduction step finds the first row and passes to a symplectic matrix of size $2g - 2$ by a Schur complement. The theorem is used in [the reduced basis](/entry/symplectic-reduction-basis/) of the chapter on sup norms of theta sections, where it puts the imaginary part of a period matrix into the reduced form of the next section.

### Symplectic matrices and the Gram matrix

We index vectors of $R^{2g}$ by two copies of $\{1, \dots, g\}$. We write a vector as $v = (x, y)$ with $x, y \in R^g$, and $e_1$ for the first basis vector of the first copy. Let
$$J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$$
in $g \times g$ blocks.

**Definition 4.4.1 (Symplectic group).** Let $R$ be a commutative ring. The symplectic group $\mathrm{Sp}_g(R)$ is the set of matrices $M$ of size $2g$ over $R$ with $M J M^{\mathsf T} = J$.

It is a group under multiplication. A real symplectic matrix has determinant $1$. For $g = 0$ the group is trivial.

**Definition 4.4.2 (Quadratic form, Gram matrix, upper left block).** For a real square matrix $G$ and a real vector $v$, put $q_G(v) = v^{\mathsf T} G v$. For an integral matrix $P$, the Gram matrix of $G$ in the basis given by the rows of $P$ is $P[G] = P G P^{\mathsf T}$. For a matrix $H$ of size $2g$, its upper left block $H_{11}$ is the $g \times g$ block with rows and columns in the first copy.

The diagonal entry of $P[G]$ at $e_1$ is $q_G(P_1)$, where $P_1$ is the first row of $P$. If $P \in \mathrm{Sp}_g(\mathbb{Z})$ and $G \in \mathrm{Sp}_g(\mathbb{R})$ is positive definite, then $P[G]$ is again symplectic and positive definite, and $(QP)[G] = Q[P[G]]$ for every integral $Q$. A positive definite $G$ has a minimum on $\mathbb{Z}^{2g} \setminus \{0\}$, because the lattice has only finitely many points in each ellipsoid $q_G \le t$.

**Example 4.4.3.** Let $g = 1$. Then $\mathrm{Sp}_1(R) = \mathrm{SL}_2(R)$, and a positive definite $G \in \mathrm{SL}_2(\mathbb{R})$ is the Gram matrix of a binary quadratic form of discriminant $-4$. The theorem below says that $\mathrm{SL}_2(\mathbb{Z})$ moves $G$ to a matrix whose upper left entry is the minimum $\rho^2$ of the form, with $\rho^2 \le 2$. Gauss reduction gives the better bound $\rho^2 \le 2/\sqrt{3}$.

### The first row

**Lemma 4.4.4 (Minkowski's bound for the minimum).** Let $G$ be a real positive definite matrix of size $n$ with $\det G = 1$. Let $m$ be the minimum of $q_G$ on $\mathbb{Z}^n \setminus \{0\}$. Then $m \le n$.

*Proof.* Diagonalize: there are $O$ with $|\det O| = 1$ and $\lambda_1, \dots, \lambda_n > 0$ with $\prod_i \lambda_i = \det G = 1$ and $q_G(x) = \sum_i \lambda_i (Ox)_i^2$. Let $c > 1$ and put $a_i = c/\sqrt{\lambda_i}$. Then $\prod_i a_i = c^n > 1$. By Minkowski's theorem for boxes, there is a nonzero $v \in \mathbb{Z}^n$ with $|(Ov)_i| < a_i$ for all $i$: the box $\{x : |(Ox)_i| < a_i\}$ is convex and symmetric, and its volume $2^n \prod_i a_i$ is larger than $2^n$. Then $m \le q_G(v) < \sum_i \lambda_i a_i^2 = n c^2$. This holds for every $c > 1$, so $m \le n$. $\square$

**Lemma 4.4.5 (A shortest vector is a first row).** Let $G \in \mathrm{Sp}_{n+1}(\mathbb{R})$ be positive definite, and let $\rho^2$ be the minimum of $q_G$ on $\mathbb{Z}^{2n+2} \setminus \{0\}$. Then $0 < \rho^2 \le 2(n+1)$, and there is $P \in \mathrm{Sp}_{n+1}(\mathbb{Z})$ with $P[G]_{e_1, e_1} = \rho^2$.

*Proof.* The minimum is positive because $G$ is positive definite. Since $G$ is symplectic, $\det G = 1$, and the previous lemma with $n$ replaced by $2(n+1)$ gives $\rho^2 \le 2(n+1)$. Let $v$ be a nonzero integral vector with $q_G(v) = \rho^2$. Every integral vector is an integral multiple of the first row of some integral symplectic matrix: write $v = m P_1$ with $P \in \mathrm{Sp}_{n+1}(\mathbb{Z})$ and $m \in \mathbb{Z}$. (This is proved by induction on $n$, with a Bézout identity for the gcd of two coordinates and the matrices $\operatorname{ext}(Q)$ defined below.) Since $v$ is shortest, $\rho^2 = m^2 q_G(P_1) \ge m^2 \rho^2$, so $m = \pm 1$. Replace $P$ by $-P$ if $m = -1$. Then $P_1 = v$ and $P[G]_{e_1,e_1} = q_G(v) = \rho^2$. $\square$

### The reduction step

**Definition 4.4.6 (Symplectic Schur complement).** Let $H$ be a real matrix of size $2n + 2$ with $h = H_{e_1, e_1} \ne 0$. Let $f_1$ be the first basis vector of the second copy. The reduction $\operatorname{red}(H)$ is the matrix of size $2n$, indexed by the basis vectors other than $e_1$ and $f_1$, with entries
$$\operatorname{red}(H)_{a,b} = H_{a,b} - \frac{H_{a,e_1} H_{e_1,b}}{h}.$$

So $\operatorname{red}(H)$ is the Schur complement of the entry $h$, with the row and column of $f_1$ also removed. If $H$ is positive definite, so is $\operatorname{red}(H)$, since it is the Gram matrix of the projections of the remaining basis vectors along $e_1$, restricted to a subspace. If $H$ is symplectic and $h \ne 0$, then $\operatorname{red}(H)$ is symplectic.

For $Q$ of size $2n$, let $\operatorname{ext}(Q)$ be the matrix of size $2n+2$ that is the identity on $e_1$ and $f_1$ and is $Q$ on the other basis vectors. If $Q \in \mathrm{Sp}_n(R)$, then $\operatorname{ext}(Q) \in \mathrm{Sp}_{n+1}(R)$. A direct computation gives
$$\operatorname{ext}(Q)[H]_{e_1,e_1} = h, \qquad \operatorname{red}\bigl(\operatorname{ext}(Q)[H]\bigr) = Q[\operatorname{red}(H)].$$

**Lemma 4.4.7 (Determinant of the upper left block).** Let $H$ be real of size $2n+2$ with $h = H_{e_1,e_1} \ne 0$, and let $Q \in \mathrm{Sp}_n(\mathbb{Z})$. Then there is $Q' \in \mathrm{Sp}_{n+1}(\mathbb{Z})$ with $Q'[H]_{e_1,e_1} = h$ and
$$\det Q'[H]_{11} = h \cdot \det Q[\operatorname{red}(H)]_{11}.$$

*Proof.* Take $Q' = \operatorname{ext}(Q)$. The first claim is the display above. For a square matrix $A$ with $A_{00} \ne 0$, the Schur formula gives $\det A = A_{00} \det(A_{ij} - A_{i0}A_{0j}/A_{00})_{i,j \ne 0}$. Apply it to $A = Q'[H]_{11}$. Its entry at $e_1$ is $h$, and its Schur complement is the upper left block of $\operatorname{red}(Q'[H]) = Q[\operatorname{red}(H)]$. $\square$

**Theorem 4.4.8 (Symplectic reduction step).** Let $n \ge 0$, $B \in \mathbb{R}$, and let $G \in \mathrm{Sp}_{n+1}(\mathbb{R})$ be positive definite. Assume that for every positive definite $H \in \mathrm{Sp}_n(\mathbb{R})$ there is $P \in \mathrm{Sp}_n(\mathbb{Z})$ with $\det P[H]_{11} \le B$. Then the minimum $\rho^2$ of $q_G$ on $\mathbb{Z}^{2n+2} \setminus \{0\}$ exists and satisfies $0 < \rho^2 \le 2(n+1)$, and there is $P \in \mathrm{Sp}_{n+1}(\mathbb{Z})$ with
$$P[G]_{e_1,e_1} = \rho^2, \qquad \det P[G]_{11} \le \rho^2 B.$$

Lean: `GroundTheory.Heights₂.Heights.SymplStep.full`

*Proof.* By the lemma on the first row, there is $P_1 \in \mathrm{Sp}_{n+1}(\mathbb{Z})$ with $H = P_1[G]$ and $H_{e_1,e_1} = \rho^2 > 0$. The matrix $H$ is symplectic and positive definite, so $\operatorname{red}(H)$ is symplectic and positive definite of size $2n$. By the assumption, there is $Q \in \mathrm{Sp}_n(\mathbb{Z})$ with $\det Q[\operatorname{red}(H)]_{11} \le B$. The determinant lemma gives $Q'$ with $Q'[H]_{e_1,e_1} = \rho^2$ and $\det Q'[H]_{11} = \rho^2 \det Q[\operatorname{red}(H)]_{11} \le \rho^2 B$. Put $P = Q' P_1$. Then $P[G] = Q'[H]$. $\square$

### The theorem

**Theorem 4.4.9 (Symplectic reduction).** Let $g \ge 1$ and let $G \in \mathrm{Sp}_g(\mathbb{R})$ be positive definite. Let $\rho^2$ be the minimum of $q_G$ on $\mathbb{Z}^{2g} \setminus \{0\}$. Then $\rho^2 \le 2g$, and there is $P \in \mathrm{Sp}_g(\mathbb{Z})$ with
$$P[G]_{e_1,e_1} = \rho^2, \qquad \det P[G]_{11} \le \rho^2 (2g)^{g-1}.$$

Lean: `GroundTheory.Heights₂.Heights.SymplecticReduction.full`

*Proof.* First we show by induction on $n \ge 0$: every positive definite $H \in \mathrm{Sp}_n(\mathbb{R})$ has some $P \in \mathrm{Sp}_n(\mathbb{Z})$ with $\det P[H]_{11} \le (2n)^n$. For $n = 0$ the block is empty, its determinant is $1$, and $(2 \cdot 0)^0 = 1$. For the step from $n$ to $n + 1$, the reduction step with $B = (2n)^n$ gives $P$ with $\det P[H]_{11} \le \rho^2 (2n)^n \le 2(n+1) \cdot (2(n+1))^n$.

Now write $g = n + 1$. The reduction step with $B = (2n)^n$, whose assumption is the claim just proved, gives $\rho^2 \le 2g$ and $P$ with $P[G]_{e_1,e_1} = \rho^2$ and $\det P[G]_{11} \le \rho^2 (2n)^n \le \rho^2 (2g)^{g-1}$. $\square$

**Remark 4.4.10.** Let $X$ be a real symmetric and $Y$ a real positive definite $g \times g$ matrix. With $M = \begin{pmatrix} 1 & X \\ 0 & 1 \end{pmatrix}$ the matrix
$$G = M^{\mathsf T} \begin{pmatrix} Y^{-1} & 0 \\ 0 & Y \end{pmatrix} M = \begin{pmatrix} Y^{-1} & Y^{-1}X \\ XY^{-1} & Y + XY^{-1}X \end{pmatrix}$$
is symplectic and positive definite, and its upper left block is $Y^{-1}$. If $G$ is reduced as in the theorem, then $(Y^{-1})_{11} = \rho^2$, the form $q_{Y^{-1}}$ is at least $\rho^2$ on $\mathbb{Z}^g \setminus \{0\}$ (these are the vectors $(l, 0)$), and $\det Y^{-1} \le \rho^2 (2g)^{g-1}$. These are the conditions of a reduced imaginary part in the next section.

**Remark 4.4.11 (Formalization).** The induction is split in two: the step is proved once ([StatementsSympl.lean](lean:GroundTheory/HeightsAndTheta/Heights/HeightKernels/StatementsSympl.lean#L143)), and both the bound $(2n)^n$ and the theorem apply it with $B = (2n)^n$ ([PSymplTop.lean](lean:GroundTheory/HeightsAndTheta/Heights/HeightKernels/PSymplTop.lean#L9)). The statement of the theorem does not record $\rho^2 > 0$, although the step proves it. The orbit lemma (every integral vector is a multiple of a first row) and Minkowski's theorem for boxes are proved in separate files of the same folder. The symplectic group is the group of Mathlib, defined by $MJM^{\mathsf T} = J$.
