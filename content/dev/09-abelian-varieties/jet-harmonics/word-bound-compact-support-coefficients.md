---
id: word-bound-compact-support-coefficients
title: The word bound for compactly supported functions, restated
kind: theorem
decl: GlobalTheory.T.wordBound_compactSupportCoefficients
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.WordBoundCompactSupportCoefficientsStatement
covers: 341
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`HatNF.wordBound_cptCoef`](/entry/word-bound-cpt-coef/). It has the same statement and its proof only calls that theorem. [`wordBound_decay`](/entry/word-bound-decay/) takes its constants and operators from it and then extends the bound to decaying functions.

## Statement

We use the notation and the predicate `WordBound` of [the entry for `wordBound_decay`](/entry/word-bound-decay/).

**Theorem.** Let $a \colon \mathbb{N} \to \mathbb{N}$ satisfy `BasicLiftAll a`. Let $p$ be a place datum and $w$ a cut word for $p$. Then there are $C$, $J$ and differential operators $\Theta_1, \dots, \Theta_s$ such that `WordBound p (a r) w C J Θs` holds for all pairs $(\varphi, f)$ with $\varphi \colon \mathbb{R} \to \mathbb{R}$ smooth and $f$ compactly supported in the sense of `CptCoef`: $f$ is smooth on $G$, it vanishes outside a ball, and $G \ge \varepsilon$ on its support for some $\varepsilon > 0$.

Unlike the decaying case, there is no constant $C_b$, no hypothesis `InDDplus2` and no bound $|w| \le N$.

## Proof

The proof is the term `GlobalTheory.HatNF.wordBound_cptCoef`. There is nothing else. The proof of that theorem builds a normal form for the operators of $p$ (`normal_form_actual`), applies the radial pointwise bound [`T.wordOperator_radial_pointwise_bound`](/entry/word-operator-radial-pointwise-bound/), and lifts the radial operators to differential operators.

## In the Lean code

The theorem is at [WordBoundCompactSupportCoefficientsStatement.lean line 6](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/WordBoundCompactSupportCoefficientsStatement.lean#L6). The proof is the usual `first | exact ... | ...` wrapper of the `T.` restatement files. `CptCoef` is in [RealInputsClosedAdmissibleSettings.lean](lean:Formalism/HermitianCurvature/RealInputsClosedAdmissibleSettings.lean#L56).
