---
title: Theta lifts keep cusp forms
decls:
  - GlobalTheory.ColTypeLift.columnLift_isTypeAt_place
  - GlobalTheory.T.columnLift_hasTypeAtPlaces
  - GlobalTheory.CuspSmoothLift.cuspidal_lift_smooth_at_of_cuspidal_lift
  - GlobalTheory.T.cuspidal_lift_smooth_at_cusps
  - GlobalTheory.FlipRun.cuspStep_of_large_flipRun
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Theta lifts keep cusp forms

This section proves that the theta lifts along the arrows of a grid converge on cusp forms and send cusp forms of the type of the source to cusp forms of the type of the target, for every theta function. We assume this for test vectors built from Fock vectors. The passage to all theta functions uses the approximation of [Theorem 3.2.4](/entry/cusp-type-lift-approx-fock-space/). The result gives the cusp step of the flips along the grid, [Theorem 3.3.6](/entry/cusp-step-of-large-flip-run/), which the flips of Section 5 and the iterated integrals of Section 4 use.

We keep the notation of the previous sections and fix the local inputs of [ThetaLocalInputs](/step/theta-local-inputs-def/). A grid $G$ has five kinds of arrows, each with a Weil representation, a measure and a fundamental domain on its source:

1. the right arrows $(i, j) \to (i + 1, j)$ for $i < m$;
2. the down arrows $(i, j + 1) \to (i, j)$ for $j < m$;
3. the arrows $P_i \to P_{i+1}$ along the row, for $i < m$, with the complex conjugate of the theta kernel;
4. the arrows $P_{i+1} \to P_i$ along the row;
5. the arrows $X_j \to X_{j+1}$ along the column, for $j < m$.

For each arrow, a test vector built from a Fock vector $f$ and a polynomial $p$ gives a theta function $\mathrm{fock}(f, p)$, as in [the previous section](/entry/cusp-type-lift-approx-fock-space/). Each arrow also carries a map $\iota_p$ from the smooth vectors of the source model to those of the target model. For a node $N$, let $\mathcal C_N$ be the space of cusp families of $N$.

**Definition 3.3.1 (Size conditions).** A datum meets the size conditions if its rank $r$ satisfies $r > 1800$, and at each real place $\tau$ the weights $b_0 < b_1 < \cdots$ of the datum satisfy $b_{j+1} - b_j > 2 N^3$ for $j + 1 < m$, where $N$ is the bound of the datum.

