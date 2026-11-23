---
id: g-tss-of-adj
title: The shift frame from the pointwise adjoint relation
kind: theorem
decl: Formalism.FourierDecayAlt.P.CutMP.Gauge.GC.gTSS_of_adj
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.cut_GCore_GTSS
covers: 570
status: drafted
drafted_by: writer@claude
---
This theorem proves `GTSS`, the existence of [a frame for the shift operators](/entry/second-shift-gauge-holds/), from one hypothesis, `GTSSAdjPt`. Its user [`second_shift_gauge_holds`](/entry/second-shift-gauge-holds/) supplies that hypothesis. The proof only fills a second hypothesis of [`gTSS_of_adj_radT`](/entry/g-tss-of-adj-rad-t/) with a proved fact. The entry for `gTSS_of_adj_radT` describes the four parts of the proof.

## Statement

`GTSS` is stated in [the entry above](/entry/second-shift-gauge-holds/). `GTSSAdjPt` says: let $e$ be a frame that intertwines each $\kappa(f)$, and let $s_l, t_l$ be smooth matrices of functions on the annulus $|\zeta|^2 > T$ such that, under the transfer `trR`, $S_l$ acts as $s_l$ and $S_l^*$ acts as $t_l$ (`SSLoc`). Then $t_l(\rho, \rho')(\zeta) = \overline{s_l(\rho', \rho)(\zeta)}$ for all $1 \le l \le k - 1$, all types $\rho, \rho'$ and all $\zeta$ in the annulus.

**Theorem.** `GTSSAdjPt` implies `GTSS`.

## Proof

The proof is `gTSS_of_adj_radT hA radial_torus_local_holds`. The proved fact `radial_torus_local_holds` gives `GTCLRadT`: under the hypotheses of the place, each operator $X.t(Y, a, b)$ acts on the restriction of a function to the radial slice as a differential operator in $\zeta$ of finite order with smooth coefficients (`RadDZ`). It is proved from three lemmas on jets and Taylor expansions, which we have not opened.

## In the Lean code

The theorem is at [cut_GCore_GTSS.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/cut_GCore_GTSS.lean#L12). `GTSSAdjPt` is in [CutGCoreGTSSCut.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutGCoreGTSSCut.lean#L49), `GTCLRadT` and `RadDZ` in [CutGCoreGTCLocalCut.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutGCoreGTCLocalCut.lean#L27), and `radial_torus_local_holds` in [CutGCoreGTCLRadT.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutGCoreGTCLRadT.lean#L8).
