---
title: Uniform integrability of Green functions
decls:
  - GroundTheory.Heights₂.Heights.AnalyticLimit.UniformIntegrability.full
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Uniform integrability of Green functions

This section proves that the regularized Green function $\log(1 + \varepsilon/\|s\|^2)$ of a section $s$ has small integral against a product of regularized semipositive forms, uniformly in the regularization parameter $t$, when $\varepsilon$ and $t$ are small. The forms may have logarithmic singularities along a boundary, and the bound uses only a tail estimate near that boundary. The result is the input [that the uniform integrability holds](/entry/unif-int-holds/) of the chapter on sup norms of theta functions. There it lets one pass to the limit $t \to 0$ in the integrals that define a height.

### The data

Let $X$ be a compact Hausdorff complex manifold of dimension $D + 1$, given by a finite holomorphic atlas. Forms are given by local potentials: a potential $P$ is a family of smooth local functions whose differences are real parts of holomorphic functions, and the form of $P$ is its complex Hessian (the Levi form). For potentials $P_0, \dots, P_{n-1}$ on a manifold of dimension $n$ and a function $g$, write $\int g\, P_0 \cdots P_{n-1}$ for the integral of $g$ against the mixed Monge-Ampère density of the $P_i$, computed in charts with a partition of unity.

**Definition 4.11.1 (Uniform integrability data).** The data consist of the following.

1. A Kähler form $\Omega$ on $X$, that is, a potential with positive definite Levi form.
2. A line bundle with weight $\varphi_L$ and a holomorphic section $s$, with norm $\|s\| = |s| e^{-\varphi_L}$, whose divisor has simple normal crossings: $\operatorname{div}(s) = \sum_k m_k \Delta_k$, where each $\Delta_k$ is a complex manifold of dimension $D$ with a holomorphic inclusion into $X$.
3. An open set $Y^\circ \subseteq X$ whose complement is an analytic subset with empty interior, and the same on each $\Delta_k$.
4. A function $r$ on $X$, and constants $C$, $C_1$, $C_E$ and $\ell_0$.
5. For $a = 0, \dots, D$, potentials $\theta_a$, functions $u_a(t)$ for $t > 0$, and limit functions $\lambda_a$.

Put $\ell(t) = \log(1/t)$ and $e_C(t) = C \log \ell(t)/\ell(t)$, and let $T_a(t) = \theta_a + u_a(t)$ be the potential of $\theta_a + dd^c u_a(t)$. For all $t > 0$ with $\ell(t) \ge \ell_0$, the data satisfy:

- each $u_a(t)$ is smooth on $X$, the forms satisfy $-\Omega \le \theta_a \le \Omega$, the form $T_a(t)$ is semipositive on $Y^\circ$, and $-C_1 \log r \le u_a(t) \le 0$ on $Y^\circ$;
- $\lambda_a \le u_a(t)$ on $Y^\circ$, and $u_a(t) \le \lambda_a + t^{1/3} + e_C(t)$ at the points of $Y^\circ$ with $r \le \ell(t)$;
- $u_a(t) \le u_a(t_0) + C e_C(t_0)$ on $X$ when $t \le t_0$ and $\ell(t_0) \ge \ell_0$;
- the tail bounds: for each $b \le D$, for the product $R$ of $T_0(t), \dots, T_{b-1}(t)$ with copies of $\Omega$ in the other slots, and for every $R_0 \ge e$,
$$\int_{\{x \in Y^\circ : r(x) \ge R_0\}} \log r \; R \le C_E\, \frac{(\log R_0)^{n+1}}{R_0},$$
where $n$ is the dimension; the same bound holds on each $\Delta_k$ for the restrictions of the products of $D$ such forms.

The function $r$ measures the distance to the boundary $X \setminus Y^\circ$: it is large near the boundary. The functions $u_a(t)$ are regularizations of the singular potentials $\lambda_a$, and they decrease to $\lambda_a$ at a controlled rate.

**Definition 4.11.2 (Green function).** For $\varepsilon > 0$ put $g_\varepsilon = \log(1 + \varepsilon/\|s\|^2)$.

The function $g_\varepsilon$ is nonnegative, it is smooth off the divisor of $s$, it decreases to $0$ as $\varepsilon \to 0$ off the divisor, and it has a logarithmic singularity along $\operatorname{div}(s)$.

### The theorem

**Theorem 4.11.3 (Uniform integrability).** For every set of uniform integrability data and every $\eta > 0$, there are $\varepsilon_0 > 0$ and $t_1 > 0$ such that
$$\int_X g_\varepsilon\, T_0(t) \cdots T_D(t) \le \eta$$
for all $0 < \varepsilon \le \varepsilon_0$ and all $0 < t \le t_1$ with $\ell(t) \ge \ell_0$.

Lean: `GroundTheory.Heights₂.Heights.AnalyticLimit.UniformIntegrability.full` (also `GroundTheory.Heights₂.Heights.AnalyticLimit.UniformIntegrability.proof`)

