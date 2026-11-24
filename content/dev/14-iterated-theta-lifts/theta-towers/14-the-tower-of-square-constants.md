---
title: The tower of square constants
decls:
  - GlobalTheory.SqTower.tower_alt_bis
  - GlobalTheory.T.witt_tower_top_stage_theta_norm_formula
  - GlobalTheory.SqTower.theta_tower_top_stage_norm_eq
  - GlobalTheory.T.theta_square_norm_comparison
  - GlobalTheory.SqCompare.theta_square_comparison
  - GlobalTheory.T.regConst_eq_away_unit_mul_factor
  - GlobalTheory.ThetaRegularizationComparison.regulator_constant_eq
  - GlobalTheory.T.thetaFlip_involutive_correspondence
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The tower of square constants

A square of the grid at $(i, j)$ compares two routes of theta lifts from the space $V_{i,j+1} \oplus V_{i+1,j}$: a big route to $V_{i+1,j+1}$ and a small route to $V_{i,j}$. The ratio of the two theta integrals is the square constant. This section proves the tower: the ratio of the square constants at an index $t$ and at the base point $\mu_0$, times a product of ratios of Hecke $L$-values, is an away unit times step ratios times the ratio of the constants of a bottom triangle times a second product of ratios of $L$-values. The tower is one of the twelve joined estimates of [Section 3.9.3](/entry/square-top-term-joined-estimates/), and it sits under the step [the hypotheses are not empty](/step/nonempty-hyps/).

We keep the notation of Sections 8, 10 and 11, the local inputs, [ThetaIntegralsAgree](/step/theta-integrals-agree-def/) and the [local matching](/step/local-matching-def/). Put $p = \lfloor (m - (j+1))/2 \rfloor$, $q = \lfloor (m - j)/2 \rfloor$ and let $e$ be the top exponent of the stage. A number $\zeta$ of the field $L$ is an away unit for an integer $n$ if $\zeta n^k = a$ for some $k$ and some integer $a$ of $L$ that divides a power of $n$. Away units for $n$ form a group.

**Definition 3.14.1 (Square constants).** Fix a Weil datum $W$, frames $B$ of the grid and a real match $\rho$. Let $t$ be an index and $(i, j)$ a square. For a volume datum $M$ at $t$ with fundamental domains $\mathcal F$ and measures $\nu$, and theta data $\Theta$, $\Theta'$ matched at $t$, write $k_{\mathrm{big}}(g, g_1)$ and $k_{\mathrm{small}}(g, g_1)$ for the kernels of the two routes, and $z \cdot k$ for a finite sum of translates with degree $\deg z$. A complex number $c$ is a square constant at $t$ if

$$\deg z \int_{\mathcal F} k_{\mathrm{big}}(g, g_1)\, d\nu = c \int_{\mathcal F} z \cdot k_{\mathrm{small}}(g, g_1)\, d\nu$$

for all $M$, $\Theta$, $\Theta'$, $z$, $g$ and $g_1$ for which both integrands are integrable. The square is nonzero at $t$ if the right side integral is not $0$ for some such data. A number $c$ is a regularized constant at $t$ if for all $M$, $\Theta$, $\Theta'$, $g$ and $g_1$ there is $z$ with $\deg z \neq 0$, both integrands integrable, and the same identity.

A stage of a tower with ranks $(p', q')$, $p' \le p$ and $q' \le q$, is a triangle $X$ on $(A, A', W)$ such that $\mathrm{rank}\, A + 2p = \mathrm{rank}\, V_{i+1,j+1} + 2p'$, $\mathrm{rank}\, A' + 2q = \mathrm{rank}\, V_{i,j} + 2q'$, the indices of $A$, $A'$ and $W$ are negative of sizes $p'$, $q'$ and $p' + q'$, and the characters of $X$ are those of the square. A factor $\lambda$ of a triangle is a function with $\lambda(t) \neq 0$ for which the two theta integrals factor through one injective map $J_t$, as $I_t = \lambda(t) J_t \circ \pi$ and $I'_t = J_t \circ \pi'$; see [Section 3.15.2](/entry/theta-tower-stage-norm-factorization/). A top triangle is a triangle on $(V_{i+1,j+1}, V_{i,j}, V_{i,j+1} \oplus V_{i+1,j})$ whose lattices and characters are those of the grid.

**Theorem 3.14.2 (Flip at the top stage).** At large scale, for every Weil datum, every top triangle $X$ that is a stage with ranks $(p, q)$, and every choice of grid frames on the four spaces, there is a function $\kappa$ on the indices with $\kappa(t) \neq 0$ and $\kappa(t) = \zeta_t\, \kappa(\mu_0)$ for an away unit $\zeta_t$ for $Q_n(t)$, with this property. Let $M$ be a volume datum at $t$ whose measures are $s$ and $s'$ times those of $X$. Let $(\Pi, \pi, \pi')$ be a match of the Weil representations at $t$, and let flip data of depth at most $n$ give Fock vectors $\tau$ and $\tau'$. If $P$, $P'$ and $g$ satisfy $\pi'(\mathrm{Fock}(f'_t, P')) \neq 0$ and $\pi(\mathrm{Fock}(f_t, P)) = g\, \pi'(\mathrm{Fock}(f'_t, P'))$, then

