---
title: Abelian parts and level covers
decls:
  - GlobalTheory.CompanionTheory.Ar.QuotUnif.main
  - GlobalTheory.T.lie_metric_height_bound
  - GlobalTheory.CompanionTheory.Ar.QuotUnif.local_bound
  - GlobalTheory.CompanionTheory.Ar.QuotLoc.abPart_principal_and_bound
  - GlobalTheory.T.principal_near_boundary
  - GlobalTheory.CompanionTheory.Ar.ChgField.exists_field
  - GlobalTheory.T.LevelCoverSt_holds
  - GlobalTheory.CompanionTheory.Ar.XR.levelCover
status: drafted
drafted_by: writer@claude-opus-5-5
---

## Abelian parts and level covers

This section proves two facts that the [good tower theorem](/entry/good-tower-and-volume/) uses. The first compares two metrics at a complex point of a Hodge component. At a point near the boundary the semi-abelian scheme degenerates, and its abelian part is a principally polarized abelian variety. The Hodge metric of the abelian part is bounded by a constant times the Lie metric of the Hodge component, with one constant for all complex points. This bound also enters the [slope bound for Hodge components](/entry/hodge-cpt-lie-metric-bound/). The second fact is a field extension: over a finite extension of the field of a generic point, the semi-abelian scheme has full $p^4$-torsion for each prime $p$ of a given finite set, and the field contains the $p^4$-th roots of unity. The proof uses level covers of the model.

We keep the setting of the earlier sections: $E$, $H$, $D$ of signature $(p, q)$, $l$, $X_o$, $c$ with field $F$, and a model $Y$ with semi-abelian scheme $t$. A Hodge component $\mathfrak{M}$ of $Y$ over a finite set $S$ lives on coordinates $y$ with values in a field $\Omega$. It has a scheme $X_{\mathfrak{M}}$, a semi-abelian scheme $t$ over it with an action of $\mathcal{O}_E$ and a Lie model. A Lie metric $h$ gives a hermitian form $h_z$ on the Lie algebra at each complex point $z$. We do not unfold these.

### Abelian parts

**Definition 8.11.1 (Abelian part).** Let $t$ be a semi-abelian scheme over $X$ with an action of $\mathcal{O}_E$ and a polarization, and let $z$ be a complex point of $X$. An abelian part of $t$ at $z$ consists of a semi-abelian scheme $t_K$ over $\mathbb{C}$ with a map $m \colon t_K \to t$ over $z$, a torus extension $0 \to T \to t_K \to B \to 0$, a semi-abelian scheme $t_B$ over $\mathbb{C}$ and an isomorphism of groups $e \colon B \to t_B$ that is compatible with the actions of $\mathcal{O}_E$ and with the polarizations. The abelian part is principal if $t_B$ is proper, its polarization line is relatively ample, and the line satisfies the triviality condition of the polarization.

Lean: `GlobalTheory.CompanionTheory.Ar.AbPart`, `GlobalTheory.CompanionTheory.Ar.IsPrincipal`.

So the abelian part is a quotient of the fibre at $z$ by a torus, with the polarization that it receives from $t$. For a tangent vector $v$ of $t_K$ at the origin, let $\bar v$ be its image in $t_B$, and let $\langle \bar v, \bar v \rangle_B$ be the Hodge inner product of the polarization of $t_B$. We say that $t$ satisfies the abelian bound with constant $K$ at $z$ if every abelian part at $z$ is principal and
$$
\operatorname{Re} \langle \bar v, \bar v \rangle_B \le K \operatorname{Re} h_z(v_0, v_0)
$$
for all tangent vectors $v$ of $t_K$ and $v_0$ of $t$ at $z$ with $m(v) = v_0$.

A complex point $z$ of $X_{\mathfrak{M}}$ is good if it lies over an embedding $\tau \colon F \to \mathbb{C}$ whose restriction to the field $K_A$ of the level maps the distinguished element $\rho$ of $K_A$ to the root $r_0$ of the host.

### The bound near the boundary

A boundary chart of $X_o$ at an embedding $\sigma \colon K_A \to \mathbb{C}$ of type $(n, a)$ is a holomorphic family $\psi$ of points of $X_o$ over the unit ball of $\mathbb{C}^n$, with a semi-abelian scheme $t$ over a ring $R$ and a Lie model on $\mathbb{C}^g$, such that the points with $u_j \ne 0$ for $j < a$ are interior. We do not unfold it further.

**Theorem 8.11.2 (Principal abelian parts near the boundary).** Let $1 \le p + q$, let $\sigma \colon K_A \to \mathbb{C}$ with $\sigma(\rho) = r_0$, and let $C$ be a boundary chart of $X_o$ at $\sigma$ of type $(n, a)$ with Lie model on $\mathbb{C}^g$. Then there are real numbers $0 < \rho_C \le 1$ and $K$ such that for every $u$ with $|u| < \rho_C$ and every abelian part $P$ of $t$ at $\psi(u)$ the following holds. The part $P$ is principal. Let $M_u$ be a Lie model of $t$ at $\psi(u)$ on $\mathbb{C}^g$ whose basis vectors lift the basis vectors of the chart. Then for every $x \in \mathbb{C}^g$ and every tangent vector $v$ of $t_K$ with $m(v) = M_u(x)$,
$$
\operatorname{Re} \langle \bar v, \bar v \rangle_B \le K \sum_{i=1}^{g} |x_i|^2.
$$

