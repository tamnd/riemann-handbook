---
title: L2 extension from the common zeros of sections
decls:
  - GlobalTheory.l2_extension_of_etale_coordinates
  - GlobalTheory.T.l2_extension_etale_coordinates_finite_zeros
  - GlobalTheory.l2ExtensionLogCanonical'
status: drafted
drafted_by: writer@claude-opus-5-5
---
## L2 extension from the common zeros of sections

This section proves an $L^2$ extension theorem of Ohsawa-Takegoshi type from a finite set. On a compact complex manifold $Y$ of dimension $n$ let $S$ be the common zero set of $n$ sections $s_1, \dots, s_n$ of $L$, finite and with nonzero Jacobian. Then any values on $S$ are the values of a global section of $K_Y + E$, with an $L^2$ bound in terms of the values and the Jacobians. The result is the statement that the literature layer of the proof takes as an input ([L2 extension from the literature](/entry/l2-extension-log-canonical-of-literature/)). That statement is one of the published results that [the literature layer](/proof/literature/) collects in one bundle for its arithmetic part.

We keep the notation of Sections 2 to 4, with $\psi = n\log|s|^2$ and $\log 0 = 0$.

**Definition 10.5.1 (Jacobian and residue norm).** Let $s = (s_1, \dots, s_n)$ be global sections of $L$ and $P \in Y$. The *Jacobian* $J_s(P)$ is the Jacobian determinant at $\phi_{i(P)}(P)$ of the map $v \mapsto (s_{k,i(P)}(\phi_{i(P)}^{-1} v))_{k=1}^n$, that is, of the $s_k$ in the chart $i(P)$ and the trivialisation of $L$ there. For $c \in \mathbb{C}$ and $E \in \mathrm{La}$ put
$$\operatorname{res}_P(c) = \Bigl|\frac{c}{J_s(P)}\Bigr|^2 e^{-\varphi^E_{i(P)}(P) + n\varphi^L_{i(P)}(P)}, \qquad c_n = \frac{2^{n+1}\pi^n}{(n-1)!}.$$

If $P \in S$ and the chart at $P$ is changed, $J_s(P)$ is multiplied by $(g^L)^n$ times the Jacobian of the chart change. The factor $e^{n\varphi^L}$ absorbs the first, and the second is the change of a value of a section of $\kappa$. So $\operatorname{res}_P(F(P))$ is an intrinsic norm of the value of a section $F$ of $\kappa + E$ at $P$, and it is the residue of $|F|^2 e^{-\psi}$ at $P$ up to the constant $c_n$.

**Theorem 10.5.2 ($L^2$ extension with étale coordinates).** Let $Y$ be compact with a weighted atlas of dimension $n \ge 1$. Let $E, L \in \mathrm{La}$ and let $s = (s_1, \dots, s_n)$ be global sections of $L$ with:

1. the common zero set $S$ of the $s_k$ is finite;
2. $J_s(P) \neq 0$ for each $P \in S$;
3. $|s|^2 \le 1$ on $Y$.

Let $\delta > 0$, and suppose that $\mathcal{L}_i(\varphi^E_i + \alpha\psi)(y)(\xi) \ge 0$ for all $\alpha \in [1, 1+\delta]$, all charts $i$, all $y \in U_i \setminus S$ and all $\xi$. Let $\Lambda$, $\tau$, $z$ and $\beta$ satisfy the five conclusions of the theorem of Section 3, with $\tau$ a global section of $\Lambda$. Then for each function $f : Y \to \mathbb{C}$ there is a global section $F$ of $\kappa + E$ with $F(P) = f(P)$ for each $P \in S$ and
$$\int_Y \frac{2^n}{1 + (\delta\psi)^2}\, |F|^2_{\kappa+E}\, e^{-\psi}\, d\mu \le \frac{34}{\delta}\, c_n \sum_{P \in S} \operatorname{res}_P(f(P)).$$

Lean: `GlobalTheory.l2_extension_of_etale_coordinates` (also `GlobalTheory.T.l2_extension_etale_coordinates_finite_zeros`, a second name).

The weight $e^{-\psi} = |s|^{-2n}$ is not integrable near a point of $S$, because $s$ is a coordinate system there with a simple zero. So a section with a finite integral is forced to have the right values on $S$, and the bound is in terms of these values only.

*Proof.* Write $\Sigma = \sum_{P \in S} \operatorname{res}_P(f(P))$. Each term is $\ge 0$.

*The case $\Sigma = 0$.* Then $f(P)/J_s(P) = 0$ for each $P \in S$, and $J_s(P) \neq 0$, so $f(P) = 0$. Take $F = 0$.

