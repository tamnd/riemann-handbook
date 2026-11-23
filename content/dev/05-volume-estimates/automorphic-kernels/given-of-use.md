---
id: given-of-use
title: The inputs of the volume branch from eight hypotheses
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Link.given_of_use
module: Development.WeilBound.CoreStatements.AutomorphicKernels.MoriwakiBigness.HilbertSamuelApplications.GivenOfUse
covers: 760
status: drafted
drafted_by: writer@claude
---
This theorem proves the bundle `Top.Given` of the volume branch from eight hypotheses. It is one application of [`T.final_theorem_of_inputs_left`](/entry/final-theorem-of-inputs-left/), a renaming of [`given_of_inputs`](/entry/given-of-inputs/), which has twelve hypotheses. This theorem fills four of them with proved theorems and three with lemmas from arithmetic positivity. It has two users: [`deepStR_of_use`](/proof/weil-bound/) (Step 5 of [the Weil bound chapter](/proof/weil-bound/)) and [`good_tower_volume_theorem_bis`](/entry/good-tower-volume-theorem-bis/).

## Statement

`Top.Given` is the conjunction of fourteen statements, listed in [the entry for `given_of_inputs`](/entry/given-of-inputs/).

**Theorem.** Assume:

1. `ArithIntersectionSystemStatement`;
2. `HSUse`, three statements on arithmetic Kleiman and the count of small sections;
3. `MoriwakiBigStatement`, the bound $\overline{A}^{D+1} \leq \mathrm{vol}(\overline{A})$;
4. `ResKStatement`;
5. `SemiAbelianHomExtension`;
6. `HT.FarguesHodgeTate`;
7. `Flat.GagaSections`;
8. `LineOfLargeDegree.Statement`, an absolute Siegel lemma.

Then `Top.Given` holds.

Hypotheses 2 and 3 are stated in Step 2 of [the Weil bound chapter](/proof/weil-bound/), and hypothesis 8 in [the Siegel lemma entry](/entry/line-of-large-degree-of-use/).

## Proof

The proof is one call of `final_theorem_of_inputs_left`. Its twelve inputs come from three sources.

- **Proved outright.** The model clause (`Top.modelClause_holds`), `KeyFormula` (`KeyFam.keyFormula_holds`), `NumericalSegre.Statement` (`Segre.numericalSegre_closed`) and `Prov.An` (`T.analytic_provision_holds`).
- **Passed through.** Hypotheses 4 to 8.
- **Built from hypotheses 1 to 4.** `PB.Inputs` by `Giv.inputs_of_use`, `Prov.HS` by `provHS_of_use`, and `Prov.ZhangDimensionPushDownGrassmannianHeightBounds` by `nineFree_of_use`.

The last three lemmas use `hsLinks_of_use`, which turns `HSUse` and `MoriwakiBigStatement` into six statements, among them the two successive minima bounds. `inputs_of_use` also uses the projection formula and degree lemmas of the intersection system and the resolution lemmas of `ResKStatement`. The rest of `PB.Inputs` comes from lemmas with no hypotheses.

## In the Lean code

The theorem is in [GivenOfUse.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/HilbertSamuelApplications/GivenOfUse.lean#L11). The lemmas:

- `T.final_theorem_of_inputs_left` in [FinalTheoremOfInputsLeftStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/FinalTheoremOfInputsLeftStatement.lean#L19).
- `Giv.inputs_of_use` in [InputsOfUse.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/HilbertSamuelApplications/InputsOfUse.lean#L8).
- `provHS_of_use` in [ProvHSOfUse.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/HilbertSamuelApplications/ProvHSOfUse.lean#L12).
- `nineFree_of_use` in [NineFreeOfUse.lean](lean:Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/HilbertSamuelApplications/NineFreeOfUse.lean#L10).

All eight hypotheses are used. Hypothesis 4 is used twice: it is passed through and it feeds the three built inputs. `Prov.ZhangDimensionPushDownGrassmannianHeightBounds` is a conjunction of five statements, and the third is `True` ([ZhangDimensionPushDownGrassmannianHeightBounds.lean#L32](lean:Development/AutomorphicSpectrum/Statements/GeometryStatements/ZhangDimensionPushDownGrassmannianHeightBounds.lean#L32)). `nineFree_of_use` fills it with `trivial`.
