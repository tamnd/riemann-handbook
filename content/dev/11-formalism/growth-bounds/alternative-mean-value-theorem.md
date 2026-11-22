---
id: alternative-mean-value-theorem
title: The model lattice bound for every model instance
kind: theorem
decl: Formalism.MainNotions.G.CountingStatementReduction.alternative_mean_value_theorem
module: Formalism.SharpRestriction.GrowthBounds.CountingStatementReduction
covers: 1688
status: drafted
drafted_by: writer@claude
---
This theorem proves the averaged bad-count bound `ModelLatticeRank` for every model instance. It is a repackaging: it reads the fields of the instance and its hypothesis and passes them to [the top-level form of `theoremMV7`](/entry/top-theorem-mv7/). The real content is in [`theoremMV7`](/entry/mc-theorem-mv7/). The result goes to [the box bound `restTM_exists`](/entry/rest-tm-exists/).

## Statement

A *model instance* $X$ (`InstM`) has a prime $p$, sizes $s$ and $r \ge 1$, letters $L$ of length $2s+1$, tie data $T$ with $t$ ties, reals $a$ and $E$, and for each tie $i$ a start $n_{0,i}$, a step $d_i$ and a length $Y_i$, and an index $\rho < r$. The hypothesis `InstM.Hyp` and the conclusion are those of `TheoremMV7`, stated in full in [its entry](/entry/mc-theorem-mv7/).

`ModelLatticeRank` $D$ $X$ says: if `X.Hyp` holds, then the mean over the progression grid of the bad count of the lattice of integral points is at most $\sum_i \varepsilon_i$ times a mean dimension, with $\varepsilon_i$ and the depth given by the fields of $X$.

**Theorem.** For each datum $D$ and each model instance $X$, `ModelLatticeRank` $D$ $X$ holds.

## Proof

Assume `X.Hyp`. It is a conjunction of eleven conditions. The proof splits it and applies `Formalism.InvariantFactorPaths.MC.Top.theoremMV7` to the fields of $X$ and the eleven parts. The derived quantities of `InstM` (`lg`, `κ`, `eps`, `D1`, `prog`, `top`) unfold to the expressions in `TheoremMV7` by definition. The lemma `eps_eq` in the same file records the case of `eps`, and its proof is `rfl`. There is nothing else.

## In the Lean code

The theorem is in [CountingStatementReduction.lean](lean:Formalism/SharpRestriction/GrowthBounds/CountingStatementReduction.lean#L19). `InstM`, `InstM.Hyp` and `ModelLatticeRank` are in [FlipOneThree.lean](lean:Formalism/SharpRestriction/GrowthBounds/FlipOneThree.lean#L345).

The datum $D$ is not used: `ModelLatticeRank` binds it as `_D` and does not read it. So the statement is the same for every $D$.

The name says "mean value theorem". The statement is a bound for a mean over a grid of integers. It is not the mean value theorem of calculus. The code has a second, unrelated definition named `ModelLatticeRank`, in the namespace `Formalism.MainNotions.ColumnSystems` ([ColumnSystems.lean](lean:Formalism/SharpRestriction/GrowthBounds/ColumnSystems.lean#L159)), with ten real constants. This theorem uses the one in `flipOneThree`.
