---
title: Regularization of singular weights and uniform integrability
decls:
  - GlobalTheory.T.global_regularization_statement_holds
  - GlobalTheory.CompanionTheory.Ar.Giv.regGlobalStatement_holds
  - GlobalTheory.T.uniform_integrability_statement_holds
  - GlobalTheory.CompanionTheory.Ar.Giv.unifInt_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Regularization of singular weights and uniform integrability

Section 7 used two inputs on singular weights. The regularization statement gives every singular weight with a gradient bound a regularized family that converges in $C^2$. The uniform integrability statement lets us pass to the limit in integrals of a Green function $-\log\lVert v\rVert$ against the Monge-Ampère measures of the regularized weights. This section proves both. The first proof regularizes in each chart and glues the local regularizations. The second proof cuts the Green function into a bounded continuous part and a part with small integrals.

### Setting

We keep the setting of Section 7. So $X$ is a compact complex manifold of dimension $e$ with a finite holomorphic atlas $A$, $\Theta$ is a smooth positive potential, $L$ is a potential with a section $s$ that has simple normal crossings with multiplicities $m_i$ along components $W_i$, and $\lVert s\rVert \leq 1$. Let $\partial = \{s = 0\}$ and $r_W = \exp(1) - 2\log\lVert s\rVert$. Then $r_W \geq \exp(1)$, so $\log r_W \geq 1$. Singular weights, gradient bounds, regularized families and $C^2$ convergence are as in Section 7, and $\varepsilon_C(t) = C \log\log(1/t)/\log(1/t)$.

For a finite set $S$ of coordinates, multiplicities $m_i \geq 1$ and $z \in \mathbb{C}^e$ put
$$
r_{\mathrm{loc}}(z) = \exp(1) + \sum_{i \in S} m_i \log \frac{4}{\lvert z_i\rvert^2}.
$$

**Definition 10.12.1.** A second atlas $B$ is adapted to $(L, s)$ if it is compatible with $A$, every chart of $B$ contains the closed ball of radius $2$ in its target, the balls of radius $1$ cover $X$, and there is a constant $M$ with this property: for each chart there are a set $S$ of coordinates and multiplicities $m_i \geq 1$ such that $\partial$ is the union of the coordinate hyperplanes $\{z_i = 0\}$ for $i \in S$ in that chart, and $\lvert r_W - r_{\mathrm{loc}}\rvert \leq M$ on the closed ball of radius $2$ off $\partial$.

So in an adapted chart the boundary is a union of coordinate hyperplanes and $r_W$ is the local log distance up to a bounded error.

### The regularization theorem

**Theorem 10.12.2 (Global regularization).** Let $B$ be an adapted atlas. Let $\theta$ be a potential, and let $\varphi$ be a singular weight for $\theta$ with constant $C_5$ that has a gradient bound with constant $C_5$ for $B$. Then there are constants $C$ and $t_0$ and a regularized family $\varphi_t$ for $\varphi$ with constants $C$ and $t_0$ that converges in $C^2$.

Lean: `GlobalTheory.CompanionTheory.Ar.Giv.regGlobalStatement_holds` (also `GlobalTheory.T.global_regularization_statement_holds`, a second name).

*Proof.* Step 1: refine the atlas. A refinement lemma gives an adapted atlas $B'$ with a gradient bound for $\varphi$ and, for each chart $j$, a point $x_j$ whose local potential $q_j$ of $\theta$ is defined on the whole ball of radius $2$ of the chart. Let $S_j$, $m_j$ and $M$ be the data of $B'$.

Step 2: move the bounds to the charts. In chart $j$, off the coordinate hyperplanes, the function $q_j + \varphi$ is smooth and its Levi form is nonnegative. A lemma on the transfer of log bounds gives one constant $C'_5$ such that, whenever $\lvert r_W - r_{\mathrm{loc}}\rvert \leq M$ and both are at least $\exp(1)$, the bound $-C_5 \log r_W \leq \varphi \leq C_5$ gives $-C'_5 \log r_{\mathrm{loc}} \leq \varphi \leq C'_5$, and the gradient bound in $r_W$ gives the gradient bound in $r_{\mathrm{loc}}$ with constant $C'_5$.

Step 3: regularize in one chart. Let $\psi = q_j + \varphi$ in the chart. For $0 < t$ let $M_t(z)$ be the supremum of $\psi$ over the closed ball of radius $t$ around $z$, with the coordinate hyperplanes removed. The local regularization lemma gives $C_j \geq 1$, $0 < t_j \leq \exp(-\exp(1))$ and smooth functions $g_{j,t}$ on the ball of radius $5/4$ for $0 < t \leq t_j$ such that:

