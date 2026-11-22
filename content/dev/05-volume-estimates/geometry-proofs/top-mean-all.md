---
id: top-mean-all
title: The mean slope bound from the volume theorem
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Plug.top_meanAll
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.AbelianCmCompLawsBound
covers: 1168
status: drafted
drafted_by: writer@claude
---
This theorem proves the bound `MeanAll` on the mean volume slope, for abelian CM fields. It joins the intersection slope bound of the volume theorem to the comparison of intersection slopes with volume slopes. It is the content of [its second name](/entry/abelian-cm-comp-laws-bound/), which [the positivity statement from the volume theorem](/entry/deep-st-r-of-volume/) uses. Step 5 of [the chapter on the Weil bound](/proof/weil-bound/) describes this part of the proof.

## Statement

The weights $u$, the norm $\|u\|_1$, the condition `WtGap u g`, the bound $B(u,g)$, the error term $\mathrm{err}(s,u,g)$ and `MeanAll s C` are as in Step 1 of [the chapter](/proof/weil-bound/). Let $\mathrm{rd}(E) = |\operatorname{disc} E|^{1/[E:\mathbb{Q}]}$, and let $L = \operatorname{Re} L'/L(1, \chi_d)$ for the quadratic character of the host.

**Theorem.** Assume `NefRR`, `Top.Given`, the existence of a full intersection system $II$, the birational pullback formula, `GoodTowerExistsX` and `VolumeTheoremX`. Then there is $C \geq 0$ such that the following holds. Let $E$ be a CM field, abelian Galois over $\mathbb{Q}$, with $\#\mathrm{CMType} \geq 2$. Take a datum with $q \geq 1$ and $3q + 1 \leq p + q$, a level that is good at all primes with $A = 1$, data $U$, $h$, $e$ (which we have not unfolded) with the laws `CompLaws`, `UnifAll` and `FnAlgClosed`. Suppose that the primes of $2 \operatorname{disc} E$ and of the level number at most $4\,\#\mathrm{CMType}\,(p+q)^2$, and that $|\tau(\xi_0)| = x$ for all base points $\xi_0$ and all $\tau$. Then `MeanAll` $U$ $x$ $(\log \mathrm{rd}(E) + |L|)$ $C$ holds.

## Proof

1. `full_intersection_good_level` uses `Top.Given`, `GoodTowerExistsX` and `VolumeTheoremX`. It gives $C_T \geq 0$, a root tower $T$ with a good origin, a bijection $\kappa$ from the components to those of $T$, bad primes equal to the primes of $2 \operatorname{disc} E \cdot M'$, and the bound `MeanSlope` with constant $C_T$. Put $C = C_T + 120$.
2. Fix $u$ and $g$ with `WtGap u g`. `tower_weight_of_zero` identifies $\|u\|_1$ and $B(u,g)$ with the tower forms, and turns `WtGap` into `WeightHyp`. Since $\#\mathrm{CMType} \geq 2$ and $p + q \geq 4$, we get $B \geq 128$ and $\lfloor B \rfloor \geq 4\,\#\mathrm{CMType}\,(p+q)^2$, so $\lfloor B \rfloor$ is above the bad primes.
3. `MeanSlope` at $\lfloor B \rfloor$, with $j = p$ and $\min(j, N - j) = q$, gives
$$\frac{1}{\#\mathrm{Comp}} \sum_c \mathrm{slope}(c) \geq -C_T \bigl( (\log(\lfloor B \rfloor\,\mathrm{rd}(E)) + |L|)\,\|u\|_1 + q\,\mathrm{spread}(u) \bigr).$$
4. [`uniform_all_norm_height_bound`](/entry/t-uniform-all-norm-height-bound/) gives $\mathrm{slope}(\kappa Z) - 2\,c_2(B)\,\|u\|_1 \leq \mu_{\mathrm{vol}}(Z, u)$ for each component $Z$. Take $\mathrm{sl}(Z)$ equal to the left side.
5. `cost_two_log_bound` gives $0 \leq c_2(B) \leq 60 (\log B + \log \mathrm{rd}(E))$.
6. So the mean of $\mathrm{sl}$ is at least $-C_T(\dots) - 120(\log B + \log \mathrm{rd}(E))\,\|u\|_1$. With $\log \lfloor B \rfloor \leq \log B$, this is at least $-(C_T + 120)\,\mathrm{err}$.

The rest is bookkeeping: the sum over components moves along $\kappa$, and `nlinarith` closes the inequality.

## In the Lean code

The theorem is in [AbelianCmCompLawsBound.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/AbelianCmCompLawsBound.lean#L54). The file also proves `primeFactors_sub`, `spread_nonneg` and `errX_eq`, which says that $\mathrm{err}$ is the sum above. Here $c_2(B)$ is `costTwo`, a finite sum of multiples of $\log \ell$ over primes $\ell$; we have not unfolded the multiples. `NefRR` and the birational pullback formula are used only in `uniform_all_norm_height_bound`. The constant 120 is twice the constant 60 of `cost_two_log_bound`.
