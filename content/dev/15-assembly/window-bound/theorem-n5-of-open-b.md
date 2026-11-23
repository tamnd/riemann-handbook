---
id: theorem-n5-of-open-b
title: The congruence length bound from the last layer of open inputs
kind: theorem
decl: Formalism.MainNotions.N.K.Final.theorem_n5_of_open_b
module: Formalism.AdmissibleDesigns.StatementOneBChangedOfOpen
covers: 878
status: drafted
drafted_by: writer@claude
---
This theorem is a pass-through. It proves the bound `GlobalLatticeIndexTheorem` on $v_{cc}(\pi)$ by calling [`theorem_n5_of_ring_inputs`](/entry/theorem-n5-of-ring-inputs/), and it builds the tuple `SelmerInequalityThree` that that theorem asks for. Its only caller is [the congruence length bound from the local inputs](/entry/theorem-n5-from-inputs/). The real content is in `theorem_n5_of_ring_inputs` and in the lemmas that fill the tuple.

## Statement

The notation is that of [the parent entry](/entry/theorem-n5-from-inputs/). Assume `admG1`, `admG2`, `admG3`, `TameGeneratorConditions`, `admG6`, `admBK`, `BlochKatoAnnihilators`, `FamilyContinuous`, `SemisimpleDecomposition`, `FontaineAtPlacesOverL`, `tateH1FinitenessAtPlacesOver`, `adm51`, `UnrIn`, `SelfGood` and the last layer `RemainingInputsLastLayer`.

**Theorem.** Under these hypotheses, `LengthBoundAtPlaces`, `LiftExponentAtPlaces` and `admTB` imply `GlobalLatticeIndexTheorem`.

## Proof

Apply `theorem_n5_of_ring_inputs`. Its last hypothesis asks, for each ring datum `Dd` with `RingDef` for $r^{\mathrm{N}}$, for `SelmerInequalityThree`. Split the last layer into its five parts `RhoOpenA`, `TBOpen`, `ChiOpen`, `FirstLocalConditionOpen` and `RowTieIn`. Then `plugOpen3_B` puts these parts, the Bloch-Kato and Fontaine inputs, and `admG2` and `SemisimpleDecomposition` moved to $r^{\mathrm{N}}$ into the fourteen components of the tuple. Each component that is not a hypothesis is a call to one lemma (`KFin.κ`, `StA.colLx`, `StD.bKa_clause`, `StD.tie_clause` and others), which we did not open.

## In the Lean code

The theorem is in [StatementOneBChangedOfOpen.lean](lean:Formalism/AdmissibleDesigns/StatementOneBChangedOfOpen.lean#L351), with `plugOpen3_B` at line 316 and `RemainingInputsLastLayer` at line 340. Every hypothesis is used. The same file defines `RemainingInputsRankFive` (line 160) and `RemainingInputsAfterColumns` (line 259), which no other file uses.
