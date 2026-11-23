---
title: A nonzero coefficient at a split point
decls:
  - GlobalTheory.FJDetect.exists_fj_ne_zero_at_split_point'
  - GlobalTheory.ArcDetect.exists_split
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A nonzero coefficient at a split point

Let $P$ be a cusp form on a Hermitian datum that does not lie in $\mathrm{SS}_{>c_1}$. Then some Fourier-Jacobi coefficient of $P$ of total order at most $c_1$ is not zero at some point of the domain. This section proves more: the point can be chosen so that the orthogonal complement of the isotropic vector splits into short lattice vectors that are adapted to the complex structure at the point, and so that the cusp of the vector has a controlled torsion index (Theorem (A nonzero coefficient at a split point)). This is the input that the next section needs to build a CM point from the frame. The bounds depend only on $r$, $E$, $c_1$, a size parameter $w$ and three integers of the datum, so they can be chosen uniformly in Corollary (Split points with the constants of the CM family).

We work with a Hermitian datum $X$ of rank $r$ over $E$ as in Section 1, with more data. There are an $\mathcal{O}_E$-lattice $L'$, natural numbers $g$, $N_A$, $N_C$ and $p_0$, and for each frame $x$ a complex structure $J_x$ on the complexified space. For an isotropic $\xi$ and a frame $x$ there is a projection $u_x(\xi, \cdot)$ to the complement of $\xi$, and there is a map $\mu \mapsto \mathrm{pr}_x(\xi, \mu)$ from a set $\Lambda_p(\xi)$ of vectors to the complexified space. We write $e\xi$ also for the image of $e\xi \in E^r$ in the complexified space. A weight $\lambda$ is *dominant* if it satisfies the dominance condition of the datum, and the *spread* of $\lambda$ at $\tau \in \Psi$ is the difference between its largest and its smallest entry.

**Definition 4.2.1 (Split data).** Let $\xi$ be isotropic, let $\Lambda_0 > 0$, let $x$ be a frame and let $\ell_1, \ldots, \ell_{r-2} \in E^r$. We say that $(\xi, \Lambda_0, x, \ell)$ is *split data* if:

1. each $\ell_i$ lies in $L'$ and $h(\ell_i, \xi) = 0$;
2. the vectors $\xi, \ell_1, \ldots, \ell_{r-2}$ are linearly independent over $E$;
3. $h(\ell_i, \ell_k) = 0$ when $i < p_0 - 1 \leq k$;
4. for $i < p_0 - 1$: $\mathrm{Re}\, \tau(h(\ell_i, \ell_i)) > 0$ for all $\tau \in \Psi$, and $J_x u_x(\xi, \ell_i) = i\, u_x(\xi, \ell_i)$;
5. for $i \geq p_0 - 1$: $\mathrm{Re}\, \tau(h(\ell_i, \ell_i)) < 0$ for all $\tau \in \Psi$, and $J_x u_x(\xi, \ell_i) = -i\, u_x(\xi, \ell_i)$;
6. $|\tau(h(\ell_i, \ell_i))| \leq \Lambda_0^2$ for all $i$ and all $\tau \in \Psi$.

So the complement of $\xi$ has a basis of short lattice vectors, orthogonal between the positive and the negative part, and each vector is an eigenvector of the complex structure at $x$ with the eigenvalue that its sign predicts. Section 3 builds a CM point from such data.

The constants are explicit functions. For $c_1 > 0$ and $w \geq 1$ there are positive reals $\varepsilon_0 = \varepsilon_0(g, d_E, f, N_A, N_C, c_1, w)$ (a flow bound), $r_h = r_h(c_1, w)$, $\Lambda_6 = \Lambda_6(r, p_0, f, d_E, \varepsilon_0, r_h)$ and $m_s = m_s(r, f, d_E, \mathrm{rd}_E, N_A, N_C, \varepsilon_0)$ (a frame index bound). We do not need their formulas, only that they depend on these arguments and nothing else.

