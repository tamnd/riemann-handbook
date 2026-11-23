---
title: Period charts at the boundary
decls:
  - GlobalTheory.ShFam.Hor.LogCh.exists_periodChart_of_latFam
  - GlobalTheory.T.exists_periodChart_holomorphicLatticeFamily
  - GlobalTheory.ShFam.Hor.LogCh.PerChart.exists_riemann_period_chart
  - GlobalTheory.T.exists_riemannForm_periodChart_genericFibre
  - GlobalTheory.ShFam.Hor.PerChart.exists_periodChart_hodge
  - GlobalTheory.T.exists_periodChart_hodgeMetric_genericFibre
  - GlobalTheory.LieBase.HodgeChart.exists_hodge_period_chart
  - GlobalTheory.T.exists_hodgeMetric_periodChart_at_boundaryPoint
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Period charts at the boundary

The main theorem needs the Hodge metric to be good in the sense of Mumford: near each boundary point it must have logarithmic growth. This section gives the local form of the Hodge metric near a boundary point. In a chart where the boundary is a union of coordinate hyperplanes, the Hodge Gram matrix is, after a holomorphic frame change, the inverse of the imaginary part of a period matrix of the form $\tau_0(z) + \sum_i (\log z_i / 2\pi i)\, B_i$ with nilpotent monodromy. This is the nilpotent orbit form of a degenerating family of abelian varieties. The next section derives [the growth bounds](/entry/lie-gram-is-good/) from it.

**Definition 7.5.1 (Period chart).** Let $n \geq a$ and $g \geq 0$. Let $\Delta^n$ be the open unit polydisc in $\mathbb{C}^n$, and $\Delta^{*}_{a,n} \subset \Delta^n$ the set of points with $z_i \neq 0$ for $i < a$. Put $\ell(w) = -\log|w| / 2\pi$. A *period chart* of rank $r$ is a holomorphic map $\tau_0 \colon \Delta^n \to M_g(\mathbb{C})$ and integral matrices $B_0, \dots, B_{a-1} \in M_g(\mathbb{Z})$ such that:

1. $r \leq g$, and $\tau_0(z)$ is symmetric for each $z$;
2. each $B_i$ is positive semidefinite and vanishes outside the upper left $r \times r$ block;
3. $\sum_i B_i$ is positive definite on the $r \times r$ block;
4. $\operatorname{Im} \tau_0(z)$ is positive definite on the complementary $(g-r) \times (g-r)$ block.

Its *period matrix* on $\Delta^*_{a,n}$ is $\tau(z) = \tau_0(z) + \sum_{i<a} (\log z_i / 2\pi i)\, B_i$, for a choice of branches, and its *Hodge Gram matrix* is
$$G(z) = \operatorname{Im} \tau(z) = \operatorname{Im} \tau_0(z) + \sum_{i<a} \ell(z_i)\, B_i,$$
which does not depend on the branches.

