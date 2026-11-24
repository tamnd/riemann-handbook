---
title: The mass of the components
decls:
  - MainStatements.Tam.Plug.comp
  - MainStatements.Tam.comp
  - MainStatements.Tam.C.sum_muF_le
  - MainStatements.Tam.Plug.tube0
  - MainStatements.Tam.tube
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The mass of the components

This section proves an explicit upper bound for the total volume of the components of a unitary Shimura variety of level $M$. The volumes are the covolumes of the arithmetic groups of the components in the real special unitary group, measured by the Riemannian Haar measure of an orthonormal frame. The bound is a product of a power of $M$, a power of $15$ and a mass term that depends only on the CM field and the rank. It is used by the [local volume factor](/entry/tamagawa-local-volume-factor/), where the bound becomes a factor of the constant in the comparison of the sup norm with the Petersson norm. The volumes here are the hermitian volumes of the base; they are the archimedean side of the [arithmetic volumes](/learn/arakelov/#arithmetic-volume-and-bigness) of the earlier sections.

Let $D$ be a datum with CM field $E$, maximal real subfield $F$, $d = [E : \mathbb{Q}] = 2f$, and rank $r \ge 2$. Let $V$ be a hermitian space of $D$, with Gram matrix $G$, a self dual lattice $L$ and its closure $\hat{L}$ in the finite adeles. We write $G(\mathbb{A})$ for the adelic unitary group of $V$ and $G(\mathbb{Q})$ for its rational points, a discrete subgroup.

**Definition 9.14.1 (Stabilizer and level groups).** The stabilizer $\mathrm{Stab}(V)$ is the set of $h \in G(\mathbb{A})$ whose finite part maps $\hat{L}$ onto itself. For an integer $M \ge 1$, the group $K_M$ is the set of $h$ whose finite part is a unitary matrix that preserves $L$ and is congruent to the identity modulo $M$ on $L$.

**Definition 9.14.2 (The mass terms).** Let $\mathrm{vol}(U_r)$ be the volume of the compact unitary group of rank $r$ in the normalization of the chapter, and let $\mathrm{mass}_I(D, r)$ be the mass of the standard lattice of rank $r$. Put

$$
\begin{aligned}
m_B(E, r) &= \Big(3\, d^2 r^4\, |\mathrm{disc}\, E|^{2/d}\Big)^{3 d r^2}, \\
m_2(E, r, M) &= M^{d r^2}\, 15^{d r^2}\, m_B(E, r).
\end{aligned}
$$

The four statements below are the inputs of the tube bound. They are proved elsewhere in the development.

1. The volume statement. For a Haar measure $\mu$ on $G(\mathbb{A})$, a fundamental domain $\mathcal{F}$ of $G(\mathbb{Q})$, a family of infinite places, frames $A$, measures $m_\rho$ on the real factors $U(p, q)$ with the normalization of the chapter, a continuous real part map $\mathrm{rp}$ from $G(\mathbb{A})$ to the product of the real factors, and every measurable set $B$ of that product,

$$
\mu(\mathcal{F})\, \Big(\prod_\rho m_\rho\Big)(B) = \mu\big(\mathrm{Stab}(V) \cap \mathrm{rp}^{-1}(B)\big)\, \mathrm{vol}(U_r)^f\, \mathrm{mass}_I(D, r).
$$

2. The stabilizer statement. $\mathrm{Stab}(V) = K_1$, each $K_M$ with $M \ge 1$ is open, and the level groups of the links of a datum lie in the stabilizer.
3. The index statement. For a self dual lattice of rank $r$ over $E$ and $M \ge 1$ there is a finite set $S$ with at most $M^{2 f r^2}$ elements, in the normalization of the field degree used there, such that every $g \in K_1$ is $s k$ with $s \in S \cap K_1$ and $k \in K_M$.
4. The numerical statement. For $r \ge 2$,

$$
r^{-r^2} \le \mathrm{vol}(U_r) \le 13^{r^2}.
$$

**Definition 9.14.3 (The tube statement).** The tube statement says: for $V$ of signature $(P, Q)$ at every real place, rank $r \ge 2$, an integer $M \ge 3$, a finite family of data $X_k$ with adelic elements $g_k$ that are pairwise inequivalent modulo $K_M$, such that each $X_k$ has the Gram matrix $-G^{T}$, the CM type of $D$, the lattice translated from $L$ by the finite part of $g_k$, the principal congruence group of level $M$ as its arithmetic group $\Gamma_k$, and an orthonormal frame $x_k$, the covolumes satisfy

$$
\sum_k \mathrm{covol}\big(\Gamma_k \backslash SU_k(\mathbb{R}), x_k\big) \le 16^{f r^2}\, M^{2 f r^2}\, \mathrm{vol}(U_r)^f\, \mathrm{mass}_I(D, r).
$$

Here $SU_k(\mathbb{R})$ is the real special unitary group of $X_k$ and the measure is the Riemannian Haar measure of the frame $x_k$.

**Theorem 9.14.4 (Tube bound).** The volume, stabilizer and index statements imply the tube statement.

Lean: `MainStatements.Tam.tube` (also `MainStatements.Tam.Plug.tube0`, a second name)

*Proof.* Fix a Haar measure $\mu$ on $G(\mathbb{A})$, which is locally compact and second countable, and a fundamental domain $\mathcal{F}$ of $G(\mathbb{Q})$. Choose a family of infinite places, frames $A$, measures $m_\rho$ and a continuous real part map $\mathrm{rp}$ as in the volume statement. Identify all $X_k$ with one flag domain $X_0$ and one orthonormal frame $x_0$. The covolume does not depend on the orthonormal frame, so each covolume can be computed on $X_0$ with the frame $x_0$.

For each $k$ choose a packing set $F_k$ in the real special unitary group whose measure is at least the covolume of $\Gamma_k$ and whose translates by $\Gamma_k$ are disjoint. Let $\pi$ be the continuous projection of the product of the real factors to the determinant one factor, and put

$$
B_k = \pi^{-1}(F_k) \cap \{ b : \mathrm{Im} \det b_{\rho_0} > 0 \}
$$

for a fixed real place $\rho_0$. Write $g_k$ with a finite part $g'_k$, and form the tubes

$$
T_k = \{ y \in G(\mathbb{A}) : g_k'^{-1} y \in K_M,\ \mathrm{rp}(y) \in B_k \}.
$$

These are measurable, since $K_M$ is open. The disjointness lemma for tubes shows that $\gamma T_k$ meets $T_{k'}$ for $\gamma \in G(\mathbb{Q})$ only if $\gamma = 1$ and $k = k'$. Hence the $T_k$ are disjoint, the union $S$ of the $T_k$ has disjoint translates under $G(\mathbb{Q})$, and

$$
\sum_k \mu(T_k) = \mu(S) \le \mu(\mathcal{F}).
$$

By translation, $\mu(T_k)$ is the measure of $K_M \cap \mathrm{rp}^{-1}(B_k)$. With $\mathrm{Stab}(V) = K_1$ and the index statement,

$$
\mu\big(\mathrm{Stab}(V) \cap \mathrm{rp}^{-1}(B_k)\big) \le M^{2 f r^2}\, \mu(T_k).
$$

The archimedean mass bound gives

$$
16^{-f r^2}\, \mathrm{vol}_{x_0}(F_k) \le \Big(\prod_\rho m_\rho\Big)(B_k).
$$

Put $c = \mathrm{vol}(U_r)^f\, \mathrm{mass}_I(D, r)$. It is positive, since $\mathrm{vol}(U_r)$ is a product of positive numbers and the mass is positive. The measure $\mu(\mathcal{F})$ is finite. It is not zero: the volume statement with $B$ the whole product gives $\mu(\mathcal{F})$ times a positive number equal to $\mu(K_1)\, c$, and $K_1$ is open and contains $1$, so $\mu(K_1) > 0$. Multiply the volume statement for $B_k$ and sum over $k$:

$$
\begin{aligned}
\mu(\mathcal{F}) \sum_k \Big(\prod_\rho m_\rho\Big)(B_k) &= c \sum_k \mu\big(\mathrm{Stab}(V) \cap \mathrm{rp}^{-1}(B_k)\big) \\
&\le c\, M^{2 f r^2} \sum_k \mu(T_k) \le c\, M^{2 f r^2}\, \mu(\mathcal{F}).
\end{aligned}
$$

Divide by $\mu(\mathcal{F})$. Then

$$
\sum_k \mathrm{covol}_k \le \sum_k \mathrm{vol}_{x_0}(F_k) \le 16^{f r^2} \sum_k \Big(\prod_\rho m_\rho\Big)(B_k) \le 16^{f r^2}\, M^{2 f r^2}\, c. \qquad \square
$$

The method is the classical one for mass formulas. The tubes are disjoint pieces of a fundamental domain, so their total measure is at most the volume of the quotient, and each tube is a product of a compact open piece at the finite places and a packing set at the real places.

**Theorem 9.14.5 (Sum of the volumes of fundamental sets).** Assume the tube statement. Let $V$ be a hermitian space of rank $r \ge 2$ and signature $(P, Q)$, let $X_k$ be a finite family of data, and let a dictionary from $G(\mathbb{A})$ to the frames of the $X_k$ be uniform for an open subgroup $K_f$ of level $M \ge 3$ and infinite embeddings $\theta$. Assume that each $X_k$ is a model of $V$ and has the CM type of $D$. For orthonormal frames $x_k$ and fundamental sets $F_k$ of the $X_k$,

$$
\sum_k \mu_k(F_k) \le 16^{f r^2}\, M^{2 f r^2}\, \mathrm{vol}(U_r)^f\, \mathrm{mass}_I(D, r).
$$

Lean: `MainStatements.Tam.C.sum_muF_le`

*Proof.* The uniform dictionary gives adelic representatives $g_k$ of the components. For each $k$ there is a lattice $\Lambda_k$ of rational vectors in the adelic translate of $L$ by the finite part of $g_k$, and there are data $X'_k$ with the lattice $\Lambda_k$ and the principal congruence group of level $M$. Each $X'_k$ has an orthonormal frame $y_k$ and a fundamental set $F'_k$ of finite measure. Conjugation by the real unitary matrices of $g_k$ at the infinite embeddings maps the arithmetic group of $X_k$ onto that of $X'_k$, in both directions, and preserves the Gram matrix. So

$$
\mu_k(F_k) = \mu'_k(F'_k).
$$

The representatives give distinct double cosets, so they are pairwise inequivalent modulo $K_M$. The elements of a principal congruence group of level $M \ge 3$ have determinant $1$. Hence the covolume of the arithmetic group of $X'_k$ in the real special unitary group equals $a\, \mu'_k(F'_k)$, with

$$
a = \Big(2^{r(r - 1)/2}\, (2\pi)^{r - 1}\, \sqrt{r}\Big)^{n_E}
$$

for the field degree $n_E$ used there. Each factor is at least $1$, so $a \ge 1$ and $\mu'_k(F'_k)$ is at most the covolume. The tube statement for the $X'_k$ bounds the sum of the covolumes. $\square$

**Theorem 9.14.6 (Components of a level).** Assume the tube statement and the numerical statement. Let $D$ be a datum, $H$ a host, $l$ a level with integer $M$, $X_o$ a family of moduli spaces, $c$ a coefficient field and $U$ the uniformizations of the components, with a dictionary that satisfies the laws of the chapter. Then for every good embedding $\sigma$ of the coefficient field, all orthonormal frames $x_k$ and fundamental sets $F_k$ of the components $X_k$ of $U_\sigma$,

$$
\sum_k \mu_k(F_k) \le m_2(E, r, M).
$$

Lean: `MainStatements.Tam.comp`

*Proof.* The laws give the open subgroup $K_f$, the embeddings, the uniform dictionary and the models for $\sigma$. The CM type condition on each component follows from the uniformization and the fixed field of the host, and $r \ge 2$ holds for every datum. The previous theorem applies to the space $W_j$ of the datum and gives the bound

$$
16^{f r^2}\, M^{2 f r^2}\, \mathrm{vol}(U_r)^f\, \mathrm{mass}_I(D, r).
$$

The numerical statement gives $0 \le \mathrm{vol}(U_r) \le 13^{r^2}$, so $\mathrm{vol}(U_r)^f \le 13^{f r^2}$. The mass of the standard lattice is at most $m_B(E, r)$. With $d = 2f$, $M^{2 f r^2} = M^{d r^2}$ and $15^{d r^2} = 225^{f r^2}$. Since $16 \cdot 13 = 208 \le 225$,

$$
16^{f r^2}\, M^{d r^2}\, 13^{f r^2}\, m_B(E, r) \le M^{d r^2}\, 15^{d r^2}\, m_B(E, r) = m_2(E, r, M). \qquad \square
$$

**Theorem 9.14.7 (Mass of the components).** The bound of the previous theorem holds with no hypotheses.

Lean: `MainStatements.Tam.Plug.comp`

*Proof.* The volume, stabilizer, index and numerical statements are proved. The tube bound turns the first three into the tube statement, and the previous theorem applies. $\square$

The bound grows like a power of $M$ of exponent $d r^2$, which is the dimension count of the index of $K_M$ in $K_1$. The term $m_B(E, r)$ is a power of the root discriminant of $E$ with exponent of order $d r^2$, so the logarithm of $m_2$ is of order $d r^2$ times the logarithm of $d$, $r$, $M$ and the root discriminant.

**Remark 9.14.8 (Formalization).** The theorem with no hypotheses is the term `comp (tube0 vol stab idx) num` in [Imports.lean](lean:Development/WeilBound/RepresentationTheoryGL/TubeMeasures/DisjointTubes/ConstantSupremum/Imports.lean#L17); the file is named `Imports` but holds four such theorems, `up`, `low`, `comp` and `size`. `MainStatements.Tam.Plug.tube0` has the type of `MainStatements.Tam.tube` and the proof `MainStatements.Tam.tube` ([Tube0.lean](lean:Development/WeilBound/RepresentationTheoryGL/TubeMeasures/DisjointTubes/ConstantSupremum/Tube0.lean#L3)). In `MainStatements.Tam.comp` the lower half of the numerical statement is used only to get $\mathrm{vol}(U_r) \ge 0$ ([SumMuFLe.lean](lean:Development/WeilBound/RepresentationTheoryGL/TubeMeasures/DisjointTubes/MeasureSumBounds/SumMuFLe.lean#L131)), and the sign of the mass is handled by a case split on its sign (line 140), while the tube bound proves both numbers positive directly ([CovolFrame.lean](lean:Development/WeilBound/RepresentationTheoryGL/TubeMeasures/DisjointTubes/FrameCovolume/CovolFrame.lean#L170)). The field degree in the index statement and in the constant $a$ is a separate function of $E$; our reading is that it equals $f$, but we have not unfolded it. We have not unfolded the laws, the uniform dictionary, the disjointness lemma for tubes, the archimedean mass bound or the volume statement; their descriptions above follow their statements.