**Theorem 4.2.2 (A nonzero coefficient at a split point).** Let $X$ be a Hermitian datum as above, $\lambda$ a dominant weight, $P$ a function on frames, and $c_1, w \in \mathbb{R}$. Assume:

1. $c_1 > 0$, $w \geq 1$, $\sum_{\tau} \mathrm{spread}_\tau(\lambda) \leq w$ and $r \leq w$;
2. $\chi_\lambda(\gamma) = 1$ for each $\gamma \in \Gamma$ with $\gamma v - v \in g\Lambda$ for all $v \in \Lambda$;
3. $P \in \mathrm{SS}(\lambda)$ and $P \notin \mathrm{SS}_{>c_1}(\lambda)$.

Then there are an isotropic $\xi$ and $\nu : \Psi \to \mathbb{R}$ with $\sum_\tau \nu_\tau \leq c_1$ and $\nu_\tau \geq 0$ for all $\tau$, such that the short vector conditions hold at some frame $z_0$, and such that for every integer $n' \geq 1000\, m_s / r_h$ there are a frame $x \in \mathcal{D}_X$ and vectors $\ell_1, \ldots, \ell_{r-2}$ with:

- $(\xi, \Lambda_6, x, \ell)$ is split data;
- for each $\mu \in \Lambda_p(\xi)$ there is $e \in E$ with $e\xi \in \Lambda$ and $n' \cdot \mathrm{pr}_x(\xi, \mu) = e\xi$;
- $\mathrm{FJ}_{\xi,\nu}(P)(x) \neq 0$.

Here the *short vector conditions* at $z_0$ are the hypotheses on $(X, \lambda, P, c_1, w)$ above, the facts $\sum_\tau \nu_\tau \leq c_1$ and $\mathrm{FJ}_{\xi,\nu}(P)(x_0) \neq 0$ for some $x_0 \in \mathcal{D}_X$, and two more: $z_0$ is a frame over a basis adapted to $\xi$, and the supremum of the normalized size $\hat{N}(\mathrm{FJ}_{\xi,\nu}(P))$ over all such frames is less than twice its value at $z_0$.

Lean: `GlobalTheory.FJDetect.exists_fj_ne_zero_at_split_point'`.

*Proof.* First we find the coefficient. Since $P \in \mathrm{SS}(\lambda)$ and $P \notin \mathrm{SS}_{>c_1}(\lambda)$, the definition of $\mathrm{SS}_{>c_1}$ gives an isotropic $\xi$, a $\nu$ with $\sum_\tau \nu_\tau \leq c_1$ and a point $x_0 \in \mathcal{D}_X$ with $\mathrm{FJ}_{\xi,\nu}(P)(x_0) \neq 0$.

