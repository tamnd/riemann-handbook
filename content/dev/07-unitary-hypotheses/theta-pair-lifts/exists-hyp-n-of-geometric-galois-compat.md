---
id: exists-hyp-n-of-geometric-galois-compat
title: The local inputs of a member from the literal hypotheses
kind: theorem
decl: GlobalTheory.MemberClose.exists_hyp_n_of_geometric_galois_compat
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ThetaLiftHypothesesOfNonvanishing
covers: 1262
status: drafted
drafted_by: writer@claude
---
This theorem turns the literal non-endoscopic hypotheses and twelve published inputs into a bundle: an elliptic hypothesis, the published inputs of the third layer, the series facts, and a local Langlands correspondence with its compatibilities. Its only user is the copy [`hyps_e_third_layer_ser_n_of_geometric_galois`](/entry/hyps-e-third-layer-ser-n-of-geometric-galois/), which the [proof that HypsAlt is nonempty](/step/nonempty-hyps/) calls in branch 1 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). The proof only sorts fields and calls named lemmas. Below this theorem are 1,262 declarations, and 1,105 of them are below [`heckeInt_transform_readTie`](/entry/hecke-int-transform-read-tie/).

## Statement

Assume:

- `NonEndoscopicHypothesesAlt`, a record with five fields: local representation theory (`loc`), global automorphic and Galois inputs with a global Artin map (`aut`), twelve facts of Galois cohomology (`coh`: Poitou-Tate duality, local and global finiteness and Euler characteristics, Bloch-Kato and others), a conjunction of five transport facts (`join`), and the Hecke-Tate functional equation (`fe`);
- `GeometricGaloisRepCompatibility`, a record of twelve published inputs: the Weil representation of a unitary pair, existence and classification of discrete series, Harish-Chandra analyticity, trace class of cusp forms, Dixmier-Malliavin and Flath factorisation, the Weil-Siegel formula, the doubling method, unramified doubling, continuation of partial Hecke $L$-functions, and a height count `HtCard`.

Then `EllipticHypothesis` (25 facts) holds, `PublishedInputsThirdLayerAlt` (14 facts) holds, `SerN` (six series facts) holds, and there is a local Langlands correspondence $hL$ with `LocalLanglandsHypothesis hL`. The last record holds again the third-layer inputs and `SerN`, and adds an archimedean comparison, a parameter statement, a point statement and a membership statement at the layer points.

## Proof

1. `localLanglandsGL_and_purity_at_member_alt`, from `loc` and `aut`, gives $hL$ and the third-layer inputs.
2. `SerN` has six parts. `seriesRatS_and_serInt_of_globalArtin` gives two from the Artin map in `aut`. [`heckeInt_transform_readTie`](/entry/hecke-int-transform-read-tie/), with no hypotheses, gives three. The sixth, a ratio of conjugates, comes from the transport fact in `join` by `toricRatioConjugates_of_transport` and `ratioConj_of_toricRatioConjugates`.
3. `EllipticHypothesis` is filled field by field: seven of the eight facts from `twist_front_inputs` (Chebotarev, cohomological dimension, tame local facts and others), seven fields of `coh`, the toric fact of `join`, five of the six parts of `SerN`, three parts of the field `what₂` of the third-layer inputs, `local_global_above_ell_of_cusp_alt` and `blochKatoLocal_allPrimes_of_blochKato`.
4. The four statements of `LocalLanglandsHypothesis hL` come from `archimedean_local_langlands_compatibility_alt`, `conjDualParam_stable_of_prime_not_dividing_level_alt`, `ptSt_of_inputs_geometric_compat` and `cuspParameter_at_member_alt`.

The rest is bookkeeping.

## In the Lean code

The theorem is at [ThetaLiftHypothesesOfNonvanishing.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ThetaLiftHypothesesOfNonvanishing.lean#L24).

- The second input is used only once, by `ptSt_of_inputs_geometric_compat`. In spite of its name, `GeometricGaloisRepCompatibility` ([GeometricGaloisRepCompatibility.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/GeometricGaloisRepCompatibility.lean#L6)) holds no statement about Galois representations.
- The functional equation `fe` and three of the five facts of `join` are never used (line 27).
- The conclusion states the third-layer inputs and `SerN` twice: once alone, and once as the fields `pr` and `ser` of `LocalLanglandsHypothesis`.
- `seriesRat_of_seriesRatS`, used for the first part of `SerN`, is the identity function.
- The file name speaks of theta lifts and nonvanishing. No theta lift appears in the statement.
