---
title: The analytic square of an adjacent swap
decls:
  - GlobalTheory.T.flag_cover_realisation_pullback
  - GlobalTheory.CompanionTheory.Relay.flag_cover_realisation_pullback
  - GlobalTheory.T.flag_adjacent_swap_square_system
  - GlobalTheory.CompanionTheory.Ar.PB.WSq.ansq_exists
  - GlobalTheory.T.flag_adjacent_rows_base_metric
  - GlobalTheory.CompanionTheory.Ar.PB.WSq.Sec.main
  - GlobalTheory.T.flag_adjacent_twisted_measure
  - GlobalTheory.CompanionTheory.Ar.PB.WSq.Sec.LocGen.main
  - GlobalTheory.T.flag_adjacent_two_frames_orbit
  - GlobalTheory.T.flag_adjacent_rows_dimension
  - GlobalTheory.CompanionTheory.Ar.PB.WSq.FC.fibre_charts
  - GlobalTheory.T.flag_adjacent_rows_resolution
  - GlobalTheory.CompanionTheory.Ar.PB.WMan.fibreSquare_atlas
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The analytic square of an adjacent swap

This section builds, for one adjacent swap of a flag, a space of pairs of flags that differ in one step, with a divisor along the diagonal and charts in which the fibres are copies of the projective line. On this space the difference of the weights of the two flags is a log-sine function of a $2 \times 2$ Gram matrix. With an algebraic square on a flag cover it gives a square system, the input of the reflection sum of Section 10. We use [line bundles and divisors](/learn/geometry/#line-bundles-and-divisors) and [resolutions](/learn/positivity-resolution/#resolution-of-singularities-and-principalization).

### Adjacent swaps

Let $M$ be a flag model of type $(N, j)$ over $y$, let $B$ be a base metric of dimension $n$ on $M$, and let $\mathcal{F}$ be analytic flag data of dimension $d$ for $B$ (Section 7), with analytic system $S$ restricted to the steps. An adjacent swap is a triple $(\tau, a, b)$ with $b = a + 1$ and either $b < j$ or $j \leq a$, so both steps lie in one block. Its coefficient is the function on steps
$$
\xi_{\tau,a}(\tau, i) = [i + 1 = a] + [i = a + 1] - 2 [i = a],
$$
and $\xi_{\tau,a}(\tau', i) = 0$ for $\tau' \neq \tau$. So $\xi_{\tau,a}(\tau, a) = -2$. Let $k_0$ be the block of the step $(\tau, a)$, let $c_a$ be the last column of the step $a$, and let $c_b = c_a + 1$.

The swap coordinates are the coordinates $y$ together with a new block: the step coordinates of $a$ computed with $g_\tau (1 + t E_{c_b, c_a})$ in place of $g_\tau$, where $t$ is transcendental. A point $x$ of the swap coordinates gives two points: the first point $z_0(x)$ forgets the new block, and the second point $z_1(x)$ puts the new block in place of the block $k_0$. They have the same base part and differ only in the step $(\tau, a)$.

For a frame $F$, a block diagonal invertible matrix $h$ and $t \neq 0$, assume that $h$ is a flag of $z_0$ for $F$ at all steps of $\tau$ and that $h (1 + t E_{c_b, c_a})$ is a flag of $z_1$. Put $u_i = 1$ at a proper step $i$. At the step with $i + 1 = j$ let $u_i$ be the value of the frame factor $\upsilon_{\tau,i}$ at the base point times the leading principal minor of $h$ on the $W$ block if $a < j$, and times $1$ if $j \leq a$. At the step $i + 1 = N$ let $u_i$ be $\upsilon_{\tau,i}$ times the principal minor of $h$ on the $\Omega$ block. The norm function of the swap is
$$
\begin{aligned}
\nu(z_0, z_1, h, t) = {} & \log \Bigl\lvert t \prod_i u_i^{\xi_{\tau,a}(\tau, i)} \Bigr\rvert \\
&+ \tfrac12 \sum_p \xi_{\tau,a}(p) \bigl(\log h_{\mathrm{FS}}(d_y(p))(z_0) + \log h_{\mathrm{FS}}(d_y(p))(z_1)\bigr) .
\end{aligned}
$$

### The swap resolution

A swap chart of an analytic log resolution $R_W$ of the swap coordinates, with a map $\mathrm{pr}$ to $X_b$, is a chart $\psi$ with a frame $F$, an index $i_0$ and holomorphic block diagonal matrices $H_{\tau'}(w)$, such that the frame is good, $H$ is a flag of $z_0$, and $H$ with $H_\tau (1 + \psi_{i_0} E_{c_b, c_a})$ in place of $H_\tau$ is a flag of $z_1$. So the coordinate $i_0$ is the swap parameter. A swap atlas is a holomorphic $\mathrm{pr}$, compatible with the base points of $z_0$, such that every point lies in a swap chart.

**Lemma 10.8.1 (Swap atlas).** Let $(\tau, a, b)$ be an adjacent swap, assume that $y$ is an arithmetic variety of dimension $d + 2$ and that $d + 1 = n + \lvert\Psi\rvert(\binom{j}{2} + \binom{N - j}{2})$. Then there are an analytic log resolution $R_W$ of dimension $d + 2$ of the swap coordinates and a map $\mathrm{pr}$ to $X_b$ that form a swap atlas.

Lean: `GlobalTheory.CompanionTheory.Ar.PB.WMan.fibreSquare_atlas` (also `GlobalTheory.T.flag_adjacent_rows_resolution`, a second name).

*Proof.* An equivalence of index sets matches the coordinates of the swap variety with the base coordinates, the lower unipotent entries and the swap parameter. Chart lemmas give, near each point, an orbit chart with the properties of a swap chart. A lemma on log resolutions from orbit charts gives $R_W$ and $\mathrm{pr}$. $\square$

**Lemma 10.8.2 (Independence of frames).** Let $(\tau, a, b)$ be an adjacent swap. If $(z_0, z_1, F, h, t)$ and $(z'_0, z'_1, F', h', t')$ are as in the definition of $\nu$, with $z_0$ and $z'_0$ in one torus orbit, $z_1$ and $z'_1$ in one torus orbit, $z_0$ and $z_1$ with the same base part and good frames, then
$$
\nu(z_0, z_1, h, t) = \nu(z'_0, z'_1, h', t') .
$$

Lean: `GlobalTheory.T.flag_adjacent_two_frames_orbit`.

*Proof.* The base parts of the two pairs agree up to the torus. A frame comparison lemma relates $h$ and $h'$ by a block triangular matrix that fixes the step columns of $a$, and relates $t$ and $t'$ by the ratio of two diagonal entries. The changes of the factors $u_i$, of $t$ and of the Fubini-Study terms cancel in $\nu$, because the coefficients $\xi_{\tau,a}$ are balanced. $\square$

**Lemma 10.8.3 (Local sections).** Let $(\tau, a, b)$ be an adjacent swap and let $R_W$, $\mathrm{pr}$ be a swap atlas of dimension $e$. Every point $x$ of $R_W$ has a swap chart $\psi$ with parameter index $i_0$, an open neighbourhood $V$ in the chart, and a holomorphic function $u$ without zeros on $V$, such that on $V$:

1. $\psi_{i_0} = 0$ exactly on the diagonal, where $z_0$ and $z_1$ lie in one torus orbit;
2. off the diagonal, $\log \lvert u\, \psi_{i_0} \rvert - \log h_A = \nu(z_0, z_1, h, t)$ for every admissible $(F, h, t)$, where $h_A$ is a fixed hermitian line on the swap coordinates.

Lean: `GlobalTheory.CompanionTheory.Ar.PB.WSq.Sec.LocGen.main` (also `GlobalTheory.T.flag_adjacent_twisted_measure`, a second name).

*Proof.* Take a swap chart at $x$. A resolution lemma gives $V$ and the zero set of $\psi_{i_0}$, and a holomorphic frame of the metric gives $u$. The flag $H$ of the chart gives one admissible tuple, and the lemma on independence of frames gives all others. $\square$

**Lemma 10.8.4 (Diagonal divisor).** Let $(\tau, a, b)$ be an adjacent swap and let $R_W$, $\mathrm{pr}$ be a swap atlas of dimension $d + 2$. Then there are a potential $L'$ on $R_W$, a section $v$ of $L'$ with simple normal crossings of multiplicity $1$ along a divisor $D$, and a constant $c$ such that:

1. the product of $s \circ \mathrm{pr}$ and $v$ has simple normal crossings for the sum of the pullback of $L$ and $L'$;
2. $\lVert v \rVert \leq 1$;
3. $\log \lVert v \rVert(x) + c = \nu(z_0, z_1, h, t)$ for every point $x$ and every admissible tuple at $x$.

Lean: `GlobalTheory.CompanionTheory.Ar.PB.WSq.Sec.main` (also `GlobalTheory.T.flag_adjacent_rows_base_metric`, a second name).

*Proof.* The lemma on local sections gives the functions $u\,\psi_{i_0}$ on a cover. Their quotients on overlaps are holomorphic without zeros, so they glue to a section $v$ of a line $L'$ whose local potentials are the logs of $h_A / \lvert u \rvert^2$, with $D$ the diagonal. Since $\psi_{i_0}$ is a coordinate transverse to the boundary, the crossings are normal, and compactness gives the constant with $\lVert v \rVert \leq 1$. $\square$

### Fibre charts

A parameter cover of a manifold is a family of charts $\Phi_m$ with measurable sets $B_m$ whose images are disjoint and cover the manifold up to a null set.

**Lemma 10.8.5 (Fibre charts).** Let $(\tau, a, b)$ be an adjacent swap with $d + 1 = n + \lvert\Psi\rvert(\binom{j}{2} + \binom{N - j}{2})$. Let $R_W$ be an analytic log resolution of dimension $d + 2$ of the swap coordinates with holomorphic maps $q_0, q_1$ to $S$ such that $q_k(x)$ lies under $z_k(x)$ and $(q_0, q_1)$ is injective. Then there are open sets $U_m \subseteq \mathbb{C}^d$, measurable $B_m \subseteq U_m$, matrix functions $G_m$ with values in $2 \times 2$ matrices, and maps $\Phi_{Y,m}$ from $\mathbb{C}^{d+1}$ to $S$ and $\Phi_{W,m}$ from $\mathbb{C}^{d+2}$ to $R_W$ such that:

1. $\Phi_Y$ is a parameter cover of $S$ over the sets of $(z, w)$ with $w \in U_m$, and $\Phi_W$ is a parameter cover of $R_W$ over the sets of $(z_0, z_1, w)$ with $w \in U_m$;
2. $\Phi_{Y,m}(z, w)$ is off the boundary;
3. each chart is a fibre chart: there are a frame index $l$ of $B$ and holomorphic block diagonal $H(w)$ such that $G_m(w)$ is the $2 \times 2$ matrix of minors of $H_\tau^* G_{l,\tau} H_\tau$ on the step columns of $a$ with $c_a$ replaced by $c_a$ or $c_b$, and the points of the charts are the flags of $H$ moved by $z$ in the fibre direction.

Lean: `GlobalTheory.CompanionTheory.Ar.PB.WSq.FC.fibre_charts` (also `GlobalTheory.T.flag_adjacent_rows_dimension`, a second name).

*Proof.* The dimension formula gives an equivalence between the complement of the swap coordinate and the base and lower unipotent coordinates. The lower unipotent family is analytic. The charts of the base and of the unipotent entries give charts of $S$ and of $R_W$, with one fibre coordinate for $S$ and two for $R_W$, and the open sets can be chosen off the closed boundary. $\square$

### The analytic square

**Definition 10.8.6.** Let $S$ be an analytic system of dimension $d + 1$ indexed by a finite set, let $a_0$ be an index and let $\varepsilon$ be integers with $\varepsilon(a_0) = -2$. An analytic square for $(S, a_0, \varepsilon)$ consists of:

1. an analytic system $S_W$ of dimension $d + 2$ indexed by the indices and one extra index $\ast$, with two holomorphic maps $q_0, q_1$ to $S$ whose preimages of the open part are the open part of $S_W$;
2. the potentials, weights and regularized weights of $S_W$ at an index $a$ are those of $S$ pulled back by $q_0$, and at $\ast$ those of $a_0$ pulled back by $q_1$; for $a \neq a_0$ the weights pulled back by $q_0$ and $q_1$ agree;
3. a potential $L'$ with a section $v$ with $\lVert v \rVert \leq 1$ and normal crossings along a divisor $D$, also together with the boundary, and a constant $c$;
4. parameter covers $\Phi_Y$ of $S$ and $\Phi_W$ of $S_W$ over open sets $U_m$, compatible with $q_0$ and $q_1$, and smooth positive definite $2 \times 2$ matrices $G_m$ on $U_m$;
5. in a fibre chart, the sum of $\varepsilon_a$ times the potentials is the $\xi$-potential of $G_m$ in the fibre coordinate plus a pluriharmonic function, and for $a \neq a_0$ the potential is a smooth function of the base coordinates plus a pluriharmonic function;
6. for $z_0 \neq z_1$ in a chart of $S_W$,
$$
\begin{aligned}
\log \lVert v \rVert + c + \tfrac12 \sum_a \varepsilon_a & \bigl(\varphi_a \circ q_0 + \varphi_a \circ q_1\bigr) \\
&= \operatorname{logsin}_{G_m(w)}(z_0, z_1) .
\end{aligned}
$$

The $\xi$-potential and the log-sine function of a positive $2 \times 2$ matrix are defined in Section 9.

**Theorem 10.8.7 (Analytic square of an adjacent swap).** Assume the inputs, let $(\tau, a, b)$ be an adjacent swap, and assume that $y$ is an arithmetic variety of dimension $d + 2$. Then there are an analytic square $Q$ for $(S, (\tau, a), \xi_{\tau,a})$, an analytic log resolution $R_W$ of dimension $d + 2$ of the swap coordinates and a holomorphic map $e : R_W \to S_W$ of degree $1$ with no branch set, such that $q_0(e(x))$ lies under $z_0(x)$, $q_1(e(x))$ lies under a point equal to $z_1(x)$, $(q_0, q_1)$ is injective, and $\log \lVert v \rVert(e(x)) + c = \nu(z_0, z_1, h, t)$ for every admissible tuple.

Lean: `GlobalTheory.CompanionTheory.Ar.PB.WSq.ansq_exists` (also `GlobalTheory.T.flag_adjacent_swap_square_system`, a second name).

*Proof.* Step 1: the space. A dimension count gives the formula for $d + 1$. The lemma on swap atlases gives $R_W$, and an analytic lemma gives $q_0, q_1$ and the descent of the weights at $a \neq a_0$.

Step 2: the system. The pullback statement of the inputs, applied to $q_0$ and $q_1$, makes the pulled back weights singular weights with regularized families. This defines $S_W$.

Step 3: the square. The lemma on the diagonal divisor gives $L'$, $v$, $D$ and $c$, and the lemma on fibre charts gives the parameter covers and $G_m$. A lemma on the log resolution in fibre charts gives parts 5 and 6.

Step 4: the map. Take $e$ to be the identity. The identity for $\nu$ is the lemma on the diagonal divisor. $\square$

### Square systems

A square system for a realization of $S$ at $(a_0, \varepsilon)$ consists of a block $k_0$, an analytic square, an algebraic square on the coordinates of the realization (a variety of pairs of points that agree outside $k_0$, with a diagonal divisor $\Delta$ and two forms $g, h$ with $\operatorname{div} g = \operatorname{div} h + \Delta$ and balanced degrees), and a realization of $S_W$ in the algebraic square of the same degree, such that the lines at $a \neq a_0$ do not depend on the block $k_0$, the lines pull back along the two projections, and almost everywhere, for $0 < t \leq t_0$,
$$
\begin{aligned}
\log \frac{\lvert g \rvert}{\lvert h \rvert} + \tfrac12 \bigl(\log \Xi_t \circ v_0 + \log \Xi_t \circ v_1\bigr) = {} & \log \lVert v \rVert + c \\
&+ \tfrac12 \sum_a \varepsilon_a \bigl(\varphi_{a,t} \circ q_0 + \varphi_{a,t} \circ q_1\bigr),
\end{aligned}
$$
where $\Xi_t$ is the product of the lines at $t$ with exponents $\varepsilon$.

**Theorem 10.8.8 (Square systems on a flag cover).** Assume the inputs. Let $\mathcal{F}$ be analytic flag data of dimension $d$ for $B$, let $M'$ be a flag cover of $M$ with a covering realization of $\mathcal{F}$, and assume that $y$ is an arithmetic variety of dimension $d + 2$. Then for every adjacent swap $(\tau, a, b)$ there is a square system for the covering realization at $((\tau, a), \xi_{\tau,a})$.

Lean: `GlobalTheory.CompanionTheory.Relay.flag_cover_realisation_pullback` (also `GlobalTheory.T.flag_cover_realisation_pullback`, a second name).

*Proof.* This is the theorem on [square systems on a flag cover](/entry/t-c-sqsys/). The theorem on the analytic square gives $Q$, $R_W$ and $e$ for $\mathcal{F}$. Two forms on the swap variety of $M'$ give the algebraic square, a realization of this variety over $R_W$ gives the realization of $S_W$, and the norm identity follows from the identity for $\nu$. $\square$

**Remark 10.8.9 (Formalization).** The second names restate their theorems, except that `GlobalTheory.CompanionTheory.Relay.flag_cover_realisation_pullback` is itself a relay to `PositivityTheory.Xgp.t_c_sqsys` (`Development/AutomorphicSpectrum/Proofs/MetricProofs/FlagCoverRealisationPullback.lean:9`). Its name describes a pullback, not the existence of square systems. Other names do not match: `flag_adjacent_rows_dimension` gives the fibre charts (`FlagAdjacentRowsDimension.lean:28`), `flag_adjacent_twisted_measure` gives local sections (`FlagAdjacentTwistedMeasure.lean:99`), `flag_adjacent_rows_base_metric` gives the diagonal divisor. In `FlagAdjacentRowsBaseMetric.lean:19` the arithmetic variety hypothesis is not used. In `FlagAdjacentSwapSquareSystem.lean` the proof uses only the pullback field of the inputs (line 54), and the map $e$ is the identity (lines 152 to 155). Analytic squares and square systems are `AnSq` and `SqSys` in `GeometricAbelianConnected.lean` (lines 14 and 131). I did not unfold the chart, comparison and twisted chart lemmas behind the four lemmas, nor the lemma on the log resolution in fibre charts.
