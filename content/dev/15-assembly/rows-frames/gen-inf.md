---
id: gen-inf
title: A form with zero theta lift has zero downward integrals against theta functions of finite type
kind: theorem
decl: GlobalTheory.GenReal.genInf
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ThetaLiftGenerationAtRealPlaces
covers: 382
status: drafted
drafted_by: writer@claude
---
This theorem proves `GenInf`, the real-place half of the generation argument; [`genFin`](/entry/gen-fin/) is the finite half. It has two users: [`liftRows_injective_and_typeProperties_of_nonvanishing`](/entry/lift-rows-injective-and-type-properties-of-nonvanishing/), in step 3 of the proof of `TypeNZ`, and its second name `thetaLift_generation_at_realPlaces`. Both lie under [`hypotheses_nonempty_of_unramified_exponents_alt`](/proof/unitary-hypotheses/), in branch 1 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/).

## Statement

Use the notation of [`genFin`](/entry/gen-fin/): the theta map $\theta_{i,t}$ (`R.thF i t`), the downward integral $d(y, f, l, g)$ and the theta functions of finite type. Let $\phi_P$ (`R.ptP i t P`) be the Fock vector of a polynomial $P$ in the Fock polynomial ring $\mathcal P$, as in [`forms_vanish_of_io`](/entry/forms-vanish-of-io/).

**Theorem.** Assume `Given R F` and `R.FullP`. Let $y \in H_V$ with $\theta_{i,t}(y) = 0$. Then $d(y, f, l, g) = 0$ for each theta function $f$ of finite type, each $l \in E^*$ and each $g \in U(W)(\mathbb A)$.

## Proof

1. Fix a Haar measure $\mu$ and a fundamental domain $\mathcal F$ for the rational matrices, with $\mu(\mathcal F) = 1$ (`exists_isCovolOne`).
2. Since $\theta_{i,t}(y) = 0$, the downward integrals of $y$ vanish on the Fock vectors of the lowest types (`theta_lift_vanishes_single_coefficient_of_kernel_kills`). By [`realFockThetaLift_vanishing_of_generating_vectors`](/entry/real-fock-theta-lift-vanishing-of-generating-vectors/), they vanish on every Fock vector: $d(y, \phi_P, l, g) = 0$ for all $P \in \mathcal P$.
3. Suppose $d(y, f, l, g) \neq 0$ and put $\epsilon = |d(y, f, l, g)|$. By `downward_theta_integral_sobolev_continuous`, there are $N$ and $\delta > 0$ such that $|d(y,f,l,g) - d(y,\phi_P,l,g)| < \epsilon$ whenever the Sobolev norm $\|f - \phi_P\|_N$ is less than $\delta$.
4. By `thetaFunction_fixedFinitePart_sobolevLimit_fockVectors`, a theta function of finite type is a Sobolev limit of Fock vectors. So some $P$ has $\|f - \phi_P\|_N < \delta$. With step 2 this gives $\epsilon < \epsilon$, a contradiction.

The Sobolev norm `sobO` is built from the $L^2(\mathcal F, \mu)$ norm and the real Heisenberg derivatives `heisDer`; we have not unfolded `wordSum`.

## In the Lean code

The theorem is at [ThetaLiftGenerationAtRealPlaces.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ThetaLiftGenerationAtRealPlaces.lean#L22). `GenInf` is in [ParamsEx.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/ParamsEx.lean#L79), and `sobO` in [SqNormIntegralFundamentalDomainEqL2NormSq.lean](lean:Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/SqNormIntegralFundamentalDomainEqL2NormSq.lean#L336).

- The four cited lemmas are second names. Their targets are `lift_vanish_single`, `GenRealFock.gen` ([`gen`](/entry/gen/)), `Sobolev` and `FinLikeClosure.closure`. We have not opened the first, third and fourth.
