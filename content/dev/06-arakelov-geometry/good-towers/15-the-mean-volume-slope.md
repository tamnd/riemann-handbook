---
title: The mean volume slope
decls:
  - GlobalTheory.CompanionTheory.Ar.Plug.SlopeVolM.slope_sub_cost_le_compVolSlope
  - GlobalTheory.CompanionTheory.Relay.uniform_all_norm_height_bound
  - GlobalTheory.T.uniform_all_norm_height_bound
  - GlobalTheory.CompanionTheory.Ar.Plug.top_meanAll
  - GlobalTheory.T.abelian_cm_comp_laws_bound
  - GlobalTheory.CompanionTheory.Ar.Plug.deepStR_of_volume
status: drafted
drafted_by: writer@claude-opus-5-5
---

## The mean volume slope

The volume theorem gives a lower bound for the mean of the intersection slopes of a root tower. This section turns it into a lower bound for the mean of the volume slopes of the moduli space, which are read from the growth of the number of small cusp sections. First we compare, on one component, the intersection slope of the tower with the volume slope. The [counting lemma](/entry/model-small-encard-le/) of the last section is the main step. Then we take the mean over the components and bound the cost at the bad primes. Last, we put the result in the form of the deep statement, which [the deep statement from use](/entry/deep-st-r-of-use/) needs.

We keep the setting of the last section: $E$ is a CM field, Galois over $\mathbb{Q}$, with host $H$, a datum $D$ with $N = p + q$, a level $l$, a moduli space $X_o$, a coefficient datum $c$ with number field $F$, unfoldings $U_\sigma$, a generic frame datum $h$ and sections $e_Z$, with the component laws and the uniformization of integral points. Let $x$ be a real number with $|\tau(\xi_0)| = x$ for every good embedding, every base point and every embedding $\tau$ of $E$. We write $\Psi$ for the set of CM types.

### Volume slopes

**Definition 8.15.1 (Volume slope).** Let $Z$ be a component, let $u$ be a weight and let $B$ be a real number. For $t \in \mathbb{R}$ let $\mathrm{vol}_Z(u, t)$ be the volume of the counts
$$
\tau \mapsto \# \mathrm{Small}_Z\bigl(\tau u, e^{\tau t}\bigr)
$$
along the integers $\tau \in 8 \mathbb{N}$, for the mixed valuations at $B$, normalized by the dimension of the flag variety and by $[F : \mathbb{Q}]$. Let $\delta_Z(u)$ be the top degree of $u$ on $Z$. The volume slope $\mu_Z(u)$ is an element of $\mathbb{R} \cup \{\pm\infty\}$. When $\delta_Z(u) > 0$, it is characterized by this property: for every real $s$,
$$
s \le \mu_Z(u) \iff \delta_Z(u)(s + t) \le \mathrm{vol}_Z(u, t) \text{ for all } t \in \mathbb{R} .
$$

We do not unfold the volume of a sequence of counts or the top degree. So $\mu_Z(u)$ is the largest $s$ such that the number of small sections of weight $\tau u$ and size $e^{\tau t}$ grows at least like the volume $\delta_Z(u)(s + t)$.

For a finite set of primes we use the constant $\varepsilon_p$ of the last section. Let $S(l, B)$ be the set of primes $p$ with $p \le B$ and $p \mid 2 |d_E| M'_l$. The cost at $B$ is
$$
c_2(l, B) = \sum_{p \in S(l, B)} \varepsilon_p \log p .
$$

### Comparison of slopes on one component

Let $Y$ be a model of $X_o$ over $\mathcal{O}_F$, let $T$ be a root tower with a good origin $o$, and let $\kappa$ be a bijection from the components of $X_{o, F}$ to the components of $T$ that matches the components of the origin. Let $\mathrm{II}$ be a full intersection system. We use the notions of a [proportional tower and the bound T1](/entry/good-tower-volume-of-reduced/). For a weight $u$ the slope $\mathrm{slope}_T(B, c, u)$ is the limit in T1 of the top intersection number of the twisted root line divided by $\dim + 1$ times its degree. A weight $u$ is regular with gap $g > 0$ if it is regular dominant, its gaps at the index $j$ of $T$ are at least $g$, and $|u(\tau, a) - u(\tau, b)| \ge g$ for $a \ne b$ in the small range of $j$. We put
$$
B_0(u, g) = 4 |\Psi| N^2 \left(1 + \frac{\|u\|_\infty}{g}\right) .
$$

