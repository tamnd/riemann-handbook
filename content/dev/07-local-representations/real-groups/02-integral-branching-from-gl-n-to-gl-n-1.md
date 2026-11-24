---
title: Integral branching from GL(N) to GL(N-1)
decls:
  - Formalism.L2.DIV.BrJ.branching_interlacing_pairs
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Integral branching from GL(N) to GL(N-1)

The branching rule of Gelfand and Tsetlin says which irreducible representations of $\mathrm{GL}_{N-1}$ occur in the restriction of an irreducible representation of $\mathrm{GL}_N$, and that each occurs once. The proof needs more than the rule: it needs the branching maps over $\mathbb{Z}$, with an explicit image of the extremal vector, an explicit integer constant and a bound on the norms of the maps for the Fock inner product. This section constructs these maps. They feed the step [HypsAlt is nonempty from the closed bound](/step/nonempty-hyps/), where they control the denominators of the coefficients of a test vector.

Background: [highest weights and branching](/learn/representations/#highest-weights-and-branching), [minors and determinant identities](/learn/combinatorics/#minors-and-determinant-identities) and [polynomials on matrices](/learn/combinatorics/#polynomials-on-matrices).

### Weyl modules and dual Weyl modules in polynomials

Fix $N \geq 1$ and let $R$ be $\mathbb{Z}$, $\mathbb{Q}$ or $\mathbb{C}$. Let $R[x]$ be the polynomial ring in the entries $x_{ij}$, $0 \leq i, j < N$, of a square matrix of variables. A *dominant weight* of $\mathrm{GL}_N$ is $\lambda \in \mathbb{Z}^N$ with $\lambda_0 \geq \lambda_1 \geq \dots \geq \lambda_{N-1}$. Put $\nu = \lambda - \lambda_{N-1}$, so that $\nu \in \mathbb{N}^N$ is dominant with $\nu_{N-1} = 0$.

**Definition 2.2.1 (Dual Weyl module).** $\nabla(\lambda)_R \subseteq R[x]$ is the set of polynomials $f$ that are homogeneous of degree $\nu_j$ in the variables of column $j$, for each $j$, and that satisfy $f(x + t\, x_{\bullet l} e_j^{T}) = f(x)$ in $R[x][t]$ for all $l < j$. Here $x + t\, x_{\bullet l} e_j^{T}$ is the matrix $x$ with $t$ times column $l$ added to column $j$.

**Definition 2.2.2 (Extremal vector and Weyl module).** Let $\Delta_s$ be the leading principal $s \times s$ minor of $x$. The *extremal vector* is $e_\lambda = \prod_{s=0}^{N-1} \Delta_{s+1}^{\nu_s - \nu_{s+1}}$, with $\nu_N = 0$. For rows $a, b$ and $k \geq 0$, let $D_{ab}^{(k)} f$ be the coefficient of $t^k$ in $f$ after the substitution $x_{bj} \mapsto x_{bj} + t\, x_{aj}$ for all $j$. The *Weyl module* $\Delta(\lambda)_R$ is the $R$-span of all $D_{a_1 b_1}^{(k_1)} \cdots D_{a_r b_r}^{(k_r)} e_\lambda$.

The operators $D_{ab}^{(k)}$ are the divided powers $E_{ab}^k / k!$ of the row operators $E_{ab} = \sum_j x_{aj}\, \partial / \partial x_{bj}$, written so that they make sense over $\mathbb{Z}$. Over $\mathbb{C}$ both $\nabla(\lambda)_\mathbb{C}$ and $\Delta(\lambda)_\mathbb{C}$ are the irreducible representation of highest weight $\lambda$; over $\mathbb{Z}$ they are two lattices in it, $\Delta \subseteq \nabla$.

**Definition 2.2.3 (The action and the Fock pairing).** For $g \in \mathrm{GL}_N(R)$ and $f \in R[x]$ put $(g \cdot f)(x) = \det(g)^{\lambda_{N-1}} f(g^{T} x)$. For $f, h \in \mathbb{C}[x]$ put
$$\langle f, h \rangle_\lambda = \frac{\sum_m f_m\, \overline{h_m}\, m!}{\sum_m |e_{\lambda, m}|^2\, m!},$$
where $f_m$ is the coefficient of the monomial $x^m$ and $m! = \prod_{ij} m_{ij}!$.

The numerator is the Fock (or Fischer) inner product, for which $x_{ij}$ and $\partial/\partial x_{ij}$ are adjoint. It is invariant under the unitary group $U(N)$. The normalisation makes $\langle e_\lambda, e_\lambda \rangle_\lambda = 1$.

The two lattices are dual to each other for this pairing. We use this fact and do not prove it in this section.

**Theorem 2.2.4 (Duality of the two lattices).** Let $f \in \nabla(\lambda)_\mathbb{Q}$. Then $\langle f, h \rangle_\lambda \in \mathbb{Z}$ for every $h \in \nabla(\lambda)_\mathbb{Z}$ if and only if $f \in \Delta(\lambda)_\mathbb{Z}$.

Lean: `Formalism.BasicNotions.factDelDualNabla`.

### The constants

Let $N = n + 1$, let $\lambda$ be a dominant weight of $\mathrm{GL}_N$ and $\sigma$ one of $\mathrm{GL}_n$. They *interlace* if $\lambda_{i+1} \leq \sigma_i \leq \lambda_i$ for $0 \leq i < n$. For interlacing weights put, for $i < n$:
$$a_i = \sigma_i - \lambda_{i+1}, \qquad b_i = \lambda_i - \sigma_i, \qquad D_0 = \sum_{i<n} a_i, \qquad D_1 = \sum_{i<n} \min(\lambda_i - \lambda_{i+1}, D_0),$$
and $\deg = \sum_i \lambda_i - \sum_i \sigma_i$. Let $R_i$ be the set of integers $v$ with $\lambda_{i+1} \leq v \leq \min(\lambda_i, \lambda_{i+1} + D_0)$.

**Definition 2.2.5 (Branching constant and branching vector).** The *branching constant* is the integer
$$c(\lambda, \sigma) = \prod_{i<n}\ \prod_{v \in R_i \smallsetminus \{\sigma_i\}}\ \prod_{j<n} \big((v - i) - \sigma_j + j\big).$$
The *branching vector* is
$$\xi(\lambda, \sigma) = \prod_{i<n} \Delta_{i+1}^{\,a_i}\, M_i^{\,b_i},$$
where $M_i$ is the minor of $x$ on the rows $0, \dots, i-1, N-1$ and the columns $0, \dots, i$. The *spread* of $\lambda$ is $\lambda_0 - \lambda_{N-1} + N$. Put
$$C(\lambda, \sigma) = (2\,\mathrm{spread}(\lambda))^{N D_1}, \qquad B(\lambda, \sigma) = C(\lambda, \sigma)\,\sqrt{\dim \Delta(\lambda)_\mathbb{C}}.$$

The factors of $c$ are values of the linear forms that separate the infinitesimal character of $\sigma$ from those of the other $\sigma'$ that interlace $\lambda$ with $\sigma'_i \in R_i$. The vector $\xi$ is a highest weight vector of weight $\sigma$ for $\mathrm{GL}_n \subseteq \mathrm{GL}_N$ inside $\nabla(\lambda)$: the minors $\Delta_{i+1}$ carry weight in the first $i+1$ coordinates, and $M_i$ trades the last row for row $i$.

**Example 2.2.6.** Let $N = 2$, $n = 1$, $\lambda = (2, 0)$, $\sigma = (1)$. Then $a_0 = 1$, $b_0 = 1$, $D_0 = 1$, $R_0 = \{0, 1\}$, and $c = (0 - 0) - 1 + 0 = -1$. The vector is $\xi = x_{00} \cdot x_{10}$: the minor $M_0$ is the $1 \times 1$ minor on row $N - 1 = 1$ and column $0$. It lies in $\nabla(2,0)$, the binary quadratic forms in the first column.

### The theorem

The classical branching rule reads: the restriction to $\mathrm{GL}_{N-1}(\mathbb{C})$ of the irreducible representation of $\mathrm{GL}_N(\mathbb{C})$ of highest weight $\lambda$ is the direct sum, each with multiplicity one, of the irreducible representations of highest weight $\sigma$ for $\sigma$ interlacing $\lambda$ (I. M. Gelfand and M. L. Tsetlin, Dokl. Akad. Nauk SSSR 71 (1950); R. Goodman and N. R. Wallach, *Symmetry, Representations, and Invariants*, Chapter 8). We embed $\mathrm{GL}_n$ in $\mathrm{GL}_N$ by $g \mapsto \mathrm{diag}(g, 1)$ and write $\ell(a) = \mathrm{diag}(1, \dots, 1, a)$.

**Theorem 2.2.7 (Integral branching maps).** Let $N = n + 1$ and let $\lambda, \sigma$ be dominant weights of $\mathrm{GL}_N$ and $\mathrm{GL}_n$ that interlace. Then $c(\lambda, \sigma) \neq 0$, $|c(\lambda, \sigma)| \leq C(\lambda, \sigma)$, $\xi(\lambda, \sigma) \neq 0$ and $\deg = \lambda_0 - D_0$. There are $\mathbb{C}$-linear maps $\iota : \mathbb{C}[x_{n \times n}] \to \mathbb{C}[x_{N \times N}]$ and $\beta : \mathbb{C}[x_{N \times N}] \to \mathbb{C}[x_{n \times n}]$ with these properties, where $B = B(\lambda, \sigma)$.

1. For each $s \in \nabla(\sigma)_\mathbb{Z}$ there is $f \in \nabla(\lambda)_\mathbb{Z}$ with $\iota(s) = f$, and $\iota(\nabla(\sigma)_\mathbb{C}) \subseteq \nabla(\lambda)_\mathbb{C}$.
2. $\iota(g \cdot s) = \mathrm{diag}(g, 1) \cdot \iota(s)$ for $g \in \mathrm{GL}_n(\mathbb{C})$ and $s \in \nabla(\sigma)_\mathbb{C}$, and $\ell(a) \cdot \iota(s) = a^{\deg}\, \iota(s)$ for $a \in \mathbb{C}^\times$.
3. $\iota(e_\sigma) = c(\lambda, \sigma)\, \xi(\lambda, \sigma)$, and $\langle \iota s, \iota s \rangle_\lambda \leq B^2 \langle s, s \rangle_\sigma$ for $s \in \nabla(\sigma)_\mathbb{C}$.
4. For each $f \in \Delta(\lambda)_\mathbb{Z}$ there is $h \in \Delta(\sigma)_\mathbb{Z}$ with $\beta(f) = h$; $\beta(\Delta(\lambda)_\mathbb{C}) \subseteq \Delta(\sigma)_\mathbb{C}$; and $\beta(f) \neq 0$ for some $f \in \Delta(\lambda)_\mathbb{C}$.
5. $\beta(\mathrm{diag}(g, 1) \cdot f) = g \cdot \beta(f)$ and $\beta(\ell(a) \cdot f) = a^{\deg} \beta(f)$ for $f \in \Delta(\lambda)_\mathbb{C}$, and $\langle \beta f, \beta f \rangle_\sigma \leq B^2 \langle f, f \rangle_\lambda$.
6. $\langle \iota s, f \rangle_\lambda = \langle s, \beta f \rangle_\sigma$ for $s \in \nabla(\sigma)_\mathbb{C}$ and $f \in \Delta(\lambda)_\mathbb{C}$.

Lean: `Formalism.L2.DIV.BrJ.branching_interlacing_pairs`.

The identity $\deg = \lambda_0 - D_0$ holds by the definitions: $\lambda_0 - D_0 = \lambda_0 + \sum_{i \geq 1} \lambda_i - \sum_i \sigma_i$.

*Proof.* This is [Theorem 4.3.3 of Volume 10](/entry/g-tlower-of/) applied to the duality of the two lattices. That theorem adds three facts over $\mathbb{C}$: $\nabla(\lambda)_\mathbb{C} = \Delta(\lambda)_\mathbb{C}$ is irreducible with a unique highest weight line; the branching rule; and Schur orthogonality for the Fock pairing. It then applies [Theorem 7.1.7 of Volume 10](/entry/wgl-g-tlower-of/). We describe the steps.

First, the numbers. Each factor $(v - i) - \sigma_j + j$ of $c$ with $v \in R_i$, $v \neq \sigma_i$, is nonzero, by the interlacing inequalities and the strict decrease of $\sigma_j - j$. There are at most $n \cdot \sum_i \min(\lambda_i - \lambda_{i+1}, D_0) \leq N D_1$ factors, and each has absolute value at most $2\,\mathrm{spread}(\lambda)$, which gives $|c| \leq C$. The vector $\xi$ is a product of nonzero minors, so it is nonzero. It lies in $\nabla(\lambda)_\mathbb{C}$, it is fixed by the upper unitriangular matrices of $\mathrm{GL}_n$, it has weight $\sigma$ for the diagonal torus of $\mathrm{GL}_n$, and $\ell(a)$ acts on it by $a^{\deg}$.

Second, a map over $\mathbb{C}$. By the branching rule, the highest weight vectors of weight $\sigma$ for $\mathrm{GL}_n$ in $\nabla(\lambda)_\mathbb{C}$ form a line, and $\xi$ spans it. Since $\nabla(\sigma)_\mathbb{C}$ is irreducible and generated by $e_\sigma$, there is a unique $\mathrm{GL}_n$-equivariant map $\iota_0 : \nabla(\sigma)_\mathbb{C} \to \nabla(\lambda)_\mathbb{C}$ with $\iota_0(e_\sigma) = \xi$, and $\ell(a)$ acts on its image by $a^{\deg}$.

Third, integrality of $\iota = c\, \iota_0$. There is a Capelli-type operator $Z$ on $\mathbb{C}[x_{N \times N}]$ that preserves $\nabla(\lambda)_\mathbb{Z}$ and that acts on the image of any equivariant map from $\nabla(\sigma')_\mathbb{C}$, $\sigma'$ interlacing $\lambda$, by an integer scalar $z(\sigma')$. Here $z(\sigma) = c(\lambda, \sigma)$, and $z(\sigma') = 0$ when $\sigma' \neq \sigma$ has the same total degree. Every $s \in \nabla(\sigma)_\mathbb{Z}$ lifts to some $m \in \nabla(\lambda)_\mathbb{Z}$ with $m - \iota_0(s)$ in the sum of the other $\mathrm{GL}_n$-isotypic parts. Applying $Z$ gives $Z(m) = c\, \iota_0(s)$, an element of $\nabla(\lambda)_\mathbb{Z}$.

Fourth, $\beta$. Choose a basis $(b_k)$ of $\nabla(\sigma)_\mathbb{C}$ that is orthonormal for $\langle \cdot, \cdot \rangle_\sigma$, and put $\beta(f) = \sum_k \langle f, \iota b_k \rangle_\lambda\, b_k$. Then property 6 holds, and $\beta$ maps into $\nabla(\sigma)_\mathbb{C} = \Delta(\sigma)_\mathbb{C}$. The equivariance of $\beta$ follows from that of $\iota$. Schur orthogonality gives $\langle \iota s, \iota s \rangle_\lambda = \langle \xi, \xi \rangle_\lambda\, |c|^2 \langle s, s \rangle_\sigma$; a second use of Schur orthogonality on $U(N)$, with the bound $|\xi(x)| \leq 1$ for $x \in U(N)$, bounds $\langle \xi, \xi \rangle_\lambda$ by $\dim \Delta(\lambda)_\mathbb{C}$, and with $|c| \leq C$ this gives the norm bound for $\iota$ and the same bound for its adjoint $\beta$. Since $\iota \neq 0$, also $\beta \neq 0$ on $\Delta(\lambda)_\mathbb{C}$.

Fifth, integrality of $\beta$. Let $f \in \Delta(\lambda)_\mathbb{Z}$. For $s \in \nabla(\sigma)_\mathbb{Z}$, $\langle s, \beta f \rangle_\sigma = \langle \iota s, f \rangle_\lambda$ is an integer, because $\iota s \in \nabla(\lambda)_\mathbb{Z}$ and $f \in \Delta(\lambda)_\mathbb{Z}$ (duality of the two lattices, one direction). By the other direction of the duality, applied to $\sigma$, $\beta f \in \Delta(\sigma)_\mathbb{Z}$. $\square$

**Remark 2.2.8 (Formalization).** The statement proved is that of [PrimeDegreeVariant.lean](lean:Formalism/SharpRestriction/Divisibility/PrimeDegreeVariant.lean#L104). The proof returns a statement with the same content written with a second copy of all the definitions (interlacing, the constants, the two maps), and the two copies agree by definition. The identity $\deg = \lambda_0 - D_0$ in the conclusion is true by the definitions and carries no information. A theorem with the same short name, in an unrelated namespace, proves a different statement ([BranchingInterlacingPairs.lean](lean:Formalism/SharpRestriction/GlobalSchurBounds/GlobalRankLatticeProofs/BranchingInterlacingPairs.lean#L53)). The Fock norm bounds are stated for the real parts of the pairings; the pairings of a vector with itself are real.
