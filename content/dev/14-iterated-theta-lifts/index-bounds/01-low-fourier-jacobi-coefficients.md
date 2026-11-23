---
title: Low Fourier-Jacobi coefficients
decls:
  - GlobalTheory.T.mem_forms_low_coeffs_vanish_iff_fourierJacobi
  - GlobalTheory.LowCoeff.mem_iff_low_coeff_vanish
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Low Fourier-Jacobi coefficients

The chapter bounds the index of a sublattice in a quotient $M / (M \cap S^\flat)$, where $M$ is a lattice of cusp forms and $S^\flat$ is the subspace of forms whose Fourier coefficients vanish at the "killed" exponents of the maximal cusps. This section proves that $S^\flat$ has a second description: a form lies in $S^\flat$ if and only if, on each component of a unitary chart, all its Fourier-Jacobi coefficients of total order at most $c_1$ vanish along all isotropic vectors (Theorem (Low coefficients)). Section 3 uses this description to find, for each form outside $S^\flat$, a CM point that sees it. The theorem is also an input of [the theorem that assembles the index bound hypotheses](/entry/inputs-net-rec-plus/).

**The setting.** Throughout the chapter we fix a datum and a core of the recursive construction of cusp forms, with its laws. We use only the following parts of them. There is a CM field $E$ with $[E : \mathbb{Q}] = 2f$, a CM type $\Phi$ of $E$ (a set of $f$ complex embeddings, one from each pair of complex conjugate embeddings), and the root discriminant $\mathrm{rd}_E = |d_E|^{1/2f}$. There are integers $r \geq 1$ (a rank) and $m$, and for each step $j$ an integer $\rho_j$; for $j < m$ in the admissible range we have $\rho_j = m - j \geq 1$. There is a number field $K$, the field of coefficients. For each step $j$ and each weight $\kappa$ there is a finite-dimensional $K$-vector space $S = S_{j,\kappa}$ of cusp forms, an $\mathcal{O}_K$-submodule $M \subset S$, and for each embedding $\sigma : K \to \mathbb{C}$ a function $F \mapsto \|F\|_\sigma$ on $S$ (the sup norm at $\sigma$) with $\|F\|_\sigma \geq 0$, $\|F\|_\sigma = 0$ only for $F = 0$, and $\|aF\|_\sigma = |\sigma(a)|\, \|F\|_\sigma$ for $a \in K$. A weight $\kappa$ is a pair of families of natural numbers $(a^+_{\tau,i})$ and $(a^-_{\tau,i})$, indexed by $\tau \in \Phi$ and decreasing in $i$, and an even integer $n \geq 0$. Its *size* is

$$\mathrm{size}(\kappa) = \sum_{\tau} \Big( \sum_i a^+_{\tau,i} + \sum_i a^-_{\tau,i} \Big) + f \cdot \max(\rho_j, 1) \cdot r \cdot n + 1 \geq 1.$$

For real numbers $C_R$, $T$ and $c$ we put $d_P = 2f\rho_j$ and

$$c_1 = c_1(C_R, T, c, j) = \frac{\mathrm{rd}_E^{\,C_R}\, T\, c\, d_P^{\,2}\, \rho_j}{2}.$$

Finally the core gives a unitary chart at a base embedding $\sigma_0$ of $K$. It has finitely many components $k$. For each $k$ there are a Hermitian datum $X_k$ and a weight $\lambda_k$ on it, defined below, and each $F \in S$ gives a function $F_k$ on the frames of $X_k$: the restriction of $F$ to the component $k$.

**Definition 4.1.1 (Hermitian datum and Fourier-Jacobi coefficient).** A *Hermitian datum* $X$ of rank $r$ over $E$ consists of a nondegenerate Hermitian form $h$ on $E^r$, an $\mathcal{O}_E$-lattice $\Lambda \subset E^r$, a set $\Psi$ of complex embeddings of $E$, a group $\Gamma$ of matrices that preserve the data, a character $\chi_\lambda$ of $\Gamma$ for each weight $\lambda$, a space of frames, and a domain $\mathcal{D}_X$ of frames (a fundamental set for $\Gamma$). A vector $\xi$ is *isotropic* if $\xi \in \Lambda$, $\xi \neq 0$ and $h(\xi, \xi) = 0$. Such a vector gives a real flow $s \mapsto \phi^\xi_s$ on frames, with $s \in \mathbb{R}^\Psi$, and a lattice of periods of this flow; let $D_\xi \subset \mathbb{R}^\Psi$ be a fundamental domain of the period lattice. For $\nu : \Psi \to \mathbb{R}$ and a function $P$ on frames, the *Fourier-Jacobi coefficient* of $P$ along $\xi$ at $\nu$ is the function

$$\mathrm{FJ}_{\xi,\nu}(P)(x) = \frac{1}{\mathrm{vol}(D_\xi)} \int_{D_\xi} P(\phi^\xi_s x)\, e^{-4\pi i \sum_\tau \nu_\tau s_\tau}\, ds$$

