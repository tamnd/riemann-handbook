---
title: Component data and the base setting
decls:
  - GlobalTheory.CompanionTheory.Ar.exists_componentData_origin
  - GlobalTheory.T.full_intersection_generic_bound
  - GlobalTheory.CompanionTheory.Relay.intersection_final_estimate
  - GlobalTheory.T.intersection_final_estimate
  - GlobalTheory.CompanionTheory.Relay.good_origin_intersection_relay
  - GlobalTheory.T.good_origin_intersection_relay
  - GlobalTheory.CompanionTheory.Ar.Cusp.testPoly_eq_slX
  - GlobalTheory.T.good_origin_intersection_tower
  - GlobalTheory.CompanionTheory.Ar.Cusp.TopBase.base_setting_of_good_origin
  - GlobalTheory.T.base_setting_of_good_tower
status: drafted
drafted_by: writer@claude-opus-5-5
---

## Component data and the base setting

The previous sections give a cusp weight with [tied regularisations](/entry/relay-cusp-weight-regularisations-tied/) and [height constants](/entry/nine-geo-u-of-given/) for the twisted cusp lines. This section puts these parts into one analytic setting on each component of a good tower, at each level $B$. The intersection number of the test polynomial on the component is then the slope of the setting times a positive volume factor, and the setting satisfies a Stokes bound. For the background see [arithmetic intersection numbers](/learn/arakelov/#arithmetic-varieties-and-intersection-numbers) and [arithmetic volume](/learn/arakelov/#arithmetic-volume-and-bigness).

Let $E$ be a CM field with host data $H$, let $D$ be a datum of signature $(p, q)$ with $N = p + q$, let $Y$ be an integral model at level $l$, and let $f$ be the number of CM types. Component data $D_c$ consist of coordinates $y$, integers $j < N$ with $j' = N - j$, a dimension $n$, a boundary set $\mathrm{Bd}$, an open part $X_o$, a set of primes $S$, vertical primes $S_B$ at each level $B$, and an ample line with a constant $K_A$. A component origin for a set of primes $S_0$ is a Hodge component $\mathfrak{M}$ of $Y$ with $S_0$ removed, on the coordinates of $D_c$, with a side for the labels and a side for the cusp weight. We do not unfold these. The component is free at a prime $\ell$ if the Hodge lattice at $\ell$ and its label parts are vector bundles of full rank on the fibre at $\ell$.

**Theorem 8.7.1 (Component data at an origin).** Assume the top level inputs and the Weil pairing statement. Let $Y$ be global, let $\mathrm{II}$ be a full intersection system, let $p, q \ge 1$, and let $\xi_0$ be a generic point of a component of $Y$. Let $S_0$ and $S_1$ be disjoint finite sets of primes such that $S_0$ contains every prime that divides the discriminant of $E$, and let $s$ be a side. Then there are component data $D_c$, Hodge data $\mathcal{H}$ and a component origin for $S_0$ with these properties.

1. Its Hodge component $\mathfrak{M}$ has the generic point of $\xi_0$, and the primes of $D_c$ are $S_1$.
2. If $s$ is the second side, $j = q$ and the labels lie on the second side. Otherwise $j = p$ and the labels lie on the first side.
3. The Hodge lattice of $\mathfrak{M}$ is a vector bundle, and $\mathfrak{M}$ is free at every prime of $S_0 \cup S_1$.

Lean: `GlobalTheory.CompanionTheory.Ar.exists_componentData_origin` (also `GlobalTheory.T.full_intersection_generic_bound`, a second name)

*Proof.* The side $s$ fixes the two label sides, with ranks $j$ and $N - j$. A global system of normal crossings charts for the component of $\xi_0$, with $S_0$ removed, gives $y$, $\mathfrak{M}$, a boundary, the vertical data, the vector bundle property and freeness at $S_0 \cup S_1$. The rank bounds of the host give $n = f\, j\, (N - j)$. The boundary points are closed and stable under the torus and under conjugation, so there are torus stable charts. A positive hermitian line is the ample line, with weight $1$ and $K_A = 0$. For each CM type the lattices of the two labels add up to a vector bundle of rank $N$, and a degree bound for this pair lattice gives the chart metrics. The intersection sum of the component data gives $\mathcal{H}$. $\square$

A component setting $X$ on $D_c$ consists of Hodge data $\mathcal{H}$ with line $\mu$, a cusp weight $U$, a complex model, a tied regularisation $S$ of log log type for $\mu$, a tied bounded regularisation $S'$ for $\varphi_\mu + U/2$, and real numbers $\mathrm{rd}$ and $L$. Let $\deg_\mu$ be the geometric degree of $\mu$, and let $\operatorname{mean}_U$ be the mean of $U$ for the measure $c_1(\mu)^n / \deg_\mu$. For $t > 0$, the regularised line $\mu_{B, t}$ is the smooth line with weights $a_\mu + \sum_{\ell \in S_B} \deg_\ell$ and metric $h_{S, t} \prod_{\ell \in S_B} v_\ell$, where $v_\ell$ is the vertical factor at $\ell$. The arithmetic limit and the slope are

$$
\operatorname{ar}_X(B) = \lim_{t \to 0^+} \mathrm{II}\big(\mu_{B, t}^{\,n + 1}\big), \qquad \operatorname{sl}_X(B) = \frac{\operatorname{ar}_X(B)}{(n + 1) \deg_\mu}.
$$

For $1 \le p' \le q'$ and $t' > 0$, let $M_{p', q', t'}$ be the twisted cusp line at the level $B$ built from $S'$.

