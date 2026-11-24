---
title: Descent of small sections
decls:
  - GlobalTheory.CompanionTheory.Relay.uniform_all_root_origin_bound
  - GlobalTheory.T.uniform_all_root_origin_bound
  - GlobalTheory.CompanionTheory.Ar.Plug.vs_fin
  - GlobalTheory.T.uniform_all_tower_bound
  - GlobalTheory.CompanionTheory.Ar.Plug.descent_small
  - GlobalTheory.T.uniform_norm_all_tower_bound
  - GlobalTheory.CompanionTheory.Ar.Plug.SlopeVol.modelSmall_encard_le
status: drafted
drafted_by: writer@claude-opus-5-5
---

## Descent of small sections

A root tower carries sections on its root models, and the moduli space carries cusp sections on its components. This section moves a small section $s$ of a root model down to a cusp section $f$ on a component $Z$ of the moduli space, with bounds for its norms and its denominators. Then we count: the number of small sections on the model is at most a power of the number of small cusp sections on $Z$. This count is a step in the proof of [the comparison of slopes](/entry/slope-sub-cost-le-comp-vol-slope/) in the next section.

### The setting

Let $E$ be a CM field that is Galois over $\mathbb{Q}$, with host $H$, a datum $D$ with $N = p + q$, a level $l$, a moduli space $X_o$ and a coefficient datum $c$ with number field $F$. For each embedding $\sigma \colon F \to \mathbb{C}$ we fix an unfolding $U_\sigma$ of the complex points, a generic frame datum $h$ and, for each component $Z$ of $X_{o, F}$, a section $e_Z$ of weight $0$. We assume the component laws for $(U, h, e)$: the components of the unfoldings match the components of $X_{o, F}$, there is a component, the unfoldings are unfoldings at the good embeddings, and $e_Z$ has value $1$ at $Z$ and $0$ at every other component. We also assume the uniformization of integral points: every algebraic integral frame over a complete discrete valuation ring over a prime $\lambda$ of $F$ becomes, after a finite extension of the ring, a frame at which the reading map is defined. We do not unfold these two statements.

A weight is a family of integers $u(\tau, i)$, for CM types $\tau$ and $0 \le i < N$. We write
$$
\|u\|_1 = \sum_{\tau, i} |u(\tau, i)| .
$$
For a prime $p$ we put
$$
\varepsilon_p = \frac{1}{p - 1} + \frac{40\, v_p(d_E)}{[E : \mathbb{Q}]} + \delta_{p, 2},
$$
where $\delta_{p, 2}$ is $1$ for $p = 2$ and $0$ otherwise.

Let $Y$ be a model of $X_o$ over $\mathcal{O}_F$, let $T$ be a root tower and let $o$ be a good origin of $Y$ over $T$. For a level $B$ and a component $b$ of $T$ we write $o_{B, b}$ for the root origin of $o$, $M = M_{B, b}$ for its root model with field $\Omega$ and coordinates $y$, $d$ for the degree of its flag and $S_B$ for the bad primes of $o$ at $B$.

**Definition 8.14.1 (Small model sections).** Let $u$ be a weight and let $R \ge 0$. An element $s \in \Omega$ satisfies the Hodge bound of size $R$ if there is a form $w$ that does not vanish on the model such that at each complex point $z$ of the model with $w(z) \ne 0$ the value of $s$ at $z$ is at most
$$
R \prod_r h_r(z)^{n_r(u)} ,
$$
where $h_r$ is the norm of the singular line of $o_{B, b}$ at the root index $r$ and $n_r(u)$ is the weight of $u$ at $r$. The set $\mathcal{M}(u, R)$ of small model sections is the set of $s$ that are in the chart lattice of degree $u$ and satisfy the Hodge bound of size $R$.

An element of the chart lattice is integral at each chart: for each choice of a nonzero coordinate $y_{k, c_k}$ in each block, $s \prod_k y_{k, c_k}^{-a_k}$ is integral over the chart ring, where $a$ is the multidegree of $u$. We do not unfold the chart ring.

