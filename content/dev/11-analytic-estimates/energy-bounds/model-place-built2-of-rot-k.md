---
id: model-place-built2-of-rot-k
title: Model places from rotation invariance and the fibre maps
kind: theorem
decl: Formalism.FourierDecayAlt.P.CutMP.modelPlaceBuilt2_of_rotK
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.CutGCoreDone
covers: 996
status: drafted
drafted_by: writer@claude
---
This theorem is a relay. It proves `ModelPlaceBuilt2` from three hypotheses, `JfSmoothDS`, `GTRRotK` and `SSnRep`. It turns `GTRRotK` into the gauge transfer `GenTransfer` and passes the rest down. Its only user is [the same statement without `GTRRotK`](/entry/formalism-fourier-decay-alt-p-cut-mp-model-place-built2-of-ssn-rep/), which proves `GTRRotK`.

## Statement

**Theorem.** If `JfSmoothDS`, `GTRRotK` and `SSnRep` hold, then `ModelPlaceBuilt2` holds.

`ModelPlaceBuilt2` is stated in [each place of a built setting is a model place](/entry/model-place-built-holds/), `JfSmoothDS` in [model places from the chart equations](/entry/model-place-built2-of-chart-eqs/), `SSnRep` in [model places from the radial polynomial relation](/entry/model-place-built2-of-poly-s/) and `GTRRotK` in [the gauge transfer from rotation invariance](/entry/gen-transfer-of-rot-k/).

## Proof

The proof is one line:

```
modelPlaceBuilt2_of_ssnRep hJ (Gauge.GC.genTransfer_of_rotK hR) h
```

1. [`genTransfer_of_rotK`](/entry/gen-transfer-of-rot-k/) proves `GenTransfer` from `GTRRotK`. `GenTransfer` gives, at each place, a frame $e_\rho(\zeta)$ of the fibres such that the transfer to the model side intertwines the operators of the level data ($\zeta^{\pm 1}$, $\bar\zeta^{\pm 1}$, $G^{\pm 1}$, $\nabla$, $\nabla^*$, $\kappa(f)$ and the shifts $S_l$, $S_l^*$) with their model versions.
2. [`modelPlaceBuilt2_of_ssnRep`](/entry/formalism-fourier-decay-alt-p-cut-mp-model-place-built2-of-ssn-rep-2/) takes `JfSmoothDS`, `GenTransfer` and `SSnRep`.

There is nothing else.

## In the Lean code

The theorem is in [CutGCoreDone.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutGCoreDone.lean#L43). The same file proves `genTransfer_of_rotK` (line 34) and `gCore_of_rotK` (line 37).

`genTransfer_of_rotK` has size 1,041, more than this theorem. It has a second user, so its subtree is not in the size of this theorem. The size 996 is one more than that of `modelPlaceBuilt2_of_ssnRep`.
