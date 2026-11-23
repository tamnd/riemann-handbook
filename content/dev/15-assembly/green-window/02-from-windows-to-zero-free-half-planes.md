---
title: From windows to zero-free half-planes
decls:
  - UpperTheory.Comparison₂.windowInequality_of_artinInputs
  - UpperTheory.Comparison₂.level_gm_le_on_family_scales
  - UpperTheory.Top.zeroFreeAll_of_topG
status: drafted
drafted_by: writer@claude-opus-5-5
---
## From windows to zero-free half-planes

This section turns the bound of the last section into the statement ZeroFreeAll: $L(s, \psi) \neq 0$ for each primitive [[Dirichlet character|JR4QSEFXWF]] $\psi$ and each $s$ with $\operatorname{Re} s > \tfrac12$. The bound at one point becomes a bound on the windows of a family. A criterion of Landau type turns a bound on windows into a zero-free half-plane. The last theorem of the section reduces ZeroFreeAll to two inputs: the connectedness statement $\mathrm{Top}_G$, which [the shape theorem](/entry/shape-closed-link-n-of-green/) proves from Green, and hosts on windows for each $\psi$, which [the hosts for one character](/entry/supply-chi/) give from VWin. It is the last step of [ZeroFreeAll from Green, VWin and HypsAlt](/step/zero-free-all-of-green-v-win/).

We keep the notation of the last section: a level $\Lambda$ with order $o$ and kept characters $K_\Lambda$, the level sum $G_\Lambda$, the explicit formula conditions $E_\Lambda$ and the core conditions.

**Definition 3.2.1 (Windows).** Let $S \subseteq \mathbb{R}$ and $\lambda > 1$. The set $S$ *has windows of scale* $\lambda$ if for each $y$ there is $Y \ge y$ with $[Y, Y^\lambda] \subseteq S$.

