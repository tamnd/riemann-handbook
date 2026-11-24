---
title: A quantitative Mahler criterion
decls:
  - GlobalTheory.htMin_of_reduced
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A quantitative Mahler criterion

Mahler's criterion says that a set of lattices in $\mathbb{R}^N$ of bounded covolume is relatively compact if and only if there is a uniform lower bound for the lengths of their nonzero vectors. This section proves a quantitative form for a unitary group over a CM field. If an element $y$ of the archimedean group has no short integral vectors, then a rational unitary element with bounded finite part moves $y$ to a point whose entries are bounded by a power of the inverse of the bound. The estimate controls the growth of automorphic functions near the cusps in the step [every character of the row](/step/every-character-of-row/). For the setting see [quotients of finite volume](/learn/groups/#quotients-of-finite-volume) and [unitary groups](/learn/groups/#unitary-groups).

**Definition 7.6.1 (Unitary instance).** A unitary instance consists of: a CM extension $E/F$ of number fields; a nondegenerate Hermitian matrix $J \in M_n(E)$; a self-dual $\mathcal{O}_E$-lattice $L \subset E^n$ that spans $E^n$; for each infinite place $v$ of $F$ a signature $\varepsilon_v \in \{\pm 1\}^n$, an embedding $\varphi_v \colon E \to \mathbb{C}$ above $v$ and an invertible matrix $P_v$ with $P_v^{*}\, \varphi_v(J)\, P_v = J_{\varepsilon_v}$, the diagonal matrix of the signs; and a group topology on $G_f = U(J)(\mathbb{A}_f)$ whose basic neighbourhoods of $1$ are the principal congruence subgroups of $L$. Put $G_\infty = \prod_v U(J_{\varepsilon_v})$.

Each rational $\gamma \in U(J)(E)$ gives a point of $G_\infty \times G_f$: the archimedean component at $v$ is $P_v^{-1} \varphi_v(\gamma) P_v$, and the finite component is $\gamma$. We call this point the diagonal image of $\gamma$.

**Definition 7.6.2 (Short vectors).** A vector $u \in E^n$ is integral if all its coordinates are in $\mathcal{O}_E$. For $y \in G_\infty$ and $u \in E^n$ put

$$\begin{aligned} \vec{y}(u) &= \bigl(y_v^{-1} P_v^{-1} \varphi_v(u)\bigr)_v \in \prod_v \mathbb{C}^n. \end{aligned}$$

For $t > 0$ we say that $y$ has no $t$-short vectors if $\| \vec{y}(u) \| \geq t$ for every nonzero integral $u$.

The vectors $\vec{y}(u)$ for integral $u$ form a lattice in $\prod_v \mathbb{C}^n \cong \mathbb{R}^{N}$, with $N = 2n[F : \mathbb{Q}]$. Its covolume does not depend on $y$, since each $y_v$ is unitary for a form of signature $\varepsilon_v$ and so has determinant of absolute value $1$. The condition "no $t$-short vectors" is the condition of Mahler's criterion for this family of lattices.

**Theorem 7.6.3 (Quantitative Mahler criterion).** For every unitary instance there are an integer $b \geq 0$, a constant $C$ and a compact set $K \subset G_f$ with the following property. Let $y \in G_\infty$ and $0 < t \leq 1$, and assume that $y$ has no $t$-short vectors. Then there is $\gamma \in U(J)(E)$ with integral entries and integral inverse, whose diagonal image $(\gamma_\infty, \gamma_f)$ has $\gamma_f \in K$ and

$$\begin{aligned} \bigl| \bigl((\gamma_\infty y)_v\bigr)_{i j} \bigr|\, t^{b} &\leq C \quad \text{for all } v, i, j. \end{aligned}$$

Lean: `GlobalTheory.htMin_of_reduced`.

*Proof.* We use four inputs.