The matrices $B_i$ are the logarithms of the unipotent monodromies around the boundary divisors, and $r$ is the toric rank of the degeneration ([semi-abelian degenerations](/learn/abelian-varieties/#semi-abelian-degenerations-and-mumfords-construction)). Conditions 3 and 4 say that $G(z)$ is positive definite near the boundary, where $\ell(z_i)$ is large. For $g = 1$, $a = n = 1$, $r = 1$, $B_0 = 1$ and $\tau_0 = 0$, we get the Tate curve: $\tau(z) = \log z / 2\pi i$ and $G(z) = -\log|z|/2\pi$.

**Definition 7.5.2 (Holomorphic lattice family).** Let $W \subseteq \mathbb{C}^n$ be open. A *holomorphic lattice family* on $W$ is a family of subgroups $K(z) \subseteq \mathbb{C}^g$, $z \in W$, such that the set $\{(z, w) : w \in K(z)\}$ is closed, and near each of its points it is the graph of a holomorphic section. Let $D_{a,n}$ be the set of $s \in \mathbb{C}^n$ with $\operatorname{Re} s_k < 0$ for $k < a$ and $|s_k| < 1$ for $k \geq a$, and let $\varepsilon(s)$ apply $\exp$ to the first $a$ coordinates. So $\varepsilon$ maps $D_{a,n}$ onto $\Delta^*_{a,n}$, and $D_{a,n}$ is a universal cover.

**Theorem 7.5.3 (Period charts of lattice families).** Let $a \leq n$, $g$, $r_0$ and $r$ be integers, $M \in M_r(\mathbb{Z})$, and $\mathbb{B}$ the unit ball of $\mathbb{C}^n$. Let $K$ be a holomorphic lattice family on $\mathbb{B}$. Let $\zeta_1, \dots, \zeta_{r_0} \colon \mathbb{B} \to \mathbb{C}^g$ be holomorphic, linearly independent over $\mathbb{R}$ at each point, with $\zeta_i(z) \in K(z)$, such that $\zeta(0)$ is a basis of $K(0)$ and each standard basis vector of $\mathbb{C}^g$ is a constant $\zeta_i$. Let $\mu_1, \dots, \mu_r \colon D_{a,n} \to \mathbb{C}^g$ be continuous, such that for each $s$:

1. $\mu(s)$ is linearly independent over $\mathbb{Z}$, spans $\mathbb{C}^g$ over $\mathbb{R}$, and $K(\varepsilon(s)) = \sum_j \mathbb{Z}\,\mu_j(s)$;
2. there is a positive definite Hermitian matrix $H$ with $\operatorname{Im} H(\mu_i(s'), \mu_j(s')) = M_{ij}$ for all $s'$ with $\varepsilon(s') = \varepsilon(s)$;
3. for each $N \geq 1$ there is a set $S \subseteq (\mathbb{Z}/N)^{r_0}$ with $N^{r_0} |S| = N^{2g}$ such that for $u \bmod N \in S$, all $u'$, all $s$ and every matrix $H$ with $\operatorname{Im} H(\mu_i(s), \mu_j(s)) = M_{ij}$, $\operatorname{Im} H(\sum_i u_i \zeta_i, \sum_j u'_j \zeta_j)$ at $\varepsilon(s)$ lies in $N\mathbb{Z}$.

Then there are a period chart $(r, \tau_0, B_i)$, numbers $0 < \rho \leq 1$ and $d > 0$, and a holomorphic map $P$ on the ball of radius $\rho$ with invertible values, such that for $s \in D_{a,n}$ with $\varepsilon(s)$ in the ball of radius $\rho$ and every matrix $H$ with $\operatorname{Im} H(\mu_i(s), \mu_j(s)) = M_{ij}$,
$$P(\varepsilon(s))^{T}\, H\, \overline{P(\varepsilon(s))} = d\, G\bigl(\rho^{-1}\varepsilon(s)\bigr)^{-1}.$$

Lean: `GlobalTheory.ShFam.Hor.LogCh.exists_periodChart_of_latFam` (also `GlobalTheory.T.exists_periodChart_holomorphicLatticeFamily`, a second name).

*Proof.* We follow the classical argument for degenerations of polarized abelian varieties.

