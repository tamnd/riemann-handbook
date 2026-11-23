---
id: cf-of-fin-bound
title: The finite-place bound for a coefficient functional of a CM arc datum
kind: theorem
decl: GlobalTheory.ArcCM.cfOf_fin_bound
module: Development.AbelianVarietyTheory.Proofs.ThetaShiftProofs.CmArcDatumFunctionalFiniteIntegralityBound
covers: 386
status: drafted
drafted_by: writer@claude
---
This theorem bounds the denominator of the coefficient functional $\phi_d$ of an arc datum at each finite place, relative to the metrized line of the CM input. It is the proof of [`cmArcDatum_functional_finite_integrality_bound`](/entry/cm-arc-datum-functional-finite-integrality-bound/), which gives condition 1 of `NumGood` in [`numGood_of_famQ`](/entry/num-good-of-fam-q/). The local work is in [`finLocalAt_of_cmIn`](/entry/fin-local-at-of-cm-in/). This theorem turns its output into a bound on valuations.

## Statement

The statement is that of [`cmArcDatum_functional_finite_integrality_bound`](/entry/cm-arc-datum-functional-finite-integrality-bound/), with the same names: $\phi_d$, $N_n = $ `s.valLine` $\mu\, n$, the total weight $A$ of $a'$, and $e(w|\lambda)$. Assume `Known`, `ModelsAt`, `Std d` and $\Lambda \ge 1$. For $F$ in `intAt` with $\phi_d(F) \neq 0$,

$$\operatorname{ord}_w \phi_d(F) - \operatorname{ord}_w I_{N_n} \ge -e(w|\lambda)\, A\, m_\lambda, \qquad m_\lambda = \max\bigl(v_\lambda(d_E), v_\lambda(n')\bigr).$$

The CM input $s$ has a line $T$ and lines $\ell_x$ for the arc letters $x$, and $N_n = T^{-n} \otimes \bigl(\bigotimes_x \ell_x^{\mu_x}\bigr)^{-1}$.

## Proof

1. [`localArcIntegrality_of_cmNormalisedTrivialisation`](/entry/local-arc-integrality-of-cm-normalised-trivialisation/) gives `FinLocalAt`: a complete ultrametric field with $|\iota x| = r^{\operatorname{ord}_w x}$ and $0 < r < 1$, a scalar $\gamma$ with $|\gamma| = r^{-\operatorname{ord}_w I_T}$, scalars $\lambda_x$ with $|\lambda_x| = r^{-\operatorname{ord}_w I_{\ell_x}}$, and frame matrices with entries of norm at most $r^{-e(w|\lambda) m_\lambda}$. In this frame, $\gamma^{-n}$ times the evaluation of $F$ has norm at most $1$.
2. `evR_arc_isHomogeneous` writes the evaluation of $F$ as a polynomial in the arc letters, homogeneous of degree $A$.
3. `FinKey.coeff_bound` gives $|\iota\, \phi_d(F)| \le |\gamma|^n \prod_x |\lambda_x|^{\mu_x}\, \bigl(r^{-e(w|\lambda) m_\lambda}\bigr)^{A}$.
4. `FinPf.zpow_bound` takes logarithms to base $r$. `CMIn.fin_count_valLine` gives $\operatorname{ord}_w I_{N_n} = -n \operatorname{ord}_w I_T - \sum_x \mu_x \operatorname{ord}_w I_{\ell_x}$. The two combine to the claim.

The rest is bookkeeping.

## In the Lean code

The theorem is in [CmArcDatumFunctionalFiniteIntegralityBound.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/CmArcDatumFunctionalFiniteIntegralityBound.lean#L64). The same file proves `CMIn.fin_Tl_ne_zero`, `CMIn.fin_line_ne_zero` and `CMIn.fin_count_valLine`. `FinKey.coeff_bound` is in [ExistsCoeffNormOne.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/ArchimedeanQuadraticData/FinitePlaceArcs/ExistsCoeffNormOne.lean#L241). We have not unfolded `evR` or `arcNum`.

- The hypothesis $\Lambda \ge 1$ is never used: the proof introduces it as `_`.
- `Std d` is only passed on. Below, only its first part `d.OverBase` is used, and that part holds for every arc datum (`ArcDatum.overBase`).