Lean: `GlobalTheory.CompanionTheory.Ar.QuotLoc.abPart_principal_and_bound` (also `GlobalTheory.T.principal_near_boundary`, a second name).

*Proof.* The chart has a family of logarithmic periods: a radius $\rho_0 \in (0, 1]$, a lattice $\Lambda$ and a polarization form $L$ on the chart, tied to the semi-abelian scheme. The logarithmic periods have a limit at the boundary, with a radius $\rho_1$ and a bound $C_b$ for the limit form. The point $\psi(u)$ lies on a discrete valuation ring through a point of the disc, with a polarized semi-abelian scheme over it, and every abelian part at $\psi(u)$ factors through this family. A polarized abelian part of such a family is principal. This proves the first claim. For the bound, take $\rho_C = \rho_0 \rho_1$ and $K = \pi C_b$, and write $u = \rho_0 u'$ with $|u'| < \rho_1$. At $u'$ the periods give the uniformization $\mathbb{C}^{g'} / \Lambda'$ of the abelian part $t_B$ with a hermitian matrix $H_m$. The period matrix gives a linear map $\ell \colon \mathbb{C}^g \to \mathbb{C}^{g'}$ that carries the Lie model to the tangent space of the uniformization. The pull back of $H_m$ by $\ell$ is a hermitian form. Its imaginary part agrees with the polarization form on the lattice. A hermitian form whose imaginary part vanishes on a full lattice is $0$, so the pull back is the form of the limit periods. The Hodge inner product of $\bar v$ is $\pi\, \ell(x) H_m \ell(x)^{*}$, and the bound for the limit form gives $\operatorname{Re} \langle \bar v, \bar v \rangle_B \le \pi C_b \sum |x_i|^2$. $\square$

**Lemma 8.11.3 (Local abelian bound).** Let $1 \le p + q$. Let $w$ be an analytic map on the open unit ball $B_1 \subset \mathbb{C}^n$ with values in the complex points of the coordinate ideal of $y$, and let $a \le n$. Assume that for $u \in B_1$ with $u_j \ne 0$ for $j < a$, every complex point $z$ of $X_{\mathfrak{M}}$ with coordinates $w(u)$ is interior. Let $u_0 \in B_1$. Then there are $\varepsilon > 0$ and $K_c \ge 1$ such that $t$ satisfies the abelian bound with every constant $K' \ge K_c$ at every good point $z$ with coordinates $w(u)$ for some $|u - u_0| < \varepsilon$.

Lean: `GlobalTheory.CompanionTheory.Ar.QuotUnif.local_bound`.

*Proof.* Recentre the ball at $u_0$ with a radius $\rho_0$ and a permutation of the coordinates. The point $w(u_0)$ is the coordinate vector of a complex point $z_0$, and the Lie model at $z_0$ is generated by finitely many values. The Hodge component has a holomorphic cover near $z_0$ by a boundary chart $C$ at an embedding $\tau$, with a radius $\rho_1$. If $\tau$ maps $\rho$ to $r_0$, then the [theorem on principal abelian parts](/entry/principal-near-boundary/) gives $\rho_2$ and $K_2$, and the comparison of the Lie metric with the chart on the boundary chart gives $\rho_3$ and $K_3$ with $\sum |x_i|^2 \le K_3 \operatorname{Re} h_z(v_0, v_0)$. An abelian part at $z$ maps to an abelian part of the chart, so the bound holds with $K' \ge |K_2| K_3$, and $\varepsilon$ is the smallest of the radii. If $\tau$ does not map $\rho$ to $r_0$, then no point near $z_0$ is good, since all of them lie over $\tau$. So the claim holds with $K_c = 1$ and $\varepsilon = \rho_0 \rho_1$. $\square$

**Theorem 8.11.4 (Lie metric bound for abelian parts).** Assume the residue field statement. Let $\mathfrak{M}$ be a Hodge component of $Y$ over $S$, let $h$ be a Lie metric for it, and let $1 \le p + q$. Then there is $K \ge 1$ such that $t$ satisfies the abelian bound with constant $K$ at every complex point $z$ of $X_{\mathfrak{M}}$.

Lean: `GlobalTheory.CompanionTheory.Ar.QuotUnif.main` (also `GlobalTheory.T.lie_metric_height_bound`, a second name).