The [[explicit formula|72WNRWJQC1]] links the size of $G_\Lambda$ to the zeros of the $L$-functions of $K_\Lambda$; see [the explicit formula](/learn/analytic-number-theory/#the-explicit-formula) in Volume 1. A proved criterion of Landau type uses this link. Let $\lambda > 1$ and $0 < \theta < 1$. If the set $\{x : G_\Lambda(x) \le x^\theta\}$ has windows of scale $\lambda$, then $L(s, \chi) \neq 0$ for each $\chi \in K_\Lambda$ and each $s$ with $\operatorname{Re} s > \theta$. Its proof weights the exceptional character by $3o+1$ and the other characters by $1$.

**Definition 3.2.2 (Families and ties).** A *family core* at scale $\varepsilon$ is a set $W \subseteq \mathbb{R}$ of *window points*, an index set $I_x$ for each $x$, and for each $x$ and $i \in I_x$ a datum $D(x,i)$ with a host $H(x,i)$ on a frame and a finite set $T(x,i)$. The family core *meets the explicit formula conditions* for $\Lambda$ if there are $C$ and $x_E$ with $E_\Lambda(H(x,i), T(x,i), x, \varepsilon, C)$ for all $x \ge x_E$ and all $i$. A *tie* is a predicate $\mathrm{Tied}(F, e_D, e_L, K, c_{HH}, e_K, C_L, x)$ on families $F$ of some type, each with a family core. The family $F$ is *tied on its windows* with exponents $e_D, e_L$ if there are $K, c_{HH}, e_K, C_L, x_0$ with $\mathrm{Tied}(F, e_D, e_L, K, c_{HH}, e_K, C_L, x)$ for each window point $x \ge x_0$.

**Definition 3.2.3 (The window inequality).** The *window inequality* for a tie and a level $\Lambda$ says: for all $e_D$, $e_L$, $\varepsilon > 0$ and each family $F$ at scale $\varepsilon$ whose core meets the explicit formula conditions for $\Lambda$ and which is tied on its windows with exponents $e_D, e_L$, there is $x_1$ with

$$G_\Lambda(x) \le x^{1/2 + (e_D + e_L + 7)\varepsilon}$$

for each window point $x \ge x_1$ of $F$.

**Theorem 3.2.4 (Window inequality from core bounds).** Take a type of families with family cores and a tie. Assume that the tie gives the core conditions: if $\mathrm{Tied}(F, e_D, e_L, K, c_{HH}, e_K, C_L, x)$, then there is $i \in I_x$ such that the core conditions hold for $H(x,i)$ and $T(x,i)$ at $(x, \varepsilon)$ with $e_D, e_L, K, c_{HH}, e_K$. Then the window inequality holds for each level $\Lambda$.

Lean: `UpperTheory.Comparison₂.windowInequality_of_artinInputs`

*Proof.* Let $F$ be a family at scale $\varepsilon$ with the constant $C$ and the bound $x_E$ of the explicit formula conditions, and the constants $K, c_{HH}, e_K, C_L, x_0$ of the tie. [The level bound at one point](/entry/core-gm/) for $\Lambda, e_D, e_L, K, c_{HH}, e_K, C, \varepsilon$ gives a bound $x_1$. Let $x \ge \max(x_1, x_0, x_E)$ be a window point. The tie at $x$ gives an index $i$ with the core conditions. The explicit formula conditions hold at $(x, i)$. So the level bound gives $G_\Lambda(x) \le x^{1/2 + (e_D+e_L+7)\varepsilon}$. $\square$

The families of the proof are the families $F$ of [the predicate Closed](/step/closed-def/), each with its family core. Their tie is the chain tie $\mathrm{ChainTied}$. It is a long existential statement: an index $i_0$, data, constants and weights with a list of bounds, among them the core conditions of the host at $(x, i_0)$.

**Theorem 3.2.5 (Window inequality for chain ties).** For each level $\Lambda$, the window inequality holds for the families of the proof with the chain tie.

Lean: `UpperTheory.Comparison₂.level_gm_le_on_family_scales`

*Proof.* This is the [window inequality from core bounds](/entry/window-inequality-of-artin-inputs/) applied to the chain tie. A chain tie at $x$ holds the core conditions at $(x, i_0)$: the set $T$ of the tie is the set $T(x, i_0)$ of the host, and each point of the second set lies in the subgroup $A_0$, since it is a digit of a cyclic subgroup. $\square$

The last theorem needs the hosts of the next section. A *scale* $s$ has a size $s.x$, a parameter $s.\varepsilon$ and a bound $s.b$. A *host requirement* $P$ is a predicate on a constant $C_5$, a scale, ranks $R$, a host $H$ on the frame of $R$ and a prime $q_0$.

**Definition 3.2.6 (Hosts on windows).** Let $\lambda > 1$ and let $P$ be a host requirement. *Hosts with $P$ exist on windows of scale* $\lambda$ if for each $\varepsilon \in (0, \tfrac{1}{52})$ there are constants $C_{T2}$, $C_8 \ge 1$, $C_5 > 0$, $c_6 > 0$, $C_b > 0$, a bound $x_0$ and a set of scales with windows of scale $\lambda$, such that each scale $s$ of the set with $s.\varepsilon = \varepsilon$ and $s.x \ge x_0$ has ranks $R$, a host $H$ and a prime $q_0$ with these properties: the ranks have the sizes fixed by $s$, the host has the constant $C_{T2}$, the host is good for $(s, C_8, C_5, c_6, C_b, q_0)$, and $P(C_5, s, R, H, q_0)$ holds.

A *requirement* $G$ is a predicate on a scale, a frame, host axioms, a finite set and a number $t$. It gives a host requirement $G.\mathrm{req}$, and for each $\lambda$ a family class $G.\mathrm{cls}(\lambda)$: the families whose window points have windows of scale $\lambda$ and whose data at each $x > x_1$ and each $i$ meet $G$ with the size data of $(x, i)$. For a primitive $\psi$ let $\Lambda_\psi$ be the level of the cyclic group generated by $\psi$. It contains $\psi$. The requirement $G_\psi$ asks the explicit formula conditions $E_{\Lambda_\psi}(H, T, s.x, s.\varepsilon, 4)$ and the bound $V(E_H, t, \sqrt{s.b})$ on the Sha lengths of the field $E_H$ of the host, as in [the window bound VWin](/step/vwin-def/). A family satisfies $\mathrm{HypV}$ if for all large $x$ and all $i$ the bound $V(E_{H(x,i)}, t(x,i), \sqrt{b(x,i)})$ holds.

**Definition 3.2.7 (Connected family classes and $\mathrm{Top}_G$).** A family class $\mathcal{E}$ is *connected* if there are $e_D, e_L$ and $\varepsilon_1 > 0$ such that for each $\varepsilon \in (0, \varepsilon_1)$ some family $F$ at scale $\varepsilon$ in $\mathcal{E}$ is tied on its windows by the chain tie with exponents $e_D, e_L$. The statement $\mathrm{Top}_G$ says: for each $\lambda > 1$ and each requirement $G$, if hosts with $G.\mathrm{req}$ exist on windows of scale $\lambda$ and each family of $G.\mathrm{cls}(\lambda)$ satisfies $\mathrm{HypV}$, then $G.\mathrm{cls}(\lambda)$ is connected.

**Theorem 3.2.8 (ZeroFreeAll from $\mathrm{Top}_G$ and hosts).** Let $\lambda > 1$. Assume $\mathrm{Top}_G$, and assume that for each primitive Dirichlet character $\psi$ hosts with $G_\psi.\mathrm{req}$ exist on windows of scale $\lambda$. Then for each primitive Dirichlet character $\psi$ and each $s \in \mathbb{C}$ with $\operatorname{Re} s > \tfrac12$, $L(s, \psi) \neq 0$.

Lean: `UpperTheory.Top.zeroFreeAll_of_topG`

*Proof.* Fix $\psi$ and $s$ with $\operatorname{Re} s > \tfrac12$, and let $\Lambda = \Lambda_\psi$.

1. Each family $F$ of $G_\psi.\mathrm{cls}(\lambda)$ satisfies $\mathrm{HypV}$ for $x > x_1 + 1$, since the requirement $G_\psi$ holds the bound $V$. So $\mathrm{Top}_G$, with the hosts for $\psi$, gives that $G_\psi.\mathrm{cls}(\lambda)$ is connected, with $e_D, e_L, \varepsilon_1$.
2. Each family of the class meets the explicit formula conditions for $\Lambda$, with $C = 4$ and $x_E = x_1 + 1$, by the first part of $G_\psi$. Its window points have windows of scale $\lambda$.
3. Put $\delta = \min(\operatorname{Re} s - \tfrac12, \tfrac12)$ and choose $\varepsilon \in (0, \varepsilon_1)$ with $(e_D + e_L + 7)\varepsilon \le \delta/2$. Step 1 gives a family $F$ at scale $\varepsilon$, tied on its windows.
4. The [window inequality for chain ties](/entry/level-gm-le-on-family-scales/) gives $x_1'$ with $G_\Lambda(x) \le x^{1/2 + (e_D+e_L+7)\varepsilon} \le x^{\theta}$ for each window point $x \ge \max(x_1', 1)$, with $\theta = \tfrac12 + \delta/2$. Since the window points have windows of scale $\lambda$ above each bound, so does $\{x : G_\Lambda(x) \le x^\theta\}$.
5. The criterion of Landau type gives $L(s', \chi) \neq 0$ for $\chi \in K_\Lambda$ and $\operatorname{Re} s' > \theta$. Since $\psi \in K_\Lambda$ and $\operatorname{Re} s > \theta$, $L(s, \psi) \neq 0$. $\square$

**Remark 3.2.9 (Formalization).** The three theorems are in [WindowInequalityOfArtinInputs.lean](lean:Development/AutomorphicArithmetic/PrimitiveCosets/WindowInequalityOfArtinInputs.lean#L17), LevelGmLeOnFamilyScales.lean (line 28) and ZeroFreeAllOfTopG.lean (line 26). The criterion of Landau type is `UpperTheory.Comparison₂.formB`, proved for every level through `Landau.zero_free_of_Chebyshev_growth`. The window inequality is `ChebyshevInequalityOnWindows` in TopWin.lean (line 26). The constant $C_L$ of a tie is carried along and never read by the window inequality. The theorem `zeroFreeAll_of_topG` uses $\mathrm{Top}_G$ only through the requirements $G_\psi$, and the constant $4$ of the explicit formula conditions comes from $G_\psi$. The level $\Lambda_\psi$ is `Level.cyc ψ`, defined as `Level.ofSub` of the subgroup generated by $\psi$; we have not unfolded `Level.ofSub` or the chain tie `ChainTied`.
