---
title: The tower conditions
decls:
  - GlobalTheory.T.full_intersection_tower_I8_identity
  - GlobalTheory.CompanionTheory.Ar.Top.full_intersection_tower_I8_relation
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The tower conditions

The volume theorem is proved by a chain of conditions on a root tower. Some conditions are geometric (proportionality, nefness, semipositivity), some are bounds for heights of points, and some are identities between intersection numbers (antisymmetry, the power sum formula, label invariance). This section defines them all, so that later sections can refer to them by their labels, and proves one of them, the antisymmetry I8, for good towers. The labels are those of [the chapter on good towers](/entry/good-tower-volume-of-reduced/).

Fix a root tower $T$ of type $(\Psi, N)$ with index $j$, bad primes $\mathcal{B}$ and twist weight $\nu$, and an intersection system $\mathrm{II}$. All objects are as in the [previous section](/entry/t-flag-degree-polynomial-eval/). For a weight $\lambda$ and $s > 0$ put $\lambda_s = \lambda - s\nu$ and $t(s) = e^{-1/s^2}$. The $j$-gap of $\lambda$ at $\tau$ is $\operatorname{gap}_j(\lambda, \tau) = \lambda(\tau, j-1) - \lambda(\tau, j)$. A wall of $\lambda$ is a pair $(\tau, a)$ with $\lambda(\tau, a) = \lambda(\tau, a+1)$.

**Definition 9.2.1 (Twisted numbers).** For $B \ge 2$, a component $c$, a weight $\lambda$ and $s > 0$ put

$$
\begin{aligned}
\overline{m}_B(c, \lambda, s) &= \mathrm{ar}_{t(s)}\big(L_{\lambda_s, s}^{\,d+1}\big), \\
m_B(c, \lambda, s) &= \mathrm{geo}\big(L_{\lambda_s, s}^{\,d}\big),
\end{aligned}
$$

on the model $M_{B, c}$. For a closed point $W$ of $M_{B,c}$, that is an arithmetic subvariety of dimension $1$, the height $\overline{h}_B(c, \lambda, s, W)$ is the height of $W$ for the line $L_{\lambda_s, s}$ at $t(s)$, divided by the degree of $W$.

**Definition 9.2.2 (Positivity).** The model $M$ is nef on the fibres at $\mu, s$ if the line $L_{\mu, s}$ has nonnegative degree on every vertical curve over every prime $p$. It is nef on the generic fibre at $\mu, s$ if $L_{\mu, s}$ has nonnegative degree on every horizontal arithmetic surface in $X$. It is semipositive at $t, \mu, s$ if the weight $\sum_r c_r \log h_{x_t(r)}$ of the line $L_{\mu, s}$ has nonnegative Levi form at every complex point of $X$ and every tangent vector. The difference is effective at $\nu$ if some positive multiple of $L_{\nu, -1}$ has a nonzero global section.

**Definition 9.2.3 (Nef threshold, gaps).** A weight $\mu$ is under the nef threshold at $b$ if $4|\Psi|\,\|\mu\|_\infty \le (b - 2)\operatorname{gap}_j(\mu, \tau)$ for all $\tau$. It has compact gaps at least $c_0$ if $\mu(\tau, i) - \mu(\tau, i+1) \ge c_0$ for all $\tau$ and all $i$ with $i + 1 < N$ and $i + 1 \ne j$.

