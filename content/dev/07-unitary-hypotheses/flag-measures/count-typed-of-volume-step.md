---
id: count-typed-of-volume-step
title: The points lemma from the volume step
kind: theorem
decl: GlobalTheory.CountBridge.count_typed_of_volumeStep
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.CountTypedOfVolumeStep
covers: 1631
status: drafted
drafted_by: writer@claude
---
This theorem puts the counting theorem in the form `PointsLemma` that its user needs. Its user is [`count_constants_of_siegelWeil`](/entry/count-constants-of-siegel-weil/), which gets the volume step from the Siegel-Weil hypothesis and then calls this theorem. That result goes to the counting row of [the unitary hypotheses node](/proof/unitary-hypotheses/). The theorem is a repackaging. The content is in [the counting theorem from the volume step](/entry/counting-theorem-of-volume-step/).

## Statement

**Theorem.** Assume `VolumeStep` (see [the counting theorem](/entry/counting-theorem-of-volume-step/)). For each real $A$ there are $n_0$ and $C_0 \ge 0$ such that for all $n_1 \ge n_0$, all $C \ge C_0$ and every datum $D$, the statement `PointsLemma D n_1 A C (1/16) (1/16)` holds.

`PointsLemma` is the counting estimate of the counting theorem, with the hypotheses grouped into two records, `HidaSetting` and `CountData`. Its conclusion is
$$\bigl|D_{\mathrm{count}} - D^{*}\bigl(\textstyle\prod_v d_v\bigr)\bigr| \le e^{-\frac{1}{16} n f \log n}\, D^{*}\bigl(\textstyle\prod_v d_v\bigr).$$

## Proof

The volume step gives `CountingTheorem` by [`unitaryAutomorphicCounting_of_compactDualVolumeRatio`](/entry/unitary-automorphic-counting-of-compact-dual-volume-ratio/). The lemma `unitaryAutomorphicCounting_unbundled` turns `CountingTheorem` into the same estimate with all hypotheses written out. The proof takes $n_0$ and $C_0$ from it, opens `PointsLemma` and passes the arguments along. The rest is bookkeeping.

## In the Lean code

The theorem is in [CountTypedOfVolumeStep.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/CountTypedOfVolumeStep.lean#L12). The quantifier over $D$ is vacuous. `PointsLemma` takes `(_D : D7)` and does not use it ([PlaceDegreeData.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/PlaceDegreeData.lean#L364)). The unbundled lemma is proved in [UnitaryAutomorphicCountingUnbundled.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/UnitaryAutomorphicCountingUnbundled.lean#L40). It sets $C_0 = \max(0, 8 \cdot 10^{14}(A+4))$ and builds the hypothesis record `CountHyp` of the counting theorem.
