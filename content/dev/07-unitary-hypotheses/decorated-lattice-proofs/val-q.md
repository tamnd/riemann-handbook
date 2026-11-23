---
id: val-q
title: The double step integral at finitely many split places
kind: theorem
decl: GlobalTheory.QVal.valQ
module: Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.DoubleStepAdelicIntegralFiniteTwistPlaces
covers: 586
status: drafted
drafted_by: writer@claude
---
This theorem proves `ValQ D`, a closed form for the iterated quotient integral of a double theta step over finitely many split places. The proof is an induction on the number of places with a trivial base case. [The induction step](/entry/val-qr-succ/) has the real content. Its second name is [the double step integral at finitely many places](/entry/double-step-adelic-integral-finite-twist-places/), which [the law for one character](/entry/one-chart/) uses.

## Statement

Let $\psi$ be a standard additive character of the adeles and $S$ a double step (`Dbl2`) with spaces $B$, $J$, $B'$ and two Weil data. Its value $\mathrm{val}_S(c_1, c_2, f_1, f_2, \varphi, f, g, h_1, h_2)$ (`Dbl2.val`) is the period over $B'$, against $h_2 f$, of a lift of $\varphi$ built from $\omega(g,h_1)f_1$, $\omega(h_1,h_2)f_2$ and the coefficients $c_1, c_2$. We have not unfolded the period or the lift.

Let $Q_1, \dots, Q_r$ be local steps (`QStep`) at distinct split places $v_1, \dots, v_r$. Each $Q_i$ carries open compact groups $U_1, U_2$, local data $D_1, D_2$, $e_0$, finite sets $A_1, A_2$, coefficients $d_1(\gamma)$, $d_2(\gamma, \beta)$, $e_2(\beta)$, weights $w_1(\gamma)$, $w_2(\beta)$, and $\mathrm{vol}_J = ([K:U_1]\,[K:U_2])^{-1}$. Let $G_1, G_2$ be the groups of $J$ and $B'$ at the places $v_i$, and $R_1, R_2$ their Jacobi and Bessel subgroups.

**Theorem.** Assume that $\mu_i, \rho_i$ are Haar measures on $G_i, R_i$ that give volume $1$ to the points that are integral at every $v_i$; that $c_1, c_2$ are `Away` at each $Q_i$; that $f_1, f_2$ are vacuum at each $Q_i$; that $\varphi, f$ are continuous automorphic and $f$ is `Typed` at each $Q_i$; and that $g, h_1, h_2$ are $1$ at the places $v_i$. Then

$$\begin{aligned}&{\mathrm{Iter}_2\Bigl(\sum_a e_0(a)\, \mathrm{val}_S(c_1, c_2, D_1 f_1, D_2 f_2, \varphi, f, ga, h_1x, h_2y)\Bigr)}\\ &{\quad = \prod_i \mathrm{vol}_J^{(i)} \sum_{\gamma} \sum_{\beta} \prod_i w_1(\gamma_i) w_2(\beta_i)\,}\\ &{\qquad \mathrm{val}_S\bigl(c_1 * d_1(\gamma), c_2 * d_2(\gamma,\beta), f_1, f_2, \varphi, e_2(\beta) f, g, h_1, h_2\bigr).}\end{aligned}$$

We read the combination `PosOne.comb` as $\sum_a e_0(a) F(a)$; we have not unfolded it. Here $e_0$, $D_1$, $D_2$, $d_1$, $d_2$, $e_2$ stand for the convolution products of the local data over $i$, and $\gamma, \beta$ run over $\prod_i A_1^{(i)}$ and $\prod_i A_2^{(i)}$.

## Proof

`valQ_of_valQr` reduces `ValQ D` to `ValQr D r` for all $r$, the same statement with exactly $r$ places. Then induct on $r$.

- $r = 0$: `T.iteratedIntegralValueAtRPlaces_zero`. The groups at the empty set of places are trivial, so both quotient integrals are evaluations.
- $r \to r+1$: [`valQr_succ`](/entry/val-qr-succ/). It computes the integral at $v_1$ and applies the induction hypothesis to the other $r$ places.

## In the Lean code

The theorem is in [DoubleStepAdelicIntegralFiniteTwistPlaces.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/DoubleStepAdelicIntegralFiniteTwistPlaces.lean#L47). `ValQ` is in [IsOneComb.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/IsOneComb.lean#L183), and `ValQr` with `valQ_of_valQr` in [ValQOfValQr.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ValQOfValQr.lean#L73).

`ValQ` takes a predicate $P$ with $P(v) \iff v = v_i$ for some $i$. It carries no information; `valQ_of_valQr` replaces it by the set of the $v_i$.