$$s\, \pi(\mathrm{Fock}(\tau, P)) = \kappa(t)\, s'\, g\, \pi'(\mathrm{Fock}(\tau', P')).$$

Lean: `GlobalTheory.T.thetaFlip_involutive_correspondence`.

*Proof.* The dictionary of theta parameters gives bijections $\sigma$ and $\sigma'$ of the parameters of the two routes. Uniqueness of the stage gives an element $E$ and a constant. A move of the frames gives a point $h$, constants $c_A$ and $c_B$ and a point $y$; the standard zeta lemma gives a point $x$. The measures differ by a ratio $s_0$, and the level volumes by $c_1$. Put

$$\kappa(t) = \frac{s_0\, c_B\, \xi_t(y)}{c_A\, c_1\, u(t)}, \qquad u(t) = \prod_w \nu(x_w).$$

The flip relation then follows from the move relation on Fock vectors. The factor $u(t)$ and the value $\xi_t(y)$ are away units times their values at $\mu_0$, by the arithmetic of $\nu$ and the imaginary part of $\xi$. $\square$

**Theorem 3.14.3 (Regularized constants).** At large scale, for every Weil datum with a standard character and numbers at $\mu_0$, every tied real match $\rho$, and every top triangle $X$ that is a stage with ranks $(p, q)$ and has a factor $\lambda$, there is $\kappa$ with the away property above such that every regularized constant $c_0$ at $t$ satisfies $c_0 = \kappa(t) \lambda(t)$.

Lean: `GlobalTheory.ThetaRegularizationComparison.regulator_constant_eq` (also `GlobalTheory.T.regConst_eq_away_unit_mul_factor`, a second name).

*Proof.* Take the largest thresholds of the dictionary of theta parameters, [Theorem 3.14.2](/entry/theta-flip-involutive-correspondence/) and the matching of finite data at each stage, and take $x \ge 12^{5/\varepsilon}$, so that each square is standing. The flip theorem gives $\kappa$. Fix $t$ and a regularized constant $c_0$. The local factors of the twisted triangles match, which gives surjections $q$, $q'$ onto one space, and the factor gives $J_t$ and a vector $P_0$ with $\pi'(P_0) \neq 0$. For a volume datum, flip data and points $g$, $g_1$ with a nonzero integral, square identities reduce the comparison to a match $(\Pi, \pi, \pi')$, and the finite data give $\gamma \neq 0$ with $\pi(\mathrm{Fock}(f_t, P_1)) = \gamma\, \pi'(\mathrm{Fock}(f'_t, P_0))$. The measures of $M$ are $s$ and $s'$ times those of $X$. A regularized comparison of theta integrals gives $c \neq 0$ such that $\deg z\, I(\Phi) = c\, g\, I'(z \cdot \Phi')$ whenever $\pi(\Phi) = g\, \pi'(\Phi')$. Apply it twice, once to the vectors of the factor and once to the flipped vectors, and compare with the identity of $c_0$. Cancel the nonzero vector $q'(\sigma' P_0)$ in the tensor product. This gives $c_0 = \kappa(t) \lambda(t)$. $\square$

**Theorem 3.14.4 (Square constants at the top).** Under the assumptions of the previous theorem, but with any real match $\rho$, there is $\kappa$ with the away property such that every square constant $c'$ at $t$ of a nonzero square satisfies $c' = \kappa(t) \lambda(t)$.

Lean: `GlobalTheory.SqCompare.theta_square_comparison` (also `GlobalTheory.T.theta_square_norm_comparison`, a second name).

*Proof.* Take the largest thresholds of three results. The first gives a tied real match $\rho_0$ and a regularized constant $c_0$ at every index for $\rho_0$. The second, the separation at the real places, gives $l \neq 0$ with $c' = l\, c_0$ for every square constant $c'$ for $\rho$ and every regularized constant $c_0$ for $\rho_0$. The third is [Theorem 3.14.3](/entry/regulator-constant-eq/) for $\rho_0$, which gives $\kappa_0$ with $c_0 = \kappa_0(t) \lambda(t)$. Put $\kappa = l\, \kappa_0$. Since $l$ does not depend on $t$, $\kappa$ has the away property with the same units. $\square$

**Theorem 3.14.5 (Top stage).** At large scale, for every Weil datum with a standard character and numbers at $\mu_0$, every real match and all $i$, $j$, there are a top triangle $X$ that is a stage with ranks $(p, q)$, constants $c$ of $X$ (the property $\mathrm{IsConst}$ of Section 8), and $\kappa$ with the away property, such that every square constant $c'$ at $t$ of a nonzero square satisfies $c' = \kappa(t)\, c(t)$.

