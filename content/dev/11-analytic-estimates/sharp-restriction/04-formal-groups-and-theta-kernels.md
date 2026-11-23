---
title: The height two formal group and theta kernels
decls:
  - Formalism.InvariantFactorPaths.G7.Top.betaIsG
  - Formalism.InvariantFactorPaths.G7.Top.entryStar
  - Formalism.InvariantFactorPaths.G7.kernel_bounds_generic
  - Formalism.InvariantFactorPaths.G7.Top.kernel_from_k_one_k
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The height two formal group and theta kernels

This section studies the formal group law of height two whose [logarithm](/learn/formal-groups/#the-invariant-derivation-and-the-logarithm) is $\sum_j X^{p^{2j}}/p^j$, and uses it to bound jet coefficients of theta kernels. It proves three results. The first classifies, up to integral exponentials, the symmetric bilinear cocycles of this law: each is a multiple of one explicit series $G_c$. The second bounds the jet pairing of an entry operator against a series of a fixed shape. The third combines the two into valuation bounds for the frame jets of a theta kernel. The first two feed [the theta and local matching step](/step/theta-local-matching/), and the third feeds [the kernel bound for the second formal group](/entry/formalism-l2-th1-d-kernel-of-f-2/). Background is in [formal group laws](/learn/formal-groups/#formal-group-laws) and [height](/learn/formal-groups/#height).

### The setting

Let $K$ be a field of characteristic $0$ with an ultrametric absolute value, and $p > 2$ a prime. A power series over $K$ is *integral* if all its coefficients have norm at most $1$. We write $\exp$ for the exponential series, and say that $f \simeq g$ if $f - g$ has constant term $0$ and $\exp(f - g)$ is integral. A ring endomorphism $\sigma$ of $K$ is an *unramified Frobenius lift* if $|p| = 1/p$, every nonzero norm is a power of $p$, and $|\sigma(a) - a^p| \leq 1/p$ whenever $|a| \leq 1$.

**Definition 8.4.1 (The height two series).** Put
$$\ell(X) = \sum_{j \geq 0} \frac{X^{p^{2j}}}{p^j}, \qquad g(X) = \sum_{j \geq 0} \frac{X^{p \cdot p^{2j}}}{p^{j+1}},$$
$$A(X_0, X_1) = \sum_{0 \leq i \leq j} \frac{X_0^{p^{2i}} X_1^{p \cdot p^{2j}}}{p^{i+j+1}}, \qquad A'(X_0, X_1) = A(X_1, X_0),$$
and, for $c, c' \in K$, $G_{c,c'} = c\,A - c'\,A'$.

A two-variable series $F$ is a *law with logarithm $\ell$* if $F(0,0) = 0$, $F$ is integral, and $\ell(F(X_0, X_1)) = \ell(X_0) + \ell(X_1)$. Since $\ell$ is invertible under composition, such an $F$ equals $\ell^{-1}(\ell(X_0) + \ell(X_1))$. The series $\ell$ is the logarithm of the [[Lubin-Tate formal group laws|77QT4B80V8]] law of height $2$ attached to the unramified quadratic extension of $\mathbb{Q}_p$ and the uniformizer $p$.

For a two-variable series $H$ put
$$(\delta_F H)(X_0, X_1, X_2) = H(F(X_0, X_1), X_2) - H(X_0, X_2) - H(X_1, X_2).$$
This is the coboundary in the first variable: $\delta_F H = 0$ says that $H$ is additive in $X_0$ for the law $F$. Write $H^{\mathrm{sw}}(X_0, X_1) = H(X_1, X_0)$.

**Definition 8.4.2 (Bilinear cocycle).** A series $\beta(X_0, X_1)$ is a *bilinear cocycle* for $F$ if every monomial of $\beta$ contains both $X_0$ and $X_1$, $\delta_F \beta \simeq 0$, $\delta_F \beta^{\mathrm{sw}} \simeq 0$, and $\beta(\zeta X_0, X_1) \simeq \beta(X_0, \zeta^p X_1)$ for every $\zeta \in K$ with $\zeta^{p^2 - 1} = 1$.

The last condition says that $\beta$ is semilinear for the action of $\mu_{p^2 - 1}$, which acts on the first variable through $\zeta$ and on the second through its Frobenius twist $\zeta^p$.

