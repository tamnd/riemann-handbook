---
id: theta-local-models-of-split-unramified-joints
title: Good local models from joints, restated
kind: theorem
decl: GlobalTheory.T.thetaLocalModels_of_splitUnramified_joints
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.ThetaLocalModelsOfSplitUnramifiedJointsStatement
covers: 2341
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`modelsOK_of_joints`](/entry/models-ok-of-joints/). It has the same statement, and its proof applies that theorem. Its user is [`modelsAt_of_part`](/entry/models-at-of-part/), which gets the joints and the stabiliser condition from a column part and then applies this theorem. The content is in `modelsOK_of_joints`, which dominates 2,340 of the 2,341 declarations below this theorem.

## Statement

Assume `AdmAtEnt2` and `CurveEx`. Let $D$ be a datum of type `D7` with size data $L$, ties $h_T$, instances $G_i$ and $G_l$, constants, division data $D_x$ and extra data `ex`, and let $t$ be a tied kernel entry of `ex`. Assume:

1. `JointsAt t μ` for each used tuple $\mu$;
2. $e_0(u, \mu_0) = e_{\mu_0}(u, 0)$ for the twisted forms of `ex`, for each word $u$;
3. `Stab0 D`;
4. $2\, r_G(\varepsilon) \le k$.

Then `ModelsOK D Gl ex.cmp Dx ex.tw` holds. All these objects are described in [`modelsOK_of_joints`](/entry/models-ok-of-joints/).

## Proof

Apply `modelsOK_of_joints`. Nothing else is used.

## In the Lean code

The theorem is at [ThetaLocalModelsOfSplitUnramifiedJointsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/ThetaLocalModelsOfSplitUnramifiedJointsStatement.lean#L8). Its proof is the tactic

```
first | exact @modelsOK_of_joints | exact modelsOK_of_joints | (intros; apply modelsOK_of_joints <;> assumption)
```

(namespaces shortened), under `set_option maxHeartbeats 1000000`. The first branch closes the goal, so the theorem is a renaming.

The words "theta" and "split unramified" in the name do not match a hypothesis. The only condition on a place $w$ in the statement is that its residue characteristic is not in the finite set $D_x.Q_p(\mu)$. We have not unfolded how $Q_p$ is built, so we do not say whether this means "split and unramified".
