---
title: Reduced symplectic bases of a principally polarized lattice
decls:
  - GlobalTheory.CompanionTheory.Ar.NForm.exists_reduced
  - GlobalTheory.T.real_part_gram_in_symplectic_group
  - GlobalTheory.CompanionTheory.Ar.NformRed.symplectic_reduction_basis
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Reduced symplectic bases of a principally polarized lattice

The theta bound of the [first section](/entry/nform/) works in one archimedean frame. Its first step puts the frame in a normal form: a period matrix $\Omega = X + iY$ whose imaginary part is reduced. This section proves that normal form. The proof has two parts. The first part is a statement about lattices: a symplectic basis can be changed by an integral symplectic matrix so that its first vector is a shortest vector and the first block of the Gram matrix has a small determinant. The second part transports this statement to the period matrix.

### Gram matrices of symplectic bases

Let $g \geq 1$. Let $\Lambda \subset \mathbb{C}^g$ be a discrete subgroup that spans $\mathbb{C}^g$ over $\mathbb{R}$. Then $\Lambda$ is free of rank $2g$. Let $H$ be a positive definite hermitian form on $\mathbb{C}^g$. Write $E = \operatorname{Im} H$. We index bases of $\Lambda$ by two copies of $\{1, \dots, g\}$ and write a basis as $(e_1, \dots, e_g, f_1, \dots, f_g)$. Let
$$
J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}
$$
in blocks of size $g$. A basis is symplectic for $H$ if $E(b_\alpha, b_\beta) = J_{\alpha\beta}$ for all basis vectors $b_\alpha, b_\beta$. The real Gram matrix of a basis is the real $2g \times 2g$ matrix $G_{\alpha\beta} = \operatorname{Re} H(b_\alpha, b_\beta)$. It is symmetric and positive definite.

For a symmetric positive definite real matrix $M$ and a real vector $v$ write $M[v] = v^{T} M v$. For a basis with Gram matrix $G$ and an integral vector $v \neq 0$, the lattice vector $x = \sum_\alpha v_\alpha b_\alpha$ is not zero and $\operatorname{Re} H(x, x) = G[v]$. So the first minimum of $\operatorname{Re} H$ on $\Lambda$ is the least value of $G[v]$ on nonzero integral vectors.

The input is the reduction theorem for real symplectic matrices from the heights chapter, [symplectic reduction](/entry/symplectic-reduction-full/). It says: let $G \in \operatorname{Sp}_{2g}(\mathbb{R})$ be positive definite and let $\rho^2$ be the least value of $G[v]$ for $v \in \mathbb{Z}^{2g}$, $v \neq 0$. Then $\rho^2 \leq 2g$, and there is $P \in \operatorname{Sp}_{2g}(\mathbb{Z})$ such that $G' = P G P^{T}$ has $G'_{11} = \rho^2$ and the upper left $g \times g$ block $G'_{11\text{-block}}$ of $G'$ satisfies
$$
\det G'_{11\text{-block}} \leq \rho^2 (2g)^{g - 1}.
$$

### Reduction of a basis

**Theorem 10.11.1 (Reduced symplectic basis).** Let $\Lambda$ and $H$ be as above. Let $(b_\alpha)$ be a symplectic basis of $\Lambda$ for $H$ whose real Gram matrix $G$ lies in $\operatorname{Sp}_{2g}(\mathbb{R})$. Then there are a symplectic basis $(e'_1, \dots, e'_g, f'_1, \dots, f'_g)$ of $\Lambda$ and a real number $\rho > 0$ with these properties.

1. $\rho^2 \leq 2g$.
2. $\operatorname{Re} H(e'_1, e'_1) = \rho^2$.
3. $\rho^2 \leq \operatorname{Re} H(l, l)$ for every $l \in \Lambda$ with $l \neq 0$.
4. The $g \times g$ matrix $A_{ij} = \operatorname{Re} H(e'_i, e'_j)$ satisfies $\det A \leq \rho^2 (2g)^{g - 1}$.

Lean: `GlobalTheory.CompanionTheory.Ar.NformRed.symplectic_reduction_basis` (also `GlobalTheory.T.real_part_gram_in_symplectic_group`, a second name).

*Proof.* Apply the reduction theorem to $G$. It gives $\rho^2 > 0$ with $\rho^2 \leq 2g$, the least value of $G[v]$ on nonzero integral vectors, and $P \in \operatorname{Sp}_{2g}(\mathbb{Z})$ with the two properties of $G' = P G P^{T}$. Put $\rho = \sqrt{\rho^2}$. Then $\rho > 0$ and property 1 holds.

