---
title: The height lower bound
decls:
  - GlobalTheory.CovHt.HtTopG.heightAt_eq_of_cover
  - GlobalTheory.CovHt.HtTopG.height_of_meanAll_bound
  - SelfIntersectionVolumeEstimates.height_lower_bound_general_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The height lower bound

This section proves the height condition: on each good cover, the height of each component with respect to a quotient weight is bounded below by a mean slope, up to errors of order $E / T$. The bound is proved on one cover from five inputs: a short generating family, a geometric condition, a carrying section of bounded cost, an error budget and a lower bound for the mean slope over the components. Then the inputs are supplied as cover statements, from [the carrying sections](/entry/cover-height-section-bound-alt/) and from results of earlier chapters. With [the cover height sum](/entry/hilbert-samuel-of-component-estimates-alt/), the height condition is the main input of the covolume bound in the next section ([heights](/learn/arakelov/#heights)).

We keep the notation of the previous sections: a point $p$, a level $i$ with $i + 1 < m$, a good cover $Y$ at level $i + 1$, the length $T$, the unit $E$, the flag dimension $d$, the exponent $\zeta$ and, for a quotient weight $u_1$, the number $\rho_B(u_1)$ and the weight $u_1' = u_1 - 3(p + q) \lambda_H$. For a weight $u$ put $\ell_1(u) = \sum_{\tau, k} |u_{\tau, k}|$. For a component $Z$, $\delta_Z(u_1)$ is the generic degree and $h_Z(u_1)$ the height.

**Definition 2.8.1 (Height condition).** At $(p, i)$, with constant $C$ and a quotient weight $u_1$, the *height bound* says: there are $c_s, c_c, X \ge 0$ and a function $s$ on the components such that for every component $Z$
$$0 \le h_Z(u_1) + c_s, \qquad \bigl(1 - \rho_B(u_1)\bigr) \max\bigl(0, s(Z) + c_s\bigr) \le h_Z(u_1) + c_s + c_c,$$
the mean of $s$ over the components is at least $-X$, and
$$T X \le C E, \qquad T c_c \le C E, \qquad c_s \bigl( 6d + 10 + T(\zeta + 2 \rho_B(u_1)) \bigr) \le C E.$$
The *height condition* is the cover statement of the height bound for all quotient weights.

The five inputs are the following conditions at $(p, i)$, with constant $C$, for a quotient weight $u_1$ on $Y$.

- *Short*: there is $\Lambda$ such that on each component the lattice of cusp forms of weight $u_1$ has a short generating family with constant $\Lambda$, and $\log \Lambda \, (6d + 10 + T(\zeta + 2 \rho_B(u_1))) \le C E$.
- *Geometric*: on each component $Z$, $Y$ is good at $u_1$, the cusp forms of weight $u_1$ are birational on $Z$, and $(1 - \rho_B(u_1)) \delta_Z(u_1) \le \delta'_Z(u_1)$, where $\delta'_Z(u_1)$ is the top degree of $u_1'$ on $Z$.
- *Multiplicity*: there is $c \ge 0$ with $T c \le C E$ such that on each component $Z$ the lattice of weight $u_1$ has no base points at the finite places, and there are a carrying section $\theta$ from $u_1'$ to $u_1$, a function $e$ on the finite places and a function $t$ on the embeddings, with the finite bound, the infinite bound and cost at most $c$.
- *Budget*: the level of $Y$ has at most $15$ prime factors, and there is a gap $g$ of $u_1'$ such that the error $\mathrm{err}(u_1', g)$ and the height cost $\mathrm{hc}(u_1', g) \, \ell_1(u_1')$ are nonnegative and at most $C E / T$.

Here the *cost* of $(e, t)$ is
$$\mathrm{cost}(e, t) = \frac{1}{[F : \mathbb{Q}]} \Bigl( \sum_\lambda e_\lambda \log N\lambda + \sum_\sigma t_\sigma \Bigr),$$
and the infinite bound says that $t$ is invariant under complex conjugation and that $\|\theta\|_y^2 \le e^{16 t_\sigma} \beta_Z(y)^8$ at every frame $y$ on $Z$ and every good embedding $\sigma$, where $\beta_Z$ is the Bergman function of weight $u_1$ of [the previous section](/entry/exp-neg-b-le-berg-on-of-mem-frames-on/). The finite bound says that, at each finite place and each recording valuation $v$ that is finite on the lattice, $8$ times the depth of the lattice under $v$ is at most $v(\theta) + 8 e_\lambda$.

**Definition 2.8.2 (Gap, bound and error).** A weight $u$ has *gap* $g > 0$ if each row $u_\tau$ is strictly decreasing and $|u_{\tau, a} - u_{\tau, b}| \ge g$ whenever $a \ne b$ and $a \ge p$. Put
$$B(u, g) = 4 f (p + q)^2 \Bigl( 1 + \frac{\max_{\tau, k} |u_{\tau, k}|}{g} \Bigr).$$
For $s \in \mathbb{R}$ the *error* is
$$\mathrm{err}_s(u, g) = \bigl( \log B(u, g) + s \bigr) \ell_1(u) + q \sum_\tau \bigl( \max_k u_{\tau, k} - \min_k u_{\tau, k} \bigr).$$
In the budget, $s = \ell$, where $\ell = \log \mathrm{rd}(E) + |\lambda_L|$ is the sum of the log root discriminant and the absolute value of the logarithmic derivative $\lambda_L$ of the $L$-function of the host at $1$, which we do not unfold.

**Definition 2.8.3 (Mean slope bound).** Let $u$ be a weight, $B, X \in \mathbb{R}$. The *mean slope bound* says that there is a function $s$ on the components with $s(Z) \le \mathrm{vs}_B(Z, u)$ for each $Z$, and with mean over the components at least $-X$. Here $\mathrm{vs}_B(Z, u)$ is the volume slope of $Z$ at the weight $u$ with the mixed valuations of the bound $B$, which we do not unfold. For $s, C \in \mathbb{R}$, the *mean slope hypothesis* $\mathrm{MS}(s, C)$ says that every weight $u$ with gap $g$ satisfies the mean slope bound with $B = B(u, g)$ and $X = C \, \mathrm{err}_s(u, g)$.

The height cost comes from the comparison of two families of valuations. Put
$$\eta(q) = \frac{1}{q - 1} + 40 \, \frac{v_q(\mathrm{disc}\, E)}{[E : \mathbb{Q}]}.$$
The *height comparison* on $Y$ says that at each prime $q$ and each finite place $\lambda$ over $q$, each recording valuation $v$ at $\lambda$ has a height valuation $w$ at $\lambda$ with $w(f) \le v(f) + v_\lambda(q) \, \eta(q) \, \ell_1(u)$ for every section $f$ of every weight $u$. The *height cost* of $(u, g)$ is $\mathrm{hc}(u, g) = \sum_q \eta(q) \log q$, the sum over the height primes of the level for the bound $B(u, g)$.

**Theorem 2.8.4 (The height bound on one cover).** Assume the volume estimate hypotheses and the published Hodge bundle theorems. Let $Y$ be good with the height comparison, let $C_0, C_s, C_m, C_b \ge 0$, $E \ge 0$, and assume $\mathrm{MS}(\ell, C_0)$ on $Y$ and that $Y$ has a component. Let $u_1$ be a weight with $\rho_B(u_1) < 1$ that satisfies the cover degree condition, and the short, geometric, multiplicity and budget conditions with constants $C_s$, $C_m$ and $C_b$. Then the height bound holds for $u_1$ with the constant
$$C_s + C_m + C_b + C_0 C_b.$$

Lean: `GlobalTheory.CovHt.HtTopG.heightAt_eq_of_cover`.

*Proof.* Take $\Lambda$ from the short condition, $c$ from the multiplicity condition and the gap $g$ from the budget. Apply $\mathrm{MS}(\ell, C_0)$ to $u_1'$ with gap $g$: this gives a function $s$ with $s(Z) \le \mathrm{vs}_B(Z, u_1')$ and mean at least $-C_0 \, \mathrm{err}_\ell(u_1', g)$, where $B = B(u_1', g)$. Put
$$c_s = \log \Lambda, \qquad c_c = c + \mathrm{hc}(u_1', g) \, \ell_1(u_1'), \qquad X = C_0 \, \mathrm{err}_\ell(u_1', g).$$
Then $c_s \ge 0$, since a short generating family has constant $\Lambda \ge 1$. By the cover degree condition $\delta_Z(u_1) > 0$ on each component.

Nonnegativity: on a component $Z$, the image height of the short generating family is nonnegative, by a divisor argument from the published list. This gives $0 \le h_Z(u_1) + \log \Lambda$.

The main inequality: fix $Z$ and $\varepsilon > 0$. The bound $s(Z) \le \mathrm{vs}_B(Z, u_1')$ gives a lower bound for the volume of $Z$ at the weight $u_1'$:
$$\delta'_Z(u_1) \bigl( s(Z) + c_s \bigr) \le \text{the component volume}.$$
The carrying section $\theta$ maps small sections of weight $8k u_1'$ to small sections of weight $8k u_1$, with the finite and infinite bounds and the height comparison controlling the losses; so the component volume is at most the volume of the small sections of weight $u_1$ with the shift $c_s + c_c + \varepsilon$. A volume bound for line bundles, from the volume estimate hypotheses, bounds the latter by
$$\delta_Z(u_1) \bigl( h_Z(u_1) + c_s + c_c + \varepsilon \bigr).$$
If $s(Z) + c_s \le 0$ the claim follows from the nonnegativity. Otherwise the geometric condition gives $(1 - \rho_B(u_1)) \delta_Z(u_1) \le \delta'_Z(u_1)$, so
$$\bigl(1 - \rho_B(u_1)\bigr) \bigl( s(Z) + c_s \bigr) \delta_Z(u_1) \le \bigl( h_Z(u_1) + c_s + c_c + \varepsilon \bigr) \delta_Z(u_1).$$
Divide by $\delta_Z(u_1) > 0$ and let $\varepsilon \to 0$.

The bounds: $T X \le C_0 C_b E$ by the budget; $T c_c \le (C_m + C_b) E$ by the multiplicity condition and the budget; and $c_s(6d + 10 + T(\zeta + 2 \rho_B)) \le C_s E$ by the short condition. All three are at most $(C_s + C_m + C_b + C_0 C_b) E$, as all constants and $E$ are nonnegative. $\square$

**Theorem 2.8.5 (The height condition from the mean slope hypothesis).** Assume the volume estimate hypotheses, the published Hodge bundle theorems, deep goodness, the size condition, the cover degree condition, and the short, geometric, multiplicity and budget conditions as cover statements. Assume the mean slope hypothesis in the following form: there is $C_0 \ge 0$ such that for every family $D$ and core $T$ with the laws of the core and $m^2 \le k$, every level $1 \le j < m$ and every good cover $Y$ at level $j$ whose level has at most $15$ prime factors, $\mathrm{MS}(\ell, C_0)$ holds on $Y$. Then the height condition holds.

Lean: `GlobalTheory.CovHt.HtTopG.height_of_meanAll_bound`.

*Proof.* Combine the seven cover statements, with constants $C_1, \dots, C_7$ for deep goodness, the size condition, the cover degree, the short, geometric, multiplicity and budget conditions. Take the constant $C_4 + C_6 + C_7 + C_0 C_7$ and the largest threshold. Fix a point, a level $i + 1 < m$, a good cover $Y$ and a quotient weight $u_1$. The size condition gives $1 \le b \le E$, so $E \ge 0$, and $\rho_B(u_1) < 1$. Deep goodness gives that $Y$ has a component. The height comparison holds on every good cover, by a comparison of valuations from the published list. The parameters of the family satisfy $m^2 \le k$, and the budget gives the bound on the prime factors, so the mean slope hypothesis applies to $Y$ at level $i + 1$. Now [Theorem 2.8.4](/entry/height-at-eq-of-cover/) gives the height bound with $C_4 + C_6 + C_7 + C_0 C_7$. $\square$

**Theorem 2.8.6 (Height lower bound).** Assume the volume estimate hypotheses, the hypotheses on the family, Grothendieck's deformation theory, the quoted results, the published Hodge bundle theorems, the hypotheses on toroidal compactifications, the deep mean slope statement, deep goodness, the size condition, the cover degree condition and the flat degree condition. Then the height condition holds.

Lean: `SelfIntersectionVolumeEstimates.height_lower_bound_general_alt`.

*Proof.* We apply [Theorem 2.8.5](/entry/height-of-mean-all-bound/). The short condition follows from the published list, deep goodness, the size condition and the flat degree condition. The geometric condition follows from the hypotheses on the family, Grothendieck's deformation theory, the quoted results, the published list, the Siegel toroidal integral, the toroidal compactifications for fans and the seminegativity of the Lie algebra, together with deep goodness and the size condition. The multiplicity condition follows from [the reference bound for the weight](/entry/refined-sum-weight-of-size-alt/), which controls the finite places, and [the carrying section with bounded cost](/entry/cover-height-section-bound-alt/). The budget follows from the host numerics, the weight numerics and the size condition. The deep mean slope statement is the mean slope hypothesis. $\square$

The mean slope hypothesis is the one input of this section that is not proved here. In the covolume bound it is supplied by a separate argument from the published results.

**Remark 2.8.7 (Formalization).** The bound on one cover is at [HeightAddLogNonneg.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/HeightAddLogNonneg.lean#L66). Its name says "eq", but it concludes the inequalities of the height bound. The same file has a cover version at line 107, and the two steps of the proof at lines 18 and 29, which use `GlobalTheory.ImageHeightNonneg.imageHeight_nonneg_of_divisor`, `GlobalTheory.CovHtCmp.compVol_le_volL_deep` and `SelfIntersectionVolumeEstimates.VolUpG.volume_line_bundle_le`. The description of these three steps follows their statements. The second theorem is at [HeightOfSteps.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/HeightOfSteps.lean#L19); it takes the height comparison from `GlobalTheory.CovHt.cover_height_comparison` and $m^2 \le k$ from `m_sq_le_k`, and it does not use the constants of deep goodness, the size condition, the cover degree or the geometric condition in the final constant. The third theorem is a term proof at [HeightLowerBoundGeneral.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/HeightLowerBoundGeneral.lean#L21); its inputs are `covering_short_of_deep_size_flatDeg`, `covHt_geom_of_siegel_toroidal_semiAbelian`, `carrying_section_integral_frame_alt` and `budget_of_hostN_of_liftWeight_of_size`, and the deep mean slope statement `DeepStR` ([ModelSmall.lean](lean:Development/AutomorphicSpectrum/Definitions/GlobalGeometry/ModelSmall.lean#L63)) is passed through as the mean slope hypothesis. We have not unfolded `IsShortGen`, `delPrime`, `compVolSlope`, `mixVals`, `NoBase`, `depthOn`, `recVals`, `htVals`, `htPrimes` or `dlogL`.
