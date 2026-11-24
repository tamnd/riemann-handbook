---
title: Gram fibres and the hyperbolic stage
decls:
  - GlobalTheory.CompanionTheory.WeilSiegel.HypStage.local_stages
  - GlobalTheory.T.zero_block_coefficient_induction_left
  - GlobalTheory.CompanionTheory.WeilSiegel.HypMass.HH.mass_isotropic
  - GlobalTheory.T.zero_block_coefficient_induction_right
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Gram fibres and the hyperbolic stage

This section sets up the measures on frames that the chapter uses, and it proves two local facts about the frames of the zero matrix in a space with a hyperbolic plane added. The first fact splits an integral over isotropic $(n+1)$-frames into an integral over one isotropic vector and an integral over $n$-frames in the smaller space. The second fact says that the local masses of the zero fibre are finite and tend to 1 fast enough for an Euler product to converge. Both facts are inputs to the induction on the rank in [the hyperbolic step](/entry/hyp-step/), which is the base of the singular case of the Siegel-Weil formula in the next section.

We fix the setting for the whole chapter. Let $F$ be a number field and let $E/F$ be a CM extension of number fields with nontrivial automorphism $\sigma$ over $F$. Let $M \ge 1$ and let $J$ be an $M \times M$ matrix over $E$ that is Hermitian ($\sigma(J_{ba}) = J_{ab}$) and nondegenerate ($\det J \ne 0$). It defines the [[Hermitian form|8NJ7XY6F1S]] $h_J(x, y) = {}^t x^\sigma J y$ on $E^M$, see [Hermitian forms](/learn/algebra/#hermitian-and-skew-hermitian-forms). For an $F$-algebra $R$ we write $R_E = R \otimes_F E$ and we extend $h_J$ to $R_E^M$.

**Definition 4.1.1 (Gram matrix and frames).** Let $X = (x_1, \dots, x_n)$ be an $n$-tuple of vectors in $R_E^M$. Its Gram matrix is the $n \times n$ Hermitian matrix $\operatorname{gr}(X) = (h_J(x_a, x_b))_{a,b}$. For an $n \times n$ Hermitian matrix $T$ over $E$, the set of frames of $T$ is
$$\operatorname{Fr}_J(T) = \{ X \in (E^M)^n : x_1, \dots, x_n \text{ linearly independent}, \ \operatorname{gr}(X) = T \}.$$

The Siegel-Weil formula compares an average of a theta function with an Eisenstein series. The theta side sums a function over the frames of $T$. To compute the average we need a measure on each fibre of the map $\operatorname{gr}$, and the next definition says what such a family of measures is. Write $\operatorname{Herm}_n(R)$ for the Hermitian $n \times n$ matrices over $R_E$.

**Definition 4.1.2 (Gram fibre family).** Let $\mu$ be a measure on $(R_E^M)^n$, let $\nu$ be a measure on $\operatorname{Herm}_n(R)$, let $U \subseteq (R_E^M)^n$ and let $B \subseteq \operatorname{Herm}_n(R)$. A family $(m(\beta))_{\beta}$ of measures on $(R_E^M)^n$ is a fibre family for $\operatorname{gr}$ over $U$ and $B$ if three conditions hold.

1. Each $m(\beta)$ is concentrated on $\operatorname{gr}^{-1}(\beta) \cap U$.
2. For each measurable $\varphi \ge 0$,
$$\int_U \varphi \, d\mu = \int_{\operatorname{Herm}_n(R)} \int \varphi \, dm(\beta) \, d\nu(\beta).$$
3. For each continuous $\varphi$ with compact support in $U$ and each $\beta \in B$, the function $\varphi$ is $m(\beta)$-integrable, and $\beta \mapsto \int \varphi \, dm(\beta)$ is continuous on $B$.

The family is free if $U$ is the set of linearly independent tuples and $B$ is all of $\operatorname{Herm}_n(R)$. It is nondegenerate if $U$ is the set of $X$ with $\operatorname{gr}(X)$ invertible and $B$ is the set of invertible Hermitian matrices.

Condition 2 is a disintegration of $\mu$ along $\operatorname{gr}$, and condition 3 makes the fibre integrals continuous in the base point. The free form allows the degenerate matrix $\beta = 0$, which is the case of this section.

The measures $\mu$ and $\nu$ are fixed by a basis. Let $b = (b_1, \dots, b_d)$ be a basis of $E$ over $F$ and let $\lambda$ be a measure on $R$. The coordinate measure on $(R_E^M)^n$ is the product of copies of $\lambda$ through the coordinates in the basis $b$. The coordinate measure on $\operatorname{Herm}_n(R)$ is the product of $\lambda$ on the half traces of the diagonal entries and of the coordinate measure on the entries above the diagonal. We use these two measures for $\mu$ and $\nu$ throughout.

**Definition 4.1.3 (Standard local measure).** Let $v$ be a finite place of $F$ with ring of integers $\mathcal{O}_v$. A measure $\lambda_v$ on $F_v$ is standard if it is an additive [[Haar measure|CE0V9686M8]] and $\lambda_v(\mathcal{O}_v) = 1$. We write $L_v \subseteq (F_v \otimes_F E)^{M \times n}$ for the set of tuples whose coordinates in the basis $b$ lie in $\mathcal{O}_v$.

**Definition 4.1.4 (Hyperbolic extension).** The hyperbolic extension of $J$ is the $(M+2) \times (M+2)$ matrix
$$J^{+} = \begin{pmatrix} H & 0 \\ 0 & J \end{pmatrix}, \qquad H = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}.$$
The vector $e_0 = (1, 0, \dots, 0)$ of $E^{M+2}$ is isotropic for $h_{J^+}$.

