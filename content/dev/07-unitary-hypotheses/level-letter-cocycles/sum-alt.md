---
id: sum-alt
title: The exponent bound for alternating signs, at a Wach module of the datum
kind: theorem
decl: Formalism.MainNotions.N.Ln17.sum_alt
module: Formalism.SharpRestriction.LevelLetterCocycles.RepresentationCongruences.LogbHBNonneg
covers: 506
status: drafted
drafted_by: writer@claude
---
This theorem is [`sumAltW`](/entry/sum-alt-w/), which has the proof, applied to the Wach module of the datum at one pair $(K, L)$. Its only work is to build the hypotheses of `sumAltW` from the global records. [`thmB_at`](/entry/thm-b-at/) uses it in the case of alternating signs.

## Statement

Use the notation of [`thmB_at`](/entry/thm-b-at/). Assume the records `AdmBoundsB` and `UsedJ`, and let $(K, L)$ be in case A at a prime $\ell$. Let $T_1, T_2$, $F$ and the parameters satisfy the hypotheses `HypB` of local lifting theorem B, let the signs alternate with no three consecutive thick letters, and let $C_b \ge 2$. Assume that no letter is thick or that $40\,\mathrm{Sg} \le b/4$.

**Theorem.** There are an integer $e$ and a finite set $Z$ of finite cocycles of $T_2$ with

$$e \le 55\,\mathrm{Sg} + 13S + \eta\beta, \qquad |Z| \le 4nm,$$

and $\ell^e c \in \mathrm{Im}(F) + \mathrm{span}(Z)$ for each finite cocycle $c$ of $T_2$. Here $\beta$ is the band indicator with the constant $C_b$.

## Proof

The lemma `coresAt` builds the record `CoresW` for the Wach module at $(K, L)$. This record has 35 fields. Four are basic facts: $\ell \ge 5$, and $O_L$ is the valuation ring of $L$. Most of the others are one field of `AdmBoundsB` or `UsedJ` at $(K, L)$: the lattice conditions, the lift and relay conditions, the arc, splitting, universal, saturation and killer conditions, and the letter condition. Five lemmas supply the rest: `gamma_uniformizer_divisible_statement` ($\gamma(\pi_0) = \pi_0 u$ with $u$ in the ring $A_\Delta$), `ptEx_at` (a $p$-th root of unity $\zeta \ne 1$ for each letter and embedding), `lext_HExt_D` (crystalline extensions of the trivial lattice), `arc_structures_hold_at` (four arc structures) and `jumps_of_surjective_lattice_map` (two conditions on jumps). Then `sumAltW` gives the result, with $p = \ell$. The rest is bookkeeping.

## In the Lean code

The theorem is in [LogbHBNonneg.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/RepresentationCongruences/LogbHBNonneg.lean#L386). `coresAt` is at [line 334](lean:Formalism/SharpRestriction/LevelLetterCocycles/RepresentationCongruences/LogbHBNonneg.lean#L334) and `CoresW` is in [ExistsGaloisExtendingAlgHom.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/RepresentationCongruences/ExistsGaloisExtendingAlgHom.lean#L30).

The hypothesis $\ell \ge 11$ comes from `HypB`. Completeness of $O_L$ comes from `isAdicComplete_integers_local`. The file name `LogbHBNonneg` names a small lemma in it, not this theorem.
