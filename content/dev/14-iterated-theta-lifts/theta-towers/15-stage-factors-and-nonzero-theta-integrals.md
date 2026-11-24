---
title: Factors of stages and nonzero theta integrals
decls:
  - GlobalTheory.T.exists_factor_of_isStageC
  - GlobalTheory.StageFactor.theta_tower_stage_norm_factorization
  - GlobalTheory.T.theta_small_rank_stage_holds
  - GlobalTheory.StageSmall.theta_stage_of_small_rank
  - GlobalTheory.T.smallStage_thetaIntegral_nonzero_case
  - GlobalTheory.StageSmallNz.smallStage_thetaIntegral_of_ne_zero
  - GlobalTheory.T.definite_theta_lift_ne_zero
  - GlobalTheory.DefThetaNZ.exists_algebraic_function_definite_theta_ne_zero
  - GlobalTheory.DefThetaNZ.exists_algebraic_vector_definite_theta_ne
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Factors of stages and nonzero theta integrals

Every stage of the tower in [Section 3.14.6](/entry/tower-alt-bis/) has a factor: its two theta integrals factor through one injective map, up to a nonzero scalar on the first. The factor is built from four facts, and the hardest one is that the second theta integral of a stage is not $0$ at some polynomial function. This section proves that fact for stages whose second space is definite, by a density argument on the Fock model. The case of a stage whose second space is not definite is a separate input that we do not open here.

