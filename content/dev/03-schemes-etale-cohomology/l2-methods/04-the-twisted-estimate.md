---
title: The twisted estimate on the étale part
decls:
  - GlobalTheory.OTY.TwEst.twisted_estimate_nz
  - GlobalTheory.T.twistedEstimate_etalePart_manifold
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The twisted estimate on the étale part

This section proves the twisted $L^2$ estimate that is the analytic core of the extension theorem of Section 5. A section $h$ of $K_Y + E$ is given near the common zeros $S$ of sections $s_1, \dots, s_n$ of $L$. We cut $h$ off with a function of $\delta\psi$, where $\psi = n \log|s|^2$, and correct the result to a holomorphic section on the étale set $N(\tau)$ of Section 3. The error is bounded by the integral of $h$ over a thin shell around $S$. This is the method of Ohsawa and Takegoshi, in the form with a twist of the weight by a function of $\psi$.

We keep the notation of Sections 2 and 3. For global sections $s = (s_1, \dots, s_n)$ of $L$ put
$$\psi(y) = n \log |s|^2(y),$$
with the convention $\log 0 = 0$. So $\psi \le 0$ when $|s|^2 \le 1$, and $\psi = 0$ on $S$, while $\psi \to -\infty$ as $y$ tends to a point of $S$. Off $S$, the function $\psi$ is smooth in each chart. Its Levi form is that of $n \log \sum_k |s_{k,i}|^2$ minus $n$ times the Levi form of $\varphi^L_i$; the first term is the Levi form of a [[plurisubharmonic|FF2P7ER3QT]] function with poles on $S$ (compare the [[Poincaré-Lelong|B2YBWQQMHA]] formula).

**Definition 10.4.1 (Cutoff and weight).** Let $T > 0$. A *cutoff* for $T$ is a smooth function $\theta : \mathbb{R} \to [0,1]$ with $\theta(x) = 1$ for $x \le -T-1$, $\theta(x) = 0$ for $x \ge -T+1$, and $|\theta'(x)| \le 3/4$ for all $x$. The *truncated weight* is
$$w_T(x) = \frac{1}{1 + \min\bigl(x^2, (T+1)^2\bigr)}.$$

A cutoff exists for each $T \ge 1$, since $\theta$ must fall from $1$ to $0$ over an interval of length $2$, and $3/4 \cdot 2 > 1$. The weight $w_T$ equals $1/(1+x^2)$ for $|x| \le T + 1$, and it is constant for $|x| \ge T + 1$.

**Theorem 10.4.2 (Twisted estimate on the étale part).** Let $Y$ be compact with a weighted atlas of dimension $n$. Let $E, L \in \mathrm{La}$ and let $s = (s_1, \dots, s_n)$ be global sections of $L$ with $|s|^2 \le 1$ on $Y$. Let $\delta > 0$, and suppose that
$$\mathcal{L}_i\bigl(\varphi^E_i + \alpha\psi\bigr)(y)(\xi) \ge 0$$
for all $\alpha \in [1, 1+\delta]$, all charts $i$, all $y \in U_i \setminus S$ and all $\xi \in \mathbb{C}^n$. Let $\Lambda$, $\tau$, $z$ and $\beta$ satisfy the five conclusions of the theorem of Section 3, with $\tau$ a global section of $\Lambda$. Let $\Omega \subseteq Y$ be open and let $h$ be a section of $\kappa + E$ on $\Omega$ with $h = 0$ off $\Omega$. Let $T \ge 300$ and let $\theta$ be a cutoff for $T$. Suppose that each $y \notin S$ with $\delta\psi(y) \le -T+1$ lies in $\Omega$, and that $\int_Y |h|^2_{\kappa+E}\, d\mu < \infty$. Then there is a section $F$ of $\kappa + E$ on $N(\tau)$ with
$$\begin{aligned}
&\int_{N(\tau)} \bigl|\theta(\delta\psi)\, h - F\bigr|^2_{\kappa+E}\; w_T(\delta\psi)\, e^{-\psi}\, d\mu \\
&\qquad \le 30 \int_{\{-T-1 \le \delta\psi \le -T+1\}} |h|^2_{\kappa+E}\, e^{-\psi}\, d\mu.
\end{aligned}$$

