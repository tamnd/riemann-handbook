---
id: built-bounds-compact-of-leaves
title: The built bounds from their leaves, second name
kind: theorem
decl: Formalism.FourierDecayAlt.P.built_bounds_compact_of_leaves
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.BuiltBoundsCompactOfLeaves
covers: 386
status: drafted
drafted_by: writer@claude
---
This theorem is a second name. Its proof is the term `PBASM.builtBounds2CptOfLeaves`, and its statement is the same proposition `BuiltBounds2CptOfLeaves`. It exists so that [the built bounds from the head formula](/entry/built-bounds-compact-of-head-top/) can call the result with a name in the namespace `Formalism.FourierDecayAlt.P`. The real content is in [the built bounds from their leaves](/entry/built-bounds2-cpt-of-leaves/).

## Statement

`BuiltBounds2CptOfLeaves` is an implication with eight premises: the radial head formula `RadHead`, the top head formula `HeadTop`, the lift degree identity `DegLift`, the top local bound `TopLocB`, the top degree identity `DegTop`, the top ratio bound `TopRatio`, the germ parts `GermPartsC`, and the uniform decay bound `DecayUnif` under the premise `ThmPActualCpt`. The conclusion is `BuiltBounds2Cpt`, which is stated in [the built bounds at the infinite places, restated](/entry/pb-built-bounds2-cpt/).

**Theorem.** `BuiltBounds2CptOfLeaves` holds.

## Proof

The proof is the name `PBASM.builtBounds2CptOfLeaves`. There is nothing else.

## In the Lean code

The theorem is in [BuiltBoundsCompactOfLeaves.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/BuiltBoundsCompactOfLeaves.lean#L57). The proposition is at [line 41](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/BuiltBoundsCompactOfLeaves.lean#L41) and the proof that it renames at [line 45](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/BuiltBoundsCompactOfLeaves.lean#L45) of the same file.