So $h_{J^+}$ is the orthogonal sum of a [[hyperbolic plane|1X5PZSK44P]] and $h_J$. For $a = (a_1, \dots, a_n) \in R_E^n$ and $Y = (y_1, \dots, y_n) \in (R_E^M)^n$ put
$$c(a, Y) = \bigl(e_0, (a_1, 0, y_1), \dots, (a_n, 0, y_n)\bigr) \in (R_E^{M+2})^{n+1}.$$
Since $h_{J^+}(e_0, (a_j, 0, y_j))$ is the second coordinate of $(a_j, 0, y_j)$, which is 0, the Gram matrix of $c(a, Y)$ is $0 \oplus \operatorname{gr}(Y)$. So $c(a, Y)$ lies in the zero fibre when $Y$ does. This is the shape of an isotropic frame after a change of basis that moves its first vector to $e_0$.

**Definition 4.1.5 (Stage integral).** Let $U_{J^+}(R)$ be the unitary group of $h_{J^+}$ over $R_E$, see [unitary groups](/learn/groups/#unitary-groups). Let $m'$ be a measure on $(R_E^M)^n$ and $\varphi \ge 0$ a measurable function on $(R_E^{M+2})^{n+1}$. For $g \in U_{J^+}(R)$ the stage integral is
$$\operatorname{St}_{m'}(\varphi)(g) = \int \int \varphi\bigl(g \cdot c(a, Y)\bigr) \, d\mu_{1,n}(a) \, dm'(Y),$$
where $\mu_{1,n}$ is the coordinate measure on $R_E^n$.

We now work over a local ring. We say that a commutative topological $F$-algebra $R$ is a local coefficient ring if it is a Hausdorff, second countable, locally compact topological ring, it is Artinian and reduced (so a finite product of fields), the inclusion of $R^\times$ in $R$ is an open embedding, and some open subgroup of $R^\times$ has an open squaring map. The completions $F_v$ are examples.

**Theorem 4.1.6 (Local stages).** Let $E/F$ be CM, let $J$ be Hermitian and nondegenerate of size $M$, and let $1 \le n$ with $2n < M$. Let $R$ be a local coefficient ring, $b$ a basis of $E/F$ and $\lambda$ an additive Haar measure on $R$. Let $m$, $m_1$ and $m'$ be free Gram fibre families for the coordinate measures: $m$ for $J^+$ in rank $n+1$, $m_1$ for $J^+$ in rank 1, and $m'$ for $J$ in rank $n$. Then for each measurable $\varphi \ge 0$ on $(R_E^{M+2})^{n+1}$ there is a measurable $\Psi \ge 0$ on $R_E^{M+2}$ such that $\Psi(g e_0) = \operatorname{St}_{m'(0)}(\varphi)(g)$ for all $g \in U_{J^+}(R)$, and
$$\int \varphi \, dm(0) = \int \Psi \, dm_1(0).$$

Lean: `GlobalTheory.CompanionTheory.WeilSiegel.HypStage.local_stages` (also `GlobalTheory.T.zero_block_coefficient_induction_left`, a second name).

*Proof.* The group $U_{J^+}(R)$ preserves the coordinate measures and the Gram map, so it preserves each fibre measure $m(0)$ and $m_1(0)$, by the uniqueness part of a disintegration. These measures are also sigma-finite. A local form of Witt's theorem moves each nonzero isotropic vector of $R_E^{M+2}$ to $e_0$ by an element of $U_{J^+}(R)$, and a unit vector can be moved in the same way. So the nonzero isotropic vectors form one orbit $U_{J^+}(R) e_0$. Define $\Psi$ on this orbit by $\Psi(g e_0) = \operatorname{St}_{m'(0)}(\varphi)(g)$. This is well defined: the stabiliser of $e_0$ acts on the pairs $(a, Y)$ by maps that preserve $\mu_{1,n} \times m'(0)$, so the stage integral depends only on $g e_0$. Next, an isotropic frame $X$ of rank $n+1$ is $g \cdot c(a, Y)$ with $g e_0 = x_1$. The local integral formula over the Gram fibre then computes $\int \varphi \, dm(0)$ as the integral over $x_1$ against $m_1(0)$ of the integral over the rest of the frame, and the uniqueness of a fibre family up to null sets identifies the inner integral with $\Psi(x_1)$. An orbit integral argument for invariant measures on $U_{J^+}(R) e_0$ gives the equality of the two integrals. $\square$

The second theorem is global in the place. Recall that the norm $q_v$ of a finite place $v$ is the order of its residue field. For $s \ge 2$ let $\zeta_v(s) = (1 - q_v^{-2s})^{-1}$ if $F_v \otimes_F E$ is a field, and $\zeta_v(s) = (1 - q_v^{-s})^{-2}$ if not.

**Theorem 4.1.7 (Masses at the isotropic stage).** Let $E/F$ and $J$ be as above, with $1 \le n$ and $2n < M$. Fix a basis $b$ of $E/F$ and standard measures $\lambda_v$ at all finite places. For each finite $v$ let $m_v$, $m_{1,v}$ and $m'_v$ be free Gram fibre families as in the theorem on local stages, over $R = F_v$. Assume that $m_{1,v}(0)(L_v) < \infty$ and $m'_v(0)(L_v) < \infty$ for all $v$, and that
$$\sum_v \bigl| m_{1,v}(0)(L_v) - 1 \bigr| < \infty, \qquad \sum_v \bigl| m'_v(0)(L_v) - 1 \bigr| < \infty.$$
Then $m_v(0)(L_v) < \infty$ for all $v$, and $\sum_v | m_v(0)(L_v) - 1 | < \infty$.

Lean: `GlobalTheory.CompanionTheory.WeilSiegel.HypMass.HH.mass_isotropic` (also `GlobalTheory.T.zero_block_coefficient_induction_right`, a second name).

*Proof.* Finiteness holds at each place by a direct bound: the zero fibre measure of the lattice is finite for a free fibre family when $2(n+1) < M+2$. For the sum, put $x_v = m'_v(0)(L_v)$, $y_v = m_{1,v}(0)(L_v)$ and $z_v = m_v(0)(L_v)$. For all but finitely many $v$ the local computation of the stages gives
$$z_v = \tau_v \, p_v \, \zeta_v(M+1-n), \qquad y_v = p_v \, \zeta_v(M+1),$$
where $p_v$ is the $m_{1,v}(0)$-measure of the primitive isotropic vectors $g e_0$ with $g$ in the stabiliser of the lattice, and $\tau_v$ is the stage factor, which equals $x_v$ at these places. Since $M + 1 - n \ge 2$, we have $1 \le \zeta_v(s) \le 1 + 4 q_v^{-2}$ for both exponents. An elementary estimate then gives, at the places where $|y_v - 1| < 1$,
$$|z_v - 1| \le 4 |x_v - 1| + 8 q_v^{-2} + |y_v - 1|.$$
The right side is summable: the first and last terms by hypothesis, and the middle term because $\sum_v q_v^{-2}$ converges for a number field. The inequality fails only at finitely many places, so $\sum_v |z_v - 1|$ converges. $\square$

**Remark 4.1.8 (Formalization).** Both theorems carry three proofs that the zero matrices of sizes $n$, $n+1$ and 1 are Hermitian, and nothing else depends on them. The names with "zero block coefficient" are second names stated by `first | exact` ([ZeroBlockCoefficientInductionLeftStatement.lean](lean:Development/WeilBound/RepresentationTheoryGL/SiegelWeil/ArchimedeanSiegelWeil/PlaceIntegrals/ZeroBlockCoefficientInductionLeftStatement.lean#L7)); they are statements about frame measures, not about Fourier coefficients. The function $\zeta_v$ treats a ramified place as a field place ([IsContent.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/IsContent.lean#L26)). The places are the height one primes of $\mathcal{O}_F$, so only finite places occur here.