*The case $\Sigma > 0$.* We use three facts, of which we read only the statements.

- (a) *Local extension.* There are an open set $\Omega$, a section $h$ of $\kappa + E$ on $\Omega$ with $h = 0$ off $\Omega$, and $m > 0$, such that: each $y$ with $|s|^2(y) < m$ lies in $\Omega$; $h(P) = f(P)$ for $P \in S$; for each $T \ge 2$,
$$\int_{\{-T-1 \le \delta\psi \le -T+1\}} |h|^2_{\kappa+E}\, e^{-\psi}\, d\mu \le \frac{62}{30} \cdot \frac{\pi^n}{(n-1)!\,\delta}\, \Sigma;$$
and $\int_Y \frac{1}{1+(\delta\psi)^2} |h|^2_{\kappa+E} e^{-\psi}\, d\mu < \infty$. In the coordinates $s$ near $P$, $h$ is the constant section with value $f(P)$, and the shell integral is an integral of $|v|^{-2n}$ over a shell in $\mathbb{C}^n$. The constant comes from the volume $2\pi^n/(n-1)!$ of the unit sphere of $\mathbb{C}^n$, with some slack.
- (b) *Small tails.* A function with finite integral has small integral over the sets $\{\delta\psi \le -T+1\}$ for large $T$, since these sets shrink to $S$, which has measure zero.
- (c) *Extension across the hypersurface.* Let $\theta$ be a cutoff for $T$ and $F_1$ a section of $\kappa + E$ on $N(\tau)$ such that the integral of $|\theta(\delta\psi) h - F_1|^2 w_T(\delta\psi) e^{-\psi}$ over $N(\tau)$ is finite. Suppose $S \subseteq \Omega$ and $\int |h|^2 d\mu < \infty$. Then there is a global section $G$ of $\kappa + E$ with $G = F_1$ on $N(\tau)$ and $G(P) = h(P)$ for $P \in S$. The section $F_1$ is in $L^2$ near the hypersurface $\{\tau = 0\}$, so it extends holomorphically across it, by the Riemann extension theorem for $L^2$ holomorphic functions. Near $P \in S$ the weight $e^{-\psi}$ is not integrable and $\theta(\delta\psi) = 1$, so $G(P) = h(P)$.

First, $\psi \le 0$ since $|s|^2 \le 1$. For $t \le 0$ one has $\frac{1}{1 + (\delta t)^2} e^{-t} \ge \min\bigl(1, \frac{1}{2\delta^2}\bigr)$, so the last property in (a) gives $\int |h|^2_{\kappa+E}\, d\mu < \infty$.

Put
$$K = \frac{\pi^n}{(n-1)!\,\delta}\, \Sigma > 0.$$
By (b) there is $T_0$ such that
$$32 \int_{\{\delta\psi \le -T+1\}} \frac{1}{1+(\delta\psi)^2}\, |h|^2_{\kappa+E}\, e^{-\psi}\, d\mu \le 4K \quad \text{for } T \ge T_0.$$
Let $T = \max(300, T_0, 2 - \delta n \log m)$. If $\delta\psi(y) \le -T+1$, then $n\delta \log|s|^2(y) \le -T + 1 < \delta n \log m$, so $|s|^2(y) < m$ and $y \in \Omega$. In particular every $y \notin S$ with $\delta\psi(y) \le -T+1$ lies in $\Omega$, and $S \subseteq \Omega$ since $|s|^2 = 0 < m$ on $S$.

Let $\theta$ be a cutoff for $T$. The [twisted estimate](/entry/twisted-estimate-nz/) of Section 4 applies, with $\Omega$, $h$, $T$ and $\theta$. It gives a section $F_1$ of $\kappa + E$ on $N(\tau)$ with
$$\int_{N(\tau)} \bigl|\theta(\delta\psi) h - F_1\bigr|^2_{\kappa+E}\, w_T(\delta\psi)\, e^{-\psi}\, d\mu \le 30 \cdot \frac{62}{30} K = 62K,$$
by (a) with $T \ge 2$. This is finite, so (c) gives a global section $G$ of $\kappa + E$ with $G = F_1$ on $N(\tau)$ and $G(P) = h(P) = f(P)$ for $P \in S$. Take $F = G$.