**Definition 8.7.2 (Stokes bound).** The setting $X$ satisfies the Stokes bound at $B$ if $(n + 1)(a - \operatorname{mean}_U / 2) \deg_\mu \le \operatorname{ar}_X(B)$ for every real $a$ with this property: for all $1 \le p' \le q'$ and all small $t' > 0$,

$$
(n + 1)\Big(a - \frac{p'}{q'} K_A\Big) \deg M_{p', q', t'} \le \widehat{\deg}\, M_{p', q', t'}^{\,n + 1}.
$$

Lean: `GlobalTheory.CompanionTheory.Ar.Top.StokesAt`

A component origin is admitted at the level $B_1$ if $Y$ is global, the component is free at the primes of $S_0$ and $D_c$, $S_0$ is the set of primes that divide $2\, d_E\, M_l$ and has at most $4 f N^2$ elements, $B_1 \ge 4f + 2$, the primes of $D_c$ are the primes $\ell \le B_1$ outside $S_0$, and $j' \le j$.

**Theorem 8.7.3 (Stokes bound for the cusp setting).** Assume the inputs of the proof theory, the analytic input, resolution of singularities in characteristic $0$, the GAGA input for flat sections and the extension theorem for homomorphisms of semi-abelian schemes. Let $E$ be abelian Galois over $\mathbb{Q}$, let $\mathrm{II}$ be full, let the origin be admitted at some level, let $U$ be a cusp weight for the origin, and let $X$ have Hodge data $\mathcal{H}$ and cusp weight $U$ on $X_o$. Assume that for every $B \ge 4f + 2$, all $1 \le p' \le q'$ and small $t'$, the lines $M_{p', q', t'}$ are semipositive, nef on the fibres and ample on the generic fibre. Then $X$ satisfies the Stokes bound at every $B \ge 4f + 2$ for which $\operatorname{ar}_X(B)$ exists.

Lean: `GlobalTheory.CompanionTheory.Relay.intersection_final_estimate` (also `GlobalTheory.T.intersection_final_estimate`, a second name)