**Theorem 8.4.3 (Cocycles of the height two law).** Let $K$ be complete, ultrametric and of characteristic $0$, let $\sigma$ be an unramified Frobenius lift on $K$, and assume that $K$ contains a primitive root of unity of order $p^2 - 1$. Let $F$ be a law with logarithm $\ell$ and $\beta$ a bilinear cocycle for $F$. Then there is $c \in K$ with $|c| \leq 1$ and $\sigma^2(c) = c$ such that $\beta \simeq G_{c, \sigma(c)}$.

Lean: `Formalism.InvariantFactorPaths.G7.Top.betaIsG` (also `Formalism.InvariantFactorPaths.G7.BetaIsG`).

*Proof (outline).* For a two-variable series $G$ put $\Delta G = p^{-1}\bigl(G^{\sigma}(X_0^p, X_1^p) - pG\bigr)$, where $G^\sigma$ applies $\sigma$ to the coefficients, and
$$H_{\gamma, \gamma'}(G) = \Delta G - \gamma\, g(X_0)\ell(X_1) - \gamma'\, \ell(X_0) g(X_1).$$

Step 0. The semilinearity under $\mu_{p^2 - 1}$ gives a series $G \simeq \beta$ whose monomials $X_0^{n_0} X_1^{n_1}$ have $n_0, n_1 \geq 1$ and $n_0 \equiv p\, n_1 \pmod{p^2 - 1}$, and which still has $\delta_F G \simeq 0$ and $\delta_F G^{\mathrm{sw}} \simeq 0$.

Step 1. There is $c$ with $|c| \leq 1$ such that $\partial_{X_0} G - c\, \ell'(X_0) g(X_1)$ is integral. The same step for $G^{\mathrm{sw}}$ gives $c'$ with $|c'| \leq 1$.

Step 2. Then $\delta_F(\Delta G) - \sigma(c)\,(\delta_F g)(X_0, X_1)\, \ell(X_2)$ is integral, and likewise for $G^{\mathrm{sw}}$ with $\sigma(c')$.

Step 3. The two facts of Step 2 together give that $H_{\sigma(c), \sigma(c')}(G)$ is integral.

Step 4. If $\partial_{X_0} G - c\,\ell'(X_0) g(X_1)$ and $H_{\sigma(c), \sigma(c')}(G)$ are integral, then $c + \sigma(c') = 0$. Applied to $G$ this gives $\sigma(c') = -c$. Applied to $G^{\mathrm{sw}}$, for which the roles of $c$ and $c'$ are exchanged, it gives $c' = -\sigma(c)$, so $\sigma(c') = -\sigma^2(c)$. Hence $\sigma^2(c) = c$.

Step 5. If $\sigma^2(c) = c$ and $H_{\sigma(c), -c}(G)$ is integral, then $G \simeq G_{c, \sigma(c)}$. Since $\simeq$ is symmetric and transitive, $\beta \simeq G \simeq G_{c, \sigma(c)}$. $\square$

### Jet pairings of entry operators

Fix integers $\nu, r_0, r_1 \geq 1$ and work with variables $x_{s,a,b}$ for $s \in \mathbb{Z}/2\nu$, $a < r_0$, $b < r_1$. The index $s$ is a colour. For a polynomial $P$ and a power series $\Theta$ in these variables, the *jet pairing* is
$$\langle P, \Theta \rangle = \sum_{\kappa} P_\kappa\, \kappa!\, \Theta_\kappa = \bigl(P(\partial)\Theta\bigr)(0),$$
where $\kappa! = \prod_v \kappa_v!$.

**Definition 8.4.4 (The class of a theta series).** For $u : \mathbb{Z}/2\nu \to K$ put
$$\pi_{s,a,b} = \sum_{l \geq 0} (-1)^l x_{s - 2l, a, b}^{\,p^{2l}}, \qquad h_u = \sum_{s} u_s \sum_{a,b} \pi_{s,a,b}^{\,p}\, \pi_{s+1,a,b}.$$
A series $\Theta$ is *in the class of $h_u$* if there are integral series $U_0, U_1, \dots$ with
$$\Theta_n = \sum_{i \leq |n|} p^{-i}\, (h_u^{\,i}\, U_i)_n \quad \text{for every exponent } n.$$
Since $h_u$ has no constant term, this says that $\Theta = \sum_i p^{-i} h_u^{\,i} U_i$.

**Definition 8.4.5 (Entry operator).** Let $T\!T \subseteq \mathbb{Z}/2\nu$ be a set of colours, $\xi : \mathbb{Z}/2\nu \times \{0, \dots, r_0 - 1\} \to K$, and $e : \mathbb{Z}/2\nu \times \{0, \dots, r_1 - 1\} \to \mathbb{N}$. Let $C$ be a number of columns, and for each column $c < C$ let $l_c$ be a height, $\mathrm{sf}(c)$ a colour, $T_c$ an $l_c \times r_0$ matrix and $I_c : \{0, \dots, l_c - 1\} \to \{0, \dots, r_1 - 1\}$. Put
$$\begin{aligned} \mathrm{top}_{s,b} &= \sum_a \xi_{s,a}\, x_{s,a,b}, \qquad m_c = \det\Bigl(\sum_a (T_c)_{i,a}\, x_{\mathrm{sf}(c), a, I_c(i')}\Bigr)_{i, i' < l_c}, \\ Q &= \prod_c m_c, \qquad P = \prod_{s,b} \mathrm{top}_{s,b}^{\,e(s,b)} \cdot Q. \end{aligned}$$
Write $\alpha_s = \sum_b e(s,b)$ and $\lambda_s = \sum_{c : \mathrm{sf}(c) = s} l_c$.

For $\gamma(p) = p/(p^2 - 1)$, $\rho(p) = 1/(p^2 - 1)$ and $\mathrm{lg}(m) = \lfloor \log_p m \rfloor + 1$ for $m \geq 1$, $\mathrm{lg}(0) = 0$, put
$$\Delta = \sum_s \bigl(r_1\, \mathrm{lg}(\alpha_s) + r_0 r_1\, \mathrm{lg}(\lambda_s)\bigr) + \sum_{s \in T\!T} \mathrm{lg}(\alpha_s)^2.$$

The expansion of $h_u$ after the shift $x_{s,a,b} \mapsto x_{s,a,b} + \xi_{s,a}\, y_{s,b}$ ($s \in T\!T$) contains two kinds of leading terms. A term of type A is indexed by $\phi = (s, i, j, a, b)$ with $i, j < E$; it is a monomial in the new variables $y$ of degree $p^{1+2i}$ at $(s - 2i, b)$ and $p^{2j}$ at $(s + 1 - 2j, b)$. A term of type B is indexed by $\kappa = (s, i, b)$; it is $y_{s,b}^{p^{2i+1}}$ times the linear form in the direction $d_\kappa$ with $d_\kappa(s + 2i + 1, a, b) = \xi_{s,a}^{p^{2i+1}}$ and $0$ elsewhere. For a polynomial $Q$ and multiplicities $\beta_\kappa$, the *Hasse derivative* $D^{\beta} Q$ is the coefficient of $\prod_\kappa t_\kappa^{\beta_\kappa}$ in $Q(x + \sum_\kappa t_\kappa d_\kappa)$.

**Theorem 8.4.6 (Entry bound).** Assume $|p| = 1/p$, $|u_s| \leq 1$, $|\xi_{s,a}| \leq 1$, $|(T_c)_{i,a}| \leq 1$, that $\Theta$ is in the class of $h_u$, and that $e(s,b) = 0$ for $s \notin T\!T$. Then either $\langle P, \Theta \rangle = 0$, or there are $E \in \mathbb{N}$ and multiplicities $\alpha_\phi$ of the terms of type A and $\beta_\kappa$ of the terms of type B such that:

1. $\alpha_\phi \neq 0$ only if both colours $s - 2i$ and $s + 1 - 2j$ lie in $T\!T$, and $\beta_\kappa \neq 0$ only if $s \in T\!T$;
2. at every index $(s, b)$ the total degree in $y_{s,b}$ of the chosen terms is at most $e(s,b)$;
3. $D^{\beta} Q \neq 0$;
4. with $|\alpha| = \sum_\phi \alpha_\phi$ and $|\beta| = \sum_\kappa \beta_\kappa$,
$$|\langle P, \Theta \rangle| \leq p^{-\bigl(\gamma(p) \sum_{s \in T\!T} \alpha_s - |\alpha| - |\beta| - \Delta + \rho(p) \sum_s (\alpha_s + \lambda_s)\bigr)}.$$

Lean: `Formalism.InvariantFactorPaths.G7.Top.entryStar` (also `Formalism.InvariantFactorPaths.G7.EntryStar`).

*Proof (outline).* The pairing $\langle P, \Theta\rangle$ is linear in $\Theta$ and turns the factors $\mathrm{top}_{s,b}^{e(s,b)}$ into a coefficient of $\Theta$ after the shift by $\xi \cdot y$. The class of $h_u$ is stable under substitutions by integral series without constant term, so the shifted $\Theta$ is in the class of the shifted $h_u$. Up to degree $D$ the shifted $h_u$ equals the sum of the terms of types A and B, an integral series all of whose monomials have degree at least $p$ in the old variables, and $p$ times an integral series. A term bound for such a decomposition, combined with the degree count $\sum_a n(s,a,b) = \lambda_s$ for the monomials of $Q$ and the degree property of Hasse derivatives, gives either $\langle P, \Theta\rangle = 0$ or the choice of $E$, $\alpha$, $\beta$ with conditions 1 to 3 and a bound through the $p$-adic valuations of factorials. Legendre's inequality $v_p(m!) \geq m/(p - 1) - \mathrm{lg}(m)$ then gives the exponent in condition 4. $\square$

### Kernel bounds for theta series

Let $\varpi \in K$ with $\varpi^{p^2 - 1} = p$, and put $\lambda_\varpi(X) = \sum_n \varpi^{n-1} \ell_n X^n$, where $\ell_n$ are the coefficients of $\ell$. The *theta substitution* uses families $\omega_r, \omega^*_r : \mathbb{Z}/2\nu \to K$ ($r < \nu$) with $|\omega_r(s)|, |\omega^*_r(s)| \leq 1$, $|\omega_r(s+1) - \omega_r(s)^p| \leq 1/p$ (and the same for $\omega^*$), and $\sum_r \omega^*_r(a)\, \omega_r(b) = \delta_{ab}$ whenever $a \equiv b \pmod 2$. For a series $\Psi$ in variables $X_{\epsilon, r, a, b}$ ($\epsilon \in \{0, 1\}$) and a power series $\mu$, put
$$z_{0,r,a,b} = \sum_{s \text{ even}} \omega^*_r(s)\, x_{s,a,b}, \qquad z_{1,r,a,b} = \sum_{s \text{ odd}} \omega_r(s)\, x_{s,a,b},$$
and let $\vartheta(\Psi)(x) = \Psi\bigl(\varpi\, \mu(z(\varpi^{-1} x))\bigr)$.

A *frame* consists of $T\!T$, numbers of columns $C_s$ for each colour $s$, heights $h_{s,c} \leq r_0$ and column choices $I_{s,c}$. Its *frame jet* $J(\Theta)$ is the polynomial in independent entries $\tau_{s,i,a}$ obtained by pairing $\Theta$ with the product over $s$ and $c$ of the minors $\det(\sum_a \tau_{s,i,a}\, x_{s,a,I_{s,c}(i')})_{i, i' < h_{s,c}}$. Put $\alpha_s = \#\{c : h_{s,c} = 1\}$ if $s \in T\!T$ and $\alpha_s = 0$ otherwise, $\kappa_s = C_s - \alpha_s$ and $\lambda_s = \sum_c h_{s,c} - \alpha_s$, and define $\Delta$ as above. The *gain* and the *excess gain* are
$$\begin{aligned} \mathcal{G} &= \gamma(p) \sum_{s \in T\!T} \alpha_s - \sum_{s \in T\!T \text{ odd}} \sum_{e \geq 0} \min\Bigl(\frac{\alpha_s}{p^{2e+1}}, \kappa_{s + 2e + 1}\Bigr) - \Delta, \\ \mathcal{X} &= \sum_{s \in T\!T} \sum_{e \geq 0} \max\Bigl(\frac{\alpha_s}{p^{2e+1}} - \kappa_{s+2e+1}, 0\Bigr) [2e + 1 \notin D_s] - \Delta, \end{aligned}$$
where $D_s$ is the set of differences $(s' - s) \bmod 2\nu$ for $s' \in T\!T$ of the other parity.

**Theorem 8.4.7 (Kernel bounds).** Let $K_0$, $\sigma$, $F$ and $\beta$ satisfy the hypotheses of the cocycle theorem. Let $K$ be ultrametric of characteristic $0$ with an isometric embedding $j : K_0 \to K$. Let $\varpi$, $\omega$, $\omega^*$ be as above, $\mu$ a power series with $\mu(0) = 0$ and $\lambda_\varpi(\mu(X)) = X$, $U_0$ an integral series, and $\Phi$ a series with $\Phi(0) = 0$ and $\Phi \simeq \sum_{r,a,b} j(\beta)(X_{0,r,a,b}, X_{1,r,a,b})$. Put $\Theta = \vartheta(\exp(-\Phi)\, U_0)$. Then for every frame and every exponent $n$:

1. $|J(\Theta)_n| \leq p^{-\mathcal{X}}$;
2. $|J(\Theta)_n| \leq p^{-(\mathcal{G} - \sum_{s \in T\!T \text{ even}} \alpha_s)}$;
3. for every $i \geq 1$, $|p^{w_i}\, J(\Theta)_n| \leq p^{-\mathcal{G}}$, where $w_i = \sum_{s,c} w_{s,c}$ with $w_{s,c} = \min(h_{s,c}, i) - m_{s,c}$ for even $s$ and $w_{s,c} = m_{s,c}$ for odd $s$, and $m_{s,c}$ is the number of columns $b < i$ in the image of $I_{s,c}$.

Lean: `Formalism.InvariantFactorPaths.G7.kernel_bounds_generic` (also `Formalism.InvariantFactorPaths.G7.Top.kernel_from_k_one_k`, a second name).

*Proof.* By the cocycle theorem, $\beta \simeq G_{c, \sigma(c)}$ with $|c| \leq 1$ and $\sigma^2(c) = c$. A substitution result for theta series then shows that $\Theta(\varpi x)$ is in the class of $h_u$, with $u_s = -\sigma(c)$ for even $s$ and $u_s = c$ for odd $s$ (transported by $j$); here $|u_s| \leq 1$ since $\sigma$ preserves the closed unit ball. Three bounds for the frame jets of a series $\Psi$ with $\Psi(\varpi x)$ in this class, one for each conclusion, finish the proof. $\square$

**Remark 8.4.8 (Formalization).** The cocycle theorem is in [IsLawOfLog.lean](lean:Formalism/ThetaLogCoordinates/UniformThetaSubstitution/IsLawOfLog.lean#L98), and its proof in [NormLiftLeOne.lean](lean:Formalism/ThetaLogCoordinates/UniformThetaSubstitution/FrobeniusLiftNorms/NormLiftLeOne.lean#L32) combines Steps 0 to 5, which are stated in FirstDeriv.lean; we read these statements but not their proofs. The entry bound is in [StatementE.lean](lean:Formalism/ThetaLogCoordinates/UniformThetaSubstitution/StatementE.lean#L176), and its proof in NormLeOfDvd.lean was not opened beyond the list of inputs; the outline names the inputs by their statements. The kernel bounds are in [StatementGK.lean](lean:Formalism/ThetaLogCoordinates/UniformThetaSubstitution/StatementGK.lean#L104) and are proved in [EGaussK.lean](lean:Formalism/ThetaLogCoordinates/UniformThetaSubstitution/FrobeniusLiftNorms/EGaussK.lean#L222). The three frame jet bounds are taken from three named results whose proofs we did not open, so the last sentence of that proof is a description of their role. The name `kernel_from_k_one_k` is a plain alias, `:= kernel_bounds_generic` ([KernelFromKOneK.lean](lean:Formalism/ThetaLogCoordinates/UniformThetaSubstitution/KernelFromKOneK.lean#L16)). In the excess gain the bracket $[2e + 1 \notin D_s]$ sets the term to $0$ when $2e + 1 \in D_s$. The law $F$ need not be given as a formal group law: it is any integral series with logarithm $\ell$.
