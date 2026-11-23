---
id: model-place-built2-of-jf
title: Model places from the smoothness of the transfer
kind: theorem
decl: Formalism.FourierDecayAlt.P.CutMP.modelPlaceBuilt2_of_jf
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.CutJAPRSSnRep
covers: 1916
status: drafted
drafted_by: writer@claude
---
This theorem is a relay. It proves `ModelPlaceBuilt2` from the hypothesis `JfSmoothDS`, and it supplies the second input of the theorem below it, the polynomial radial relation. Its only user is [model places from the chart equations](/entry/model-place-built2-of-chart-eqs/), which proves `JfSmoothDS`. The statement `ModelPlaceBuilt2` is given in words in [each place of a built setting is a model place](/entry/model-place-built-holds/).

## Statement

**Theorem.** If `JfSmoothDS` holds, then `ModelPlaceBuilt2` holds.

`JfSmoothDS` says: there is $C_c$ such that at each built place with constant $C_c$, the transfer `B.JF` of each $f_v$ lies in the function space `Q.FFl` on the domain `OmP`. We have not unfolded `Q.FFl`.

## Proof

The proof is one line:

```
modelPlaceBuilt2_of_polyS hJ JA.SSn.Rep.Core.TC.PR.polynomial_radial_holds
```

[`modelPlaceBuilt2_of_polyS`](/entry/model-place-built2-of-poly-s/) takes `JfSmoothDS` and `PolyRadialS` and gives `ModelPlaceBuilt2`. `polynomial_radial_holds` proves `PolyRadialS` with no hypothesis, as `polyRadialS_of` applied to `CP.radial_decomposition_holds` and `CP.word_polynomial_vector_holds`. The entry for `modelPlaceBuilt2_of_polyS` states `PolyRadialS`.

## In the Lean code

The theorem is in [CutJAPRSSnRep.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutJAPRSSnRep.lean#L6). `polynomial_radial_holds` is in [CutJAPRFinal.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutJAPRFinal.lean#L7), and `JfSmoothDS` in [CutRegFF.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutRegFF.lean#L28).

The size of this theorem is 1,916 and that of `modelPlaceBuilt2_of_polyS` is 1,283. So about 630 declarations lie below `polynomial_radial_holds` and are reached only through this theorem.