when $\nu$ satisfies the integrality condition of the period lattice, and $\mathrm{FJ}_{\xi,\nu}(P) = 0$ otherwise.

This is the classical Fourier-Jacobi expansion of a [modular form](/learn/theta-functions-cm/#modular-forms-as-rules) along a boundary component: the flow $\phi^\xi$ is the action of the centre of the unipotent radical of the parabolic subgroup that fixes the line $E\xi$, and $\mathrm{FJ}_{\xi,\nu}$ is the term of frequency $\nu$ in the expansion of $P$ in this action ([Fourier coefficients](/learn/automorphic-forms/#fourier-coefficients-and-whittaker-functions)).

**Definition 4.1.2 (Cusp forms and low coefficients).** Let $X$ be a Hermitian datum and $\lambda$ a weight. A *bounded section* of weight $\lambda$ is a section $P$ whose pointwise Petersson norm is bounded. The space $\mathrm{SS}(\lambda)$ of *cusp forms* is the set of bounded sections $P$ with $\mathrm{FJ}_{\xi,0}(P) = 0$ for all isotropic $\xi$. For $c \in \mathbb{R}$, the set $\mathrm{SS}_{>c}(\lambda)$ is the set of $P \in \mathrm{SS}(\lambda)$ such that $\mathrm{FJ}_{\xi,\nu}(P)(x) = 0$ for all isotropic $\xi$, all $\nu$ with $\sum_\tau \nu_\tau \leq c$, and all $x \in \mathcal{D}_X$.

So $P \in \mathrm{SS}_{>c}(\lambda)$ means that each Fourier-Jacobi expansion of $P$ starts above the total order $c$. The condition for $c = 0$ and $\nu = 0$ is the vanishing of the [constant terms](/learn/automorphic-forms/#constant-terms-and-cusp-forms).

The subspace $S^\flat$ is defined with maximal cusps instead of isotropic vectors.

**Definition 4.1.3 (Killed exponents).** Let $X$ be a Hermitian datum and $\rho \geq 1$. A *cusp frame* of size $\rho$ is a family $u = (e_1, \ldots, e_\rho)$ of vectors of $E^r$ that are linearly independent over $E$ and satisfy $h(e_a, e_b) = 0$ for all $a, b$. A Hermitian matrix $\chi \in M_\rho(E)$ is an *exponent* for $u$ if its phases with respect to $u$ are integers. For $\eta \in E^\rho$ put

$$h_\chi(\eta) = \sum_{a,b} \eta_a\, \chi_{ab}\, \bar{\eta}_b.$$

The pair $(u, \chi)$ is *killed at level* $c$ if there is $\eta \neq 0$ in $E^\rho$ with $\sum_a \eta_a e_a \in \Lambda$ and $\sum_{\tau \in \Psi} \mathrm{Re}\, \tau(h_\chi(\eta)) \leq c$. The *coefficient* of a function $P$ on frames at $(u, \chi)$ is

$$a_{u,\chi}(P)(x) = \int_{[0,1]^{N}} P(t \cdot_u x)\, e^{-2\pi i \sum_k t_k \varphi_k(\chi)}\, dt,$$

where $t \cdot_u x$ is the action of the torus of the cusp $u$ and $\varphi(\chi)$ is the phase vector of $\chi$.

In the setting above, the cusp data at step $j$ are the pairs $(k, u)$ of a component $k$ and a cusp frame $u$ of size $\rho_j$ for $X_k$. For each such pair there is a set of admissible exponents $\chi$ (Hermitian, positive definite and integral on a lattice $X_{k,u} \subset E^{\rho_j}$), and a $K$-linear map $s_{u,\chi}$ on $S$ with $s_{u,\chi}(F) = a_{u,\chi}(F_k)$ on $\mathcal{D}_{X_k}$ and $0$ outside. The pair is killed if some $\eta \neq 0$ in the trace dual of $X_{k,u}$ has $\sum_{\tau \in \Phi} \mathrm{Re}\, \tau(h_\chi(\eta)) \leq c_1$. Then

$$S^\flat = S^\flat(C_R, T, c) = \bigcap_{(u,\chi) \text{ killed}} \ker s_{u,\chi} \subset S.$$

We use one result on maximal cusps, which is proved outside this chapter.

**Proposition 4.1.4 (Maximal cusps).** Let $X$ be a Hermitian datum of rank $r$ over $E$ and $\rho \in \mathbb{N}$. Assume that each isotropic vector lies in the $E$-span of some cusp frame of size $\rho$, that each cusp frame of size $\rho$ has a $\mathbb{Z}$-basis in the sense of its period lattice, and that $\chi_\lambda(\gamma) = 1$ for each $\gamma \in \Gamma$ that is a unipotent element of the centre of a cusp frame. Let $c \in \mathbb{R}$ and $P \in \mathrm{SS}(\lambda)$. Then $P \in \mathrm{SS}_{>c}(\lambda)$ if and only if $a_{u,\chi}(P)(x) = 0$ for every cusp frame $u$ of size $\rho$, every exponent $\chi$ for $u$ such that $(u, \chi)$ is killed at level $c$, and every $x \in \mathcal{D}_X$.

Lean: `GlobalTheory.maxCusps_iff_killed_coeff_vanish`.

*Proof.* The proof combines two lemmas, one for each direction: a killed coefficient of a form in $\mathrm{SS}_{>c}(\lambda)$ vanishes, and a cusp form whose killed coefficients all vanish lies in $\mathrm{SS}_{>c}(\lambda)$. We do not reproduce them here. $\square$

**Theorem 4.1.5 (Low coefficients).** Let $j < m$ be in the admissible range, let $\kappa$ be a weight, let $C_R, T, c \in \mathbb{R}$ and let $F \in S_{j,\kappa}$. Then:

1. for each component $k$ the restriction $F_k$ lies in $\mathrm{SS}(\lambda_k)$;
2. $F \in S^\flat(C_R, T, c)$ if and only if $F_k \in \mathrm{SS}_{>c_1}(\lambda_k)$ for every component $k$, with $c_1 = c_1(C_R, T, c, j)$.

Lean: `GlobalTheory.LowCoeff.mem_iff_low_coeff_vanish` (also `GlobalTheory.T.mem_forms_low_coeffs_vanish_iff_fourierJacobi`, a second name).

*Proof.* Part 1. The space $S_{j,\kappa}$ consists of holomorphic sections of the cusp space. The restriction of such a section to a component of the chart is a bounded section with vanishing constant terms. This is a general lemma on holomorphic sections, applied with the algebra of the Siegel space. So $F_k \in \mathrm{SS}(\lambda_k)$.

Part 2. Fix a component $k$. We check the three hypotheses of Proposition (Maximal cusps) for $X_k$ with $\rho = \rho_j$. The laws of the core give a cusp frame of size $\rho_j$, a $\mathbb{Z}$-basis for each cusp frame, and $\chi_{\lambda_k} = 1$ on all of $\Gamma$. For the first hypothesis, let $\xi$ be isotropic. Since $\rho_j = m - j \geq 1$, the cusp frame of the laws has size at least $1$. A lemma of linear algebra says: if a Hermitian space has a cusp frame of size $n + 1$, then each nonzero vector $\xi$ with $h(\xi, \xi) = 0$ lies in the span of some cusp frame of size $n + 1$. So the Proposition applies, with $c = c_1$: $F_k \in \mathrm{SS}_{>c_1}(\lambda_k)$ if and only if the coefficients $a_{u,\chi}(F_k)$ vanish on $\mathcal{D}_{X_k}$ for all killed pairs $(u, \chi)$.

It remains to compare these pairs with the pairs in the definition of $S^\flat$. Three facts do this. First, an exponent in the sense of the Proposition is the same as a Hermitian matrix that is integral on $X_{k,u}$; the laws of the core give this. Second, a vector $\eta$ lies in the trace dual of $X_{k,u}$ if and only if $\sum_a \eta_a e_a \in \Lambda$, and the sum over $\Phi$ equals the sum over $\Psi$, since $\Phi \subset \Psi$ by the laws of the chart. So the two notions of "killed" agree. Third, $s_{u,\chi}(F) = 0$ if and only if $a_{u,\chi}(F_k)$ vanishes on $\mathcal{D}_{X_k}$, by the definition of $s_{u,\chi}$.

The admissible exponents in the definition of $S^\flat$ are also positive definite, and the Proposition has no such condition. So in the direction from $S^\flat$ to $\mathrm{SS}_{>c_1}$ we need one more fact: if $a_{u,\chi}(F_k)(x) \neq 0$ at a point $x$ of the domain for a cusp form $F_k$, then $\chi$ is positive definite. This is a lemma on cusp forms, proved with the same three hypotheses: then $\mathrm{Re}\, \sigma(h_\chi(\eta)) > 0$ for every $\eta \neq 0$ and every embedding $\sigma$ of $E$. With it, a nonzero coefficient at a killed pair would come from an admissible exponent, and $F \in S^\flat$ gives a contradiction. In the other direction, each admissible killed exponent is an exponent for the Proposition, and the vanishing follows directly. $\square$

**Remark 4.1.6 (Formalization).** The cusp data, the period lattices, the torus action of a cusp and the integrality of phases are definitions that we have described only through their roles; we did not unfold them. Proposition (Maximal cusps) is the statement `MaxCuspsStatement` in [MaxCuspsSt.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/ArchimedeanQuadraticData/MaximalCuspKernels/MaxCuspsSt.lean#L22); its third hypothesis is stated for the elements of $\Gamma$ of the form $1 + \sum_{a,b} \beta_{ab} e_a h(\cdot, e_b)$ with $\beta$ skew-Hermitian. In the theorem the subspace $S^\flat$ is the infimum `WeightFamilies.MggK`, and the trace in the killed condition is `trF`, the sum over the CM type.
