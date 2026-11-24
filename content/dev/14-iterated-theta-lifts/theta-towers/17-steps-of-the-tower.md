---
title: The steps of the tower
decls:
  - GlobalTheory.T.witt_tower_constant_ratio_eq_bottom
  - GlobalTheory.SqTower.theta_tower_bottom_constant_ratio
  - GlobalTheory.T.witt_tower_norm_step_of_large_rank
  - GlobalTheory.SqStepBig.theta_tower_norm_step_large_rank
  - GlobalTheory.SqStepBig.theta_tower_step_norm_identity
  - GlobalTheory.ReBase.rebase_ratio_real_part
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The steps of the tower

The tower of [Section 3.14.6](/entry/tower-alt-bis/) goes down from the top stage of a square to a bottom triangle, one stage at a time. This section proves three of its inputs. The first is a step at large rank: the factor of a stage with ranks $(p+1, 0)$ is a step ratio times a Hecke $L$-value times the constants of a stage with ranks $(p, 0)$. The second is the last move: the constants of a stage with ranks $(0, 0)$ become constants of a bottom triangle after multiplication by a function whose values at $t$ and at $\mu_0$ differ by an away unit. The third compares the constants of two sets of characters before and after a change of base. All three are used in the proof of [the tower](/entry/tower-alt-bis/).

We keep the notation of Sections 14 and 15: a Weil datum $W$ with a standard character and numbers at $\mu_0$, a square $(i, j)$, stages with ranks $(p', q')$, the constants of a triangle, the factors of [Section 3.15.2](/entry/theta-tower-stage-norm-factorization/), the integer $Q_n(t)$ and away units. Let $L$ be the number field of the datum with its embedding $\sigma_0 : L \to \mathbb C$. Let $S_0$ be the finite set of places of the grid, and for $v \in S_0$ let $q_v$ be the absolute norm of $v$ and $c_v$ the exponent of the conductor at $v$.

**Definition 3.17.1 (Step ratio).** Two complex numbers $u_1$ and $u_0$ are in step ratio for $n$ if there are an away unit $b \in L$ for $n$ and, for each $v \in S_0$, integers $g_v$ and $g'_v$ that divide $q_v^{c_v}$, such that

