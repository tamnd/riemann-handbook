---
id: period-ne-of-eigen
title: The bottom period is not zero on K-finite core vectors
kind: theorem
decl: UpperTheory.Lit.Branch.periodNe_of_eigen
module: Development.AutomorphicArithmetic.ThetaCorrespondence.RealBands.BranchPeriod
covers: 651
status: drafted
drafted_by: writer@claude
---
This theorem proves $\mathrm{PeriodNe}$: at the bottom of the tower, every nonzero row vector has a nonzero period against some $K$-finite core vector. It is the first fact that [real functionals separate](/proof/bessel-seesaw/) builds on. That entry calls it with the fields `harishChandraModules`, `casselmanWallach` and `cuspRapidDecay` of the bundle [ThetaLocalInputs](/step/published-results-first/) and with the real input that [the real branching input holds](/entry/real-input-e-holds/) proves. The proof joins [the cusp form with a nonzero theta period](/proof/siegel-weil/), which gives some nonzero period, with a short lemma that moves the nonzero value to every $w \neq 0$ and to a $K$-finite vector.

## Statement

The bottom period is
$$P_0(F, u) = \int_{[U(V_{0,0})]} F(\iota_0(h))\, u(h)\, dh,$$
where $F$ is a form on the core node `.core 0`, $u$ is a function on the row group, and $\iota_0$ is the stabilizer embedding.

Assume `HarishChandraModules`, `CasselmanWallach`, `CuspRapidDecay` and `RealInputE`. Then, for all large enough data of the tower, the following holds. Let $M_0$ and $M_P$ be models (`DSModel`, not unfolded here) for the row and the core. Let $t$ be a nonzero map in `Rows`, from smooth vectors of $M_0$ to automorphic functions on the row group. Then for each smooth vector $w \neq 0$ of $M_0$ there are $y$ in `CoreForms` and $v$ in the span of pure tensors of $K$-finite vectors of $M_P$ with
$$P_0(y(v), t(w)) \neq 0.$$

"Large enough" is the quantifier `Ev`: for each $\varepsilon$ and each $C_F \geq 6510$ there is $x_0$ such that the claim holds for all data with parameter $x \geq x_0$.

## Proof

1. Feed `RealInputE` through `packEx_of_eigen`, and take `GlobalTheory.T.gridDepth_pays_every_loss`. With the three cited inputs, [`exists_cusp_form_theta_period_ne_zero`](/proof/siegel-weil/) gives, for large data and each nonzero $t$, some $y$, $v'$, $w'$ with $P_0(y(v'), t(w')) \neq 0$.
2. Apply `GlobalTheory.PeriodNePf.exists_kf` to this $y$. Its proof has three steps:
   - If the integral of $y(v') \circ \iota_0$ against every real translate of $t(w)$ were zero, then `GlobalTheory.T.integral_eq_zero_of_orthogonal_real_translates` would make $P_0(y(v'), t(w')) = 0$. So one translate $h$ gives a nonzero integral.
   - The lemma `real_translate` moves $h$ onto the core side, so $P_0(y(v''), t(w)) \neq 0$ for a new vector $v''$.
   - If $P_0(y(a), t(w))$ were zero for every $K$-finite $a$, then `GlobalTheory.T.period_eq_zero_of_vanishing_on_kFinite_values` would make it zero at $v''$ too.

I have not unfolded the two `GlobalTheory.T` lemmas.

## In the Lean code

The theorem is at [BranchPeriod.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/RealBands/BranchPeriod.lean#L14). `PeriodNe` is at [OffQOfSizeRows.lean](lean:Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/OffQOfSizeRows.lean#L119), and `exists_kf` is at [PeriodNonvanishingOfArchimedeanInputs.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/PeriodNonvanishingOfArchimedeanInputs.lean#L65).

- `CasselmanWallach` is only passed to `exists_cusp_form_theta_period_ne_zero`. The step `exists_kf` uses `CuspRapidDecay` and `HarishChandraModules`.
- [`GlobalTheory.T.gridDepth_pays_every_loss`](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/GridDepthPaysEveryLossStatement.lean#L11) is proved by a `first | exact ...` list of three ways to apply `GlobalTheory.SepPer.depth_pays`.
