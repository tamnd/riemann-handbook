---
title: Line heights and graded degrees of flags
decls:
  - GlobalTheory.CompanionTheory.Ar.RootHt.one_label
  - GlobalTheory.CompanionTheory.Ar.RootHt.root_height
  - GlobalTheory.T.flag_line_degree_formula
status: drafted
drafted_by: writer@claude-opus-5-5
---

## Line heights and graded degrees of flags

A flag of a hermitian bundle over $\mathcal{O}_L$ has graded pieces, and each graded piece has an arithmetic degree. A hermitian line on the base gives a height to every algebraic point. This section proves that the two numbers differ by a bounded amount when the flag comes from a fixed flag of the Lie algebra and the line is the graded line of that flag. The bound is the comparison between the [heights](/learn/arakelov/#heights) of points and the [degrees of hermitian lattices](/learn/arakelov/#hermitian-lattices-and-slopes). The setting of $X$, $\xi$, $y$, Lie models and Lie metrics is the one of [the previous section](/entry/torus-unif/).

**Definition 8.2.1 (Hermitian line).** A hermitian line on the coordinates $y$ is a weight vector $a : K \to \mathbb{Z}$ together with a positive function $h$ on $\prod_k \mathbb{C}^{J_k}$ such that

$$
h(c \cdot z) = \prod_k |c_k|^{a_k}\, h(z)
$$

for all scalars $c_k \in \mathbb{C}^\times$. The line is smooth if $h$ is $C^\infty$ off the locus where some block $z_k$ is $0$. The dual line has weights $-a$ and function $h^{-1}$.

**Definition 8.2.2 (Line height).** Let $A = (a, h)$ be a hermitian line, $L$ a number field and $w = (w_{k,i})$ a point with coordinates in $L$. The line height of $w$ is

$$
\begin{aligned}
\operatorname{ht}_A(w) = \frac{1}{[L:\mathbb{Q}]} \Big( &\sum_{v \nmid \infty} \sum_k a_k \log \max_i |w_{k,i}|_v \\
&+ \sum_{\sigma : L \to \mathbb{C}} \log h(\sigma w) \Big).
\end{aligned}
$$

Since the dual line has weights $-a$ and function $h^{-1}$, its height is $-\operatorname{ht}_A(w)$, and the dual of a smooth line is smooth.

Lean: `GlobalTheory.CompanionTheory.Ar.Ht.lineHt`, `GlobalTheory.CompanionTheory.Ar.RootHt.lineHt_dualLine`

**Definition 8.2.3 (Saturated flag).** Let $B$ be a hermitian bundle over $\mathcal{O}_L$. A saturated flag of length $r$ is a chain $0 = F_0 \subset F_1 \subset \dots \subset F_r$ of saturated $\mathcal{O}_L$-submodules with $\operatorname{rk} F_i = i$. Its graded degrees are

$$
\operatorname{gr}_i F = \widehat{\deg}_n F_{i+1} - \widehat{\deg}_n F_i , \qquad 0 \le i < r .
$$

**Definition 8.2.4 (Flag sandwich).** Let $V$ be a lattice of the Lie algebra over $X$, that is, a submodule $V_p$ of the generic Lie algebra at every point $p$, and let $b_0 = (b_{0,1}, \dots, b_{0,r})$ be an independent family. Let $m \ge 1$ be an integer. The pair $(V, b_0)$ is sandwiched with constant $m$ if at each point there is a frame $b$ of $V$ with the same flag as $b_0$ such that $m\, b_i$ lies in the lattice of the Lie model and $m\, \pi_i$ maps the lattice of the Lie model into the regular functions, where $\pi$ is the dual frame. The $i$-th graded line of $V$ along $b_0$ has degree $a$ with generator $e_0$ on all charts if, on the chart $c$, it is spanned by $\prod_k y_{k,c(k)}^{a_k}\, e_0$.

**Theorem 8.2.5 (Line height of one graded piece).** Let $\Omega$ have characteristic $0$ and let $G$ be a smooth commutative group scheme over $X$ with Lie model $M$ and Lie metric $h$. Let $V$ be a lattice, $b_0$ an independent family of length $r$ and $m \ge 1$, such that $(V, b_0)$ is sandwiched with constant $m$. Let $0 \le i < r$, and let $A$ be a smooth hermitian line such that the $i$-th graded line of $V$ along $b_0$ has degree $a$ with generator $e_0$ on all charts, where $a$ is the weight of $A$. Then there is a constant $C$ with this property. Let $L$ be a number field, $z : \operatorname{Spec} \mathcal{O}_L \to X$, and let $w$ be the coordinates of $z$. Let $(B, M_B)$ be the fibre of $h$ at $z$, and let $F$ be a saturated flag of $B$ of length $r$ such that each $F_j$ is the sub-fibre of the span of $b_{0,1}, \dots, b_{0,j}$. Then

$$
\big| \operatorname{ht}_A(w) - \operatorname{gr}_i F \big| \le C .
$$

Lean: `GlobalTheory.CompanionTheory.Ar.RootHt.one_label`

*Proof.* Choose $s \in F_{i+1}$ that maps to the generator of the graded line at $z$, and let $f$ be a basis of $F_i \otimes L$. The graded degree is

$$
\begin{aligned}
[L:\mathbb{Q}]\,\operatorname{gr}_i F = {}&\log \#\big(F_{i+1} / (F_i + \mathcal{O}_L s)\big) \\
&- \tfrac{1}{2} \sum_\sigma \big( \log \|\mathrm{Gram}(f, s)\|_\sigma - \log \|\mathrm{Gram}(f)\|_\sigma \big).
\end{aligned}
$$

At each finite place $v$ the sandwich gives a local ratio $\rho_v$ between the frame of $V$ and the lattice of $B$, within a factor $m$. So the logarithm of the index differs from $\sum_v (\log \rho_v - \log |\varphi(s)|_v)$ by at most $[L:\mathbb{Q}] \log m$, where $\varphi$ is the coordinate of $s$ on the graded line. The product formula turns the sum of the local ratios into the finite part of $\operatorname{ht}_A(w)$, since the graded line has degree $a$ on every chart. At each complex embedding the quotient of Gram determinants is the norm of $s$ in the graded line for $h$. Its logarithm differs from $\log h(\sigma w)$ by a constant $C_0$, because $A$ is smooth and the graded line of $h$ has the same weights. The constant $C = \log m + |C_0|$ works. $\square$

Now let $\mathfrak{M}$ be a Hodge component of signature $(p, q)$ with Lie metric $h$, and let $\Phi$ be the set of CM types. A flag datum for $\mathfrak{M}$ is a basis $b_s$ of the Lie algebra for each label $s$ in two copies of $\Phi$, such that each Hodge lattice $V_s$ is a flag bundle along $b_s$ everywhere. Its root lines are indexed by $(\tau, r)$ with $\tau \in \Phi$ and $0 \le r < p + q$. For $r < p$ the root line is the $r$-th graded line of the first copy, and for $r \ge p$ it is the dual of the $(p + q - 1 - r)$-th graded line of the second copy. A family of degrees $a_{(\tau, r)}$ and generators $e_{(\tau, r)}$ is a root line datum if each root line has degree $a_{(\tau, r)}$ with generator $e_{(\tau, r)}$ on all charts.

A flag pair of $B$ for $\Phi$ of type $(p, q)$ is a pair of saturated flags $W_\tau$ of length $p$ and $S_\tau$ of length $q$, for each $\tau \in \Phi$.

**Theorem 8.2.6 (Flag line degree formula).** Let $\mathfrak{M}$ be a Hodge component with flag datum $b$ and Lie metric $h$. Let $x_{(\tau, r)}$ be smooth hermitian lines whose weights and generators $e$ form a root line datum. Then there is a constant $C$ with this property. Let $L$ be a number field, $z : \operatorname{Spec}\mathcal{O}_L \to X$ with coordinates $w$, let $(B, M_B)$ be the fibre of $h$ at $z$, and let $(W, S)$ be a flag pair of $B$ such that each step of $W_\tau$ is the sub-fibre of the matching step of $b_{(1, \tau)}$, and each step of $S_\tau$ is the sub-fibre of the matching step of $b_{(2, \tau)}$. Then for all $\tau$,

$$
\begin{aligned}
\big| \operatorname{ht}_{x_{(\tau, i)}}(w) - \operatorname{gr}_i W_\tau \big| &\le C, & 0 \le i < p, \\
\big| \operatorname{ht}_{x_{(\tau, p + i)}}(w) + \operatorname{gr}_{q-1-i} S_\tau \big| &\le C, & 0 \le i < q.
\end{aligned}
$$

Lean: `GlobalTheory.CompanionTheory.Ar.RootHt.root_height` (also `GlobalTheory.T.flag_line_degree_formula`, a second name)

*Proof.* Each label $s$ has a sandwich constant $m$ for $(V_s, b_s)$. The group scheme is smooth because it is semi-abelian, and $\Omega$ has characteristic $0$ because the structure map of $\mathfrak{M}$ is injective. For $r = i < p$ the root line is the $i$-th graded line of $V_{(1, \tau)}$, and the line height theorem for one graded piece applies to $x_{(\tau, i)}$ and $W_\tau$. It gives a constant $C_W(\tau, i)$.

For $r = p + i$ the root line is the dual of the $(q-1-i)$-th graded line of $V_{(2, \tau)}$. So the $(q-1-i)$-th graded line has degree $-a$ with generator $e^{-1}$, which are the weight and generator of the dual line of $x_{(\tau, p+i)}$. The dual line is smooth, and the theorem for one graded piece gives

$$
\big| -\operatorname{ht}_{x_{(\tau, p+i)}}(w) - \operatorname{gr}_{q-1-i} S_\tau \big| \le C_S(\tau, i).
$$

The constant $C = \sum_\tau \big( \sum_i |C_W(\tau, i)| + \sum_i |C_S(\tau, i)| \big)$ bounds all the terms. $\square$

**Remark 8.2.7 (Formalization).** The degree formula, the index bound and the archimedean bound in the proof of `one_label` are the named results `T.graded_degree_formula`, `T.log_card_quotient_bound`, `T.local_ratio_product_formula` and `T.hermitian_line_metric_bound`, which we do not unfold. The sandwich constants of the flag datum come from `T.flag_label_bases_exist`. The dual root lines use the lemmas `isDegOn_of_tens_neg_one` and `isDegOn_inr` of FlagLineDegreeFormula.lean, which convert the degree of a line tensored to the power $-1$ into the degree $-a$ with generator $e^{-1}$.
