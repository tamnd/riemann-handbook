---
title: Moves and symmetric kernels
decls:
  - GlobalTheory.T.term_integral_near_one_bound
  - GlobalTheory.HL.FibU.shares
  - GlobalTheory.HL.MoveTotal.total_moves
  - GlobalTheory.T.exists_symm_invariant_kernel_hermitian_frames
  - GlobalTheory.HL.exists_symm_invariant_kernel
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Moves and symmetric kernels

The local amplitude at a finite place is a sum of phases over the terms of a pair of Hermitian frames. To show that this sum is small compared with the mass of the terms, we construct a Markov-type kernel on the terms: a symmetric, invariant kernel whose rows sum to almost $1$, but whose rows, twisted by the phase, sum to almost $0$. The kernel counts the *moves* of a term: Eichler transformations that carry one term lattice to another. This section first proves a local count on a quadric, then the estimates for the total measure of the moves, and then constructs the kernel. The kernel is used in the [cancellation bound](/entry/amp-le-mass/) of the next section.

### The local frames setting

Let $F$ be a nonarchimedean local field of characteristic $0$, with uniformizer $\varpi$ and residue field of size $q$. Let $E$ be a reduced quadratic $F$-algebra with conjugation $x \mapsto \bar x$ and ring of integers $\mathcal{O}$, and let $\psi_0$ be a fixed additive character of $E$. Let $n = k + 2r + 1$ and $V = E^n$, with a nondegenerate Hermitian form $h$.

