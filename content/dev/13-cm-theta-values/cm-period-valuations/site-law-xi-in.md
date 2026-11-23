---
id: site-law-xi-in
title: The transformation law and the Ξ condition at a joint site
kind: theorem
decl: GlobalTheory.TwV.site_law_xiIn
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.KernelSiteLawAndFixedCoordinateStabiliserLaw
covers: 359
status: drafted
drafted_by: writer@claude
---
This theorem gives two inputs of the hypothesis `AdmAtEnt2` at a joint site, the stabiliser law `LawInLt` and the condition `XiIn`, and also the full transformation law `S.Law`. It is used in the restated form [`kernelSite_law_and_fixedCoordinateStabiliserLaw`](/entry/kernel-site-law-and-fixed-coordinate-stabiliser-law/), which [`admissible_at_each_site`](/entry/admissible-at-each-site/) calls in its step 2.

## Statement

Let $S$ be a joint site (`Joint.At`) over a joint $J$, with the notation of [`admissible_at_each_site`](/entry/admissible-at-each-site/). Let $X$ be the local system `sysS H X std` at $p$. From $S$ the Lean code builds a family of power series $\Theta_j(L, L')$, one for each step $j$ and each pair of lattice tuples at steps $j$ and $j+1$ (`thFOf X pos (FrecG …)`). Its inputs include $E$, $\lambda$ and $\mu_T$ of $S$, the base $B$, character $\chi$, bad set $SS$ and level $c_l$ of $t$, and $\Xi_0 = $ `J.xi0 std S.Xi`, the adelic datum of $S$ read on lattice tuples.

The four hypotheses are predicates on $S$: `Pair` (`PairOK`: at each step $j < m$, admitted kernel lattices, local constancy of $\Xi_0$, algebraic kernel series and scalars, invertible frames), `Pos` (`LamPos`: $\lambda$ agrees with the local embeddings $\rho_v$), `Move` (`MoveTie`: moving a tuple by $\gamma$ changes the data by a unitary matrix and an algebraic scalar) and `Away` (`AwayTie`: a suitable split prime outside $SS$ at each $v$ and $j < m$).

**Theorem.** If `Pair`, `Pos`, `Move` and `Away` hold for $S$, then:

1. (`S.Law`, which is `KapLawLt`) for $j < m$, a component $c$, a lattice tuple $L$ and $\gamma$ in the group $\Gamma$ of $c$, $\Theta_j(c, \gamma L, L') = \kappa_j(c, \gamma)^{-1} \cdot S_A(\gamma)\,\Theta_j(c, L, L')$;
2. (`LawInLt`) the same law at representative tuples $L_0$ and elements $\varepsilon$ with $\varepsilon L_0 = L_0$, so that $\Theta_j(c, L_0, L')$ is fixed by the twisted action of $\varepsilon$;
3. (`XiIn`) for each $v$ and $j < m$, `XiEx` holds for the series of the pending element $S.Y$.

We have not unfolded $\kappa_j$ (`kapG`), the substitution $S_A$ (`SA`), `FrecG` or `XiEx`.

## Proof

1. `base_data` gives $\delta \neq 0$ and three properties of $B$. `lev_pos_and_noConj`, applied to the adelic data of $J$, gives $c_l > 0$ and that $SS$ holds no prime with its conjugate. `sysS_ranks` gives $m_X = m$.
2. `kapLawLt_frecG`, with `Pair`, `Pos` and `Move`, gives `S.Law`.
3. `KapLawLt.stab` puts $\gamma = \varepsilon$ with $\varepsilon L_0 = L_0$ in the law. This is `LawInLt`.
4. `xiEx_theta_general`, with `Pair`, `Away` and the two facts `model_at_split_places_holds` and `split_place_moves_compose`, gives `XiEx` for $\Theta$. `pendT_ThF_lt_of_kapLawLt` uses the law to carry it to the series of $S.Y$.

## In the Lean code

The theorem is at [KernelSiteLawAndFixedCoordinateStabiliserLaw.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/KernelSiteLawAndFixedCoordinateStabiliserLaw.lean#L20), under `set_option maxHeartbeats 2000000`. `KapLawLt` is in [NatCastMemOfPlace.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/NatCastMemOfPlace.lean#L24), `LawInLt` in [ThetaSeriesDataHypothesesBelowMaximalLevel.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/ThetaSeriesDataHypothesesBelowMaximalLevel.lean#L92) and `XiIn` in [StatementAdmAt.lean](lean:Formalism/LocalToGlobal/InertKernelTheory/StatementAdmAt.lean#L45). The work is in `kapLawLt_frecG` and `xiEx_theta_general`, which this theorem only calls. The second conclusion is a special case of the first. `Pos` and `Move` are used only for the law, and `Away` only for `XiIn`.
