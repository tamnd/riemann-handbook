---
title: Theorem A for towers of kernels
decls:
  - Formalism.FourierDecayAlt.P.theorem_a_after
  - Formalism.FourierDecayAlt.Final.tc_theoremAAfter
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Theorem A for towers of kernels

Theorem A bounds a sum of squared norms of vectors in a Hilbert space by the limit of a base energy, times a factor close to $1$. The vectors come with a tower of kernels, one for each level $i = 0, 1, \dots, r + 1$, and the proof is an induction on the level: each level is bounded by the levels below it, and a recursion lemma solves the resulting system of inequalities. This section states the abstract setting, proves the recursion lemma, and derives Theorem A from a one-level inequality and a limit step.

**Definition 3.3.1 (Points and towers).** Let $E$ be a field. A *point* is a finite list $p = ((s_1, t_1), \dots, (s_m, t_m))$ with $s_k \in \mathbb{N}$ and $t_k \in E$. Its *level* is $s_1 + \dots + s_m$, and $p$ is a *point of level $i$* if its level is $i$, each $s_k \geq 1$ and each $t_k \neq 0$. For a point $h$, $s \geq 1$ and $t \in E$ let $h \oplus (s, t)$ be the list $h$ followed by $(s, t)$. A *tower* $T$ is a family of finite sets $\Sigma(b, s) \subseteq E \setminus \{0\}$ for $b, s \in \mathbb{N}$, together with the sets $X_i$ of points of level $i$ whose $k$-th entry $(s_k, t_k)$ has $t_k \in \Sigma(s_1 + \dots + s_{k-1} + 1, s_k)$.

So $X_i$ is finite, and $X_0 = \{()\}$ contains only the empty point. A point of $X_i$ whose last block has size $s$ is $h \oplus (s, t)$ with $h \in X_{i-s}$ and $t \in \Sigma(i - s + 1, s)$.

**Definition 3.3.2 (Kernel data).** *Kernel data* $D$ over $E$ consist of the following.

1. Integers $r, f, K \geq 0$.
2. A set $W$ of *words* with weights $\mathrm{wt}(w) \in \mathbb{R}$ and counts $\mathrm{cnt}(w) \in \mathbb{N}$, a finite set $W_{\mathrm{all}} \subseteq W$, and an empty word $\emptyset \in W_{\mathrm{all}}$ with $\mathrm{cnt}(\emptyset) = 0$ and $\mathrm{wt}(\emptyset) = 1$.
3. Gram kernels $G_{\varepsilon, i, w}(p, q) \in \mathbb{C}$ for $\varepsilon > 0$, $i \in \mathbb{N}$ and $w \in W$.
4. Level kernels $K_i(p, q)$, with $K_0((), ()) = 1$, and numbers $e_i \in \mathbb{R}$.
5. Additive subgroups $\Lambda(b, s)$, $\Lambda'(b, s)$ and $\Lambda^*(i)$ of $E$, a Fourier coefficient $\widehat N_{\varepsilon, i, w}(Y, \kappa, l) \in \mathbb{C}$, size vectors $\rho_D(i), \rho_L(b, s) \in \mathbb{R}^f$, real functions $a_v : E \to \mathbb{R}$ for $v = 1, \dots, f$, and volumes $\mathrm{vol}(b, s) \in \mathbb{R}$.

Put $N_{\mathrm{top}} = 4K(r + 1)$, $\mathrm{bud}(i) = 4K(r + 1 - i)$, and $W(n) = \{w \in W_{\mathrm{all}} : \mathrm{cnt}(w) \leq n\}$. The *majorant* of $l \in E$ at sizes $\rho$ is $m_\rho(l) = \prod_{v} \min(1, (\rho_v / a_v(l))^K)$.

