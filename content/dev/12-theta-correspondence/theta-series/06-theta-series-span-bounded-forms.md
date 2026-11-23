---
title: Theta series span the bounded forms
decls:
  - GlobalTheory.SW.SpanMain.theta_span
  - GlobalTheory.T.hermitianTheta_series_span_bounded_forms
  - GlobalTheory.SW.level_theta_span
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Theta series span the bounded forms

This section proves the main result of the chapter. Let a theta system $(\Delta, \mathcal{L}, \Phi, \mu)$ be given, as in [the previous section](/entry/kernel-identity/). Then each bounded holomorphic automorphic form for $\Delta$ of a fixed weight is a finite linear combination of derivatives of theta series $\Theta_{\Phi_{L,\Lambda}}$ at highest weight harmonic polynomials. The proof uses the [kernel identity](/entry/kernel-identity/), a reproducing property of the kernel $K_P$ on a thin slab of frames, and a Neumann series that inverts the matrix of inner products $\langle \Phi_{L,\Lambda}, \Phi_{L',\Lambda} \rangle$. A second theorem applies this to the theta systems that come from a level datum. These results are the [[theta function|2F5CYQJVAF]] side of the method of [theta kernels](/learn/theta/#theta-kernels).

### Bounded automorphic forms

We keep the notation of the earlier sections: a unitary period datum of rank $r$ with a symplectic basis, the period domain $\mathcal{D}$, the Gram matrices $g_\tau(x)$, the signs $\epsilon(a)$ and $\epsilon_i$, the theta derivatives $\Theta^P_\varphi(x)$, the class sum $\sum_M$ over $V_n(M)$, and the kernel $K_P(x_1, x_2)$.

**Definition 3.6.1 (Weights and the Borel set).** A *weight* is a family $\lambda = (\lambda_{\tau, i})$ of integers indexed by $\tau \in \Psi$ and $1 \le i \le r$. The *Borel set* $B$ is the set of frames $b$ with each $b_\tau$ upper triangular and invertible. Frames act on frames on the right by $(x b)_\tau = x_\tau b_\tau$, and the *character* of $\lambda$ is
$$\chi_\lambda(b) = \prod_{\tau \in \Psi} \prod_{i=1}^r (b_\tau)_{ii}^{\lambda_{\tau, i}}.$$
For a function $F$ on frames, put
$$\|F\|_\lambda(x) = |F(x)| \prod_{\tau \in \Psi} \prod_{i=1}^{r} \Big| \frac{d_{\tau, i}(x)}{d_{\tau, i-1}(x)} \Big|^{-\lambda_{\tau, i}/2},$$
where $d_{\tau, i}(x)$ is the leading principal $i \times i$ minor of $g_\tau(x)$ and $d_{\tau, 0} = 1$.

If $g_\tau(x)$ is the diagonal matrix $\operatorname{diag}(\epsilon(a))$ for each $\tau$, then each quotient of minors has absolute value $1$, and $\|F\|_\lambda(x) = |F(x)|$.

**Definition 3.6.2 (Bounded automorphic form).** Let $\Delta$ be a group of unitary matrices in $\mathrm{GL}_r(E)$, let $\mathcal{L}$ be a set of lattices in $E^r$ that $\Delta$ preserves, let $\mu(\gamma, L) \in \mathbb{C}$, and let $\lambda$ be a weight. A *bounded form* of weight $\lambda$ for $(\Delta, \mathcal{L}, \mu)$ is a family $F = (F_L)_{L \in \mathcal{L}}$ of functions on frames such that, for $L \in \mathcal{L}$ and $x \in \mathcal{D}$:

1. $F_L$ is holomorphic on $\mathcal{D}$;
2. $F_L(x b) = \chi_\lambda(b) F_L(x)$ for $b \in B$;
3. $F_{\gamma L}(\gamma x) = \mu(\gamma, L)^{-1} F_L(x)$ for $\gamma \in \Delta$;
4. there is $C$, independent of $L$ and $x$, with $\|F_L\|_\lambda(x) \le C$.

For types $(c, c')$ as in [the kernel identity](/entry/kernel-identity/), the weight $\lambda(c, c')$ is given as follows. For each $\tau$, the partitions of $c_\tau$ and of $c'_\tau$ give integers $\pi_{\tau, i}$ for $i \le q_0$ and $\pi'_{\tau, i}$ for $i \le p_0$. The weight $\lambda(c, c')$ is $\pi_{\tau, i} + n/2$ at the rows of the first block and $-\pi'_{\tau, i} - n/2$ at the rows of the second block. We do not unfold the map from $c_\tau$ to its partition.

**Definition 3.6.3 (Theta span).** A family $F = (F_L)_{L \in \mathcal{L}}$ is in the *theta span* of $\Phi$ at level $M$ and type $(c, c')$ if there are finitely many $\Lambda_1, \dots, \Lambda_m \in V_n(M)$, highest weight harmonic polynomials $P_1, \dots, P_m$ of type $(c, c')$ and $a_1, \dots, a_m \in \mathbb{C}$ with
$$F_L(x) = \sum_{i=1}^m a_i\, \Theta^{P_i}_{\Phi_{L, \Lambda_i}}(x)$$
for all $L \in \mathcal{L}$ and all $x \in \mathcal{D}$.

### The spanning theorem

**Theorem 3.6.4 (Theta series span bounded forms).** Let $n$ be even with $4r < n$, let $M > 0$, and let $(\Delta, \mathcal{L}, \Phi, \mu)$ be a theta system of level $M$. Let $(c, c')$ be a type. Then every bounded form of weight $\lambda(c, c')$ for $(\Delta, \mathcal{L}, \mu)$ is in the theta span of $\Phi$ at level $M$ and type $(c, c')$.

Lean: `GlobalTheory.SW.SpanMain.theta_span` (also `GlobalTheory.T.hermitianTheta_series_span_bounded_forms`, a second name)

*Proof.* Let $F$ be a bounded form of weight $\lambda = \lambda(c, c')$. Put
$$C(L, L') = \sum\nolimits_M \langle \Phi_{L, \Lambda}, \Phi_{L', \Lambda} \rangle.$$

Step 1 (Polynomials). Since $p_0 + q_0 = r \le n$, a result of the sources gives a unitarily invariant family $P_1, \dots, P_m$ of highest weight harmonic polynomials of type $(c, c')$, not all $0$.

Step 2 (The matrix $C$). By a result of the sources, the axioms of a theta system give $a > 0$ and $\theta < 1$ such that for $L, L' \in \mathcal{L}$ and $\gamma \in \Delta$: $C(L, L) = a$; the sum $\sum_{L' \ne L} |C(L, L')|$ converges and is at most $\theta a$; and $C(\gamma L, \gamma L')\, \mu(\gamma, L)\, \overline{\mu(\gamma, L')} = C(L, L')$. So $C = a(1 + T)$ where $T$ has norm at most $\theta < 1$ as an operator on bounded families. A Neumann series result of the sources inverts it: there is a bounded form $F'$ of weight $\lambda$ for $(\Delta, \mathcal{L}, \mu)$ with
$$F_L(x) = \sum_{L' \in \mathcal{L}} C(L, L')\, F'_{L'}(x)$$
for all $L \in \mathcal{L}$ and $x \in \mathcal{D}$.

Step 3 (The slab). For $\delta > 0$ let $S_\delta$ be the set of frames $x$ with $|g_\tau(x)_{ab} - \epsilon(a)\delta_{ab}| < \delta$ for all $\tau$, $a$ and $b$. By results of the sources, for small $\delta$ the following hold. The set $S_\delta$ is open and lies in $\mathcal{D}$. Each unitary $\gamma$ maps $S_\delta$ to itself and preserves Lebesgue measure on it. Each $x \in S_\delta$ is $x' b$ with $g_\tau(x') = \operatorname{diag}(\epsilon(a))$ and $b \in B$ with entries and inverse diagonal entries bounded by a constant $K$. With condition 4 and the remark after the definition of $\|F\|_\lambda$, this gives a bound $|F'_L(y)| \le B'$ for all $L$ and all $y \in S_\delta$. Also for small $\delta$, $y \mapsto K_P(x, y)$ is integrable on $S_\delta$, and there is $\rho > 0$ with
$$\int_{S_\delta} K_P(x, y)\, G(y)\, dy = \rho\, G(x)$$
for every holomorphic $G$ on $\mathcal{D}$ with $G(yb) = \chi_\lambda(b) G(y)$ and $\|G\|_\lambda$ bounded. This reproducing property uses $2r \le n$ and that some $P_j \ne 0$. Fix such a $\delta$.

Step 4 (Kernel identity). Let $\kappa \ne 0$ be the constant of the [kernel identity](/entry/kernel-identity/). For $L, L' \in \mathcal{L}$, $x \in \mathcal{D}$ and $y \in S_\delta$, condition 3 gives $F'_{\gamma L'}(\gamma y) = \overline{\mu(\gamma, L')} F'_{L'}(y)$, since $|\mu(\gamma, L')| = 1$. So the kernel identity, times $\kappa^{-1} F'_{L'}(y)$, gives
$$\sum_{\gamma \in \Delta} C(L, \gamma L')\, K_P(x, \gamma y)\, F'_{\gamma L'}(\gamma y) = \kappa^{-1} \sum\nolimits_M \sum_{j=1}^m \Theta^{P_j}_{\Phi_{L,\Lambda}}(x)\; \overline{\Theta^{P_j}_{\Phi_{L',\Lambda}}(y)}\; F'_{L'}(y).$$
The right side is a finite sum, by the finiteness of the classes in $V_n(M)$, a result of the sources. Each term is a function of $(L, x)$, namely $\Theta^{P_j}_{\Phi_{L,\Lambda}}(x)$, times a function of $(L', y)$.

Step 5 (Unfolding). Put $f_{L, x}(L', y) = C(L, L')\, K_P(x, y)\, F'_{L'}(y)$. By Steps 2 and 3 this is integrable on $S_\delta$ for each $L'$, and the integrals of $|f_{L, x}(L', \cdot)|$ are summable over $L'$. The group $\Delta$ acts on pairs $(L', y) \in \mathcal{L} \times S_\delta$ and preserves the measure. A result of the sources gives a fundamental domain for this action: $\mathcal{L}$ is countable, and for each $L'$ there is a measurable set $D_{L'}$ such that almost every $y$ has exactly one $\gamma \in \Delta$ with $\gamma y \in D_{\gamma L'}$. We unfold the sum over $L'$ and the integral over $S_\delta$ into a sum over the orbits and an integral over the domains $D_{L'}$. The inner sum over $\Delta$ is the left side of Step 4. So
$$\sum_{L' \in \mathcal{L}} \int_{S_\delta} f_{L, x}(L', y)\, dy = \sum_{i=1}^{N} b_i\, \Theta^{P_{j_i}}_{\Phi_{L, \Lambda_i}}(x)$$
for some $N$, classes $\Lambda_i \in V_n(M)$, indices $j_i$ and constants $b_i$ that do not depend on $(L, x)$.

Step 6 (Conclusion). By Step 3, the integral of $f_{L,x}(L', \cdot)$ is $\rho\, C(L, L')\, F'_{L'}(x)$. By Step 2 the sum of these over $L'$ is $\rho F_L(x)$. Divide by $\rho$. So $F_L(x) = \sum_i \rho^{-1} b_i\, \Theta^{P_{j_i}}_{\Phi_{L, \Lambda_i}}(x)$ for all $L$ and all $x \in \mathcal{D}$. $\square$

### Level data

A theta system comes from a level datum. Let $E(u, v)$ be the rational trace form on $E^r$ built from $\kappa_0 / 2$ and $h_G$; we do not unfold it. A lattice $L \subset E^r$ is *self-dual* if it is finitely generated and $L = \{u : E(u, v) \in \mathbb{Z} \text{ for all } v \in L\}$.

**Definition 3.6.5 (Level datum).** A *level datum* consists of:

1. an ideal $\mathfrak{m} \ne 0, \mathcal{O}_E$ of $\mathcal{O}_E$ that is prime to $\bar{\mathfrak{m}}$ and to $2$;
2. vectors $\beta_1, \dots, \beta_r \in \Lambda$ with $\Lambda \subset \sum_i \mathcal{O}_E \beta_i + \mathfrak{m}\Lambda$;
3. a subgroup $J$ of $\mathrm{GL}_r(\mathcal{O}_E / \mathfrak{m})$ and a character $\lambda_J \colon J \to \mathbb{C}^\times$;
4. an integral $w \in E$ with $w + \bar w = 1$.

Two vectors $u, v \in E^r$ are *congruent* mod $\mathfrak{m}$ if $s(u - v) \in \mathfrak{m}\Lambda$ for some $s \in \mathcal{O}_E$ prime to $\mathfrak{m}$. A family $u_1, \dots, u_r$ *reduces* to $k \in J$ if $k$ has an integral lift $k'$ with $u_i$ congruent to $\sum_j k'_{ji} \beta_j$ for each $i$. The *level group* $\Delta_D$ is the group generated by the unitary $\gamma$ such that $\gamma\beta_1, \dots, \gamma\beta_r$ reduces to some $k \in J$. The *level lattices* $\mathcal{L}_D$ are the self-dual $L$ with $sL \subset \Lambda$ and $s\Lambda \subset L$ for some $s$ prime to $\mathfrak{m}\bar{\mathfrak{m}}$. For a lattice $L$, the *shift* $L^\sharp$ is the set of $v$ with $bv \in \mathfrak{m}L$ for all $b \in \bar{\mathfrak{m}}$.

For $r \le n$ and functions $v_0(L)$ on $M_{n \times g}(\mathbb{Q})$, the *level test functions* are
$$\Phi^D_{L, \Lambda} = \sum_{y} \lambda_D(y)\, \rho(y)\, u\big(P_{\Lambda \otimes L^\sharp}\, v_0(L)\big),$$
with the vacuum projection $P$ and the normalization $u$ of [the first section](/entry/is-mu-multiplier-sq-mul-det/). Here $y$ runs over representatives of $(\Lambda \otimes 2\bar{\mathfrak{m}} L) / (\Lambda \otimes 2\bar{\mathfrak{m}}\mathfrak{m} L)$, and $\lambda_D(y) = \lambda_J(k)$ if the first $r$ rows of $y$ reduce to $k \in J$ and the other rows are congruent to $0$, and $\lambda_D(y) = 0$ otherwise.

**Theorem 3.6.6 (Theta series span bounded forms at a level).** Let $n$ be even with $4([E:\mathbb{Q}]\, r) + 4 \le n$, let $D$ be a level datum, and let $M > 0$ with $M \in \mathfrak{m}$. Let $v_0(L)$ be a vacuum for $\mathcal{O}_E^n \otimes L^\sharp$, with respect to $w$, for each $L \in \mathcal{L}_D$, and let $\mu$ satisfy
$$\omega(\gamma)\, v_0(L) = \mu(\gamma, L)\, \lambda_J(k)\, v_0(\gamma L)$$
for $\gamma \in \Delta_D$, $L \in \mathcal{L}_D$ and $k \in J$ such that $\gamma\beta_1, \dots, \gamma\beta_r$ reduces to $k$. Then for every type $(c, c')$, every bounded form of weight $\lambda(c, c')$ for $(\Delta_D, \mathcal{L}_D, \mu)$ is in the theta span of $\Phi^D$ at level $M$ and type $(c, c')$.

Lean: `GlobalTheory.SW.level_theta_span`

*Proof.* Since $[E:\mathbb{Q}] \ge 1$, we have $4r \le 4[E:\mathbb{Q}]r < n$, and $r \le n$. A theorem proved elsewhere in the formalization says that, under the hypotheses, $(\Delta_D, \mathcal{L}_D, \Phi^D, \mu)$ is a theta system of level $M$. The [spanning theorem](/entry/theta-span/) applies. $\square$

**Remark 3.6.7.** Results of this kind, that theta series with harmonic coefficients span a space of modular forms, go back to the basis problem of Hecke and Eichler. The highest weight harmonic polynomials are those of Kashiwara and Vergne (Kashiwara and Vergne, *On the Segal-Shale-Weil representations and harmonic polynomials*, Invent. Math. 44 (1978)), who decompose the harmonic polynomials in the [Fock model](/learn/theta/#the-fock-model) of the [[Weil representation|H3Q2703KKV]].

**Remark 3.6.8 (Formalization).** The spanning theorem is proved in [HermitianThetaSeriesSpanBoundedForms.lean](lean:Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation/HermitianThetaSeriesSpanBoundedForms.lean#L168). The existence of the polynomials, the coefficient bounds, the Neumann series, the slab, the integrability and reproducing property of the kernel, the finiteness of the classes and the fundamental domain are lemmas cited there. The unfolding is the lemma `unfold_span` of the same file. The theorem at a level is in [LevelThetaSpan.lean](lean:Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation/LevelThetaSpan.lean#L10). Its bound $4([E:\mathbb{Q}]\,r) + 4 \le n$ is stronger than the bound $4r < n$ of the spanning theorem; it is the hypothesis of the result that the level data form a theta system. The map from $c_\tau$ to a partition, `Harm.partOf`, and the trace form `EF` are not unfolded here.
