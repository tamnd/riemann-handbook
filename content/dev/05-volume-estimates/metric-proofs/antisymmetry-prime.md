---
id: antisymmetry-prime
title: The sign change of the height defect, the statement form
kind: theorem
decl: GlobalTheory.T.antisymmetry'
module: Development.AutomorphicSpectrum.Proofs.MetricProofs.AntisymmetryStatement
covers: 624
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It states $\mathrm{Antisymmetry}$, and its proof applies [the sign change of the height defect](/entry/antisymmetry/), where the real content is. Its user is [the swap relation from seven statements](/entry/good-tower-antisymmetry-of/), which passes it to `AntisymmetryFibreSquares` as the input `Antisymmetry`.

## Statement

$\mathrm{Antisymmetry}$ is stated in full in [the sign change of the height defect](/entry/antisymmetry/). In short: for a realization $\mathrm{Re}$ of an analytic system $S$ with a flag system for $j$, the polynomial $\mathrm{PB}^{\mathrm{wt}} - \mathrm{vol}(S)\, h$ is homogeneous of degree $|\Psi|\binom{N}{2} + 1$ and changes sign under each block simple swap. Here $\mathrm{PB}^{\mathrm{wt}}$ is the limit height polynomial of $\mathrm{Re}$ in gap coordinates, and $h$ is the height polynomial of the flag variety.

## Proof

The proof is `first | exact @GlobalTheory.CompanionTheory.Ar.PB.Top.antisymmetry | ...`. It applies the theorem with the same statement.

## In the Lean code

The theorem is in [AntisymmetryStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/MetricProofs/AntisymmetryStatement.lean#L9). The statement `Antisymmetry` is in [AgreementIffGuarded.lean](lean:Development/AutomorphicSpectrum/Statements/MetricStatements/AgreementIffGuarded.lean#L82). The prime in the name does not mark a variant: the statement is the same as that of `GlobalTheory.CompanionTheory.Ar.PB.Top.antisymmetry`.