Lean: `GlobalTheory.OTY.TwEst.twisted_estimate_nz` (also `GlobalTheory.T.twistedEstimate_etalePart_manifold`, a second name).

The section $\theta(\delta\psi) h$ is defined on all of $Y$: it is $h$ where $\delta\psi \le -T-1$, that is very near $S$, and it is $0$ where $\delta\psi \ge -T+1$. Where $\theta(\delta\psi) h$ is not zero, we have $\delta\psi \le -T+1$, so the point is in $\Omega$ or in $S$. The derivative $\bar\partial(\theta(\delta\psi) h) = \delta\,\theta'(\delta\psi)\, \bar\partial\psi \cdot h$ is supported in the shell $\{-T-1 \le \delta\psi \le -T+1\}$, and the right side of the estimate is an integral over that shell.

The proof uses a twisted form of Hörmander's estimate on an étale Stein space. We state it as we use it.

**Theorem 10.4.3 (Twisted extension on an étale Stein space).** Let $(M, z, e)$ be an étale Stein space of dimension $n$. Let $\varphi$ and $\psi \le 0$ be smooth on $M$, with $\mathcal{L}(\varphi + \alpha\psi) \ge 0$ for $\alpha \in [1, 1+\delta]$, where $\delta > 0$. Suppose $-\psi \le N e + C$ for a natural number $N$ and a constant $C$. Let $T \ge 300$, let $\theta$ be a cutoff for $T$, let $\Omega \subseteq M$ be open with $\{\delta\psi \le -T+1\} \subseteq \Omega$, and let $G$ be measurable on $M$ and holomorphic on $\Omega$, with $\int |\theta(\delta\psi) G|^2 e^{-\varphi}\, d\operatorname{vol} < \infty$. Then there is a holomorphic $F$ on $M$ with
$$\int_M \bigl|\theta(\delta\psi) G - F\bigr|^2 w_T(\delta\psi)\, e^{-(\varphi+\psi)}\, d\operatorname{vol} \le 30 \int_{\{-T-1 \le \delta\psi \le -T+1\}} |G|^2 e^{-(\varphi+\psi)}\, d\operatorname{vol}.$$

