---
id: built-ex-of-published-inputs-prime
title: The automorphic side exists at a stage
kind: theorem
decl: GlobalTheory.HeightCounting.Fin3.builtEx_of_published_inputs'
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.FinitenessOfHyp
covers: 456
status: drafted
drafted_by: writer@claude
---
At a stage $x$ with a `StrictHenselianAcyclicLevel` datum $l$, the automorphic side exists. This is step 1 of [the level 3 record at one stage](/entry/lv3-of-third-alt-alt/), where it discharges the premise of `EtaStatement'`. The proof collects the hypotheses of [`side_rational_hecke_data_alt`](/entry/side-rational-hecke-data-alt/). The content is in [`ndSpec_exists_alt`](/entry/nd-spec-exists-alt/) and [`locAll_exists_alt`](/entry/loc-all-exists-alt/).

## Statement

Let $A$, $M$, $\chi$ and `tup` be the data that $l$ carries. `AutomorphicSideExists A M χ tup` says: for each finite set `big` of complex numbers at each place, there is $L$ of type `LocAll` such that

1. there is `Sp : NdSpec` for $L$ whose coefficient embeddings reach each number of `big`;
2. an `AutomorphicSpecialisation` ties $L$ to $A$, $M$ and `tup`;
3. each residual representation $\bar\rho_{\sigma, w}$ of $L$ is semisimple.

**Theorem.** If `PublishedInputsThirdLayerAlt` holds, then `AutomorphicSideExists A M χ tup`.

## Proof

Apply `side_rational_hecke_data_alt` at `Dof x`. Its hypotheses come from:

- global Artin reciprocity: the field `art` of the published inputs;
- `ChebSplit`: `chebSplit_nd`, from the input `ChebotarevDegreeOne`;
- `MtInput`: `mtInput_of_levelC`;
- the conditions on `star`, on `eExp` and on split places: the fields of `l.a.elem`;
- the values of the twist characters: `twDat_psi_valuesIn_LL`;
- `OtoLL` is injective onto the integers of a subfield: `l.a.omax`;
- `BlocksUnique`: `blocksUnique_of_cgTrue_alt`, from five published inputs and `l.a.cg`.

## In the Lean code

The theorem is in [FinitenessOfHyp.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FinitenessOfHyp.lean#L35). `AutomorphicSideExists` and the condition `BuiltAlt` are in [ForcedByAutomorphicSemisimpleData.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ForcedByAutomorphicSemisimpleData.lean#L15).

- The name says `builtEx`, but the conclusion is `AutomorphicSideExists`. The older `builtEx`, in [FinitenessOfHyp.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/FinitenessOfHyp.lean#L47), proves `BuiltEx`.
- We have not read the proof of `blocksUnique_of_cgTrue_alt`.
