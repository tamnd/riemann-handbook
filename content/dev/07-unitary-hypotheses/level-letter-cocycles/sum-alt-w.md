---
id: sum-alt-w
title: The exponent bound for alternating signs, from the arcs
kind: theorem
decl: Formalism.MainNotions.N.Ln17.sumAltW
module: Formalism.SharpRestriction.LevelLetterCocycles.RepresentationCongruences.LogbHBNonneg
covers: 505
status: drafted
drafted_by: writer@claude
---
This theorem proves the exponent bound of [`sum_alt`](/entry/sum-alt/) for any Wach module $W$ that satisfies the record `CoresW`. It cuts $\mathbb{Z}/n$ into arcs, gets a lift at each arc from [`arc_proposition_alternative`](/entry/arc-proposition-alternative/), and puts the arcs together.

## Statement

Use the notation of [`thmB_at`](/entry/thm-b-at/), with $p$ the prime of $W$. A letter $i \in \mathbb{Z}/n$ is *thick* if $b \le \mathrm{size}(i) \le b + \eta$, else *thin*. The *arcs* (`arcOf`) cut $\mathbb{Z}/n$ into blocks: each block is one thin letter and the run of thick letters after it. A *cut* $c$ is the last letter of a block, and $\mathrm{len}(c)$ is the length of that block.

**Theorem.** Let $W$ satisfy `CoresW`. Let $T_1, T_2$, $F$ and the parameters satisfy `HypB`. Let the signs alternate with no three consecutive thick letters, let $C_b \ge 2$, and assume that no letter is thick or that $40\,\mathrm{Sg} \le b/4$. Then there are an integer $e$ and a finite set $Z$ of finite cocycles of $T_2$ with

$$e \le 55\,\mathrm{Sg} + 13S + \eta\beta, \qquad |Z| \le 4nm,$$

and $p^e c \in \mathrm{Im}(F) + \mathrm{span}(Z)$ for each finite cocycle $c$ of $T_2$.

## Proof

1. **Setup.** `arc_setup_theorem` gives: the arc datum $A$ is admissible; $T_1, T_2$ lie in its window; the block lengths add up to $n$ and are at most 3; a number $\sigma$ of $A$ satisfies $\sigma \le 3\,\mathrm{Sg}$; and there is $r_r \le 3\,\mathrm{Sg}$ such that $F$, and the projection of each crystalline extension of the trivial lattice by a cocycle of $T_2$, satisfy the killing condition `KillsΔ` at level $r_r$ at each cut. We have not unfolded `KillsΔ`.
2. **Lifts at each arc.** Let $E_1 = \lfloor 40\,\mathrm{Sg} + \eta\beta \rfloor$. At each cut, $\mathrm{len}(c) \le 2$ or $40\,\mathrm{Sg} \le b/4$: if no letter is thick, all lengths are 1 (`arc_len_le_one_of_no_thick`). So `arc_proposition_alternative` gives lifts with exponent $E_1$ at each cut.
3. **Classes at each arc.** `arc_length_bound_theorem` turns these lifts into a set $Z_c$ of classes in $H^1_f(T_2)$ with $|Z_c| \le m\,\rho(c)(\mathrm{len}(c) + 1)$, with $\rho(c)$ the number of thick letters in the block. For each class $x$ attached to the cut $c$, $p^{\sigma + \kappa_c + E_1} x$ lies in $F_*H^1_f(T_1) + \mathrm{span}(Z_c)$. Here $\kappa_c$ is $\mathrm{len}(c)$ plus a sum of $\mathrm{len}(c) + 1 + v_p(j)$ over the nonzero $j$ of a window of jumps. `kappa_le_of_alternating` gives $\kappa_c \le 13S + 3\,\mathrm{lg} + 3$.
4. **Sum over the arcs.** Let $\kappa = \max_c \kappa_c$ and $E = \sigma + \kappa + E_1$. `split_sum` writes $p^{r_r + 2\sigma}$ times each class of $H^1_f(T_2)$ as $\pm$ a sum of classes attached to the cuts. So $p^{r_r + 2\sigma + E} x \in F_*H^1_f(T_1) + \mathrm{span}\bigl(\bigcup_c Z_c\bigr)$ for each $x \in H^1_f(T_2)$.
5. **From classes to cocycles.** `cocycle_classes_exponent` picks a cocycle in each class, which gives $Z$ with $|Z| \le |\bigcup_c Z_c|$.
6. **The numbers.** With $e = r_r + 3\sigma + \kappa + E_1$, these bounds and `logb_le_Sg` ($3\,\mathrm{lg} + 3 \le 3\,\mathrm{Sg}$) give $e \le (3 + 9 + 3 + 40)\,\mathrm{Sg} + 13S + \eta\beta$. Since $\rho(c) \le \mathrm{len}(c) \le 3$, we have $\rho(c)(\mathrm{len}(c) + 1) \le 4\,\mathrm{len}(c)$, so $|Z| \le 4m\sum_c \mathrm{len}(c) = 4nm$.

## In the Lean code

The theorem is in [LogbHBNonneg.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/RepresentationCongruences/LogbHBNonneg.lean#L100). The lemmas it calls:

- `arc_setup_theorem` in [ArcSetupTheorem.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/RepresentationCongruences/ArcSetupTheorem.lean#L22);
- `arc_length_bound_theorem` in [ArcLengthBoundTheorem.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/RepresentationCongruences/ArcLengthBoundTheorem.lean#L26);
- `kappa_le_of_alternating` in [SumPadicValIntWindowLe.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/RepresentationCongruences/SumPadicValIntWindowLe.lean#L287);
- `cocycle_classes_exponent` in [CocycleClassesExponent.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/RepresentationCongruences/CocycleClassesExponent.lean#L23);
- `split_sum` and `logb_le_Sg` in the same file.

`arcOf` is in [AdmBoundsBOfAdm.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/AdmBoundsBOfAdm.lean#L42) and $\sigma$ is `ArcP.σ` in [ArcLiftingSetup.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/ArcLiftingSetup.lean#L131).
