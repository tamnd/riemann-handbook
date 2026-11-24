---
title: Grassmannian heights, packing and normal crossing charts
decls:
  - GlobalTheory.T.grassmann_height_Z2_of_inputs_and_Z2
  - GlobalTheory.CompanionTheory.Ar.Giv.grassmann_height_Z2_of_push
  - GlobalTheory.T.packing'
  - GlobalTheory.CompanionTheory.Ar.Small.packing
  - GlobalTheory.T.lintegral_fibre_logNorm_finite
  - GlobalTheory.CompanionTheory.Ar.Pub.CxChart.logNorm_mass_lt_top
  - GlobalTheory.T.snc_resolution_boundary_normal_crossing
  - GlobalTheory.CompanionTheory.Ar.Cmp.SncRes.Par.exists_sncData_of_isSncModel
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Grassmannian heights, packing and normal crossing charts

This section proves four results that the volume theorem uses as inputs. The first is a lower bound for the height of a product of Grassmannians, paired against a class built from the flag data. The second counts small sections: their number grows at most like $\exp(C\tau^{D+1})$. The third says that $\log\lVert s\rVert$ has finite mass against smooth forms, read through a finite projection to affine space. The fourth gives local coordinates on a model with simple normal crossings, in which every form with zeros on the boundary is a unit times a monomial. Each proof combines results of the heights chapter.

### The height of a product of Grassmannians

Let $\Psi$ be a finite set, let $N \geq 2$ and $1 \leq j \leq N - 1$. The flag variety of this chapter is the product over $\Psi$ of the Grassmannians of $j$-planes in $N$-space. Its dimension is $\delta = \lvert\Psi\rvert\, j (N - j)$. Let $h_{\mathrm{Fl}}$ be the height polynomial of the flag variety for a system of intersection numbers $I$, as in Section 10, viewed as a linear form on polynomials in the root variables. For a rational number $c$ let $\phi_c$ be the fibre polynomial of the flag data and $\mu$ the polynomial of the base line. Put
$$
F_c = \mu^{\delta + 1} \phi_c, \qquad J_c = \int_{\mathrm{Fl}} \mu^{\delta} \phi_c .
$$

**Theorem 10.15.1 (Grassmannian height bound).** Assume the inputs of the development, the existence of an arithmetic intersection system and an upper bound for successive minima. Let $I$ be a system of intersection numbers, $N \geq 2$, $1 \leq j \leq N - 1$ and $c$ rational with $J_c > 0$. Let $e$ be real with
$$
\tfrac12 \log\det(1 + Z Z^{*}) \leq e
$$
for every complex $(N - j) \times j$ matrix $Z$ whose entries have absolute value $1$. Then
$$
-h_{\mathrm{Fl}}(F_c) \leq (\delta + 1)\, J_c\, \lvert\Psi\rvert\, e .
$$

Lean: `GlobalTheory.CompanionTheory.Ar.Giv.grassmann_height_Z2_of_push` (also `GlobalTheory.T.grassmann_height_Z2_of_inputs_and_Z2`, a second name).

*Proof.* The heights chapter reduces the bound to three facts. The first is the upper bound for successive minima. The second is the push formula for the flag variety: the height of the flag variety against $F_c$ is the pushforward of the heights of its Grassmannian factors, which follows from the inputs and the intersection system. The third is the positivity of the geometric degree of the ideal of the flag variety, which comes from the degree input and the positivity of multidegrees of Plücker blocks.

If $\Psi$ is empty, then $\delta = 0$ and the right side is $0$, and the height is $0$ as well. Otherwise the Plücker coordinates of the points with $Z$ unimodular give sections of small norm. On the chart $\binom{1}{Z}$ the Fubini-Study norm of the Plücker vector is $\det(1 + Z Z^{*})^{1/2}$, so its log is at most $e$. The successive minima bound turns these small sections into a lower bound for the height of each Grassmannian, namely $-(\delta + 1) J_c e$ per factor after pairing with $F_c$, and the push formula adds the $\lvert\Psi\rvert$ factors. $\square$

### Packing of small sections

Let $\Omega$ be a field and $y$ a point with coordinates $y_{k,i} \in \Omega$. Its coordinate ideal $P_y$ is the kernel of the map $R \to \Omega[x]$, $x_{k,i} \mapsto y_{k,i} x_k$. The point is birational if every $s \in \Omega$ is a quotient $g(y)/h(y)$ of two forms of the same degree with $h(y) \neq 0$. Let $A$ be a smooth hermitian line of degree $a$.

**Definition 10.15.2.** An element $s \in \Omega$ is a small section of $\tau A$ if, for all forms $g$ and $h$ with $\deg g = \deg h + \tau a$ and $g(y) = s\, h(y)$, and all complex points $z$ of $P_y$,
$$
\lvert g(z)\rvert \leq \lvert h(z)\rvert \, h_A(z)^{\tau}.
$$

