---
title: Positive semidefinite kernels
decls:
  - Formalism.FourierDecayAlt.P.HilbertSchmidtNorm.localCores
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Positive semidefinite kernels

The energy bounds of this chapter are statements about kernels: functions $k(x, y)$ of two points whose matrices on finite sets are positive semidefinite. This section fixes the definition, proves that three common forms of it agree, and proves the closure rules that the later sections use many times: products, differences of products, diagonal scaling and block diagonal parts. It ends with the theorem that collects these rules with the local kernel results of [Section 3.2.6](/entry/second-gram-and-vanishing/) into one statement, which the proof uses through [the applied Theorem PB](/entry/pb-applied/).

Let $\alpha$ be a set, let $F \subseteq \alpha$ be finite, and let $k : \alpha \times \alpha \to \mathbb{C}$.

**Definition 3.1.1 (Positive semidefinite kernel).** The kernel $k$ is *positive semidefinite on $F$* if the matrix $(k(x, y))_{x, y \in F}$ is a [[positive|0KX66CZMBB]] semidefinite Hermitian matrix: $k(y, x) = \overline{k(x, y)}$ for $x, y \in F$, and
$$\sum_{x, y \in F} \overline{c_x}\, k(x, y)\, c_y \geq 0 \quad \text{for each } c \in \mathbb{C}^F.$$

A kernel of the form $k(x, y) = \langle v_y, v_x \rangle$, with vectors $v_x$ in a [[Hilbert space|HM2HHE3J51]] (inner product linear in the first slot), is positive semidefinite on each finite set: the sum above is $\|\sum_y c_y v_y\|^2$. Each positive semidefinite matrix is a Gram matrix of this kind, so the definition says that $k$ restricted to $F$ is a Gram kernel.

**Lemma 3.1.2 (Three forms of positivity).** For $k$ and $F$ as above, the following are equivalent.

1. The matrix $(k(x, y))_{x, y \in F}$ is positive semidefinite.
2. $k(y, x) = \overline{k(x, y)}$ for $x, y \in F$, and $\sum_{x, y} \overline{c_x}\, k(x, y)\, c_y$ is real and nonnegative for each $c \in \mathbb{C}^F$.
3. For each $a \in \mathbb{C}^F$, the number $Q(a) = \sum_{x, y \in F} a_x \overline{a_y}\, k(x, y)$ has $\mathrm{Im}\, Q(a) = 0$ and $\mathrm{Re}\, Q(a) \geq 0$.

*Proof.* The first two forms are the definition of a positive semidefinite matrix, written out. Put $c = \bar a$; then $Q(a)$ is the sum of form 2, so form 2 gives form 3. Conversely, assume form 3. Then $Q(a)$ is real for each $a$. Apply this to $a = e_x + e_y$ and $a = e_x + i e_y$: the real parts of $k(x, y) - \overline{k(y, x)}$ and of $i(k(x, y) - \overline{k(y, x)})$ vanish, so $k(y, x) = \overline{k(x, y)}$. This is polarization. The sign condition of form 2 is then the sign condition of form 3 with $a = \bar c$. $\square$

**Proposition 3.1.3 (Closure rules).** Let $P$ be a finite set, let $F \subseteq \alpha$ be finite, and let all kernels be complex valued on $\alpha \times \alpha$.

1. (Schur products.) If $k_p$ is positive semidefinite on $F$ for each $p \in P$, then so is $(x, y) \mapsto \prod_{p \in P} k_p(x, y)$.
2. (Domination of products.) If $k_p$ and $K_p - k_p$ are positive semidefinite on $F$ for each $p \in P$, then so is $\prod_p K_p - \prod_p k_p$.
3. (Real scaling.) If $k$ is positive semidefinite on $F$ and $a : \alpha \to \mathbb{R}$, then so is $a(x)\, a(y)\, k(x, y)$.
4. (Phases.) If $k$ is positive semidefinite on $F$ and $d : \alpha \to \mathbb{C}$, then so is $d(x)\, \overline{d(y)}\, k(x, y)$.
5. (Block diagonal parts.) Let $c : \alpha \to \beta$ be a map to a set $\beta$. If $k$ is positive semidefinite on each fibre $F \cap c^{-1}(b)$, then the kernel equal to $k(x, y)$ when $c(x) = c(y)$ and to $0$ otherwise is positive semidefinite on $F$.

