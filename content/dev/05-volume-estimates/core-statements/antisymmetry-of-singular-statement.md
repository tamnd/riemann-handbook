---
id: antisymmetry-of-singular-statement
title: The swap relation on a good tower, given the singular metric statement
kind: theorem
decl: SquareStatements.antisymmetry_of_singular_statement
module: Development.WeilBound.CoreStatements.MultihomogeneousSquares.AntisymmetryOfSingularStatement
covers: 1488
status: drafted
drafted_by: writer@claude
---
This theorem only passes hypotheses along. It is [the swap relation from seven statements](/entry/good-tower-antisymmetry-of/) with six of the seven statements filled by proved lemmas. One statement stays a hypothesis: the singular metric statement `StSing`. [The swap relation on a good tower](/entry/good-tower-antisymmetry/) fills that last one. The real content is in [the seven statements entry](/entry/good-tower-antisymmetry-of/) and in the lemmas below.

## Statement

**Theorem.** Assume `StSing`. Then `GoodTowerAntisymmetry` holds.

`StSing` says: for a flag model $M$ with a Hodge base metric, and Hermitian lines $s_r$ with the right degrees that are Hodge lines of a flag, the combined line of the $s_r$ for each root $a$ has the same metric as the base metric for $a$, at each point of the model in the orbit of a point off the boundary. `GoodTowerAntisymmetry` is stated in full in [the entry on the seven statements](/entry/good-tower-antisymmetry-of/).

## Proof

The proof is one term. It applies `good_tower_antisymmetry_of` to:

- `stXB` for `StX` (the singular combined lines are limits of smooth metrics);
- `alg_of stEmb stFormB` for `StAlg` (the analytic realization of a flag model is algebraic);
- `HeightCancellation.stHt` for `StHt` (a vector bundle condition on the Hodge-Tate pieces passes along a map of Hodge data);
- `hSing` for `StSing`;
- `stBase` for `StBase` (a Hodge compactification with simple normal crossings boundary exists);
- `stCmp` for `StCmp` (two Hodge ties have intersection data that differ by the degree of the flag);
- `antisymmetry_transposition_factor` for `AntisymmetryFibreSquares`.

The words in parentheses describe the Lean statements in `AntisymmetryFibreSquares.lean`. We have not read the proofs of these lemmas.

## In the Lean code

The theorem is in [AntisymmetryOfSingularStatement.lean](lean:Development/WeilBound/CoreStatements/MultihomogeneousSquares/AntisymmetryOfSingularStatement.lean#L13). The statements are in [AntisymmetryFibreSquares.lean](lean:Development/WeilBound/CoreStatements/MultihomogeneousSquares/AntisymmetryFibreSquares.lean#L78). The lemmas are `stXB` in [SmoothComb.lean](lean:Development/WeilBound/CoreStatements/MultihomogeneousSquares/SmoothComb.lean#L19), `alg_of` in [IsMultiHomogRenameBaseInc.lean](lean:Development/WeilBound/CoreStatements/MultihomogeneousSquares/IsMultiHomogRenameBaseInc.lean#L57), `stHt` in [HtCancel.lean](lean:Development/WeilBound/CoreStatements/JacobiBlockDeterminants/HtCancel.lean#L19), `stBase` in [ExistsBase.lean](lean:Development/WeilBound/CoreStatements/MultihomogeneousSquares/ExistsBase.lean#L103) and `stCmp` in [PolySmulOfSameSing.lean](lean:Development/WeilBound/CoreStatements/MultihomogeneousSquares/PolySmulOfSameSing.lean#L71).
