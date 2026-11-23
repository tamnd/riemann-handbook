---
id: part-i-of-semistable-reduction-of-arc-fam
title: Part I from semistable reduction and arcs with frames
kind: theorem
decl: GlobalTheory.partI_of_semistableReduction_of_arcFam
module: Development.AbelianVarietyTheory.Proofs.ModuliProofs.PartIOfSemistableReductionOfArcFam
covers: 328
status: drafted
drafted_by: writer@claude
---
This theorem derives $\mathrm{PartI}$ from two statements: the semistable reduction theorem and `ArcFamSt`. [Part I from semistable reduction](/entry/part-i-of-semistable-reduction/) applies it with [`arcFam_closed`](/entry/arc-fam-closed/) as the second input. Its dominator in the written proof is the step [EveryCharacter from the literature and VWin](/step/every-character-of-literature/).

## Statement

**Theorem.** `SemistableReductionSt` and `ArcFamSt` together imply $\mathrm{PartI}$.

The three statements are given in the entries above: $\mathrm{PartI}$ and `SemistableReductionSt` in [Part I from semistable reduction](/entry/part-i-of-semistable-reduction/), and `ArcFamSt` in [`arcFam_closed`](/entry/arc-fam-closed/).

## Proof

The proof applies `T.modelSystems_jointProperties_of_laws`. That lemma takes fourteen statements and gives $\mathrm{PartI}$. Twelve of them come from proven lemmas:

- `twistedPrincipalPolarisation_sections_baseChange`;
- the six laws on abelian schemes, from `all_six_abelian_scheme_laws_hold`;
- `ega_holds`;
- `uniformisation_dvr_unconditional` and `linearUniformisation_triples_torsion`;
- `homExtension_semiAbelian_discreteValuationRing`: homomorphisms of semi-abelian schemes extend from the generic fibre over a discrete valuation ring;
- `siegelFamilies_exist`, which gives the clause $N_0$ on Siegel families.

The two hypotheses give the other two. `ArcFamSt` is used as it is. The semistable reduction theorem gives `ModelsSt` through `modelsSt_of_semistableReduction`. `ModelsSt` says: for each $E$, $H$, $D$ with $p + q \ge 1$ and each family of moduli spaces, there is a system of local models, one for each prime $p$ and each valuation subring $W \subset \mathbb{C}$ with $p \in \mathfrak{m}_W$, with the clauses `N2`, `SplitFibres` and `Amp` at each level, and with `N6`. That lemma applies `T.exists_localModelSystems_ampleFrames` to [`exists_fullLevelAmpleModel_of_semistableReduction`](/entry/exists-full-level-ample-model-of-semistable-reduction/), and through it the projective model of [`topAmpExists`](/entry/top-amp-exists/) enters.

## In the Lean code

The theorem is in [PartIOfSemistableReductionOfArcFam.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/PartIOfSemistableReductionOfArcFam.lean#L25). It is an assembly, and the work is in the lemmas that it calls.

- `T.modelSystems_jointProperties_of_laws` is in [ModelSystemsJointPropertiesOfLawsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ModelSystemsJointPropertiesOfLawsStatement.lean#L21).
- `modelsSt_of_semistableReduction` is in [ModelsOfSemistableReduction.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/ModelsOfSemistableReduction.lean#L20).
- `ModelsSt` is in [ArcFamSt.lean](lean:Development/AbelianVarietyTheory/Statements/SemistableTorsion/ArcFamSt.lean#L26).

We have not unfolded the proof of `modelSystems_jointProperties_of_laws` or of `exists_localModelSystems_ampleFrames`.
