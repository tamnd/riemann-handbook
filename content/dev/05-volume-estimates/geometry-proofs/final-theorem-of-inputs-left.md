---
id: final-theorem-of-inputs-left
title: The inputs of the volume branch from twelve hypotheses, restated
kind: theorem
decl: GlobalTheory.T.final_theorem_of_inputs_left
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.FinalTheoremOfInputsLeftStatement
covers: 1192
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`given_of_inputs`](/entry/given-of-inputs/), which assembles the conjunction `Top.Given` from twelve hypotheses. That entry has the content. This theorem has three users: [`goodTower_volume_of_reduced`](/entry/good-tower-volume-of-reduced/), `given_of_use` (which [`deepStR_of_use`](/proof/weil-bound/) calls) and `given_of_moriwaki`.

## Statement

The statement is the same as that of [`given_of_inputs`](/entry/given-of-inputs/). If the following twelve statements hold, then `Top.Given` holds:

1. the model clause (`PartI`, `N1ab`, `N1c` and the toroidal compatibilities of level and Hecke operators);
2. `KeyFormula`;
3. `SemiAbelianHomExtension`;
4. `NumericalSegre.Statement`;
5. `ResKStatement`;
6. `HT.FarguesHodgeTate`;
7. `Flat.GagaSections`;
8. `LineOfLargeDegree.Statement`, an absolute Siegel lemma;
9. `PB.Inputs`;
10. `Prov.HS`;
11. `Prov.An`;
12. `Prov.ZhangDimensionPushDownGrassmannianHeightBounds`.

## Proof

The statement is the same as that of `given_of_inputs`, and the proof applies it.

## In the Lean code

The theorem is in [FinalTheoremOfInputsLeftStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/FinalTheoremOfInputsLeftStatement.lean#L19). The proof is

```
first | exact @GlobalTheory.CompanionTheory.Ar.Top.given_of_inputs | ...
```

The name does not say what the theorem proves. The conclusion is `Top.Given`, a list of inputs, not a final theorem. We found no meaning for "left" in the statement. The file `FinalTheoremOfInputsRight.lean` holds `goodTower_volume_of_reduced`, which uses this theorem.
