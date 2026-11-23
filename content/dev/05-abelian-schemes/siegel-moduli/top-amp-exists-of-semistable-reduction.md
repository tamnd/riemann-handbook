---
id: top-amp-exists-of-semistable-reduction
title: The inputs of the projective model with ample frames
kind: theorem
decl: GlobalTheory.topAmpExists_of_semistableReduction
module: Development.AbelianVarietyTheory.Proofs.ModuliProofs.ExistsFullLevelAmpleModelOfSemistableReduction
covers: 1071
status: drafted
drafted_by: writer@claude
---
This theorem proves `TopAmpExists` from the semistable reduction theorem. It fills the ten hypotheses of [`exists_fullLevel_model_ample_frames`](/entry/exists-full-level-model-ample-frames/): nine with proven theorems, and one with the hypothesis itself. Its result is renamed as [`exists_fullLevelAmpleModel_of_semistableReduction`](/entry/exists-full-level-ample-model-of-semistable-reduction/).

## Statement

**Theorem.** `SemistableReductionSt` implies `TopAmpExists`.

`SemistableReductionSt` is Grothendieck's semistable reduction theorem for polarized abelian varieties over finite extensions of $\mathbb{Q}_p$; see [Part I](/entry/part-i-of-semistable-reduction/). `TopAmpExists` is stated in full in [`topAmpExists`](/entry/top-amp-exists/): for each unitary PEL datum and each auxiliary prime $n$, a normal projective flat model of level $n^J$ with ample frames of level $(n^k)^2$.

## Proof

Let $S$ be the proof of `SemistableReductionSt`. The proof applies `exists_fullLevel_model_ample_frames` to these ten terms, in the order of its hypotheses.

1. `HomExtSt`: `T.homExtension_semiAbelian_discreteValuationRing`.
2. `Out.Laws` and 3. `Out.Laws2`: the first two parts of `T.all_six_abelian_scheme_laws_hold`.
4. `SemistableReductionSt`: $S$.
5. `ThmUSt` and 6. `UTorsSt`: the two parts of `T.uniformisationExistence_and_torsion_statements`.
7. `ZHGeoSt`: [`T.zarhinGeometric_of_semistableReduction`](/entry/zarhin-geometric-of-semistable-reduction/) $S$.
8. The reduction statement for theta objects over complete discrete valuation rings: `T.goodReduction_of_thetaPoint_units`, applied to the two laws, to `T.semistableReductionSplit_of_padic` $S$ (of type `SS.SemistablePol`) and to the two uniformization statements.
9. The theorem of the cube: `T.theorem_of_cube_polAbelianScheme`.
10. `ThetaUnifAV`: `T.theta_uniformisation_complex_abelian_varieties`.

So $S$ enters three times: directly, through `ZHGeoSt`, and through the reduction statement 8. The entry [`topAmpExists`](/entry/top-amp-exists/) says what each hypothesis states.

## In the Lean code

The theorem is in [ExistsFullLevelAmpleModelOfSemistableReduction.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/ExistsFullLevelAmpleModelOfSemistableReduction.lean#L24). The proof is a single term.

The lemmas it calls have closed types: each is a statement with no hypothesis, or, for 7 and 8, a function of $S$ and of the other proven lemmas. So the theorem only distributes $S$ and nine theorems to the hypotheses of the next lemma. The work is in [`topAmpExists`](/entry/top-amp-exists/).

The term `T.all_six_abelian_scheme_laws_hold` is a conjunction of six bundles `Laws` to `Laws6`. This proof uses only the first two. The term `T.uniformisationExistence_and_torsion_statements` is written out three times; this has no effect on the statement.