*Proof.* The residue field statement gives finitely many charts $w_1, \dots, w_k$ on the unit ball of $\mathbb{C}^n$ with the hypotheses of the local bound, such that every complex point has coordinates $b \cdot w_i(u)$ with $|u| \le 1/2$ and a vector $b$ of non-zero scalars. The closed ball of radius $1/2$ is compact. The [local abelian bound](/entry/quot-unif-local-bound/) gives at each of its points an open ball and a constant, and finitely many of these balls cover it. The largest of their constants is a constant $K_i$ for the chart $w_i$. Put $K = 1 + \sum_i K_i$. Then $K \ge 1$ and $K \ge K_i$ for each $i$. A good point $z$ has coordinates $w_i(u)$ up to the scalars $b$, so the bound holds at $z$ with $K$. Every complex point is good or the complex conjugate of a good point, and the abelian bound at a point gives the abelian bound with the same constant at its conjugate. $\square$

### Level covers and the field of torsion

**Theorem 8.11.5 (Level covers).** Let $e$ be a generic point of $Y$ and let $N \ge 1$. Then there are a field $\Omega$ of characteristic $0$, a projective model $M$ over $\mathbb{Z}$ on coordinates $x \in \Omega^n$ with generic point $\xi_M$, a finite morphism $f \colon M \to Y$ with $f(\xi_M) = e$, a point $y$ of the generic fibre of $X_o$ over $\Omega$ with $f \circ \xi_M = j \circ y$, a semi-abelian scheme $t_M$ over $M$ with a map $t_M \to t$ over $f$, a unit $z \in \Omega^{\times}$ and sections $\mathrm{ev}$ of $t_M$ indexed by the lattice of $D$, with these properties: $\xi_M$ is a normal component, $t_M$ has full level $N$ at $\xi_M$ with respect to $(z, \mathrm{ev})$, $t_M$ has full $N$-torsion at $\xi_M$, and $z$ is a unit at every point of every component of $M$.

Lean: `GlobalTheory.CompanionTheory.Ar.XR.levelCover` (also `GlobalTheory.T.LevelCoverSt_holds`, a second name).

*Proof.* The generic point $e$ has normal coordinates over a field $K$ and a point $y_0$ of the generic fibre. There is a finite extension $\Omega$ of $K$ with a unit $z$ and sections $\mathrm{ev}$ that give full level $N$ over $\Omega$. Since $Y$ is projective over the integers of $F$, it is projective over $\mathbb{Z}$, and the residue field of the image point is finite over the residue field of $e$. So there is a finite normal model $M$ over $\mathbb{Z}$ with a finite map $\pi \colon M \to Y$ through the point over $\Omega$. The full level structure at the generic point spreads to a semi-abelian scheme $t_M$ over $M$ with the stated properties. $\square$

**Theorem 8.11.6 (Field with full torsion).** Let $\Omega_1$ be a field of characteristic $0$ and $\xi_1 \colon \operatorname{Spec} \Omega_1 \to Y$ a point whose image is a generic point of $Y$. Let $S$ be a finite set of primes. Then there are a field $\Omega$ of characteristic $0$ and a homomorphism $i \colon \Omega_1 \to \Omega$ such that $\Omega$ is finite over $\Omega_1$, the group of $t$ has full $p^4$-torsion at $\xi_1 \circ i$ for every $p \in S$, and $\Omega$ contains a primitive $p^4$-th root of unity for every $p \in S$.

Lean: `GlobalTheory.CompanionTheory.Ar.ChgField.exists_field`.

*Proof.* Let $N = \prod_{p \in S} p^4$. Then $N \ne 0$. The [theorem on level covers](/entry/level-cover/) at the image $e$ of $\xi_1$ gives a field $\Omega'$ and a point over $e$ with full $N$-torsion. Both $\xi_1$ and this point factor through the residue field $\kappa$ of $e$. Let $\Omega_2$ be a compositum of $\Omega_1$ and $\Omega'$ over $\kappa$, finite over $\Omega_1$. Adjoin a primitive $N$-th root of unity $\zeta$ to get $\Omega$, finite over $\Omega_2$. Full $N$-torsion is preserved by field extension, so it holds at $\xi_1 \circ i$. For $p \in S$ we have $p^4 \mid N$, so full $N$-torsion gives full $p^4$-torsion, and $\zeta^{N/p^4}$ is a primitive $p^4$-th root of unity. $\square$

**Remark 8.11.7 (Formalization).** The non-good branch of `local_bound` is vacuous: there the proof shows by `exfalso` that no point near $z_0$ is good (LieMetricHeightBound.lean:185 to 200). The abelian bound and the good points are the definitions `AbBound` and `GoodPt` of AbBound.lean:19 and 29. The steps go through named results such as `T.hodge_component_finite_charts`, `T.boundary_chart_lie_metric_bound`, `T.good_point_or_conjugate`, `T.abelian_bound_conjugate`, `T.exists_log_period_family`, `T.log_period_limit`, `T.hol_unif_period_matrix_middle`, `T.full_level_generic_cover` and `T.exists_full_level_finite_extension`, which we do not unfold. The level cover statement is also used in IsPrimitiveRootOfLevel.lean:105.
