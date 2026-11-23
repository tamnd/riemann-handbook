---
id: theorem-mxb
title: The averaged bad-count bound with free constants
kind: theorem
decl: Formalism.InvariantFactorPaths.MC.theoremMXB
module: Formalism.ThetaLogCoordinates.PartnerMeanCoordinates.PartnerMeanProofs.GramHypothesisOfLogBound
covers: 937
status: drafted
drafted_by: writer@claude
---
This theorem is the general form of [the averaged bad-count bound](/entry/mc-theorem-mv7/). The constants $X_b$, $\kappa$, $\kappa_4$, $\lambda$ and $e_1$ are free, and a list of inequalities links them. [`theoremMV7Of`](/entry/theorem-mv7-of/) chooses them. The Lean proof is one line: `theoremMXB_of_point` applied to six inputs. The averaging argument is in `theoremMXB_of_point`, and we give it here.

## Statement

The notation is that of [the parent entries](/entry/mc-theorem-mv7/), with letters $L$ of any length $N$ and $\varepsilon_i = 2S_i/Y_i + (2\kappa + 2S_i\lambda/Y_i)/E$.

**Theorem.** Let $p \ne 2$, $r \ge 2$, $\rho = r - 1$, $T$ admissible for $L$, $E \ge 1$, $Y_i \ge 1$, $d_i > 0$ prime to $p$ and $S_i \le n_{0,i}$. Assume that each degree of $L_{n^{\mathrm{top}}}$, each $2S_i$, $Y_i$, $z_i + \deg_{\mathrm{pos}_i}$ and $r$ are at most $X_b$, and that

$$ \log_p X_b + 1 \le \lambda, \quad \tfrac32 (N+2) r^2 \lambda \le \kappa, \quad e_1 (N+2) \le \kappa, \quad 3\lambda + \kappa_4 \le \kappa. $$

Assume `HypP`, `HypW` (with $e_1$) and the Gram bound (with $\kappa_4$) at each grid point, as in [`theoremMV7Of`](/entry/theorem-mv7-of/). Then the averaged bound of the parent entry holds.

## Proof

Let $L^{(i)}$ be the truncation of $L_n$ to rows $\le \mathrm{pos}_i$. For each weight $w$, `AdaptedBasisExists` gives a $\mathbb{Z}_p$-basis $f_1, \dots, f_{m_w}$ of the integral part of the weight space `MMw` of $L^{(i)}$, adapted to the filtration by order. Let $A_w(y)$ be the matrix $p^{\lceil\kappa\rceil}\,\Gamma(y; f_a, f_b)$, where $\Gamma$ is `tieGam` (built from `freeze`, which we did not unfold). `SmithZp` gives a Smith form of $A_w(y)$. Let $c_w(y)$ be the number of its diagonal entries of norm $< p^{-E}$. Only the weights in a finite box have `MMw` $\ne 0$.

The lemma `grid_average` says: if $\mathrm{bad}(n) \le \sum_i B_i(n)$ on the grid, and for each $i$ and $n$ the sum of $B_i(n[i \mapsto y])$ over the $Y_i$ values $y$ is at most $Y_i\,\varepsilon_i\,D_i(n)$, then the average of bad is at most $\sum_i \varepsilon_i$ times the average of $D_i$. Here $D_i(n) = \dim Y(L_{n[i\mapsto n^{\mathrm{top}}_i]})$ and

$$ B_i(n) = \sum_w c_w(n_i)\, \dim YY_i(n, f^{(w)}), $$

with $f^{(w)}$ a nonzero element of `MMw` and $YY_i$ the space `YYsp`.

1. **Pointwise.** `PointMX` gives $\mathrm{bad}(n) \le \sum_i B_i(n)$. It uses `HypP`, `HypW` and the first two bounds on $\kappa$.
2. **Monotone dimension.** `WeightSpaceDimMonotone`: $\dim YY_i$ does not decrease as $n_i$ grows. So each $\dim YY_i(n[i\mapsto y], f^{(w)})$ is at most its value at the top.
3. **Mean count.** $L^{(i)}$ does not depend on $n_i$. So [`meanGamX`](/entry/mean-gam-x/) applies to one basis along the progression $n_{0,i} + d_i j$. It gives $\sum_y c_w(y) \le Y_i\, m_w\, \varepsilon_i$, with $\kappa_i = ((\mathrm{pos}_i + 4) r + 6)\lambda \le \kappa$ and $\kappa_i + 3\lambda + \kappa_4 \le 2\kappa$.
4. **Count of weights.** `MonoCount`: $\sum_w m_w \dim YY_i(n, f^{(w)}) = \dim Y(L_n)$.

Steps 2 to 4 give the second hypothesis of `grid_average`.

## In the Lean code

The theorem is in [GramHypothesisOfLogBound.lean](lean:Formalism/ThetaLogCoordinates/PartnerMeanCoordinates/PartnerMeanProofs/GramHypothesisOfLogBound.lean#L17). The statement is in [TheoremMXB.lean](lean:Formalism/ThetaLogCoordinates/PartnerMeanCoordinates/TheoremMXB.lean#L118), with `PointMX` at line 93. The proof above is [TheoremMXBOfPoint.lean](lean:Formalism/ThetaLogCoordinates/PartnerMeanCoordinates/PartnerMeanProofs/TheoremMXBOfPoint.lean#L7), and `grid_average` is in [TheoremM.lean](lean:Formalism/MahlerMeasure/MahlerMeasureProofs/TheoremM.lean#L256).

The pointwise input is `pointMX_of_partner` applied to `bad_criterion_holds`, `tieOpsX_main` and `partner_condition_holds`. Each input except `meanGamX` is written `first | exact A | exact B`, which tries a list of alternative names (for example `Top.smithZp` or `smith_form_p_adic_integers`, `bad_criterion_holds` or `Top.badCrit`).
