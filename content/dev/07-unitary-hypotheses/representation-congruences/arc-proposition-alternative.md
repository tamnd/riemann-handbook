---
id: arc-proposition-alternative
title: A lift at one arc, for alternating signs
kind: theorem
decl: Formalism.MainNotions.N.FrobeniusPowerSeries.arc_proposition_alternative
module: Formalism.SharpRestriction.LevelLetterCocycles.RepresentationCongruences.ArcPropositionAlternative
covers: 500
status: drafted
drafted_by: writer@claude
---
This theorem gives a lift at one arc, with an exponent at most $40\,\mathrm{Sg} + \eta\beta$. [`sumAltW`](/entry/sum-alt-w/) calls it at each cut, and puts the lifts together. The proof is a case split on the length of the arc and on the signs. Each case is one lemma.

## Statement

Use the notation of [`sumAltW`](/entry/sum-alt-w/): a Wach module $W$ with prime $p$ and $n$ letters, the arc datum $A$ built from $(b, w, S, \eta, \mathrm{up}, \mathrm{size})$, its cuts $c$ and lengths $\mathrm{len}(c)$.

**Theorem.** Assume that $W$ is in case A, that $O$ is a complete discrete valuation ring, and that $W$ satisfies 26 of the 35 conditions of the record `CoresW` (lattice conditions, relay, arc, saturation and killer conditions, the letter condition, and others). Let $T_1, T_2$, $F$ and the parameters satisfy `HypB`, and let $T_1, T_2$ lie in the window of $A$. Let $r_r \le 3\,\mathrm{Sg}$ be such that $F$ satisfies `KillsΔ` at level $r_r$ at each cut. Let the signs alternate with no three consecutive thick letters, and let $C_b \ge 2$. Let $c$ be a cut with $\mathrm{len}(c) \le 2$ or $40\,\mathrm{Sg} \le b/4$. Let $b_1, \dots, b_d$ be a horizontal family (`IsHor`) in the module of $T_2$, let $k_0$ be an index that meets `InLpp`, and let $f$ meet `InFF`. Then there is $e_1 \le 40\,\mathrm{Sg} + \eta\beta$ with `LiftsAt` at $(c, b, k_0, f, e_1)$.

`LiftsAt` says: there are $w_1$ in the module of $T_1$ and $z$ in that of $T_2$, with filtration conditions on $w_1$, $F(w_1)$ and $z$, such that $F(w_1) - z$ is represented (`RepVV`) in the family $b$ by the coordinates $p^{e_1} f$ at $k_0$ and $0$ at the other indices. We have not unfolded the filtration conditions or `RepVV`.

## Proof

`arcBasic` gives $1 \le \mathrm{len}(c) \le 3$, $\sigma \le 3\,\mathrm{Sg}$, and `HypB` gives $p \ge 11$, so $\mathrm{Sg} \ge 1$.

1. **Length 1.** `arc_single_type_bound` gives $e_1 \le 6\,\mathrm{Sg} + 1$.
2. **Length 2.** The signs alternate, so $\mathrm{up}(c-1) \ne \mathrm{up}(c)$. `arc_length_one_two_theorem` gives $e_1 \le 15\,\mathrm{Sg} + 1 + \eta\beta$. It splits on $\mathrm{up}(c)$ and on one inequality between the sizes of $c - 1$ and $c$, and calls one of four lemmas: `arc_length_one_or_two_case_b`, `arc_length_one_or_two_case_c`, `exists_liftsAt_arcOf_of_up_eq_false`, `arc_length_two_case_down`.
3. **Length 3.** Then $40\,\mathrm{Sg} \le b/4$. If $\mathrm{up}(c-2)$ is false, `arc_length_three_theorem` gives $e_1 \le 22\,\mathrm{Sg} + 1 + \eta\beta$, by `arc_length_three_case_c` or `arc_length_three_case_d`. If it is true, `exists_liftsAt_of_arc_len_three_of_up` gives $e_1 \le 34\,\mathrm{Sg} + 1 + \eta\beta$, by `exists_exponent_le_and_liftsAt_arc` or `exists_liftsAt_le_of_len_three_of_up`.

Since $\mathrm{Sg} \ge 1$, each bound is at most $40\,\mathrm{Sg} + \eta\beta$.

## In the Lean code

The theorem is in [ArcPropositionAlternative.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/RepresentationCongruences/ArcPropositionAlternative.lean#L133). The two case lemmas for lengths 2 and 3 are at [line 34](lean:Formalism/SharpRestriction/LevelLetterCocycles/RepresentationCongruences/ArcPropositionAlternative.lean#L34) and [line 100](lean:Formalism/SharpRestriction/LevelLetterCocycles/RepresentationCongruences/ArcPropositionAlternative.lean#L100) of the same file. `LiftsAt` is in [ArcGamLiftCore.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/RepresentationCongruences/ArcGamLiftCore.lean#L31).

- The theorem takes 26 fields of `CoresW` as separate hypotheses. The hypotheses `P3`, `P4`, the roots of unity and the letter condition are used only for length 3 with $\mathrm{up}(c-2)$ false.
- The parameters $m$, $M_i$ and $h_i$ occur only through `HypB`.
- The proof shows $\mathrm{Sg} \ge 1$ again inline; the lemma `one_le_Sg` in [LogbHBNonneg.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/RepresentationCongruences/LogbHBNonneg.lean#L77) says the same.
- The namespace `FrobeniusPowerSeries` does not describe the statement. "Alternative" refers to the alternating signs.
