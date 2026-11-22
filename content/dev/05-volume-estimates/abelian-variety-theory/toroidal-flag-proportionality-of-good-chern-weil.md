---
id: toroidal-flag-proportionality-of-good-chern-weil
title: Proportionality on toroidal flag spaces, from good Chern-Weil theory (restatement)
kind: theorem
decl: GlobalTheory.T.toroidalFlagProportionality_of_goodChernWeil
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ToroidalFlagProportionalityOfGoodChernWeilStatement
covers: 1341
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [Mumford proportionality from good Chern-Weil theory](/entry/mumford-proportionality-of-good-chern-weil/). It has the same statement and its proof only calls that theorem. Its one caller is [`toClassicalTheorems`](/entry/to-classical-theorems/), which feeds it the field `p16` of the bundle `PublishedHodgeBundleTheorems` (see the step [PublishedHodgeBundleTheorems from the literature](/step/published-results-arithmetic/)). All the mathematics is in the entry that it renames.

## Statement

**Theorem.** If $\mathrm{GoodChernWeil}$ holds, then $\mathrm{MumfordProportionality}$ holds.

Both statements are defined and explained in [the entry that it renames](/entry/mumford-proportionality-of-good-chern-weil/). In short, $\mathrm{GoodChernWeil}$ says that Chern forms of good metrics integrate to Chern numbers, with a push-forward formula for flag bundles. $\mathrm{MumfordProportionality}$ says that on each component of a toroidal flag space, $(L_\lambda^{\dim})$ is the covolume times a flag degree.

## Proof

Apply `GlobalTheory.Proportionality.mumfordProportionality_of_goodChernWeil`. There is nothing else.

## In the Lean code

The theorem is in [ToroidalFlagProportionalityOfGoodChernWeilStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ToroidalFlagProportionalityOfGoodChernWeilStatement.lean#L5). The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)` with the same theorem in each branch.

The callers are `PublishedHodgeBundleTheorems.toClassicalTheorems` in [CoveringTopologyRefinement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/CoveringTopologyRefinement.lean#L10) and `Hypotheses2.toClassicalTheorems` in [StrongerPublishedHypothesesImply.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/StrongerPublishedHypothesesImply.lean#L10). Both pass it to a `toClassicalTheoremsOf` lemma, for example [ToKnownTheoremsOf.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/ToKnownTheoremsOf.lean#L39). That lemma applies it to the field `p16` of the input, of type `GoodChernWeil`, and fills the field `p16` of the output structure `Hypotheses''`, of type `MumfordProportionality`. So one field name stands for two different statements in the two structures. The lemma first tries `exact h.p16`, which fails on the type, and then `exact hM'`.

The name says "toroidal flag proportionality". The statement is the one that the code calls `MumfordProportionality`. The two names refer to the same result.
