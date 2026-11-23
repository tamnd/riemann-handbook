---
id: twist-core-surjective
title: Lifts down the core column reach every core form, second name
kind: theorem
decl: GlobalTheory.T.twist_core_surjective
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.TwistCoreSurjectiveOfLocalComponents
covers: 332
status: drafted
drafted_by: writer@claude
---
This theorem is a second name. It proves the statement `CoreOnto`, which [the separation of rows by real functionals](/proof/bessel-seesaw/) needs as one input of `rowSeparation_by_realFunctionals_of_chain_steps`. The proof only applies [`twist_core_surjective_of_local_components`](/entry/twist-core-surjective-of-local-components/), and that entry has the real content.

## Statement

**Theorem.** Assume [`ThetaLocalInputs`](/step/theta-local-inputs-def/) and eleven named literature statements: `HarishChandraFinite`, `CuspRapidDecay`, `DiscreteSeriesCover`, `HarishChandraModules`, `CasselmanWallach`, `HoweUnram`, `WeilRepresentationUnitaryPair`, `WeilSiegelFormulaUnitary`, `SiegelWeilUnitaryConvergent`, `DoublingMethodLocalZetaIntegrals` and `UnramifiedDoublingGL`. Then `CoreOnto` holds.

`CoreOnto` says, in short, that each automorphic form on the first node of the core column, evaluated at a $K$-finite vector, is in the span of the forms that a chain of theta lifts down the core column reaches from the top. [The child entry](/entry/twist-core-surjective-of-local-components/) states it in full.

## Proof

The proof is `first | exact twist_core_surjective_of_local_components | ...`. The first branch closes the goal, since the two statements are the same.

## In the Lean code

The theorem is in [TwistCoreSurjectiveOfLocalComponents.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistCoreSurjectiveOfLocalComponents.lean#L32). `CoreOnto` is in [OffQOfSizeRows.lean](lean:Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/OffQOfSizeRows.lean#L123).

The one caller passes nine of the eleven statements as fields of the `ThetaLocalInputs` record that it also passes. Only `HoweUnram` and `SiegelWeilUnitaryConvergent` are new inputs.