1. *A period frame.* Write the lattice basis $\mu(s)$ in the holomorphic frame given by $\zeta$. This gives a holomorphic matrix $P$ and a period matrix $\tau(s)$ on $D_{a,n}$, symmetric with positive definite imaginary part by the Riemann relations of condition 2, and with integral monodromy: $\tau(s + 2\pi i e_k) = \tau(s) + B_k$.
2. *Nilpotent orbit form.* Since the monodromies are translations by $B_k$, the function $\tau_0 = \tau - \sum_k (s_k / 2\pi i) B_k$ is invariant, so it descends to $\Delta^*_{a,n}$. Positivity of $\operatorname{Im} \tau$ as $\operatorname{Re} s_k \to -\infty$ forces each $B_k$ to be positive semidefinite, and the bound on $\tau_0$ near the boundary, together with Riemann's removable singularity theorem, extends $\tau_0$ holomorphically to the polydisc.
3. *Toric positivity.* Choose $r$ so that the $B_k$ live on the $r \times r$ block. If $\sum_k B_k$ were not positive definite there, there would be a nonzero integral vector $v$ in the common kernel of the $B_k$ on the block. Then $\tau_0 v$ would give a section of the lattice family that extends continuously over the boundary, against the closedness of the family.
4. *Abelian positivity.* On the complementary block the Hodge Gram matrix is $\operatorname{Im} \tau_0$. The identity theorem for holomorphic functions extends the relations between $\tau_0$ and the lattice from the image of $\varepsilon$ to the whole ball, and this gives positivity on the block.
5. *Rescaling.* Rescale the ball of radius $\rho$ to the unit polydisc. This replaces $\tau_0(z)$ by $\tau_0(\rho z) + \sum_k (\log \rho / 2\pi i) B_k$ and gives the identity for $G(\rho^{-1} \varepsilon(s))$. $\square$

**Theorem 7.5.4 (Riemann forms in an exponential chart).** Let $x_0$ be a complex point of the generic fibre of the toroidal model. Then there are $n$, $a \leq n$, $g$, a period chart $(r, \tau_0, B_i)$ and an exponential chart $\phi_0$ of the universal family near $x_0$ with $\phi_0(x_0) = 0$, in which a point $x$ is off the boundary exactly when $\phi_0(x)_i \neq 0$ for all $i < a$, and a constant $d > 0$, such that at each point $x$ off the boundary the matrix $d\, G(\phi_0(x))^{-1}$ is a Riemann form: it is Hermitian and positive definite, its imaginary part is integral on the lattice of the uniformization of the fibre at $x$, and it is compatible with the cubical Weil pairings on torsion points.

Lean: `GlobalTheory.ShFam.Hor.LogCh.PerChart.exists_riemann_period_chart` (also `GlobalTheory.T.exists_riemannForm_periodChart_genericFibre`, a second name).

*Proof.* A framed chart of the toroidal model near $x_0$, with an exponential map onto the fibres, gives a holomorphic lattice family, the kernel of the exponential map. Its real independence and the constant sections come from the toroidal model. The cubical Weil pairing on $N$-torsion is constant in the holomorphic family and is $1$ at one complex point on the toric part, and the count of torsion points through the exponential lattice gives condition 3. A constant Riemann form on the chart gives condition 2. The [theorem on lattice families](/entry/exists-period-chart-of-lat-fam/) gives the period chart and the constant $d$, and the exponential chart is rescaled to the unit polydisc. $\square$

**Theorem 7.5.5 (The Hodge metric in an exponential chart).** In the setting of the last theorem, there are also positive numbers $\kappa_\tau$ ($\tau \in I$), with $g = \sum_\tau m_\tau$, such that at each point $x$ off the boundary there are a frame $f$ of the Lie algebra and vectors $W_{\tau,b}$ ($b < m_\tau$) with
$$\operatorname{gram}_\tau(x, f)_{b',b} = \kappa_\tau\, \bigl(G(\phi_0(x))^{-1}\bigr)(W_{\tau,b'}, W_{\tau,b}),$$
and $(G(\phi_0(x))^{-1})(W_{\tau,b}, W_{\tau',b'}) = 0$ for $\tau \neq \tau'$. Here $\operatorname{gram}_\tau(x, f)$ is the Gram matrix of the Hodge metric in the eigenframe $f$.

Lean: `GlobalTheory.ShFam.Hor.PerChart.exists_periodChart_hodge` (also `GlobalTheory.T.exists_periodChart_hodgeMetric_genericFibre`, a second name).

