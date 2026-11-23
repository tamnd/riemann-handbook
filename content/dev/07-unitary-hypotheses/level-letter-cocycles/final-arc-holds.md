---
id: final-arc-holds
title: The arc data at one cut, for a surjection of crystalline lattices
kind: theorem
decl: Formalism.MainNotions.N.Ln03.Pf.finalArc_holds
module: Formalism.SharpRestriction.LevelLetterCocycles.LevelKernelDetection.PfAssemble
covers: 463
status: drafted
drafted_by: writer@claude
---
This theorem proves the arc statement `FinalArc` at one cut $c$ for the map of coordinates of a surjection $f \colon T_1 \to T_2$ of crystalline lattices. [`realised2_pf`](/entry/realised2-pf/) calls it at each cut, and the result becomes the last hypothesis of [theorem E in final form](/entry/theorem-e-final-form/).

## Statement

Let $C_1, C_2$ be coordinates of $T_1, T_2$ with a map $h$ over $f$. Let $c$ be a cut, $\ell_c \le n$ its length, $\varpi$ irreducible in $\mathcal{O}$, and let $j \le \ell_c$, $M$, $g$, $G_0$, $S$, $\eta$ be integers with $3g \le (\ell - 1) M$. Let $e_1, e_2$ be bases of the Wach modules of $T_1, T_2$ at the index $c - \ell_c$, and let $P$ be the matrix of constant terms of $h$ in these bases.

`FinalArc` says that there is arc data with these properties:

- (`lev₁`, `lev₂`) for each lattice, a level model at the steps $s < \ell_c$: the kinds and sizes agree with the window data, each step has a filtration whose jumps lie in the window of its kind, the basis spans the module at $c - \ell_c$, and some vectors $\lambda$ form a basis over $L$;
- (`mapFl`, `cMap`) two conditions on the level map, which we have not unfolded; `cMap` is asked only at the steps of kind "up";
- (`prLIs`) $h(e_{1,k}) - \sum_l P_{lk}\, e_{2,l}$ lies in $X$ times the module at $c - \ell_c$.

**Theorem.** Assume the level-map compatibilities and the Wach lemmas of [`realised2_pf`](/entry/realised2-pf/), `DdREqDcris`, and that jumps of a quotient are jumps of the source. Assume that $T_1$ has jumps in the windows of type `ty`, that $K$ is unramified, $\ell \ge 5$, and $L$ contains a primitive $\ell^n$-th root of unity. Assume also the identities of power series: $q$ is a unit times the shifted cyclotomic polynomial, $\varphi(X) = (1+X)^\ell - 1$, and $1 + \rho_\zeta(X) = \zeta \exp(X)$. Then `FinalArc` holds at $c$.

We have not unfolded the fields of the level models.

## Proof

1. `jumps_bound` bounds the jumps of each $T_i$ by some $m_i$. It uses `DdREqDcris` and $K$ unramified.
2. `lvHyp_holds'` builds the level hypotheses for each lattice.
3. `levSteps_holds'` proves the level conditions for $T_1$ from its window type.
4. `levSteps_holds_quot'` proves them for $T_2$ with the same window type. The jumps of $T_2$ are jumps of $T_1$, since $f$ is onto.
5. `mapSteps_holds`, with `mapHyp_of`, proves the conditions on the level map and on $P$.
6. `arc_of_steps` packs the five results into `FinalArc`.

## In the Lean code

The theorem is at [PfAssemble.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/LevelKernelDetection/PfAssemble.lean#L521). The steps are `jumps_bound` ([line 322](lean:Formalism/SharpRestriction/LevelLetterCocycles/LevelKernelDetection/PfAssemble.lean#L322)), `lvHyp_holds'` ([line 330](lean:Formalism/SharpRestriction/LevelLetterCocycles/LevelKernelDetection/PfAssemble.lean#L330)), `levSteps_holds'` ([line 423](lean:Formalism/SharpRestriction/LevelLetterCocycles/LevelKernelDetection/PfAssemble.lean#L423)), `levSteps_holds_quot'` ([line 470](lean:Formalism/SharpRestriction/LevelLetterCocycles/LevelKernelDetection/PfAssemble.lean#L470)) and `mapSteps_holds` ([line 270](lean:Formalism/SharpRestriction/LevelLetterCocycles/LevelKernelDetection/PfAssemble.lean#L270)). `LevSteps`, `MapSteps` and `arc_of_steps` are in [FinalLevelsOf.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/FinalLevelsOf.lean#L134). `FinalArc` is at [FinalArcProps.lean](lean:Formalism/DistinguishedUnitIdeals/FinalArcProps.lean#L219).

- The function $H$ of the arc is a free parameter. The theorem holds for every $H$.