*Proof.* Rule 1 is the Schur product theorem (Horn and Johnson, *Matrix Analysis*, 2nd ed., Theorem 7.5.3) for two factors: if $A = \sum_i u_i u_i^*$ and $B = \sum_j w_j w_j^*$, then the entrywise product is $\sum_{i, j} (u_i \circ w_j)(u_i \circ w_j)^*$. Induction on $|P|$ gives the finite product, and the empty product is the kernel $1$, which is $\mathbf{1}\mathbf{1}^*$. For rule 2, order $P$ as $p_1, \dots, p_n$. Then
$$\prod_{i} K_{p_i} - \prod_{i} k_{p_i} = \sum_{j = 1}^{n} \Big(\prod_{i < j} K_{p_i}\Big)\, (K_{p_j} - k_{p_j})\, \Big(\prod_{i > j} k_{p_i}\Big),$$
since the sum telescopes. Each $K_p = k_p + (K_p - k_p)$ is a sum of two positive semidefinite kernels, so it is positive semidefinite. Each term of the sum is then a Schur product of positive semidefinite kernels, and a sum of positive semidefinite kernels is positive semidefinite. Rules 3 and 4 say that $D A D^*$ is positive semidefinite for a diagonal matrix $D$: the form of $D A D^*$ at $c$ is the form of $A$ at $D^* c$. For rule 5, the form at $c$ splits as a sum over $b \in \beta$ of the form of $k$ on the fibre over $b$ at the restriction of $c$, and each term is nonnegative. $\square$

Rule 2 is the tool for comparison. If a kernel $K$ dominates a kernel $k$ at each place of a product, the product of the $K$ dominates the product of the $k$. In [Theorem A](/entry/theorem-a-after/) the leading term of the energy is compared in this way.

**Theorem 3.1.4 (Local cores).** The following hold together.

1. The three forms of positivity of the Lemma agree.
2. The five closure rules of the Proposition hold.
3. The block kernel of a local field satisfies [the Gram and support property](/entry/second-gram-and-vanishing/): it is positive semidefinite on finite sets of points of equal size, and it vanishes off the ring condition.
4. The single block formula of [Theorem 3.2.10](/entry/first-kernel-explicit-formula/) holds, and the averaging identity of [Lemma 3.2.8](/entry/lattice-average-identity/) holds for the Gram kernel.
5. Twenty further statements about local systems of kernels hold: pullbacks of kernels at the local and top levels, unit heads, a global kernel built from local ones, a uniform majorant, the axioms of a kernel system built from local systems and from families, positivity of local kernels, two domination statements, a base kernel equal to $1$, a Parseval identity and a theta identity for one block, the support and block diagonal form of the normalized kernel, and the assembly of the main kernel lemma.

Lean: `Formalism.FourierDecayAlt.P.HilbertSchmidtNorm.localCores`.

*Proof.* Each item is proved separately, and the theorem is their conjunction. Items 1 and 2 are the Lemma and the Proposition above. Item 3 is [Theorem 3.2.6](/entry/second-gram-and-vanishing/) of Section 2, and item 4 is [Theorem 3.2.10](/entry/first-kernel-explicit-formula/) of Section 2 and an averaging statement proved from the Gram property. The statements of item 5 are proved by the results that the Remark below names. $\square$

**Remark 3.1.5 (Formalization).** `localCores` is a 32-tuple proving `PB.LocalCores` ([StatementPB.lean](lean:Formalism/HermitianCurvature/StatementPB.lean#L337)); its entries are second names in the namespace `Formalism.FourierDecayAlt.Final`, such as `jx_schurProduct`, `gram_determinant_dual_bound_a` and `latticeAverage_of_gram`. The closure rules are `SchurProduct`, `ProductDomination`, `DiagScale`, `DiagPhase` and `BlockDiagPSD` in [StatementJ.lean](lean:Formalism/HermitianCurvature/StatementJ.lean#L617), and the three forms of positivity are `TB.PSDOn` (Mathlib's `Matrix.PosSemidef`), `TA.PSDOn` and `A5.IsPSD`, compared by `PSDAgree` at line 19. We opened the statements of items 1 to 4. We did not unfold the twenty statements of item 5 (`ProductLemma`, `ScaleOk`, `PhaseOk`, `OutsideSysOk` and the others), so item 5 only paraphrases their names. The namespace `HilbertSchmidtNorm` and the file name SecondDerivativeHolds.lean say nothing about this content, and the file ends with an empty namespace block.
