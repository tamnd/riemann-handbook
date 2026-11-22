---
id: vanish
title: Linear independence of twisted Satake power sums, by the pole of the Rankin-Selberg L-function
kind: theorem
decl: GlobalTheory.JSW.Rigid.vanish
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.JacquetShalikaRigidityHolds
covers: 2251
status: drafted
drafted_by: writer@claude
---
This lemma is the analytic core of [the Jacquet-Shalika rigidity theorem](/entry/jacquet-shalika-rigidity-holds/). It says that the power sums of the Satake parameters of distinct twisted unitary cuspidal representations are linearly independent over $\mathbb{Z}$. The proof compares the logarithms of Rankin-Selberg L-functions near $s = 1$.

## Statement

Let $E$ be a totally complex number field and $T$ a finite set of primes of $E$. Let $S$ be a finite set of pairs $p = (\sigma_p, t_p)$, where $\sigma_p$ is a unitary [[cuspidal representation|9AZ164C298]] of $\mathrm{GL}_a$ over $E$ with $a \geq 1$ that has Satake parameters at each $w \notin T$, and $t_p \in \mathbb{R}$. Let $c \colon S \to \mathbb{Z}$. Suppose that for all $w \notin T$ and $r \geq 0$
$$\sum_{p \in S} c(p)\, Nw^{-(r+1)t_p} \sum_{\alpha \in \mathrm{sat}(\sigma_p, w)} \alpha^{r+1} = 0.$$

**Theorem.** $c(p) = 0$ for all $p \in S$.

## Proof

For unitary $\sigma, \sigma'$ the Lean code defines
$$\log RS_T(\sigma, \sigma', x) = \sum_{w \notin T} \sum_{r \geq 0} \frac{p_{r+1}(\sigma, w)\, \overline{p_{r+1}(\sigma', w)}\, Nw^{-(r+1)x}}{r+1},$$
with $p_{r+1}(\sigma, w)$ the $(r+1)$st power sum of the Satake parameters. This is a logarithm of the partial L-function $L^T(x, \sigma \times \tilde\sigma')$.

1. Suppose some $c(p) \neq 0$. Among these $p$, take $p_0 = (\sigma_0, t_0)$ with the least $t_p$.
2. Multiply the hypothesis by $\overline{p_{r+1}(\sigma_0, w)}\, Nw^{-(r+1)(x - t_0)}/(r+1)$ and sum over $w$ and $r$. For $x > 1$ all the series converge (`summable_rsTerm`), and
$$\sum_{p} c(p)\, \log RS_T(\sigma_p, \sigma_0, x + t_p - t_0) = 0.$$
3. Take real parts and let $x \to 1^{+}$. If $t_p > t_0$, the term is bounded, because the series converges absolutely at $1 + (t_p - t_0)$ (`norm_logRS_add_le`). If $t_p = t_0$ and $\sigma_p \neq \sigma_0$, the real part is bounded, because $L^T(x, \sigma_p \times \tilde\sigma_0)$ has a nonzero finite limit (`abs_re_logRS_bdd`).
4. The term of $p_0$ itself tends to $+\infty$, because $L^T(x, \sigma_0 \times \tilde\sigma_0)$ has a pole at $1$ (`tendsto_re_logRS_self`).
5. Since $|c(p_0)| \geq 1$, the sum cannot be $0$ near $1$. This is a contradiction.

The two analytic facts are standard. The partial L-function $L(s, \pi \times \tilde\pi)$ has a simple pole at $s = 1$, and for $\pi \not\cong \pi'$ the function $L(s, \pi \times \tilde\pi')$ is finite and nonzero at $s = 1$ (H. Jacquet and J. Shalika, Amer. J. Math. 103, 1981; F. Shahidi, Amer. J. Math. 103, 1981).

## In the Lean code

The lemma is at [line 131 of JacquetShalikaRigidityHolds.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/JacquetShalikaRigidityHolds.lean#L131). The three bounds are at [line 38](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/JacquetShalikaRigidityHolds.lean#L38), [line 62](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/JacquetShalikaRigidityHolds.lean#L62) and [line 78](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/JacquetShalikaRigidityHolds.lean#L78). `rsTerm` and `logRS` are in [RsTerm.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/RsTerm.lean#L14), and `sat`, `UnrOutside`, `locL` and `partialL` are in [UnrOutside.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/UnrOutside.lean#L16).

The analytic facts enter through three statements in the same folder: `localRankinSelberg_logarithm_formula`, `rankinSelberg_partialL_tendsto_ne_zero_at_one` and `rankinSelberg_partialL_pole_at_one_conj`. Each is proved in one line, by `first | exact ...`, from the theorems `JSLog.logRankinSelberg`, `RSNonvan.tendsto_partialL_ne_zero` and `RSPole.rs_pole_conj`. We have not unfolded those three proofs. In the Lean form the pole is stated with a continuous $L(x) \geq 1$ and a limit $(x-1)L(x) \to c > 0$.
