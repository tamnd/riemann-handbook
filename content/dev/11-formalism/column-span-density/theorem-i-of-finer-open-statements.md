---
id: theorem-i-of-finer-open-statements
title: The base-level projection bound from the finer open statements
kind: theorem
decl: Formalism.MainNotions.flipOneThree.Pf.theorem_I_of_finer_open_statements
module: Formalism.SharpRestriction.GrowthBounds.ColumnSpanDensity.TheoremIOfLatticeFunctorComparison
covers: 430
status: drafted
drafted_by: writer@claude
---
This theorem reduces `SecondPartClosed D` to three statements: `LPRingIndep`, `LatticeFunctorComparison` and `RestCloudMaps`. Its only caller is [the bound from the lattice functor comparison](/entry/theorem-i-of-lattice-functor-comparison/), which proves `LPRingIndep`. The proof turns the two other statements into three intermediate bounds and passes them to `second_estimate_of_restrictions`.

## Statement

The three statements and `SecondPartClosed D` are as in the entries above: `LPRingIndep` in [the parent entry](/entry/theorem-i-of-lattice-functor-comparison/), `LatticeFunctorComparison` in [the bound from the model identification](/entry/theorem-i-of-model-identification/), and `RestCloudMaps` in [the bound from the explicit minor map](/entry/theorem-i-of-explicit-minor-map/).

**Theorem.** For each datum $D$, `LPRingIndep`, `LatticeFunctorComparison` and `RestCloudMaps` imply `SecondPartClosed D`.

## Proof

Assume `AdmBE D`. `tools_of_admitted_statements` specializes it at $C_c = 4$ and gives `AdmT D`. The proof takes two tools from it: `TypeDecompositionsCommute D`, that is `DualHeightBasis`, `DualHeightInclusion`, `BePerfect` and `HLSpans`; and `PairedPathIndependence D`, whose second half is `WeylV`: $\dim V(\lambda_0)$ is the product of $(\lambda_i - \lambda_j + j - i)/(j - i)$ over $i < j$ and over the factors. This has the form of the Weyl dimension formula for $\mathrm{GL}_{m+1}$ (Fulton and Harris, *Representation Theory*, Theorem 6.3).

1. **`RhoSumLowerBoundEdge`.** `lattice_maps_of_functor_comparison` turns `LatticeFunctorComparison` into `RhoSumLatticeMaps`. `rho_sum_bound_of_maps_splitting` adds `blockSplit'` (proved from `KP.blockSplit`).
2. **`CloudWeightLowerBound`.** `cloud_bound_of_maps`, from `RestCloudMaps`, `BePerfect`, `DualHeightBasis` and `WeylV`.
3. **`ResidueClassCount`.** `tensor_bound_of_order_bound`, from `restTensor`, `restOrdBound`, `DualHeightBasis` and `DualHeightInclusion`. The first two are proved.

`second_estimate_of_restrictions`, in the same file, takes `LPRingIndep` and these three bounds. It takes `AdmT D` again, gets `RestDims` from `PairedPathIndependence D` by `restDims_of`, and calls `theorem_I_of_intermediate_bounds` with the mean bound `midMean_of`, the bound `midLP_of rho_lower_bound_large_conductor` and the threshold facts `thrLP` and `thrFM`.

We have not unfolded the three intermediate bounds, and we have not followed `theorem_I_of_intermediate_bounds` past its first lines. There it specializes `AdmBE D` at $C_c = 4$, $C_{E1} = C_{E2} = C_m = T_1$ and $C_H = T_2$, as `tools_of_admitted_statements` does.

## In the Lean code

The theorem is in [TheoremIOfLatticeFunctorComparison.lean](lean:Formalism/SharpRestriction/GrowthBounds/ColumnSpanDensity/TheoremIOfLatticeFunctorComparison.lean#L54), with `second_estimate_of_restrictions` at line 45 and `tools_of_admitted_statements` at line 31. The callees are in the same folder: [RhoSumBoundOfMapsSplitting.lean](lean:Formalism/SharpRestriction/GrowthBounds/ColumnSpanDensity/RhoSumBoundOfMapsSplitting.lean#L88), [CloudPropOfMapsBasis.lean](lean:Formalism/SharpRestriction/GrowthBounds/ColumnSpanDensity/CloudPropOfMapsBasis.lean#L106), [TensorBoundOfOrderBound.lean](lean:Formalism/SharpRestriction/GrowthBounds/ColumnSpanDensity/TensorBoundOfOrderBound.lean#L48) and [TheoremIOfIntermediateBounds.lean](lean:Formalism/SharpRestriction/GrowthBounds/ColumnSpanDensity/TheoremIOfIntermediateBounds.lean#L28).

The tools come from the hypothesis `AdmBE D`, not from proofs. So `DualHeightBasis`, `BePerfect` and `WeylV` are assumed here, though `WeylV` has the form of a classical formula. This theorem and the three above it in this file are a chain of reductions; each one removes or replaces one hypothesis.
