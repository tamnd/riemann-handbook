---
id: std-good
title: Standard frames are good, given fixed depth vectors
kind: theorem
decl: GlobalTheory.AscFin.GoodStd.std_good
module: Development.AbelianVarietyTheory.Proofs.TwistedOperators.StandardAuxiliaryFramesGoodRowGrids
covers: 1303
status: drafted
drafted_by: writer@claude
---
This theorem proves that standard frames meet the local conditions of each rung of the ascent of Bessel periods. It is the proof behind [`standardAuxiliaryFrames_good_row_grids`](/entry/standard-auxiliary-frames-good-row-grids/). Through [`towerEx_of_depFixed`](/entry/tower-ex-of-dep-fixed/) it gives the "good" half of `TowerEx`, the frame input of [`ascent_of_depFixed`](/entry/ascent-of-dep-fixed/). The ascent in turn serves [`real_functionals_separate_of_hypothesis`](/entry/real-functionals-separate-of-hypothesis/) (Step 6 of [Bessel periods, seesaw and separation of functionals](/proof/bessel-seesaw/)).

## Statement

Use the grid datum, `DepFixed` and the frames $F$ of [`towerEx_of_depFixed`](/entry/tower-ex-of-dep-fixed/). Write $\Lambda_{\mathrm{row}}(i)$, $\Lambda_{\mathrm{core}}(i)$ for the depth lattices of the row and core pairs, and $K_i$ for the level group of the row space $V_i$. A *$\Gamma$-vacuum* is a theta function fixed by the Heisenberg translations $2u$, $u \in \Gamma$ (and by some $u$ themselves).

The frames are *standard* (`Std F`) if their matrices come from the grid: $\zeta_\rho = (-\xi_0)^\rho \zeta_0$, and each decomposition is given by the frame or the columns of the grid data at its level. The *line lattice* $\mathrm{lineLat}(F)_0$ is the pull-back of $\Lambda_{\mathrm{core}}(0)$ to the line summand; for $\rho > 0$ it is the lattice `latO` built from the core lattice and a fractional ideal times $\mathcal O_E \zeta_0$.

**Theorem.** Assume `DepFixed`. For every grid datum, volume data $v$ and standard $F$, the frames are good with $\Gamma_L = \mathrm{lineLat}(F)$:

1. (`bf`) For each Bessel-to-Fourier-Jacobi step from $V_{2\rho+2}$ to $V_{2\rho+1}$ with the row Weil representation, there are a set $\mathcal S$ of theta functions and a lattice $\Gamma_0$ such that $(\mathcal S, \Gamma_0, K_{2\rho+1})$ satisfy `Loc`, every $\Phi \in \mathcal S$ is a $\Lambda_{\mathrm{row}}(2\rho+1)$-vacuum, and box products of core vacua with line vacua are $\Gamma_0$-vacua.
2. (`fb`) The same for each Fourier-Jacobi-to-Bessel step from $V_{2\sigma+3}$ to $V_{2\sigma+2}$, with $K_{2\sigma+2}$.
3. (`lineNe`) Each line lattice has a nonzero vacuum.
4. (`last`) The bottom data `LastLat` hold for the first Fourier-Jacobi frame.

`Loc` lists the local facts that the unfolding of a period needs: $\mathcal S$ is stable under some Heisenberg translations; the map `flatS` sends $\mathcal S$ to $\Gamma_0$-vacua; $K$ is compact open in the finite adelic group and fixes $\mathcal S$; if $\mathrm{flatS}(\omega(1,h)\Phi) \neq 0$, then $h \in R \cdot G_\infty \cdot K$, with $G_\infty$ the archimedean part and $R$ the group of $r$ with $r x = x u$ for the matrix $x$ of the step; and `flatS` is not zero on $\mathcal S$.

## Proof

The lemmas fall into five groups.

- **Grid facts.** `T.weil_datum_conjugation_dictionary_row_grid` is the only use of `DepFixed`: $K_i$ fixes each $\Lambda_{\mathrm{row}}(i)$-vacuum. `T.depthCongruenceSubgroup_compactOpen_places_to_adeles` and `T.latticeStabilizerAtPlace_mem_depthCongruence_gridNode` say that $K_i$ is compact open, contains the local lattice stabilizers outside the bad set $S_0$, and give a local-to-global test for $h \in R \cdot G_\infty \cdot K_i$.
- **Pieces.** For each step, $\mathcal S$ is the class `cls` of theta functions with prescribed Heisenberg characters on the pieces `pcBF` or `pcFB`, and $\Gamma_0$ is the core piece. `T.besselToFourierJacobi_mixedPieces_admissible` and `T.fourierJacobi_step_pieces_admissible_splits` say that the pieces are admissible and split.
- **Support.** The local-to-global test, fed by one-coset lemmas at each place (for example `T.goodPlace_oneCoset_of_besselLevel`).
- **Unfolding.** The helper `loc_cls` turns these facts into `Loc`, from four unfolding lemmas on `cls`. For field 2, `xLast_rat` shows by a Gram matrix computation that the matrix of the step is rational of full rank.
- **Box and bottom.** `T.boxDepthData_mul_lineVacua_besselLevel` and `T.fourierJacobi_depthDatum_mul_lineVacuum_isVacuum` give the box clauses. `T.last_seesaw_lattices_nonzero_line_vacua` gives fields 3 and 4.

The rest is bookkeeping.

## In the Lean code

The theorem is in [StandardAuxiliaryFramesGoodRowGrids.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/StandardAuxiliaryFramesGoodRowGrids.lean#L122), with the helpers at lines 42 and 94. `Frames.Good` and `Loc` are in [TowerEx.lean](lean:Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/TowerEx.lean#L214); `Std`, `lineLat` and `cls` are in [IsAuxiliaryVectorWittDec.lean](lean:Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/IsAuxiliaryVectorWittDec.lean#L167).

- Only the last of the seven clauses of `weil_datum_conjugation_dictionary_row_grid` is used.
- In field 2 the support proof drops its hypothesis that the condition is stable under $K$ ([line 171](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/StandardAuxiliaryFramesGoodRowGrids.lean#L171)).
- We have not unfolded `Pieces.Is`, `Splits`, `Cond`, `flatAt`, or the lemmas beyond their statements.
