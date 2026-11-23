---
title: Extensions and split representations
decls:
  - GlobalTheory.T.deRhamExtension_potentiallySemistable
  - GlobalTheory.PMon.extStep_holds
  - GlobalTheory.T.potentially_semistable_reducible_unramified_split
  - GlobalTheory.PMon.Red.redStep
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Extensions and split representations

This section proves step 4 of section 21, the reduction for split representations. Let $\rho : G_K \to \mathrm{GL}_n(\mathbb{Q}_\ell^{\mathrm{ur}})$ be $r$-rational and de Rham admissible, and assume that $\rho$ splits at level $r$. If the matrix form of the monodromy theorem holds in all smaller dimensions, then $\rho$ is semistable admissible. After a change of basis, $\rho$ is block upper triangular, and both diagonal blocks are semistable admissible by induction. So the key point is that an extension of two semistable admissible representations that is de Rham admissible is again semistable admissible. That is the extension step, and it rests on [the matrix form of Hyodo's theorem](/entry/hyodo-theorem-matrix-unramified-coefficients/) of the previous section. The reduction is used in [the proof of the matrix form](/entry/mat-thm-holds/), at the case where the weight modification of section 21 does not apply.

We keep the notation of sections 15 and 21. For finite sets $a$ and $b$, a matrix indexed by $a \sqcup b$ is written in blocks $\begin{pmatrix} A & C \\ 0 & D \end{pmatrix}$, with rows and columns in $a$ first.

**Definition 6.25.1 (Extension and sub-quotient steps).** Each statement quantifies over every prime $\ell$, all tied local period data, all finite sets $a$ and $b$, every finite extension $K$ of $\mathbb{Q}_\ell$, every $r \geq 0$, and all homomorphisms $\rho : G_K \to \mathrm{GL}_{a \sqcup b}(\mathbb{Q}_\ell^{\mathrm{ur}})$, $\rho_1 : G_K \to \mathrm{GL}_a(\mathbb{Q}_\ell^{\mathrm{ur}})$, $\rho_2 : G_K \to \mathrm{GL}_b(\mathbb{Q}_\ell^{\mathrm{ur}})$ and maps $c : G_K \to M_{a \times b}(\mathbb{Q}_\ell^{\mathrm{ur}})$ such that $\rho$ is $r$-rational and
$$\rho(g) = \begin{pmatrix} \rho_1(g) & c(g) \\ 0 & \rho_2(g) \end{pmatrix} \quad \text{for all } g \in G_K.$$

1. (Extension.) If $\rho$ is de Rham admissible and $\rho_1$ and $\rho_2$ are semistable admissible, then $\rho$ is semistable admissible.
2. (Sub-quotient.) If $\rho$ is de Rham admissible, then $\rho_1$ and $\rho_2$ are de Rham admissible.

Lean: `GlobalTheory.PMon.ExtStep` (also `GlobalTheory.PMon.SubQuot`, the second statement).

The sub-quotient step is proved elsewhere in this development. In terms of representations, $\rho_1$ is the subrepresentation on the span of the basis vectors in $a$, and $\rho_2$ is the quotient.

### The extension step

The extension class of $\rho$ lives in the cohomology of the representation $\mathrm{Hom}(\rho_2, \rho_1)$. In matrices, $G_K$ acts on $M_{a \times b}$ by $X \mapsto \rho_1(g)\, X\, \rho_2(g)^{-1}$. Identify $M_{a \times b}$ with column vectors indexed by $a \times b$. Then this action is the Kronecker product
$$\eta(g) = \rho_1(g) \otimes \big(\rho_2(g)^{-1}\big)^{\mathsf{T}} \in \mathrm{GL}_{a \times b}(\mathbb{Q}_\ell^{\mathrm{ur}}),$$
and the extension cocycle is $e(g) = c(g)\, \rho_2(g)^{-1}$, viewed as a vector indexed by $a \times b$. The upper right block of $\rho(gh) = \rho(g)\rho(h)$ is $c(gh) = \rho_1(g) c(h) + c(g) \rho_2(h)$. Multiply on the right by $\rho_2(gh)^{-1} = \rho_2(h)^{-1}\rho_2(g)^{-1}$:
$$e(gh) = e(g) + \rho_1(g)\, e(h)\, \rho_2(g)^{-1} = e(g) + \eta(g)\, e(h).$$
So $e$ is a cocycle for $\eta$. If $Q_1$ and $Q_2$ are period matrices for $\rho_1$ and $\rho_2$ over $B_{\mathrm{st}}$, then $Q_1 \otimes (Q_2^{-1})^{\mathsf{T}}$ is a period matrix for $\eta$, since $X \mapsto Q_1 X Q_2^{-1}$ intertwines the trivial action twisted by $g$ with the action of $\eta$.

We use the following facts, proved elsewhere in this development. Let $\rho$, $\rho_1$, $\rho_2$ and $c$ be as in the definition, with $\rho$ $r$-rational, and let $K' \supseteq K$ be a finite extension.

1. (Rationality.) The entries of $e$ are fixed by $\sigma^r$ and continuous in $g$, $e$ is a cocycle for $\eta$ on $G_{K'}$, and the restriction of $\eta$ to $G_{K'}$ is $r$-rational.
2. (Period matrix.) If $Q_1 \in \mathrm{GL}_a(B_{\mathrm{st}})$ and $Q_2 \in \mathrm{GL}_b(B_{\mathrm{st}})$ satisfy $\rho_i(g)\, g(Q_i) = Q_i$ for all $g \in G_{K'}$, then $\eta(g)\, g\big(Q_1 \otimes (Q_2^{-1})^{\mathsf{T}}\big) = Q_1 \otimes (Q_2^{-1})^{\mathsf{T}}$ for all $g \in G_{K'}$.
3. (De Rham.) If $\rho$ and $\rho_2$ are de Rham admissible, then for every $m \geq 0$ there is $v_m \in B_{\mathrm{dR}}^{a \times b}$ with $\sigma^m(e(g)) = \sigma^m(\eta(g))\, g(v_m) - v_m$ for all $g \in G_K$.
4. (Gluing.) With $Q_1$ and $Q_2$ as in 2, if $v \in B_{\mathrm{st}}^{a \times b}$ satisfies $e(g) = \eta(g)\, g(v) - v$ for all $g \in G_{K'}$, then there is $Q \in \mathrm{GL}_{a \sqcup b}(B_{\mathrm{st}})$ with $\rho(g)\, g(Q) = Q$ for all $g \in G_{K'}$.

Fact 4 is a computation with block matrices: if $v$ is viewed as an $a \times b$ matrix $V$, the matrix $Q = \begin{pmatrix} Q_1 & -V Q_2 \\ 0 & Q_2 \end{pmatrix}$ is invertible, with inverse $\begin{pmatrix} Q_1^{-1} & Q_1^{-1} V \\ 0 & Q_2^{-1} \end{pmatrix}$, and it is a period matrix for $\rho$.

**Theorem 6.25.2 (Extension step).** Let $\ell$, $a$, $b$, $K$, $r$, $\rho$, $\rho_1$, $\rho_2$ and $c$ be as in the definition, with $\rho$ $r$-rational and block upper triangular. If $\rho$ is de Rham admissible and $\rho_1$ and $\rho_2$ are semistable admissible, then $\rho$ is semistable admissible.

Lean: `GlobalTheory.T.deRhamExtension_potentiallySemistable` (also `GlobalTheory.PMon.extStep_holds`, the proof).

*Proof.* Choose finite extensions $K_1, K_2 \supseteq K$ and period matrices $Q_1$ on $G_{K_1}$ and $Q_2$ on $G_{K_2}$. Let $K' = K_1 K_2$ be the compositum. Then $G_{K'} \subseteq G_{K_1} \cap G_{K_2}$, so $Q_1$ and $Q_2$ are period matrices on $G_{K'}$. By the sub-quotient step, $\rho_2$ is de Rham admissible.

We apply [the matrix form of Hyodo's theorem](/entry/hyodo-theorem-matrix-unramified-coefficients/) over $K'$ to $\tau = \eta$ restricted to $G_{K'}$, with $Q = Q_1 \otimes (Q_2^{-1})^{\mathsf{T}}$ and the cocycle $e$. Its hypotheses hold: $\eta$ is $r$-rational on $G_{K'}$ and $e$ is a cocycle with $\sigma^r$-fixed continuous entries by fact 1; $Q$ is a period matrix on $G_{K'}$ by fact 2; and for each $m$ the vector $v_m$ of fact 3 kills $\sigma^m(e)$ over $B_{\mathrm{dR}}$ on $G_K$, hence on $G_{K'}$. The theorem gives $v \in B_{\mathrm{st}}^{a \times b}$ with $e(g) = \eta(g)\, g(v) - v$ on $G_{K'}$. Fact 4 gives a period matrix $Q$ for $\rho$ on $G_{K'}$. So $\rho$ is semistable admissible. $\square$

### Split representations

Let $\rho : G_K \to \mathrm{GL}_n(\mathbb{Q}_\ell^{\mathrm{ur}})$ and let $X \in M_{n' \times n}$ and $Y \in M_{n \times n'}$ satisfy $XY = 1$ and $YX = 1$. Then $\rho'(g) = X \rho(g) Y$ is a homomorphism $G_K \to \mathrm{GL}_{n'}(\mathbb{Q}_\ell^{\mathrm{ur}})$, the conjugate of $\rho$. We use the following facts, proved elsewhere in this development.

1. (Rationality of conjugates.) If the entries of $X$ and $Y$ are fixed by $\sigma^r$ and $\rho$ is $r$-rational, then $\rho'$ is $r$-rational.
2. (Admissibility of conjugates.) If the entries of $X$ and $Y$ are fixed by $\sigma^r$, and every $\sigma^r$-fixed element of $\mathbb{Q}_\ell^{\mathrm{ur}}$ lies in $K$, then $\rho'$ is de Rham admissible if $\rho$ is, and semistable admissible if $\rho$ is.

Fact 2 holds because the entries of $X$ and of $\sigma^m(X)$ lie in $K$ and so are fixed by $G_K$: if $Q$ is a period matrix for $\rho$ at level $m$, then $\sigma^m(X)\, Q\, \sigma^m(Y)$ is one for $\rho'$, because $\sigma^m(Y)\sigma^m(X) = 1$.

**Lemma 6.25.3 (Inverse of a rational matrix).** If $p \in \mathrm{GL}_n(\mathbb{Q}_\ell^{\mathrm{ur}})$ has entries fixed by $\sigma^r$, then so does $p^{-1}$.

Lean: `GlobalTheory.PMon.Red.rat_inv`.

*Proof.* Apply $\sigma^r$ to the entries of $p^{-1} p = 1$. This gives $\sigma^r(p^{-1})\, p = 1$, so $\sigma^r(p^{-1}) = p^{-1}$. $\square$

**Theorem 6.25.4 (Reduction for split representations).** Let $\ell$ be a prime with tied local period data, $n$ a finite set, $K$ a finite extension of $\mathbb{Q}_\ell$, $r \geq 0$, and $\rho : G_K \to \mathrm{GL}_n(\mathbb{Q}_\ell^{\mathrm{ur}})$ an $r$-rational, de Rham admissible homomorphism that splits at level $r$. Assume that for every finite set $a$ with $|a| < |n|$, every $r$-rational, de Rham admissible $\rho' : G_K \to \mathrm{GL}_a(\mathbb{Q}_\ell^{\mathrm{ur}})$ is semistable admissible. Then $\rho$ is semistable admissible.

Lean: `GlobalTheory.T.potentially_semistable_reducible_unramified_split` (also `GlobalTheory.PMon.Red.redStep`, the proof).

*Proof.* Take $s \subseteq n$, nonempty and proper, and $p$ with $\sigma^r$-fixed entries and $(p^{-1}\rho(g)p)_{ij} = 0$ for $i \notin s$, $j \in s$. Choose $x \in s$ and $y \notin s$. Reorder $n$ as $s \sqcup (n \setminus s)$. Let $X$ be the matrix of the rows of $p^{-1}$ in this order, and $Y$ the matrix of the columns of $p$ in this order. Then $XY = 1$ and $YX = 1$, since $p^{-1}p = 1$ and $pp^{-1} = 1$. The entries of $Y$ are fixed by $\sigma^r$ by assumption, and those of $X$ by the Lemma.

Let $\rho' = X \rho Y$. By facts 1 and 2, $\rho'$ is $r$-rational and de Rham admissible; the condition that $\sigma^r$-fixed elements lie in $K$ is part of $r$-rationality of $\rho$. The block of $\rho'(g)$ with rows outside $s$ and columns in $s$ is zero, so
$$\rho'(g) = \begin{pmatrix} \rho_1(g) & c(g) \\ 0 & \rho_2(g) \end{pmatrix},$$
where $\rho_1$ and $\rho_2$ are the diagonal blocks. These are homomorphisms, because the diagonal blocks of a product of block upper triangular matrices are the products of the diagonal blocks, and they are $r$-rational because their entries are entries of $\rho'$. By the sub-quotient step, $\rho_1$ and $\rho_2$ are de Rham admissible. Since $y \notin s$, $|s| < |n|$, and since $x \in s$, $|n \setminus s| < |n|$. By the hypothesis on smaller dimensions, $\rho_1$ and $\rho_2$ are semistable admissible. The extension step shows that $\rho'$ is semistable admissible. Finally $\rho = Y \rho' X$, and fact 2 applied to this conjugate shows that $\rho$ is semistable admissible. $\square$

**Remark 6.25.5 (Formalization).** The extension step uses [the matrix form of Hyodo's theorem](/entry/hyodo-theorem-matrix-unramified-coefficients/) over $K'$, and its semistability hypothesis is met on $G_{K'}$, not on $G_K$; this is why the compositum is formed first. Facts 1 to 4 of the extension step are `GlobalTheory.T.matrixHomRepresentationCocycle_rational_continuous` with `GlobalTheory.T.matrixHomRepresentation_restrict_rational_continuous`, `GlobalTheory.T.matrixHom_periodMatrix_semistable`, `GlobalTheory.T.blockTriangular_extensionCocycle_trivial_deRham` and `GlobalTheory.T.extension_block_periodMatrix_semistable`; we read their statements, and the proof of fact 4 for the explicit matrix. The sub-quotient step is `GlobalTheory.T.deRham_blockTriangular_diagonal_blocks`. The facts on conjugates are `isRat_of`, `deRham_of_conjugate_unramified_rational` and `semistable_of_conjugate_unramified_rational` in [PotentiallySemistableReducibleUnramifiedSplit.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/PotentiallySemistableReducibleUnramifiedSplit.lean#L58).