A *frames record* $S$ consists of two frames $f_0, \dots, f_r$ and $f'_0, \dots, f'_r$ in $V$ with parameters $T, T' \in F^\times$, and isotropic dual vectors $e_0, \dots, e_{r-1}$ and $e'_0, \dots, e'_{r-1}$:
$$h(f_a, f_b) = \begin{cases} -T & a = b = r, \\ 0 & \text{otherwise}, \end{cases} \qquad h(f_a, e_j) = \delta_{a j},$$
and the same for the second frame. Let $D_l$ be the leading $l \times l$ minor of the matrix $(h(f'_b, f_a))_{a,b}$, and assume
$$G_S = D_{r+1} \overline{D_{r+1}} - T T' D_r \overline{D_r} \ne 0.$$
The record also fixes a flag that tells whether $E$ is split with unit parameters. Let $\theta = \varpi$ in this split case and $\theta = 1$ otherwise. Put
$$a = v_E(G_S) - 2(r+1)\, v(\theta).$$
Let $N$ and $N'$ be the unipotent groups of the two frames, with characters $\psi$ and $\psi'$, and let $N_0 = N \cap N'$. Let $M_E$ be the span of the two frames and $W_0 = M_E^\perp$. For $J \le r + 1$ let $X_J$ and $X'_J$ be the spans of the $f_i$ and of the $f'_i$ with $i < J$, and $Y_J = X_J + X'_J$.

**Definition 2.19.1 (Terms, defect and families).** A *datum* $d$ consists of two inner lattices $A$ and $A'$ for the two frames and a graph. A *term* of $d$ is an $\mathcal{O}$-lattice
$$\Lambda = n \operatorname{std}(f, A) = n' \operatorname{std}(f', A'), \qquad n \in N,\ n' \in N',$$
with $n' f'_b - n f_b \in \theta \Lambda$ for all $b$, and with the graph of $d$ determined by $\Lambda$. The *frames of the term* are $g_b = n f_b$ and $g'_b = n' f'_b$. Its *mass* is $\mu(\Lambda) = 1/\operatorname{vol}(N_0 \cap \operatorname{Stab}\Lambda)$, for a fixed compact open subgroup of volume $1$, and its *phase* is $\omega(\Lambda) = \psi(n)\psi'(n')^{-1}$. The *defect lattice* is the span $M(\Lambda)$ of the $g_b$ and the $\theta^{-1}(g'_b - g_b)$, and the *defect index* is $\beta(\Lambda) = [\Lambda \cap M_E : M(\Lambda)]$.

Each $y \in \Lambda \cap M_E$ has a *level*: the least $j$ such that $\theta y = \sum \alpha_i g_i + \sum \alpha'_i g'_i$ with $\alpha'_i \in \mathcal{O}$ and $\alpha_i + \alpha'_i \in \theta \mathcal{O}$ for $i \ge j$. A term is of the *second type* if its defect is nonzero, all levels are at most $r$, and a pairing condition between the two isotropic spans holds. For $\beta, J, \beta_J \in \mathbb{N}$, the *family* $\mathcal{F}(\beta, J, \beta_J)$ is the set of second type terms with defect index $\beta$, largest level $J$, and $\beta_J$ cosets of $M(\Lambda)$ at level $J$.

**Definition 2.19.2 (Index integral).** Let $A$ be an additive group and $\varphi \colon A \to \mathbb{C}$. Suppose that some subgroup $B \le A$ of finite index leaves $\varphi$ invariant and that the support of $\varphi$ meets finitely many cosets of $B$. Then $\varphi$ is *integrable* on $A$ and
$$\int_A \varphi = \frac{1}{[A : B]} \sum_{c \in A/B} \varphi(c).$$
This does not depend on $B$, and $\int_A 1 = 1$.

### A count on the quadric

Put $\varepsilon = q^{2r + 4 - k}$. Let $U_J(\Lambda) = \Lambda \cap Y_J^\perp$. A vector $u$ lies on the *quadric* $Z$ if $h(u, u) \in \varpi^{a} \mathcal{O}_F$. It *leaks* if there is no $y \in \Lambda \cap W_0$ with $h(u, y) = 1$.

**Proposition 2.19.3 (Shares of the quadric).** Let $k \ge 4r + 7$, $J \in \mathbb{N}$, and let $\Lambda$ be a term of a datum $d$. Write $U = U_J(\Lambda)$. Then:

1. $\big| q^{a} \int_U \mathbf{1}_Z - 1 \big| \le \tfrac{8}{7}\, \varepsilon$;
2. $q^{a} \int_U \mathbf{1}[u \in Z,\ u \text{ leaks}] \le \tfrac{16}{7}\, \varepsilon$;
3. for every $y \in V$ such that $u \mapsto \psi_0(h(y, u))$ is not trivial on $U$,
$$q^{a} \Big| \int_U \mathbf{1}_Z(u)\, \psi_0(h(y, u)) \Big| \le \tfrac{8}{7}\, \varepsilon.$$

Lean: `GlobalTheory.HL.FibU.shares` (also `GlobalTheory.T.term_integral_near_one_bound`, a second name).

*Proof.* The term $\Lambda$ is self-dual. Let $N \ge a + 1$. Since $\mathcal{O}/\varpi^N \mathcal{O}$ is finite, the subgroup $\varpi^N \Lambda \cap U$ has finite index in $U$, so there is a finite set $R \subseteq U$ of representatives of $U$ modulo $\varpi^N \Lambda$. The quadric condition is invariant under $\varpi^N \Lambda$: if $u \in Z$ and $b \in \varpi^N \Lambda$, then $h(u + b, u + b) - h(u, u) \in \varpi^{a+1} \mathcal{O}_F$, by self-duality. The leak condition is invariant in the same way. For a function that is invariant under $\varpi^N \Lambda$, the index integral over $U$ is the mean over $R$:
$$\int_U \mathbf{1}_Z\, g = \frac{1}{\# R} \sum_{u \in R \cap Z} g(u).$$
So the three claims are statements about finite sums over $R$. A finite count on the quadric modulo $\varpi^N$ gives them: the number of $u \in R$ on the quadric is $\# R\, q^{-a}$ up to an error of $\tfrac{8}{7}\varepsilon \cdot \# R\, q^{-a}$; the leaking points are at most $\tfrac{16}{7}\varepsilon \cdot \# R\, q^{-a}$; and a nontrivial character sum over the points of the quadric is at most $\tfrac{8}{7}\varepsilon \cdot \# R\, q^{-a}$. Dividing by $\# R\, q^{-a}$ gives (1) and (2) with $N = a + 1$. For (3), choose $m$ with $\varpi^m y$ in the dual of $\Lambda$ and take $N = m + a + 1$. Then $u \mapsto \psi_0(h(y, u))$ is invariant under $\varpi^N \Lambda$, it is not trivial on $R$, and the count applies. $\square$

### Moves

Let $J \ge 1$ and let $\Lambda$ be a term. A *move* at level $J$ is a tuple $w = (x, x', u, t)$ in the group
$$A_J(\Lambda) = B_J(\Lambda) \times U_J(\Lambda) \times T_a,$$
where $B_J(\Lambda)$ is the group of pairs $(x, x') \in X_J \times X'_J$ with $x + x' \in \theta \Lambda$, and $T_a$ is the group of $t \in \varpi^{a}\mathcal{O}$ with $t + \bar t = 0$. Put $s = \tfrac12 h(u, u) + t$. The tuple *is a move* if the level of $x + x'$ is $J$ and $s \in \varpi^{a}\mathcal{O}$. Its *Eichler transformation* is
$$E_w(v) = v + h(v, u)\, x - h(v, x)\,(u + s x),$$
and $w$ *moves* $\Lambda$ to $\Lambda_1 = \{v : E_w(v) \in \Lambda\}$. For $j < r$ and a pair $b = (x, x')$ let
$$\chi(b, u) = \psi_0\big(-\theta^{-1} h(y_b, u)\big), \qquad y_b = h(x, e_j)\, g_{j+1} + h(x', e'_j)\, g'_{j+1}.$$
Finally put $c_K = q^{a} \beta / \beta_J$.

**Theorem 2.19.4 (Total measure of moves).** Let $k \ge 4r + 7$, $j < r$, and let $\Lambda$ be a term of $d$ in the family $\mathcal{F}(\beta, j + 1, \beta_J)$. Write $A = A_{j+1}(\Lambda)$ and $\mathbf{1}_{\mathrm{mv}}$ for the indicator of the moves at level $j + 1$. Then the functions $\mathbf{1}_{\mathrm{mv}}$, $\mathbf{1}_{\mathrm{mv}} \cdot \mathbf{1}[u \text{ leaks}]$ and $\mathbf{1}_{\mathrm{mv}} \cdot \chi$ are integrable on $A$, and
$$\begin{aligned} \Big| c_K \operatorname{Re} \int_A \mathbf{1}_{\mathrm{mv}} - 1 \Big| &\le \tfrac{8}{7}\, \varepsilon, \\ c_K \operatorname{Re} \int_A \mathbf{1}_{\mathrm{mv}}\, \mathbf{1}[u \text{ leaks}] &\le \tfrac{16}{7}\, \varepsilon, \\ c_K \Big| \int_A \mathbf{1}_{\mathrm{mv}}\, \chi \Big| &\le \tfrac{8}{7}\, \varepsilon. \end{aligned}$$

Lean: `GlobalTheory.HL.MoveTotal.total_moves`.

*Proof.* There is a subgroup of finite index in $A$ that leaves the moves, the leak condition of $u$ and the character $\chi$ invariant, and whose cosets meet the moves in a finite set; this gives the integrability. A tuple is a move if and only if $(x, x')$ has level $j + 1$, $u \in U_{j+1}(\Lambda) \cap Z$, and $t$ lies in the fibre $\{t : \tfrac12 h(u,u) + t \in \varpi^a \mathcal{O}\}$. For each $u \in Z$ this fibre has measure one in $T_a$. So the index integral over $A$ splits as a product:
$$\int_A \mathbf{1}_{\mathrm{mv}}(w)\, \phi(b, u) = \int_{B} \mathbf{1}[\text{level } j + 1] \int_U \mathbf{1}_Z(u)\, \phi(b, u)$$
for each invariant $\phi$, where $B = B_{j+1}(\Lambda)$ and $U = U_{j+1}(\Lambda)$. The share of the pairs of top level is
$$\int_{B} \mathbf{1}[\text{level of } x + x' \text{ is } j + 1] = \frac{\beta_J}{\beta},$$
because the top level cosets are $\beta_J$ of the $\beta$ cosets of the defect lattice. With $\phi = 1$ and $\phi = \mathbf{1}[u \text{ leaks}]$, the product is $(\beta_J/\beta)$ times the integral over $U$. Multiplying by $c_K$ gives $q^a$ times the integral over $U$, and parts (1) and (2) of the [Proposition 2.19.3](/entry/shares/) give the first two bounds. For the third bound, fix $b$ of top level. Then $u \mapsto \chi(b, u)$ is not trivial on $U$, so part (3) of the Proposition bounds the inner integral by $\tfrac{8}{7}\varepsilon\, q^{-a}$. Integrating over $b$ gives the factor $\beta_J / \beta$, and multiplying by $c_K$ gives the bound. If $q^a = 0$, then $c_K = 0$ and the third bound is trivial. $\square$

### The kernel

**Definition 2.19.5 (Move kernel).** For terms $\Lambda$, $\Lambda_1$ of $d$ put
$$K(\Lambda, \Lambda_1) = c_K \operatorname{Re} \int_{A_{j+1}(\Lambda)} \mathbf{1}[w \text{ moves } \Lambda \text{ to } \Lambda_1].$$

**Theorem 2.19.6 (A symmetric invariant kernel).** Let $k \ge 4r + 7$, $j < r$, $\beta, \beta_J \in \mathbb{N}$, a datum $d$, and let $P$ be the set of terms of $d$ in $\mathcal{F}(\beta, j + 1, \beta_J)$. Then there is a kernel $K$ on lattices such that:

1. $K(h\Lambda, h\Lambda_1) = K(\Lambda, \Lambda_1)$ for $h \in N_0$ and $\Lambda, \Lambda_1 \in P$;
2. for $\Lambda \in P$, only finitely many $\Lambda_1 \in P$ have $K(\Lambda, \Lambda_1) \ne 0$;
3. $K(\Lambda, \Lambda_1) \ge 0$ and $K(\Lambda, \Lambda_1) = K(\Lambda_1, \Lambda)$ for $\Lambda, \Lambda_1 \in P$;
4. for $\Lambda \in P$,
$$\Big| \sum_{\Lambda_1 \in P} K(\Lambda, \Lambda_1) - 1 \Big| \le \tfrac{24}{7}\, \varepsilon, \qquad \Big| \sum_{\Lambda_1 \in P} K(\Lambda, \Lambda_1)\, \omega(\Lambda_1) \Big| \le \tfrac{24}{7}\, \varepsilon.$$

Lean: `GlobalTheory.HL.exists_symm_invariant_kernel` (also `GlobalTheory.T.exists_symm_invariant_kernel_hermitian_frames`, a second name).

*Proof.* Take the move kernel. Invariance holds because $N_0$ fixes both frames: conjugation by $h \in N_0$ carries the moves of $\Lambda$ to $\Lambda_1$ onto the moves of $h\Lambda$ to $h\Lambda_1$, and it keeps the index integral. A move determines its target, and the moves of $\Lambda$ meet finitely many cosets of a subgroup of finite index, so only finitely many targets occur; this gives (2). The kernel is the real part of the integral of an indicator, so it is nonnegative. Symmetry holds because a flip of the tuple, which is a bijection from $A_{j+1}(\Lambda)$ to $A_{j+1}(\Lambda_1)$, carries the moves of $\Lambda$ to $\Lambda_1$ onto the moves of $\Lambda_1$ to $\Lambda$, and the reference subgroups of the two terms have the same relative index, so the index integral is kept.

For (4), split the moves of $\Lambda$ by their targets. A move whose $u$ does not leak carries $\Lambda$ to a term in $P$. So the row sum over $P$ differs from $c_K \operatorname{Re}\int \mathbf{1}_{\mathrm{mv}}$ by at most the measure of the leaking moves. By the [Theorem 2.19.4](/entry/total-moves/) on the total measure of moves, the row sum is within $\tfrac{8}{7}\varepsilon + \tfrac{16}{7}\varepsilon = \tfrac{24}{7}\varepsilon$ of $1$. For the twisted sum, the phase of the target of a move $w = (b, u, t)$ is $\omega(\Lambda_1) = \omega(\Lambda)\, \chi(b, u)$, and $|\omega(\Lambda)| = 1$. So the twisted row sum is $c_K \int \mathbf{1}_{\mathrm{mv}}\, \chi$ up to the leaking moves, and the same Theorem bounds it by $\tfrac{8}{7}\varepsilon + \tfrac{16}{7}\varepsilon$. Only the row sums use $k \ge 4r + 7$. $\square$

**Remark 2.19.7 (Formalization).** The index integral is `cint` and integrability is `Nice` ([Cint.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/Cint.lean#L16)); `cint` returns $0$ for a function that is not integrable. The groups of moves, the leak condition `NoLeak`, the quadric `InZ`, the character `chiM` and the kernel `kern` are in [NoLeak.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/NoLeak.lean#L19). The condition "is a move" is `IsMove`, which also asks $s + \bar s = h(u, u)$; this holds for every $s = \tfrac12 h(u,u) + t$ with $t + \bar t = 0$. The phase $\omega$ is defined with a chosen witness $(n, n')$, and with $(1, 1)$ for a lattice that is not a term. The kernel theorem quantifies over a predicate $P$ with $P(\Lambda) \iff (\Lambda \text{ is a term in the family})$, and its proof replaces $P$ by this condition at once ([ExistsSymmInvariantKernelHermitianFrames.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/ExistsSymmInvariantKernelHermitianFrames.lean#L20)). The count on the quadric is the lemma `quadric_character_leak_shares_finite`, which is not unfolded here. The constant $\varepsilon$ is written as $q^{1 - (k - 2r - 3)}$.
