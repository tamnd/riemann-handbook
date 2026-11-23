---
id: row-placement-exists
title: A finite element that places the rows and matches the levels
kind: theorem
decl: GlobalTheory.rowPlacement_exists
module: Development.AbelianVarietyTheory.Proofs.TwistedOperators.ExistsRowPlacementFiniteElementMatchesLevels
covers: 450
status: drafted
drafted_by: writer@claude
---
This theorem is the proof behind [the row placement statement](/entry/exists-row-placement-finite-element-matches-levels/), which repeats its statement word for word. It finds a finite adelic element $t$ that carries the level of the first row space onto the Hida level group, and it then compares the good rows at a second element $t_S$. The theorem joins three lemmas. The geometric content is in [the conjugation of levels](/entry/exists-finite-element-conj-row-level-character/).

## Statement

Let $V = Y_0$ be the first row space of the datum $D$, with adelic unitary group $G(\mathbb{A})$. Let $G_f^c \subset G(\mathbb{A})$ be the elements with trivial archimedean part. Let $K = \mathrm{levS}(V, \beta_Y, L)$ be the level subgroup of the frame $\beta_Y$ and the level data $L$ of the true row, with character $\chi = \mathrm{levChi}$. Let $\iota$ be the rational embedding into the group of the Hida setting $X$. Let $K_2$ be the level group of $X$, with character $\chi_2$.

Assume the discrete series classification, the hypotheses on $R$ (levels, group, models), the host hypotheses, the pinning data `hpin`, and $t_S \in G_f^c$. Assume also `hmove`: if some $t \in G_f^c$ has property $P(t)$, then $P(t_S)$ holds. Here $P(t)$ says that conjugation by $t$ carries $(K, \chi)$ onto $(\iota^{-1}(1, K_2), \bar\chi_2)$ (this is `ConjLevel`) and that `RowLevelMatchAt R F X h t` holds. Then some $t \in G_f^c$ has $P(t)$, and there is $c'$ with `EvalTieT ... ι tS c'`. The last statement says that a linear isomorphism identifies the forms with the evaluations $x \mapsto \mathrm{ev}(v_0, T)(\iota^{-1}(x)\, t_S)$, with norms scaled by $c'$.

## Proof

1. Rewrite $\iota$ as `iotaX X h` by `rowPlacement_iota_eq`.
2. The conjugation lemma gives $t \in G_f^c$ with `ConjLevel` and a frame condition.
3. `rowLevelMatchAt_of_levelConjugation` turns these into `RowLevelMatchAt` at $t$.
4. `hmove` moves both facts to $t_S$.
5. `goodRows_compare_by_levelMatching_evaluation` gives `EvalTieT` at $t_S$.

## In the Lean code

The theorem is in [ExistsRowPlacementFiniteElementMatchesLevels.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExistsRowPlacementFiniteElementMatchesLevels.lean#L24). `ConjLevel` is in [EvalTieTOne.lean](lean:Formalism/LocalToGlobal/IndefiniteReal/EvalTieTOne.lean#L14), `EvalTieT` on line 18 of the same file, and `RowLevelMatchAt` in [RowLevelMatch.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RowLevelMatch.lean#L42). We have not unfolded the reduction data inside `RowLevelMatchAt`.

The hypothesis `hmove` carries most of the weight for $t_S$: the proof never shows that $t_S$ matches the levels, it assumes it. The first conjunct does not use `hmove`, $t_S$ or the discrete series classification. The classification is used only in the last lemma.
