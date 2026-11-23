---
id: degree-and-coordinates-of-resolution
title: The projection formula for heights, from resolution (second name)
kind: theorem
decl: GlobalTheory.T.degree_and_coordinates_of_resolution
module: Development.AutomorphicSpectrum.Proofs.MetricProofs.DegreeAndCoordinatesOfResolutionStatement
covers: 328
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the projection formula, in two forms, from resolution](/entry/gen-deg-and-pf-coord/). It has three users below the [literature step](/step/every-character-of-literature/). [The arithmetic intersection system from Poincaré-Lelong and resolution](/entry/arith-intersection-system-of-poincare-lelong-res-k/) takes its second half. [The arithmetic Hilbert-Samuel formula on one block](/entry/theorem-hsmblock/) and [arithmetic volume and Hilbert-Samuel bounds from three inputs](/entry/hs-chain/) also call it.

## Statement

Suppose that `ResExistsStatement` holds: complex-analytic log resolutions exist for arithmetic varieties in products of projective spaces over $\mathbb{Z}$. Then two projection formulas hold for every family of heights with the axioms `IsFamily`:

1. `GenDegStatement`: let $\pi \colon X' \to X$ be the projection that forgets some factors, with $\dim X' = \dim X$. Then the height of $X'$ for pulled-back metrized line bundles is the degree of the generic fibre of $\pi$ times the height of $X$.
2. `PFCoordStatement`: the same formula when $X'$ is the closure of a point $y$ with coordinates in a field of characteristic $0$. There, the degree is the degree of the extension of function fields.

The [parent entry](/entry/gen-deg-and-pf-coord/) gives both statements in full.

## Proof

The proof is `exact genDeg_and_pfCoord`. The statement is the same, term for term.

## In the Lean code

The theorem is in [DegreeAndCoordinatesOfResolutionStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/MetricProofs/DegreeAndCoordinatesOfResolutionStatement.lean#L11). Its proof is the tactic `first | exact @genDeg_and_pfCoord | exact genDeg_and_pfCoord | (intros; apply genDeg_and_pfCoord <;> assumption)`. The two types are equal, so this is a renaming. The users call this name, not the original.
