---
id: good-tower-i5
title: The height bounds of points on a good tower (statement form)
kind: theorem
decl: GlobalTheory.T.good_tower_I5
module: Development.AutomorphicSpectrum.Proofs.DivisibilityProofs.GoodTowerI5Statement
covers: 827
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It has the same statement as [`i5_and_i6_of_isGlobal_of_goodOrigin`](/entry/i5-and-i6-of-is-global-of-good-origin/), and its proof applies that theorem. The work is done in [`global_model_tower_fifth_condition`](/entry/global-model-tower-fifth-condition/) and [`tower_good_of_sandwich_split`](/entry/tower-good-of-sandwich-split/). The user is [the volume theorem for good root towers](/entry/volume-theorem-x-of-inputs/).

## Statement

Use the notation of [the volume theorem for good root towers](/entry/volume-theorem-x-of-inputs/). A *point* of the root model $M_{B,c}$ is a prime ideal $W$ of its multihomogeneous coordinate ring that contains the ideal of $M_{B,c}$ and is an arithmetic variety of dimension $1$. For a weight $\mu$ and $s > 0$, the height $h_{B,c}(\mu, s; W)$ is a linear combination, with coefficients that depend on $\mu$ and $s$, of the intersection numbers of $W$ with the lines $\overline x_r(e^{-1/s^2})$, divided by the degree of $W$. We have not unfolded the coefficients. Let $\nu$ be the weight of the tower, and $\mathrm{gap}_\tau(\lambda) = \lambda_{\tau, j-1} - \lambda_{\tau, j}$.

For $c_0 > 0$ and $\theta_0 > 0$, call $(\lambda, \theta, s)$ *admissible* if $\lambda$ is a rational weight with $\|\lambda\| \leq 1$, $0 < \theta \leq \theta_0$, $s = \theta^2 \in \mathbb{Q}$, $\theta \leq \mathrm{gap}_\tau(\lambda)$ for each $\tau$, and $\lambda_{\tau,i} - \lambda_{\tau,i+1} \geq c_0$ for each $\tau$ and each $i$ with $i + 1 < N$ and $i + 1 \neq j$.

- $\mathrm{I5}$: for each $c_0 > 0$ there are $\theta_0 > 0$ and $C$ such that for all $B \geq 2$, all $c$, all admissible $(\lambda, \theta, s)$ and all points $W$ of $M_{B,c}$, $h_{B,c}(\lambda - s\nu, s; W) \geq -C \log(B/s)$.
- $\mathrm{I6}$: the same, with the conclusion that there is a Zariski dense set of points $W$ of $M_{B,c}$ with $h_{B,c}(\lambda - s\nu, s; W) \leq C \log B$.

**Theorem.** Assume $\mathrm{Given}$. Let $E$ be a CM field, abelian over $\mathbb{Q}$, with host $H$ and datum $D$ with $p, q \geq 1$. Let $Y$ be a global integral model, $T$ a root tower for $N = p + q$, $o$ a good origin of $Y$ for $T$ with `Extra`, and $II$ a full intersection system. Then $T$ satisfies $\mathrm{I5}$ and $\mathrm{I6}$ for $II$.

## Proof

Apply `i5_and_i6_of_isGlobal_of_goodOrigin`.

## In the Lean code

The theorem is in [GoodTowerI5Statement.lean](lean:Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/GoodTowerI5Statement.lean#L16). The proof is `first | exact @… | exact … | (intros; apply … <;> assumption)`, as in the other statement files of this chapter. `I5` and `I6` are in [Proportional.lean](lean:Development/AutomorphicSpectrum/Definitions/DivisibilityTowers/Proportional.lean#L94), and the height of a point is `RootModel.ht` in [Birational.lean](lean:Development/AutomorphicSpectrum/Definitions/DivisibilityTowers/Birational.lean#L112). The name mentions only `I5`; the conclusion is `I5 ∧ I6`.
