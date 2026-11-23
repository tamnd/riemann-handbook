---
id: gen-fin
title: Downward theta integrals are fixed by the theta functions of finite type
kind: theorem
decl: GlobalTheory.DownLift.GenFinite.genFin
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ThetaLiftGenerationFinitePlaces
covers: 476
status: drafted
drafted_by: writer@claude
---
This theorem proves `GenFin`: for a form $y$ with no level character, if the downward theta integrals of $y$ vanish against the theta functions of finite type, they vanish against all theta functions. It has two users: [`liftRows_injective_and_typeProperties_of_nonvanishing`](/entry/lift-rows-injective-and-type-properties-of-nonvanishing/), where it is step 3 of the proof of `TypeNZ`, and its second name `thetaLift_generation_finitePlaces`. Both lie under [`hypotheses_nonempty_of_unramified_exponents_alt`](/proof/unitary-hypotheses/), branch 1 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/).

## Statement

Let $R$, $F$, $i$, $t$ be as in the parent entry. Let $\omega$ be the Weil representation `R.ωP i t` of $U(V)(\mathbb A) \times U(W)(\mathbb A)$, and $v$ the theta vector `R.vP i t`. For $y \in H_V$ let $\tilde y$ be the $E$-valued function on $U(V)(\mathbb A)$ attached to $y$ (`R.extV i t y`), with $E$ the coefficient space `R.cV i`. For a theta function $f$, $l \in E^*$ and $g \in U(W)(\mathbb A)$, the *downward integral* (`downInt`) is

$$d(y, f, l, g) = \int_{\mathcal F_V} (\omega(h,g) f)(0)\; l(\tilde y(h))\, d\nu_V(h),$$

over a fundamental domain $\mathcal F_V$. A theta function $f$ is *of finite type* (`FinLike`) if each finite relation $\sum_u c_u\, \rho(u) v = 0$, with $\rho$ the Heisenberg action `heisO` and each $u$ of zero archimedean part, also holds with $f$ in place of $v$. The form $y$ has *no level character* (`NoChi`) if certain weighted averages of $l \circ \tilde y$ over the finite group $G$ vanish; we have not unfolded the average `gaL`.

**Theorem.** Assume `HoweUnram`, `Given R F` and `R.FullP`. Let $y \in H_V$ have no level character, and let $d(y, f, l, g) = 0$ for all $f$ of finite type and all $l, g$. Then $d(y, f, l, g) = 0$ for every theta function $f$ and all $l, g$.

## Proof

Let $\mathcal A$ be the set of theta functions $f$ with $d(y, f, \cdot, \cdot) = 0$. Since $d$ is linear in $f$ (`downInt_add`, `downInt_smul`), $\mathcal A$ is a subspace. Then:

1. $\mathcal A$ contains each translate $\omega(1, g')f$ of an $f$ of finite type (`downInt_transl`).
2. $\mathcal A$ contains the level averages `avgW` of theta functions, by `level_averages_theta_pair_zero_without_character`. This is the step that uses `NoChi`.
3. Let $f$ be of level type (`TypeVec`): the level group acts on $f$ by the inverse of the level character. By `thetaFunction_levelType_mem_span_averages`, $f$ is in the span of the level averages and of the vectors of level type that are clean (`Clean`). A clean vector of level type is in the span of the translates of step 1, by [`thetaFunction_levelType_mem_span_translates`](/entry/theta-function-level-type-mem-span-translates/). So $f \in \mathcal A$.
4. $\mathcal A$ contains each difference $\omega(\kappa,1)f - \chi(\kappa)^{-1} f$ with $\kappa$ in the level group, by `downwardLift_level_acts_by_inverse_character`.
5. Each theta function is in the span of the vectors of level type and these differences (`thetaFunction_mem_span_levelType_differences`).

## In the Lean code

The theorem is at [ThetaLiftGenerationFinitePlaces.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ThetaLiftGenerationFinitePlaces.lean#L60). `GenFin`, `FinLike`, `NoChi` and `downInt` are in [ParamsEx.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/ParamsEx.lean#L46). `Gen`, `TypeVec`, `TypeDiff` and `AvgIm` are in [HeisOAdd.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/HeisOAdd.lean#L27).

- The conclusion is stated as `¬ SomeLift R i t y`: no theta function gives a nonzero downward integral.
- `HoweUnram` is used only through `thetaFunction_levelType_mem_span_translates`, which holds the main local work.