**Definition 8.14.2 (Reading and trace).** Let $\Omega_Z$ be the field of rational functions in the flag variables over the residue field of the generic point of $Z$. A reading of $Z$ is a field map $\varphi \colon \Omega_Z \to \Omega$ together with torus elements $t_i \in \Omega^\times$. For a weight $u$ the gauge $\gamma_u$ is the product of powers of the $t_i$ and of the root parameters $e_r^{-n_r(u)}$ of the origin. The trace of $s \in \Omega$ is
$$
\operatorname{tr}_u(s) = \operatorname{Tr}_{\Omega / \Omega_Z}(s / \gamma_u) .
$$
A reading is geometric if the image of the generic frame of $Z$ under $\varphi$ is a frame $y'$ and $y'$ differs from the base frame of the origin by the torus element of the reading.

For a prime $\lambda$ of $F$ above $p$, a valuation at $\lambda$ from an integral point is a map $g \mapsto v_R(g(y))/e$, where $R$ is a complete discrete valuation ring over $\lambda$ with ramification $e$ and $y$ is an algebraic integral frame over $R$.

### The root origin bound

**Theorem 8.14.3 (Root origin bound).** Assume the top level inputs, the component laws and the uniformization of integral points. Let $o$ be a root origin over a finite set $S$ of primes for a root model $M$, with a generic frame, let $Z$ be a component and let $\varphi$ be a linked reading of $Z$. Assume that the model of $o$ satisfies the valuation condition of root origins, and that every prime that divides $d_E$ is in $S$. Then for every finite set $B_1 \subset \Omega$ there are finite sets $B_2 \subset \Omega$ and $B_3 \subset \Omega_Z$ with this property. Let $A \subseteq \Omega$ be a subring that contains $B_1 \cup B_2$ and let $A' \subseteq \Omega_Z$ be a subring that contains $B_3$. Let $p$ be a prime, let $\mathrm{ev}_1 \colon A \to \overline{\mathbb{Q}}_p$ be a ring map with algebraic values, let $\lambda$ be a prime of $F$ above $p$, let $R$ be a complete discrete valuation ring over $\lambda$ with ramification $e_0$, let $y$ be an algebraic integral frame over $R$, let $\iota$ be an embedding of the fraction field of $R$ into $\overline{\mathbb{Q}}_p$ that gives the normalized absolute value, and let $\mathrm{ev} \colon A' \to \operatorname{Frac} R$ be a ring map that is regular at $Z$ for $y$ and compatible with $\mathrm{ev}_1$ through $\varphi$. Then there are an algebraic $p$-adic point $z$ of $M$ and positive reals $\rho_r$, one for each root index $r$, such that:

1. each $b \in B_1$ has the value $\mathrm{ev}_1(b)$ at $z$;
2. for each root index $r$,
$$
\bigl|\log \sup\nolimits_r(z) - \log \rho_r\bigr| \le c_p \log p,
$$
where $c_p = \frac{1}{p-1} + \delta_{p, 2} + \frac{v_p(d_E)}{[E : \mathbb{Q}]}$ for $p \in S$ and $c_p = 0$ for $p \notin S$;
3. for each weight $a$ and each section $f$ of weight $a$, the reading of $f$ times $\prod_r e_r^{-n_r}$ has a value $v$ at $z$, and if the normalized valuation of $f(y)$ is $e_\lambda s$, then $|v| = p^{-s} \prod_r \rho_r^{n_r}$.

Lean: `GlobalTheory.CompanionTheory.Relay.uniform_all_root_origin_bound` (also `GlobalTheory.T.uniform_all_root_origin_bound`, a second name).

*Proof.* A lemma on frame heights gives a finite set $B$ of elements of $\Omega$ at which the origin is good. A point lemma for the birational coordinates $y$ gives a finite set $B_2$ and, for each $A$ and $\mathrm{ev}_1$, an algebraic $p$-adic point $z$ of $M$ in a subring $A_2 \subseteq A$ with the right values on $B_1$, on $B$, on the ratios $y_a / y_b$ and on the inverses of the torus elements. We take $B_3 = \emptyset$. A finite extension of $R$ carries the values of $\mathrm{ev}_1$, and the integral frame $y$ moves to this extension by base change. The uniformization of integral points gives a further extension with a frame at which the reading is defined. The torus elements of the reading and the groupoid law of the Borel torus give a torus element that joins this frame to the frame of the origin. So we get an integral point of the tower at $z$. Two lemmas on root origins, one for sections and one for degrees, bound the values of sections and the sup norms at this point. A reading lemma combines them into the numbers $\rho_r$ and gives properties 2 and 3. We do not unfold these lemmas. $\square$

