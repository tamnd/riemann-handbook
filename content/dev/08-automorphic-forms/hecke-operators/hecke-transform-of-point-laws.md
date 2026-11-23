---
id: hecke-transform-of-point-laws
title: Hecke transforms from the point laws
kind: theorem
decl: GlobalTheory.HeckeEx.heckeTransform_of_pointLaws
module: Development.AbelianVarietyTheory.Proofs.TwistedOperators.HeckeTransformOfPointLaws
covers: 431
status: drafted
drafted_by: writer@claude
---
This theorem is the transform part of [the Hecke integrality, transform and reading facts](/entry/hecke-int-transform-read-tie/). It says that the point laws of Hecke correspondences give Hecke operators on sections. It only pairs two proofs. The content is in [the section transform](/entry/sec-transform/).

## Statement

If `HeckePointLaws` holds, then `HeckeTransform` holds. Here `HeckeTransform` is `SecTransform ∧ CuspTransform`.

- `SecTransform`: at a split-off prime, every section $f$ of weight $(a, n)$ has a transform $g$ of the same weight, with $g(y) = \mathrm{hkScal} \cdot \sum_C f(y/C)$ at every geometric point $y$, summed over the Hecke kernels $C$.
- `CuspTransform`: for every datum, at a split-off prime and in the allowed range, `KeepsCusp` holds. `KeepsCusp` says that whenever the transform exists, points detect sections, and the kernels are finite, the Hecke operator maps cusp forms to cusp forms.

`HeckePointLaws` is the conjunction of four laws: the kernels are finite, every kernel has a target point, the target point is unique, and points detect sections.

## Proof

The proof is `fun h => ⟨secTransform h, cuspTransform⟩`.

## In the Lean code

The theorem is on [line 419 of HeckeTransformOfPointLaws.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/HeckeTransformOfPointLaws.lean#L419). `cuspTransform` is on line 404 and takes no hypothesis. This is possible because `KeepsCusp` assumes the transform, detection and finiteness itself ([SplitOffDetection.lean](lean:Development/AbelianVarietyTheory/BlockTheory/TwistedDiscreteSeries/SplitOffDetection.lean#L50)). The point laws are in [HeckePrimeDetection.lean](lean:Development/AbelianVarietyTheory/BlockTheory/TwistedDiscreteSeries/HeckePrimeDetection.lean#L56). Only two of the four laws are used, by `secTransform`.