We keep the notation of Sections 11 and 14, the local inputs, [ThetaIntegralsAgree](/step/theta-integrals-agree-def/) and the [local matching](/step/local-matching-def/). For a triangle $X$ on $(A, A', W)$ the second theta integral $I'_t(P')$ of a polynomial function $P'$ on the Fock space of $(W, A')$ is a function on the group of $W$. Its kernel is integrable if the theta kernel of $P'$ at each point is integrable on the fundamental domain of $X$.

**Definition 3.15.1 (Factor).** Let $X$ be a triangle with index set $\mathcal T$. A function $\lambda$ on $\mathcal T$ is a factor of $X$ if $\lambda(t) \neq 0$ for all $t$ and there are a space $\Pi$, a surjective linear map $\pi$ on the polynomial functions of $(W, A)$, a linear map $\pi'$ on those of $(W, A')$, and injective linear maps $J_t$ on $\Pi$ with the following properties. All kernels of the first integral are integrable, and $I_t(P) = \lambda(t)\, J_t(\pi P)$. Whenever the kernel of $P'$ is integrable, $I'_t(P') = J_t(\pi' P')$. Some $P'$ with integrable kernel has $\pi'(P') \neq 0$. A factor gives constants of $X$ (the property $\mathrm{IsConst}$ of Section 8) when $\mathcal T$ is not empty, and two constants of a triangle with a factor differ by a scalar.

**Theorem 3.15.2 (Factor of a stage).** At large scale, for every Weil datum with a standard character and numbers at $\mu_0$, every square $(i, j)$, all $p'$, $q'$ and every triangle $X$ that is a stage with ranks $(p', q')$, there is a factor of $X$.

Lean: `GlobalTheory.StageFactor.theta_tower_stage_norm_factorization` (also `GlobalTheory.T.exists_factor_of_isStageC`, a second name).

*Proof.* Take the largest thresholds of four facts on a stage: the theta integrals converge, the kernels of the theta integrals have a characterization through the maps $\pi$ and $\pi'$, the stage is liftable (it gives $\lambda$ and the maps $J_t$), and [the second integral is not zero](/entry/theta-stage-of-small-rank/). A lemma assembles the four facts into a factor. $\square$

**Theorem 3.15.3 (Nonzero second integral).** At large scale, for every Weil datum with a standard character and numbers at $\mu_0$, every square, all $p'$, $q'$ and every stage $X$ with ranks $(p', q')$, there is a polynomial function $P'$ with integrable kernels such that $I'_t(P') \neq 0$ for every $t$.

Lean: `GlobalTheory.StageSmall.theta_stage_of_small_rank` (also `GlobalTheory.T.theta_small_rank_stage_holds`, a second name).

*Proof.* Take the larger thresholds of the case $q' = 0$ and of the case $q' > 0$. If $q' = 0$, the second space of the stage is definite at the real places, the theta kernels of a definite seesaw stage are integrable for every $P'$, and [Theorem 3.15.4](/entry/small-stage-theta-integral-of-ne-zero/) gives $P'$. If $q' > 0$, a separate result for large rank gives $P'$ with both properties. $\square$

**Theorem 3.15.4 (The definite case).** At large scale, for every Weil datum with a standard character and numbers at $\mu_0$, every square, every $p'$ and every stage $X$ with ranks $(p', 0)$ whose second kernels are all integrable, there is $P'$ with $I'_t(P') \neq 0$ for every $t$.

Lean: `GlobalTheory.StageSmallNz.smallStage_thetaIntegral_of_ne_zero` (also `GlobalTheory.T.smallStage_thetaIntegral_nonzero_case`, a second name).

*Proof.* Howe duality at the real places is part of the local inputs, and the local factors of the twisted triangles match. Take the larger thresholds of a seesaw dictionary for the stage (frames, signatures and the data at each index) and of the nonvanishing at the finite places. The dictionary gives frames of $A$, $A'$ and $W$, and $A'$ is positive definite at every real place, since $q' = 0$. The matching of local factors gives surjections $q$, $q'$ onto one space $\Pr$. For each index $t$, the transfer of Weil representations gives a match $(\Pi, \pi, \pi')$ of the triple at $t$, and the nonvanishing at the finite places gives a finite vector $y \neq 0$. So $\Pr$ is not $0$, and $\pi'(\mathrm{Fock}(f'_t, P')) \neq 0$ whenever $q'(P') \neq 0$.

If there is no index, take $P' = 0$; the claim is empty. Otherwise $\Pr \neq 0$; take $x \neq 0$ in $\Pr$ and $P_0$ with $q'(P_0) = x$. Suppose $I'_t(P_0) = 0$ for some $t$. The second integral of $P_0$ is the theta integral of the Fock vector $\mathrm{Fock}(f'_t, P_0)$. By [Theorem 3.15.6](/entry/exists-algebraic-function-definite-theta-ne-zero/) some Fock vector $\Phi$ has a nonzero theta integral. A vanishing result for definite small stages says the following: since the match is irreducible and $\pi'$ does not kill $\mathrm{Fock}(f'_t, P_0)$, the vanishing of its theta integral forces the theta integral to vanish on all Fock vectors. This contradicts the choice of $\Phi$. $\square$

The next two results work with one triple of Hermitian spaces $W$, $W_1$ and $X$ with Hecke characters $\alpha$, $\beta$ (the triple condition of [Section 3.11.3](/entry/real-quotient-complement-minor/)). The space $\mathrm{alg}$ of Fock functions is the span of the Fock vectors $\mathrm{Fock}(f, P)$ for finite Schwartz functions $f$ and polynomials $P$. For a Haar measure $\nu_1$ on the group of $W_1$ and a fundamental domain $\mathcal F_1$, the theta integral of $\Phi$ is

$$I(\Phi)(h) = \int_{\mathcal F_1} \theta_\Phi(g, h)\, d\nu_1(g).$$

**Lemma 3.15.5 (Polynomial vectors suffice).** Assume the local inputs. Let a triple of local models with Weil representations $\omega$, $\omega'$ satisfy the decay condition. If $\Phi'$ is in the Schwartz span and $I(\Phi') \neq 0$, then there is $\Phi_D$ in the span of the polynomial Fock vectors with $I(\Phi_D) \neq 0$.

Lean: `GlobalTheory.DefThetaNZ.exists_algebraic_vector_definite_theta_ne`.

*Proof.* Suppose that $I$ vanishes on all polynomial Fock vectors. Fix a point $h$. We prove $I(\Phi')(h) = 0$ by induction on the span. For a sum, a multiple or $0$ this follows from the linearity of $I$, using that the Weil representation preserves the Schwartz space and that the decay condition makes the integrals converge. For a pure tensor $f \otimes \varphi$ with an archimedean Schwartz function $f$, the map $f \mapsto I(f \otimes \varphi)(h)$ is continuous on the archimedean Schwartz space, so the set of $f$ where it vanishes is closed. It contains the polynomial Fock functions, which are dense. So it is the whole space. This contradicts $I(\Phi') \neq 0$. $\square$

**Theorem 3.15.6 (An algebraic function with nonzero theta integral).** Assume the local inputs, the agreement of theta integrals and the local matching. Let the character be standard. Let $W$, $W_1$ and $X$ form a triple with $\alpha$, $\beta$, let $W_1$ be positive definite at the real places, and let $\nu_1$, $\mathcal F_1$ be a Haar measure and a fundamental domain. For every match $(\omega_A, \omega_B, \Pi, \pi, \pi')$ of the triple there is $\Phi \in \mathrm{alg}$ for $(W_1, X)$ with

$$\int_{\mathcal F_1} \theta_\Phi\, d\nu_1 \neq 0.$$

Lean: `GlobalTheory.DefThetaNZ.exists_algebraic_function_definite_theta_ne_zero` (also `GlobalTheory.T.definite_theta_lift_ne_zero`, a second name).

*Proof.* Choose a Haar measure and a fundamental domain for $W$. A placewise seesaw triple over the Hermitian spaces gives local models of the triple, with Weil representations $\omega$, $\omega'$ and a dictionary to the global objects. The local matching gives a representation $R$ in this model. The agreement of theta integrals gives the decay condition and a Schwartz vector $\Phi'$ with $I(\Phi') \neq 0$. [Lemma 3.15.5](/entry/exists-algebraic-vector-definite-theta-ne/) gives a polynomial vector $\Phi_D$ with $I(\Phi_D)(h') \neq 0$ at some $h'$. The dictionary gives $\Phi \in \mathrm{alg}$ that corresponds to $\Phi_D$. The map from the unitary group of $X$ to the group of transposed Gram matrices is surjective, so $h' = e(h)$ for some $h$, and the theta integral of $\Phi$ at $h$ is the model integral of $\Phi_D$ at $h'$. So it is not $0$. $\square$

**Remark 3.15.7 (Formalization).** The theorem on an algebraic function ([ExistsAlgebraicFunctionDefiniteThetaNeZero.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/ExistsAlgebraicFunctionDefiniteThetaNeZero.lean#L64)) takes the definiteness of $W_1$ and the standard character and uses neither; both binders at line 71 are marked as unused. The vector lemma in the same file (line 24) has "definite" in its name, but no definite space appears in it. The factor theorem ([ThetaTowerStageNormFactorization.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/ThetaTowerStageNormFactorization.lean#L26)) speaks of a norm in its name, but no norm appears, and it has an empty variable section at lines 21 to 24. The name "of small rank" in [ThetaSmallRankStageHolds.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/ThetaSmallRankStageHolds.lean#L20) covers both the definite case and the case $q' > 0$. The definite case is in [SmallStageThetaIntegralNonzeroCase.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/SmallStageThetaIntegralNonzeroCase.lean#L25). We have not opened the four parts of the factor, the case $q' > 0$, the seesaw dictionary, the transfer of Weil representations, the vanishing result for definite stages, the density of polynomial Fock vectors or the continuity of theta integrals.
