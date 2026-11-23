---
id: cls-pin-d-of-fam-col-of-true-w
title: Class data from the column condition
kind: theorem
decl: GlobalTheory.AdForm.clsPinD_of_famCol_of_trueW
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ClsPinDOfFamCol
covers: 531
status: drafted
drafted_by: writer@claude
---
For a family character $f$ with the column condition, this theorem builds one real datum $\rho$ and, for each index $t$, a kernel class datum and a tail class datum over $\rho$. Together these are `ClsPinD f.t`. Through the restatement [`cls_pin_d_of_true_family`](/entry/cls-pin-d-of-true-family/), [the column data of a true geometric family](/entry/laws-links-of-geo-rows-cols-alt/) uses it in step 6, where three see-saw lemmas turn the class data into the laws `KerX`, `PerX` and `RdX`.

## Statement

Let $W$ be a real package over $D$ = `I.rec7 l Z`, $u$ a word, and $f$ a family character (`FamilyCharacter`: a geometry $f.g$, a linear map $f.j$, a row choice and a column choice). Each $t$ gives a tuple $f.t(t)$, whose tail coefficients are read from $f.j$ (`tailCoefficient`).

`ClsPinD f.t` says: there is a real datum $\rho$ (`RealD`: ranks $N_j$, frames, dominant weights $\lambda_j$, scalars, a function $J$ on the top space and a lowering map) with $\rho$.`Is`, and for each $t$ a kernel class datum (`ClsK`: subgroups $U_j$, characters $\chi_j$, representatives and values) and a tail class datum (`ClsT`: a subgroup $U$ of the top group, representatives and linear forms $\ell$), each with its `Is`. The field `tail` of `ClsT.Is` says that a sum over the classes of the $\ell$ applied to lowered values equals $c_P$ times the tail of $f.t(t)$.

**Theorem.** Assume `ValidRealPackage W`, `TwStdAlt W`, `LeadingReadAt W u f.j f.g.bT`, `f.RowOK` and `FamilyColumnCondition f`. Then `ClsPinD f.t`.

`FamilyColumnCondition f` gives $c_0$ with `PinX` for the lattices and vacua of $f.g$, and for each $t$ a twist datum on which the column is pinned (`PinChL`) and a top datum (`PinTopL`). `TwStdAlt W` says that the twisted columns of $W$ are the standard ones `I.tw l l0 Z`.

## Proof

1. `exists_nonzero_jetScale_trueColumns` gives jet scales $s$ (`JetS`), and `exists_translates_of_values_frames` gives $J$ with `JOf R f.j J`, where $R$ = `pk_z W`.
2. Put $\rho$ = `realOf u R f.g s J`. `trueColumns_realData_spec` proves $\rho$.`Is`. It uses `PinX`, the first part of the leading reading, and the embedding condition of `PinTopL` at the base twist $\mu_0$.
3. For each $t$, [`kernelPart_laws_of_columnPins`](/entry/kernel-part-laws-of-column-pins/) proves that the kernel class datum `clsKL` built from `PinChL` is good.
4. For the tail datum, the proof first finds, for the tuple $\mu$ of $t$, classes $K$ at a set of bad primes, an isomorphism $e_W$ and, for each $\psi$ and $F$, a reading $G'$ with $\mathrm{tail}(\psi, F) = \tilde P(\psi, G')$. For $\mu = \mu_0$ the forms come from the columns of $W$ and the field `std` of the valid package. For $\mu \neq \mu_0$ they come from the twisted columns, which `TwStdAlt` identifies with the standard ones. In both cases `exists_rowForm_reading_levelForm_lastSpace` gives $G'$, and unfolding `tailCoefficient` gives the equality.
5. `exists_lastPeriod_classData_of_lastStep` turns this into a good tail class datum.

## In the Lean code

The theorem is at [ClsPinDOfFamCol.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ClsPinDOfFamCol.lean#L22). `ClsPinD`, `RealD`, `ClsK` and `ClsT` are in [OnFramesRdApply.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/OnFramesRdApply.lean#L152), `FamilyColumnCondition` and `TwStdAlt` in [FamCol.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FamCol.lean#L23), and `ValidRealPackage`, `RowOK` in [TrueW.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TrueW.lean#L38). The lemmas it calls:

- `exists_nonzero_jetScale_trueColumns`, `exists_translates_of_values_frames`, `trueColumns_realData_spec`;
- `kernelPart_laws_of_columnPins`;
- `exists_rowForm_reading_levelForm_lastSpace`, `exists_lastPeriod_classData_of_lastStep`.

We have not unfolded `PinX`, `PinChL`, `PinTopL`, `JetS`, `JOf` or `realOf`. Of `RowOK` the proof uses only the field `x` (the lattices are good); its other four fields, `meas`, `last`, `row` and `same`, are not used. Of `ValidRealPackage` it uses only `ok`, `pins` and `std`. The case $\mu \neq \mu_0$ needs `cases ex` and two substitutions to match the twisted columns of $W$ with the standard ones. The "trueW" of the name is the file `TrueW.lean`, where `ValidRealPackage` is defined.
