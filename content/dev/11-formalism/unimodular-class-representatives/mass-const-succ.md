---
id: mass-const-succ
title: The mass constant, from one dimension to the next
kind: theorem
decl: Formalism.HermitianLattices.Ext.L3.massConst_succ
module: Formalism.GL3MeanSquares.GenusMeanAsymptotics.UnimodularClassRepresentatives.MassConstSucc
covers: 334
status: drafted
drafted_by: writer@claude
---
This theorem is the induction step of a mass formula for Hermitian lattices. If the mass of every integral lattice of dimension $m-1$ is a constant $c$ times a product of local factors, then the same holds in dimension $m$ with the constant $c \cdot \rho(m)$. The proof counts the vectors of bounded norm in the genus in two ways. Its callers are `massConst_all`, which runs the induction from dimension $1$, and `cMass_spec` in `Assemble.lean`. In the spine it is below the step [EveryCharacter from theta integrals and local matching](/step/theta-local-matching/).

## Statement

Let $K$, $F$ and the local factors $\lambda_{\mathfrak p}(L)$ be as in [the local identity](/entry/li-stat/). For an integral lattice $L$ in a totally positive definite Hermitian space $(V,h)$ over $K$, let
$$\operatorname{mass}(L) = \sum_{M} \frac{1}{\#\operatorname{Aut}(M)}, \qquad \lambda(L) = \prod_{\mathfrak p} \lambda_{\mathfrak p}(L),$$
where $M$ runs over representatives of the isometry classes in the genus of $L$, and $\mathfrak p$ over the maximal ideals of $\mathcal O_F$. Say $\mathrm{MassConst}(m, c)$ holds if $\operatorname{mass}(L) = c\, \lambda(L)$ for all such $L$ with $\dim V = m$.

Let $d$ be the number of infinite places of $K$, $v = \lvert d_K \rvert^{1/2d} / 2$, and $\eta$ the character of $K/F$ as in [the local identity](/entry/li-stat/). Put
$$\rho(m) = \Bigl(\frac{(m-1)!}{\pi^m}\Bigr)^{d} \frac{v^{dm}}{\sqrt{(2v)^d}}\, L_F(m, \eta), \qquad L_F(m,\eta) = \prod_{\mathfrak p} \bigl(1 - \eta(\mathfrak p)^m N\mathfrak p^{-m}\bigr)^{-1}.$$

**Theorem.** Assume `HermRepUnram`: for each field $K'$ as above and all totally positive $a, b, n \in K'$ fixed by the involution, there are $s, t \in K'$ with $a s \bar s + b t \bar t = n$. Assume [the local identity](/entry/li-stat/). Let $m \geq 2$ and $c > 0$. If $\mathrm{MassConst}(m-1, c)$ holds, then $\mathrm{MassConst}(m, c\, \rho(m))$ holds.

## Proof

Fix $L$ of dimension $m$ and representatives $M$ of its genus (`exists_classReps`). Let $B(M, T)$ be the number of $x \in M$ with $\operatorname{Re} \varphi(h(x,x)) \leq T$ for each embedding $\varphi$ (`ballCount`). Divide $\sum_M B(M, j^2) / \#\operatorname{Aut}(M)$ by $j^{2dm}$ and let $j \to \infty$.

1. **Volume.** `tendsto_ballCount` gives the limit $(\pi^m/m!)^d / (v^{dm} \sqrt{N \operatorname{disc} L})$ for each $M$; all $M$ in the genus have the same discriminant. So the sum tends to $\operatorname{mass}(L)$ times this (`Step.tendsto_left`).
2. **Values.** Sort the vectors by $n = h(x,x)$. Then the sum is $\operatorname{mass}(L) + \sum_{n} r(L, n)$, where $n$ runs over the totally positive $n \in \mathcal O_F$ in the box of size $j^2$ and $r(L,n)$ is the mass of representations of $n$ (`sum_ballCount_eq`). The lemma `repMass_eq` uses `HermRepUnram`, the local identity and $\mathrm{MassConst}(m-1, c)$ to write $r(L,n) = c\, \lambda(L)\, (\sqrt{N \operatorname{disc} L})^{-1} N(n)^{m-1} S(L, n)$, with a singular series $S$ (`singS`). Then `tendsto_singS_sum` gives the limit of the averaged sum, $m^{-d} (2v)^{-d/2} L_F(m, \eta)$. The term $\operatorname{mass}(L)/j^{2dm}$ tends to $0$ (`Step.tendsto_right`).

The two limits are equal. `Step.final_algebra` solves for $\operatorname{mass}(L)$, with $m! = m \cdot (m-1)!$. Then `massRatio_eq_lvalue` identifies the constant with $\rho(m)$ as the Lean code defines it.

## In the Lean code

The theorem is in [MassConstSucc.lean](lean:Formalism/GL3MeanSquares/GenusMeanAsymptotics/UnimodularClassRepresentatives/MassConstSucc.lean#L99), with `Step.tendsto_left`, `Step.tendsto_right`, `Step.final_algebra` and `Step.normD_pos` in the same file. `MassConst` is in [LocalDensityRatio.lean](lean:Formalism/GL3MeanSquares/GenusMeanAsymptotics/UnimodularClassRepresentatives/LocalDensityRatio.lean#L114) and `massRatioRightSide` in [StatementMass.lean](lean:Formalism/HermitianLattices/StatementMass.lean#L40). There $\rho(m)$ is written with an Euler product over the primes of $K$ (`lValEta`); `massRatio_eq_lvalue` rewrites it over $F$. We have not unfolded the proofs of `tendsto_ballCount`, `tendsto_singS_sum`, `sum_ballCount_eq` or `repMass_eq`.

The hypothesis $c > 0$ (`hc0`) is never used in the proof.
