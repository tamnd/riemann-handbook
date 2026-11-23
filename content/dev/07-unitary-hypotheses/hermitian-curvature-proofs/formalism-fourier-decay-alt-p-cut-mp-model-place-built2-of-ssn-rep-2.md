---
id: formalism-fourier-decay-alt-p-cut-mp-model-place-built2-of-ssn-rep-2
title: Model places from the gauge transfer and the fibre maps
kind: theorem
decl: Formalism.FourierDecayAlt.P.CutMP.modelPlaceBuilt2_of_ssnRep
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.CutJABddDone
covers: 995
status: drafted
drafted_by: writer@claude
---
This theorem is a relay. It proves `ModelPlaceBuilt2` from `JfSmoothDS`, `GenTransfer` and `SSnRep`. It uses `SSnRep` only to get the bounded operator hypothesis `JABddOpQQ`. Its only user is [model places from rotation invariance and the fibre maps](/entry/model-place-built2-of-rot-k/), which gets `GenTransfer` from the rotation invariance.

## Statement

**Theorem.** If `JfSmoothDS`, `GenTransfer` and `SSnRep` hold, then `ModelPlaceBuilt2` holds.

The entry for [`modelPlaceBuilt2_of_rotK`](/entry/model-place-built2-of-rot-k/) says where each of these statements is given in words. The name differs from `modelPlaceBuilt2_of_SSnRep`, the theorem two levels up, only in the case of one letter.

## Proof

The proof is one line:

```
modelPlaceBuilt2_of_bdd hJ hG (JA.jABddOpQQ_of_ssnRep h)
```

1. [`jABddOpQQ_of_ssnRep`](/entry/j-abdd-op-qq-of-ssn-rep/) proves `JABddOpQQ` from `SSnRep`: each element of the bounded set of the model algebra is realized on the group side by an operator of order zero with polynomially bounded coefficients.
2. [`modelPlaceBuilt2_of_bdd`](/entry/model-place-built2-of-bdd/) takes `JfSmoothDS`, `GenTransfer` and `JABddOpQQ`.

There is nothing else. The size 995 is $1 + 570 + 372 + 52$: the last 52 declarations lie below this theorem but below neither branch alone.

## In the Lean code

The theorem is in [CutJABddDone.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CutJABddDone.lean#L26). The same file proves `jABddOpQQ_of_ssnRep` (line 17) and `kappa_quadratic_bound_holds` (line 14). `modelPlaceBuilt2_of_bdd` is in [ModelPlaceBuilt2OfBdd.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/ModelPlaceBuilt2OfBdd.lean#L6).

The two names `modelPlaceBuilt2_of_SSnRep` and `modelPlaceBuilt2_of_ssnRep` are in the same namespace and differ only in case. They take different hypotheses: the first has no `GenTransfer`.