The proof replaces the forms $T_a(t)$ by $\Omega$ one at a time. For $a = 0, \dots, D + 1$ let $R_a(t)$ be the product of $T_0(t), \dots, T_{a-1}(t)$ with $D - a$ copies of $\Omega$ (for $a \le D$), and put
$$J_a(\varepsilon, t) = \int_X g_\varepsilon\, T_0(t) \cdots T_{a-1}(t)\, \Omega^{D + 1 - a}.$$
So $J_0 = \int g_\varepsilon\, \Omega^{D+1}$ and $J_{D+1}$ is the integral of the theorem. Four lemmas control $J_a$. In the second and third lemma, $a \le D$, and
$$\kappa_\varepsilon = 2\varphi_L + \log(\|s\|^2 + \varepsilon)$$
is the regularized curvature potential.

**Lemma 4.11.4 (Start).** For every $\eta > 0$ there is $\varepsilon_0 > 0$ with $J_0(\varepsilon, t) \le \eta$ for all $0 < \varepsilon \le \varepsilon_0$ and all $t$.

Lean: `GroundTheory.Heights₂.Heights.AnalyticLimit.GreenMassZero.full`

*Proof.* $J_0$ does not depend on $t$: it is the integral of $g_\varepsilon$ against the measure $\mu$ of $\Omega^{D+1}$. For $0 < \varepsilon \le 1$ we have $0 \le g_\varepsilon \le g_1 = \log(\|s\|^2 + 1) - 2\log\|s\|$, and $g_1$ is $\mu$-integrable, because $\log\|s\|$ is integrable for a section with normal crossings. Since $g_\varepsilon \to 0$ pointwise as $\varepsilon \to 0$, dominated convergence gives $\int g_\varepsilon\, d\mu \to 0$. $\square$

**Lemma 4.11.5 (Step).** For $0 < \varepsilon$ and $0 < t$ with $\ell(t) \ge \ell_0$,
$$J_{a+1}(\varepsilon, t) \le J_a(\varepsilon, t) + P_a(\varepsilon, t),$$
where
$$P_a(\varepsilon, t) = \int_X u_a(t)\, \kappa_\varepsilon\, R_a(t) - 2 \sum_k m_k \int_{\Delta_k} u_a(t)\, R_a(t).$$

Lean: `GroundTheory.Heights₂.Heights.AnalyticLimit.GreenMassStep.full`

*Proof.* Move slot $a$ to the front. Off the divisor, $g_\varepsilon = \log(\|s\|^2 + \varepsilon) - 2\log\|s\|$, and the divisor is a null set. In $J_{a+1}$ the slot $a$ holds $T_a = \theta_a + u_a$; in $J_a$ it holds $\Omega = \theta_a + (\Omega - \theta_a)$. The form of $\Omega - \theta_a$ is semipositive and $g_\varepsilon \ge 0$, so $\int g_\varepsilon\, \theta_a R_a \le J_a$. It remains to treat $\int g_\varepsilon\, dd^c u_a\, R_a$. Symmetry of the mixed integral for the smooth function $\log(\|s\|^2 + \varepsilon)$ moves $dd^c$ onto it. For the term $-2\log\|s\|$, the Poincaré-Lelong formula gives
$$\int_X (-2\log\|s\|)\, dd^c u_a\, R_a = 2\int_X u_a\, \varphi_L\, R_a - 2\sum_k m_k \int_{\Delta_k} u_a\, R_a.$$
The sum of the two terms is $P_a$. $\square$

**Lemma 4.11.6 (Replacement).** There is $C_\kappa \ge 0$ such that for every $a \le D$ and every $t_0 > 0$ with $\ell(t_0) \ge \ell_0$ there is $K \ge 0$ with
$$P_a(\varepsilon, t) \le K J_a(\varepsilon, t) + C_\kappa E_W(t_0, t) + 2E_\Delta(t_0, t)$$
for $0 < \varepsilon \le 1$ and $0 < t \le t_0$. Here $h = u_a(t_0) + C e_C(t_0) - u_a(t)$ is the gap, $E_W = \int_X h\, \Omega\, R_a(t)$ and $E_\Delta = \sum_k m_k \int_{\Delta_k} h\, R_a(t)$.

Lean: `GroundTheory.Heights₂.Heights.AnalyticLimit.GreenMassReplace.full`

*Proof.* Since $\varphi_L$ is smooth and $X$ is compact, there is $C_\kappa$ with $\kappa_\varepsilon + C_\kappa \Omega$ semipositive for all $\varepsilon > 0$. Put $v = u_a(t_0) + C e_C(t_0)$, a smooth function, so that $u_a(t) = v - h$ with $h \ge 0$ by the monotonicity condition. By linearity, $P_a(u_a(t)) = P_a(v) - \int h\, \kappa_\varepsilon R_a + 2E_\Delta$. The Poincaré-Lelong formula and symmetry, read backwards, give $P_a(v) = \int g_\varepsilon\, dd^c v\, R_a$. On the compact space $X$ there is $K$ with $|dd^c v| \le K\Omega$, so $P_a(v) \le K J_a$, since $g_\varepsilon \ge 0$ and $R_a$ is semipositive on the dense open set $Y^\circ$. Finally $-\int h\,\kappa_\varepsilon R_a \le C_\kappa \int h\,\Omega R_a = C_\kappa E_W$, by the semipositivity of $\kappa_\varepsilon + C_\kappa\Omega$. $\square$

