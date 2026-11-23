---
id: theta-function-even-bound
title: The pointwise bound of a theta function, the statement form
kind: theorem
decl: GlobalTheory.T.theta_function_even_bound
module: Development.AutomorphicSpectrum.Proofs.MetricProofs.ThetaFunctionEvenBoundStatement
covers: 362
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. Its proof calls [the normal form bound](/entry/nform/), which holds the content. Its one user is [the mean of the log sup](/entry/mean-log-sup/), which applies it in every archimedean frame.

## Statement

There is a constant $C_0 \geq 0$ with this property. Let $a$ be an archimedean frame of genus $g \geq 1$ with lattice $\Lambda$, hermitian form $H$ and multiplier $\chi$. Assume that $\operatorname{Im} H$ is integral on $\Lambda$, that $\Lambda$ is self-dual for $\operatorname{Im} H$, that $\chi$ is a semicharacter for $\operatorname{Im} H$, and that $\chi^2 = 1$. Let $\vartheta$ be a theta function of level one with $L^2$ norm $b$. Then there is $\rho$ with $0 < \rho \leq \sqrt{2g}$ such that the normalized norm of $\vartheta$ is at most $b \exp(E)$, with $E = g \log(1 + 1/\rho) + C_0 g \log 2g$, and such that the torsion sum bound of [the normal form bound](/entry/nform/) holds.

## Proof

The proof is `first | exact @GlobalTheory.CompanionTheory.Ar.NForm.nform | ...`. The statement is the same as that of `nform`.

## In the Lean code

The theorem is in [ThetaFunctionEvenBoundStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/MetricProofs/ThetaFunctionEvenBoundStatement.lean#L12). Its user is at [ExistsThetaSupBoundLogMean.lean](lean:Development/AutomorphicSpectrum/Proofs/MetricProofs/ExistsThetaSupBoundLogMean.lean#L456).

The word "even" in the name does not match a hypothesis or a conclusion of the statement. The nearest condition is $\chi^2 = 1$, which makes the theta characteristic half-integral.