**Theorem 8.15.2 (Comparison of slopes).** Assume the arithmetic Riemann-Roch statement for nef lines, the top level inputs and the arithmetic volume inequality. Let $T$, $o$, $\kappa$ and $\mathrm{II}$ be as above, with $T$ proportional and satisfying T1. Let $Z$ be a component, let $u$ be a weight with strictly decreasing rows that is regular with gap $g$, and let $B \ge B_0(u, g)$. Then
$$
\begin{aligned}
&\mathrm{slope}_T(\lfloor B \rfloor, \kappa Z, u) - 2\, c_2(l, B)\, \|u\|_1 \\
&\qquad \le \mu_Z(u) ,
\end{aligned}
$$
where $\mu_Z(u)$ is taken for the mixed valuations at $B$.

Lean: `GlobalTheory.CompanionTheory.Ar.Plug.SlopeVolM.slope_sub_cost_le_compVolSlope` (also `GlobalTheory.CompanionTheory.Relay.uniform_all_norm_height_bound` and `GlobalTheory.T.uniform_all_norm_height_bound`, second names).

*Proof.* Let $s_0$ be the left side and $\delta = \delta_Z(u)$. The Riemann-Roch statement gives $\delta = \mathrm{vol}(\kappa Z) \deg_{\mathrm{fl}}(u) > 0$. A lemma on generic frames gives $k_0 \in 8\mathbb{N}$, $R_0 > 0$ and $d$ small model sections $f_1, \dots, f_d$ of weight $k_0 u$ whose traces are nondegenerate. By the definition of the volume slope it is enough to show $\delta(s_0 + t - \varepsilon) \le \mathrm{vol}_Z(u, t)$ for every $t$ and every $\varepsilon > 0$. Put $t' = t - 2 c_2(l, B) \|u\|_1 - \varepsilon$. The arithmetic volume inequality bounds $\delta(\mathrm{slope}_T + t')$ by the volume of the counts $\# \mathcal{M}(\tau u, e^{\tau t'})$ of small model sections, normalized by $d\,[F : \mathbb{Q}]$. The set $S(l, B)$ is the set of bad primes of $o$ at $\lfloor B \rfloor$. The [counting lemma](/entry/model-small-encard-le/) with $R' = e^{(\tau + k_0) t}$ bounds each count by
$$
\# \mathrm{Small}_Z\bigl((\tau + k_0) u, e^{(\tau + k_0) t}\bigr)^d
$$
once $N\, d\, e^{\tau t'} R_0 \le e^{(\tau + k_0) t}$, where $N = \prod_{p \in S(l, B)} p^{\lceil 2 \varepsilon_p \|(\tau + k_0) u\|_1 \rceil}$. Since $\log N \le 2 c_2(l, B) \|(\tau + k_0)u\|_1 + \sum_p \log p$, this holds for all large $\tau$: the term $\tau \varepsilon$ absorbs the constants. A comparison lemma for volumes of counts says that if $m(\tau) \le m'(\tau + k_0)^d$ for all large $\tau$, with $8 \mid k_0$, then the volume of $m$ normalized by $d\,[F : \mathbb{Q}]$ is at most the volume of $m'$ normalized by $[F : \mathbb{Q}]$. This gives $\delta(s_0 + t - \varepsilon) \le \mathrm{vol}_Z(u, t)$. $\square$

### The mean over the components

Let $\mathrm{rd}_E = |d_E|^{1/[E : \mathbb{Q}]}$ be the root discriminant, and let $L_H$ be the logarithmic derivative at $1$ of the $L$-function of the quadratic character of the host. For a weight $u$, a real number $g$ and a real number $s$ we put
$$
\begin{aligned}
\mathrm{err}(s, u, g) = {} & \bigl(\log B_0(u, g) + s\bigr) \|u\|_1 \\
& + q \sum_\tau \bigl(\max\nolimits_i u(\tau, i) - \min\nolimits_i u(\tau, i)\bigr) .
\end{aligned}
$$

**Definition 8.15.3 (Mean volume slope bound).** A weight $u$ has gap $g$ if $g > 0$, the rows of $u$ decrease strictly, and $|u(\tau, a) - u(\tau, b)| \ge g$ for all $\tau$ and all $a \ne b$ with $a \ge p$. The mean volume slope bound with constants $s$ and $C$ says: for every weight $u$ with gap $g$ there are real numbers $\mathrm{sl}(Z)$, one for each component $Z$, with $\mathrm{sl}(Z) \le \mu_Z(u)$ for the mixed valuations at $B_0(u, g)$, and
$$
\frac{1}{\# \mathrm{Comp}} \sum_Z \mathrm{sl}(Z) \ge -C\, \mathrm{err}(s, u, g) .
$$

The numbers $\mathrm{sl}(Z)$ are lower bounds for the volume slopes. So the bound says that the mean volume slope is at least $-C\, \mathrm{err}(s, u, g)$.

**Theorem 8.15.4 (Mean volume slope bound).** Assume the arithmetic Riemann-Roch statement for nef lines, the top level inputs, the existence of a full intersection system, the arithmetic volume inequality, and the [good tower statement and the volume statement](/entry/good-tower-volume-of-reduced/). Then there is $C \ge 0$ with this property. Let $E$ be a CM field that is abelian over $\mathbb{Q}$, let $(U, h, e)$ satisfy the component laws and the uniformization of integral points, and assume that the function fields are algebraically closed in the sense of the frames, which we do not unfold. Assume that $l$ is good at every prime and $A_l = 1$, that $q \ge 1$ and $3q + 1 \le p + q$, that $|\Psi| \ge 2$, and that the number of primes that divide $2 d_E$ or $M'_l$ is at most $4 |\Psi| N^2$. Then the mean volume slope bound holds with $s = \log \mathrm{rd}_E + |L_H|$ and $C$.

Lean: `GlobalTheory.CompanionTheory.Ar.Plug.top_meanAll` (also `GlobalTheory.T.abelian_cm_comp_laws_bound`, a second name).

*Proof.* A lemma on full intersection systems at good levels uses the top level inputs, the good tower statement and the volume statement. It gives $C_T \ge 0$, a model $Y$, a root tower $T$ with a good origin, a matching bijection $\kappa$ of the components, such that the bad primes of $T$ are the primes of $2 d_E M'_l$, $T$ is proportional, satisfies T1, and satisfies the mean slope bound with $C_T$. We put $C = C_T + 120$. Let $u$ have gap $g$ and let $B = B_0(u, g)$. Since $p > q \ge 1$, the gap of $u$ makes $u$ regular with gap $g$ at $j = p$. Since $|\Psi| \ge 2$ and $N \ge 4$, we get $B \ge 128$ and $\lfloor B \rfloor \ge 4 |\Psi| N^2$, so $T$ has at most $\lfloor B \rfloor$ bad primes. The mean slope bound at $\lfloor B \rfloor$, with $\min(j, N - j) = q$, gives
$$
\begin{aligned}
&\frac{1}{\# \mathrm{Comp}} \sum_c \mathrm{slope}_T(\lfloor B \rfloor, c, u) \\
&\quad \ge -C_T \Bigl( \bigl(\log(\lfloor B \rfloor\, \mathrm{rd}_E) + |L_H|\bigr) \|u\|_1 + q\, \mathrm{spr}(u) \Bigr),
\end{aligned}
$$
where $\mathrm{spr}(u)$ is the sum over $\tau$ of $\max_i u(\tau, i) - \min_i u(\tau, i)$. We take
$$
\mathrm{sl}(Z) = \mathrm{slope}_T(\lfloor B \rfloor, \kappa Z, u) - 2\, c_2(l, B)\, \|u\|_1 .
$$
The [comparison of slopes](/entry/slope-sub-cost-le-comp-vol-slope/) gives $\mathrm{sl}(Z) \le \mu_Z(u)$. A bound for the cost gives $0 \le c_2(l, B) \le 60 (\log B + \log \mathrm{rd}_E)$. The sum over $Z$ moves to the sum over the components of $T$ along $\kappa$. So the mean of $\mathrm{sl}$ is at least the bound above minus $120 (\log B + \log \mathrm{rd}_E) \|u\|_1$. With $\log \lfloor B \rfloor \le \log B$, this is at least $-(C_T + 120)\, \mathrm{err}(s, u, g)$. $\square$

### The deep statement

The deep statement is about the data of the main argument. A deep datum $D$ has integers $m \ge 2$, $k$ and $n$ with $r = k + m - 1$, a host with a CM field $E$ that is abelian over $\mathbb{Q}$, and a core $T$ with its laws. For $1 \le j < m$ a deep setting $Y$ at $j$ has a level, a moduli space for the datum of $T$ at $j$, unfoldings $U$, and a goodness condition for parameters $e$ and $o$. We do not unfold these. We write $\xi_D$ for the absolute value of the base points of $D$ and $\ell(D) = \log \mathrm{rd}_E + |L_H|$.

**Definition 8.15.5 (Deep statement).** The deep statement says: there is $C \ge 0$ such that for every deep datum $D$ and core $T$ with its laws and with $m^2 \le k$, every $j$ with $1 \le j < m$, and every good deep setting $Y$ at $j$ whose number $M'$ has at most $15$ prime factors, the mean volume slope bound for $U$ holds with $x = \xi_D$, $s = \ell(D)$ and $C$.

**Theorem 8.15.6 (Deep statement from the volume theorem).** Assume the arithmetic Riemann-Roch statement for nef lines, the top level inputs, the existence of a full intersection system, the arithmetic volume inequality, the good tower statement and the volume statement. Then the deep statement holds.

Lean: `GlobalTheory.CompanionTheory.Ar.Plug.deepStR_of_volume`.

*Proof.* Let $C$ be the constant of the [mean volume slope bound](/entry/top-mean-all/). Let $D$, $T$, $j$ and $Y$ be as in the deep statement. A lemma on good deep data gives the component laws for $U$, a level that is good at every prime with $A = 1$, the algebraic closedness of the function fields, $q = m - j$, $p + q = r$, $|\Psi| = 2n$, and the identities for $\mathrm{rd}_E$ and $L_H$. The uniformization of integral points holds. We check the numerical hypotheses. Since $j < m$, $q \ge 1$. Since $m \ge 2$, $2m \le m^2 \le k$, so
$$
3q + 1 \le 3m - 2 \le k + m - 1 = p + q .
$$
The CM field has $|\Psi| \ge 2$. Among the primes that divide $2 d_E$ or $M'$, at most $|\{\text{primes of } M'\}| + 3 \le 18$ are larger than $n$, and at most $n + 1$ are at most $n$. So there are at most $n + 19$ of them. Since $N = p + q \ge 4$ and $n \ge 1$, this is at most $8n \cdot 16 \le 4 |\Psi| N^2$. Then the mean volume slope bound applies, and the identities for $\mathrm{rd}_E$ and $L_H$ turn its constant into $\ell(D)$. $\square$

So the two conditions $m^2 \le k$ and "at most $15$ prime factors" of the deep statement are used only to check the numerical hypotheses of the mean volume slope bound.

**Remark 8.15.7 (Formalization).** The comparison of slopes has three names, in a chain of two renamings proved by `first | exact @...`; the name `uniform_all_norm_height_bound` speaks of a height bound, but the conclusion compares two slopes. The mean volume slope bound also has the second name `T.abelian_cm_comp_laws_bound`, and its statement file imports `Mathlib` twice (AbelianCmCompLawsBoundStatement.lean:1 and 3). The arithmetic volume inequality is the hypothesis `BirationalPullbackPushforwardFormula` (ArithmeticHilbertSamuelLowerBound.lean:126): it bounds an intersection number by an arithmetic volume of small sections and has no pullback and no pushforward. The gap condition asks for the gap only at indices $a \ge p$ (SemiposAtOfPositive.lean:88). In the proof of the deep statement, the conditions $m^2 \le k$ and $\#\{\text{primes of } M'\} \le 15$ are not named; they are introduced at DeepStROfVolume.lean:26 and enter only through `omega` (lines 33 and 54). The uniformization of integral points is the proved result `Ref.unifAll_holds` (line 56). We do not unfold the slope, the top degree or the volume of counts.
