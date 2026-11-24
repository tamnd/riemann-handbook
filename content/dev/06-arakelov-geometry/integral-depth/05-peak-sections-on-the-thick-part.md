---
title: Peak sections on the thick part
decls:
  - GlobalTheory.PeakThick.peak
  - GlobalTheory.T.exists_cusp_form_peak_at_injective_chart_frame
  - GlobalTheory.HormanderPeak.hormander_peak
  - GlobalTheory.T.exists_hormanderPeak_orthonormalFrame_l2Bound
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Peak sections on the thick part

This section constructs, at a frame where the chart is injective, a cusp form whose value at the frame controls its $L^2$ norm on a fundamental set. The weight must have large gaps. The construction has two steps. First, the $L^2$ method of Hörmander gives a holomorphic function on the chart domain that is $1$ at the frame, vanishes at the other points of the orbit and has a bounded weighted $L^2$ norm ([$L^2$ estimates](/learn/positivity-resolution/#l2-estimates)). Second, a Poincaré series turns it into a cusp form. The result is the peak section that [the Bergman kernel bound](/entry/exp-neg-b-le-berg-on-of-mem-frames-on/) of the previous chapter uses on the thick part.

Let $E$ be a CM field and $r \ge 1$. Fix unitary data $\mathcal{X}$ of rank $r$ over $E$: a CM type $\Psi$, an index $r_0$, an arithmetic group $\Gamma$ acting on the left on frames, a Borel subgroup $\mathrm{Bor}$ acting on the right, and for each frame $x$ a chart $z \mapsto \mathrm{cpt}(x, z)$ from a complex vector space $V$ to frames, with a domain $\Omega_x \subseteq V$ and a measure $\mu_x$ on $V$. A *weight* is a function $\lambda$ on $\Psi \times \{0, \dots, r - 1\}$ with integer values, and we put
$$|\lambda| = \sum_{\tau \in \Psi} \sum_{a < r} |\lambda(\tau, a)|, \qquad R = (|\Psi|\, r)^8.$$
For a weight $\lambda$, the cusp forms of weight $\lambda$ form a space $S_\lambda$, and $\|P\|_\lambda(x)$ is the pointwise norm of $P \in S_\lambda$ at a frame $x$. We do not unfold the data, orthonormal frames, fundamental sets, cusp forms or the pointwise norm ([Shimura varieties](/learn/geometry/#shimura-varieties-and-toroidal-compactifications), [metrics](/learn/positivity-resolution/#metrics-curvature-and-positivity)).

The two theorems share the following conditions on a constant $C$, a weight $\lambda$ and a frame $x$, which we call the *peak conditions*:

1. $0 < r_0 < r$, and $x$ is orthonormal;
2. for each $\tau$ and each $a$ with $a + 1 < r$ and $a + 1 \ne r_0$, $\lambda(\tau, a) - \lambda(\tau, a + 1) \ge C R$;
3. for each $\tau$, $\lambda(\tau, r - 1) - \lambda(\tau, 0) \ge C R$;
4. the chart at $x$ is injective modulo $\Gamma$ and $\mathrm{Bor}$ on the ball of radius $1/(100 r^2)$: if $\gamma \in \Gamma$, $\|z\|, \|z'\| \le 1/(100 r^2)$, $b \in \mathrm{Bor}$ and $\gamma \cdot \mathrm{cpt}(x, z) = \mathrm{cpt}(x, z') \cdot b$, then $\gamma = 1$.

**Theorem 3.5.1 (Hörmander peak).** There is $C \ge 0$ with the following property. For all CM fields $E$, $r$, data $\mathcal{X}$, weights $\lambda$ and frames $x$ that satisfy the peak conditions with $C$, there are a function $F$ on $V$, holomorphic on $\Omega_x$, and a function $P_0$ on frames with:

1. $P_0$ is equivariant for $\mathrm{Bor}$ with the weight $\lambda$, and $P_0(\mathrm{cpt}(x, z)) = F(z)$ for $z \in \Omega_x$;
2. $P_0(x) = 1$, and $P_0(\gamma x) = 0$ for all $\gamma \in \Gamma$ with $\gamma \ne 1$;
3. $F$ satisfies the integrability condition at $x$ with the weight $W$ of $\lambda$ and the exponent $\epsilon = 4|\Psi| r^2 + 1$, and
$$\begin{aligned}
&\int_V \frac{|F(z)|^2}{\kappa_\epsilon(z)}\, W(\mathrm{cpt}(x, z))\, d\mu_x(z) \\
&\quad \le e^{C(|\lambda| + R)}\, \mu_x\bigl(B(0, \tfrac{1}{100 r^2}) \cap \Omega_x\bigr).
\end{aligned}$$

Here $W$ and $\kappa_\epsilon$ are a weight function on frames and a singular weight on $V$ that we do not unfold.

Lean: `GlobalTheory.HormanderPeak.hormander_peak` (also `GlobalTheory.T.exists_hormanderPeak_orthonormalFrame_l2Bound`, a second name).

*Proof.* Let $C_1$ be the constant of a lemma on cutoffs and singular weights, an input, and take $C = C_1 + 2$. The lemma gives a radius $\rho$, a cutoff function $F_0$ that is $1$ near $0$ and supported in the ball of radius $1/(100 r^2)$, and a plurisubharmonic weight $\varphi$ with a logarithmic pole at $0$ and at the points of $\Omega_x$ that correspond to the other points of the orbit $\Gamma x$. The domain $\Omega_x$ is open, and the exhaustion function of the chart is smooth with positive Levi form. A lemma on the $\bar\partial$ equation, an input, applies to the form $\bar\partial F_0$ with the weight $\varphi$ and gives a solution $u$ with weighted $L^2$ bound, obtained as a decreasing limit of plurisubharmonic weights. Put $F = F_0 - u$. Then $F$ is holomorphic on $\Omega_x$. Since $u$ is square integrable against a weight with a pole of high order at $0$, and $u$ is holomorphic near $0$, $u$ vanishes at $0$; so $F(0) = 1$. The bound $|F|^2 \le 2|F_0|^2 + 2|u|^2$ and the bounds of the two lemmas give the integral bound with $e^{(C_1 + 2)(|\lambda| + R)}$. An extension lemma, also an input, gives $P_0$ equivariant for $\mathrm{Bor}$ with $P_0 \circ \mathrm{cpt}(x, \cdot) = F$ on $\Omega_x$. Then $P_0(x) = F(0) = 1$. A lemma on peak extensions, an input, uses the injectivity of the chart and the poles of $\varphi$ at the other orbit points to give $P_0(\gamma x) = 0$ for $\gamma \ne 1$. $\square$

**Theorem 3.5.2 (A cusp form peaked at an injective frame).** There is $C \ge 0$ with the following property. Let $E$, $r$, $\mathcal{X}$, $\lambda$ and $x$ satisfy the peak conditions with $C$. Let $x_0$ be an orthonormal frame and $\Phi \subseteq V$ a fundamental set for the chart at $x_0$. Then there is a cusp form $P \in S_\lambda$ with $P(x) \ne 0$ and
$$\begin{aligned}
&e^{-C(|\lambda| + R)} \int_\Phi \|P\|_\lambda(\mathrm{cpt}(x_0, z))^2\, d\mu_{x_0}(z) \\
&\quad \le \|P\|_\lambda(x)^2\, \mu_{x_0}(\Phi).
\end{aligned}$$

Lean: `GlobalTheory.PeakThick.peak` (also `GlobalTheory.T.exists_cusp_form_peak_at_injective_chart_frame`, a second name).

*Proof.* Let $C_H$ be the constant of the Hörmander peak and $C_S$ the constant of a Poincaré $L^2$ inequality on fundamental sets, an input. Take $C = C_H + C_S + 1$; the peak conditions with $C$ imply those with $C_H$. Take $F$ and $P_0$ from the Hörmander peak. Let $P$ be the Poincaré series of $P_0$, the sum of the translates of $P_0$ by $\Gamma$ with the factor of automorphy of $\lambda$. Since $|\Psi| \ge 1$, there is $\tau_0 \in \Psi$. A lemma on cusp conditions, an input, uses the gaps of $\lambda$ at $\tau_0$ to show that the series converges, is bounded and is a cusp form of weight $\lambda$. At $x$, only the term $\gamma = 1$ is nonzero, since $P_0(\gamma x) = 0$ for $\gamma \ne 1$. The character of the factor of automorphy is $1$ at $\gamma = 1$, so $P(x) = P_0(x) = 1 \ne 0$. As $x$ is orthonormal, $\|P\|_\lambda(x) = 1$.

The Poincaré inequality bounds the integral of $\|P\|_\lambda^2$ over $\Phi$ by $e^{C_S(|\lambda| + R)}$ times the integral of $|F|^2/\kappa_\epsilon$ against $W$ over the chart at $x$. The Hörmander peak bounds this by $e^{C_H(|\lambda| + R)}$ times $\mu_x\bigl(B(0, \tfrac{1}{100 r^2}) \cap \Omega_x\bigr)$. By the injectivity of the chart on this ball, its image modulo $\Gamma$ meets each orbit once, and a comparison of chart integrals with the fundamental set gives that this volume is at most $\mu_{x_0}(\Phi)$. Collecting the exponents gives
$$\int_\Phi \|P\|_\lambda^2\, d\mu_{x_0} \le e^{(C_H + C_S)(|\lambda| + R)}\, \mu_{x_0}(\Phi),$$
which implies the claim with $C = C_H + C_S + 1$, since $\|P\|_\lambda(x) = 1$. $\square$

**Remark 3.5.3 (Formalization).** The constants are explicit sums of the constants of the inputs: $C_H + C_S + 1$ in the theorem on cusp forms ([ExistsCuspFormPeakAtInjectiveChartFrame.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsCuspFormPeakAtInjectiveChartFrame.lean#L30)) and $C_1 + 2$ in the Hörmander peak ([ExistsHormanderPeakOrthonormalFrameL2Bound.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsHormanderPeakOrthonormalFrameL2Bound.lean#L38)). The weight function $W$ is the weight of $\lambda$ with the zero shift. The lemma on cutoffs and singular weights, the $\bar\partial$ lemma, the extension lemma, the vanishing of the peak at other orbit points, the cusp condition, the Poincaré $L^2$ inequality and the comparison of chart integrals with fundamental sets are known to us by their statements. The integrability condition, the singular weight $\kappa_\epsilon$ and the exhaustion function are not unfolded.
