---
id: local-component-measure-identity-alt-bis
title: Self-dual lattices integral in given normal frames, in statement form
kind: theorem
decl: GlobalTheory.T.local_component_measure_identity_alt_bis
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.LocalComponentMeasureIdentityAltBis
covers: 375
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`exists_shape_integral_in_normal_frames_alt`](/entry/exists-shape-integral-in-normal-frames-alt/). Its only user is [`lattices_frames_basePoints_exist_alt`](/entry/lattices-frames-base-points-exist-alt/), which calls it in step 4 of its proof to get the lattices $N_j$ on the spaces $Y_j$. The real content is in `exists_shape_integral_in_normal_frames_alt`.

## Statement

The statement is word for word the statement of `exists_shape_integral_in_normal_frames_alt`. In short: take the data and hypotheses of [`lattices_frames_basePoints_exist_alt`](/entry/lattices-frames-base-points-exist-alt/), and assume also that the level places $P_G$ and the twist places $P_T$ are disjoint. Let normal frames $F_Y$ and units $s$ be given at each place of $P_g$ or $Q$ (`IsNormalFr`). Then there are lattices $N_j$ of $Y_j$, a finitely supported twist $d_T$, and lattices $M$ and frames $\beta_0$ on the Bessel spaces, such that:

1. `ShapeOff` holds for the level data and type data updated by $N$, $d_T$, $M$, $\beta_0$;
2. the support of $d_T$ satisfies `CombAt` at $P_T$;
3. $N_j$ is self-dual for $j < m$;
4. at each place, each frame $F_Y$ is integral for $N_j$ (`IntIn`).

## Proof

The proof applies `exists_shape_integral_in_normal_frames_alt`. Nothing else happens.

## In the Lean code

The theorem is at [LocalComponentMeasureIdentityAltBis.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LocalComponentMeasureIdentityAltBis.lean#L16). The proof is the tactic `first | exact @GlobalTheory.Fam.LatShape.exists_shape_integral_in_normal_frames_alt | ...`, so the theorem only passes its hypotheses along. The target is in [ExistsShapeIntegralInNormalFrames.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsShapeIntegralInNormalFrames.lean#L24). The name is misleading: measures appear only in the hypotheses, and the conclusion has no identity between measures. It asserts the existence of self-dual lattices in which the given frames are integral, as the name of the target says.