Lean: `GlobalTheory.SqTower.theta_tower_top_stage_norm_eq` (also `GlobalTheory.T.witt_tower_top_stage_theta_norm_formula`, a second name).

*Proof.* Take the largest thresholds of the existence of a top triangle for a square tower, of the [existence of a factor](/entry/exists-factor-of-is-stage-c/) and of [Theorem 3.14.4](/entry/theta-square-comparison/). The first gives $X$; the second gives a factor $\lambda$; the third gives $\kappa$. A factor gives constants when the tuples are not empty, so take $c = \lambda$. $\square$

**Theorem 3.14.6 (The tower).** Assume the local inputs, the agreement of theta integrals, the local matching and $\mathrm{LNe}$. At large scale the following holds. Let $W$ be a Weil datum with a standard character and numbers at $\mu_0$, let $c$ and $c_0$ be square constants of nonzero squares at $t$ and $\mu_0$, let $X$ be a bottom triangle with constants $c_*$, and let $\Lambda$ and $\Lambda_0$ be $L$-functions of $\nu_t$ and $\nu_{\mu_0}$. Then there are step ratios $u_k$ for $k < p + q$ and an away unit $\zeta$ for $Q_n(t)$ with

$$\begin{aligned} \frac{c}{c_0} \prod_{k < q} \frac{\Lambda(e+k+1)}{\Lambda_0(e+k+1)} &= \zeta \prod_k u_k\, \frac{c_*(t)}{c_*(\mu_0)} \\ &\quad \cdot \prod_{k < p} \frac{\Lambda(e+q-k)}{\Lambda_0(e+q-k)}. \end{aligned}$$

Lean: `GlobalTheory.SqTower.tower_alt_bis`.

*Proof.* Take the largest thresholds of the top stage, the existence of factors, the steps of the tower at small and at large rank, the ratio of constants at the bottom, and $\mathrm{LNe}$. By uniqueness of $L$-functions, $\Lambda$ and $\Lambda_0$ are the $L$-functions that $\mathrm{LNe}$ gives. The top stage gives a triangle $X_1$, constants $c_T$ and $\kappa_T$ with $c = \kappa_T(t)\, c_T(t)$ and $c_0 = \kappa_T(\mu_0)\, c_T(\mu_0)$. A factor of $X_1$ shows $c_T(t) \neq 0$. The descent, by induction on the stages, gives a last stage $Y$ with constants $c_Y$, step ratios $u_k(t)$ and $\kappa$ with

$$\begin{aligned} c_T(t) \prod_{k<q} \Lambda_t(e+k+1) &= \kappa \prod_{k<p+q} u_k(t)\, c_Y(t) \\ &\quad \cdot \prod_{k<p} \Lambda_t(e+q-k). \end{aligned}$$

The ratio of constants at the bottom gives $v$ with $v(t) = \zeta_v\, v(\mu_0)$ for an away unit $\zeta_v$, such that $v\, c_Y$ are constants of $X$. Two constants of a triangle with a factor differ by a scalar, so $c_*(t) = (a/b)\, v(t)\, c_Y(t)$. The values $\Lambda_{\mu_0}(n)$ for $1 \le n$ up to the half rank are not $0$ by $\mathrm{LNe}$, so both products at $\mu_0$ and $c_Y(\mu_0)$ are not $0$. Take the step ratios $u_k(t)/u_k(\mu_0)$ and $\zeta = \zeta_T \zeta_v^{-1}$. Divide the identity at $t$ by the identity at $\mu_0$. $\square$

**Remark 3.14.7 (Formalization).** The tower ([TowerOfThetaMatching.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TowerOfThetaMatching.lean#L32)) has the name "alt bis", empty variable sections at lines 23 to 28, and a renaming at line 111; the descent and its helpers are in [TowerOfThetaMatching.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TowerOfThetaMatching.lean#L99). The statement of the tower is defined in [NormSmall.lean](lean:Development/AbelianVarietyTheory/Statements/PlaceShiftStatements/NormSmall.lean#L128). In the comparison of square constants ([ThetaSquareNormComparison.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/ThetaSquareNormComparison.lean#L17)) the nonzero square hypothesis is not used, and the combinators that join three thresholds appear twice under two names. The names speak of norms ("norm comparison", "norm formula", "norm eq") and of a regulator ([RegConstEqAwayUnitMulFactor.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/RegConstEqAwayUnitMulFactor.lean#L51)), but the statements are about square constants and regularized constants. The flip theorem ([ThetaFlipInvolutiveCorrespondence.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/ThetaFlipInvolutiveCorrespondence.lean#L164)) is named for an involution, but nothing involutive appears in it. We have not opened the dictionary of theta parameters, the uniqueness of stages, the steps of the tower, the separation at the real places or the regularized comparison of integrals.
