---
id: harmonic-value-canonical-connection-eq-poly-deriv
title: Harmonic values of the canonical connection are derivatives of theta functions, as a statement
kind: theorem
decl: GlobalTheory.T.harmonicValue_canonicalConnection_eq_polyDeriv
module: Development.AbelianVarietyTheory.Proofs.CuspFormEvaluations.HarmonicValueCanonicalConnectionEqPolyDerivStatement
covers: 358
status: drafted
drafted_by: writer@claude
---
This theorem is a second name, used by the step [every character of literature](/step/every-character-of-literature/). Its proof only calls [harm-nab-eq-poly-deriv](/entry/harm-nab-eq-poly-deriv/), which has the same statement and the real proof.

## Statement

Assume `ChartIndepSt2`. Let $y$ be a complex framed point with an analytic uniformization $\Phi$ of dimension $g$ (`AnPt`), and let `nab` be a canonical connection (`IsNab`). Let $F_1, \dots, F_n$ be sections of the $k$-th power of the line bundle, and let $\theta_b$ be the function on $\mathbb{C}^g$ that reads $F_b$ in the frame of $\Phi$. Let $P$ be a harmonic polynomial (`HHa`) in the letters $(b, \ell)$. Then

$$\sum_{m} P_m \prod_b \nabla_y(F_b)(m_b) = \partial_P\Bigl(z \mapsto \prod_b \theta_b(z_b)\Bigr)(0),$$

where $m_b$ is the column of the multi-index $m$ at $b$ and $\partial_P$ is the constant coefficient differential operator `I2.polyDeriv` with the directions `letDir el`. In words: the harmonic polynomial evaluated on the canonical connection values equals $P$ as a differential operator applied to the product of theta functions at $0$.

## Proof

The proof is one tactic line: `first | exact @GlobalTheory.AnVal.harm_nab_eq_polyDeriv | ...`. The first branch closes the goal.

## In the Lean code

The theorem is in [HarmonicValueCanonicalConnectionEqPolyDerivStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/HarmonicValueCanonicalConnectionEqPolyDerivStatement.lean#L10). The proof it calls is in [HarmonicValueCanonicalConnectionEqPolyDeriv.lean](lean:Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/HarmonicValueCanonicalConnectionEqPolyDeriv.lean#L25). The hypothesis `ChartIndepSt2` is proved as `chartIndep` in [EmbeddingsDifferOnInteger.lean](lean:Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/EmbeddingsDifferOnInteger.lean#L98), so it is not a real assumption.
