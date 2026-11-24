---
title: The fibre input and the bounds I5 and I6
decls:
  - GlobalTheory.CompanionTheory.Ar.TopFibre.fibreInput
  - GlobalTheory.T.root_model_flag_height
  - GlobalTheory.CompanionTheory.Ar.Ht.TopLower.i5_of_hasRef_of_fibreInput
  - GlobalTheory.T.tower_i5_of_fibre_input
  - GlobalTheory.CompanionTheory.Ar.TopGood.tower_intersection_of_ample_flat
  - GlobalTheory.CompanionTheory.Ar.TopGood.tower_good_of_sandwich_split
  - GlobalTheory.T.tower_intersection_of_sandwich_split
status: drafted
drafted_by: writer@claude-opus-5-5
---

## The fibre input and the bounds I5 and I6

A good tower is a family of root models, one for each level $B \ge 2$ and each component $c$, whose modified heights satisfy two bounds. The bound I5 is a lower bound at every point, and the bound I6 is an upper bound on a Zariski dense set of points. This section proves both bounds for the tower of a good origin. The lower bound needs a fibre input: at every algebraic point, the root line heights are close to the graded degrees of an orthogonal flag pair of a hermitian bundle with small slopes. The two previous sections, [on Lie metrics](/entry/slope-unif/) and [on graded degrees](/entry/root-height/), give this input. For the background see [heights](/learn/arakelov/#heights) and [arithmetic volume](/learn/arakelov/#arithmetic-volume-and-bigness).

A root model of type $(\Phi, N)$ carries coordinates $y$ in a field $\Omega$, a set of points $P$, integer degrees $x_{\deg}$, a family of smooth hermitian lines $x_t(\tau, i)$ for $\tau \in \Phi$ and $0 \le i < N$ with weights $x_{\deg}(\tau, i)$, and an ample hermitian line $A$. We do not unfold the other parts. For $N = p + q$, a flag pair of type $(p, q)$ of a hermitian bundle $E$ is orthogonal and full if the tops of its flags are pairwise orthogonal and their ranks add up to the rank of $E$.

**Definition 8.3.1 (Fibre input).** A root model $R$ of type $(\Phi, p + q)$ has the fibre input if there is $C \ge 0$ with this property. For every number field $L$ and every point $w$ of $R$ with values in $L$, there are a finite extension $L'$ of $L$, a hermitian bundle $E$ over $\mathcal{O}_{L'}$ and an orthogonal full flag pair $(W, S)$ of $E$ of type $(p, q)$ such that, for every $\tau$,

$$
\begin{aligned}
\big| \operatorname{ht}_{x_1(\tau, i)}(w) - \operatorname{gr}_i W_\tau \big| &\le C, & 0 \le i < p, \\
\big| \operatorname{ht}_{x_1(\tau, p + i)}(w) + \operatorname{gr}_{q-1-i} S_\tau \big| &\le C, & 0 \le i < q,
\end{aligned}
$$

and

$$
\mu_{\max}(E) \le C \log\big(2 + C + \max(-\widehat{\deg}_n E, 0)\big) + C .
$$

Lean: `GlobalTheory.CompanionTheory.Ar.Ht.FibreInput`

**Theorem 8.3.2 (Fibre input of a root model).** Assume the existence of the moduli schemes for $1 \le p + q$, the first part of the integral model theory, resolution of singularities in characteristic $0$, the extension theorem for homomorphisms of semi-abelian schemes and the slope input. Let $R$ be a root model of type $(\Phi, p + q)$ with $1 \le p + q$, let $\mathfrak{M}$ be a Hodge component on the coordinates of $R$, and let $b$ be a flag datum of $\mathfrak{M}$. If the degrees $x_{\deg}$ and some generators $e$ form a root line datum for $b$, then $R$ has the fibre input.

Lean: `GlobalTheory.CompanionTheory.Ar.TopFibre.fibreInput` (also `GlobalTheory.T.root_model_flag_height`, a second name)

*Proof.* There is a Lie metric $h$ for $\mathfrak{M}$ that is orthogonal for the decomposition of the Lie algebra by the labels. The slope bound for Hodge components gives a constant $C_1$, and the flag line degree formula for the lines $x_1$ gives a constant $C_2$. Let $C = \max(C_1, C_2)$.

Let $w$ be a point of $R$ with values in $L$. It extends to an integral point $z_0 : \operatorname{Spec}\mathcal{O}_L \to X$. The slope bound gives a finite extension $L'$. Let $z$ be the base change of $z_0$ to $\mathcal{O}_{L'}$ and let $E$ be the fibre of $h$ at $z$. Since $h$ is orthogonal for the labels, the flag datum gives an orthogonal full flag pair $(W, S)$ of $E$ whose steps are the sub-fibres of the steps of $b$. The slope bound applies to $E$. The flag line degree formula applies at $z$ with the coordinates $w$ seen in $L'$. Line heights do not change under a finite extension of the field, so these are the line heights of $w$ over $L$. $\square$

A root tower $T$ of type $(\Phi, N)$ is a family of root models $T_{B, c}$ for levels $B$ and components $c$, with an integer $j$ and an intersection system $\mathrm{II}$ that gives the modified heights $\bar m_{B, c, \lambda, s}(W)$ of points $W$. We do not unfold the modified heights. A reference for $T$ is a family of root models $R_c$, one for each component.