1. $q_j + g_{j,t}$ has a nonnegative Levi form;
2. $-C_j \log\log(1/t) \leq g_{j,t} \leq C_j$;
3. off the hyperplanes $\varphi \leq g_{j,t}$, and $g_{j,t} \leq \varphi + t^{1/3}$ where $r_{\mathrm{loc}} \leq \log(1/t) + M$;
4. $M_t - \varepsilon_{C_j}(t) \leq q_j + g_{j,t} \leq M_t$;
5. $g_{j,t} \leq g_{j,t'} + \varepsilon_{C_j}(t')$ for $t \leq t' \leq t_j$;
6. $g_{j,t}$ converges to $\varphi$ in $C^2$ on compact sets off the hyperplanes.

The construction is a regularized maximum: one first takes the local supremum $M_t$, which is plurisubharmonic, and then smooths it by convolution at a smaller scale. The gradient bound controls how far $M_t$ is from $\psi$ near the hyperplanes.

Step 4: compare the charts. On the overlap of two chart balls of radius $5/4$, the two local suprema minus their local potentials differ by at most $C' \varepsilon(t)$ for some constant $C'$ and all small $t$. This holds since $\theta$ changes by a pluriharmonic function between charts and the radius $t$ is small compared with the overlap. Put $C_m = 1 + \sum_j \lvert C_j\rvert$ and $C_l = \lvert C'\rvert + C_m$. With the sandwich of Step 3, the local regularizations $g_{j,t}$ differ on overlaps by at most $\varepsilon_{C_l}(t)$.

Step 5: choose the scale. An epsilon schedule lemma says that $\varepsilon_{C_l}(t) \to 0$, that it is monotone and small for small $t$, and that a common $t_m$ below all $t_j$ exists. Let $t_0$ be the minimum of $t_m$, the scale of Step 4, a scale where $\varepsilon_{C_l}(t) \leq 1$, and $\exp(-\exp(1))$. For $t \leq t_0$ we have $\log\log(1/t) \geq 0$.

Step 6: glue. The gluing lemma takes local functions $f_{j,t}$ on the chart balls that are smooth, bounded, plurisubharmonic with $\theta$, and differ on overlaps by at most $\delta(t)$ with $t \leq \delta(t) \leq 1$ and $\delta(t) \to 0$. It returns a constant $K$ and smooth functions $F_t$ with
$$
f_{j,t} \leq F_t \leq f_{j,t} + K \delta(t)
$$
on each chart ball such that $\theta + F_t + K\delta(t)\Theta$ is plurisubharmonic. It also passes $C^2$ convergence on compact sets from the local functions to $F_t$. We apply it with $f_{j,t} = g_{j,t}$ and $\delta = \varepsilon_{C_l}$. The local bound of Step 3 gives the bound $C_l + C_l \log\log(1/t)$ for $\lvert g_{j,t}\rvert$. The $C^2$ convergence of the $g_{j,t}$ moves through the charts.

Step 7: the bounds. A final lemma collects the properties of the glued family. The sandwich in Step 6 and the bounds of Step 3 give the upper bound by $C$, the lower bound by $-C\log\log(1/t)$ and the inequality $\varphi \leq F_t$. The positivity holds with $\varepsilon_C(t)\Theta$ once $C \geq K C_l$. The estimates of $F_t - \varphi$ come from item 3 of Step 3 where $r_W \leq \log(1/t)$, and from $\log r_W \geq 1$ elsewhere. The monotonicity comes from item 5. Put $\varphi_t = F_t$. $\square$

### Uniform integrability

Let $\varphi_1, \dots, \varphi_e$ be singular weights for potentials $\theta_1, \dots, \theta_e$ with constant $C_5$, with regularized families $\varphi_{i,t}$ with constants $C$ and $t_0$ that converge in $C^2$. Let $\mu$ be the mixed Monge-Ampère measure of the potentials $\theta_i + \varphi_i + \Theta$, and $\mu_t$ that of $\theta_i + \varphi_{i,t} + \Theta$.

**Theorem 10.12.3 (Uniform integrability).** Let $L'$ be a potential with a section $v$ such that $\lVert v\rVert \leq 1$, $v$ has simple normal crossings along one divisor $D$ with multiplicity $1$, and the product $s v$ has simple normal crossings along the components of $s$ and $D$. Put $G = -\log\lVert v\rVert$. Then $G$ is integrable for $\mu$, it is integrable for $\mu_t$ for all small $t > 0$, and
$$
\int_X G \, d\mu_t \longrightarrow \int_X G \, d\mu \qquad (t \to 0^+).
$$

Lean: `GlobalTheory.CompanionTheory.Ar.Giv.unifInt_holds` (also `GlobalTheory.T.uniform_integrability_statement_holds`, a second name).

