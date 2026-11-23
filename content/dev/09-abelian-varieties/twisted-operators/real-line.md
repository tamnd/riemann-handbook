---
id: real-line
title: The periods of the row test factor through one functional
kind: theorem
decl: GlobalTheory.RowReal.realLine
module: Development.AbelianVarietyTheory.Proofs.TwistedOperators.RealLine
covers: 418
status: drafted
drafted_by: writer@claude
---
This theorem proves the fact `RealLine` for all large admissible choices. [The unfolding of the iterated theta lift](/entry/twisted-theta-integral-unfolding/) uses it directly: it lets the sum of periods on the right side of the unfolding be written as one number $\ell(\sigma)$ times a constant. It is a short deduction from [`rowTest_realPlaces_definitePeriods_onOneLine`](/entry/row-test-real-places-definite-periods-on-one-line/), which carries the content.

## Statement

For a pair $P = (P_1, P_2)$ of polynomial data on the column and on the row, and a pure datum $d$, let $\mathcal{P}_M(P, d)$ be the period `defPer`: the integral over a fundamental domain of the lift of the column function $\varphi_a$ along the column times the lift of $F_y$ along the row, with Fock vectors given by $P$ and $d$. For finite combinations $\sigma$ of pairs and $\tau$ of pure data, let $\mathcal{P}_M(\sigma, \tau) = \sum_{P, d} \sigma_P \tau_d\, \mathcal{P}_M(P, d)$ (`defTot`).

Call $(t, a, \beta, M, \tau)$ *admissible* if the sum condition `SumOK` holds at $(t, \Phi_a)$, $\beta$ is in the support, $M$ is a volume for the term at $\beta$ (`IsTermVol`), and $\tau$ is an expansion of the term at $\beta$.

**Theorem.** For all large admissible choices $\mathrm{ch}$ (in the sense of `Big`) there is a nonzero function $\ell$ on pairs $P$ with:

1. for each admissible $(t, a, \beta, M, \tau)$ and each $y$ there is $K \in \mathbb{C}$ with $\mathcal{P}_M(\sigma, \tau) = \bigl(\sum_P \sigma_P \ell(P)\bigr) K$ for all $\sigma$;
2. for each $z \in \mathbb{C}$ there is $\sigma$ with $\sum_P \sigma_P \ell(P) = z$, and $\sigma = 0$ if $z = 0$.

The function $\ell$ does not depend on $t$, $a$, $\beta$, $M$, $\tau$ or $y$.

## Proof

The input statement `PeriodsOnLine` gives a function $\ell_0$ such that for each admissible tuple, each $d$ in the support of $\tau$ and each $y$, the vector $P \mapsto \mathcal{P}_M(P, d)$ is a multiple $\kappa_d \ell_0$. The lemma `realLine_of_periodsOnLine` turns this into `RealLine`. If $\ell_0 \neq 0$, put $\ell = \ell_0$. If $\ell_0 = 0$, all periods vanish; put $\ell = 1$ and $\kappa_d = 0$. In both cases $K = \sum_d \tau_d \kappa_d$ (lemma `sum_sum_line`). For clause 2, pick $P_0$ with $\ell(P_0) \neq 0$ and put $\sigma = (z / \ell(P_0))\, \delta_{P_0}$.

## In the Lean code

The theorem is in [RealLine.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/RealLine.lean#L9). Its proof is `big_mono` with `realLine_of_periodsOnLine` applied to `GlobalTheory.T.rowTest_realPlaces_definitePeriods_onOneLine`. `RealLine`, `PeriodsOnLine` and the lemma are in [RealLineOfPeriodsOnLine.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/RealLineOfPeriodsOnLine.lean#L14).

- Clause 2 follows from $\ell \neq 0$ alone.
- The word "real" in the name does not mean real values: $\ell$ is complex valued.
- We have not unfolded `liftP`, `movedVec` or `W.fock`.
