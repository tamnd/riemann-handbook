---
id: i-holds
title: A lower bound for derivatives of translated theta sections
kind: theorem
decl: GlobalTheory.ThetaTorus.I_holds
module: Development.AbelianVarietyTheory.Proofs.TorusSplitting.GCauchyHolds
covers: 565
status: drafted
drafted_by: writer@claude
---
This theorem bounds from below the sum, over a set of translates of one theta section, of the squared size of a fixed derivative at $0$. It combines [the existence of one good section](/entry/j-holds/) with an orthogonal basis of translates by the [[Cauchy-Schwarz inequality|0RFWW56Y22]]. [The lower bound for the theta rule sum](/entry/theta-rule-sum-lower/) uses it.

## Statement

Let $X$ be a polarized torus datum `PT E` for a CM field $E$: a lattice $L$ in $V = \mathbb{C}^{d}$, stable under $\mathcal{O}_E$, on which $\operatorname{Im} H$ is integral and perfect, with a sign function $\varepsilon$. Let $\mathrm{Sec}(q, n)$ be the space of holomorphic $F$ on $V^n$ with $F(v + \gamma) = \varepsilon(\gamma)^q e^{q\pi H(v,\gamma) + q\pi H(\gamma,\gamma)/2} F(v)$ for $\gamma \in L^n$, where $\varepsilon(\gamma) = \prod_k \varepsilon(\gamma_k)$. Let $\|F\|^2_q$ be the mean of $|F(v)|^2 e^{-q\pi \operatorname{Re} H(v,v)}$ over a fundamental domain. Let $D$ be the differential operator given by the product $P_1$ of the powers of minors of the disjoint blocks `bs`, and let $J(n)$ be the explicit constant `Par.Jbound`.

**Theorem (`IStatement`).** Let $P$ be a set of parameters. Let $\pi$ be a linear map that commutes with $\mathcal{O}_E$, preserves $L$, multiplies $H$ by $q$ and has $\varepsilon(\pi x) = \varepsilon(x)^q$. Let $s \neq 0$ be in $\mathrm{Sec}(1, 1)$, and let $K$ be a set of representatives of the $b$ with $qb \in L^n$, modulo $\pi^{-1}L^n$. Put $s_0(v) = \prod_k s(\pi v_k)$ and let $U_b$ be the translation by $b$. Then
$$J(n)\, \|s\|_1^{2n} \leq \sum_{b \in K} |D(U_b s_0)(0)|^2.$$

## Proof

The proof is `iOf J_holds N_holds`. Here `N_holds` is `lemmaN dim_holds`, which returns `thetaBasis_holds`: the $U_b s_0$ for $b \in K$ lie in $\mathrm{Sec}(q, n)$, are pairwise orthogonal, have $\|U_b s_0\|_q^2 = \|s\|_1^{2n}$, and span $\mathrm{Sec}(q, n)$.

The proof of `iOf` runs as follows.

1. `J_holds` gives $F \in \mathrm{Sec}(q, n)$ with $\|F\|_q^2 = 1$ and $J(n) \leq |DF(0)|^2$.
2. By the span, $F = \sum_{b} l_b\, U_b s_0$. By orthogonality, $1 = \|s\|_1^{2n} \sum_b |l_b|^2$.
3. $D$ is linear (`polyDeriv_sum`), so $|DF(0)| \leq \sum_b |l_b|\, |D(U_b s_0)(0)|$.
4. Cauchy-Schwarz (`Finset.sum_mul_sq_le_sq_mul_sq`) gives $|DF(0)|^2 \leq \sum_b |l_b|^2 \cdot \sum_b |D(U_b s_0)(0)|^2$. Multiply by $\|s\|_1^{2n}$.

## In the Lean code

The theorem is at [GCauchyHolds.lean](lean:Development/AbelianVarietyTheory/Proofs/TorusSplitting/GCauchyHolds.lean#L34). The statements are in [GCauchyStatement.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/SquareIntegrability/GCauchyStatement.lean#L224), and `iOf` is in [ContDiffOfDifferentiableFd.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/SquareIntegrability/ContDiffOfDifferentiableFd.lean#L148). The real analytic content is in [`J_holds`](/entry/j-holds/). The lemma `lemmaN` names its hypothesis `_hd : DimStatement` and does not use it. We have not unfolded `thetaBasis_holds`.
