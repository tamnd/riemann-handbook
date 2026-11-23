---
id: start-admissible
title: The start data fit each model level
kind: theorem
decl: Formalism.FourierDecayAlt.P.start_admissible
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.CoordinateCommuteRaisingConstant
covers: 509
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the start data at a model level](/entry/start-ok/). The two statements differ only in how the laws of the algebra enter. Here they are an explicit hypothesis. There they are a type class instance. The real content is in that entry. The theorem is one of the inputs of the model frame `model_frame_algebra`, which is below the trunk node [HypsAlt is nonempty](/step/nonempty-hyps/).

## Statement

Let $P$ be parameters with `P.OK`. Let $D$ be an algebra with coordinates and Euler operators that satisfies the laws `D.Laws` for the constant $T T'$ of $P$. Let $L$ be level data whose fields are all the model operators (`IsModelLevel`). Let `startM P D l` be the start data of [the start data at a model level](/entry/start-ok/).

**Theorem.** For each $l$, the data `startM P D l` is a start for $L$ (`IsLevelStart`).

## Proof

The proof turns the hypothesis `D.Laws P.TT` into an instance of `Fact (D.Laws P.TT)`. Then it applies `startOK`. Nothing else happens.

## In the Lean code

The theorem is at [CoordinateCommuteRaisingConstant.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CoordinateCommuteRaisingConstant.lean#L6160). The statement `StartOKD` is in [StatementMA.lean](lean:Formalism/HermitianCurvature/StatementMA.lean#L522). The file of the theorem has the same wrapper for other statements, for example `level_star_holds` at line 6155. The users are `model_frame_algebra` at line 6190 and a proof in [IsAdmissibleSplittingCharPairMulTwist.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/IsAdmissibleSplittingCharPairMulTwist.lean#L5469).
