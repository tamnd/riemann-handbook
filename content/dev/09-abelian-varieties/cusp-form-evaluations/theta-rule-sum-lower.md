---
id: theta-rule-sum-lower
title: A lower bound for the sum of squared values of theta rules over level classes
kind: theorem
decl: GlobalTheory.ThetaLower.thetaRule_sum_lower
module: Development.AbelianVarietyTheory.Proofs.CuspFormEvaluations.SumLeFinsumOfSurjectsOntoFinset
covers: 646
status: drafted
drafted_by: writer@claude
---
This theorem is used by the step [every character of literature](/step/every-character-of-literature/). It bounds from below the sum of $\lvert f_t(y)\rvert^2$, where the $f_t$ are theta rules (values of the canonical connection on level $M$ theta sections, combined by a harmonic polynomial) and $t$ runs over all tuples of level classes. The bound is the torus bound `I_holds`, carried to the point $y$.

## Statement

The data: a CM field $E$, a datum `Dw` with integers $p, q$, multiplicities $\mathrm{mult}(\tau)$ and a lattice $\Lambda$, a level $l$ with integer $M$ and ideal $\bar M$, a coefficient field $F$ with $\sigma \colon F \to \mathbb{C}$, and a canonical connection `nab` (`IsNab`). Assume:

- `ChartIndepSt2`: the chart value of the connection does not depend on the chart;
- an unfolding $U$ (`IsUnf`, `GoodEmb`) and a point $y = U(k, x)$ whose frame $x$ is orthogonal, with $\lvert\tau(\xi_0)\rvert = x_R$ for all $\tau$;
- $\alpha \in \mathcal{O}_E$ with $\alpha\bar\alpha = M$ and $\bar M = (\bar\alpha)$;
- $P_1$ a harmonic polynomial in `harmA` that is a product of blocks (`IsBlockProd`);
- `RunOK`: for each torus of rank $r$ with a dimension at most $m$ there are parameters `Par`; and $p \le m$ or $q \le m$.

Then there are a torus $T$ of rank $r$ and parameters $\Pi$ with $\Pi.q = M$, $\Pi.m = m$ and a fixed phase $\Pi.\mathrm{ph}$, such that for every family $f$ indexed by $t \in (\Lambda/\bar M\Lambda)^n$, with $f_t$ a theta rule for $P_1$ at the representatives of $t$:

$$\Bigl(\frac{2x_R}{M}\Bigr)^{\deg P_1} J_n(\Pi) \le \sum_t \lvert f_t(y)\rvert^2 .$$

Here $J_n(\Pi) = 4^{-n}\bigl(6(2d^*)^{d^*/2}\bigr)^{-n} 2^{-(r+2)\deg P_1} e^{-2\pi n C_\chi \mathrm{ph}/M}$ is `Par.Jbound`, with $d^* = 2fm$ for the integer $f$ = `PT.f E`.

## Proof

1. Choose a unit frame `Wu` at $y$. Its Hermitian matrix is $2x_R I$ (`hm_eq_diagonal`).
2. Build a torus $T$ with the same rows (`exists_torusOf_rows`) and check that its phase is $\Pi.\mathrm{ph}$ (`isTorusAt_of_isTorusOf`).
3. Rename the variables of $P_1$ to the torus blocks (`blockProd_rename`).
4. The theta function of `Wu` gives a section $s \ne 0$ of $L^2$ norm $1$ on $T$ (`theta_section_l2_torus`).
5. Get a finite set $K$ of level translates (`isReps_level_translates`) and the parameters $\Pi$ from `RunOK`.
6. `I_holds` gives $J_n(\Pi) \le \sum_{b \in K} \lvert \partial_{P_1} (T_b s)(0)\rvert^2$.
7. Each point of $K$ comes from some $t$. By `sum_le_finsum`, the sum over $K$ is at most the sum over all $t$, if each term for $t$ equals the term for its image.
8. That equality: `thetaRule_value_periods` writes $f_t(y)$ as $M^{-\deg P_1}$ times a polynomial derivative of a product of translated theta functions. `value_torus` moves this to $T$ with a factor $\kappa$, $\lvert\kappa\rvert^2 = M^{\deg P_1}$ (`exists_kappa`). `norm_sq_value` then gives the factor $(2x_R/M)^{\deg P_1}$.

## In the Lean code

The theorem is at [SumLeFinsumOfSurjectsOntoFinset.lean](lean:Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/SumLeFinsumOfSurjectsOntoFinset.lean#L240). The helpers `exists_kappa` (L114), `sum_le_finsum` (L139), `value_torus` (L190) and `norm_sq_value` (L232) are in the same file. `thetaRule_value_periods` is in [ThetaRuleValuePeriods.lean](lean:Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/ThetaRuleValuePeriods.lean#L22), and `I_holds` is in [GCauchyHolds.lean](lean:Development/AbelianVarietyTheory/Proofs/TorusSplitting/GCauchyHolds.lean#L34). `Par` and `Jbound` are in [GCauchyStatement.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/SquareIntegrability/GCauchyStatement.lean#L156).

The module is named after the helper `sum_le_finsum`, not after this theorem. The hypothesis `ChartIndepSt2` is proved as `chartIndep` in [EmbeddingsDifferOnInteger.lean](lean:Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/EmbeddingsDifferOnInteger.lean#L98), so it is not a real assumption.
