---
id: cm-arc-datum-functional-finite-integrality-bound
title: The integrality of the coefficient functional at the finite places (statement form)
kind: theorem
decl: GlobalTheory.T.cmArcDatum_functional_finite_integrality_bound
module: Development.AbelianVarietyTheory.Proofs.ThetaShiftProofs.CmArcDatumFunctionalFiniteIntegralityBoundStatement
covers: 388
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`cfOf_fin_bound`](/entry/cf-of-fin-bound/), which has the real content. Its one user is [`numGood_of_famQ`](/entry/num-good-of-fam-q/), where it gives condition 1 of `NumGood`: the bound of the coefficient functional at the finite places.

## Statement

Let $E$ be a CM field with a host datum, a datum $D_w$, a level, a moduli space $X_o$ and a coefficient datum with number field $k$. Let $K_1 \supseteq k$ be a number field and $d$ an arc datum over $K_1$ with monomial $\mu$, integer $j_0$ and coefficient functional $\phi_d$ (`cfOf`), as in [the entry for `qat_of_kill_detect`](/entry/qat-of-kill-detect/). Let $s$ be CM input data for $d$ with parameters $n' > 0$, $\Lambda$, $c_1$, and let $N_n = $ `s.valLine` $\mu\, n$ be its metrized line (see [the entry for `numGood_of_famQ`](/entry/num-good-of-fam-q/)).

**Theorem.** Assume `Known`, `ModelsAt` $X_o$, `Std d` and $\Lambda \ge 1$. Let $\lambda$ be a prime of $k$ and $w$ a prime of $K_1$ over $\lambda$. Let $a'$ be a weight with total weight $A$ (`absA`) and $n \in \mathbb{N}$. Let $F$ be a section of weight $(a', n)$ with $v(F) \ge 0$ for each valuation $v$ in `valSet` over $\lambda$ (the set `intAt`). If $\phi_d(F) \neq 0$, then

$$\operatorname{ord}_w \phi_d(F) - \operatorname{ord}_w I_{N_n} \ge -e(w|\lambda)\, A \max\bigl(v_\lambda(d_E), v_\lambda(n')\bigr).$$

So, at primes $\lambda$ prime to $d_E n'$, $\phi_d(F)$ lies in the ideal $I_{N_n}$ locally at $w$.

## Proof

The statement is the same as that of `GlobalTheory.ArcCM.cfOf_fin_bound`, and the proof applies it. That proof uses [`localArcIntegrality_of_cmNormalisedTrivialisation`](/entry/local-arc-integrality-of-cm-normalised-trivialisation/), `evR_arc_isHomogeneous` and `FinKey.coeff_bound`.

## In the Lean code

The theorem is in [CmArcDatumFunctionalFiniteIntegralityBoundStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/CmArcDatumFunctionalFiniteIntegralityBoundStatement.lean#L10). The proof is `first | exact @GlobalTheory.ArcCM.cfOf_fin_bound | ...`, a tactic that tries the alias in three forms. `intAt` is in [FinLocalCutAt.lean](lean:Development/AbelianVarietyTheory/Definitions/ArchimedeanThetaValues/FinLocalCutAt.lean#L148).