Second, $\nu \geq 0$. A bounded section has a nonzero Fourier-Jacobi coefficient only at frequencies $\nu$ with all $\nu_\tau \geq 0$. This is the positivity of the coefficients of moderate growth, a lemma on the [Fourier expansion](/learn/automorphic-forms/#fourier-coefficients-and-whittaker-functions) of a bounded function along a cusp, which is proved outside this chapter.

Third, we choose $z_0$. A lemma on bounded sections, applied to $P$ and to the nonzero value $\mathrm{FJ}_{\xi,\nu}(P)(x_0)$, gives a frame $z_0$ over a basis adapted to $\xi$ at which $\hat{N}(\mathrm{FJ}_{\xi,\nu}(P))$ is more than half of its supremum over such frames. With this $z_0$ all the short vector conditions hold.

Fourth, we move from $z_0$ to a point of the domain with split data. This is a theorem on the geometry of the fundamental domain, proved outside this chapter. It takes as inputs the following results: a translate of the orthonormal flag of $z_0$ into the domain, a control of the chart norm on orthonormal frames, a statement on Fourier-Jacobi coefficients near their supremum (built from the holomorphic extension of periodic functions, a norm bound and the positivity of moderate coefficients), the Schwarz lemma on a ball, a bound for short orthonormal vectors that comes from a covering radius bound for CM lattices, and a move of the unitary complement by unipotent elements with a majorant bound. The output is, for each $n' \geq 1000\, m_s / r_h$, the frame $x$, the vectors $\ell_i$ with split data for $\Lambda_6$, the torsion condition with $n'$, and $\mathrm{FJ}_{\xi,\nu}(P)(x) \neq 0$. $\square$

The next section uses this theorem with explicit constants $n'$ and $\Lambda_0$. They are

$$n_Q = \Big\lceil \frac{1000\, m_s}{r_h} \Big\rceil + 1, \qquad \Lambda_Q = \max(1, \Lambda_6),$$

with $\varepsilon_0$, $r_h$, $m_s$ and $\Lambda_6$ computed from $(r, E, g, N_A, N_C, c_1, w)$ and $p_0 = q$.

**Corollary 4.2.3 (Split points with the constants of the CM family).** Let $X$ be a Hermitian datum as above, with $p_0 = q$ and $g$ as given, let $\lambda$ be a dominant weight and $P$ a function on frames, and let $c_1, w \in \mathbb{R}$. Assume $c_1 > 0$, $w \geq 1$, $\sum_\tau \mathrm{spread}_\tau(\lambda) \leq w$, $r \leq w$, $\chi_\lambda(\gamma) = 1$ for all $\gamma \in \Gamma$, $P \in \mathrm{SS}(\lambda)$ and $P \notin \mathrm{SS}_{>c_1}(\lambda)$. Then there are an isotropic $\xi$, a $\nu$ with $\sum_\tau \nu_\tau \leq c_1$, a frame $x \in \mathcal{D}_X$ and vectors $\ell_1, \ldots, \ell_{r-2}$ such that $(\xi, \Lambda_Q, x, \ell)$ is split data, for each $\mu \in \Lambda_p(\xi)$ there is $e \in E$ with $e\xi \in \Lambda$ and $n_Q \cdot \mathrm{pr}_x(\xi, \mu) = e\xi$, and $\mathrm{FJ}_{\xi,\nu}(P)(x) \neq 0$.

Lean: `GlobalTheory.ArcDetect.exists_split`.

*Proof.* This is Theorem (A nonzero coefficient at a split point) applied with $n' = n_Q$. The second hypothesis of the theorem holds since $\chi_\lambda$ is trivial on all of $\Gamma$. The bound $n_Q \geq 1000\, m_s / r_h$ holds since $\lceil y \rceil \geq y$. Split data for $\Lambda_6$ is split data for $\Lambda_Q$, since only the sixth condition involves $\Lambda_0$ and $\Lambda_6^2 \leq \Lambda_Q^2$: here $\Lambda_6 \geq 0$ by a direct check on its formula. $\square$

**Remark 4.2.4 (Formalization).** The name of the theorem has a prime, and there is no version without the prime in the code base. The point assembly theorem [FdPointAssembly.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/FundamentalDomains/FundamentalDomainExtension/PointAssembly/FdPointAssembly.lean#L6) takes nine hypotheses and does not use three of them (the short vector bound, the isotropic coefficient splitting and the lower bound with no short vector); the theorem passes all nine. The corollary asks that $\chi_\lambda$ be trivial on all of $\Gamma$, which is stronger than the congruence condition of the theorem ([ExistsFamilyMemberFunctionalNeZero.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/ExistsFamilyMemberFunctionalNeZero.lean#L142)); its conclusion drops $\nu \geq 0$ and the short vector conditions. We have not unfolded the flow bound $\varepsilon_0$, the constants $r_h$, $\Lambda_6$, $m_s$, the normalized size $\hat{N}$, the complex structure $J_x$ or the frames over a basis.
