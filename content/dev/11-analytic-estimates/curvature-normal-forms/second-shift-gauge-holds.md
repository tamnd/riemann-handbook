---
id: second-shift-gauge-holds
title: A frame for the shift operators
kind: theorem
decl: Formalism.FourierDecayAlt.P.CutMP.Gauge.GC.second_shift_gauge_holds
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.cut_GCore_GTSS
covers: 571
status: drafted
drafted_by: writer@claude
---
This theorem proves `GTSS`, the third stage of the frame construction in [the gauge transfer from rotation invariance](/entry/gen-transfer-of-rot-k/). It has no hypothesis. The proof is one line: it gives the proved fact `second_shift_adjoint_pointwise` to [`gTSS_of_adj`](/entry/g-tss-of-adj/). The real content is in [the phase change](/entry/second-shift-phase-holds/) and in [the extra shift relations](/entry/shift-extra/).

## Statement

Use the radial space $\mathcal{R}$, the frames $e$ and the transfer `trR` of [the gauge transfer from rotation invariance](/entry/gen-transfer-of-rot-k/). Let the data $P$, $X$, $d$ satisfy `GTHyp`, the list of hypotheses of that entry (`IsPlace`, $k \ge 2$, `CSec`, `IsActualLevel`, `IsStarLevel`, the relations `d.Rel`, and $X$ and $d$ have the same matrix `QQ`).

**Theorem.** Let $e$ be a frame (`IsFrameB`) such that `trR` intertwines each $\kappa(f)$ with the diagonal operator $f(\rho)$ (`KapF`), and $\nabla$, $\nabla^*$ with the model operators (`NabF`). Then there is a frame $e'$ with the same three properties such that `trR` also intertwines each shift $S_l$ and $S_l^*$, $1 \le l \le k - 1$, with the model shift `MA.SS` and its adjoint (`SSF`).

## Proof

`second_shift_gauge_holds` is `gTSS_of_adj second_shift_adjoint_pointwise`. The fact `second_shift_adjoint_pointwise` proves `GTSSAdjPt`: when $S_l$ and $S_l^*$ act in a frame by matrices of functions $s_l$ and $t_l$, then $t_l(\rho, \rho') = \overline{s_l(\rho', \rho)}$ on the annulus $|\zeta|^2 > T$. It comes from `radial_adjoint_identity_holds`, whose statement we have not unfolded.

## In the Lean code

The theorem is at [cut_GCore_GTSS.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/cut_GCore_GTSS.lean#L14). `GTSS` and `SSF` are in [CutGCoreGenTransferCut.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutGCoreGenTransferCut.lean#L67). `second_shift_adjoint_pointwise` is in [CutGCoreGTSSAdj.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutGCoreGTSSAdj.lean#L268).
