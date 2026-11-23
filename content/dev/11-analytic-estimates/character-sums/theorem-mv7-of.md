---
id: theorem-mv7-of
title: The averaged bad-count bound with the lattice hypotheses as inputs
kind: theorem
decl: Formalism.InvariantFactorPaths.MC.theoremMV7Of
module: Formalism.ThetaLogCoordinates.PartnerMeanCoordinates.PartnerMeanProofs.GramHypothesisOfLogBound
covers: 941
status: drafted
drafted_by: writer@claude
---
This theorem is [the averaged bad-count bound](/entry/mc-theorem-mv7/) with one more hypothesis: the lattice conditions `HypP`, `HypW` and the Gram bound at each grid point. The parent entry proves that hypothesis and calls this theorem. The proof only fixes the constants of [`theoremMXB`](/entry/theorem-mxb/) and checks arithmetic. The real content is in `theoremMXB`.

## Statement

The notation is that of [the parent entry](/entry/mc-theorem-mv7/).

**Theorem.** Assume all hypotheses of the parent theorem. Assume also that for each $n \in G$, $L_n$ satisfies `HypP` and `HypW` with $e_1 = \lfloor r^2\lambda \rfloor$, and that for each $i$ the truncation of $L_n$ to rows $\le \mathrm{pos}_i$ satisfies `GramDeterminantGradedHypothesis` with $\kappa_4 = (s+4)r^2\lambda$. Then the averaged bound of the parent entry holds.

## Proof

Apply `theoremMXB` with $N = 2s+1$ and

$$ X_b = \lfloor 8a + r \rfloor, \quad \kappa = 3(s+2)r^2\lambda, \quad \kappa_4 = (s+4)r^2\lambda, \quad e_1 = \lfloor r^2\lambda \rfloor. $$

The bound $\log_p X_b + 1 \le \lambda$ is `natLog_floor_lgSeg`. The size conditions of `theoremMXB` come from `SizeHypothesis` and `deg_le_total'`. The three conditions on $\kappa$ are linear in $r^2\lambda$, with $N + 2 = 2s + 3$:

- $\tfrac32 (2s+3) r^2\lambda \le 3(s+2) r^2\lambda$;
- $e_1 (2s+3) \le (2s+3) r^2\lambda \le 3(s+2) r^2\lambda$;
- $3\lambda + (s+4)r^2\lambda \le 3(s+2)r^2\lambda$, since $3\lambda \le (2s+2) r^2\lambda$ when $r^2 \ge 4$.

## In the Lean code

The theorem is in [GramHypothesisOfLogBound.lean](lean:Formalism/ThetaLogCoordinates/PartnerMeanCoordinates/PartnerMeanProofs/GramHypothesisOfLogBound.lean#L124). The statement `TheoremMV7Of` is in [ChainOrderLetters.lean](lean:Formalism/PolynomialDimension/ChainOrderLetters.lean#L38). `lgSeg` and `kapSeg` are in [DigitSumValuationBound.lean](lean:Formalism/PolynomialDimension/DigitSumValuationBound.lean#L12).

The proof introduces the hypotheses `hch` (`ChainOrderLetters`) and `hcond` (`ConditionShape`) on line 126 and never uses them. The hypothesis $a \ge 1$ is used only to make $8a + r$ positive.
