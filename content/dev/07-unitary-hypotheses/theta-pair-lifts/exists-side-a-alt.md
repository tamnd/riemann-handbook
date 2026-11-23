---
id: exists-side-a-alt
title: A host embedding on a relabelled layer
kind: theorem
decl: GlobalTheory.HeightCounting.TopA.exists_sideA_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ConclOfGrp
covers: 442
status: drafted
drafted_by: writer@claude
---
This theorem builds, for a datum $D$ with true types, a layer of $D$ that carries a full host embedding record. It relabels $D$ so that a group side gives the tame generators, then calls [`conclusion_of_group_side`](/entry/conclusion-of-group-side/). It reaches [membership and bundles at the origin parameters](/entry/exists-base-lattice-of-prime-alt/) through the second name [`types_true_of_ray_class_alt`](/entry/types-true-of-ray-class-alt/), which gives the hypotheses.

## Statement

The hypotheses are those of [`types_true_of_ray_class_alt`](/entry/types-true-of-ray-class-alt/). The conclusion is `ConclAlt` $h_L$ $D$ $cf$ $j_E$ `rep`: there are a layer $L$ of $D$ (a `Lay0`, with the conditions `ZOk` and `EtaOk`) and a record $A$ of type `CharFrameHostEmbedding` for the datum `setK D L` and its frame, such that:

1. `CGTrueT` holds for the Weil-Deligne tie `A.wdT`, `AutomorphicSideRealised` holds for it and the automorphic side `A.au`, and `RepresentationParametersHold` holds for `rep` and the row side of $A$;
2. `TypesTrue` holds for $L$ and $cf$;
3. $L$ agrees with $D$ in nine parts: the places `PlG` and `plGw`, the two centres `cenAmb` and `cenMt`, the local part `loc`, and the ring `Om` with its three instances;
4. the generator $\zeta_k$ of the group side of $A$ is the generator of `labDat` $g_k$, for each $k$;
5. `LabConj` holds for `A.wdT`.

`CharFrameHostEmbedding` is a record of twelve parts: the emptiness of `Loc`, a Weil-Deligne tie with true labels, a character side, a row side, a place side with embeddings, a Weil-Deligne side, a group side, a parameter side, an automorphic side and a character condition `ChiTOk`. We have not unfolded them.

## Proof

1. `exists_tame_generators_green_cuspidal_labelling` uses `GreenCuspidal`, `GlobalArtinReciprocity`, the integrality of `eExp` and `TypesTrue`. It gives a layer $L$ with `ZOk` and `EtaOk`, such that `setK D L` has empty `Loc` and true types, the nine agreements of item 3, a group side $\Gamma$ with the generators of item 4, and `ChiTOk`.
2. `RowDepth` passes to `setK D L` through the agreement of the places.
3. [`conclusion_of_group_side`](/entry/conclusion-of-group-side/) gives `ConclAlt` for `setK D L`.
4. `concl_setK_alt` carries `ConclAlt` from `setK D L` back to $D$, by composing the agreements.

## In the Lean code

The theorem is in [ConclOfGrp.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ConclOfGrp.lean#L161), with `ConclAlt` at [line 16](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ConclOfGrp.lean#L16) and `concl_setK_alt` at [line 31](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ConclOfGrp.lean#L31). The record: [HeckeOpen.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/HeckeOpen.lean#L52). The lemma of step 1 is a second name of `TameGrp.exists_tame_generators_cuspidal_labelling`, in [ExistsTameGeneratorsGreenCuspidalLabellingStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsTameGeneratorsGreenCuspidalLabellingStatement.lean#L9). We have not read the lemma behind it.

Odd points:

- The statement writes `ConclAlt` out in full, as an existential with nineteen components.
- The ray prime hypothesis is stated for $D$ and passed to `conclusion_of_group_side` for `setK D L` with no rewrite.
- The name "side A" does not match an object of the statement.