**Definition 9.2.4 (Geometric conditions).** The tower is *proportional* if $\operatorname{vol}(c) > 0$ for all $c$, $\mathrm{geo}_{M_{B,c}}(F) = \operatorname{vol}(c) \deg_{\mathrm{Fl}}(F)$ for all $B$, $c$ and $F \in R$, and $\mathrm{geo}_{M_{B,c}}$ does not depend on $B$. It has *equal volumes* if $\operatorname{vol}(c) = \operatorname{vol}(c')$ for all $c, c'$.

Proportionality is the arithmetic form of the Hirzebruch-Mumford proportionality principle: the Chern numbers of the automorphic lines on a Shimura variety are the volume times the Chern numbers on the compact dual, here the flag variety.

**Definition 9.2.5 (Conditions I1 to I7).** The tower satisfies:

1. I1 if there is $C$ with $|\mathrm{PP}_{B,c}(m)| \le C \log B$ for all $B \ge 2$, all $c$ and all monomials $m$;
2. I2 if for every $a$ there are $s_0 > 0$ and $C$ such that $|\overline{m}_B(c, \lambda, s) - \mathrm{PP}_{B,c}(L_{\lambda_s, s}^{\,d+1})| \le C s$ for $B \ge 2$, $\|\lambda\|_1 \le a$, $0 < s \le s_0$ and $\lambda_s$ dominant;
3. A1 if for every $a$ there is $s_0 > 0$ such that, in the same range, $M_{B,c}$ is semipositive at $t(s), \lambda_s, s$;
4. I3 if for every $a$ there is $s_0 > 0$ such that, in the same range and with $\lambda_s$ under the nef threshold at $B$, the model $M_{B,c}$ is nef on the fibres and semipositive at $\lambda_s, s$;
5. I5 and I6, the lower and upper bounds for heights of points stated in [the chapter on good towers](/entry/good-tower-volume-of-reduced/): for every $c_0 > 0$ there are $\theta_0 > 0$ and $C$ such that, for rational $\lambda$ with $\|\lambda\|_\infty \le 1$, compact gaps at least $c_0$ and $j$-gaps at least $\theta$, $0 < \theta \le \theta_0$, and $s = \theta^2$ rational, every point has $\overline{h}_B(c, \lambda, s, W) \ge -C \log(B/s)$ (this is I5), and there is a Zariski dense set of points with $\overline{h}_B(c, \lambda, s, W) \le C \log B$ (this is I6);
6. I7 if every $M_{B,c}$ is nef on the generic fibre at $(\lambda, 0)$ for dominant $\lambda$ and at $(0, 1)$, and the difference is effective at $\nu$.

The conditions M1 and M2 say that $M_{B,c}$ is nef on the fibre at $p$ at $(\mu, 0)$ for dominant $\mu$, for $p \in S_B$ (M1) and for $p \notin S_B$ with $\mu$ under the nef threshold at $p$ (M2). The condition ANef says that every $M_{B,c}$ is nef on the fibres at $(0, 1)$.

The remaining conditions compare $\mathrm{PP}$ with a linear functional $h \colon R \to \mathbb{R}$, which in the application is the arithmetic flag height. Let $p_k^\tau = \sum_i x_{\tau, i}^k$ be the power sums. Put

$$
\begin{aligned}
\operatorname{Sh}_j(\tau, F) &= \deg_{\mathrm{Fl}}\Big(\sum_{i < j} \partial F / \partial x_{\tau, i}\Big), \\
\operatorname{Tot}(\tau, F) &= \deg_{\mathrm{Fl}}\Big(\sum_{i} \partial F / \partial x_{\tau, i}\Big).
\end{aligned}
$$

**Definition 9.2.6 (Conditions on a functional).** Let $h$ be linear.

1. $h$ satisfies I9 if $h(\ell_\lambda^{\,d+1}) = 0$ for every dominant $\lambda$ with a wall, $h(\ell_\lambda^{\,d+1}) \ge 0$ for every dominant $\lambda$, and $h(p_1^\tau Q) = 0$ for every $\tau$ and every $Q$ homogeneous of degree $d$.
2. The tower satisfies I8 for $h$ if, for $B \ge 2$, every $c$, $\tau$ and $a$ with $a + 1 \ne j$, and every weight $\lambda$, with $s\lambda$ the weight with $\lambda(\tau, a)$ and $\lambda(\tau, a+1)$ exchanged,

$$
\mathrm{PP}_{B,c}(\ell_{s\lambda}^{\,d+1}) - \operatorname{vol}(c)\, h(\ell_{s\lambda}^{\,d+1}) = -\big(\mathrm{PP}_{B,c}(\ell_{\lambda}^{\,d+1}) - \operatorname{vol}(c)\, h(\ell_{\lambda}^{\,d+1})\big).
$$

3. Theorem B holds for $h$ if there are $C$ and $B_1$ such that for every $B \ge B_1$ there are $\alpha, \beta \colon \Psi \to \mathbb{R}$ with

$$
\Big|\mathrm{PP}_B(m) - \operatorname{vol}(T)\Big(h(m) - \sum_\tau (\alpha_\tau - \beta_\tau)\operatorname{Sh}_j(\tau, m) - \sum_\tau \beta_\tau \operatorname{Tot}(\tau, m)\Big)\Big| \le \frac{C \log B}{B}
$$

for every monomial $m$ of degree $d + 1$. The averaged Theorem B is the same with constants $\alpha, \beta \in \mathbb{R}$ in place of functions of $\tau$.

**Definition 9.2.7 (Conditions at the primes).** Let $\mathrm{frob}$ give for each prime $p$, each $\tau$ and each $n \ge 0$ a label $\mathrm{frob}_p(\tau, n) \in \Psi \sqcup \Psi$. For a label put $p^{\mathrm{Lie}}_k(\tau, \text{left}) = \sum_{i < j} x_{\tau, i}^k$ and $p^{\mathrm{Lie}}_k(\tau, \text{right}) = \sum_{i \ge j} (-x_{\tau, i})^k$. Define

$$
\begin{aligned}
\delta_p(\tau, k, Q) = k \log p\, \Big(&\sum_{n \ge 0} p^{-k(n+1)} \deg_{\mathrm{Fl}}\big(p^{\mathrm{Lie}}_{k-1}(\mathrm{frob}_p(\tau, n))\, Q\big) \\
&- \frac{\deg_{\mathrm{Fl}}\big(p^{\mathrm{Lie}}_{k-1}(\tau, \text{left})\, Q\big)}{p - 1}\Big).
\end{aligned}
$$

1. Proposition 6 holds for $\mathrm{frob}$ if, for $2 \le B_0 \le B$, every $c$, $\tau$, $1 \le k \le N$ and $Q$ homogeneous of degree $d + 1 - k$,

$$
\mathrm{PP}_{B_0, c}(p_k^\tau Q) = \mathrm{PP}_{B, c}(p_k^\tau Q) + \operatorname{vol}(c) \sum_{\substack{B_0 < p \le B \\ p \notin \mathcal{B}}} \delta_p(\tau, k, Q).
$$

2. Proposition A holds if there is a subgroup $\Gamma$ of the permutations of $\Psi$, transitive on $\Psi$, such that $\mathrm{PP}_B(\sigma F) = \mathrm{PP}_B(F)$ for $\sigma \in \Gamma$, $B \ge 2$ and $F \in R$, where $\sigma$ acts on the variables by $x_{\tau, i} \mapsto x_{\sigma\tau, i}$.
3. Proposition F holds with $C$, $\mathrm{rd}$ and $L$ if there are numbers $h_B(c, \tau)$ with $\mathrm{PP}_{B,c}(p_1^\tau Q) = h_B(c, \tau) \operatorname{vol}(c) \deg_{\mathrm{Fl}} Q$ for $B \ge 2$ and $Q$ homogeneous of degree $d$, and $|h_B(c, \tau)| \le C N \Lambda_B$ for $B \ge 128$ with $|\mathcal{B}| \le B$, where $\Lambda_B = \log(B\,\mathrm{rd}) + |L|$.

A label map has Frobenius shape if $\mathrm{frob}_p(\tau, n)$ is a left label for one $\tau$ exactly when it is a left label for all $\tau$.

**Definition 9.2.8 (The bounds of the volume theorem).** Let $u$ be a weight and $g > 0$. The pair $(u, g)$ is admissible if $u$ is regular dominant, $\operatorname{gap}_j(u, \tau) \ge g$ for all $\tau$, and $|u(\tau, a) - u(\tau, b)| \ge g$ whenever $a \ne b$ and $a$ is in the small block (the indices $a < j$ if $j \le N - j$, and $a \ge j$ otherwise). Put $B_0(u, g) = 4|\Psi| N^2 (1 + \|u\|_\infty / g)$ and

$$
\beta_B(u) = \Lambda_B \|u\|_1 + \min(j, N - j)\operatorname{spread}(u).
$$

1. T1 holds if, for admissible $(u, g)$, $B + 1 > B_0(u, g)$ and every $c$: for all small $s > 0$ the model $M_{B,c}$ is nef on the fibres and semipositive at $u_s, s$; as $s \to 0^+$, $\overline{m}_B(c, u, s) \to \mathrm{PP}_{B,c}(\ell_u^{\,d+1})$ and $m_B(c, u, s) \to \operatorname{vol}(c)\deg_{\mathrm{Fl}}(u) > 0$; and $\overline{m}_B / ((d+1) m_B) \to \operatorname{slope}_B(c, u)$.
2. Theorem W holds if for every $c_0 > 0$ there are $C$ and $B_1$ with $|\mathrm{PB}_B(\lambda)| \le C \log B / B$ for $B \ge B_1$ and every $\lambda$ in a wall at some $\tau_0$: $\|\lambda\|_\infty \le 1/2$, $\operatorname{gap}_j(\lambda, \tau_0) = 0$, $\operatorname{gap}_j(\lambda, \tau) \ge c_0$ for $\tau \ne \tau_0$, and compact gaps at least $c_0$.
3. T2 holds with $C$, $\mathrm{rd}$, $L$ if $\mathrm{PB}_B(u) \ge -C(d+1)\operatorname{vol}(T)\deg_{\mathrm{Fl}}(u)\,\beta_B(u)$ for admissible $(u, g)$, $B \ge 128$, $B + 1 > B_0(u, g)$ and $|\mathcal{B}| \le B$.
4. The mean slope bound holds with $C$, $\mathrm{rd}$, $L$ if, in the same range, $|\mathrm{Comp}|^{-1}\sum_c \operatorname{slope}_B(c, u) \ge -C \beta_B(u)$.

In the application $\Psi$ is the set of CM types of a host field $H$ of a CM field $E$, the tower lives over an integral model $Y$ of a unitary Shimura variety of signature $(p, q)$, and $N = p + q$. A good origin of $T$ over $Y$, with its extra conditions, is the datum built in [the existence theorem for good towers](/entry/exists-good-root-tower/): it ties every model $M_{B,c}$ to a Hodge component of $Y$. The functional $h$ is the arithmetic flag height $h_{\mathrm{Fl}}$: on a monomial $m$ it is $(-1)^{\deg m}$ times the arithmetic intersection number, on a model of the flag variety over $\mathbb{Z}$, of the standard hermitian lines of $m$.

**Theorem 9.2.9 (Antisymmetry I8).** Assume the comparison statement, the top level inputs and the Weil pairing statement. Let $E$ be a CM field with host $H$, let $D$ be a datum of signature $(p, q)$ with $p, q \ge 1$, let $Y$ be an integral model and let $T$ be a root tower of type $(\Psi, p + q)$ with a good origin over $Y$ that satisfies the extra conditions. Let $\mathrm{II}$ be a full intersection system. Then $T$ satisfies I8 for $h_{\mathrm{Fl}}$.

Lean: `GlobalTheory.T.full_intersection_tower_I8_identity` (also `GlobalTheory.CompanionTheory.Ar.Top.full_intersection_tower_I8_relation`, a second name)

*Proof.* This is the [antisymmetry theorem for good towers](/entry/good-tower-antisymmetry/), applied to the same data. $\square$

The reason for the sign is the $\mathbb{P}^1$ fibration of the flag variety attached to the simple reflection at $(\tau, a)$. Exchanging $\lambda(\tau, a)$ and $\lambda(\tau, a+1)$ is the action of this reflection on weights, and the difference between the tower and the flag variety changes sign under it. The case $a + 1 = j$ is excluded because the Hodge filtration of the tower breaks the symmetry there.

**Remark 9.2.10 (Formalization).** In the conditions I2, A1 and I3 the bound on $\|\lambda\|_1$ is quantified with a variable named `abelian₂`, a name with no meaning here ([Proportional.lean](lean:Development/AutomorphicSpectrum/Definitions/DivisibilityTowers/Proportional.lean#L74)). The norm $\|\cdot\|_\infty$ is the sup norm on functions. The good origin, its extra conditions and the intersection system enter the antisymmetry theorem only as hypotheses passed on to the cited theorem. The explanation of the sign by the $\mathbb{P}^1$ fibration is a heuristic; we did not open the proof of the cited theorem.
