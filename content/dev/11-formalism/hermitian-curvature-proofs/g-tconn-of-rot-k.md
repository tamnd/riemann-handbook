---
id: g-tconn-of-rot-k
title: A frame for the connection from rotation invariance
kind: theorem
decl: Formalism.FourierDecayAlt.P.CutMP.Gauge.GC.gTConn_of_rotK
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.CutGCoreDone
covers: 433
status: drafted
drafted_by: writer@claude
---
This theorem proves `GTConn`, the second stage of the frame construction in [the gauge transfer from rotation invariance](/entry/gen-transfer-of-rot-k/). Its only hypothesis is `GTRRotK` from that entry. The proof is an assembly. It puts a reference frame, built from `GTRRotK`, into a phase argument on the annulus. Only the reference frame uses the hypothesis. The other inputs are proved facts with no hypothesis.

## Statement

Use the frames $e$, the transfer `trR` and the hypothesis list `GTHyp` of [the gauge transfer from rotation invariance](/entry/gen-transfer-of-rot-k/). Let $\mathrm{Ann} = \{\zeta : T < |\zeta|^2\}$. The model connection has the coefficients $A^{\mathrm{m}}_\rho = a_\rho\bar\zeta/(|\zeta|^2 - T)$ and $B^{\mathrm{m}}_\rho = a_\rho\zeta/(|\zeta|^2 - T)$.

**Theorem.** Assume `GTRRotK`. Let the data satisfy `GTHyp`, and let $e$ be a frame (`IsFrameB`) in which `trR` intertwines each $\kappa(f)$ with $f(\rho)$ (`KapF`). Then there is a frame $e'$ with these two properties such that `trR` also intertwines $\nabla$ and $\nabla^*$ with the model operators (`NabF`).

## Proof

In the frame $e$, the operators $\nabla$ and $\nabla^*$ act as $\partial_\zeta + A_\rho$ and $-\partial_{\bar\zeta} + B_\rho$, with $A$, $B$ smooth on $\mathrm{Ann}$ and $B = \bar A$. Put $\alpha = A^{\mathrm{m}} - A$. If $\mathrm{Re}\,\partial_{\bar\zeta}\alpha = 0$ and the imaginary part of each circle integral $\oint_{|w|=R}\alpha\,dw$ is in $\pi\mathbb{Z}$, then there is a smooth unit function $u$ with $\bar u\,\partial u = \alpha$. The frame $e' = u\cdot e$ then has the model connection.

The two conditions on $\alpha$ come from a reference frame $e_0$ (`GTCRef`). Any two such frames differ by a unit phase, and the phase moves $A$ by $\bar u\,\partial u$. So the conditions pass from $e_0$ to $e$. For $e_0$, `GTRRotK` and seven proved facts give an integer $n$ with $\mathrm{Re}(\zeta(A^{\mathrm{m}} - A_0)) = n/2$ on $\mathrm{Ann}$. Then the imaginary part of each circle integral is $2\pi\cdot n/2 = \pi n$. Most of the steps use facts whose statements we have not unfolded, for example `gauge_transform_holds` and `connection_phase_holds`.

## In the Lean code

The theorem is at [CutGCoreDone.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutGCoreDone.lean#L31). It calls `gTConn_of_leaves` ([CutGCoreGTConnFinal.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutGCoreGTConnFinal.lean#L7)) with the curvature and holonomy facts from `gTCRef_of_rotK`. The phase argument is in [cut_GCore_GTConnCut.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/cut_GCore_GTConnCut.lean#L158). The passage from $e_0$ to $e$ is in [CutGCoreGTCHolRest.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutGCoreGTCHolRest.lean#L25). The proof builds `gTCRef_of_rotK h` two times, once for each fact.