**Definition 3.3.3 (Energies).** For a finite set $Y$ of points, a kernel $\kappa$, $s \geq 1$ and $t, t' \in E$ put
$$\begin{aligned} S_{\varepsilon, i, w}(Y) &= \mathrm{Re} \sum_{p, q \in Y} K_i(p, q)\, G_{\varepsilon, i, w}(p, q), \qquad Q_{\varepsilon, i}(w) = S_{\varepsilon, i, w}(X_i) / \mathrm{wt}(w), \\ N^{s}_{\varepsilon, i, w}(Y, \kappa; t, t') &= \mathrm{wt}(w)^{-1} \sum_{h, h' \in Y} \kappa(h, h')\, G_{\varepsilon, i, w}(h \oplus (s, t), h' \oplus (s, t')), \\ N^0_{\varepsilon, k, w}(Y, \kappa) &= \mathrm{wt}(w)^{-1}\, \mathrm{Re} \sum_{h, h' \in Y} \kappa(h, h')\, G_{\varepsilon, k, w}(h, h'). \end{aligned}$$
For a kernel $\kappa$ let $\kappa^{s}_{t, t'}(h, h') = \kappa(h \oplus (s, t), h' \oplus (s, t'))$.

The quantity $Q_{\varepsilon, i}(w)$ is the energy of level $i$ seen through the word $w$. The words at level $i$ have count at most $\mathrm{bud}(i)$, so each step down a level allows $4K$ more letters.

**Definition 3.3.4 (Domination).** A family of kernels $\Theta_{i, s, t}$ *dominates* the tower $T$ if for $1 \leq s \leq i \leq r + 1$, with $b = i - s + 1$ and $Y = X_{i-s}$:

