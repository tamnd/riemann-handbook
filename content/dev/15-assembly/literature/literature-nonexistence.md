---
id: literature-nonexistence
title: The non-endoscopic bundle from the literature
kind: theorem
decl: UpperTheory.LiteratureTheorems.literature_nonexistence
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.EveryCharacterOfLiteratureOfVWin
covers: 1622
status: drafted
drafted_by: writer@claude
---
This theorem fills a structure of five earlier results. It has no mathematical content of its own. Its result is the field `litN` of the 60-field bundle [UnitaryGroupThirdPlaceHypotheses](/step/published-results-eigen/), which goes to [EveryCharacter from the literature and VWin](/step/every-character-of-literature/). Below it are 1,622 declarations. Most of them are below its field `join`, which is [JoinOut from the literature](/entry/join-out-of-literature/).

## Statement

Let $O$ be a proof of the structure [OpenLiteratureStatements](/step/open-literature-statements-def/). Then the structure `NonEndoscopicHypothesesAlt` holds. It is a `Prop` with five fields:

- `loc`: the 19-field bundle `LocalRepresentationTheoryHypothesesAlt`, results on representations of $p$-adic $\mathrm{GL}_n$ (by their names: Bernstein-Zelevinsky finiteness, Langlands exhaustion, the local converse theorem, local Langlands);
- `aut`: the 16-field bundle `GlobalAutomorphicGaloisHypotheses'`, results on automorphic forms and their Galois representations;
- `coh`: the 12-field bundle `LitCoh`, results on Galois cohomology (Poitou-Tate, local Tate duality, Euler characteristics, Greenberg-Wiles, Bloch-Kato);
- `join`: the statement `JoinOut`, a conjunction of five statements on CM fields and values of Hecke L-functions;
- `fe`: the statement `HeckeTateFunctionalEquation`, a functional equation for Hecke L-functions of a totally complex number field.

We have not unfolded the fields of `loc`, `aut` and `coh`.

## Proof

The proof fills each field with a theorem of the same file applied to $O$: `literature_local`, `literature_automorphy`, `literature_cohomology`, [`join_out_of_literature`](/entry/join-out-of-literature/) and `heckeTateFunctionalEquation'`. This is bookkeeping.

The theorem reads $O$ only through its first two fields. `literature_local` puts the field `localLanglandsExists` of $O$ in its field `llc`. `literature_automorphy` puts `O.caraianiLocalGlobalDual` in its field `car`, and it uses `pair_u_of_literature` and `hecke_l_adic_character_above_of_literature`, which read $O$ too. The other three fields ignore $O$.

## In the Lean code

The theorem is at [EveryCharacterOfLiteratureOfVWin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L639). The structure is at [BernsteinUnitaryProductIrreducible.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean#L12).

- The name says "nonexistence", but the structure is `NonEndoscopicHypothesesAlt`, and no field states that something does not exist.
- A second structure, `LitNE` in [HypothesisBundleConversions.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/HypothesisBundleConversions.lean#L30), has the same five field names, with the types `LitLoc` and `LitAut` in place of the first two.