### Bounded denominators

**Theorem 8.14.4 (Denominators of descended sections).** Assume the top level inputs, the component laws and the uniformization of integral points. Let $T$ be a root tower with a good origin $o$, let $B$ be a level, $b$ a component of $T$, $Z$ a component of $X_{o, F}$ and $\varphi$ a reading of $Z$. Let $u$ be a weight, let $s$ be in the chart lattice of degree $u$, and let $f$ be a section of weight $u$ that is supported on $Z$ and has the value $\operatorname{tr}_u(s)$ at the generic frame of $Z$. Then for each prime $p$, each prime $\lambda$ of $F$ above $p$ and each valuation $v$ at $\lambda$ from an integral point,
$$
v(f) \ge -v_\lambda(p)\, \varepsilon_p'\, \|u\|_1 ,
$$
where $\varepsilon_p' = \varepsilon_p$ for $p \in S_B$ and $\varepsilon_p' = 0$ for $p \notin S_B$.

Lean: `GlobalTheory.CompanionTheory.Ar.Plug.vs_fin` (also `GlobalTheory.T.uniform_all_tower_bound`, a second name with one more hypothesis: the reading is geometric).

*Proof.* If $f(y) = 0$, then $v(f) = \infty$. Otherwise $y$ lies on $Z$. A lemma on good origins shows that the reading is linked, and the primes that divide $d_E$ are in $S_B$. The [root origin bound](/entry/relay-uniform-all-root-origin-bound/) gives a $p$-adic point $z$ of the model and numbers $\rho_r$ with $|\log \sup_r(z) - \log \rho_r| \le c_p \log p$. At $z$ the reading of $f$ has norm $p^{-s_0} \prod_r \rho_r^{n_r}$, where $v(f) = e_\lambda s_0$. The image of $\operatorname{Tr}(s/\gamma_u)$ is a sum of evaluations of $s/\gamma_u$ at the conjugate points. The image of $f$ is not $0$, since $y$ can be moved to a regular point. Because $s$ is in the chart lattice, each evaluation has norm at most $p^{s_0 + c_p \|u\|_1}$ times the norm of the image of $f$. The ultrametric inequality for the sum gives $s_0 \ge -c_p \|u\|_1$. Last, $c_p \le \varepsilon_p'$ and $v_\lambda(p) = e_\lambda$. $\square$

### Descent

**Theorem 8.14.5 (Descent of small sections).** Assume the top level inputs, the component laws and the uniformization of integral points, and let $x$ be a real number with $|\tau(\xi_0)| = x$ for every good embedding $\sigma$, every base point $\xi_0$ of $U_\sigma$ and every embedding $\tau$ of $E$. Let $T$ be a root tower with a good origin $o$, let $B$ be a level, $b$ a component of $T$, $Z$ a component and $\varphi$ a geometric reading of $Z$. Let $u$ be a weight with strictly decreasing rows, let $R \ge 0$ and let $s \in \mathcal{M}(u, R)$. Then there is a cusp section $f$ on $Z$ of weight $u$ with these properties.

1. The value of $f$ at the generic frame of $Z$ is $\operatorname{tr}_u(s)$.
2. At each frame of $Z$ over each good embedding, the norm of $f$ is at most $dR$.
3. For each prime $p$, each prime $\lambda$ of $F$ above $p$ and each valuation $v$ at $\lambda$ from an integral point, $v(f) \ge -v_\lambda(p)\, \varepsilon_p'\, \|u\|_1$, with $\varepsilon_p'$ as in the last theorem.

Lean: `GlobalTheory.CompanionTheory.Ar.Plug.descent_small` (also `GlobalTheory.T.uniform_norm_all_tower_bound`, a second name).

*Proof.* The index of the tower is $j = p$ and $1 \le j < N$, so $p, q \ge 1$. A lemma for the component laws uses the chart lattice condition on $s$. It gives a section $f$ of weight $u$, supported on $Z$, with the value $\operatorname{tr}_u(s)$ at the generic frame. A norm lemma uses the Hodge bound and the condition on $|\tau(\xi_0)|$, and bounds the norm of $f$ by $dR$ at each frame of $Z$ over each good embedding. Since $p, q \ge 1$, the rows of $u$ decrease strictly and the norm of $f$ is bounded, $f$ is a cusp section on $Z$. The valuation bound is the [theorem on denominators](/entry/vs-fin/). $\square$