The lattice of integral sections of $\tau A$ consists of the $s$ such that, in each affine chart $c$ with $y_{k, c_k} \neq 0$, the element $s \prod_k y_{k,c_k}^{-\tau a_k}$ is integral over the ring $\mathbb{Z}[y_{k,i}/y_{k,c_k}]$.

**Theorem 10.15.3 (Packing).** Let $P_y$ be an arithmetic variety of dimension $D + 1$, let $y$ be birational and $A$ smooth. Let $\Lambda_\tau$ be subgroups of the lattices of integral sections of $\tau A$. Then each $\Lambda_\tau$ contains only finitely many small sections, and there is $C$ with
$$
\log \#\{ s \in \Lambda_\tau : s \text{ small} \} \leq C (\tau + 1)^{D + 1}
$$
for all $\tau \geq 0$.

Lean: `GlobalTheory.CompanionTheory.Ar.Small.packing` (also `GlobalTheory.T.packing'`, a second name).

*Proof.* Step 1: rank. The integral sections of $\tau A$ lie in a finitely generated group of rank at most $C_1 (\tau + 1)^{D}$. This follows from the finiteness of the normalization over the chart rings, which gives a conductor, and from the bound for the dimension of the space of forms of degree $\tau a$ on a variety of dimension $D$ over $\mathbb{Q}$.

Step 2: separation. There is a finite grid of complex points with this property: two distinct small sections differ at some grid point by at least $\exp(-C_2(\tau + 1))$ after normalization. The proof writes the difference as a norm form over a finite projection, bounds the fibre norms by the sup norms of the sections, and uses that a nonzero integral norm has absolute value at least $1$ outside finitely many bad primes, whose contribution is bounded by $C_2 (\tau + 1)$.

Step 3: count. The small sections have values of absolute value at most a constant on the grid, and by Step 2 they are $\exp(-C_2(\tau + 1))$ apart in the evaluation map, which is injective on the group of Step 1. A volume count in a real space of dimension at most the rank gives
$$
\log \# \leq C_1 (\tau + 1)^{D} \cdot C_3 (\tau + 1).
$$
This is the bound with $C = C_1 C_3$. Finiteness is part of the count. $\square$

### Finite mass of the log norm

Let $Q$ be a complex variety of dimension $e$ in the product of projective spaces, with cone points $\hat X$. A good projection is a linear map $\Psi$ from the Segre coordinates to $\mathbb{C}^{e+1}$ that does not vanish on the Segre image of $\hat X$. It gives a finite map from $X$ to $\mathbb{P}^e$. In the affine chart $\mathbb{C}^e$ of $\mathbb{P}^e$, the integral of a function $g$ against $\omega_L$ on $X$ is the integral over $y \in \mathbb{C}^e$ of the sum over the fibre of the sheet densities of $g$.

**Theorem 10.15.4 (Finite mass of the log norm).** Let $\Psi$ be a good projection for $Q$, let $L_1, \dots, L_e$ and $A$ be smooth lines, and let $s \notin Q$ be a form of the degree of $A$. Then
$$
\int_{\mathbb{C}^e} \sum_{w \in \Psi^{-1}(y)} \bigl\lvert \rho_w(\log\lVert s\rVert_A)(y) \bigr\rvert \, dy < \infty ,
$$
where $\rho_w$ is the sheet density of the mixed form $\omega_L$ at the fibre point $w$.

Lean: `GlobalTheory.CompanionTheory.Ar.Pub.CxChart.logNorm_mass_lt_top` (also `GlobalTheory.T.lintegral_fibre_logNorm_finite`, a second name).

*Proof.* Step 1: positive densities. There are smooth lines $N_1, \dots, N_e$ whose sheet densities are nonnegative and dominate the absolute densities for $L$ for every nonnegative integrand. So it suffices to bound the mass of $\lvert\log\lVert s\rVert_A\rvert$ for $N$.

Step 2: cells. For each Segre index $i$ let the cell of $i$ be the set of cone points where the Segre coordinate $i$ has the largest absolute value. The cells cover $\hat X$, there are finitely many, and $\lvert\log\lVert s\rVert_A\rvert$ is at most the sum of its restrictions to the cells. The fibres of a good projection are finite, so the sum over the fibre is finite at each $y$.

Step 3: one cell. The integral of a density does not depend on the good projection. So for a cell that meets $\hat X$ we may choose a good projection whose first coordinate is the Segre coordinate $i$. On the cell this coordinate is not $0$, so the chart is affine and $\log\lVert s\rVert_A$ is $\log\lvert f\rvert$ plus a bounded function, where $f$ is a polynomial that does not vanish on $X$. A log of a polynomial is locally integrable against smooth forms, and the cell is relatively compact in the chart. So the mass on the cell is finite. For a cell that does not meet $\hat X$ the integrand is $0$. Sum over the cells. $\square$