**Lemma 4.11.7 (Error).** For every $a \le D$ and $\delta > 0$ there is $\tau > 0$ such that $E_W(t_0, t) \le \delta$ and $E_\Delta(t_0, t) \le \delta$ for all $0 < t \le t_0 \le \tau$ with $\ell(t_0) \ge \ell_0$.

Lean: `GroundTheory.Heights₂.Heights.AnalyticLimit.GreenMassError.full`

*Proof.* Let $N(t_0) = t_0^{1/3} + |e_C(t_0)| + |C|\,|e_C(t_0)|$, which tends to $0$ as $t_0 \to 0$. On $Y^\circ$ the gap satisfies
$$0 \le h \le |C_1| \log r \cdot \mathbf{1}_{\{r \ge \ell(t_0)\}} + N(t_0).$$
Where $r \le \ell(t_0)$, use $\lambda_a \le u_a(t)$ and the upper bound of $u_a(t_0)$ by $\lambda_a$. Where $r > \ell(t_0)$, use $u_a(t_0) \le 0$ and $u_a(t) \ge -C_1 \log r$. The total mass of $\Omega R_a(t)$ is a cohomological quantity and does not depend on $t$. The tail bound with $R_0 = \ell(t_0)$ gives
$$\begin{aligned}
E_W &\le N(t_0) \int_X \Omega R_a + |C_1|\,|C_E|\, \frac{(\log \ell(t_0))^{D+2}}{\ell(t_0)},
\end{aligned}$$
and the same estimate with exponent $D + 1$ on each $\Delta_k$ bounds $E_\Delta$. Both bounds tend to $0$ as $t_0 \to 0$. $\square$

*Proof of the theorem.* We prove by induction on $a \le D + 1$: for every $\eta > 0$ there are $\varepsilon_0, t_1 > 0$ with $J_a(\varepsilon, t) \le \eta$ for $0 < \varepsilon \le \varepsilon_0$, $0 < t \le t_1$ and $\ell(t) \ge \ell_0$. For $a = 0$ this is the start lemma, with $t_1 = 1$.

Let $a < D + 1$ and $\eta > 0$. Take $C_\kappa$ from the replacement lemma, put $\delta = \eta/(2(C_\kappa + 2))$, and take $\tau$ from the error lemma. Let $t_0 = \min(\tau, e^{-\ell_0})$, so that $\ell(t_0) \ge \ell_0$, and take $K$ from the replacement lemma for this $t_0$. By induction there are $\varepsilon_1, t_2$ with $J_a \le \eta/(2(K + 1))$. Put $\varepsilon_0 = \min(\varepsilon_1, 1)$ and $t_1 = \min(t_2, t_0)$. For $\varepsilon \le \varepsilon_0$ and $t \le t_1$, the step and the replacement lemmas give
$$\begin{aligned}
J_{a+1} &\le J_a + P_a \le (1 + K) J_a + C_\kappa E_W + 2E_\Delta \\
&\le \frac{\eta}{2} + (C_\kappa + 2)\,\delta = \eta.
\end{aligned}$$
For $a = D + 1$, all slots hold the forms $T_a(t)$, and $J_{D+1}$ is the integral of the theorem. $\square$

**Remark 4.11.8.** The order of the choices matters. The constant $K$ depends on the second derivatives of $u_a(t_0)$, so $t_0$ must be fixed before $K$, and the induction hypothesis must then give $J_a$ smaller than $\eta/(2(K+1))$. The tail bound is the only place where the singularities of the forms near the boundary enter. The rate $(\log R_0)^{n+1}/R_0$ is what makes the logarithmic growth of $u_a(t)$ near the boundary harmless.

**Remark 4.11.9 (Formalization).** The statement is in [UIObjects.lean](lean:GroundTheory/HeightsAndTheta/Heights/AnalyticLimit/UIObjects.lean#L128), the induction in [UniformIntegrability.lean](lean:GroundTheory/HeightsAndTheta/Heights/AnalyticLimit/UniformIntegrability.lean#L19), and the final assembly in [OfListTailLog.lean](lean:GroundTheory/HeightsAndTheta/Heights/AnalyticLimit/OfListTailLog.lean#L24). The data are the structure `UIData` ([UIObjects.lean](lean:GroundTheory/HeightsAndTheta/Heights/AnalyticLimit/UIObjects.lean#L43)). The condition on each $u_a(t)$ asks for a bounded potential form and for smoothness on all of $X$; the second makes the smoothness on $Y^\circ$ and the alternative "smooth or with a pole" in the bounded form automatic ([Objects.lean](lean:GroundTheory/HeightsAndTheta/Heights/AnalyticLimit/Objects.lean#L55)). The function $r$ has no hypotheses of its own; it enters only through the tail bounds. The mixed integral is defined as $0$ when the atlas has no partition of unity. The normalization of $dd^c$ is the one of the development, which is why the Poincaré-Lelong formula carries the factor $2$.
