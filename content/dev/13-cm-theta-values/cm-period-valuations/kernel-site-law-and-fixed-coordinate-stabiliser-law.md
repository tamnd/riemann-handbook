---
id: kernel-site-law-and-fixed-coordinate-stabiliser-law
title: The theta law, the stabiliser law and the inner condition at a joint site
kind: theorem
decl: GlobalTheory.T.kernelSite_law_and_fixedCoordinateStabiliserLaw
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.KernelSiteLawAndFixedCoordinateStabiliserLawStatement
covers: 360
status: drafted
drafted_by: writer@claude
---
This theorem is a restatement of [`site_law_xiIn`](/entry/site-law-xi-in/): the statements are the same, and the proof only calls that theorem. [The pending system is admitted at each joint site](/entry/admissible-at-each-site/) uses this theorem to get the inputs `XiIn` and `LawInLt` of `AdmAtEnt2`.

## Statement

Let $S$ be a joint site with top level $m$, as in the parent entry. `Pair` and `Pos` are stated in [the kernel difference at every level below the top](/entry/tie-del-all-steps/). `Move` and `Away` are tie conditions (`MoveTie`, `AwayTie`).

**Theorem.** If $S$ satisfies `Pair`, `Pos`, `Move` and `Away`, then:

1. `S.Law`: for $j < m$, a component $c$, lattice tuples $L$, $L_a'$ and $\gamma$ in the level group, $\Theta_j(c, \gamma L, L_a') = \kappa(\gamma)^{-1} \cdot \mathrm{SA}_j(\gamma)\bigl(\Theta_j(c, L, L_a')\bigr)$, with a scalar factor $\kappa$ (`kapG`) and an action $\mathrm{SA}_j$ on power series;
2. `LawInLt`: the stabiliser law `StabLawLt` for the same theta series (not unfolded);
3. `XiIn`: `XiEx` holds for the theta function of the pending element at each place $v$ and each $j < m$.

## Proof

The proof is `site_law_xiIn`. There, `LawAll.kapLawLt_frecG` proves `S.Law` from `Pair`, `Pos` and `Move`; `KapLawLt.stab` derives `LawInLt` from `S.Law`; and `XiGen.xiEx_theta_general` with `pendT_ThF_lt_of_kapLawLt` gives `XiIn` from `S.Law`, `Pair` and `Away`.

## In the Lean code

The theorem is in [KernelSiteLawAndFixedCoordinateStabiliserLawStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/KernelSiteLawAndFixedCoordinateStabiliserLawStatement.lean#L8), under `set_option maxHeartbeats 1000000`. `site_law_xiIn` is in [KernelSiteLawAndFixedCoordinateStabiliserLaw.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/KernelSiteLawAndFixedCoordinateStabiliserLaw.lean#L20). `LawInLt` is in [ThetaSeriesDataHypothesesBelowMaximalLevel.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/ThetaSeriesDataHypothesesBelowMaximalLevel.lean#L92) and `XiIn` in [StatementAdmAt.lean](lean:Formalism/LocalToGlobal/InertKernelTheory/StatementAdmAt.lean#L45).

The name leaves out the third part, `XiIn`. `LawInLt` has a second definition with the same body in [the `Formalism` tree](lean:Formalism/LocalToGlobal/InertKernelTheory/ThetaSeriesDataHypothesesBelowMaximalLevel.lean#L45).
