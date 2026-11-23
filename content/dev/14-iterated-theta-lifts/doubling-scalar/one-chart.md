---
id: one-chart
title: The iterated integral law for one character of a pinned tuple
kind: theorem
decl: GlobalTheory.QLawPf.oneChart
module: Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.SeeSawIteratedIntegralLawAtTwistOfFactorisation
covers: 618
status: drafted
drafted_by: writer@claude
---
This theorem proves the law `QLaw` of a pinned tuple for one character $\alpha$ at a time. It is the general local computation of [the double step at finitely many places](/entry/double-step-adelic-integral-finite-twist-places/), applied to the local data of the pin. [The law for a pinned tuple](/entry/q-law-of-pin/) adds these laws over $\alpha$.

## Statement

We use the names and the hypotheses on $\mu_i, \rho_i, \Psi_1, \Psi_2$ of [the law for a pinned tuple](/entry/q-law-of-pin/). Let $w$ be pinned by a family $F$ of local data $Q_1, \dots, Q_r$ at distinct split places, and let `Chars` hold: a character $\chi_z$ with $\chi_V = \chi_j\chi_z$, $\chi_W = \chi_j$ for the first see-saw step, $\chi_V = \chi_{j+1}$, $\chi_W = \chi_{j+1}\chi_z$ for the second, and the Weil data of $t$ at $j$ and $j+1$.

**Theorem.** Let $\alpha \in \mathrm{Ch}_j$, let $\varphi$ and $f$ be continuous automorphic, and let $f \in F_Y(j+2)$. Then

$$\begin{aligned}&{\mathrm{Iter}_2\Bigl(\sum_g \varepsilon(j,\alpha)(g)\, P\bigl(h(\varphi, g, q_1, q_2),\, q_2 f\bigr)\Bigr)}\\ &{\quad = c_Q(j) \sum_\gamma \sum_\beta P\bigl(b(\varphi, d_Q(j,\alpha,\gamma) * d_Q(j+1,\gamma,\beta)),\, \varepsilon(j+2,\beta) f\bigr).}\end{aligned}$$

## Proof

1. For each $i$, `stepOf` turns the local datum $Q_i$ and the component $\alpha_i$ of $\alpha$ (by the bijection $\mathrm{Ch}_j \simeq \prod_i \mathrm{Ch}_j(Q_i)$ of the pin) into a local step `QStep` at the place of $Q_i$. The record `Chars` gives a global double step `dblOf H`.
2. Apply [`doubleStep_adelicIntegral_finiteTwistPlaces`](/entry/double-step-adelic-integral-finite-twist-places/) to these $r$ steps, with $g = h_1 = h_2 = 1$ and the trivial coefficients $c_1 = c_2 = \delta_0$. Its hypotheses come from the pin:
   - the places of the $Q_i$ are distinct and their set is $Q$ (`hF.inj`, `hF.places`);
   - `norm_eq` identifies the integral points of the steps with the elements that fix the lattice of $v$ (by `T.splitPlace_local_group_closedEmbedding_integral`), so the measures are normalised;
   - `model_of_vac` makes $\Psi_1, \Psi_2$ vacuum at each step (by `T.integralIndicator_gives_localVacuum_splitPlace`);
   - $f$ is typed at each place (`hF.FY`).
3. Multiply both sides by the weight $\prod_i \mathrm{wt}(\alpha_i)$.
4. Left side: by `hF.ε`, the weight times the convolution of the local $\varepsilon_L$ is $\varepsilon(j,\alpha)$. By `hF.eQ` and `AvgMid.theta_comb`, the value of the double step is the integrand $h$ (`val_eq_hand` with `handIsLift`, which uses `Unf.Contr.contrLaw`).
5. Right side: the product of the local factors $\mathrm{vol}_J$ of the steps is $c_Q(j)$ by `hF.cQ`, since the two indices are the numbers $\mathrm{idx}(j+1)$ and $\mathrm{idx}(j+2)$ of $Q_i$ (`idx_mid`). Reindex the sums over $\gamma$ and $\beta$ through the pin bijections. The local weights $w_1 w_2$ become the weights of $\gamma$ and $\beta$, which `hF.dQ` and `hF.ε` absorb into $d_Q$ and $\varepsilon(j+2,\beta)$. Pull the scalars out of $b$, $P$ and $\varepsilon f$.

The rest is bookkeeping.

## In the Lean code

The theorem is in [SeeSawIteratedIntegralLawAtTwistOfFactorisation.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SeeSawIteratedIntegralLawAtTwistOfFactorisation.lean#L229). `QStep` and `ValQ` are in [IsOneComb.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/IsOneComb.lean#L71). The helpers `stepOf`, `dblOf`, `handIsLift`, `norm_eq`, `model_of_vac`, `fin_eQ` and `fin_dQ` are in the same file as the theorem.

The theorem uses the general statement only at $g = h_1 = h_2 = 1$ and $c_1 = c_2 = \delta_0$, so the condition `Away` on $c_1, c_2$ holds trivially.
