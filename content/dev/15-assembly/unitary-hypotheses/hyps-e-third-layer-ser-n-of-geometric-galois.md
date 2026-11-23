---
id: hyps-e-third-layer-ser-n-of-geometric-galois
title: The local inputs of a member from the literal hypotheses, restated
kind: theorem
decl: GlobalTheory.T.hyps_e_third_layer_ser_n_of_geometric_galois
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ThetaLiftHypothesesOfNonvanishing
covers: 1263
status: drafted
drafted_by: writer@claude
---
This theorem is a copy of [`exists_hyp_n_of_geometric_galois_compat`](/entry/exists-hyp-n-of-geometric-galois-compat/) under a second name. That entry has the real content. It turns the literal non-endoscopic hypotheses and a list of published inputs into the bundle of local inputs that the [proof that HypsAlt is nonempty](/step/nonempty-hyps/) needs. It has two users: [`hypotheses_nonempty_of_unramified_exponents_alt`](/proof/unitary-hypotheses/) and [`member_bundles_large_unramified_exponents_alt`](/entry/member-bundles-large-unramified-exponents-alt/). Both call it on the fields `litN` and `toHypothesesX` of their bundle. This is step 2 of branch 1 in the [unitary hypotheses chapter](/proof/unitary-hypotheses/). Below this theorem are 1,263 declarations, one more than below the copy.

## Statement

The statement is the statement of the copy, word for word. Assume `NonEndoscopicHypothesesAlt` (local representation theory, global automorphic and Galois inputs, cohomology, a join of five transport facts and a functional equation) and `GeometricGaloisRepCompatibility` (twelve published inputs). Then there are:

1. the elliptic hypothesis `EllipticHypothesis`, a record of 25 facts;
2. the published inputs of the third layer, `PublishedInputsThirdLayerAlt`;
3. the series facts `SerN`;
4. a local Langlands correspondence `hL : RecTExists`, with the compatibilities `LocalLanglandsHypothesis hL`.

## Proof

The proof is `exact exists_hyp_n_of_geometric_galois_compat`, inside a `first | … | …` tactic that tries three forms of the same call. There is no other content.

## In the Lean code

The theorem is at [ThetaLiftHypothesesOfNonvanishing.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ThetaLiftHypothesesOfNonvanishing.lean#L51), and the copy at line 24 of the same file. The copy sits in the namespace `GlobalTheory.MemberClose`, this theorem in `GlobalTheory.T`. The proof runs with `maxHeartbeats 1000000`.

The file name speaks of theta lifts and nonvanishing. No theta lift appears in the statement.
