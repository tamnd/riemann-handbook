---
id: nform
title: The normal form bound of a theta function
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.NForm.nform
module: Development.AutomorphicSpectrum.Proofs.MetricProofs.ThetaFunctionEvenBound
covers: 361
status: drafted
drafted_by: writer@claude
---
This theorem bounds a theta function of level one in one archimedean frame. It gives a pointwise bound by the $L^2$ norm and a lower bound for the sum of $-\log$ of its normalized values at torsion points. Both bounds depend on one number $\rho$ that comes from a reduced period matrix. [The statement form](/entry/theta-function-even-bound/) repeats it, and [the mean of the log sup](/entry/mean-log-sup/) uses it at every complex place.

## Statement

There is $C_0 \geq 0$ with this property. Let $a$ be an archimedean frame of genus $g \geq 1$ with lattice $\Lambda$, hermitian form $H$ and multiplier $\chi$. Assume that $\operatorname{Im} H(\Lambda, \Lambda) \subset \mathbb{Z}$, that a $w$ with $\operatorname{Im} H(w, \Lambda) \subset \mathbb{Z}$ is in $\Lambda$, that $\chi(l + l') = \chi(l)\chi(l') e^{\pi i \operatorname{Im} H(l, l')}$, and that $\chi^2 = 1$. Let $\vartheta$ be a theta function of level one with $L^2$ norm $b$. Put $\lVert\vartheta\rVert(w) = \lvert\vartheta(w)\rvert e^{-\frac{\pi}{2} H(w,w)}$.

**Theorem.** There is $\rho$ with $0 < \rho \leq \sqrt{2g}$ such that, with $E = g \log(1 + 1/\rho) + C_0 g \log 2g$:

1. $\lVert\vartheta\rVert(w) \leq b\, e^{E}$ for every $w$;
2. for all large $m$: if $r_1, \dots, r_n$ are $m$-torsion points with $\vartheta(r_i) \neq 0$, one in each class mod $\Lambda$ of such points, then $n \geq 1$ and $n\bigl(\frac{\pi}{96\rho^2} - E\bigr) \leq \sum_i -\log\bigl(\lVert\vartheta\rVert(r_i)/b\bigr)$.

## Proof

1. `exists_reduced` gives a symplectic basis of $\Lambda$ and a period matrix $X + iY$ with $Y$ reduced for $\rho$ (`IsReducedImaginaryPart`: $\rho^2 \leq 2g$ and $(Y^{-1})_{00} = \rho^2$, among others).
2. `semicharacter_theta_characteristic` gives a characteristic $(a_0, c_0)$ with entries in $\{0, \tfrac12\}$. `theta_function_canonical_multiplier` writes $\vartheta$ as $\kappa$ times the canonical theta function `canTh` with this characteristic, and `theta_function_canonical_form` gives $b = \lvert\kappa\rvert (2^g \det Y)^{-1/4}$.
3. `ThetaBound.full` bounds the canonical theta function. With `theta_norm_in_period_coordinates` this gives $\lVert\vartheta\rVert(w) \leq b \exp(-\frac{\pi}{2\rho^2} d(w)^2 + E)$, where $d(w)$ is the distance to $\mathbb{Z}$ of the first period coordinate of $w$ plus $a_0$. Part 1 follows.
4. `theta_zero_divisor_jet_bound` gives, for large $m$, $n \geq 1$ and $n \leq 3 \#\{i : d(r_i) \geq \tfrac14\}$. So $\sum_i d(r_i)^2 \geq n/48$, and the bound of step 3 at each $r_i$ gives part 2.

## In the Lean code

The theorem is in [ThetaFunctionEvenBound.lean](lean:Development/AutomorphicSpectrum/Proofs/MetricProofs/ThetaFunctionEvenBound.lean#L174), and `exists_reduced` is at line 98. `ThetaBound.full` is in [AssemblyAnalytic.lean](lean:GroundTheory/HeightsAndTheta/Heights/HeightKernels/AssemblyAnalytic.lean#L51). Its statement and `thetaNorm` are in [KernelsMatrix.lean](lean:GroundTheory/HeightsAndTheta/Heights/KernelsMatrix.lean#L71). We did not unfold the `GlobalTheory.T` lemmas of steps 2 to 4. The constant $C_0$ is the constant of `ThetaBound.full`.
