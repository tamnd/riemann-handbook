---
id: tower-ex-of-dep-fixed
title: Good frames for the theta tower exist, given fixed depth vectors
kind: theorem
decl: GlobalTheory.AscFin.towerEx_of_depFixed
module: Development.AbelianVarietyTheory.Proofs.TwistedOperators.ExistsGoodGridFramesOfDepthFixed
covers: 1355
status: drafted
drafted_by: writer@claude
---
This theorem builds the frames that the ascent of Bessel periods needs. It is the proof behind the renaming [`existsGoodGridFrames_of_depthFixed`](/entry/exists-good-grid-frames-of-depth-fixed/), which [`ascent_of_depFixed`](/proof/bessel-seesaw/) uses as the frame input of the tower of periods (Step 6 of [Bessel periods, seesaw and separation of functionals](/proof/bessel-seesaw/)). The proof is an assembly of three lemmas. The real content is in [`std_good`](/entry/std-good/).

## Statement

The statements quantify over a *grid datum*, through the predicate `All`: a datum $D$ with the coprimality condition `OffQ D`, level characters $L$ with `L.Is μ0`, constants, a grid $G$ of Hermitian spaces $G.V(X)$ over the CM field $E$ of $D$ (row spaces $X = \mathrm{grid}(i)$ and core spaces $X = \mathrm{core}(i)$, for $0 \le i \le m$), a Weil datum $W$ (an additive character $\psi$ and Weil representations $\omega_p$ for the pairs $p$ of the grid, as in the [[theta correspondence|6WB6TKE70H]]), and volume data $M$ with `M.IsRow`. We have not unfolded `GridData` or `Weil`.

**Hypothesis** `DepFixed`. For every grid datum, every $i < m$, every pair $p$ that is the row pair $\chi(i)$ or the core pair $\mathrm{core}(i)$, and every depth vector $f$ of $p$ (a theta function that is a vacuum for the lattice `depLat G p`), we have $\omega_p(k, k') f = f$ for all $k$ in the level group of the small space of $p$ and $k'$ in the level group of the big space.

**Conclusion** `TowerEx`. For every grid datum and every choice $v$ of volume data on the core spaces, there are frames $F$ with `F.Ends v W M` and lattices $\Gamma_L$ with `F.Good v W Γ_L`.

A system of *frames* (`Frames G`) is: a line $L_z$ of rank 1 with an orthogonal decomposition $G.V(\mathrm{core}\,0) = Y_0 \oplus L_z$; anisotropic vectors $\zeta_\rho$ of $-L_z$, with links between $\zeta_{\rho+1}$ and $\zeta_\rho$; and, for each $\rho$ with $2\rho + 2 \le m$, volume data `VolN` that we have not unfolded and Witt decompositions with $\rho$ hyperbolic planes $H$:

$$\begin{aligned} G.V(\mathrm{grid}\,(2\rho+2)) &= V_0(\rho) \oplus H^{\rho}, \qquad V_0(\rho) = G.V(\mathrm{core}\,(2\rho+2)) \oplus (-L_z), \\ G.V(\mathrm{grid}\,(2\rho+1)) &= G.V(\mathrm{core}\,(2\rho+1)) \oplus H^{\rho}.\end{aligned}$$

`F.Ends` says two things. At the bottom, the embedding of $Y_0$ is the stabilizer embedding of the grid. At the top ($2\rho + 2 = m$), for rapidly decreasing forms, if the Bessel period of the last frame is not zero, then the period `Bplus` is not zero. `F.Good` asks, for each Bessel-to-Fourier-Jacobi step and each Fourier-Jacobi-to-Bessel step of the tower, for a set of theta functions with the local conditions `Loc` that the rungs of the ascent use, and for the bottom data `LastLat`. The entry [`std_good`](/entry/std-good/) gives the fields.

## Proof

Fix a grid datum and $v$.

1. `T.exists_standardAuxiliaryFrames_allRowGrids` gives frames $F$ that are *standard* (`Std F`): their matrices are read off from the column data of the grid.
2. `T.standardAuxiliaryFrames_fit_grid_ends` proves `F.Ends v W M` for every standard $F$.
3. Take $\Gamma_L = \mathrm{lineLat}(F)$. [`standardAuxiliaryFrames_good_row_grids`](/entry/standard-auxiliary-frames-good-row-grids/) proves `F.Good v W Γ_L` for every standard $F$, from `DepFixed`.

## In the Lean code

The theorem is in [ExistsGoodGridFramesOfDepthFixed.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExistsGoodGridFramesOfDepthFixed.lean#L17). The proof is one anonymous constructor with the three lemmas above. `TowerEx` is defined in [TowerEx.lean](lean:Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/TowerEx.lean#L229), and `DepFixed` in [OffQOfSizeRows.lean](lean:Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/OffQOfSizeRows.lean#L104).

Only step 3 uses `DepFixed`. Steps 1 and 2 hold with no hypothesis. The existential $\Gamma_L$ in `TowerEx` is always the explicit `lineLat F`.
