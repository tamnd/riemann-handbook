---
title: Period charts at the cusps
decls:
  - GlobalTheory.CompanionTheory.Ar.Cusp.ChartFree.exists_actPeriods_chart
  - GlobalTheory.T.component_data_hodge_bound
  - GlobalTheory.CompanionTheory.Ar.Cusp.CorrPsh.chart_formula
status: drafted
drafted_by: writer@claude-opus-5-5
---

## Period charts at the cusps

Near a boundary point of a toroidal compactification, the abelian part of the universal semi-abelian scheme is described by periods on a product of punctured discs. The periods become single valued on the logarithmic cover, and the monodromy around each puncture is a unipotent map of the lattice. This section builds such a period chart around every point of a chart of the component data, with an action of $\mathcal{O}_E$ and holomorphic eigenframes. It then writes the Hodge potential and the cusp weight in the chart as a holomorphic part plus a log determinant of the period lattice. For the background see [toroidal compactifications](/learn/abelian-varieties/#toroidal-and-minimal-compactifications) and [semi-abelian degenerations](/learn/abelian-varieties/#semi-abelian-degenerations-and-mumfords-construction).

Fix the component data $D_c$ of an intersection system, with integers $j < N$, a set $\Phi$ of CM types and charts $\gamma_a$ from the unit ball of $\mathbb{C}^n$ into the complex coordinates, where $n = |\Phi|\, j\, (N - j)$. The data has a boundary set $\mathrm{Bd}$. Fix Hodge data for $D_c$, which gives a hermitian line $\mu$ on the coordinates, and let $\varphi_\mu = \log h_\mu$ be its potential. Fix a component origin, which gives a Hodge component $\mathfrak{M}$ with an interior, a labelling of the CM types, and the fact that a point is interior if and only if its coordinates are off $\mathrm{Bd}$.

**Definition 8.4.1 (Logarithmic periods).** Let $a \le n$ and $g \ge 0$. The logarithmic cover is the set of $w \in \mathbb{C}^n$ with $\operatorname{Re} w_i < 0$ for $i < a$ and $|w_k| < 1$ for $k \ge a$. The exponential map sends $w$ to the point with coordinates $e^{w_i}$ for $i < a$ and $w_k$ for $k \ge a$, which lies in the punctured ball $\{u : |u| < 1, u_i \ne 0 \text{ for } i < a\}$. A logarithmic period family of type $(n, a, g)$ consists of the following data.

1. A free $\mathbb{Z}$-module $\Lambda$ of rank $2g$ with a unimodular alternating form $E$.
2. Period maps $P_w : \Lambda \to \mathbb{C}^g$, holomorphic in $w$ on the logarithmic cover.
3. Positive hermitian matrices $H(e^w)$ with $\operatorname{Im}\big(P_w x \cdot H(e^w)\, \overline{P_w y}\big) = E(x, y)$.
4. Monodromy maps $T_i$ of $\Lambda$ for $i < a$ with $P_{w + 2\pi i e_i} = P_w \circ T_i$.

It is a family with $\mathcal{O}_E$ action if $\Lambda$ is an $\mathcal{O}_E$-module with $E(c x, y) = E(x, \bar c y)$, and there are endomorphisms $B(z)(c)$ of $\mathbb{C}^g$, holomorphic in $z$ on the unit ball, with $P_w(c x) = B(e^w)(c)\, P_w(x)$.

Lean: `GlobalTheory.CompanionTheory.Ar.Flat.LogPeriods`, `GlobalTheory.CompanionTheory.Ar.Cusp.ActPeriods`

At each $w$ the data defines a Riemann lattice $R_w$ with $\mathcal{O}_E$ action. For a family $\sigma$ of embeddings indexed by $\Phi$, its cusp weight is

$$
\operatorname{cw}_\sigma(R) = \max\Big(0, \sup_I \big(-\log \nu_\sigma(I)\big)\Big),
$$

where $I$ runs over the nonzero saturated isotropic submodules and $\nu_\sigma(I)$ is a normalized product of Gram determinants of eigencomponents. We do not unfold $\nu_\sigma$. The log determinant of frames $b_\tau$ is $\operatorname{ld}(b) = \sum_\tau \log \det \mathrm{Gram}(b_\tau)$. A family $\sigma$ is a CM family if it is injective and, for each embedding $s$, it contains $s$ if and only if it does not contain $\bar s$. Frames $b_{\tau, i}(t)$ are eigenframes for $B$ on a set $U$ if they are holomorphic on $U$ and, at each $t \in U$, $b_\tau(t)$ is a basis of the $\sigma_\tau$ eigenspace of $B(t)$.

**Theorem 8.4.2 (Period chart at a cusp).** Assume the top level inputs. Let $a$ be a chart index and let $t_0$ be in the unit ball of $\mathbb{C}^n$. Then there are integers $a_0, g$, a family of logarithmic periods $L$ of type $(n, a_0, g)$ with $\mathcal{O}_E$ action, a permutation $\pi$ of the coordinates, a radius $\rho > 0$, a CM family $\sigma$, a map $\mathrm{pt}$ from the unit ball to the complex points of $X$, a Hodge frame $d$ at $\gamma_a(t_0)$, sections $s_{\tau, i}$ of the Lie algebra that are a small part of $d$, and eigenframes $b$ for $B$ on the unit ball, with these properties. Write $t(u) = t_0 + \rho\,(u \circ \pi)$.

1. For every $u$ in the unit ball, $t(u)$ lies in the unit ball and in the frame domain of $d$, the coordinates of $\mathrm{pt}(u)$ are $\gamma_a(t(u))$, the labels of $\mathrm{pt}(u)$ are given by $\sigma$, and $\mathrm{pt}(u)$ is interior if and only if $u$ lies in the punctured ball.
2. For every $w$ in the logarithmic cover there are tangent vectors $v_{\tau, i}$ at $\mathrm{pt}(e^w)$ with Lie values $s_{\tau, i}$, such that $R_w$ is the period lattice of the fibre at $\mathrm{pt}(e^w)$ with the vectors $b(e^w)$ matching the $v$.

Lean: `GlobalTheory.CompanionTheory.Ar.Cusp.ChartFree.exists_actPeriods_chart` (also `GlobalTheory.T.component_data_hodge_bound`, a second name)

*Proof.* The point $\gamma_a(t_0)$ is the coordinate vector of a complex point $z_0$. The component data gives a Hodge frame $d$ at $z_0$ with a small part $s$, and each $s_{\tau, i}$ is the value of a tangent vector at $z_0$. A local form of the Hodge component near a normal crossings chart gives $a_0$, $\pi$, a first radius $\rho_1$, a holomorphic family of complex points $\psi$, a map to $X$ and vectors with the values $s$. A family of logarithmic periods $L_0$ with radius $\rho_2 \le 1$ exists on the boundary chart, and the $\mathcal{O}_E$ action of the semi-abelian scheme gives holomorphic endomorphisms $B$ that preserve the period lattices. These endomorphisms define the $\mathcal{O}_E$-module structure on $\Lambda$.

The period maps are injective because $E$ is unimodular. The adjoint relation $E(c x, y) = E(x, \bar c y)$ follows from the compatibility of the $\mathcal{O}_E$ action with the hermitian form at one base point $w_0$ of the logarithmic cover. The CM family $\sigma$ comes from the holomorphic points of the component and the side of the labelling. The eigenframes come from the Hodge lattice of the abelian family. The radius is $\rho = \rho_1 \rho_2$, and the map is $\mathrm{pt}(u) = \psi(\rho_2 u)$ followed by the map to $X$. $\square$

A function $U$ on the complex coordinates is a cusp weight for the origin if, at every interior complex point $z$ with coordinates $w$, there are a Riemann lattice $R$ that is the period lattice of the fibre at $z$ and a family $\sigma$ that gives the labels of $z$, such that $U(w) = \operatorname{cw}_\sigma(R)$.

**Proposition 8.4.3 (Chart formula).** Assume the top level inputs, and let $U$ be a cusp weight for the origin. Let $a$ be a chart index and let $t_0$ be in the unit ball. Then there are $a_0, g$, a family of logarithmic periods $L$ with $\mathcal{O}_E$ action, a permutation $\pi$, radii $\rho > 0$ and $0 < r \le 1$, a CM family $\sigma$, eigenframes $b$ for $B$ on the unit ball, and a function $G$ holomorphic on the ball of radius $r$, with these properties. Write $t(u) = t_0 + \rho\,(u \circ \pi)$.

1. For every $u$ in the unit ball, $t(u)$ lies in the unit ball, and $t(u)$ is off the boundary if and only if $u$ lies in the punctured ball.
2. For every $w$ in the logarithmic cover such that $e^w$ lies in the punctured ball and $|e^w| < r$,

$$
\begin{aligned}
\varphi_\mu\big(\gamma_a(t(e^w))\big) &= \operatorname{Re} G(e^w) + \tfrac{1}{2}\, \operatorname{ld}_{R_w}\big(b(e^w)\big), \\
U\big(\gamma_a(t(e^w))\big) &= \operatorname{cw}_\sigma(R_w).
\end{aligned}
$$

Lean: `GlobalTheory.CompanionTheory.Ar.Cusp.CorrPsh.chart_formula`

*Proof.* Take the period chart of the theorem. The Hodge frame $d$ at $\gamma_a(t_0)$ has a unit whose value at $t_0$ is nonzero. So there are $r > 0$ and a holomorphic $G_0$ on the ball of radius $r$ around $t_0$ such that the logarithm of the norm of the unit and of the chart monomial is $\operatorname{Re} G_0$. Shrink $r$ so that $t(u)$ stays in this ball for $|u| < r$, and let $G(u) = G_0(t(u)) + C/2$ with $C = |\Phi|\, (N - j) \log \pi$.

The first property follows from the first property of the period chart and the description of the interior by the boundary set. For the second, the point $\mathrm{pt}(e^w)$ is interior. The fibre of the Hodge line at this point is computed by the frame $d$, the small part $s$ and the period lattice $R_w$ with the vectors $b(e^w)$. This gives $\varphi_\mu$ as the sum of the unit term and half the log determinant, up to the constant $C/2$. The cusp weight $U$ at an interior point equals $\operatorname{cw}_\sigma(R)$ for any period lattice of the fibre with the labels $\sigma$, and $R_w$ is one. $\square$

**Remark 8.4.4 (Formalization).** The theorem is stated with the name `component_data_hodge_bound`, but its content is the existence of the period chart. The proof uses the named results `T.complex_points_iff_centres`, `T.component_data_intersection_bound`, `T.snc_chart_hodge_component_local`, `T.boundary_chart_log_period_family`, `T.holomorphic_endomorphism_family` and `T.log_periods_module_structure`, which we do not unfold. The affine map $u \mapsto t_0 + \rho\,(u \circ \pi)$ used in the chart formula is `aff`. The same definition appears three times, in ChartPshPhMu.lean:27 (namespace `Cusp.MuPsh`), HodgeIPOfFibreLatVec.lean:47 (namespace `Cusp.CuspCorrespondence`) and CuspIntersectionComparison.lean:30 (namespace `Cusp.GVal`). The chart formula opens `CuspCorrespondence` and uses that copy.