**Definition 3.3.2 (Lifts of Fock vectors keep cusp forms).** We say that lifts of Fock vectors keep cusp forms if the following holds for every datum that meets the size conditions, every real datum $R$ with the base conditions of the rows and every grid $G$ for $R$ with the grid conditions. For each arrow $N \to N'$ of the five kinds, each Fock vector $f$ of the arrow and each cusp family $F \in \mathcal C_N$, there is a cusp family $F' \in \mathcal C_{N'}$ such that for every polynomial $p$, every smooth vector $v$ of the source and every point $h$ of the target, the integral

$$\Theta_{\mathrm{fock}(f, p)}\bigl(F(v)\bigr)(h) = \int_{\mathcal F} \theta_{\mathrm{fock}(f, p)}(h, g)\, F(v)(g)\, d\nu(g)$$

converges absolutely and equals $F'(\iota_p(v))(h)$.

So the lift of a cusp family by a Fock vector is again a cusp family, in a way that is compatible with the vectors. The definition says nothing about other theta functions. The next three results extend it.

**Lemma 3.3.3 (Column lifts keep the type).** Assume that lifts of Fock vectors keep cusp forms, and that the datum meets the size conditions. Let $j < m$, let $\Phi$ be a theta function of the column arrow $X_j \to X_{j+1}$, and let $\varphi$ be a cusp form of the type of $X_j$ such that the integrand of $\Theta_\Phi(\varphi)$ is integrable for each point of the target. Then $\Theta_\Phi(\varphi)$ has the type $\sigma_\tau$ of $X_{j+1}$ at every real place $\tau$.

Lean: `GlobalTheory.ColTypeLift.columnLift_isTypeAt_place` (also `GlobalTheory.T.columnLift_hasTypeAtPlaces`, a second name).

*Proof.* The spaces $X_j$ and $X_{j+1}$ of the column are positive definite at every real place. For a definite unitary group, the cusp forms of a fixed type form a space that decomposes into finitely many pieces: $\varphi = \sum_{l=1}^n F_l(w_l)$ with cusp families $F_l$ and vectors $w_l$. The theta lift of each term is smooth and has the type of $X_{j+1}$, and the lift is linear. A finite sum of functions of type $\sigma_\tau$ at $\tau$ has type $\sigma_\tau$ at $\tau$. $\square$

**Theorem 3.3.4 (All theta lifts keep cusp forms).** Assume that lifts of Fock vectors keep cusp forms. Let $D$ be a datum that meets the size conditions, $R$ a real datum with the base conditions of the rows, and $G$ a grid for $R$ with the grid conditions. Let $N \to N'$ be an arrow of one of the five kinds, and let $\Phi$ be any theta function of the arrow. Then for every cusp form $\varphi$ of the type of $N$:

1. the integrand $g \mapsto \theta_\Phi(h, g)\varphi(g)$ is integrable on the fundamental domain for every $h$;
2. $\Theta_\Phi(\varphi)$ is a cusp form of the type of $N'$, that is, it is smooth automorphic, cuspidal and of type $\sigma_\tau$ at every $\tau$.

Lean: `GlobalTheory.CuspSmoothLift.cuspidal_lift_smooth_at_of_cuspidal_lift` (also `GlobalTheory.T.cuspidal_lift_smooth_at_cusps`, a second name).

*Proof.* We treat each kind of arrow, and on each arrow the four parts of the conclusion in turn.

Integrability. A cusp form is rapidly decreasing, by the input on rapid decay of cusp forms. The theta kernel grows at most like a power of the height function, as in the proof of [Theorem 3.2.3](/entry/cusp-form-approx-by-lift-of-type/). The fundamental domain has finite volume. So the integrand is integrable.

Smooth automorphic. The same decay lets one differentiate under the integral sign, and the kernel is automorphic in $h$. So the lift is smooth and of moderate growth, and it is $\mathfrak z$-finite. On the column arrows the target is positive definite at each real place, and smoothness follows from that.

Cuspidal. Let $C$ be a compact set of the target. By [Theorem 3.2.4](/entry/cusp-type-lift-approx-fock-space/), $\Theta_\Phi(\varphi)$ is a uniform limit on $C$ of finite sums of lifts $\Theta_{\mathrm{fock}(f_l, p_l)}(F_l(v_l))$. By the assumption on Fock vectors, each term is a value of a cusp family of the target, so it is cuspidal. A constant term is an integral over a compact quotient, so a locally uniform limit of cusp forms has vanishing constant terms. On the column arrows the target is positive definite, so it has no proper parabolic subgroups over $F$ and every automorphic function is cuspidal.

Type. On the right, down and row arrows, the type passes to the limit by the same approximation and the inputs on discrete series, Harish-Chandra modules and Casselman-Wallach globalization: a locally uniform limit of automorphic forms of a fixed discrete series type keeps that type. On the column arrows we use [Lemma 3.3.3](/entry/column-lift-is-type-at-place/). $\square$

The cusp step is the form of this theorem that the flips use. It is stated for the choices of the row at a large scale, which we now define.

**Definition 3.3.5 (At large scale).** Let $Q$ be a property of choices of the row. We say that $Q$ holds at large scale if there is $C_{F,0}$ such that for all $\varepsilon > 0$ and $C_F \ge C_{F,0}$ there is $x_0$ with the following property. For every datum $D$, every large datum with exponent $\varepsilon$ and $x \ge x_0$, every finite group $\Gamma$, every family $A$, every number field $K_s$, every real datum $R$ and every face $F$ in a Hida setting, and every choice $c$ for $R$ that meets its conditions and is at scale $(C_F, b)$, the property $Q(c)$ holds.

A choice $c$ fixes a grid, a Weil datum $W$ and a real matching $\rho$. A volume datum $M$ on the grid gives a measure and a fundamental domain at each node, and it may be good at an index $t$. We have not unfolded the choices, the faces, the volume data or the condition to be good at $t$.

**Theorem 3.3.6 (Cusp step along the grid).** Assume that lifts of Fock vectors keep cusp forms. Then the following holds at large scale. Let $c$ be a choice, $t$ an index and $M$ a volume datum good at $t$. Let $a$ be a right or down arrow of the grid at $t$, let $e$ be an idempotent sum over the local places of $t$, and let $\phi$ and $f$ be local vectors on the pair of $a$ for $e$ and the vacuum of $\rho$. Then for every polynomial $Q$ on the pair and every listed cusp form $F$ on the source of $a$, the lift of $F$ with the test vector $\mathrm{fock}(f, Q)$ converges, and the lift is a listed cusp form on the target of $a$.

Lean: `GlobalTheory.FlipRun.cuspStep_of_large_flipRun`.

*Proof.* By [Theorem 3.3.4](/entry/cuspidal-lift-smooth-at-of-cuspidal-lift/), all theta lifts along the grid keep cusp forms. From this, one lemma gives the statement for the right arrows and one for the down arrows. Each holds at large scale with the thresholds $C_{F,0} = 0$ and $x_0 = 0$. A property that holds at large scale for each of two statements holds for their conjunction, with the larger thresholds. A grid arrow is a right arrow or a down arrow, and we apply the lemma for its case. $\square$

**Remark 3.3.7 (Formalization).** The condition that lifts of Fock vectors keep cusp forms is not new: it is proved from the local inputs elsewhere, and the row properties of Section 6 use that proof. In the theorem on all theta lifts, this condition is used only for the cuspidal part and the type. The integrability and smoothness lemmas take it and do not use it, and on the column arrows cuspidality uses neither the condition nor $\varphi$. In the cusp step the words "large" and "flip run" do no work: both case lemmas hold with thresholds $0$ ([CuspStepOfLargeFlipRun.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/CuspStepOfLargeFlipRun.lean#L15)). Its second name at line 34 has the same statement. The local vectors, the listed cusp forms and the convergence condition are not unfolded.
