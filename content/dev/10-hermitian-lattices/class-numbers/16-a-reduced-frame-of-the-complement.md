---
title: A reduced frame of the complement
decls:
  - ReciprocityTheory.ChartRestriction.G.FD.orthonormalShortVectorBound_of
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A reduced frame of the complement

This section turns the [short vector bound](/entry/short-vector-bound/) into a reduced basis. Let $\xi$ be an isotropic vector and $z_0$ a frame at which a Fourier-Jacobi coefficient along $\xi$ is near its maximum. The short vector bound says that the Hermitian lattice of the vectors orthogonal to $\xi$, modulo $\xi$, has no short vectors at $z_0$. A transference theorem from the geometry of numbers then gives $r - 2$ lattice vectors of bounded length that split into a positive and a negative part. A unitary change of frame that fixes the plane of $\xi$ moves $z_0$ to a frame in which these vectors are eigenvectors of the complex structure, and close to a given orthonormal frame. The result serves the [nonvanishing of a Fourier-Jacobi coefficient at a split point](/entry/exists-fj-ne-zero-at-split-point-prime/) in a later volume.

We keep the notation of the last section: the CM field $E$ of degree $2f$, the CM type $\Psi$, the Hermitian form $h$ of signature $(p_0, r - p_0)$, the lattices $\Lambda$ and $L'$, the domain $\mathcal{D}$ of frames, the majorants $m_{x, \tau}$, the components $v^\perp_x$, the short vector hypotheses for $(\lambda, P, \xi, \nu, c_1, w, z_0)$, and the constant $\varepsilon_0$. For a frame $x$, $J_x$ is the complex structure $u \mapsto i(2 p_{x, \tau} u - u)$ at each $\tau$.

### The covering radius theorem

The input from the geometry of numbers is the following theorem. For $p \leq r$ and $u, v \in \mathbb{C}^r$, let $j_p(u, v) = \sum_k s_k \overline{u_k} v_k$ with $s_k = 1$ for $k < p$ and $s_k = -1$ otherwise, and let $\| u \|^2 = \sum_k |u_k|^2$.

**Theorem 1.16.1 (Covering radius).** Let $K$ be a CM field of degree $2f$ and $(\sigma_i)_{i \in I}$ a CM type of $K$, with $|I| = f$. Let $S$ be a Hermitian form on $K^r$, $p \leq r$, $\lambda^* > 0$, and $Q_i \in \mathrm{GL}_r(\mathbb{C})$ with $\sigma_i(S(x, y)) = j_p(Q_i \sigma_i x, Q_i \sigma_i y)$. Let $L \subseteq K^r$ be a lattice, self-dual for $S$, such that every nonzero $v \in L$ has $\lambda^{*2} \leq \| Q_i \sigma_i v \|^2$ for some $i$. Let $\mu = 4 (f r)^3 |d_K| / \lambda^*$. Then:

1. for every $(w_i) \in (\mathbb{C}^r)^I$ there is $l \in L$ with $\sum_i \| Q_i \sigma_i l - w_i \|^2 \leq \mu^2$;
2. there are $r$ vectors of $L$, linearly independent over $K$, with $\sum_i \| Q_i \sigma_i v \|^2 \leq \mu^2$ for each of them.

Lean: `ReciprocityTheory.ChartRestriction.G.FD.CoveringRadiusStatement`.

Source: this is a form of the transference theorem of W. Banaszczyk, "New bounds in some transference theorems in the geometry of numbers", *Math. Ann.* 296 (1993), for the lattice $L$ in $\mathbb{R}^{2fr}$, with a weaker constant. In that theorem a lower bound for the first minimum of the dual lattice gives an upper bound for the covering radius and for the last successive minimum.

### The reduced frame

