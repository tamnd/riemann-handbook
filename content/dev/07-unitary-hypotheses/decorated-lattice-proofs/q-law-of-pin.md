---
id: q-law-of-pin
title: The iterated integral law for a pinned tuple
kind: theorem
decl: GlobalTheory.QLawPf.qLaw_of_pin
module: Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.SeeSawIteratedIntegralLawAtTwistOfFactorisation
covers: 635
status: drafted
drafted_by: writer@claude
---
This theorem proves the iterated integral law `QLaw` for a pinned decorated tuple, as a finite sum over $\alpha$ of [the law for one character](/entry/one-chart/). Its second name is [the iterated integral law at the twist](/entry/see-saw-iterated-integral-law-at-twist-of-factorisation/), and [the laws for a rescaled pinned tuple](/entry/laws-of-pin-resc/) uses that name.

## Statement

We use the names of [the parent entry](/entry/laws-of-pin-resc/). Fix $D$, $c$, $v$, $t$ and a decorated tuple $w$ over $t$.

**Theorem.** If $c$, $t$ and $v$ satisfy `Is`, $v$ satisfies `WeilOK` for $t$, and $w$ is pinned, then `QLaw v w` holds. That is, fix a middle step $j$ with index $\sigma$. Let $G_1$ be the group of the space $V(j+1)$ at the places of $Q$, and $R_1$ its intersection with the Jacobi group. Let $G_2$ and $R_2$ be the same for $V(j+2)$ and the Bessel group. Let $\mu_i$ and $\rho_i$ be Haar measures on $G_i$ and $R_i$ that give volume $1$ to the elements that fix the lattice of $v$ at $Q$ (`IsNormAt`). Let $\Psi_1, \Psi_2$ be vacuum vectors at $Q$, let $\varphi_\alpha$ be continuous automorphic and in $F_X(j, \alpha)$, and let $f$ be automorphic and in $F_Y(j+2)$. Then

$$\begin{aligned}&{\mathrm{Iter}_2\Bigl(\sum_\alpha \sum_g \varepsilon(j,\alpha)(g)\, P\bigl(h(\varphi_\alpha, g, q_1, q_2),\, q_2 f\bigr)\Bigr)}\\ &{\quad = c_Q(j) \sum_\beta P\Bigl(\sum_\alpha \sum_\gamma b\bigl(\varphi_\alpha, d_Q(j,\alpha,\gamma) * d_Q(j+1,\gamma,\beta)\bigr),\, \varepsilon(j+2,\beta) f\Bigr).}\end{aligned}$$

Here $q_i \in G_i$, $P$ is the period `per` of the datum $B(j+2)$ of $c$, $h$ is the chain step integrand `Chain.hand` built from $e_Q(j)\Psi_1$ and $e_Q(j+1)\Psi_2$, $b$ is the lift `c.bl` applied to a contraction of $\Psi_1$ and $\Psi_2$, and $\varepsilon f = \sum_g \varepsilon(g)\, g f$. $\mathrm{Iter}_2$ is an iterated integral: for fixed $q_1$, integrate over $R_2\backslash G_2$; then integrate the result over $R_1\backslash G_1$. We have not unfolded $P$, $h$ or $b$.

## Proof

1. From the pin, `hF.mid` gives a character $\chi_z$ that links the characters of the two see-saw steps to those of the pin. With the Weil data `hF.kom` this gives a record `Chars`.
2. For each $\alpha$, [`oneChart`](/entry/one-chart/) gives the law with only the term $\alpha$ on the left and $c_Q(j)\sum_\gamma\sum_\beta$ on the right.
3. `isIteratedQuotientIntegral_finset_sum` adds the $|\mathrm{Ch}_j|$ laws.
4. On the right, pull out $c_Q(j)$, swap the sums over $(\alpha,\gamma)$ and $\beta$, and move the sum over $(\alpha,\gamma)$ inside the period with `per_sum`. This needs `contAut_lift` and `contAut_trc`.

The rest is bookkeeping.

## In the Lean code

The theorem is in [SeeSawIteratedIntegralLawAtTwistOfFactorisation.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SeeSawIteratedIntegralLawAtTwistOfFactorisation.lean#L310). `QLaw` is in [PlaceLaws.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/PlaceLaws.lean#L228) and `QPin` in [CosInj.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/CosInj.lean#L152).

Unused hypotheses: the proof binds `t.Is` to `_`, and it never uses $\varphi_\alpha \in F_X(j,\alpha)$ (the pin says nothing about $F_X$). Of "$f$ is automorphic" it uses only that $f$ is continuous automorphic.