It remains to prove the bound. The set $N(\tau)$ is dense and is the complement of the zero set of a section that is not zero on any component, so its complement has measure zero. Fix $y \in N(\tau)$ and put $x = \delta\psi(y)$, $u = \theta(x) h(y)$ and $v = \theta(x) h(y) - F_1(y)$, so that $F(y) = u - v$. For complex numbers,
$$|u - v|^2 \le \tfrac{32}{31} |v|^2 + 32 |u|^2.$$
Since $1/(1+x^2) \le w_T(x)$ and $u = 0$ unless $x \le -T+1$,
$$\frac{|F(y)|^2 e^{-\psi(y)}}{1 + x^2} \le \tfrac{32}{31}\, |v|^2 w_T(x) e^{-\psi(y)} + 32\, \mathbf{1}_{\{x \le -T+1\}}\, \frac{|h(y)|^2 e^{-\psi(y)}}{1+x^2},$$
with pointwise norms in $\kappa + E$ and $0 \le \theta \le 1$. Integrate over $Y$ and multiply by $2^n$:
$$\int_Y \frac{2^n}{1+(\delta\psi)^2} |F|^2_{\kappa+E} e^{-\psi}\, d\mu \le 2^n\Bigl(\tfrac{32}{31} \cdot 62K + 4K\Bigr) = 2^n \cdot 68K.$$
Finally $2^n \cdot 68 K = \frac{34}{\delta} \cdot \frac{2^{n+1}\pi^n}{(n-1)!}\, \Sigma = \frac{34}{\delta} c_n \Sigma$. $\square$

The theorem has the data $\Lambda$, $\tau$, $z$, $\beta$ as hypotheses. Section 3 removes them, at the price of a positive bundle.

**Theorem 10.5.3 ($L^2$ extension from a finite set).** Let $Y$ be compact with a weighted atlas of dimension $n \ge 1$, and suppose that some $H \in \mathrm{La}$ is positive. Let $E, L \in \mathrm{La}$ and let $s = (s_1, \dots, s_n)$ be global sections of $L$ with items 1 to 3 of the last theorem. Let $\delta > 0$, and suppose that $\mathcal{L}_i(\varphi^E_i + \alpha\psi)(y)(\xi) \ge 0$ for all $\alpha \in [1, 1+\delta]$, all charts $i$, all $y \in U_i \setminus S$ and all $\xi$. Then for each function $f : Y \to \mathbb{C}$ there is a global section $F$ of $\kappa + E$ with $F(P) = f(P)$ for each $P \in S$ and
$$\int_Y \frac{2^n}{1 + (\delta\psi)^2}\, |F|^2_{\kappa+E}\, e^{-\psi}\, d\mu \le \frac{34}{\delta}\, c_n \sum_{P \in S} \operatorname{res}_P(f(P)).$$

Lean: `GlobalTheory.l2ExtensionLogCanonical'`.

*Proof.* The [étale frame theorem](/entry/exists-etale-frame-of-finite-zero-set/) of Section 3 gives $\Lambda$, $\tau$, $z$ and $\beta$ from $H$, $E$, $L$, $s$ and the finiteness of $S$. The last theorem, applied to these data and to the other hypotheses, gives $F$. $\square$

The name of the statement refers to the weight $e^{-\psi} = |s|^{-2n}$. The $s_k$ have a simple common zero at each point of $S$, so the exponent $n$ is the log canonical threshold of the ideal that they generate: it is the first exponent for which the weight is not integrable near $S$. The factor $1/(1+(\delta\psi)^2)$ makes the integral of $|F|^2 e^{-\psi}$ finite in spite of this pole, and the bound then depends only on the values of $F$ on $S$.

**Remark 10.5.4 (Formalization).** The statement is the proposition `L2ExtensionLogCanonical` in PublishedTheorems/Divisors₂/L2ExtensionLogCanonical.lean, line 32, with `jacAt`, `psi`, `resSq` and `resConst` defined above it. The facts (a), (b) and (c) are `exists_local_holomorphic_extension_near_zeros`, `lintegral_sublevel_tail_le_of_finite` and `extension_across_hypersurface_values_at_zeros`, used through their second names in the `T` namespace. We read their statements, not their proofs, and the reasons given for them are the standard ones. The elementary steps are `norm_sub_sq_le_of_split`, `weight_ge_of_nonpos` and `final_pointwise_le`, in the same file as the theorem. The factor $2^n$ and the constant $34/\delta$ come from the slack constants $62/30$, $30$ and $32/31$ of the proof, not from a sharp computation. We have not matched them to a numbered theorem of a source. The only direct user of `l2ExtensionLogCanonical'` is `UpperTheory.LiteratureTheorems.l2_extension_log_canonical_of_literature`.