Let $\rho = 1 / (12 \pi (c_1 + w))$. A frame $x_0$ is *orthonormal* if, for each $\tau$, the Gram matrix of the columns of $x_{0, \tau}$ for $h_\tau$ is the diagonal matrix of the signs of the signature. For a coordinate $Z = (Z_\tau)$ with $Z_\tau \in M_{(r - p_0) \times p_0}(\mathbb{C})$, $x_0 Z$ is the frame $x_{0, \tau} n(Z_\tau)$, with $n(Z_\tau)$ the lower unipotent matrix of block $Z_\tau$, and $\| Z \|$ is the maximum over $\tau$ of the operator norms of $Z_\tau$. Let $\Lambda_a = (2 \cdot 4 \sqrt{r - 2} \, \mu' / (\rho / 40))^{2 p_0 - 1}$, where $\mu' = 4 (f (r - 2))^3 |d_E| / \sqrt{\varepsilon_0}$.

**Theorem 1.16.2 (Reduced orthonormal frame).** Assume the short vector hypotheses, and let $x_0 \in \mathcal{D}$ be an orthonormal frame with the same flag as $z_0$. Then there are $\lambda_1, \ldots, \lambda_{r-2} \in E^r$, a family $h_1 = (h_{1, \tau})$ of matrices that preserve each $h_\tau$, and a coordinate $Z_1$ such that:

1. $h_1$ fixes every vector $(s_\tau \tau \xi + J_{z_0}(t_\tau \tau \xi))_\tau$ of the plane of $\xi$, and $h_1$ maps the orthogonal complement of this plane into itself;
2. each $\lambda_j$ lies in $L'$ and is orthogonal to $\xi$, and $\xi, \lambda_1, \ldots, \lambda_{r-2}$ are linearly independent;
3. $h(\lambda_j, \lambda_k) = 0$ for $j < p_0 - 1 \leq k$ (indices from $0$);
4. for $j < p_0 - 1$, $\operatorname{Re} \tau h(\lambda_j, \lambda_j) > 0$ for all $\tau$ and $J_z({\lambda_j}^\perp_z) = i {\lambda_j}^\perp_z$, and for $j \geq p_0 - 1$, $\operatorname{Re} \tau h(\lambda_j, \lambda_j) < 0$ and $J_z({\lambda_j}^\perp_z) = -i {\lambda_j}^\perp_z$, where $z = h_1 z_0$;
5. $| \tau h(\lambda_j, \lambda_j) | \leq \Lambda_a^2$ for all $j$ and $\tau$;
6. $h_1 z_0$ has the same flag as $x_0 Z_1$, and $\| Z_1 \| \leq \rho / 100$.

Lean: `ReciprocityTheory.ChartRestriction.G.FD.orthonormalShortVectorBound_of`.

*Proof.* The theorem takes the short vector bound and the covering radius theorem as hypotheses. We use these facts, proved in another part of the development. We have opened their statements.

1. There is a basis $f$ of the orthogonal complement of the plane of $\xi$ at $z_0$, adapted to $x_0$. We do not unfold the conditions on $f$. The vectors of its positive part are eigenvectors of $J_{z_0}$ with eigenvalue $i$, and those of its negative part with eigenvalue $-i$.
2. *Reduction.* There are $\beta_1, \ldots, \beta_{r-2}$ orthogonal to $\xi$, such that $\xi, \beta_1, \ldots, \beta_{r-2}$ are linearly independent and every $x$ orthogonal to $\xi$ is $\sum c_k \beta_k + e \xi$, a Hermitian form $S$ on $E^{r-2}$ with $S(c, c') = h(\sum c'_k \beta_k, \sum c_k \beta_k)$, a lattice $L_B = \{c : \sum c_k \beta_k + e \xi \in L' \text{ for some } e\}$, self-dual for $S$, and matrices $Q_\tau$ with $\tau S = j_{p_0 - 1}(Q_\tau \cdot, Q_\tau \cdot)$, such that $(\sum c_k \beta_k)^\perp_{z_0}$ has coordinates $Q_\tau \tau c$ in the basis $f$.
3. *Reduced lattice.* Given fact 2, the covering radius theorem, $0 < \varepsilon \leq 1$, $0 < \rho \leq 1$, and the conclusion of the short vector bound with $\varepsilon$, there are $\lambda_j$ with items 2, 3 and 5 and the signs in item 4, whose components ${\lambda_j}^\perp_{z_0}$ are linearly independent, lie in the span of $f$, and are close to the basis $f$: for a vector in the span of the positive ${\lambda_j}^\perp_{z_0}$, the sum of the squares of its negative coordinates in the basis $f$ is at most $(\rho / 120)^2$ times the sum of the squares of its positive coordinates.
4. *Gram-Schmidt.* For such components there is $h_1$ with item 1 that maps the span of the positive part of $f$ to the span of the positive ${\lambda_j}^\perp_{z_0}$, and maps a vector of the matching part of $f$ to each ${\lambda_j}^\perp_{z_0}$.
5. *Coordinates.* With the bound $\rho / 120$ of fact 3, there is $Z_1$ such that $h_1 z_0$ has the same flag as $x_0 Z_1$ and $\| Z_1 \| \leq \rho / 120$.
6. *Moving the frame.* For $h_1$ with item 1, $h_1 z_0 \in \mathcal{D}$, the projection to the line of $\xi$ does not change on the vectors orthogonal to $\xi$, the majorant of $\xi$ does not change, and $J_{h_1 z_0} h_1 = h_1 J_{z_0}$ on the orthogonal complement of the plane.

Apply the short vector bound with $z_0$; it gives the hypothesis of fact 3 with $\varepsilon = \varepsilon_0$. As in the proof of the short vector bound, $0 < \varepsilon_0 \leq 1$, and $0 < \rho \leq 1$ since $\pi > 3$ and $c_1 + w \geq 1$. Facts 1, 2 and 3 give $\lambda$. Fact 4 gives $h_1$, and fact 5 gives $Z_1$ with $\| Z_1 \| \leq \rho / 120 \leq \rho / 100$. For the eigenvalues in item 4, write ${\lambda_j}^\perp_{z_0} = h_1 u_j$ with $u_j$ in the part of $f$ of the same sign. By facts 1 and 6, ${\lambda_j}^\perp_{h_1 z_0} = h_1 u_j$ and $J_{h_1 z_0}(h_1 u_j) = h_1 J_{z_0} u_j = \pm i \, h_1 u_j$. $\square$

**Remark 1.16.3 (Classical form).** The covering radius theorem is a form of the transference theorems of Banaszczyk (1993), with a weaker constant. The reduced frame plays the part of reduction theory for the Hermitian lattice $\xi^\perp / \xi$, in the sense of Siegel sets (A. Borel, *Introduction aux groupes arithmétiques*, Hermann, 1969), with constants that the proof computes: the lengths of the $\lambda_j$ are bounded in terms of $\varepsilon_0$, and the frame $h_1 z_0$ is within $\rho / 100$ of an orthonormal frame.

**Remark 1.16.4 (Formalization).** The theorem is at [OrthonormalShortVectorBoundOf.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/FundamentalDomains/OrthonormalShortVectorBoundOf.lean#L108). It takes the short vector bound and the covering radius theorem `CoveringRadiusStatement` as hypotheses, and the final assembly `fundamentalDomain_of_transference` passes `shortVectorBound` for the first. The covering radius theorem is proved twice in the development: `Formalism.L2.Pj.FundamentalDomainD5.d5_translation` in [FundamentalDomainD5.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/ArchimedeanQuadraticData/FundamentalDomainD5.lean#L17) and `GlobalTheory.CMTransference.cmApproximation_transference` in [CmApproximationTransference.lean](lean:Development/AbelianVarietyTheory/Proofs/CubicalLineBundles/CmApproximationTransference.lean#L293). We have not opened these proofs. The facts are `exists_unitary_basis_same_flag`, `exists_perp_hermitian_reduction`, `reducedLattice_short_bound`, `gramSchmidt_eigenframe`, `unitary_fixing_isotropic_plane` and `unitaryComplementMove`; the eigenvalues in fact 1 come from `eigenspan_perp_isotropic`. The proof gets $\| Z_1 \| \leq \rho / 120$, and the statement weakens it to $\rho / 100$ at [line 167](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/FundamentalDomains/OrthonormalShortVectorBoundOf.lean#L167). The theorem proves $0 < \varepsilon_0 \leq 1$ again with `epsilonZero_pos_le_one`, which repeats a part of `epsilonZero_spec`. In the covering radius theorem the form $j_p$ is conjugate linear in its first argument, while $h$ is conjugate linear in its second; fact 2 accounts for this with the order of $c$ and $c'$ in $S(c, c')$. The constant $\Lambda_a$ is `d6La`, with `approxR` and `d5mu` unfolded.
