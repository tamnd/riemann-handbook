---
title: The log-sine Monge-Ampère fibre integral
decls:
  - GlobalTheory.T.square_polar_integral_identity
  - GlobalTheory.CompanionTheory.Ar.PB.AnSq.sum_polar_gH_eq
  - GlobalTheory.T.log_sine_monge_ampere_integral
  - GlobalTheory.CompanionTheory.Ar.PB.FibPt.fibre_integral_any_frame
  - GlobalTheory.T.log_sine_monge_ampere_normalized
  - GlobalTheory.CompanionTheory.Ar.PB.FibN.fibre_integral_normal
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The log-sine Monge-Ampère fibre integral

This section computes the mixed Monge-Ampère integrals of the norm function of an analytic square (Section 8). In a fibre chart the square is a family of pairs of points of the projective line, the norm function is a log-sine function of a positive $2 \times 2$ matrix, and the potentials are $\xi$-potentials of the same matrix. We first compute the integral over one pair of fibres when the matrix is the identity to second order, then for any matrix by a unitary change of frame and a Möbius change of variables, and then we integrate over the base with a parameter cover. The result is a polar identity: a combination of mixed integrals on the square is $2\kappa(k)$ times a mixed degree on the base. It is the analytic input of the reflection sum in Section 10. For the background we use [Chern-Weil forms](/learn/positivity-resolution/#chern-weil-forms) and [arithmetic intersection numbers](/learn/arakelov/#arithmetic-varieties-and-intersection-numbers).

### Fibre functions

For a positive definite $2 \times 2$ matrix $G$ and $a, a' \in \mathbb{C}$ put $\langle a, a' \rangle_G = (1, \bar a)\, G\, (1, a')^{T}$. The $\xi$-potential and the log-sine function of $G$ are
$$
\xi_G(a) = -\log \langle a, a \rangle_G + \tfrac12 \log \det G,
$$
$$
\operatorname{logsin}_G(a_0, a_1) = \tfrac12 \log \Bigl(1 - \frac{\lvert\langle a_0, a_1 \rangle_G\rvert^2}{\langle a_0, a_0 \rangle_G \langle a_1, a_1 \rangle_G}\Bigr) .
$$
For $G = 1$, the point $a$ of the projective line corresponds by stereographic projection to a unit vector $n(a)$ in $\mathbb{R}^3$, and $\operatorname{logsin}_1(a_0, a_1) = \frac12 \log((1 - n(a_0) \cdot n(a_1))/2)$.

For functions $\varphi_1, \dots, \varphi_D$ on an open set of $\mathbb{C}^D$ with complex Hessians $H_r$, the Monge-Ampère density is
$$
\operatorname{MA}(\varphi)(z) = \Bigl(\frac{2}{\pi}\Bigr)^{D} \operatorname{Re} \sum_{S \subseteq \{1, \dots, D\}} (-1)^{D - \lvert S\rvert} \det \sum_{r \in S} H_r(z) .
$$
This is $D!$ times the mixed discriminant of the Hessians, normalized by $(2/\pi)^D$.

**Definition 10.9.1.** For $k \geq 1$ let
$$
g_k(X_0, X_1) = X_1 \sum_{j < 2k} (-1)^j X_0^{2k-1-j} X_1^j ,
$$
and let $\sigma$ be the normalized surface measure on the unit sphere $S^2$. Put
$$
\begin{aligned}
\kappa(k) = -\int_{S^2} \int_{S^2} & \tfrac12 \log \frac{1 - n_1 \cdot n_2}{2} \\
& \cdot \partial_0 \partial_1 g_k(n_{1,3}, n_{2,3})\, d\sigma(n_1)\, d\sigma(n_2) .
\end{aligned}
$$

The fibre local statement is a list of five sphere moment identities. The last one says
$$
\kappa(k) = \frac12 \sum_{j < k} \frac{1}{2j + 1},
$$
so $\kappa(1) = 1/2$ and $\kappa(2) = 2/3$. The first one says that the same double integral with $a \cdot n_1$ and $a \cdot n_2$ in place of $n_{1,3}$ and $n_{2,3}$ is $-\kappa(k)\, \lvert a\rvert^{2k-2}$ for every $a \in \mathbb{R}^3$.

### The integrands

Fix $d$ and $k$ with $1 \leq k$ and $2k \leq d + 2$. Let $G$ be a family of $2 \times 2$ matrices on $\mathbb{C}^d$ and $\alpha$ a function on $\mathbb{C}^d$. For $i < k$ define $d + 2$ functions of $(z_0, z_1, w) \in \mathbb{C} \times \mathbb{C} \times \mathbb{C}^d$: for $r < 2k$
$$
\varphi^{(i)}_r = u_{r,0}\, \xi_{G(w)}(z_0) + u_{r,1}\, \xi_{G(w)}(z_1),
$$
and $\varphi^{(i)}_r = \alpha(w)$ for $r \geq 2k$, where $u_0 = (1, -1)$, $u_1 = (0, 1)$, $u_r = (1, 0)$ for $2 \leq r < 2 + 2i$, and $u_r = (0, 1)$ for $2 + 2i \leq r < 2k$. On $\mathbb{C} \times \mathbb{C}^d$ define $\psi_r(z, w) = \xi_{G(w)}(z)$ for $r < 2k - 1$ and $\psi_r = \alpha(w)$ for the other $d + 2 - 2k$ indices.

### The normalized fibre integral

**Theorem 10.9.2 (Normalized fibre integral).** Assume the fibre local statement. Let $y \in \mathbb{C}^d$, assume that $G$ is positive definite near $y$, that $G$ and $\alpha$ are of class $C^2$ at $y$, that $G(y) = 1$ and that the derivative of $G$ at $y$ is $0$. Then
$$
\begin{aligned}
\sum_{i < k} \int_{\mathbb{C}^2} & \operatorname{logsin}_{G(y)}(p_0, p_1)\, \operatorname{MA}(\varphi^{(i)})(p_0, p_1, y)\, dp \\
&= 2 \kappa(k) \int_{\mathbb{C}} \operatorname{MA}(\psi)(a, y)\, da .
\end{aligned}
$$

Lean: `GlobalTheory.CompanionTheory.Ar.PB.FibN.fibre_integral_normal` (also `GlobalTheory.T.log_sine_monge_ampere_normalized`, a second name).

*Proof.* Step 1: the Hessian. Since $G(y) = 1$ and $dG(y) = 0$, the complex Hessian of $(a, w) \mapsto \xi_{G(w)}(a)$ at $(a, y)$ is block diagonal. Its fibre block is $-\omega(a)$, where $\omega(a) = (1 + \lvert a\rvert^2)^{-2}$ is the Fubini-Study density, and its base block is $\sum_{m} n_m(a)\, T_m$ for three fixed hermitian matrices $T_m$ and the coordinates $n_m(a)$ of the unit vector $n(a)$.

Step 2: linear algebra. The mixed discriminant is multilinear. With the Hessian of $\alpha$ in the remaining slots, a lemma on mixed discriminants gives a linear functional $\Lambda$ on $\mathbb{R}^3$ such that each density on the left is a sum of products of $\omega(p_0)$ or $\omega(p_1)$ with polynomials in $\Lambda(n(p_0))$ and $\Lambda(n(p_1))$. The pattern of the vectors $u_r$ makes the sum over $i$ telescope into the polynomial $\partial_0 \partial_1 g_k$ evaluated at $\Lambda(n(p_0))$ and $\Lambda(n(p_1))$.

Step 3: the sphere. Stereographic projection sends $\omega(a)\, da$ to a multiple of $\sigma$. The left side becomes a double integral over $S^2 \times S^2$ of $\frac12 \log((1 - n_1 \cdot n_2)/2)$ against $\partial_0 \partial_1 g_k$, which the first sphere moment identity evaluates as $-\kappa(k)$ times a power of the norm of the vector of $\Lambda$. The right side is an integral over one sphere of a power of $\Lambda(n)$, which another moment identity evaluates as the same power. Comparing the two gives the factor $2\kappa(k)$. $\square$

### Any frame

**Theorem 10.9.3 (Fibre integral in any frame).** Assume the fibre local statement. Let $y \in \mathbb{C}^d$, assume that $G$ is positive definite near $y$ and that $G$ and $\alpha$ are of class $C^2$ at $y$. Then the identity of the normalized fibre integral holds at $y$.

Lean: `GlobalTheory.CompanionTheory.Ar.PB.FibPt.fibre_integral_any_frame` (also `GlobalTheory.T.log_sine_monge_ampere_integral`, a second name).

*Proof.* A lemma on local frames gives a family $g(w)$ of invertible $2 \times 2$ matrices, of class $C^2$ at $y$, such that $G'(w) = g(w)^* G(w) g(w)$ is positive definite near $y$, $G'(y) = 1$ and $dG'(y) = 0$. The normalized theorem holds for $G'$ and $\alpha$.

The matrix $g(y)$ acts on the projective line by a Möbius transformation $\mu$. For the new frame, $\xi_{G'(w)}(a) = \xi_{G(w)}(\mu_w(a)) + \log \lvert j_w(a) \rvert^2$ with a holomorphic factor $j_w$, so the complex Hessians agree after the change of variables, and the Monge-Ampère densities transform with the Jacobian of $\mu$. The log-sine function is invariant: $\operatorname{logsin}_{G'(y)}(a_0, a_1) = \operatorname{logsin}_{G(y)}(\mu(a_0), \mu(a_1))$. The change of variables formula for $\mu$ on $\mathbb{C}$ and for $(\mu, \mu)$ on $\mathbb{C}^2$ holds off the null set where a denominator of $\mu$ vanishes. So both sides of the identity for $G'$ equal the corresponding sides for $G$. $\square$

### The polar identity of a square

Let $S$ be an analytic system of dimension $d + 1$ indexed by a finite set, and let $Q$ be an analytic square for $(S, a_0, \varepsilon)$ with system $S_W$, maps $q_0, q_1$, section $v$ and constant $c_Q$. For an index $a$ of a system let $\theta_a + \varphi_a$ be its singular potential, and for indices $w_1, \dots, w_D$ let $\operatorname{deg}(w)$ be the mixed integral of $\theta_{w_1}, \dots, \theta_{w_D}$. The norm function of the square is
$$
g_H = \log \lVert v \rVert + c_Q + \tfrac12 \sum_a \varepsilon_a \bigl(\varphi_a \circ q_0 + \varphi_a \circ q_1\bigr) .
$$
For $c_1, \dots, c_D$ functions on the indices and a function $F$ of words of length $D$ put
$$
\operatorname{pol}_D(F)(c) = \sum_{w} \Bigl(\prod_{r} c_r(w_r)\Bigr) F(w) ,
$$
the multilinear extension of $F$. For a function $c$ on the indices of $S$ let $c^{(0)}$ be $c$ on the indices of $S_W$ and $0$ at $\ast$, and let $c^{(1)}$ be $c(a_0)$ at $\ast$, $0$ at $a_0$ and $c$ elsewhere. These are the coefficients of a combination pulled back by $q_0$ and by $q_1$. For $i < k$ let $W^{(i)}$ be the sequence of $d + 2$ coefficients
$$
\varepsilon^{(0)} - \varepsilon^{(1)},\ \varepsilon^{(1)},\ \underbrace{\varepsilon^{(0)}, \dots}_{2i},\ \underbrace{\varepsilon^{(1)}, \dots}_{2k - 2 - 2i},\ c^{(0)}, \dots, c^{(0)} .
$$
Let $\operatorname{mix}(\varepsilon, c)$ be the sequence of $2k - 1$ copies of $\varepsilon$ followed by $d + 2 - 2k$ copies of $c$.

**Theorem 10.9.4 (Polar identity of a square).** Assume the inputs and the fibre local statement. Let $Q$ be an analytic square for $(S, a_0, \varepsilon)$, let $c$ be a function on the indices with $c(a_0) = 0$, and let $1 \leq k$ with $2k \leq d + 2$. Then
$$
\begin{aligned}
\sum_{i < k} \operatorname{pol}_{d+2}&\Bigl(w \mapsto \int_{S_W} g_H\, \operatorname{MA}(\theta + \varphi)_{w}\Bigr)(W^{(i)}) \\
&= 2 \kappa(k)\, \operatorname{pol}_{d+1}(\operatorname{deg})\bigl(\operatorname{mix}(\varepsilon, c)\bigr) .
\end{aligned}
$$

Lean: `GlobalTheory.CompanionTheory.Ar.PB.AnSq.sum_polar_gH_eq` (also `GlobalTheory.T.square_polar_integral_identity`, a second name).

*Proof.* Step 1: from words to sums. The regularized potentials of the square converge, and the open parts of $S$ and $S_W$ are open with null complements and $C^2$ potentials. By the signed convergence statement of the inputs, the singular potentials of $S$ are integrable for the mixed Monge-Ampère measure, and their mixed integrals are the mixed degrees. By multilinearity, each side is the mixed integral of the sums of potentials with the given coefficients, so the left side is an integral of $g_H$ against the Monge-Ampère density of $d + 2$ potentials on $S_W$, and the right side is an integral of $1$ against $d + 1$ potentials on $S$.

Step 2: parameter covers. The parameter covers $\Phi_W$ of $S_W$ and $\Phi_Y$ of $S$ turn both integrals into sums over $m$ of integrals over $\mathbb{C}^2 \times B_m$ and $\mathbb{C} \times B_m$. A density lemma for squares shows that in the charts the sums of potentials are, up to pluriharmonic functions, the functions $\varphi^{(i)}$ and $\psi$ for $G = G_m$ and the base potential $\alpha_m$ of the combination $c$. The first coefficient $\varepsilon^{(0)} - \varepsilon^{(1)}$ gives $\xi(z_0) - \xi(z_1)$, which is the vector $u_0 = (1, -1)$. The condition $c(a_0) = 0$ makes the base coefficients agree under $q_0$ and $q_1$. Pluriharmonic terms do not change the densities.

Step 3: the fibres. By Fubini, each integral over $\mathbb{C}^2 \times B_m$ is an integral over $w \in B_m$ of an integral over the fibre $\mathbb{C}^2$. The diagonal $z_0 = z_1$ is a null set, and off it $g_H$ is $\operatorname{logsin}_{G_m(w)}(z_0, z_1)$ by the square. The theorem on the fibre integral in any frame, applied at each $w \in B_m$, gives $2\kappa(k)$ times the fibre integral on the right. Summing over $m$ gives the identity. $\square$

**Remark 10.9.5 (Formalization).** The second names only restate their theorems (`Development/AutomorphicSpectrum/Proofs/MetricProofs/SquarePolarIntegralIdentityStatement.lean`, `LogSineMongeAmpereIntegralStatement.lean` and `LogSineMongeAmpereNormalizedStatement.lean`). The fibre local statement is `GroundTheory.Heights₂.Heights.Inter.FibreLocal.Statement` (`GroundTheory/HeightsAndTheta/Heights/Intersections/StatementsFibreLocal.lean:26`). It is proved as `FibreLocal.proof` in `PFibreLocal.lean:166`, yet all three theorems carry it as a hypothesis instead of using the proof. The $\xi$-potential and the log-sine function are `xiPot` and `logSin` in `InFlagDomainOne.lean` (lines 31 and 34), the density is `maDens` in `MaIntEmpty.lean:34`, $\kappa$ is `kappa` in `KappaSt.lean:21`, and the multilinear extension and the coefficients are `polar`, `pull0`, `pull1`, `wcoef` and `gH` in `Definitions/MetricPeriods/Pull1.lean`; the mixed sequence is `mix` and the word pattern is `word` in `CompRightEqZero.lean` (lines 9 and 16). The density in the Lean code is written as $D!$ times a mixed discriminant with the factor $1/D!$, which is the formula above. The normalized theorem is in `LogSineMongeAmpereNormalized.lean:115`, the theorem in any frame in `LogSineMongeAmpereIntegral.lean:251`, and the polar identity in `SquarePolarIntegralIdentity.lean:130`, which calls the density lemma at line 169 and the theorem in any frame at line 202. I did not unfold the Hessian decomposition of the $\xi$-potential, the lemma on mixed discriminants, the sphere moment lemmas, the Möbius lemmas, nor the density lemma for squares, so the formulas in Step 1 of the normalized proof and in Step 2 of the polar identity follow their names and their use.