**Definition 8.3.3 (Bounds I5 and I6).** The tower $T$ satisfies I5 if for every $c_0 > 0$ there are $\theta_0 > 0$ and $C$ with this property. Let $B \ge 2$, let $c$ be a component, let $\lambda$ be a rational weight with $\|\lambda\| \le 1$, let $0 < \theta \le \theta_0$ and let $s \in \mathbb{Q}$ with $s = \theta^2$. Assume that every gap of $\lambda$ is at least $\theta$ and that the compact gaps of $\lambda$ are at least $c_0$. Then every point $W$ of $T_{B, c}$ satisfies

$$
-C \log(B / s) \le \bar m_{B, c, \lambda, s}(W).
$$

The tower satisfies I6 if, with the same quantifiers and hypotheses, there is a Zariski dense set $F$ of points of $T_{B, c}$ with $\bar m_{B, c, \lambda, s}(W) \le C \log B$ for all $W \in F$.

Lean: `GlobalTheory.CompanionTheory.Ar.Top.RootTower.I5`, `GlobalTheory.CompanionTheory.Ar.Top.RootTower.I6`

A reference $R$ is close to $T$ if there are $C$ and $s_0 > 0$ such that, for every $B \ge 2$ and every component $c$, there are an embedding of fields and units $u$ that make $T_{B, c}$ close to $R_c$ within $C \log B$, and the archimedean parts of the root heights of $T_{B, c}$ and $R_c$ differ by an amount in $[-C \log(1/s) - C, C]$ for every dominant weight $\mu$ with $\|\mu\| \le 2$ and every $0 < s \le s_0$. A root model has flat units if, for each $\tau$, a positive multiple of $\sum_i x_{\deg}(\tau, i)$ is the degree of a unit with a vertical bound.

**Theorem 8.3.4 (I5 from the fibre input).** Let $T$ be a root tower of type $(\Phi, (j + 1) + (k + 1))$, let $\mathrm{II}$ be an intersection system and let $R$ be a reference close to $T$. If each $R_c$ has an ample line, flat units and the fibre input for $(j + 1, k + 1)$, then $T$ satisfies I5.

Lean: `GlobalTheory.CompanionTheory.Ar.Ht.TopLower.i5_of_hasRef_of_fibreInput` (also `GlobalTheory.T.tower_i5_of_fibre_input`, a second name)

*Proof.* For each component, the ample line, the flat units and the fibre input give a lower bound for the root heights of $R_c$. The root height at weight $0$ is at least $-C$, and the root height at a dominant weight $\mu$ with $\|\mu\| \le 2$ is at least $-C \log(2 + C + h_0) - C$, where $h_0$ is the root height at weight $0$. A reference close to $T$ with these lower bounds gives I5. $\square$

**Corollary 8.3.5.** Let $p, q \ge 1$, let $T$ be a root tower of type $(\Phi, p + q)$ and let $R$ be a reference close to $T$. If each $R_c$ has an ample line, flat units and the fibre input for $(p, q)$, then $T$ satisfies I5.

Lean: `GlobalTheory.CompanionTheory.Ar.TopGood.tower_intersection_of_ample_flat`

*Proof.* Write $p = j + 1$ and $q = k + 1$ and apply the theorem. $\square$

A good origin $g$ for a model $Y$ and a root tower $T$ gives, for each level $B$, a finite set of primes $S_B$ and origins at every component, and for each component a reference origin. The reference origin consists of a reference root model $R_c$, a Hodge component $\mathfrak{M}_c$ with no primes removed, a flag datum and a root line datum. The good origin also gives an ample line for each $R_c$, and its integer $j$ satisfies $0 < j < p + q$ with $j = p$.

**Theorem 8.3.6 (Good towers from sandwiches).** Assume the top level inputs and the flat line generator input. Let $Y$ be an integral model with split components, let $T$ be a root tower of type $(\Phi, p + q)$ with a good origin $g$, and let $\mathrm{II}$ be an intersection system. Assume that for every level $B$, every component $a$ and every prime $\ell \in S_B$ the Hodge component of the origin at $(B, a)$ has a sandwich at $\ell$ with some constant $\kappa$. Then $T$ satisfies I5 and I6.

Lean: `GlobalTheory.CompanionTheory.Ar.TopGood.tower_good_of_sandwich_split` (also `GlobalTheory.T.tower_intersection_of_sandwich_split`, a second name)

*Proof.* The sandwiches at all primes give that the references $R_c$ of $g$ are close to $T$. A reference close to $T$ gives I6 directly. For I5 we use the corollary. The integer $j$ of the tower satisfies $0 < j < p + q$ and $j = p$, so $p \ge 1$ and $q \ge 1$. Each $R_c$ has an ample line from $g$. The flat line generator input and the split components give flat units for $R_c$ from the root line datum of the reference origin. The fibre input of a root model gives the fibre input of $R_c$. $\square$

**Remark 8.3.7 (Formalization).** The lower bound for the root heights in the proof of I5 is `Ht.RefLower`, obtained by `T.ref_lower_of_fibre_input`, and the passage to I5 is `T.tower_i5_of_reference`. Closeness is `Ht.HasRef`, obtained from the sandwiches by `T.has_reference_of_sandwich_all_primes`, and I6 is `T.tower_i6_of_reference`. We do not unfold these. The fibre input is a statement about the lines $x_1$ at the parameter $t = 1$ only.
