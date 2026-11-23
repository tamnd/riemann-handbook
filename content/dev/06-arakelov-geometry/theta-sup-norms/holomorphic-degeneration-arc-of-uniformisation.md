---
id: holomorphic-degeneration-arc-of-uniformisation
title: Holomorphic arcs from the uniformisation, second name
kind: theorem
decl: GlobalTheory.T.holomorphic_degenerationArc_of_uniformisation
module: Development.AbelianVarietyTheory.Proofs.ThetaShiftProofs.HolomorphicDegenerationArcOfUniformisationStatement
covers: 718
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`HolomorphicArc.main`](/entry/holomorphic-arc-main/). It has no proof of its own. Its only caller is [`arcClause_closed`](/entry/arc-clause-closed/), which supplies the three hypotheses.

## Statement

Assume the bundle `Out.Laws` of 24 facts about abelian schemes, the bundle `Out.Laws2` of 4 more facts (fields `secBaseChangeAny`, `secTwist`, `charPair`, `smoothDense`, not unfolded here), and the analytic uniformisation `ThetaUnifAV` of complex abelian varieties. Then `ToroidalArchimedeanCondition` holds: each formal arc into a projective model whose generic point is in the open moduli space is the expansion of a holomorphic family on a half plane. The [entry for `HolomorphicArc.main`](/entry/holomorphic-arc-main/) states it in full.

## Proof

The proof is `exact @GlobalTheory.HolomorphicArc.main`, inside a `first` combinator with two fallbacks that are never reached.

## In the Lean code

The theorem is at [HolomorphicDegenerationArcOfUniformisationStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/HolomorphicDegenerationArcOfUniformisationStatement.lean#L6). The type is word for word the type of `HolomorphicArc.main`. The line before it sets `maxHeartbeats` to 1000000 for this theorem.