### Counting

For a finite set $S$ of primes and a weight $u$ let
$$
N_S(u) = \prod_{p \in S} p^{\lceil 2 \varepsilon_p \|u\|_1 \rceil} .
$$
For a real number $B_d$ let $\mathrm{Small}_Z(u, R')$ be the set of cusp sections on $Z$ of weight $u$ that are integral for the mixed valuations at $B_d$ and have norm at most $R'$ at each frame over each good embedding. The mixed valuations are the height valuations at the primes of the set $S(l, B_d)$ of primes $p \le B_d$ and $p \mid 2|d_E| M'_l$, and the valuations from integral points at the other primes. We count with values in $\mathbb{N} \cup \{\infty\}$.

**Lemma 8.14.6 (Counting small sections).** Keep the assumptions of the descent theorem, and assume the low height comparison at the primes, which we do not unfold. Let $B_d$ be a real number with $S(l, B_d) = S_B$, and assume $d > 0$. Let $k_0 \in \mathbb{N}$, $R_0 \ge 0$ and $f_1, \dots, f_d \in \mathcal{M}(k_0 u, R_0)$, and assume that the traces are nondegenerate: for every weight $v$ and every $s \in \Omega$, if $\operatorname{tr}_v(s f_i) = 0$ for all $i$, then $s = 0$. Let $\tau > 0$ be an integer, let $R \ge 0$, and let $R'$ be a real number with
$$
N_{S_B}\bigl((\tau + k_0) u\bigr)\, d\, R R_0 \le R' .
$$
Then
$$
\# \mathcal{M}(\tau u, R) \le \Bigl(\# \mathrm{Small}_Z\bigl((\tau + k_0) u, R'\bigr)\Bigr)^d .
$$

Lean: `GlobalTheory.CompanionTheory.Ar.Plug.SlopeVol.modelSmall_encard_le`.

*Proof.* It is enough to give a relation from $\mathcal{M}(\tau u, R)$ to $d$-tuples in $\mathrm{Small}_Z$ that is total and injective. Let $s \in \mathcal{M}(\tau u, R)$ and $N = N_{S_B}((\tau + k_0) u)$. A product lemma gives $s f_i \in \mathcal{M}((\tau + k_0) u, R R_0)$. The [descent theorem](/entry/descent-small/) gives a cusp section $g_i$ on $Z$ with the value $\operatorname{tr}(s f_i)$ at the generic frame, norm at most $d R R_0$, and the lower bound for its valuations at $S_B$. With the low height comparison, this lower bound shows that $N g_i$ is integral for the mixed valuations. Its norm is at most $N d R R_0 \le R'$. So $N g_i \in \mathrm{Small}_Z((\tau + k_0) u, R')$. If $s$ and $s'$ give the same tuple, then $g_i = g_i'$, so $\operatorname{tr}((s - s') f_i) = 0$ for each $i$ since the trace is additive, and $s = s'$ by nondegeneracy. $\square$

**Remark 8.14.7 (Formalization).** The component laws are a hypothesis of the root origin bound, but its proof does not use them (UniformAllRootOriginBound.lean:23 to 24), and the set $B_3$ is always empty (line 38). That proof runs with `maxHeartbeats 1600000` (line 22). In the theorem on denominators the proof uses the constant $c_p$ with the factor $1$ in front of $v_p(d_E)/[E : \mathbb{Q}]$, where $\varepsilon_p$ has $40$ (`exTwo` in ModelSmall.lean:50 and `htEx` in SemiposAtOfPositive.lean:76). So the stated bound is weaker than the proved one. The second name `T.uniform_all_tower_bound` asks that the reading is geometric and does not use it (UniformAllTowerBoundStatement.lean:17). The name `T.uniform_norm_all_tower_bound` speaks of a norm bound, but the statement also gives the descent and the valuation bound. In the counting lemma, nondegeneracy is assumed for every weight $v$ and used only at $v = (\tau + k_0) u$ (UniformAllNormHeightBound.lean:248). The valuation condition of root origins and the linked readings are not unfolded here. The statement file of the root origin bound imports `Mathlib` twice (UniformAllRootOriginBoundStatement.lean:1 and 3).
