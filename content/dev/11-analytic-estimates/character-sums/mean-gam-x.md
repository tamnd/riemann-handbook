---
id: mean-gam-x
title: The mean count of small Smith entries along a progression
kind: theorem
decl: Formalism.InvariantFactorPaths.MC.meanGamX
module: Formalism.ThetaLogCoordinates.PartnerMeanCoordinates.PartnerMeanProofs.GramHypothesisOfLogBound
covers: 336
status: drafted
drafted_by: writer@claude
---
This theorem is a pass-through. It applies `meanGamX_of` to four proved statements: `GamDeg`, `GamLead`, `GamIntC` and `WindowFullAP`. [`theoremMXB`](/entry/theorem-mxb/) uses it in its mean count step. The mathematics is in `meanGamX_of` and the four inputs, which have no entries.

## Statement

Let $L$ be letters with $K+1$ rows and sign $+$ on the last row. Let $f_1, \dots, f_m$ be a $\mathbb{Z}_p$-basis of the integral weight space `MMwZ`, adapted to the filtration `FilE` by the order in the variable $x_{K,\rho}$. Let $\Gamma(y; f, g)$ be `tieGam`. For $j < Y$ let $U_j\,\mathrm{diag}(\delta_j)\,V_j$ be a Smith form over $\mathbb{Z}_p$ of $\bigl(p^{\lceil\kappa\rceil}\,\Gamma(s + dj; f_a, f_b)\bigr)_{a,b}$, with $d > 0$ prime to $p$ and $s \ge \deg L$.

**Theorem.** Assume $E \ge 1$, that $2\deg L$, $z + \deg_K$, $Y$ and $r$ are at most $X_b$, that $\log_p X_b + 1 \le \lambda$ and $((K+4)r + 6)\lambda \le \kappa$, and the Gram bound with $\kappa_4$. Then

$$ \frac1Y \sum_{j<Y} \#\{a : |\delta_j(a)|_p < p^{-E}\} \le m\Bigl(\frac{2\deg L}{Y} + \frac{1}{E}\Bigl(\kappa + 3\lambda + \kappa_4 + \frac{2\deg L\,\lambda}{Y}\Bigr)\Bigr). $$

## Proof

`meanGamX_of` writes $p^{c}\,\Gamma(y; f_a, f_b)$ as an integral combination of $\binom{y}{k}$, with $c \le \kappa$ (`GamIntC`). This gives a matrix of polynomials in a binomial basis. Its determinant is a constant times a product of linear factors over an algebraic closure of $\mathbb{Q}_p$. `GamDeg` bounds the degrees. `GamLead` gives the leading coefficients as Fock pairings of initial parts $\mathrm{in}(f_a)$, and the Gram bound gives a lower bound for their determinant. Then `WindowFullAP` counts the Smith entries of norm $\le p^{-E}$ along $s + dj$, and this count is at least the count with $<$.

## In the Lean code

The theorem is in [GramHypothesisOfLogBound.lean](lean:Formalism/ThetaLogCoordinates/PartnerMeanCoordinates/PartnerMeanProofs/GramHypothesisOfLogBound.lean#L11). `MeanGamX` is in [TheoremMXB.lean](lean:Formalism/ThetaLogCoordinates/PartnerMeanCoordinates/TheoremMXB.lean#L7) and `meanGamX_of` in [NatLogLeOfLe.lean](lean:Formalism/ThetaLogCoordinates/PartnerMeanCoordinates/PartnerMeanProofs/NatLogLeOfLe.lean#L95). Each input is chosen by `first | exact A | exact B`, which tries a list of alternative names. We did not unfold `freeze` inside `tieGam`.