*Proof.* On the exponential chart the Hodge metric is a constant multiple $\kappa'_\tau$ of the Riemann form on each eigenspace. Combine this with the [Riemann form in the chart](/entry/exists-riemann-period-chart/) and put $\kappa_\tau = \kappa'_\tau d$. The orthogonality of different eigenspaces is part of the same comparison. $\square$

**Theorem 7.5.6 (Period charts on a Lie base).** Let $X, j, f, \mathcal{E}, A_0$ be a Lie base with open part $O$ and Hodge metric $h$, and let $y \in X(\mathbb{C})$ be a point not in $O(\mathbb{C})$. Then there are a holomorphic chart $\phi$ of $X(\mathbb{C})$ near $y$ onto the unit polydisc, with $\phi(y) = 0$, in which the complement of $O$ is $\{z : z_i = 0 \text{ for some } i < a\}$; a period chart $(r, \tau_0, B_i)$; a frame $A \in S(y)$; and holomorphic matrices $Q_\tau$ of size $m_\tau \times g$ with $\sum_\tau m_\tau = g$ and with linearly independent rows at $0$, such that on $O$, in the chart,
$$h_A(z)_\tau = Q_\tau(z)\, G(z)^{-1}\, Q_\tau(z)^*, \qquad Q_\tau(z)\, G(z)^{-1}\, Q_{\tau'}(z)^* = 0 \quad (\tau \neq \tau').$$

Lean: `GlobalTheory.LieBase.HodgeChart.exists_hodge_period_chart` (also `GlobalTheory.T.exists_hodgeMetric_periodChart_at_boundaryPoint`, a second name).

*Proof.* Apply [the Hodge metric in an exponential chart](/entry/exists-period-chart-hodge/) at the image of $y$ in the generic fibre. In the exponential chart there is a holomorphic eigenframe whose directions are the vectors $W_{\tau,b}$, and the exponential chart gives a holomorphic chart of $X$, since $j$ is an open immersion. A point of $X$ lies in $O$ if and only if its image is off the boundary. The rows of $Q_\tau$ are the vectors $W_{\tau,b}$ with the factor $\kappa_\tau^{1/2}$, and the chart is rescaled to the unit polydisc. $\square$

**Remark 7.5.7.** The nilpotent orbit form goes back to the theory of degenerations of abelian varieties of Mumford and of Faltings and Chai (G. Faltings and C.-L. Chai, *Degeneration of Abelian Varieties*, Chapter IV), and in the general Hodge-theoretic setting to the nilpotent orbit theorem (W. Schmid, "Variation of Hodge structure: the singularities of the period mapping", Invent. Math. 22 (1973), 211 to 319).

**Remark 7.5.8 (Formalization).** The period chart and its Hodge Gram matrix are `IsPeriodChart` and `hodgeGram` in HodgePeriodGram.lean (namespace `GlobalTheory.IndefiniteRowSideFullHecke.HodgePeriodGram`, lines 22 and 49). The name says nothing about Hecke operators. The first theorem is in [ExistsPeriodChartHolomorphicLatticeFamily.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsPeriodChartHolomorphicLatticeFamily.lean#L21); its steps are `exists_periodFrame_of_holomorphicLatticeFamily`, `periodMatrix_boundaryExtension_monodromy_posSemidef`, `exists_common_int_kernel_psd_block_not_posDef` with a closedness condition, `eqOn_ball_of_eqOn_punctPolydiscCoveringExp_image` and `periodChart_rescale_ball_to_unitPolydisc`. We did not open these lemmas; the classical reasons given in the proof are ours. In the second and third theorems, the exponential chart (`IsExpChart`) and the cubical Weil pairing condition (`CubWeil`) were not unfolded; we state them in words. The comparison in the third proof is the lemma `hodgeMetric_eq_const_mul_riemannForm_on_expChart`, which we did not open.