We take this theorem as given here, and we read only its statement. Its proof applies a twisted form of [Hörmander's estimate](/entry/hormander/) on the étale Stein space. In such a proof the weight is a function of $\delta\psi$, and the condition for all $\alpha \in [1, 1+\delta]$ is what keeps the curvature term nonnegative after the twist.

*Proof of the twisted estimate on the étale part.* Write $U = N(\tau)$.

First, $U$ is an étale Stein space. The map $z$ is étale on $U$, so it is a local homeomorphism of $U$ to $\mathbb{C}^n$. Put $e = -\log|\tau|^2_\Lambda$ on $U$. In the chart $i$ this is $-\log|\tau_i|^2 + \varphi^\Lambda_i$. The first term is pluriharmonic where $\tau_i \neq 0$, and $\Lambda$ is semipositive, so $e$ has nonnegative Levi form. For $c \in \mathbb{R}$ the set $\{e \le c\} = \{|\tau|^2_\Lambda \ge e^{-c}\}$ is closed in the compact space $Y$ and lies in $U$, so it is compact. Hence $(U, z, e)$ is an étale Stein space.

Second, the bound on $\psi$. Since $|s|^2 \le 1$, we have $\psi \le 0$. By item 5 of Section 3, $|\tau|^2_\Lambda \le C |s|^2$, so $\log|s|^2 \ge -e - \log C$ on $U$, and
$$-\psi \le n e + n \log C.$$

Third, the weight. On $U$ the frame $\beta$ of $\kappa + E$ has no zero and $z$ is étale. Write a section $F$ of $\kappa + E$ on an open set of $U$ as $F = G \beta$ for a function $G$. The Jacobian $\det dz$, with the value $\det d(z \circ \phi_i^{-1})$ in the chart $i$, is a section of $\kappa$ on $U$, because the Jacobians of the chart changes are the cocycle of $\kappa$. In terms of the coordinates $z$, the measure and the norm become
$$|F|^2_{\kappa+E}\, d\mu = |G|^2 e^{-\varphi}\, d\operatorname{vol}, \qquad \varphi = -\log|\beta|^2_{\kappa+E} + \log|\det dz|^2_{\kappa},$$
where $\operatorname{vol}$ is the fibre measure of $z$. Indeed, in the chart $i$ we have $d\mu = e^{\varphi^\kappa_i} dv$ and $dv = |\det d(z \circ \phi_i^{-1})|^{-2} d\operatorname{vol}$, and the factors $e^{\pm\varphi^\kappa_i}$ cancel. So in the chart $i$,
$$\varphi = -\log|\beta_i|^2 + \log\bigl|\det d(z \circ \phi_i^{-1})\bigr|^2 + \varphi^E_i.$$
The first two terms are pluriharmonic, since $\beta_i$ and the Jacobian are holomorphic without zeros on $U$. So $\mathcal{L}\varphi = \mathcal{L}\varphi^E_i$, up to the linear change of coordinates from $\phi_i$ to $z$, which keeps the sign of a Levi form. The hypothesis on $\varphi^E + \alpha\psi$ off $S$ gives $\mathcal{L}(\varphi + \alpha\psi) \ge 0$ on $U$ for $\alpha \in [1, 1+\delta]$. The functions $\varphi$ and $\psi$ are smooth on $U$, since $U \cap S = \emptyset$.

Fourth, the data. Let $G = h/\beta$ on $U$. It is holomorphic on $U \cap \Omega$ and zero off $\Omega$, so it is measurable. The open set $U \cap \Omega$ contains $\{y \in U : \delta\psi(y) \le -T+1\}$ by hypothesis, since $U$ does not meet $S$. By the transfer of measures in the third step and $0 \le \theta \le 1$,
$$\int_U |\theta(\delta\psi) G|^2 e^{-\varphi}\, d\operatorname{vol} = \int_U \theta(\delta\psi)^2 |h|^2_{\kappa+E}\, d\mu \le \int_Y |h|^2_{\kappa+E}\, d\mu < \infty.$$

Now the twisted extension theorem on $(U, z, e)$ with $\varphi$, $\psi$, $N = n$, $\Omega \cap U$ and $G$ gives a holomorphic $F_0$ on $U$ with the estimate in the variables of $U$. Put $F = F_0 \beta$, a section of $\kappa + E$ on $U$. Since $\theta(\delta\psi) h - F = (\theta(\delta\psi) G - F_0)\beta$, the transfer of measures turns both sides of the estimate into the two sides of the claimed estimate. $\square$

The density of $N(\tau)$ is not used in this proof. It is used in Section 5, to extend $F$ across the hypersurface $\{\tau = 0\}$.

**Remark 10.4.4 (Formalization).** The cutoff is `IsCut T θ` and the weight is `wT T` in Definitions/Divisors/EtaleEmpty.lean, lines 63 to 67. The function $\psi$ is `psi A L s`, defined with `Real.log`, so $\psi = n \log 0 = 0$ on $S$. The twisted extension theorem is `twisted_extension_etaleStein_logGrowthWeight`, used through its second name in the `T` namespace; it reaches `hormander` through `twistedExtension_etaleStein_sqIntegrable`, `twistedExtension_sqInt` and `tw`. The first and third steps are `nonvanishingSet_etale_stein` and `frameWeight_singularWeight_smooth_leviNonneg`, the second step is `nz_facts`, and the transfer of measures is `lintegral_weightedAtlas_frame_etale_transfer` with `weighted_l2_estimate_twisted_sections`. We read the statements of these results, not their proofs. The density hypothesis of item 4 of Section 3 is taken apart as `_hdense` and not used.
