---
title: Heights of points for the twisted cusp lines
decls:
  - GlobalTheory.CompanionTheory.Ar.Cusp.PtHt.g_height
  - GlobalTheory.T.cusp_intersection_height
  - GlobalTheory.CompanionTheory.Relay.phiDeg_fibLat_le_of_isOFamily_of_isAdapted
  - GlobalTheory.T.phiDeg_fibLat_le_of_isOFamily_of_isAdapted
  - GlobalTheory.CompanionTheory.Ar.Cusp.TopHt.htU_of_given
  - GlobalTheory.T.cusp_height_upper
  - GlobalTheory.T.intersection_degree_lower
  - GlobalTheory.CompanionTheory.Ar.Cusp.TopNine.nineGeoU_of_given
  - GlobalTheory.T.exists_geometric_height_constants
status: drafted
drafted_by: writer@claude-opus-5-5
---

## Heights of points for the twisted cusp lines

The regularised cusp weight of [the previous section](/entry/relay-cusp-weight-regularisations-tied/) gives a family of hermitian lines $\overline M_{B, p, q, t'}$ on each component. This section proves three properties of these lines. They are semipositive, nef on the fibres and ample on the generic fibre. The heights of points are bounded below by $-C f j' \Lambda_B$, up to a term from the auxiliary line. The mean of the cusp weight against the Hodge measure has an upper bound of the same size. The lower bound for heights comes from an identity that expresses the height of a point through a degree of the fibre lattices at the point. For the background see [heights](/learn/arakelov/#heights) and [arithmetic intersection numbers](/learn/arakelov/#arithmetic-varieties-and-intersection-numbers).

We keep the setting of the previous sections. The component data $D_c$ has $f = |\Phi|$, integers $j \le N$ with $j' = N - j$, a finite set $S_B$ of primes for each level $B$, vertical factors $v_\ell$ with degrees $d_\ell$ for $\ell \in S_B$, an auxiliary positive line $\overline A'$ with weights $a'$ and a constant $K_A$. The Hodge line $\mu$ has weights $a_\mu$. The twisted weight of level $B$ is $a_\mu + \sum_{\ell \in S_B} d_\ell$. Let

$$
\Lambda_B = \log(B\, \mathrm{rd}_E) + |L_H|,
$$

where $\mathrm{rd}_E = |d_E|^{1/[E:\mathbb{Q}]}$ is the root discriminant and $L_H = \operatorname{Re}\, (L'/L)(1, \chi)$ for the quadratic character $\chi$ of the host.

For weights $a$, an archimedean function $\phi$ and a point $w$ over a number field $L$, the point height is

$$
\begin{aligned}
\operatorname{ht}_{a, \phi}(w) = \frac{1}{[L:\mathbb{Q}]} \Big( &\sum_{v \nmid \infty} \sum_k a_k \log \max_i |w_{k,i}|_v \\
&+ \sum_{\sigma} \phi(\sigma w) \Big).
\end{aligned}
$$

A linear point $A$ of an integral point $z$ of the Hodge component, with abelian part $P$ and Lie model $V$, consists of an action $\rho$ of $\mathcal{O}_E$ on $V$, a lattice $I$, eigenspaces $V_s$ for the labels $s$ and further data that we do not unfold. A family $v_1, \dots, v_r$ in $I$ is an $\mathcal{O}_E$-family if it is independent over $\mathcal{O}_E$ and its $\mathcal{O}_E$-span has finite index in $I$. For lattices $F_\tau$ in $V$ and families $q_\tau$ adapted to $v$, the $\Phi$-degree is

$$
\begin{aligned}
\deg_\Phi(F; v, q) = {}&\sum_\tau \deg_{s(\tau)}(F_\tau; v, q_\tau) - \tfrac{1}{2} \log [I : \mathcal{O}_E v] \\
&+ \tfrac{1}{2}\, f\, r \log(4\pi),
\end{aligned}
$$

where $s(\tau)$ is the label of $\tau$ and we do not unfold the label degrees $\deg_s$. The fibre lattice of a Hodge lattice $V_s$ at $z$ is the $\mathcal{O}_L$-lattice in $V$ of vectors whose tangent values lie in $V_s$ at every prime of $\mathcal{O}_L$.

**Theorem 8.6.1 (Height identity for linear points).** Assume the top level inputs, and let $E$ be abelian over $\mathbb{Q}$. Let the component origin be good, let $B$ be a level, let $z : \operatorname{Spec}\mathcal{O}_L \to X$ have coordinates $w$, and let $A$ be a linear point of $z$. Let $v_1, \dots, v_r$ be an $\mathcal{O}_E$-family, and for each $\tau$ let $q_\tau$ be a family of length $k$, adapted to $v$ at the label $s(\tau)$, with values in the eigenspace of $s(\tau)$. Then there are real numbers $x_e$, one for each embedding $e : L \to \mathbb{C}$, such that $x_e$ is a $\Phi$-weight value of the origin at the complex point $e \circ z$, and

$$
\begin{aligned}
&\operatorname{ht}_{a_B, \phi_B}(w) + \frac{1}{[L:\mathbb{Q}]} \sum_e x_e \\
&\quad = -\deg_\Phi\big(F; v, q\big).
\end{aligned}
$$

Here $a_B$ is the twisted weight of level $B$, $\phi_B = \sum_{\ell \in S_B} \log v_\ell$, and $F_\tau$ is the fibre lattice of the Hodge lattice of label $s(\tau)$, patched at the primes $S_0 \cup S_B$.

Lean: `GlobalTheory.CompanionTheory.Ar.Cusp.PtHt.g_height` (also `GlobalTheory.T.cusp_intersection_height`, a second name)

*Proof.* The coordinates $w$ give a Hodge frame datum at $z$: a chart, a unit, frames $s_\tau$ of the de Rham lattices and their values. No prime of $S_0 \cup S_B$ lies in the residue characteristic of the generic fibre, so the patched lattices equal the de Rham lattices at the generic point of $z$. The frames $s_\tau$ lift to the abelian part over $\mathcal{O}_L$. The set of CM types is nonempty, and the ranks satisfy $r + k = N - j$. The finite part of the height is a sum of local indices of the frames in the fibre lattices, and the archimedean values $x_e$ are the logarithms of the Hodge norms at the complex points. Both sides then agree term by term. $\square$

**Theorem 8.6.2 (Bound for the $\Phi$-degree).** Assume the top level inputs and the flat degree input. Then there is $C \ge 0$ with this property. Let $E$ be abelian over $\mathbb{Q}$, let the component origin be admitted at some level $B_1$, and let $B \ge 4 f N^2$. Let $A$ be a linear point of an integral point $z$, whose hermitian part has rank at most $f(p + q)$. Let $v$ be an $\mathcal{O}_E$-family of length $r$, and let $q_\tau$ be families of length $k$ adapted to $v$ in the eigenspaces, with $r + k = j'$. Then

$$
\deg_\Phi(F; v, q) \le C\, f\, j'\, \Lambda_B,
$$

where $F_\tau$ are the patched fibre lattices as above.

Lean: `GlobalTheory.CompanionTheory.Relay.phiDeg_fibLat_le_of_isOFamily_of_isAdapted` (also `GlobalTheory.T.phiDeg_fibLat_le_of_isOFamily_of_isAdapted`, a second name)

*Proof.* The flat degree input gives a saturation statement for flat hermitian fibres of the right signature. The height comparison on the global model then gives the bound. $\square$

The admission condition at $B_1$ says: the model is global, the origin is good, $S_0$ is the set of primes dividing $2\, d_E\, M'$ with $|S_0| \le 4 f N^2$, $B_1 \ge 4f + 2$, the primes of $D_c$ are the primes $\ell \le B_1$ outside $S_0$, and $j' \le j$. Let $S'$ be a bounded regularisation setting for the corrected weight $\psi_U$, with regularised weights $\psi_{t'}$ and reference line $h_{\mathrm{ref}}$. The twisted cusp line $\overline M_{B, p, q, t'}$ has weights $q\, a_B + p\, a'$ and metric

$$
\big( h_{\mathrm{ref}}\, e^{\psi_{t'}} \big)^q \prod_{\ell \in S_B} v_\ell^{\,q}\; h_{A'}^{\,p},
$$

replaced by a smooth line invariant under conjugation with the same metric on the points of the component when one exists. For a horizontal prime $P$ of dimension $1$ that contains the ideal of the component, let $\operatorname{ht}(P; \overline M)$ be the intersection number $\mathrm{II}(P; \overline M)$ divided by $q \deg P$.

**Theorem 8.6.3 (Lower bound for heights).** Assume the top level inputs and the flat degree input. Then there is $C_h$ with this property. Let $E$ be abelian over $\mathbb{Q}$, let $\mathrm{II}$ be a full intersection system, let the origin be admitted at some $B_1$, let $U$ be a cusp weight and let $S'$ be tied. Let $B \ge 4 f N^2$ and $1 \le p \le q$. Then there is $t_0 > 0$ such that, for $0 < t' \le t_0$ and every horizontal prime $P$ as above,

$$
\operatorname{ht}(P; \overline M_{B, p, q, t'}) \ge -C_h\, f\, j'\, \Lambda_B - \frac{p}{q} K_A .
$$

Lean: `GlobalTheory.CompanionTheory.Ar.Cusp.TopHt.htU_of_given` (also `GlobalTheory.T.cusp_height_upper`, a second name)

*Proof.* Take $C_h = C$ from the bound for the $\Phi$-degree. Since $S'$ is tied, for small $t'$ the regularised weight $\psi_{t'}$ dominates the potential of $S'$, and $\overline M_{B, p, q, t'}$ is smooth with the metric above on the points of the component. Take $t_0$ in this range. The prime $P$ is the ideal of a point $w$ over a number field $L_0$, and $\operatorname{ht}(P; \overline M)$ is the line height of $w$. The auxiliary line gives $\operatorname{ht}_{\overline A'}(w) \ge -K_A$.

After a finite extension $L$ the point $w$ extends to an integral point $z$ of the Hodge component with an abelian part and a linear point $A$. Here $2f = [E : \mathbb{Q}]$, and there are an $\mathcal{O}_E$-family $v$ and adapted families $q_\tau$ in the eigenspaces with $r + k = j'$. The height identity gives the values $x_e$. Since $U$ is a cusp weight, $x_e$ is at most $\psi_{t'} + \log h_{\mathrm{ref}}$ at $e(w)$. The line height splits as

$$
\operatorname{ht}_{\overline M}(w) = q\, \big( \operatorname{ht}_{a_B, \phi_B}(w) + \operatorname{arch}(w) \big) + p\, \operatorname{ht}_{\overline A'}(w),
$$

and heights do not change from $L_0$ to $L$. The identity and the bound for the $\Phi$-degree give the result. $\square$

**Theorem 8.6.4 (Positivity of the twisted cusp lines).** Assume the top level inputs and the Weil bound statement for the outer theory. Let $E$ be abelian over $\mathbb{Q}$, let $\mathrm{II}$ be a full intersection system, let the origin be admitted at some $B_1$, and let $S'$ be a tied bounded regularisation setting for $\psi_U$. Then for every $B \ge 4f + 2$ and $1 \le p \le q$ there is $t_0 > 0$ such that, for $0 < t' \le t_0$, the line $\overline M_{B, p, q, t'}$ is semipositive, nef on the fibres and ample on the generic fibre.

Lean: `GlobalTheory.T.intersection_degree_lower` (a second name of `GlobalTheory.CompanionTheory.Relay.intersection_degree_lower`)

*Proof.* For a full intersection system and a tied setting, positivity of the twisted lines follows from a bound on the intersection degrees at each level $B \ge 4f + 2$. The admitted origin gives this bound. $\square$

**Theorem 8.6.5 (Geometric height constants).** Assume the top level inputs, the Weil bound statement and the flat degree input. Then there are constants $C_h$ and $C_u$ with this property. Let $E$ be abelian over $\mathbb{Q}$, let $\mathrm{II}$ be a full intersection system, let the origin be admitted at some $B_1$, let $U$ be a cusp weight and let $S'$ be a tied bounded regularisation setting for $\psi_U$. Then:

1. the positivity of the twisted cusp lines holds for $B \ge 4f + 2$;
2. the lower bound for heights holds with the constant $C_h$ for $B \ge 4 f N^2$;
3. if $1 \le j'$ and $3 j' + 1 \le N$, then for every $B \ge 4 f N^2$ the mean of $U$ over the complex points against the Monge-Ampère measure of $\varphi_\mu$, divided by the degree of $\mu$, is at most $C_u\, f\, j'\, \Lambda_B$.

Lean: `GlobalTheory.CompanionTheory.Ar.Cusp.TopNine.nineGeoU_of_given` (also `GlobalTheory.T.exists_geometric_height_constants`, a second name)

*Proof.* Take $C_h$ from the lower bound for heights and $C_u$ from the bound for the sum of cusp volumes. For given data the positivity theorem gives the first part, and the two constants give the second and third parts. $\square$

**Remark 8.6.6 (Formalization).** The three parts of the last theorem are `PosU`, `HtU` and `MeanU`, and their conjunction is `NineGeoU`. The positivity theorem is proved by `T.posU_of_full_intersection_system` from `T.intersection_degree_upper`. The bound for the $\Phi$-degree is `LevelTowerAlt.height_comparison_global_model` applied to `flat_saturation_of_degree`. The mean bound is `T.cusp_volume_sum`. The archimedean upper bound for $x_e$ is `T.cusp_intersection_finite`. The Weil bound statement is `Out.WeilSt` and the flat degree input is `Fl.FlatDegree`. We do not unfold these.
