---
id: local-arc-integrality-of-cm-normalised-trivialisation
title: Local integrality of an arc datum in the CM frame, as a named statement
kind: theorem
decl: GlobalTheory.T.localArcIntegrality_of_cmNormalisedTrivialisation
module: Development.AbelianVarietyTheory.Proofs.ThetaShiftProofs.LocalArcIntegralityOfCmNormalisedTrivialisationStatement
covers: 338
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`finLocalAt_of_cmIn`](/entry/fin-local-at-of-cm-in/). It has the same statement, and its proof only applies that lemma. [`cfOf_fin_bound`](/entry/cf-of-fin-bound/) uses it to bound one coefficient of an arc datum at a finite place. The real content is in the entry for `finLocalAt_of_cmIn`.

## Statement

Let $d$ be an arc datum over a number field $K_1$, with a CM input $s$: an integer $n' > 0$, a line $T$ and lines $\ell_x$. Let $w$ be a prime of $K_1$ above a prime $\lambda$ of $K = c.F$, and $m_\lambda = \max\bigl(v_\lambda(d_E), v_\lambda(n')\bigr)$.

**Theorem.** Assume `Known`, `ModelsAt Xo c` and `Std d`. Then for every weight $(a', n)$, `FinLocalAt` holds at $w$ with the exponents $-\operatorname{ord}_w I_T$ for $\gamma$, $-\operatorname{ord}_w I_{\ell_x}$ for the scalars, and $e(w|\lambda)\, m_\lambda$ for the frame matrix, for all sections in `intAt Xo c a' n λ`. The entry for `finLocalAt_of_cmIn` states `FinLocalAt` in full.

## Proof

The proof is `finLocalAt_of_cmIn`, applied to the same arguments.

## In the Lean code

The theorem is in [LocalArcIntegralityOfCmNormalisedTrivialisationStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/LocalArcIntegralityOfCmNormalisedTrivialisationStatement.lean#L10). The proof is `first | exact @GlobalTheory.ArcCM.finLocalAt_of_cmIn | ...`, so the two statements are the same up to elaboration. Of the hypothesis `Std d`, only the part `d.OverBase` is used below, and that part holds for every arc datum.
