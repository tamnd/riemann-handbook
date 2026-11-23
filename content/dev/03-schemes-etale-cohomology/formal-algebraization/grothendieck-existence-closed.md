---
id: grothendieck-existence-closed
title: Grothendieck's existence theorem for closed subschemes, second name
kind: theorem
decl: GlobalTheory.T.grothendieck_existence_closed
module: Development.AutomorphicSpectrum.Proofs.BlockDecomposition.GrothendieckExistenceClosedStatement
covers: 499
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`GE.geClosed`](/entry/ge-closed/), which has the content. It proves the statement `GEClosed`: over a Noetherian ring $R$ that is complete for an ideal $I$, a compatible system of closed subschemes of the thickenings $X \times_R R/I^{e+1}$, with proper reduction, comes from one closed subscheme of $X$ that is proper over $R$. Its one user is [the formal algebraisation theorem](/entry/formal-thickening-formal-algebraisation/), which passes it to `formal_morphism_existence` to build morphisms from compatible families of morphisms. Below this theorem are 499 declarations.

## Statement

**Theorem.** `GEClosed` holds.

The full statement, with all hypotheses, is in [the entry for `geClosed`](/entry/ge-closed/).

## Proof

Apply `GlobalTheory.CompanionTheory.GE.geClosed`.

## In the Lean code

The file is [GrothendieckExistenceClosedStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/GrothendieckExistenceClosedStatement.lean#L7). The proof is the tactic `first | exact @GE.geClosed | exact GE.geClosed | (intros; apply GE.geClosed <;> assumption)`. The first branch succeeds, so the proof is the term `geClosed`. The statement `GEClosed` is defined in [GEClosedProj.lean](lean:Development/WeilBound/CoreStatements/TemperedRepresentationTheory/FormalAlgebraisation/GEClosedProj.lean#L13).

The theorem is used once, in [Development.lean](lean:Development/WeilBound/CoreStatements/TemperedRepresentationTheory/FormalAlgebraisation/Development.lean#L20), as the first argument of `formal_morphism_existence`. The other input there is `iso_of_thickenings`, a proof of `IsoOfThick`.

The size of this node (499) is one more than the size of `geClosed` (498). The extra declaration is this name.