### Normal crossing charts

Let $y$ be a point with coordinates in a field of characteristic $0$, and let $J$ be a multihomogeneous ideal with $J \not\subseteq P_y$. We say that $y$ is a model with simple normal crossings for $J$ in dimension $e$ if each affine chart ring is covered by smooth open pieces $D(f_l)$, each with elements $z_1, \dots, z_e$ whose differentials form a basis of the Kähler differentials, such that a prime of the piece contains $J$ if and only if it contains one of $z_1, \dots, z_n$ for some $n \leq e$.

**Theorem 10.15.5 (Normal crossing charts).** Let $P_y$ be an arithmetic variety of dimension $e + 1$ and let $y$ be a model with simple normal crossings for $J$ in dimension $e$. Then every complex point $x$ in an affine chart has local parameters $r_1, \dots, r_e$ and a set $S$ of boundary indices with an injective map $\sigma$ from $S$ to the boundary components such that:

1. near $x$, each boundary component $k$ is the set $\{r_l = 0\}$ for the $l \in S$ with $\sigma(l) = k$;
2. every form $f \notin P_y$ whose complex zeros lie in $V(J)$ is, in the local ring at $x$,
$$
f = u \prod_{l \in S} r_l^{\,\operatorname{ord}_{\sigma(l)}(f)}
$$
with a unit $u$, where $\operatorname{ord}_k(f)$ is the order of $f$ along the component $k$.

Lean: `GlobalTheory.CompanionTheory.Ar.Cmp.SncRes.Par.exists_sncData_of_isSncModel` (also `GlobalTheory.T.snc_resolution_boundary_normal_crossing`, a second name).

*Proof.* Step 1: parameters. In a smooth piece that contains $x$, the elements $z_i - z_i(x)$ are local parameters at $x$, by the basis of differentials and the Jacobian criterion. Let $S$ be the set of $i \leq n$ with $z_i(x) = 0$, and let $r_i = z_i - z_i(x)$, so $r_i = z_i$ for $i \in S$.

Step 2: the boundary. By the model condition, near $x$ the radical of the boundary ideal is the radical of the product $\prod_{i \in S} r_i$. Each $r_i$ with $i \in S$ defines a smooth hypersurface through $x$, and it lies in exactly one boundary component. This gives $\sigma$, which is injective since distinct parameters cut out distinct hypersurfaces at $x$. This is part 1.

Step 3: the factorization. Let $f$ have its zeros in $V(J)$. In the regular local ring at $x$, the zero set of $f$ is contained in the union of the hyperplanes $r_l = 0$, $l \in S$. A regular local ring is factorial and the $r_l$ are primes, so $f$ is a unit times a monomial in the $r_l$. The exponent of $r_l$ is the largest $n$ with $f \in (r_l)^{(n)}$, a symbolic power, and this is the order of $f$ along the component $\sigma(l)$, computed as the largest $n$ such that $s f$ lies in the $n$-th power of the component modulo $P_y$ for some $s$ outside the component. $\square$

**Remark 10.15.6 (Formalization).** The Grassmannian bound is at `Development/AutomorphicSpectrum/Proofs/MetricProofs/GrassmannHeightZ2OfInputsAndZ2.lean:19`; it applies `GrassmannianHeightZTwo.proof` with `flag_grassmann_push_of_inputs` and `FSGeomDegPos.proof`. Its statement `GrassmannianHeightZTwo.Statement` is defined at `GroundTheory/HeightsAndTheta/Heights/HodgeLowerBound/FlagIndices.lean:95`, and a second definition with the same name and the same body sits in another namespace at `FlagSectionNeZero.lean:68` of the same folder. In that statement $\delta$ is `dimN`, $F_c$ is `FA`, $J_c$ is `Jint`, and the third hypothesis named "successive minima" is passed under the variable name `hZ2`. The packing theorem is one line, `MultiProjectiveCoordinates.packing_statement`, at `PackingAlt.lean:9`; that proof is at `Development/WeilBound/CoreStatements/RationalSupMetrics/PullRatiosAlgebraic.lean:70`. The count in its statement is `smallSectionCount`, which is already the logarithm of the number of small sections (`ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/PenVol.lean:32`), and the lattices are `chartLatNm`. The mass bound is at `LintegralFibreLogNormFinite.lean:124` with the cell lemma at line 78; the cells are `domCell` (`MemChartComponents.lean:45`). The chart theorem is at `SncResolutionBoundaryNormalCrossing.lean:18`, and the model condition is `IsSncModel` (`Development/AutomorphicSpectrum/Definitions/GlobalGeometry/IsSncModel.lean:30`). The second names are relays at `GrassmannHeightZ2OfInputsAndZ2Statement.lean:15`, `PackingStatement.lean:7`, `LintegralFibreLogNormFiniteStatement.lean:17` and `SncResolutionBoundaryNormalCrossingStatement.lean:6`.
