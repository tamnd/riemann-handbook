---
title: Plurisubharmonicity and growth of the cusp weight
decls:
  - GlobalTheory.CompanionTheory.Ar.Cusp.CorrPsh.near_all
  - GlobalTheory.CompanionTheory.Relay.cusp_intersection_positive
  - GlobalTheory.T.cusp_intersection_positive
  - GlobalTheory.CompanionTheory.Ar.Cusp.CorrBdd.near_bdd
  - GlobalTheory.CompanionTheory.Ar.Cusp.CorrBdd.corr_bdd
  - GlobalTheory.T.cusp_chart_log_growth_bounds
  - GlobalTheory.CompanionTheory.Relay.cusp_weight_regularisations_tied
  - GlobalTheory.T.cusp_weight_regularisations_tied
status: drafted
drafted_by: writer@claude-opus-5-5
---

## Plurisubharmonicity and growth of the cusp weight

The Hodge line $\mu$ has a singular metric at the boundary, and the cusp weight $U$ corrects it. This section uses the chart formula of [the previous section](/entry/chart-formula/) to prove three facts about the potential $\varphi_\mu$ and the corrected weight $\varphi_\mu + U/2$. Both are plurisubharmonic and continuous off the boundary. The corrected weight is locally bounded, and $U$ and $\varphi_\mu$ grow at most like the logarithm of the logarithmic size of the chart. These facts give the regularisation settings that the height bounds of the next sections use. For the background see [hermitian line bundles](/learn/arakelov/#hermitian-line-bundles) and [toroidal compactifications](/learn/abelian-varieties/#toroidal-and-minimal-compactifications).

We keep the setting of the previous section: component data $D_c$ with charts $\gamma_a$ on the unit ball of $\mathbb{C}^n$ and boundary set $\mathrm{Bd}$, Hodge data with line $\mu$ and potential $\varphi_\mu$, and a component origin with Hodge component $\mathfrak{M}$. The off boundary part of the chart $a$ is the set of $t$ in the unit ball with $\gamma_a(t) \notin \mathrm{Bd}$. For a cusp weight $U$, the corrected weight is

$$
\psi_U(z) = \varphi_\mu(z) + \tfrac{1}{2} U(z).
$$

Each chart $a$ has a logarithmic size function $\ell_a \ge 1$ on the unit ball, which is large near the boundary. We do not unfold it.

**Lemma 8.5.1.** Assume the top level inputs, and let $U$ be a cusp weight for the origin. Let $a$ be a chart index and let $t_0$ be off the boundary. Then there is an open set $V \ni t_0$ on which $\varphi_\mu \circ \gamma_a$ is plurisubharmonic and continuous, and there is an open set $V' \ni t_0$ on which $\psi_U \circ \gamma_a$ is plurisubharmonic and continuous.

Lean: `GlobalTheory.CompanionTheory.Ar.Cusp.CorrPsh.near_all`

*Proof.* Take the chart formula at $t_0$, with $a_0$ punctured coordinates. The point $u = 0$ maps to $t_0$, which is off the boundary, so $0$ lies in the punctured ball. This forces $a_0 = 0$. Then the logarithmic cover is the unit ball, the exponential map is the identity, and the Riemann lattices $R_u$ form a holomorphic family on the unit ball with fixed form. The frames $b$ are eigenframes for this family. For such a family and a CM family $\sigma$, the log determinant $\operatorname{ld}_{R_u}(b(u))$ and the sum $\operatorname{ld}_{R_u}(b(u)) + \operatorname{cw}_\sigma(R_u)$ are plurisubharmonic, and the cusp weight $\operatorname{cw}_\sigma(R_u)$ is continuous. On the ball of radius $r$ the chart formula gives

$$
\begin{aligned}
\varphi_\mu(\gamma_a(t(u))) &= \operatorname{Re} G(u) + \tfrac{1}{2}\operatorname{ld}_{R_u}(b(u)), \\
\psi_U(\gamma_a(t(u))) &= \operatorname{Re} G(u) + \tfrac{1}{2}\big(\operatorname{ld}_{R_u}(b(u)) + \operatorname{cw}_\sigma(R_u)\big).
\end{aligned}
$$

The real part of a holomorphic function is pluriharmonic. The map $u \mapsto t(u) = t_0 + \rho\,(u \circ \pi)$ is an affine isomorphism, so the image $V$ of the ball of radius $r$ is an open set around $t_0$, and both properties transfer to $V$. $\square$

**Theorem 8.5.2 (Plurisubharmonicity of the Hodge weights).** Assume the top level inputs, let $E$ be an abelian Galois extension of $\mathbb{Q}$, and let $U$ be a cusp weight for the origin. Then for every chart $a$, the functions $\varphi_\mu \circ \gamma_a$ and $\psi_U \circ \gamma_a$ are plurisubharmonic and continuous on the off boundary part of the chart.

Lean: `GlobalTheory.CompanionTheory.Relay.cusp_intersection_positive` (also `GlobalTheory.T.cusp_intersection_positive`, a second name)

*Proof.* The off boundary part is open. Plurisubharmonicity is a local property, and the lemma gives it near every point. Continuity at each point follows from continuity on an open neighbourhood. $\square$

**Lemma 8.5.3.** Assume the top level inputs, let $U$ be a cusp weight for the origin, and assume that $\psi_U \circ \gamma_a$ is plurisubharmonic on the off boundary part of every chart. Let $a$ be a chart index and let $t_0$ be in the unit ball. Then there are $\varepsilon > 0$ and $C$ such that every $t$ off the boundary with $\|t - t_0\| < \varepsilon$ satisfies

$$
\begin{aligned}
|\psi_U(\gamma_a t)| &\le C, \\
U(\gamma_a t) &\le C \log \ell_a(t), \\
|\varphi_\mu(\gamma_a t)| &\le C \log \ell_a(t).
\end{aligned}
$$

Lean: `GlobalTheory.CompanionTheory.Ar.Cusp.CorrBdd.near_bdd`

*Proof.* Take the chart formula at $t_0$, with $a_0$ punctured coordinates. For $u$ in the punctured ball write $\lambda(u) = 1 + \log(1 + \sum_{i < a_0} |\log|u_i||)$. A lower bound for the Riemann form near the cusp gives $\rho_1 > 0$ and $C_1$ such that, for $|u| < \rho_1$,

$$
\operatorname{cw}_\sigma(R_w) \le C_1 \lambda(u), \qquad |\operatorname{ld}_{R_w}(b(u))| \le C_1 \lambda(u),
$$

where $u = e^w$. A second estimate near the centre gives $C_2$ with $\operatorname{ld} + \operatorname{cw} \ge -C_2$, and $|\operatorname{Re} G|$ is bounded by some $B$ near $0$. So on a small punctured ball the function $\psi_U \circ \gamma_a \circ t$ is plurisubharmonic, bounded below by $-B - C_2/2$, and bounded above by $(B + |C_1|)\lambda$. A plurisubharmonic function on a punctured ball with growth at most $C\lambda$ is bounded above on the punctured ball of half the radius. This gives $|\psi_U| \le C_3$. The same estimates bound $U$ and $\varphi_\mu$ by a multiple of $\lambda$, and $\lambda(u) \le A \log \ell_a(t(u))$ for a constant $A$. Since the inverse of $u \mapsto t(u)$ is continuous, a ball of radius $\varepsilon$ around $t_0$ maps into the small punctured ball. $\square$

**Theorem 8.5.4 (Log growth near the boundary).** Assume the top level inputs, let $E$ be an abelian Galois extension of $\mathbb{Q}$, and let $U$ be a cusp weight for the origin. Then the corrected weight $\psi_U$ is bounded near every point of every chart: for every $a$ and every $t_0$ in the unit ball there are $\varepsilon > 0$ and $C$ with $|\psi_U(\gamma_a t)| \le C$ for all $t$ off the boundary with $\|t - t_0\| < \varepsilon$. Also, for every $a$ and $t_0$ there are $\varepsilon > 0$ and $C$ with

$$
U(\gamma_a t) \le C \log \ell_a(t), \qquad |\varphi_\mu(\gamma_a t)| \le C \log \ell_a(t)
$$

for all such $t$.

Lean: `GlobalTheory.CompanionTheory.Ar.Cusp.CorrBdd.corr_bdd` (also `GlobalTheory.T.cusp_chart_log_growth_bounds`, a second name)

*Proof.* The theorem on plurisubharmonicity gives the hypothesis of the lemma, and the lemma gives both parts. $\square$

A complex model of the component data is a compact complex space with an atlas and a projection from the coordinates. A regularisation setting of log log type for a hermitian line $A$ consists of a smooth reference line with the weights of $A$, a regularising chart family, a mollifier, cutoff functions and functions $K(t)$ and $e_1(t)$. A bounded regularisation setting for a weight $w$ has the same parts, with bounded plurisubharmonic data in place of the log log data. A setting is tied if $e_1(t) \to 0$ as $t \to 0^+$ and the regularised potentials of two overlapping charts differ by at most $e_1(t)$ for small $t$. The log log type also asks that $K(t) \to \infty$ and that $K(t) \ge C \log\log(1/t)$ for small $t$. We do not unfold the regularisations.

**Theorem 8.5.5 (Tied regularisations of the cusp weight).** Assume the top level inputs, and let $E$ be an abelian Galois extension of $\mathbb{Q}$. Then there are a function $U$, a complex model of the component data, a regularisation setting $S$ of log log type for $\mu$ on the open part, and a bounded regularisation setting $S'$ for the corrected weight $\psi_U$, with these properties.

1. $U$ is a cusp weight for the origin, and $U \ge 0$.
2. On the open part, $U$ is invariant under the torus action: $U(t \cdot z) = U(z)$ for every $t \in (\mathbb{C}^\times)^K$.
3. $S$ and $S'$ are tied.
4. For every level $B \ge 4f + 2$ and all $1 \le p \le q$ there is $t_0 > 0$ such that, for $0 < t' \le t_0$, the regularised twisted line built from $S'$ with exponents $(p, q)$ at the parameter $t'$ is invariant under complex conjugation.

Lean: `GlobalTheory.CompanionTheory.Relay.cusp_weight_regularisations_tied` (also `GlobalTheory.T.cusp_weight_regularisations_tied`, a second name)

*Proof.* The intersection system gives a weight $U$ that is a cusp weight, nonnegative, torus invariant on the open part and conjugation invariant. The theorem on plurisubharmonicity gives that $\varphi_\mu$ and $\psi_U$ are plurisubharmonic on the charts and that $\psi_U$ is continuous there. The theorem on log growth gives that $\psi_U$ is locally bounded. The Hodge metric frames show that $\varphi_\mu$ and $\psi_U$ transform correctly under the torus action and under conjugation. With a complex model of the component data, the plurisubharmonicity of $\varphi_\mu$ gives a tied setting $S$ of log log type. The properties of $\psi_U$ give a tied bounded setting $S'$ with the conjugation property. $\square$

**Remark 8.5.6 (Formalization).** The plurisubharmonicity theorem `Relay.cusp_intersection_positive` (CuspIntersectionPositive.lean:268) assumes `[IsAbelianGalois ℚ E]`, but its proof only calls `near_all`, which does not take this instance. The proof introduces it as an anonymous `_` and never uses it. The log growth theorem `corr_bdd` (CuspIntersectionLimit.lean:220) carries the same instance only to call `T.cusp_intersection_positive`; its lemma `near_bdd` does not need it. The local plurisubharmonicity of log determinants is `T.log_det_eigen_frame_plurisubharmonic`, and the growth estimates are `T.riemann_form_lower_bound_near_cusp` and `T.psh_log_growth_bounded_near_puncture`. The regularisations come from `T.exists_regularization_of_hodge_metric` and `T.exists_regularization_setting`. We do not unfold these.