1. $\Theta_{i, s, t} - (K_i)^s_{t, t}$ is positive semidefinite on $Y$ for $t \in \Sigma(b, s)$;
2. $\Theta_{i, s, t} = \Theta_{i, s, t'}$ on $Y$ when $t, t' \in \Sigma(b, s)$ and $t - t' \in \Lambda(b, s)$;
3. $(1 + e_i) K_{i - s} - \sum_{t \in S} \Theta_{i, s, t}$ is positive semidefinite on $Y$ for each $S \subseteq \Sigma(b, s)$ whose elements are pairwise incongruent modulo $\Lambda(b, s)$.

Domination is the local input of the induction: up to the factor $1 + e_i$, the kernel at level $i$ is controlled by the kernel at level $i - s$, one residue class modulo $\Lambda(b, s)$ at a time.

**Definition 3.3.5 (Hypotheses of Theorem A).** We use these conditions on $D$, a Hilbert space $H$, vectors $V_p \in H$, coefficients $c_\rho(p) \in \mathbb{C}$, and numbers $\vartheta, j, \varepsilon_0, C_4$.

1. *Positivity.* Each $G_{\varepsilon, i, w}$ ($\varepsilon > 0$) and each $K_i$ is positive semidefinite on each finite set, each $\mathrm{wt}(w) > 0$, and $0 \leq e_i \leq 1$ for $1 \leq i \leq r + 1$.
2. *Support.* If $h, h'$ have level $i - s$, $t, t'$ are nonzero and distinct, and $K_i(h \oplus (s, t), h' \oplus (s, t')) \neq 0$, then $(i, s) \neq (r + 1, 1)$ and $t^{-1} - t'^{-1} \in \Lambda'(i - s + 1, s)$.
3. *Domination.* Each tower has a dominating family.
4. *Wave estimate.* For each word $w$ with $\mathrm{cnt}(w) + K \leq N_{\mathrm{top}}$ there are probability vectors $\theta_A$ on $W(\mathrm{cnt}(w) + K)$ such that, for $Y$ of level $i - 1$ and $\kappa$ positive semidefinite on $Y$, $\widehat N(Y, \kappa, 0) = N^0_{i-1, w}(Y, \kappa)$, and for $0 \neq l \in \Lambda^*(i)$ some $A$ gives $|\widehat N(Y, \kappa, l)| \leq m_{\rho_D(i)}(l) \sum_{w'} \theta_A(w') N^0_{i - 1, w'}(Y, \kappa)$.
5. *Poisson step.* If the sum of $|\widehat N(Y, \kappa, l)|$ over each finite set of nonzero $l \in \Lambda^*(i)$ is at most $B$, then $\sum_{t \in S} \mathrm{Re}\, N^1_{i, w}(Y, \kappa; t, t) \leq |\widehat N(Y, \kappa, 0)| + B$ for each finite $S$ of nonzero $t$ in one coset of $\Lambda(i, 1)$.
6. *Lift estimate.* The off-diagonal terms $|N^s(Y, \kappa^s_{t, t'}; t, t')|$ with $t^{-1} \neq t'^{-1}$ are bounded by $m_{\rho_L}(t^{-1} - t'^{-1})$ times an average of the diagonal terms at $t$ and $t'$ over pairs of words.
7. *Block estimate.* For $2 \leq s$ and $\mathrm{vol}(b, s) \leq 1$, the sum of $\mathrm{Re}\, N^s(Y, \kappa; t, t)$ over $t$ in one coset of $\Lambda(b, s)$ is at most $C_4^{fs} \prod_{1 \leq s' < s} \mathrm{vol}(b, s')$ times an average of $N^0_{i - s, w'}(Y, \kappa)$.
8. *Lattice sums.* The majorants $m_{\rho_D(i)}$ over nonzero elements of $\Lambda^*(i)$, and $m_{\rho_L(b, s)}$ over nonzero elements of $\Lambda'(b, s)$, have all finite sums at most $\varepsilon_0$.
9. *Sizes.* $\mathrm{vol}(b, s) \geq 0$, and $\mathrm{vol}(b, s) \leq \vartheta^{-2f}$ when $b, s \geq 1$ and $b + s \leq r + 2$.
10. *Base limit.* $\mathrm{Re}\, G_{\varepsilon, 0, w}((), ()) / \mathrm{wt}(w) \to j$ as $\varepsilon \to 0^+$, for $w \in W(N_{\mathrm{top}})$.
11. *Cutoff.* For each finite set $Y$ of points of level $r + 1$, for all small $\varepsilon > 0$, $G_{\varepsilon, r+1, \emptyset}(p, q) = \langle V_q, V_p \rangle$ when $p, q \in Y$ and $K_{r+1}(p, q) \neq 0$.
12. *Leading domination.* $c_\rho(p) \neq 0$ only for points of level $r + 1$; $K_{r+1} - \sum_{\rho \in R} c_\rho \otimes \overline{c_\rho}$ is positive semidefinite on each finite set of such points, for each finite $R$; and $\sum_p |c_\rho(p)| \|V_p\| < \infty$.

**Lemma 3.3.6 (Recursion).** There is $C$ such that the following holds. Let $r \in \mathbb{N}$, $0 \leq \varepsilon \leq a \leq 1/2$ with $ra \leq 1$, and let $e_i, \sigma_i \geq 0$ satisfy, for $1 \leq i \leq r + 1$,
$$\sigma_i \leq (1 + \varepsilon) \sqrt{1 + e_i}\, \sigma_{i-1} + \sum_{t = 2}^{i} a^{t - 1} \sigma_{i - t}.$$
Then $\sigma_{r+1}^2 \leq (1 + C(r + 1) a) \prod_{i = 1}^{r + 1} (1 + e_i)\, \sigma_0^2$.

*Proof.* Put $P_i = \prod_{j \leq i} \sqrt{1 + e_j}$, so $1 \leq P_{i - t} \leq P_{i - 1}$ and $\sqrt{1 + e_i}\, P_{i - 1} = P_i$. Let $\tau_i = \sigma_i / P_i$ and $M_i = \max_{j \leq i} \tau_j$. Dividing the hypothesis by $P_i$ gives $\tau_i \leq (1 + \varepsilon) \tau_{i-1} + \sum_{t \geq 2} a^{t-1} \tau_{i - t}$. So $\tau_i \leq (1 + \varepsilon + a/(1 - a)) M_{i-1} \leq (1 + 3a) M_{i-1}$, since $\varepsilon \leq a$ and $a \leq 1/2$. By induction $M_{r+1} \leq (1 + 3a)^{r+1} \sigma_0$. Since $(r + 1) a \leq 3/2$, we get $(1 + 3a)^{2(r+1)} \leq e^{6(r+1)a} \leq 1 + C(r + 1) a$ with $C = 2(e^9 - 1)/3$, by convexity of the exponential on $[0, 9]$. Then $\sigma_{r+1}^2 = P_{r+1}^2 \tau_{r+1}^2$ gives the claim. $\square$

**Proposition 3.3.7 (One level).** Assume conditions 1, 2 and 4 to 8 of the hypotheses with $\varepsilon_0 \geq 0$ and $C_4 \geq 1$, and $0 \leq \mathrm{vol}(b, s) \leq 1$ for $b, s \geq 1$, $b + s \leq r + 2$. Let $T$ be a tower with a dominating family, $\varepsilon > 0$ and $1 \leq i \leq r + 1$. If $\sigma_k \geq 0$ and $Q_{\varepsilon, k}(w) \leq \sigma_k^2$ for $k < i$ and $w \in W(\mathrm{bud}(k))$, then for $w \in W(\mathrm{bud}(i))$
$$\begin{aligned} \sqrt{Q_{\varepsilon, i}(w)} \leq{} & \sqrt{(1 + 3^f \varepsilon_0)(1 + 2^f \varepsilon_0)(1 + e_i)}\; \sigma_{i-1} \\ &+ \sum_{s = 2}^{i} \Big((1 + 3^f \varepsilon_0)(1 + e_i)\, C_4^{fs} \prod_{1 \leq s' < s} \mathrm{vol}(i - s + 1, s')\Big)^{1/2} \sigma_{i - s}. \end{aligned}$$

*Proof (outline).* Split $X_i$ by the size $s$ of the last block. The form $S_{\varepsilon, i, w}$ is a squared norm (a Schur product of two positive semidefinite kernels, by [the closure rules](/entry/local-cores/)), so its square root is at most the sum of the square roots of the pieces. In each piece, the support condition and the lift estimate bound the terms with $t \neq t'$, and the lattice sums give the factor $1 + 3^f \varepsilon_0$. The diagonal terms are bounded by the dominating family, one residue class at a time. For $s = 1$ the Poisson step and the wave estimate bound one residue class by $N^0$ plus $2^f \varepsilon_0$ times the largest $N^0$, and condition 3 of domination sums the classes with the factor $1 + e_i$. For $s \geq 2$ the block estimate does the same with the volume factor. The induction hypothesis bounds each $N^0$ at level $i - s$ by $\sigma_{i - s}^2$, since the words that occur have count at most $\mathrm{bud}(i) + (s + 1) K \leq \mathrm{bud}(i - s)$. $\square$

**Lemma 3.3.8 (Limit step).** Assume conditions 1 (for $G$ and $K$), 10, 11 and 12. Let $B \in \mathbb{R}$, and assume that for each tower $T$, $\varepsilon > 0$ and $\sigma$ with $\mathrm{Re}\, G_{\varepsilon, 0, w}((), ())/\mathrm{wt}(w) \leq \sigma$ for $w \in W(N_{\mathrm{top}})$, we have $S_{\varepsilon, r+1, \emptyset}(X_{r+1}) \leq B \sigma$. Then $\sum_{\rho \in R} \|\sum_p c_\rho(p) V_p\|^2 \leq B j$ for each finite $R \subseteq \mathbb{N}$.

*Proof (outline).* The series converge absolutely by condition 12, so it is enough to bound the partial sums over finite sets $Y$ of points of level $r + 1$. Take a tower whose sets $\Sigma$ contain all entries of these points; then $Y \subseteq X_{r+1}$. For small $\varepsilon$, the cutoff identifies $G_{\varepsilon, r+1, \emptyset}$ with the Gram kernel of the $V_p$ where $K_{r+1} \neq 0$, and leading domination with rule 2 of [the closure rules](/entry/local-cores/) gives $\sum_\rho \|\sum_{p \in Y} c_\rho(p) V_p\|^2 \leq S_{\varepsilon, r+1, \emptyset}(X_{r+1})$. By the base limit, $\sigma = j + \delta$ is admissible for small $\varepsilon$. Let $\delta \to 0$. $\square$

**Theorem 3.3.9 (Theorem A).** For $C_1, C_4 \geq 1$ there are $C, C'$ with the following property. Let $D$ be kernel data with $K \geq 4$ and $f \geq 1$, let $\vartheta > 0$ with $C' \leq \vartheta$ and $r (C/\vartheta)^f \leq 1$, and let $j \in \mathbb{R}$, $H$ a complex Hilbert space, $V_p \in H$ and $c_\rho(p) \in \mathbb{C}$. Assume conditions 1 to 12 with this $C_4$ and with $\varepsilon_0 = (C_1 \vartheta^{-(K - 5/2)})^f$. Then for each finite $R \subseteq \mathbb{N}$
$$\sum_{\rho \in R} \Big\| \sum_p c_\rho(p)\, V_p \Big\|^2 \leq \Big(1 + C(r + 1) \Big(\frac{C}{\vartheta}\Big)^f\Big) \prod_{i = 1}^{r + 1} (1 + e_i)\; j.$$

Lean: `Formalism.FourierDecayAlt.P.theorem_a_after` (also `Formalism.FourierDecayAlt.Final.tc_theoremAAfter`, a second name).

*Proof.* Put $C_0 = \max(3C_1, 2C_4)$, and let $C_J$ be the constant of the recursion lemma, applied in the form with $a = (C_0/\vartheta)^f$ and $\varepsilon = (C_0 \vartheta^{-(K - 5/2)})^f$. Take $C = \max(C_0, C_J)$ and $C'$ large enough that $\vartheta \geq \max(3C_1, 1)$ and that $a \leq 1/2$. Fix a tower $T$, $\varepsilon > 0$ and $\sigma$ as in the limit step. Let $\sigma_k$ be the square root of the largest positive part of $Q_{\varepsilon, k}(w)$ over $w \in W(\mathrm{bud}(k))$. Then $\sigma_0^2 \leq \sigma$, since $\mathrm{bud}(0) = N_{\mathrm{top}}$ and $X_0 = \{()\}$ with $K_0((), ()) = 1$. Since $\vartheta^{-(K - 5/2)} \leq \vartheta^{-1}$, we have $3^f \varepsilon_0 \leq 1$ and $3^f \varepsilon_0 \leq \varepsilon$, so the first coefficient of the one-level inequality is at most $(1 + \varepsilon)\sqrt{1 + e_i}$. By the size condition the product of volumes is at most $\vartheta^{-2f(s-1)}$, and with $e_i \leq 1$ and $C_0 \geq 2C_4$ the coefficient of $\sigma_{i-s}$ is at most $a^{s-1}$. So the one-level inequality gives the hypothesis of the recursion lemma for the $\sigma_k$, and $\sigma_{r+1}^2 \leq (1 + C(r+1)(C/\vartheta)^f) \prod (1 + e_i)\, \sigma$. The empty word lies in $W(\mathrm{bud}(r+1)) = W(0)$ and has weight $1$, so $S_{\varepsilon, r+1, \emptyset}(X_{r+1}) = Q_{\varepsilon, r+1}(\emptyset) \leq \sigma_{r+1}^2$. The limit step, applied with the zero family in place of the domination kernels, gives the theorem. $\square$

**Remark 3.3.10 (Formalization).** Theorem A is `TC.TheoremAAfter` ([StatementTC.lean](lean:Formalism/HermitianCurvature/StatementTC.lean#L88)); the conditions are the definitions in [StatementTB.lean](lean:Formalism/HermitianCurvature/StatementTB.lean#L128), and domination is `DomMin` (line 42 of StatementTC.lean). It differs from the older `TB.TheoremA` only in that domination replaces `KernelPSD` and `ThetaDomination`. `theorem_a_after` ([RecursionWithDensities.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/RecursionWithDensities.lean#L1122)) applies `theoremAAfterOfSteps` (line 822) to `oneLevelAfter`, `limitStep` ([FinitePointSets.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/FinitePointSets.lean#L116)) and `joint_theorem_A'`. The recursion lemma is `RecursionText` (Statement.lean, line 16), proved as `coarseBound` in RecText.lean; we did not open that proof and give our own. The one-level inequality is `OneLevelAfter`; we opened the statements of its steps (`SplitBySize`, `SchurStep`, `DiagStep`, `OneStep`, `MultiStep`) but not their proofs, so its proof here is an outline. The second name `tc_theoremAAfter` is at line 1208 of HeisenbergConjugationMeasurePreserving.lean, whose name says nothing about Theorem A.