*Proof.* Resolution gives the integrability of point integrals, and the degree input gives that generic and geometric degrees agree. The vertical factors are positive and smooth, and so is $\mu_{B, t}$. A telescoping Stokes formula writes the difference between the self intersections of $M_{p', q', t'}$ and of $\mu_{B, t}$ as a sum of point integrals. The mixed top intersections are polynomials in the parameters, and semipositivity makes the integrands monotone. Pass to the limit in $t'$, then in an auxiliary $\varepsilon$, then in $t$. The integral of $U/2$ against $c_1(\mu)^n$ is $\operatorname{mean}_U \deg_\mu / 2$. $\square$

A good tower $T$ has, for each level $B$ and component $c$, a model $T.M_{B, c}$, an intersection number $\mathrm{PP}_{B, c}(F)$ for each polynomial class $F$, and a volume $\operatorname{vol}(c)$. Let $d$ be the dimension of the moduli space for the integer $j$ of $T$. The test polynomial is $F_j = \mu_{\mathrm{sm}}^{\,d + 1} \phi_j$, where $\mu_{\mathrm{sm}}$ is the small Hodge class and $\phi_j$ the fibre class, and the flag degree $\deg_j$ of $\mu_{\mathrm{sm}}^{\,d} \phi_j$ is positive. We do not unfold these. The tower is proportional if each volume is positive, the geometric degree of every class $F$ on $T.M_{B, c}$ is $\operatorname{vol}(c)$ times the flag degree of $F$, and these geometric degrees do not depend on $B$.

**Theorem 8.7.4 (Intersection relay).** Assume the positivity of agreement, the proportionality input, the comparison input, the top level inputs and the integrability of point integrals. Let $E$ be abelian Galois over $\mathbb{Q}$, let $T$ be a root tower of type $(\Phi, p + q)$ with a good origin $o$ with the extra conditions, let $\mathrm{II}$ be full, and let $1 \le q \le p$, $2 \le B \le B_1$ and $c$ a component. Let $X$ be a component setting on $D_c$ with an origin for the bad primes of $T$. Assume the labels lie on the first side and the cusp weight on the second, the component is free at the primes of $S_0$ and $D_c$, its generic point is that of the reference origin of $o$ at $c$, and the primes of $D_c$ are the primes $\ell \le B_1$ that are not bad. Then there are an arithmetic variety $P$ of dimension $n + 1 + e$ with a block map onto the coordinates of $D_c$, a number $\delta > 0$, coefficients $c_m$ and smooth lines $M_t$ and $N_t(m)$ with these properties.

1. For small $t > 0$, $M_t$ is the pullback of $\mu_{B, t}$, and the weights of $N_t(m)$ do not depend on $t$.
2. As $t \to 0^+$, $\sum_m c_m\, \mathrm{II}\big(M_t^{\,n+1} N_t(m)\big) \to \delta\, \mathrm{PP}_{B, c}(F_j)$.
3. For small $t > 0$, $\sum_m c_m \int_P \log h_{M_t}^{\,n}\, N_1(m)$ is $\delta$ times the geometric degree of $\mu_{\mathrm{sm}}^{\,d} \phi_j$ on $T.M_{B, c}$.

Lean: `GlobalTheory.CompanionTheory.Relay.good_origin_intersection_relay` (also `GlobalTheory.T.good_origin_intersection_relay`, a second name)

*Proof.* The primes of $o$ at the level $B$ are the bad primes and the vertical primes $S_B$ of $D_c$. The Hodge Tate lattices of a free component do not depend on the level, and the Hodge line is compatible with the root model. So $T.M_{B, c}$ and the coordinates of $D_c$ have a common model with two block maps. An analytic core on the common model replaces the singular Hodge metric by the regularisations of $X$, whose weights converge uniformly on compact sets. The base side of the common model gives $P$, the lines, the coefficients and $\delta$. $\square$

**Theorem 8.7.5 (Test polynomial and slope).** Under the hypotheses of the intersection relay, $\deg_\mu > 0$, the limit $\operatorname{ar}_X(B)$ exists, and

$$
\mathrm{PP}_{B, c}(F_j) = \operatorname{sl}_X(B)\, (d + 1) \operatorname{vol}(c) \deg_j .
$$

Lean: `GlobalTheory.CompanionTheory.Ar.Cusp.testPoly_eq_slX` (also `GlobalTheory.T.good_origin_intersection_tower`, a second name)

*Proof.* The agreement with the real tower and the proportionality input make $T$ proportional. The comparison of heights between models gives that $\operatorname{ar}_X(B)$ exists, with value $\Lambda$, and the geometric degrees of $\mu_{B, t}$ tend to $\deg_\mu$. Take the data of the relay. Let $\phi = \sum_m c_m \phi_m$, where $\phi_m$ is the fibre number of the weights of $N_1(m)$; it does not depend on $t$. For small $t$ the projection formula for the block map gives $\sum_m c_m\, \mathrm{II}(M_t^{\,n+1} N_t(m)) = \phi\, \mathrm{II}(\mu_{B, t}^{\,n+1})$, and the same formula for point integrals turns property 3 into $\phi$ times the geometric degree of $\mu_{B, t}$. Uniqueness of limits and proportionality give

$$
\begin{aligned}
\delta\, \mathrm{PP}_{B, c}(F_j) &= \phi\, \Lambda, \\
\delta \operatorname{vol}(c) \deg_j &= \phi \deg_\mu .
\end{aligned}
$$

The left side of the second line is positive, and $\deg_\mu \ge 0$, so $\deg_\mu > 0$. The labels lie on the first side, so $j = p$ and $n = d$. Divide the first line by $\delta$ and substitute $\phi$ from the second. $\square$

**Definition 8.7.6 (Strict base degree setting).** Let $T$ be a root tower of type $(\Phi, N)$ and let $C_h$, $C_u$, $\mathrm{rd}$ and $L$ be real numbers. The tower has a strict base degree setting at $(B, c)$ if there are component data $D_c$ with $N$ and the integer $j$ of $T$, and a component setting $X$ on $D_c$ with the numbers $\mathrm{rd}$ and $L$, with these properties. Write $\Lambda_{B'} = \log(B' \mathrm{rd}) + |L|$.

1. For $B' \ge 4f + 2$, $1 \le p' \le q'$ and small $t'$, the twisted lines are semipositive, nef on the fibres, ample on the generic fibre and invariant under conjugation.
2. For $B' \ge 4 f N^2$, $1 \le p' \le q'$ and small $t'$, every point $W$, on or off the boundary, has height at least $-C_h f j' \Lambda_{B'} - (p'/q') K_A$ for the twisted line at $(B', p', q', t')$.
3. If $1 \le j'$ and $3 j' + 1 \le N$, then $\operatorname{mean}_U \le C_u f j' \Lambda_{B'}$ for every $B' \ge 4 f N^2$.
4. $\deg_\mu > 0$, $\operatorname{ar}_X(B)$ exists, and $X$ satisfies the Stokes bound at $B$.
5. $\mathrm{PP}_{B, c}(F_j) = \operatorname{sl}_X(B)\, (d + 1) \operatorname{vol}(c) \deg_j$.

