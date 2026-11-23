---
id: mean-log-sup
title: The mean of the log sup of a theta section
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Sl.Sup.mean_log_sup
module: Development.AutomorphicSpectrum.Proofs.MetricProofs.ExistsThetaSupBoundLogMean
covers: 405
status: drafted
drafted_by: writer@claude
---
This theorem bounds the sup norm of a theta section at all complex places at once, in mean, by its $L^2$ norm. The statement is in [the statement form](/entry/exists-theta-sup-bound-log-mean/), which we do not repeat. The loss is $C g \log(2 + g + \Phi)$. The proof makes the local bound of [the pointwise bound of a theta function](/entry/theta-function-even-bound/) global with an arithmetic input: torsion values of the theta section are algebraic integers.

## Statement

There is $C \geq 0$ such that for all $E, L, D, \vartheta, \Phi$ with $g \geq 1$, $\Phi \geq 0$ and `HasTheta` $\vartheta$ $\Phi$, there are $M_\sigma > 0$ with `SupLe` $\vartheta$ $M$ and $\operatorname{mean}_\sigma \log M_\sigma \leq \Phi + C g \log(2 + g + \Phi)$.

## Proof

Let $b_\sigma$ be the $L^2$ norms from `HasTheta`, so $\operatorname{mean} \log b \leq \Phi$. Put $E(\rho) = g \log(1 + 1/\rho) + C_0 g \log 2g$ and $\varphi(\rho) = \frac{\pi}{96 \rho^2} - E(\rho)$.

1. In each frame $a$ at $\sigma$, `theta_function_archimedean_frame` and `theta_multiplier_quadratic_character` give the hypotheses of `theta_function_even_bound`. That lemma gives $\rho_\sigma(a) \in (0, \sqrt{2g}]$, the bound $\mathrm{nrm} \leq b_\sigma e^{E(\rho)}$, and the torsion sum bound with $\varphi(\rho)$.
2. `tors_mean`: for every choice $f$ of frames, $\sum_\sigma \varphi(\rho_\sigma(f_\sigma)) \leq \sum_\sigma \log b_\sigma$. Its proof takes a full torsion field, notes that a product of torsion values $T$ is a nonzero algebraic integer with $\lvert \tau T \rvert$ a power of $\mathrm{nrm}$, and uses $\sum_\tau \log \lvert \tau T \rvert \geq 0$ (`sum_log_norm_nonneg`, from the norm of $T$).
3. `Ef_le` gives $E \leq \varphi + K_1$. With step 2 this bounds $E(\rho_\sigma(a))$ over all frames. Let $e_\sigma$ be the supremum, choose $f_\sigma$ within $1$ of it, and put $M_\sigma = b_\sigma e^{e_\sigma}$. Then `SupLe` holds by step 1.
4. `WeakMatrixArithmetic.intersectionNumber_baseChange` turns $\operatorname{mean} \varphi(\rho_\sigma(f_\sigma)) \leq \Phi$ into $\operatorname{mean} \rho^{-2} \leq C(\Phi + g^2 \log 2g)$ and a bound for $\operatorname{mean} \log^+(1/\rho)$. Then `final_bound`, an inequality of real numbers, gives the constant $C'$.

## In the Lean code

The theorem is in [ExistsThetaSupBoundLogMean.lean](lean:Development/AutomorphicSpectrum/Proofs/MetricProofs/ExistsThetaSupBoundLogMean.lean#L452). `tors_mean` is at line 190, `Ef` at line 317 and `final_bound` at line 353. The `GlobalTheory.T` lemmas are statement forms that we did not unfold. The lemma of step 4 is in [CoordWeak.lean](lean:GroundTheory/HeightsAndTheta/Heights/HeightKernels/CoordWeak.lean#L72) and proves `WeakMatrixArithmetic.Statement` of [KernelsMatrix.lean](lean:GroundTheory/HeightsAndTheta/Heights/KernelsMatrix.lean#L84). Its name speaks of intersection numbers and base change, but its content is an inequality about finite means of real numbers.