*Proof.* Step 1: weak convergence. The convergence statement, applied with bounded continuous functions $g$ and $g_t = g$, gives that $\mu$ and all $\mu_t$ are finite and that $\int g \, d\mu_t \to \int g \, d\mu$. Here $\lvert g\rvert \leq B \leq B \log r_W$, since $\log r_W \geq 1$.

Step 2: the zero set has measure zero. The zero set of $v$ is a closed analytic subset with empty interior. A mixed Monge-Ampère measure of locally bounded potentials gives no mass to such a set. So $\mu(\{v = 0\}) = 0$ and $\mu_t(\{v = 0\}) = 0$. Also $N = \lVert v\rVert$ is continuous with $0 \leq N \leq 1$.

Step 3: the case $e = 0$. Then $X$ is a compact manifold of dimension $0$, hence finite, and every function on it is integrable for every finite measure. The family $\varphi_{i,t}$ is empty, so $\mu_t = \mu$ and the limit is trivial.

Step 4: small Green integrals. For $\varepsilon > 0$ put $G_\varepsilon = \log(1 + \varepsilon/N^2)$. The convergence theorem for mixed measures along a normal crossing divisor, with the input on uniform integrability from the heights chapter and the tail bound for regularized families, gives this. For each $\eta > 0$ there are $\varepsilon_0 > 0$ and $t_1 > 0$ such that, for $0 < \varepsilon \leq \varepsilon_0$ and $0 < t \leq t_1$, the function $G_\varepsilon$ is integrable for $\mu_t$ and $\int G_\varepsilon \, d\mu_t \leq \eta$.

Step 5: cut the Green function. Off $\{N = 0\}$,
$$
G = -\log N = \tfrac12 G_\varepsilon - \tfrac12 \log(N^2 + \varepsilon).
$$
The second term is continuous, with $\log\varepsilon \leq \log(N^2 + \varepsilon) \leq \log(1 + \varepsilon)$. So by Step 1 its integrals converge. The first term is nonnegative and has integral at most $\eta/2$ for $\mu_t$, uniformly in $t \leq t_1$. For $\mu$, the bounded continuous truncations $\min(G_\varepsilon, k)$ have integrals at most $\eta$ by Step 1, and monotone convergence in $k$ gives $\int G_\varepsilon \, d\mu \leq \eta$, since $\{N = 0\}$ is null. So $G$ is integrable for $\mu$ and for $\mu_t$. Finally
$$
\limsup_{t \to 0^+} \Bigl\lvert \int G \, d\mu_t - \int G \, d\mu \Bigr\rvert \leq \eta,
$$
and $\eta > 0$ is arbitrary. $\square$

Step 5 is the standard argument for weak convergence of measures with an unbounded integrand: weak convergence plus uniformly small tails gives convergence of the integrals. The small tails come from the normal crossings of $s v$, which make $G_\varepsilon$ small in the mixed measures uniformly in the regularization.

**Remark 10.12.4 (Formalization).** The statements are `RegGlobalStatement` and `UnifIntStatement` in `ReciprocityTheory/AnalyticForms/LeviForms/IsRegFamilyInhabitStatement.lean` (lines 116 and 166). The same file defines $\partial$ as `bdry` (line 12), $r_W$ as `rW` (line 14), $\varepsilon_C$ as `epsT` (line 69), $r_{\mathrm{loc}}$ as `rLoc` (line 71), the adapted atlas (line 74), the regularized family (line 83), $C^2$ convergence (line 95), singular weights (line 105), gradient bounds (line 110) and the convergence statement (line 147). The regularization proof is at `Development/AutomorphicSpectrum/Proofs/MetricProofs/GlobalRegularizationStatementHolds.lean:21`. It calls the local lemma through `GlobalTheory.T.local_levi_psh_regularization`, a relay for `regularise_one_chart` (`LocalLeviPshRegularizationStatement.lean:10`), and the local supremum $M_t$ is `polyMaxOff` (`ReciprocityTheory/AnalyticForms/LeviForms/RegChart.lean:12`). The uniform integrability proof is at `UniformIntegrabilityStatementHolds.lean:44`; the null boundary lemma `maMeasure_bdry_null_any` is local to that file (line 15). Step 5 is the relay `weak_convergence_off_zero_set` (`WeakConvergenceOffZeroSetStatement.lean:8`) for `tendsto_integral_neg_log_of_green_small`. The second names are at `GlobalRegularizationStatementHoldsStatement.lean:10` and `UniformIntegrabilityStatementHoldsStatement.lean:8`. The hypothesis $\lVert v\rVert \leq 1$ and the normal crossings of $s v$ are explicit hypotheses; the multiplicity $1$ for $D$ is fixed in the statement.