Define the new basis by $b'_\alpha = \sum_\beta P_{\alpha\beta} b_\beta$. Since $P$ is invertible over $\mathbb{Z}$, the vectors $b'_\alpha$ form a basis of $\Lambda$. Write $e'_i$ and $f'_i$ for its two halves.

The forms are bilinear over $\mathbb{Z}$ in the real and imaginary parts. So
$$
\operatorname{Re} H(b'_\alpha, b'_\delta) = \sum_{\beta, \gamma} P_{\alpha\beta} G_{\beta\gamma} P_{\delta\gamma} = (P G P^{T})_{\alpha\delta},
$$
and in the same way the imaginary Gram matrix of the new basis is $P J P^{T}$. A symplectic matrix satisfies $P J P^{T} = J$, since its transpose is also symplectic. So the new basis is symplectic, and its real Gram matrix is $G'$.

Property 2 is $G'_{11} = \rho^2$. Property 4 is the determinant bound for the upper left block of $G'$, since that block is $A$.

For property 3 let $l \in \Lambda$ be nonzero. Write $l = \sum_\alpha v_\alpha b_\alpha$ with $v \in \mathbb{Z}^{2g}$. Since the $b_\alpha$ are linearly independent, $v \neq 0$. Then $\operatorname{Re} H(l, l) = G[v] \geq \rho^2$, since $\rho^2$ is the least value. $\square$

The first minimum is the same for every basis, since it is a property of $\Lambda$ and $H$. So property 3 does not depend on the new basis. Only properties 2 and 4 need the change of basis.

### The reduced period matrix

Let $(e_i, f_i)$ be a symplectic basis. The normal form of a hermitian form gives a complex matrix $h$ with $\det h \neq 0$, a real symmetric matrix $X$ and a positive definite real matrix $Y$ with three properties. Put $\Omega = X + iY$. Then $h e_i$ is the $i$-th unit vector, $h f_i$ is the $i$-th column of $\Omega$, and
$$
H(z, w) = H_\Omega(hz, hw), \qquad H_\Omega(z, w) = {}^{t}\bar z\, Y^{-1} w
$$
up to the order of the arguments. The real Gram matrix of the basis is then the Siegel matrix
$$
S(X, Y) = \begin{pmatrix} Y^{-1} & Y^{-1} X \\ X Y^{-1} & Y + X Y^{-1} X \end{pmatrix}.
$$
For $X$ symmetric and $Y$ positive definite, $S(X, Y)$ lies in $\operatorname{Sp}_{2g}(\mathbb{R})$ and is positive definite. This is the statement on Siegel coordinates from the heights chapter.

**Definition 10.11.2.** Let $Y$ be a positive definite real $g \times g$ matrix and $\rho$ a real number. The pair $(Y, \rho)$ is reduced if $\rho > 0$, $\rho^2 \leq 2g$, $(Y^{-1})_{11} = \rho^2$, $\rho^2 \leq Y^{-1}[l]$ for all $l \in \mathbb{Z}^g$ with $l \neq 0$, and $\det Y^{-1} \leq \rho^2 (2g)^{g - 1}$.

This is the reduction condition of the [theta bound](/entry/theta-bound-full/) of the heights chapter.

**Theorem 10.11.3 (Reduced period matrix).** Let $g \geq 1$. Let $\Lambda \subset \mathbb{C}^g$ be a discrete subgroup that spans $\mathbb{C}^g$ over $\mathbb{R}$, and let $H$ be a positive definite hermitian form. Assume that $E = \operatorname{Im} H$ takes integral values on $\Lambda \times \Lambda$, and that every $w \in \mathbb{C}^g$ with $E(w, \Lambda) \subset \mathbb{Z}$ lies in $\Lambda$. Then there are a basis $(e_i, f_i)$ of $\Lambda$, a complex matrix $h$ with $\det h \neq 0$, a real symmetric matrix $X$, a positive definite real matrix $Y$ and a real number $\rho$ such that:

1. the pair $(Y, \rho)$ is reduced;
2. $H(z, w) = H_\Omega(hz, hw)$ for all $z, w$, where $\Omega = X + iY$;
3. for $x = \sum_i m_i e_i + \sum_i n_i f_i$ in $\Lambda$ we have $h x = m + \Omega n$;
4. for $x$ as in 3 and $y = \sum_i m'_i e_i + \sum_i n'_i f_i$ we have
$$
E(x, y) = \sum_{i = 1}^{g} (n_i m'_i - m_i n'_i).
$$

