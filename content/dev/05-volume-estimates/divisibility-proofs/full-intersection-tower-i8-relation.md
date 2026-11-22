---
id: full-intersection-tower-i8-relation
title: The antisymmetry of the height defect on a good tower
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Top.full_intersection_tower_I8_relation
module: Development.AutomorphicSpectrum.Proofs.DivisibilityProofs.FullIntersectionTowerI8Identity
covers: 1619
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It is the term `SquareStatements.good_tower_antisymmetry`, with the same statement. That theorem is again one line, and the real content is in [`good_tower_antisymmetry_of`](/entry/good-tower-antisymmetry-of/). Its user is the statement form [`full_intersection_tower_I8_identity`](/entry/full-intersection-tower-i8-identity/).

## Statement

The statement is that of [`full_intersection_tower_I8_identity`](/entry/full-intersection-tower-i8-identity/). Assume `CmpSt`, $\mathrm{Given}$ and `Out.WeilSt`. For a good tower $T$ with `Extra`, a full intersection system and $p, q \geq 1$, the defect $D_{B,c}(\lambda) = \mathrm{PP}_{B,c}(L_\lambda^{d+1}) - \mathrm{vol}(c)\,h_{\mathrm{Fl}}(L_\lambda^{d+1})$ changes sign when two adjacent entries $a, a+1$ of $\lambda$ with $a + 1 \neq j$ are swapped.

## Proof

The proof is a chain of three names with the same statement:

1. [`good_tower_antisymmetry`](/entry/good-tower-antisymmetry/) is `antisymmetry_of_singular_statement HeightCancellation.stSing`.
2. [`antisymmetry_of_singular_statement`](/entry/antisymmetry-of-singular-statement/) applies `good_tower_antisymmetry_of` to the inputs `stXB`, `alg_of stEmb stFormB`, `HeightCancellation.stHt`, the singular statement, `stBase`, `stCmp` and `antisymmetry_transposition_factor`.
3. [`good_tower_antisymmetry_of`](/entry/good-tower-antisymmetry-of/) applies the fibre square result `AntisymmetryFibreSquares` with `antisymmetry'`, `agreement_positive`, the tenth part of $\mathrm{Given}$ (`PB.Inputs`) and a square from `sq_of`.

## In the Lean code

The theorem is in [FullIntersectionTowerI8Identity.lean](lean:Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/FullIntersectionTowerI8Identity.lean#L28). The chain is in [GoodTowerAntisymmetry.lean](lean:Development/WeilBound/CoreStatements/MultihomogeneousSquares/GoodTowerAntisymmetry.lean#L20), [AntisymmetryOfSingularStatement.lean](lean:Development/WeilBound/CoreStatements/MultihomogeneousSquares/AntisymmetryOfSingularStatement.lean#L13) and [GoodTowerAntisymmetryOf.lean](lean:Development/WeilBound/CoreStatements/MultihomogeneousSquares/GoodTowerAntisymmetryOf.lean#L20). With the statement form, four names carry one statement. We have not unfolded `AntisymmetryFibreSquares`, `sq_of`, `tie_of` or the inputs `stXB`, `stSing` and the others.
