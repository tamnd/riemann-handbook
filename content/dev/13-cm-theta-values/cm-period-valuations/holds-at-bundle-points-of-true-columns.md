---
id: holds-at-bundle-points-of-true-columns
title: The arithmetic row at bundle points, from pinned rows (restatement)
kind: theorem
decl: GlobalTheory.T.holds_at_bundlePoints_of_trueColumns
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.DeliveryAtBundlePointsOfTrueColumnsStatement
covers: 574
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`row_aAtG_of_rowPin`](/entry/row-a-at-g-of-row-pin/), with the same statement. Its user is [`row_aAtG_at_built_alt`](/entry/row-a-at-g-at-built-alt/), which proves the row `aAtG` of the record [HypsAlt](/step/hyps-alt-def/) with it. The content is below `row_aAtG_of_rowPin`.

## Statement

Let $Q$ be a slot (`V4.Slot`) and $L_k$ a linkage of bundles (`LkT Bd`).

**Theorem.** Assume that each point of $Q$ has a part $w$ (`HasPart`) such that `RowPin` holds for the true-columns datum $w.I$ of the part and each tuple $a$. Then `ArithmeticConditionAtBundlePoints Q Lk` holds.

`ArithmeticConditionAtBundlePoints Q Lk` is `Row Q Lk (fun 𝒜 _ => H_aAtG 𝒜)`, the row `aAtG` on the families built from the slot: a constant $C_1$ bounds the valuations of the period coordinates at used tuples, and `familySizeBoundAtTypePrime` holds. `RowPin` asks, for each word $u$, for a linear isomorphism $e$ from the period space at $u$ and $a$ to the ambient space at $a$, such that $e$ is the given map `eMt u` at $a = \mu_0$ and `eMtTw u a` otherwise, each generator of $\widetilde M_a$ is the image of a row form, and a vector $z$ lies in the lattice `MtildeL` exactly when the image of its row form is a combination of these generators with integral coefficients.

## Proof

The proof is `exact row_aAtG_of_rowPin`, through a `first | exact … | …` tactic block.

## In the Lean code

The theorem is at [DeliveryAtBundlePointsOfTrueColumnsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/DeliveryAtBundlePointsOfTrueColumnsStatement.lean#L8). `ArithmeticConditionAtBundlePoints` and `H_aAtG` are at [LevelPrimeColumnValuationsAtBundlePoints.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/LevelPrimeColumnValuationsAtBundlePoints.lean#L21), and `RowPin` at [JetSplitAmb.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/JetSplitAmb.lean#L35).