Lean: `GlobalTheory.CompanionTheory.Ar.NForm.exists_reduced`.

*Proof.* Step 1: a symplectic basis. The form $E$ is alternating, integral on $\Lambda$ and unimodular by the dual condition. So $\Lambda$ has a basis $(b_\alpha)$ that is symplectic for $H$. This is the Frobenius normal form of a principal polarization.

Step 2: the Gram matrix is symplectic. Apply the normal form to $(b_\alpha)$. It gives $X_0$ symmetric and $Y_0$ positive definite such that the real Gram matrix of $(b_\alpha)$ is $S(X_0, Y_0)$. By the statement on Siegel coordinates, this matrix lies in $\operatorname{Sp}_{2g}(\mathbb{R})$ and is positive definite.

Step 3: reduce. The theorem on reduced symplectic bases gives a new symplectic basis $(e_i, f_i)$ and $\rho > 0$ with its four properties.

Step 4: the normal form again. Apply the normal form to $(e_i, f_i)$. It gives $h$, $X$ and $Y$ with $\det h \neq 0$, $X$ symmetric, $Y$ positive definite, $h e_i$ the $i$-th unit vector, $h f_i$ the $i$-th column of $\Omega$ and $H(z, w) = H_\Omega(hz, hw)$. This is property 2. Property 3 follows from the values of $h$ on the basis, since $h$ is linear and $x = \sum m_i e_i + \sum n_i f_i$.

Step 5: the entries of $Y^{-1}$. Since $h e_i$ and $h e_j$ are unit vectors, $\operatorname{Re} H(e_i, e_j) = \operatorname{Re} H_\Omega(\epsilon_i, \epsilon_j) = (Y^{-1})_{ij}$, where $\epsilon_i$ is the $i$-th unit vector. So $Y^{-1}$ is the matrix $A$ of the reduced basis.

Step 6: the pair is reduced. The conditions $\rho > 0$ and $\rho^2 \leq 2g$ come from Step 3. By Step 5 and property 2 of Step 3, $(Y^{-1})_{11} = \operatorname{Re} H(e_1, e_1) = \rho^2$. The determinant bound is property 4 of Step 3, by Step 5. For the minimum, let $l \in \mathbb{Z}^g$ be nonzero and put $x = \sum_i l_i e_i$. Then $h x = l$, viewed as a complex vector. So $x \neq 0$, since $h x \neq 0$. Property 3 of Step 3 gives
$$
\rho^2 \leq \operatorname{Re} H(x, x) = \operatorname{Re} H_\Omega(l, l) = Y^{-1}[l].
$$

Step 7: the alternating form. Expand $E(x, y)$ by bilinearity in the basis. Since the basis is symplectic, $E(e_i, e_j) = E(f_i, f_j) = 0$, $E(e_i, f_j) = -\delta_{ij}$ and $E(f_i, e_j) = \delta_{ij}$. The sum gives property 4. $\square$

**Remark 10.11.4 (Formalization).** The reduced period matrix is `exists_reduced` at `Development/AutomorphicSpectrum/Proofs/MetricProofs/ThetaFunctionEvenBound.lean:98`. Its only user is the theta bound `nform` in the same file (line 174). The reduction condition is the structure `IsReducedImaginaryPart` at `GroundTheory/HeightsAndTheta/Heights/KernelsMatrix.lean:63`; the reduction theorem for symplectic matrices is `SymplecticReduction.Statement` in the same file (line 14), and `siegelGram` is at line 24. The proof calls the normal form `GlobalTheory.T.hermitian_form_period_matrix_normal_form` twice (lines 113 and 116); the first call keeps only the Gram matrix. The statement on Siegel coordinates is reached through a lemma named `SiegelCoordinates.intersectionNumber_baseChange` (line 114). The name has nothing to do with intersection numbers or base change; the codebase uses this name for many unrelated closing lemmas. In the statement, "$\det h$ is a unit" stands for $\det h \neq 0$, and the order of the arguments of the hermitian form follows the convention of `hermForm`. The reduced basis is `symplectic_reduction_basis` at `RealPartGramInSymplecticGroup.lean:113`; it applies `SymplecticReduction.full` and builds the new basis with `twist_apply` (line 96). The second name, at `RealPartGramInSymplecticGroupStatement.lean:21`, closes its goal by `first | exact ...` over several forms of the same term.
