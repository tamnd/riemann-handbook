---
title: Analytic flag data and step weights
decls:
  - GlobalTheory.CompanionTheory.Ar.PB.stepWeight_exists
  - GlobalTheory.T.partial_flag_bundle_metric_line
  - GlobalTheory.CompanionTheory.Ar.PB.FA.step_member
  - GlobalTheory.CompanionTheory.Ar.PB.FA.flagAn_of_res
  - GlobalTheory.CompanionTheory.Ar.PB.FA.flagAn_exists
  - GlobalTheory.T.flag_model_analytic_data_exists
  - GlobalTheory.CompanionTheory.Ar.PB.ConjOf.flagAn_exists_conj
  - GlobalTheory.T.flagModel_arith_dimension_boundary
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Analytic flag data and step weights

This section turns a flag model with a base metric into an analytic system: a compact complex manifold with a family of singular hermitian lines, one for each step of the flag, together with smooth regularizations of their weights. We first prove that the metric of one step differs from a Fubini-Study metric by a singular weight with a gradient bound. Then we regularize the weights, collect them into analytic flag data, and make the data invariant under conjugation. The analytic flag data are the input of [square systems on a flag cover](/entry/t-c-sqsys/) and of the adjacent swap squares of Section 8. We use [metrics and positivity](/learn/positivity-resolution/#metrics-curvature-and-positivity) and [Chern-Weil forms](/learn/positivity-resolution/#chern-weil-forms).

### Singular weights and regularized families

Let $X$ be a compact complex manifold of dimension $e$ with a finite holomorphic atlas, let $\Theta$ be a smooth positive potential, and let $L$ be a potential with a section $s$ that has simple normal crossings and $\lVert s\rVert \leq 1$. Let $\partial = \{ s = 0 \}$ and let $r_W$ be the log distance to $\partial$, so $r_W \geq 1$. Plurisubharmonic means here that the Levi form is nonnegative in every chart.

**Definition 10.7.1.** Let $\theta$ be a potential and let $C_5$ be a number. A function $\varphi : X \to \mathbb{R}$ is a singular weight for $\theta$ with constant $C_5$ if $\varphi$ is smooth off $\partial$, $\theta + \varphi$ is plurisubharmonic off $\partial$, and $-C_5 \log r_W \leq \varphi \leq C_5$ off $\partial$. It has a gradient bound with constant $C_5$ for an adapted atlas if, in each chart and off $\partial$ on the ball of radius $3/2$,
$$
\lVert d\varphi \rVert \leq C_5\, r_W^{C_5}\, \exp(r_W / 2) .
$$

For $0 < t < 1$ and a constant $C$ put
$$
\varepsilon_C(t) = \frac{C \log\log(1/t)}{\log(1/t)} .
$$

**Definition 10.7.2.** A regularized family for a singular weight $\varphi$ of $\theta$ with constants $C$ and $0 < t_0 < 1$ is a family $\varphi_t$ such that for $0 < t \leq t_0$:

1. $\varphi_t$ is smooth, $\varphi_t \leq C$, and $\varphi_t \geq -C \log\log(1/t)$;
2. $\varphi \leq \varphi_t$ off $\partial$;
3. $\theta + \varphi_t + \varepsilon_C(t)\, \Theta$ is plurisubharmonic;
4. off $\partial$, $\varphi_t \leq \varphi + t^{1/3} + \varepsilon_C(t)\, r_W$, and $\varphi_t \leq \varphi + t^{1/3} + \varepsilon_C(t)$ where $r_W \leq \log(1/t)$;
5. $\varphi_t \leq \varphi_{t'} + C \varepsilon_C(t')$ for $t \leq t' \leq t_0$.

It converges in $C^2$ if $\varphi_t$ and its first and second derivatives converge to those of $\varphi$, uniformly on compact sets off $\partial$ in each chart, as $t \to 0^+$.

The inputs of the development include two statements on these objects. The regularization statement says that a singular weight with a gradient bound for an adapted atlas has a regularized family that converges in $C^2$. The pullback statement says that a regularized family pulls back along a holomorphic map of log resolutions to a regularized family with new constants.

### The weight of one step

Let $M$ be a flag model of type $(N, j)$ over $y$ and let $B$ be a base metric of dimension $n$ on $M$, with lines $h_p$ for the steps $p = (\tau, i)$ (Section 6). For a multidegree $a$ let $h_{\mathrm{FS}}(a)$ be the Fubini-Study metric of this multidegree on the product of projective spaces. A block map $(\kappa, v)$ keeps the step $p$ if every block of the base and the block of $p$ is in the image of $\kappa$.

**Theorem 10.7.3 (Step weight).** Let $p$ be a step and let $(\kappa, v)$ be a block map that keeps $p$. Let $R$ be an analytic log resolution of dimension $e$ of the coordinate ideal of $y \circ v$, with a holomorphic map $\mathrm{pr}$ to the resolution $X_b$ of $B$ and an atlas $A'$. Assume that every point $x$ of $R$ has a lift $z$ to the coordinates $y$ with $z \circ v$ equal to the point of $x$ and with base part in the orbit of the point of $\mathrm{pr}(x)$. Assume that the pullbacks of $L$ and $s$ are a potential and a section with normal crossings, and that $A'$ is adapted to them. Then there are $\varphi$ and $C_5$ such that:

1. off $\partial$, for every lift $z$ of $x$,
$$
\log h_p(z) = \log h_{\mathrm{FS}}(d_y(p))(z) + \varphi(x) ;
$$
2. $\varphi(x) = \varphi(x')$ if $\mathrm{pr}(x) = \mathrm{pr}(x')$ and the coordinates of $x$ and $x'$ in the block of $p$ are proportional;
3. $\varphi$ is a singular weight with constant $C_5$ for the Fubini-Study potential of degree $d_y(p) \circ \kappa$;
4. $\varphi$ has a gradient bound with constant $C_5$ for $A'$.

Lean: `GlobalTheory.CompanionTheory.Ar.PB.stepWeight_exists` (also `GlobalTheory.T.partial_flag_bundle_metric_line`, a second name).

*Proof.* Let $\varphi$ be the step gap: the difference of $\log h_p$ and $\log h_{\mathrm{FS}}(d_y(p))$ at a lift, pulled back to $R$. Four pullback lemmas show that $\varphi$ is smooth off $\partial$, that $h_{\mathrm{FS}} + \varphi$ is plurisubharmonic off $\partial$, that $\varphi$ is bounded above by a constant $C_1$, and that its gradient is controlled by the gradient bound of $B$.

A lemma on singular potentials with log growth gives a constant $C_2$ such that $\varphi$ is a singular weight with constant $C_2$. A local lemma for adapted atlases gives a constant $C_3$ for the gradient bound. Put $C_5 = \max(C_2, C_3)$. Since $\log r_W \geq 0$, the lower bound with $C_2$ implies the one with $C_5$. Parts 1 and 2 are the two remaining pullback lemmas. $\square$

### Step members

Fix the regularization and pullback statements. Let $R$ be an analytic log resolution of the coordinate ideal of $y$, of dimension
$$
e = n + \lvert\Psi\rvert \Bigl(\tbinom{j}{2} + \tbinom{N - j}{2}\Bigr),
$$
with a holomorphic map $\mathrm{pr}$ to $X_b$ that is compatible with the base points, and with $L$ and $s$ pulled back to a potential and a section with normal crossings. A step member for $p$ is a tuple $(\varphi, \varphi_t, h_t, C_5, C, t_0)$ with these properties:

1. $\varphi$ is a singular weight for $h_{\mathrm{FS}}(d_y(p))$ with constant $C_5$, and $\varphi_t$ is a regularized family for it with constants $C$ and $t_0$, for $\Theta = h_{\mathrm{FS}}(1)$, that converges in $C^2$;
2. each $h_t$ is a hermitian line of degree $d_y(p)$ that depends only on the base part and the block of $p$; for $0 < t \leq t_0$ it is smooth and $\log h_t = \log h_{\mathrm{FS}}(d_y(p)) + \varphi_t$;
3. off $\partial$, $\log h_p = \log h_{\mathrm{FS}}(d_y(p)) + \varphi$;
4. $\varphi$ and $\varphi_t$ satisfy the descent condition of part 2 of the step weight theorem;
5. if $p$ is the last step, $i + 1 = N$, then $\varphi_t = \varphi$ for all $t$, and $h_{\mathrm{FS}}(d_y(p)) + \varphi$ and its negative are both plurisubharmonic.

**Lemma 10.7.4 (Step member).** Under these assumptions every step $p$ has a step member.

Lean: `GlobalTheory.CompanionTheory.Ar.PB.FA.step_member`.

*Proof.* Step 1: the partial resolution. Restrict the coordinates to the base blocks and the block of $p$. This is a block map that keeps $p$. A lemma on partial flag bundles gives an analytic log resolution $R_p$ of the partial coordinate ideal, with a map $\mathrm{pr}_p$ to $X_b$ and compatible charts. The pullback of $L$ and $s$ to $R_p$ has normal crossings and an adapted atlas. The step weight theorem on $R_p$ gives a weight $\varphi'$ with constant $C_5$ and a gradient bound.

Step 2: the projection. The projection of blocks is a holomorphic map $h : R \to R_p$, and $\mathrm{pr} = \mathrm{pr}_p \circ h$.

Step 3: regularization on $R_p$. If $p$ is the last step, the weight $\varphi'$ is flat off $\partial$, and a central regularity lemma gives a smooth weight $\varphi_2$ equal to $\varphi'$ off $\partial$ such that the potential and its negative are plurisubharmonic; put $\varphi_{2,t} = \varphi_2$. Otherwise the regularization statement gives a regularized family $\varphi_{2,t}$ for $\varphi_2 = \varphi'$ that converges in $C^2$.

Step 4: transport to $R$. The weight descends along orbits, so $\log h_p = \log h_{\mathrm{FS}} + \varphi_2 \circ h$ off $\partial$. The pullback statement gives a regularized family on $R$ with constants $C'$ and $t_0'$. The Fubini-Study potential of $R_p$ pulls back to that of $R$ because the degrees vanish outside the block of $p$. Put $\varphi = \varphi_2 \circ h$, $\varphi_t = \varphi_{2,t} \circ h$, and
$$
T = \min\bigl(t_0, t_0', \exp(-1)\bigr) ,
$$
and enlarge the constants to $\lvert C' \rvert$ and $T$.

Step 5: the lines. For $0 < t \leq T$, the smooth function $\varphi_{2,t}$ is the log of a hermitian line of degree $0$ on $R_p$, and a lemma on step lines turns it into a line $h_t$ of degree $d_y(p)$ on the step. For other $t$ we use the trivial line. The last step case of part 5 follows by pulling back the two plurisubharmonic potentials along $h$. $\square$

### Analytic flag data

**Definition 10.7.5.** Analytic flag data of dimension $d$ for a base metric $B$ on $M$ consist of an analytic system $S$ of dimension $d + 1$, indexed by the steps and one extra index $\ast$, with a realization in the coordinate ideal of $y$, such that:

1. the realization has degree $1$ and no branch set, with reference lines $h_{\mathrm{FS}}(d_y(p))$ at the steps and $h_{\mathrm{FS}}(1)$ at $\ast$;
2. the line, the weight and the regularized weights at $\ast$ are $h_{\mathrm{FS}}(1)$, $0$ and $0$, and for some $c_0 > 0$ the regularized potential at $\ast$ minus $c_0 \Theta$ is plurisubharmonic for all $t$;
3. there is a holomorphic map $\mathrm{pr}$ to $X_b$, compatible with the base points, along which $L$ and $s$ pull back to those of $S$;
4. on the open part, $\log h_p = \log h_{\mathrm{FS}}(d_y(p)) + \varphi_p$;
5. the lines at each step depend only on the base part and the block of the step, and the weights satisfy the descent condition;
6. at a last step the regularized potential and its negative are plurisubharmonic and $\varphi_{p,t} = \varphi_p$.

**Lemma 10.7.6 (Analytic flag data from a resolution).** Fix the regularization and pullback statements. Let $R$ be an analytic log resolution of dimension $d + 1$ of the coordinate ideal of $y$, with a holomorphic map $\mathrm{pr}$ to $X_b$ that is compatible with the base points. Assume that the coordinate ideal of $y$ is an arithmetic variety of dimension $d + 2$, that
$$
d + 1 = n + \lvert\Psi\rvert \Bigl(\tbinom{j}{2} + \tbinom{N - j}{2}\Bigr),
$$
and that near every point there is a chart of $R$ whose coordinates contain, through an embedding of index sets, the coordinates of a chart of $X_b$ at the image. Then there are analytic flag data of dimension $d$ for $B$.

Lean: `GlobalTheory.CompanionTheory.Ar.PB.FA.flagAn_of_res`.

*Proof.* The chart condition shows that $L$ and $s$ pull back to $R$ with normal crossings and an adapted atlas. The Fubini-Study potential $\Theta = h_{\mathrm{FS}}(1)$ is positive. Choose a step member for every step by the lemma. For the index $\ast$, a lemma on smooth members gives, for the weight $0$, a singular weight constant $C_0$, a regularized family and $C^2$ convergence. There are finitely many indices, so take common bounds $D_5$ and $D$ for the constants and a common scale $T > 0$ below all $t_0$ and below $\exp(-\exp(1))$; enlarging the constants keeps the step member properties. The analytic system has the potentials $h_{\mathrm{FS}}(d_y(p))$ and $\Theta$, the weights of the step members and $0$, and the constants $D_5$, $D$ and $T$. The realization is the identity on $R$, of degree $1$, with no branch set. At $\ast$ take $c_0 = 1$: the regularized potential minus $\Theta$ is $0$. The other properties are those of the step members. $\square$

**Theorem 10.7.7 (Analytic flag data).** Assume the inputs. Let $M$ be a flag model of type $(N, j)$ over $y$ and let $B$ be a base metric of dimension $n$ on $M$. If the coordinate ideal of $y$ is an arithmetic variety of dimension $d + 2$ and
$$
d + 1 = n + \lvert\Psi\rvert \Bigl(\tbinom{j}{2} + \tbinom{N - j}{2}\Bigr),
$$
then there are analytic flag data of dimension $d$ for $B$.

Lean: `GlobalTheory.CompanionTheory.Ar.PB.FA.flagAn_exists` (also `GlobalTheory.T.flag_model_analytic_data_exists`, a second name).

*Proof.* Apply the lemma on partial flag bundles to the identity block map, which keeps every step. It gives an analytic log resolution $R$ of the coordinate ideal of $y$ with a map to $X_b$, compatible base points and compatible charts. Its dimension is the number $d + 1$ of the hypothesis. The lemma on analytic flag data from a resolution, with the regularization and pullback statements of the inputs, gives the data. $\square$

### Invariance under conjugation

A hermitian line $h$ is invariant under conjugation if $h(\bar z) = h(z)$ for all $z$.

**Theorem 10.7.8 (Conjugation invariant flag data).** Under the hypotheses of the theorem on analytic flag data, assume that:

1. if the base point of $x'$ is in the orbit of the conjugate of the base point of $x$, then $x' \in \partial$ if and only if $x \in \partial$, and $r_W(x') = r_W(x)$;
2. off $\partial$, every line $h_p$ of $B$ is invariant under conjugation at the points over $x$.

Then there are analytic flag data of dimension $d$ for $B$ whose lines are all invariant under conjugation.

Lean: `GlobalTheory.CompanionTheory.Ar.PB.ConjOf.flagAn_exists_conj` (also `GlobalTheory.T.flagModel_arith_dimension_boundary`, a second name).

*Proof.* Take analytic flag data by the theorem. Since the realization has degree $1$ and no branch set, it is a biholomorphism onto the resolution, and the resolution carries a complex conjugation $c$ that is antiholomorphic in charts. Replace each step line $h_t$ by its conjugation average
$$
\bar h_t(z) = \sqrt{\lvert h_t(z)\, h_t(\bar z) \rvert}
$$
at the clamped parameter, that is at $T$ when $t$ is not in $(0, T]$. Replace each regularized weight by the mean of $\varphi_t$ and $\varphi_t \circ c$. The weights $\varphi_p$ are invariant under $c$ by assumption 2, and the boundary and $r_W$ by assumption 1, so the mean is again a regularized family after a monotone change of constants. The averaged lines are on the steps and invariant. $\square$

**Remark 10.7.9 (Formalization).** The second names only restate their theorems. In `Development/AutomorphicSpectrum/Proofs/MetricProofs/PartialFlagBundleMetricLineStatement.lean:8` and in `PartialFlagBundleMetricLine.lean:19` the statement quantifies over a natural number `d` that does not occur in it. The name `flagModel_arith_dimension_boundary` does not describe its statement, which is the conjugation invariance of the lines; its proof in `FlagModelArithDimensionBoundary.lean:10` applies `flagAn_conj` (`SmoothContinuous.lean:339`) to the theorem on analytic flag data. The conjugation results live in a file named `SmoothContinuous.lean` (the main proof is `conj_of_flagAn`, line 112, with the averages `avgSys` and `avgLine` at lines 61 and 73). Analytic flag data are `FlagAn` in `Definitions/MetricPeriods/IsPeriodOn.lean:72`, and step members are `IsStepMember` in `PartialFlagBlocks.lean:48`. The two lemmas and the main theorem are in `FlagModelAnalyticDataExists.lean` (lines 74, 230 and 359); the theorem uses only the fields `regGlobal` and `pullback` of the inputs. I did not unfold the pullback lemmas behind the step weight, the lemma on partial flag bundles, the central regularity lemma, the lemma on step lines, nor the lemmas on the conjugation of lift systems.