Lean: `GlobalTheory.CompanionTheory.Ar.Top.RootTower.HasBaseDegreeSettingStrict`

Let $\mathrm{rd}_E = |d_E|^{1/[E : \mathbb{Q}]}$, and let $L_H = \operatorname{Re} L'(1, \chi) / L(1, \chi)$ for the quadratic character $\chi$ of the host.

**Theorem 8.7.7 (Base setting of a good tower).** Let $C_h$ and $C_u$ be geometric height constants. Assume the Weil pairing statement, the positivity of agreement, the proportionality input, the comparison input, the top level inputs and the integrability of point integrals. Let $E$ be abelian Galois over $\mathbb{Q}$, let $Y$ be global, let $T$ be a root tower of type $(\Phi, p + q)$ with a good origin $o$ with the extra conditions, and let $\mathrm{II}$ be full. Assume $1 \le q \le p$ and that $T$ has at most $4 f (p + q)^2$ bad primes. Then for every $B \ge 4 f (p + q)^2$ and every component $c$, the tower has a strict base degree setting at $(B, c)$ with $C_h$, $C_u$, $\mathrm{rd}_E$ and $L_H$.

Lean: `GlobalTheory.CompanionTheory.Ar.Cusp.TopBase.base_setting_of_good_origin` (also `GlobalTheory.T.base_setting_of_good_tower`, a second name)

*Proof.* Since $f \ge 1$ and $N \ge 2$, we have $B \ge 16 f \ge 4f + 2$. The origin of $o$ at $(B, c)$ and the reference origin at $c$ factor through the same point, so they have the same generic point. Let $S_1$ be the set of primes $\ell \le B$ that are not bad. The bad primes divide $2\, d_E\, M_l$ and contain the primes of the discriminant. The theorem on component data with $S_0$ the bad primes, $S_1$ and the first side gives $D_c$, Hodge data and an origin with $j = p$, the labels on the first side, the cusp weight on the second side and freeness at $S_0 \cup S_1$. This origin is admitted at $B$, since $j' = q \le p = j$.

The theorem on tied regularisations gives a cusp weight $U \ge 0$, invariant under the torus, with tied settings $S$, $S'$ and the conjugation property. The height constants give positivity, the height bound and the mean bound for $S'$. The regularisation of the corrected weight turns these into $X$ with Hodge data $\mathcal{H}$, cusp weight $U$ on $X_o$, the numbers $\mathrm{rd}_E$ and $L_H$, and properties 1 to 3. The theorem on the test polynomial with $B_1 = B$ gives property 5 and the first two parts of property 4. The Stokes bound for the cusp setting gives the last part. $\square$

**Remark 8.7.8 (Formalization).** The name `T.full_intersection_generic_bound` describes no bound: `exists_componentData_origin` is an existence statement. Its conclusion `Or.𝔐.OmVB` is discarded in `base_setting_of_good_origin`. The Stokes bound is an alias of `ModelDimension.abelian_cm_stokes_identity`, whose proof `stokes_of_statements` (AbelianCmStokesIdentity.lean:87) introduces `Prov.An`, `Flat.GagaSections`, `SemiAbelianHomExtension`, the `IsAbelianGalois` instance, `admitted`, `IsCuspWeight`, `X.H = Hd` and the equality of cusp weights, and never uses them. The relay is an alias of `LevelTowerAlt.good_origin_tower_height`, whose proof `tie_of` (PullCst.lean:69) introduces `PB.Proportional`, `Cmp.CmpSt`, `PtsIntegrableStatement`, `Top.IsGlobal` and $2 \le B$ as `_` and never uses them. The corrected weight of `ComponentSetting` is `cuspCorr` (CpRegPhRegOfNonneg.lean:71), equal to $\varphi_\mu + U/2$. A second definition `cuspCorrected` (Weights.lean:145) is $\varphi_\mu + U$, and the lines `MU`, `topMU`, `geomDegMU` and `htMU` of that file use it; this section uses `MUc`.