1. Reduced bases. There are $N$, $R$ and $C_0$ such that for every $y \in G_\infty$ there is a $\mathbb{Z}$-basis $e_1, \dots, e_N$ of $\mathcal{O}_E^n$ of type bounded by $R$ with $\| \vec{y}(e_j) \|\, t^{N} \leq C_0$ for all $j$, whenever $0 < t \leq 1$ and $y$ has no $t$-short vectors. Here the type is bounded by $R$ if multiplication by the elements of an integral basis of $\mathcal{O}_E$ has integer coefficients of size at most $R$ in the basis $e$, and the trace form has entries of size at most $R$ on $e$.
2. Finiteness. There is a finite set $\mathcal{S}$ of $\mathbb{Z}$-bases of $\mathcal{O}_E^n$ such that every basis of type bounded by $R$ has the form $e_j = \gamma^{-1} e^{0}_j$ for some $e^{0} \in \mathcal{S}$ and some $\gamma \in U(J)(E)$ with integral entries and integral inverse. This is the finiteness of classes of bounded type under the integral unitary group.
3. Compactness. There is a compact $K \subset G_f$ that contains the finite component of the diagonal image of every $\gamma \in U(J)(E)$ with integral entries and integral inverse.
4. Spanning. For each $\mathbb{Z}$-basis $e^0$ of $\mathcal{O}_E^n$ the vectors $\vec{1}(e^0_l)$ span $\prod_v \mathbb{C}^n$ over $\mathbb{R}$, because $\mathcal{O}_E^n$ is a lattice of full rank there. So each standard basis vector $\epsilon_{v, i}$ is a real combination $\sum_l c_l\, \vec{1}(e^0_l)$, and since $\mathcal{S}$ is finite there is $M$ with $\sum_l |c_l| \leq M$ for all $e^0 \in \mathcal{S}$ and all $(v, i)$.

Now let $y$ have no $t$-short vectors. Take the reduced basis $e$ of input 1. By input 2 write $e = \gamma^{-1} e^0$ with $e^0 \in \mathcal{S}$. By input 3, $\gamma_f \in K$. Since $(\gamma_\infty)_v = P_v^{-1} \varphi_v(\gamma) P_v$,

$$\begin{aligned} \vec{\gamma_\infty y}(e^0_l) &= y^{-1} \gamma_\infty^{-1} P^{-1} \varphi(\gamma e_l) = \vec{y}(e_l). \end{aligned}$$

Write $z = \gamma_\infty y$. Apply $z_v^{-1}$ to the expansion of $\epsilon_{v, i}$ in input 4. Since $z_v^{-1}$ is linear, the $j$-th entry of the column $z_v^{-1} \epsilon_{v, i}$ satisfies

$$\begin{aligned} \bigl| (z_v^{-1})_{j i} \bigr| &\leq \sum_l |c_l|\, \| \vec{z}(e^0_l) \| = \sum_l |c_l|\, \| \vec{y}(e_l) \|. \end{aligned}$$

Multiply by $t^N$ and use input 1: the right side is at most $M \max(C_0, 0)$. Finally, $z_v$ lies in $U(J_{\varepsilon_v})$ and $J_{\varepsilon_v}$ is diagonal with entries $\pm 1$, so $z_v^{-1} = J_{\varepsilon_v} z_v^{*} J_{\varepsilon_v}$ and $|(z_v)_{i j}| = |(z_v^{-1})_{j i}|$. This gives the bound with $b = N$ and $C = M \max(C_0, 0)$. $\square$

**Remark 7.6.4 (Formalization).** The exponent $b$ is the rank $N$ of the reduced basis given by `existsReducedBasisBoundedType_of_instance`. Short vectors are measured on $\mathcal{O}_E^n$, through the predicate `IntVec`, and not on the lattice $L$ of the instance; $L$ enters only through the topology of $G_f$ and so through the compact set $K$ ([IsRealCoord.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/IsRealCoord.lean#L17)). The four inputs are the lemmas `existsReducedBasisBoundedType_of_instance`, `integralVectorBases_bounded_finite_unitaryClasses`, `exists_compact_integral_unitary_finitePart` and `cusp_integralBasis_covolume_constant`, which are not unfolded here.
