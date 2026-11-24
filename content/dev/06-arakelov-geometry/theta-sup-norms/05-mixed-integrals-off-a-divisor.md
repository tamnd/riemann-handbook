---
title: Mixed integrals of singular potentials off a divisor
decls:
  - GlobalTheory.CompanionTheory.Ar.Giv.tailLogProducts
  - GlobalTheory.T.mixed_energy_uniform_bound
  - GlobalTheory.CompanionTheory.Ar.Giv.Conv.position_tail
  - GlobalTheory.CompanionTheory.Ar.Giv.mixed_integral_tendsto_of_C2_off_divisor
  - GlobalTheory.T.mixed_integral_tendsto_off_divisor
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Mixed integrals of singular potentials off a divisor

This section proves that mixed Monge-Ampère integrals are continuous under a regularization of the potentials. The potentials have logarithmic singularities along a divisor, and the regularized potentials converge to them in $C^2$ only on compact sets off the divisor. The key estimate is a uniform bound for the mass of $\log r$ near the divisor, where $r$ is a function that grows like $\log(1/\lvert y\rvert^2)$ at the divisor. The result is used in [the volume theorem from its inputs](/entry/volume-theorem-x-of-inputs/), where an arithmetic volume is computed as a limit of integrals for smooth metrics. For the forms we use [Chern-Weil forms](/learn/positivity-resolution/#chern-weil-forms) and [metrics, curvature and positivity](/learn/positivity-resolution/#metrics-curvature-and-positivity).

### Potentials and mixed integrals

Let $X$ be a compact Hausdorff complex manifold of dimension $e$ with a finite holomorphic atlas. A local potential $\Theta$ on $X$ is a family of real functions $\Theta_x$ on open neighbourhoods of the points $x$. It is a potential if every $\Theta_x$ is smooth and any two of them differ, near every common point, by the real part of a holomorphic function. So $\Theta$ defines a closed real $(1,1)$ form $dd^c \Theta$, as the curvature of a smooth hermitian metric does. The potential is plurisubharmonic if its Levi form is positive semidefinite in every chart, and positive if its Levi form is positive definite. For a function $f$ on $X$ we write $\Theta + f$ for the local potential $\Theta_x + f$.

For local potentials $\Phi_1, \dots, \Phi_e$ and a function $g$, the mixed integral is
$$
\operatorname{mInt}(\Phi; g) = \int_X g\; dd^c \Phi_1 \wedge \cdots \wedge dd^c \Phi_e ,
$$
computed in charts with a fixed partition of unity and the local density of the wedge product (the mixed discriminant of the complex Hessians). The pair $(\Phi, g)$ is integrable if $g$ times the local density is integrable on every compact subset of every chart.

A regular chart datum on $X$ consists of an open set $Y^\circ$ and a function $r \geq 1$ on $Y^\circ$ with the following shape. In each chart $j$ there is a set $S_j$ of coordinates such that $Y^\circ$ is the complement of the coordinate hyperplanes $y_i = 0$, $i \in S_j$, and
$$
r = \exp(1) + f_j + \sum_{i \in S_j} \log \frac{1}{\lvert y_i\rvert^2}
$$
for a bounded smooth function $f_j$. So $X \setminus Y^\circ$ is a divisor with normal crossings and $\log r$ is of size $\log \log (1/\mathrm{dist})$ near it.

**Definition 10.5.1.** Let $R_0 \geq \exp(1)$ and let $T_{R_0} = \{\, x \in Y^\circ : r(x) \geq R_0 \,\}$. A family $\Phi$ of $e$ local potentials has a tail log bound with constant $C_E$ if, for every $R_0 \geq \exp(1)$, the function $\log r$ on $T_{R_0}$ (extended by zero) is integrable for $\Phi$ and
$$
\operatorname{mInt}\bigl(\Phi; \mathbf{1}_{T_{R_0}} \log r\bigr) \leq C_E\, \frac{(\log R_0)^{e+1}}{R_0} .
$$

### The uniform tail bound

**Theorem 10.5.2 (Uniform tail bound).** Let $\Theta$ be a positive potential, let $P_1, \dots, P_e$ be potentials, and let $C$ be real. There is $C_E$ with this property. If $f_1, \dots, f_e$ are smooth functions on $X$ such that $P_i + f_i$ is plurisubharmonic and
$$
\lvert f_i\rvert \leq C + C \log r, \qquad f_i \leq C
$$
on $Y^\circ$ for every $i$, then $(P_i + f_i)_i$ has a tail log bound with constant $C_E$.

Lean: `GlobalTheory.CompanionTheory.Ar.Giv.tailLogProducts` (also `GlobalTheory.T.mixed_energy_uniform_bound`, a second name).

*Proof.* The statement follows from a tail mass bound for smooth families, which is proved from a lemma on the tail mass of products. We shift $r$ to $r' = r + \exp(1) - 1$, which is again the function of a regular chart datum, with $r' \geq \exp(1)$ on $Y^\circ$. Put $\vartheta_i = P_i + C$. A bounding Kähler form gives a smooth Kähler form $\omega$ that bounds all $dd^c \vartheta_i$. Put $u_i = f_i - C$. Then $u_i \leq 0$ and
$$
u_i \geq -3 \lvert C\rvert \log(r + \exp(1) - 1)
$$
on $Y^\circ$. So $P_i + f_i = \vartheta_i + u_i$ is a bounded perturbation of a smooth potential by a function with logarithmic growth in $r'$, and the tail mass bound for smooth families gives the tail log bound for $\vartheta + u$. It is the bound for $(P_i + f_i)_i$, since the two families are equal. The constant does not depend on $f$, because only $C$, $\Theta$ and the $P_i$ enter the bounds. $\square$

### Tails of partial families

The convergence theorem expands the mixed integral of $(P_i + f_i)_i$ by inclusion and exclusion over subsets $T$ of the indices. For each $T$ it needs the tail bound for the family in which the indices outside $T$ are replaced by $\Theta$ alone.

**Lemma 10.5.3 (Tails of partial families).** Let $\Theta$ be a positive potential, let $P_1, \dots, P_e$ be potentials, let $C$ be real and let $T \subseteq \{1, \dots, e\}$. For $i \in \{1, \dots, e\}$ and functions $u_i$ put
$$
\Phi^T_i = \begin{cases} P_i + u_i + \Theta, & i \in T, \\ \Theta, & i \notin T. \end{cases}
$$
There is $C_E$ such that for all smooth $u_1, \dots, u_e$ with $P_i + u_i + \Theta$ plurisubharmonic, $\lvert u_i\rvert \leq C + C \log r$ and $u_i \leq C$ on $Y^\circ$, every $\Phi^T_i$ is plurisubharmonic and $\Phi^T$ has a tail log bound with constant $C_E$.

Lean: `GlobalTheory.CompanionTheory.Ar.Giv.Conv.position_tail`

*Proof.* For $i \in T$ the potential $\Phi^T_i$ is plurisubharmonic by hypothesis. For $i \notin T$ it is $\Theta$, which is positive and so plurisubharmonic. Apply the theorem on the uniform tail bound to the potentials $P_i + \Theta$ for $i \in T$ and $\Theta$ for $i \notin T$, with the functions $u_i$ for $i \in T$ and $0$ for $i \notin T$, and with the constant $\lvert C\rvert$. Its constant does not depend on $u$. $\square$

### Convergence

**Theorem 10.5.4 (Convergence of mixed integrals off a divisor).** Let $(Y^\circ, r)$ be a regular chart datum on $X$, let $\Theta$ be a positive potential and let $C$ be real. Let $P_1, \dots, P_e$ be potentials, let $f_1, \dots, f_e$ be smooth on $Y^\circ$, and let $G$ be a function on $X$. For small $t > 0$ let $f_{i,t}$ be smooth functions on $X$ and $G_t$ functions on $X$. Assume:

1. for small $t > 0$ and every $i$, the potential $P_i + f_{i,t} + \Theta$ is plurisubharmonic, $\lvert f_{i,t}\rvert \leq C + C \log r$ and $f_{i,t} \leq C$ on $Y^\circ$;
2. in every chart, $f_{i,t} \to f_i$ as $t \to 0^+$ uniformly on compact subsets of $Y^\circ$, together with the first and second derivatives;
3. for small $t > 0$, $G_t$ is measurable on $Y^\circ$ and $\lvert G_t\rvert \leq C + C \log r$ on $Y^\circ$;
4. $G_t \to G$ uniformly on compact subsets of $Y^\circ$.

Then $(P + f, G)$ is integrable, $(P + f_t, G_t)$ is integrable for small $t$, and
$$
\lim_{t \to 0^+} \operatorname{mInt}(P + f_t; G_t) = \operatorname{mInt}(P + f; G) .
$$

Lean: `GlobalTheory.CompanionTheory.Ar.Giv.mixed_integral_tendsto_of_C2_off_divisor` (also `GlobalTheory.T.mixed_integral_tendsto_off_divisor`, a second name).

*Proof.* The set $Y^\circ$ is open, and its complement has measure zero in every chart.

Step 1: inclusion and exclusion. The local density of the wedge product is multilinear in the complex Hessians. So in every chart, for every measurable set $K$ inside the chart and every weight $w$,
$$
\begin{aligned}
\int_K w\, \operatorname{dens}(P + f) = \sum_{T} (-1)^{e - \lvert T\rvert} \int_K w\, \operatorname{dens}(\Phi^T),
\end{aligned}
$$
where $\Phi^T$ is the family of the lemma with $u = f$, and the left side is integrable when all terms on the right are. The same identity holds for $f_t$ in place of $f$. Each $\Phi^T_i$ is a sum of $\Theta$ and possibly $P_i + f_i$, so the wedge product of $\Phi^T$ is a wedge of positive and plurisubharmonic forms.

Step 2: the tails. By the lemma on partial families with $u = f_t$, every family $\Phi^T$ for $f_t$ has a tail log bound with one constant $C_E$, for all small $t$. On the tail $T_{R_0}$ the weights $G_t$ are bounded by $C + C\log r$, so the mass of $G_t$ on $T_{R_0}$ for $\Phi^T$ is at most of order $(\log R_0)^{e+1}/R_0$, uniformly in $t$. This tends to $0$ as $R_0 \to \infty$.

Step 3: the compact part. On $\{\, r \leq R_0 \,\}$, which is compact in $Y^\circ$, the potentials converge in $C^2$ and the weights converge uniformly, by conditions 2 and 4. So the local densities converge uniformly there, and the integrals over this part converge. The integrability of $(P + f, G)$ follows from the tail bound for the limit, which is obtained from the bounds of Step 2.

Step 4: the sum. For each $T$, Steps 2 and 3 give the convergence of the integral of $G_t$ against the density of $\Phi^T$ for $f_t$ to the integral of $G$ against the density of $\Phi^T$ for $f$. Summing over $T$ with the signs of Step 1, and then over the charts of the partition of unity, gives the convergence of the mixed integrals. $\square$

The function $\Theta$ is added because $P_i + f_{i,t}$ need not be plurisubharmonic. Only $P_i + f_{i,t} + \Theta$ is, and the inclusion and exclusion removes $\Theta$ again.

**Remark 10.5.5 (Formalization).** The plurisubharmonic predicate in this section is the one for local potentials on an atlas: the Levi form is positive semidefinite at every point of every chart (`ReciprocityTheory/AnalyticForms/PotentialTheory/IsPotentialOfFun.lean:101`). It differs from the predicate of Section 4. The mixed integral is defined with a partition of unity chosen by the axiom of choice, and it is $0$ when no partition exists (`IsPotentialOfFun.lean:127`). The tail sets and the tail log bound are in `GroundTheory/HeightsAndTheta/Heights/AnalyticLimit/Objects.lean` (lines 62 and 73), and regular chart data in `GroundTheory/HeightsAndTheta/Heights/Regularisation/Statements.lean:92`. Both second names only restate their theorems. The uniform tail bound is proved in `Development/AutomorphicSpectrum/Proofs/MetricProofs/MixedEnergyUniformBound.lean` (line 32) from the statement `ListTailLogSmooth.Statement`, the shift `regChartShift`, the bounding Kähler form `BoundingKaehler.full`, and the comparison lemmas `tailLogBound_of_φ_eq` and `tailLogBound_of_le`; I did not unfold the tail mass bound for smooth families. The lemma on partial families (line 53) and the convergence theorem (line 213) are in `MixedIntegralTendstoOffDivisor.lean`. Step 1 is the local lemma `expand_on` (line 114) with `GlobalTheory.T.local_density_inclusion_exclusion`, and Steps 2 and 3 for one $T$ are `GlobalTheory.T.mixed_integral_regularized_convergence`, which I did not unfold; my description of Steps 2 and 3 follows its hypotheses. The integrability of the limit is the local lemma `mIntegrable_of_logBound` (line 146).