$$u_1 = \sigma_0\Bigl(b \prod_{v \in S_0} \frac{g_v}{g'_v}\Bigr)\, u_0.$$

A step ratio is an away unit up to numbers that only involve the primes of $S_0$. The tower collects one step ratio for each stage, and the bound on square constants only needs to control such numbers.

**Definition 3.17.2 (Step factor).** For an index $t$, a base that fits $t$, ideals $\mathfrak b$ and $\mathfrak c$ of the field $E$ and a complex number $s$, the step factor $\mathrm{st}_t(s)$ is the product of the values of the Hecke character $\nu_t$ of the stage at $\mathfrak b$ and at $\mathfrak c$, of the values of local characters at the split places of $S_0$, and of local epsilon factors at $s$. We have not unfolded all of its terms; we use it only through the two theorems below.

Let $L^{S_0}(s, \nu_t)$ be the partial Hecke $L$-function of $\nu_t$, with the Euler factors at $S_0$ removed.

**Theorem 3.17.3 (Step identity).** Assume the local inputs, the agreement of theta integrals [ThetaIntegralsAgree](/step/theta-integrals-agree-def/) and the [local matching](/step/local-matching-def/). At large scale the following holds for every Weil datum $W$ with a grid choice, a standard character and numbers at $\mu_0$. Let $X$ be a stage with ranks $(p+1, 0)$, let $\lambda$ be a factor of $X$, and let $\mathrm{rank}\, A = \mathrm{rank}\, A' + 2e$. Then there are a stage $Y$ with ranks $(p, 0)$ and constants $c$ of $Y$ with this property. For each $t$ there are a base that fits $t$, units $e_1$, $e_2$ and $s$, ideals $\mathfrak b$ and $\mathfrak c$, a constant $C$ and an away unit $\zeta$ for $Q_n(t)$ such that

$$\lambda(t) = C\, \zeta\, \mathrm{st}_t(1 - e)\, L^{S_0}(e, \nu_t)\, c(t),$$

and an identity of the same form holds at $\mu_0$ with no away unit.

Lean: `GlobalTheory.SqStepBig.theta_tower_step_norm_identity`.

*Proof.* The rank of $A$ exceeds the rank of $A'$ by $2e$, and the first rank of the stage is $p + 1 > 0$. So $A$ splits off a hyperbolic plane, and the complement gives the stage $Y$ with ranks $(p, 0)$. Choose self-dual oriented models for $X$ and $Y$ and rebase the geometry of $X$ to the geometry of $Y$. The agreement of theta integrals contains the comparison of constants for signatures $(a, b + 2)$ and $(a, b)$: the two constants differ by an explicit step factor times the partial $L$-value $L^{S_0}(e, \nu_t)$. Apply it to the factor $\lambda$ of $X$, which writes the theta integrals of $X$ through one injective map. The change of models and the rebasing contribute the constant $C$ and, at $t$, an away unit $\zeta$ for $Q_n(t)$, since the lattices at $t$ and at $\mu_0$ differ only at the primes of $Q_n(t)$. $\square$

**Theorem 3.17.4 (Step at large rank).** Under the assumptions of the step identity, at large scale the following holds for every such Weil datum. Let $X$ be a stage with ranks $(p+1, 0)$, let $\lambda$ be a factor of $X$, and let $\mathrm{rank}\, A = \mathrm{rank}\, A' + 2e$. Let $\Lambda_t$ be a Hecke $L$-function of $\nu_t$ for each $t$. Then there are a stage $Y$ with ranks $(p, 0)$, constants $c$ of $Y$ and a function $y$ with $y(t) \neq 0$,

$$\lambda(t) = y(t)\, \Lambda_t(e)\, c(t)$$

for every $t$, and $y(t)$, $y(\mu_0)$ in step ratio for $Q_n(t)$.

Lean: `GlobalTheory.SqStepBig.theta_tower_norm_step_large_rank` (also `GlobalTheory.T.witt_tower_norm_step_of_large_rank`, a second name).

*Proof.* Take $Y$, $c$ and the data at $t$ from [Theorem 3.17.3](/entry/theta-tower-step-norm-identity/). The partial $L$-function differs from the complete one by the Euler factors at $S_0$:

$$L^{S_0}(e, \nu_t) = \Lambda_t(e) \prod_{v \in S_0} E_v(e, \nu_t),$$

where each $E_v$ is the inverse of a local Euler factor, a ratio of numbers that divide a power of $q_v$. Put $y(t) = C\, \zeta\, \mathrm{st}_t(1 - e) \prod_{v \in S_0} E_v(e, \nu_t)$. The step factor at $t$ divided by the step factor at $\mu_0$ is a unit times a quotient of Gauss sums, and a Gauss sum at $v$ has absolute norm a power of $q_v$. So the ratio $y(t)/y(\mu_0)$ is $\sigma_0$ of an away unit for $Q_n(t)$ times quotients of divisors of $q_v^{c_v}$. This is a step ratio. The values $y(t)$ are not $0$ since $\lambda(t) \neq 0$. $\square$

**Theorem 3.17.5 (Ratio at the bottom).** Assume the local inputs, the agreement of theta integrals and the local matching. At large scale the following holds for every Weil datum with a grid choice, a standard character and numbers at $\mu_0$. Let $X$ be a bottom triangle at $(i, j)$, and let $Y$ be a stage with ranks $(0, 0)$ with constants $c$. Then there is a function $v$ on the indices such that $v\, c$ are constants of $X$, $v(t) \neq 0$, and

$$v(t) = \zeta\, v(\mu_0)$$

for an away unit $\zeta$ for $Q_n(t)$, for every $t$.

Lean: `GlobalTheory.SqTower.theta_tower_bottom_constant_ratio` (also `GlobalTheory.T.witt_tower_constant_ratio_eq_bottom`, a second name).

*Proof.* We make four moves. First, a stage with ranks $(0, 0)$ is definite, and its constants transport to a definite bottom with the same constants. Second, the lattices of this bottom and of $X$ differ, and a change of lattices multiplies constants by a function $v_1$ whose values are away units for $Q_n(t)$ up to their value at $\mu_0$. Third, a change of frames at stage zero gives a function $v_2$ of the same kind. Fourth, the constants of the two towers that end at $X$ differ by a factor $\kappa$ that does not depend on $t$. Put $v = \kappa\, v_2\, v_1$. Then $v\, c$ are constants of $X$, each factor is not $0$, and the away units of $v_1$ and $v_2$ multiply to an away unit for $Q_n(t)$, since away units form a group. $\square$

The last result compares two sets of characters on one geometry. Let $G$ be a geometry of a triangle, and let $G'$ be its rebasing along spaces $V$, $V'$ and a datum $Z$. For a set of characters $X_a$ on $G$ with Hecke character $\nu_a$, a constant of $X_a$ is a number $c_a$ for which the theta integrals of $X_a$ on $G$ are $c_a$ times the standard integral; let $d_a$ be a constant of the same characters on $G'$.

**Theorem 3.17.6 (Rebasing and ratios).** Assume the local inputs and the agreement of theta integrals. Let $X_a$ and $X_b$ be two sets of characters with Hecke characters $\nu_a$ and $\nu_b$, matched on $G$ with one set of real maps and on $G'$ with a second set. Let $c_a$, $c_b$ be constants of $X_a$, $X_b$ on $G$ and $d_a$, $d_b$ constants on the rebased geometry $G'$. Then there is an idele $k$ such that

$$d_a\, c_b = \frac{\nu_a(k)}{\nu_b(k)}\, d_b\, c_a.$$

Lean: `GlobalTheory.ReBase.rebase_ratio_real_part`.

*Proof.* The local inputs give a local isomorphism of the Weil representations under the rebasing, with a finite scalar $l_0$, and the rebasing is given by $l_0$ and an idele $\kappa$ that conjugates the Cartan involution of $G$ to that of $G'$. The real maps of a geometry are unique, so this conjugation fixes the comparison at the real places. A constant of a set of characters on $G'$ is then $l_0\, \nu(\kappa)$ times a constant on $G$, with the same $l_0$ and $\kappa$ for every set of characters:

$$d_a = l_0\, \nu_a(\kappa)\, c_a, \qquad d_b = l_0\, \nu_b(\kappa)\, c_b.$$

Multiply the first identity by $c_b$ and the second by $c_a \nu_a(\kappa)/\nu_b(\kappa)$; the right sides agree. Take $k = \kappa$. $\square$

**Remark 3.17.7 (Formalization).** The ratio at the bottom ([WittTowerConstantRatioEqBottom.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/WittTowerConstantRatioEqBottom.lean#L18)) has all thresholds $0$, so its "large scale" is empty, and it drops its three hypotheses (the local inputs, the agreement of theta integrals and the local matching) at once; its second name is at line 55. The file of the step at large rank has an empty namespace block at lines 23 to 25 ([WittTowerNormStepOfLargeRank.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/WittTowerNormStepOfLargeRank.lean#L23)); the step identity is at line 76, the step at large rank at line 173 and its second name at line 222. The names speak of norms and of a Witt tower, but the statements are about factors and constants of stages. The rebasing theorem ([DvReBaseMain.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/DvReBaseMain.lean#L117)) is named for a real part, but no real part appears in it. We have not unfolded the step factor, the self-dual oriented models, the transport to a definite bottom, the change of lattices or the change of frames.
