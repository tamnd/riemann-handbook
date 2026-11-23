---
id: val-qr-succ
title: The double step integral at r + 1 split places, from r places
kind: theorem
decl: GlobalTheory.QVal.valQr_succ
module: Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.DoubleStepAdelicIntegralFiniteTwistPlaces
covers: 569
status: drafted
drafted_by: writer@claude
---
This theorem is the induction step of [`valQ`](/entry/val-q/). That theorem computes an iterated adelic integral of a double theta step over $r$ split places, by induction on $r$. The base case is `iteratedIntegralValueAtRPlaces_zero`. This theorem passes from $r$ to $r + 1$ places. It splits off the first place and uses a Fubini theorem for iterated quotient integrals over a product of groups. The result goes through `valQ` to [`doubleStep_adelicIntegral_finiteTwistPlaces`](/entry/double-step-adelic-integral-finite-twist-places/).

## Statement

Fix a datum $D$, an additive character $\psi$ of $\mathbb{A}_F$ with `IsStdChar D ψ (-1)`, an integer $\sigma$ and a double step datum $S$ (`Dbl2 ψ σ`). $S$ carries three hermitian spaces with adelic groups $G_0$, $G_1$, $G_2$, a Jacquet subgroup $R_1 \subset G_1$, a Bessel subgroup $R_2 \subset G_2$, and a value functional $S.\mathrm{val}$, a period of a contracted theta kernel. A local step $Q$ (`QStep S`) is a nonarchimedean local field $k$ at a split place $v$, maps $\mathrm{GL}_{a_i}(k) \to G_i$, levels $L_0, L_1, L_2$, finite sets $A_1, A_2$ of representatives, weights $w_1, w_2$ (inverse volumes of cells) and a factor $\mathrm{vol}_J$ (an inverse product of two indices).

For $r$ steps $Q_0, \dots, Q_{r-1}$ at distinct places $P$, put $G_i(P)$ for the part of $G_i$ at $P$. `ValQr D r` says: for Haar measures $\mu_1, \rho_1, \mu_2, \rho_2$ on $G_1(P)$, $R_1 \cap G_1(P)$, $G_2(P)$, $R_2 \cap G_2(P)$ that give the integral points measure 1 (`Norm`), and for data that meet `Hyps` (theta functions with vacua at each $Q_i$, automorphic $\varphi$ and $f$, coefficients supported away from the steps, and $g, h_1, h_2$ trivial at $P$),

$$\int_{R_1 \backslash G_1(P)} \int_{R_2 \backslash G_2(P)} I_Q(x, y)\, dy\, dx = \prod_i \mathrm{vol}_J(Q_i) \sum_{\gamma, \beta} \prod_i w_1(\gamma_i) w_2(\beta_i)\, S.\mathrm{val}(\dots).$$

Here $I_Q$ is `integrand Q` and the right side is `value Q`. The double integral is `Iter2`: there is $F_1$ on $G_1(P)$ with $F_1(x)$ the inner quotient integral, and the outer quotient integral of $F_1$ is the value. Each quotient integral is `IsQuotIntL1`, the integral of an integrable function on the group whose average over the subgroup is the integrand.

**Theorem.** `ValQr D r` implies `ValQr D (r + 1)`.

## Proof

Write $Q' = (Q_1, \dots, Q_r)$ and let $Q_0$ be the split-off place.

1. `periodGroups_reduce_splitPlaceFamily_succ` writes $G_i(P)$ as $G_i(P') \times \mathrm{GL}_{a_i}(k_0)$. It gives normalized measures on the groups at $P'$, local Haar measures $m_i, s_i$ at $Q_0$ (`LocNorm`), product measures on the product subgroups, and a reduction: the iterated integral over the product groups of $I(x' \cdot x_0, y' \cdot y_0)$ gives the iterated integral over $G_i(P)$.
2. `isCompactOpen_product_levels_family`: the levels at $P'$ are compact open.
3. `doubleThetaStep_integrand_invariant_at_succ_places`: the split integrand `pint` is left invariant under the Jacquet and Bessel subgroups and right invariant under the levels.
4. `doubleThetaStep_integrand_finite_doubleCosets`: its support lies in finitely many double cosets.
5. `iteratedInnerIntegral_at_first_of_splitPlaces`: the local double integral at $Q_0$ is `innerVal`.
6. `iteratedIntegralValue_succ_places_outer`, with the hypothesis `ValQr D r`: the double integral of `innerVal` over $P'$ is `value Q`.
7. `haar_measure_quotient_group_product` combines 2 to 6 into the integral over the product groups, and step 1 finishes.

## In the Lean code

The theorem is at [DoubleStepAdelicIntegralFiniteTwistPlaces.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/DoubleStepAdelicIntegralFiniteTwistPlaces.lean#L25). `ValQr`, `integrand`, `innerVal`, `value`, `Hyps`, `Norm` and `pint` are in [ValQOfValQr.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ValQOfValQr.lean#L73), and `Iter2` is in [ValLastX.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/ValLastX.lean#L21). Each lemma of steps 1 to 7 is a `Statement` file that calls a lemma in another namespace (`QRed.reduce`, `QValInner.innerVal_iter2`, `QValOuter.outer`, `IterPeel.iterated_integral_product_groups` and others). We have not opened those proofs. The rest is bookkeeping.
