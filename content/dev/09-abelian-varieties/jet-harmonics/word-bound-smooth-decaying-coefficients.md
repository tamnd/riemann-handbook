---
id: word-bound-smooth-decaying-coefficients
title: The word bound for smooth decaying functions, restated
kind: theorem
decl: GlobalTheory.T.wordBound_smooth_decaying_coefficients
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.WordBoundSmoothDecayingCoefficientsStatement
covers: 349
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`HatNF.wordBound_decay`](/entry/word-bound-decay/). It has the same statement and its proof only calls that theorem. [`top_density_dominated`](/entry/top-density-dominated/) uses it in its first step, to bound the word vectors of $(\varphi \circ G) f$ at a point by the vectors of finitely many derivatives of $f$.

## Statement

**Theorem.** Let $a \colon \mathbb{N} \to \mathbb{N}$ satisfy `BasicLiftAll a`, and let $C_b \in \mathbb{R}$. There is $C_c$ with this property. Let $p$ be a place datum with `InDDplus2` for $C_b$, let $N \in \mathbb{N}$, and let $w$ be a cut word with $|w| \le N$. Then there are $C$, $J$ and differential operators $\Theta_1, \dots, \Theta_s$ such that `WordBound p (a r) w C J Θs` holds for all pairs $(\varphi, f)$ of this kind: for some $e \in \mathbb{N}$ and $A \in \mathbb{R}$, $\varphi$ is a cut power of degree $e$, $f$ is smooth on $G$ with decay of order $A$ for all its derivatives, and $C_c (r+1)^4 (N n^2 + n^3) \le A - (2r+2)e$.

The predicate `WordBound` and the words "cut power" are defined in [the entry for `wordBound_decay`](/entry/word-bound-decay/).

## Proof

The proof is the term `GlobalTheory.HatNF.wordBound_decay`. There is nothing else. The approximation argument is in [`wordBound_decay`](/entry/word-bound-decay/), and the bound for compactly supported functions that it extends is in [`wordBound_cptCoef`](/entry/word-bound-cpt-coef/).

## In the Lean code

The theorem is at [WordBoundSmoothDecayingCoefficientsStatement.lean line 6](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/WordBoundSmoothDecayingCoefficientsStatement.lean#L6). The proof is the usual `first | exact ... | ...` wrapper of the `T.` restatement files.
