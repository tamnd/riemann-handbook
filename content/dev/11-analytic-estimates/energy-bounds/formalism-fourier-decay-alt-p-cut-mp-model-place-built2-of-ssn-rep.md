---
id: formalism-fourier-decay-alt-p-cut-mp-model-place-built2-of-ssn-rep
title: Model places from the fibre maps, with the rotation input supplied
kind: theorem
decl: Formalism.FourierDecayAlt.P.CutMP.modelPlaceBuilt2_of_SSnRep
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.GaugeConstructionHolds
covers: 997
status: drafted
drafted_by: writer@claude
---
This theorem is a relay. It proves `ModelPlaceBuilt2` from the hypotheses `JfSmoothDS` and `SSnRep`, and it removes one hypothesis of the theorem below it: the rotation invariance `GTRRotK`. Its only user is [model places from the radial polynomial relation](/entry/model-place-built2-of-poly-s/), which proves `SSnRep`. That entry states `SSnRep` in words; [each place of a built setting is a model place](/entry/model-place-built-holds/) states `ModelPlaceBuilt2`.

## Statement

**Theorem.** If `JfSmoothDS` and `SSnRep` hold, then `ModelPlaceBuilt2` holds.

## Proof

The proof is one line:

```
modelPlaceBuilt2_of_rotK hJ Gauge.GC.rotation_K_invariance_holds h
```

[`modelPlaceBuilt2_of_rotK`](/entry/model-place-built2-of-rot-k/) needs `GTRRotK` in addition to the two hypotheses. `rotation_K_invariance_holds` proves `GTRRotK` with no hypothesis, from six lemmas on the rotation $\zeta \mapsto e^{i\varphi}\zeta$ (a matrix form, a finiteness fact, a centre condition, a section fact, an ODE fact and a Wirtinger derivative fact). The entry [the gauge transfer from rotation invariance](/entry/gen-transfer-of-rot-k/) states `GTRRotK`. The content is in the theorems below: [`modelPlaceBuilt2_of_hat`](/entry/model-place-built2-of-hat/) and [`jABddOpQQ_of_ssnRep`](/entry/j-abdd-op-qq-of-ssn-rep/).

## In the Lean code

The theorem is in [GaugeConstructionHolds.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/GaugeConstructionHolds.lean#L12). `rotation_K_invariance_holds` is in [CutGCoreGTRRotK.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutGCoreGTRRotK.lean#L10).

The file name refers to the other theorem in it, `gauge_construction_holds : GCore` (line 6), which is `gCore_of_rotK rotation_K_invariance_holds`. This theorem does not use it. The chain below gets `GCore` again from `GenTransfer` through `gCore_of_genTransfer`.

The size is 997, and that of `modelPlaceBuilt2_of_rotK` is 996. So the subtree of `rotation_K_invariance_holds` is not counted here: it is shared with `gauge_construction_holds`.
