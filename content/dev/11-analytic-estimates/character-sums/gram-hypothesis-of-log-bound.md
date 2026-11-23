---
id: gram-hypothesis-of-log-bound
title: The Gram hypothesis from two logarithm bounds
kind: theorem
decl: Formalism.InvariantFactorPaths.MC.gram_hypothesis_of_log_bound
module: Formalism.ThetaLogCoordinates.PartnerMeanCoordinates.PartnerMeanProofs.GramHypothesisOfLogBound
covers: 508
status: drafted
drafted_by: writer@claude
---
This lemma proves the Gram hypothesis `GramDeterminantGradedHypothesis` from two bounds on $\log_p$ of the total degree. [The averaged bad-count bound](/entry/mc-theorem-mv7/) calls it once for each tie position. The lemma only selects one of two proved bounds and checks the arithmetic. The work is in `graded_bound_saturation_holds`, `graded_bound_pos_of_proj` and `restricted_saturation_holds`, which we did not open in full.

## Statement

Let $L$ be letters with $K+1$ rows and sign $+$ on the last row, total degree $d$, and thresholds $(J, M)$. The Gram hypothesis with constant $\kappa_4$ says: for each weight $w$, each $e$ and each $\mathbb{Z}_p$-basis $g_1, \dots, g_k$ of the graded lattice `grLat` (initial parts of order $e$ in $x_{K,\rho}$),

$$ \Bigl|\det\Bigl(\frac{\langle g_a, g_b\rangle}{\prod_j \deg_j!}\Bigr)\Bigr|_p \ge p^{-\kappa_4 k}. $$

**Lemma.** Let $r \ge 2$, $\rho = r - 1$, and let $\lambda$ satisfy $\lfloor\log_p(d + r - 1)\rfloor \le \lambda$ and $\lfloor\log_p(4d + r - 1)\rfloor \le \lambda$. If $(K + 7)\,r^2\lambda/2 \le \kappa_4$, then the Gram hypothesis holds for $L$ with $\kappa_4$.

## Proof

Put $e_1 = \binom r2 \lfloor\log_p(d + r - 1)\rfloor$ (`kapC`) and $c_0 = 2\binom r2 \lfloor\log_p(4d + r - 1)\rfloor$. Since $\binom r2 \le r^2/2$ (`choose_two_le`), both $e_1$ and $c_0/2$ are at most $r^2\lambda/2$. The lemma `hypPE_setLast` gives `HypP` and `HypE` with $e_1$ for $L$ with the last degree lowered to any $o \le \deg_K$ (`setLast`).

1. **$K = 0$.** `restricted_saturation_zero` gives the saturation input `ResSatL` with $c_0 = 0$. `graded_bound_saturation_holds` then needs $(K+5)e_1 = 5e_1 \le \kappa_4$. This holds since $5 \le 7$.
2. **$K \ge 1$.** `restricted_saturation_holds` gives `ResSatL` for these lowered letters, with a constant in $\log_p(4d' + r - 1)$ for a total degree $d' \le d$. `resSatL_mono` raises it to $c_0$. `graded_bound_pos_of_proj`, with `highest_vector_projection_holds`, needs $(K+3)e_1 + 2c_0 \le \kappa_4$. The left side is at most $(K + 3 + 4)\,r^2\lambda/2$.

The second log bound is not used when $K = 0$.

## In the Lean code

The lemma is in [GramHypothesisOfLogBound.lean](lean:Formalism/ThetaLogCoordinates/PartnerMeanCoordinates/PartnerMeanProofs/GramHypothesisOfLogBound.lean#L83). The Gram hypothesis is in [StatementT.lean](lean:Formalism/MahlerMeasure/StatementT.lean#L29). The two bounds are in [GramBoundUnconditionalOfSat.lean](lean:Formalism/ThetaLogCoordinates/FockResolutionOnto/FockMonomialProofs/GramBoundUnconditionalOfSat.lean#L135) and [GramBoundPosOfProjSat.lean](lean:Formalism/ThetaLogCoordinates/FockResolutionOnto/FockMonomialProofs/GramBoundPosOfProjSat.lean#L51). `ResSatL` asks that each integral element of a space `XSp` (not unfolded) is $p^{-c_0}$ times the initial part of an integral element of $Y$.
