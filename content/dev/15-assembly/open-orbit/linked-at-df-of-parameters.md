---
id: linked-at-df-of-parameters
title: The defect row holds at every choice of parameters
kind: theorem
decl: GlobalTheory.Fc.RL.DefSide.linkedAt_df_of_parameters
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.PointEvaluationSide
covers: 1185
status: drafted
drafted_by: writer@claude
---
This theorem proves the defect condition `RowDefectCondition`, the row form of the [definite side condition](/step/definite-side-condition-def/), at every choice of parameters. It is the defect field of the twelve open parameter statements of branch 3 of [the unitary hypotheses node](/proof/unitary-hypotheses/). Its only user is [`linkedAt_prmR_df_of_cuspRapidDecay`](/entry/linked-at-prm-r-df-of-cusp-rapid-decay/), which feeds [`weil_unitary_entries'`](/entry/weil-unitary-entries-prime/). Almost all of its size is in [`definiteSideCondition_of_nprimeDef_of_nuFull`](/entry/definite-side-condition-of-nprime-def-of-nu-full/) (1,104 of 1,185 declarations).

## Statement

**Theorem.** Let `hL` be a witness of `RecTExists` and let $p$ be parameters for `hL`. Then `LinkedAt p RowDefectCondition`.

`LinkedAt p r` applies the row statement $r$ to the bundle linkage of $p$, inside a statement `Lg1` that we have not unfolded. `RowDefectCondition` is the [row](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/ValidForConstructedPointClassesEventuallyWorking.lean#L268) whose property $H(\mathcal A, \sigma)$ is `EvWC`. In words, $H(\mathcal A, \sigma)$ says: the following holds in the [closed](/step/closed-def/) sense on the class $W_3(\mathcal A)$. For each family $F$ in $W_3(\mathcal A)$ and each $C_H$, there is $C_0 \ge 0$ such that for each $C \ge C_0$ there is $x_0$ with this property: for all $x > x_1$ with $x \ge x_0$ and all $i \in I_x$, the selected bundle $\sigma(F, x, i)$ satisfies `DefiniteSideCondition` with the reals $C$ and $C_H$.

$W_3(\mathcal A)$ is $\mathcal A$ cut down by several conditions on the family. The ones that the proof uses are `TuSize F` and the existence of $C_H'$ with `ChosenE F 3 CH'`.

## Proof

1. **The property of the row.** Take $E$ = `PointEvaluationSide` for every parameter $\kappa$. `pointEvaluationSide_of_isLinked` proves that each bundle that the linkage of $p$ attaches to a point has this property. Through `pointEvaluationSide_of_bWit`, it reads the fields of the bundle witness and calls `exists_symmetricColumnForms_stepZeroFiniteCharacter`, `kernelCompatibilities_standardKernelData_trueColumns` and `kerSizes_of_stdKer`. We have not opened these three lemmas.
2. **The constant.** For reals $C_Y, C_T$, let $c_0(C_Y, C_T)$ be the constant of `definiteSideCondition_of_nprimeDef_of_nuFull` at $C_Y$ and $\max(C_T, 0)$.
3. **Closedness.** `closed_Csz_ge_fn` gives, in the closed sense, $c_0(C_{YL}, C_{Tu}) \le C_{sz}$ for the constants $C_{YL}, C_{Tu}$ and $C_{sz}$ of the family. This works because the threshold for $C_{sz}$ may depend on the list `cOut`, which holds $C_{YL}$ and $C_{Tu}$. `Closed.imp` then reduces the claim to one large family $F$.
4. **The hypotheses, eventually.** The selection gives `PointEvaluationSide` at every $\sigma(F,x,i)$. Its first part, for $x \ge x_1 + 1$, is `RealPlaceSecondLayerConditions F`. With `TuSize F` and `ChosenE`, `full_rank` gives eventually `NuFull` and positive ranks. `famRowsSizes` gives eventually `HtRowsS` and the four size bounds, with $\max(C_{Tu}, 0)$. The fact `DelNat` that it needs comes from the field `DH` of the bundle.
5. Take $C_0 = 0$ and $x_0$ the maximum of the three thresholds. Step 2 then gives `DefiniteSideCondition`, with `NprimeDef` from the field `nprimeDef` of $F$ and with $c = C_{sz}$.

The rest is bookkeeping.

## In the Lean code

The theorem is at [PointEvaluationSide.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PointEvaluationSide.lean#L65). It calls:

- `LinkedAt.of_row` ([RowGood.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowGood.lean#L40)), with the trivial large base condition;
- `pointEvaluationSide_of_isLinked` (same file, line 45);
- [`definiteSideCondition_of_nprimeDef_of_nuFull`](/entry/definite-side-condition-of-nprime-def-of-nu-full/);
- `closed_Csz_ge_fn` ([AdmissibleFamilyOfThreshold.lean](lean:Formalism/SharpRestriction/Divisibility/ClosedSizeLink/AdmissibleFamilyOfThreshold.lean#L77));
- `full_rank` ([WeilUnitaryEntries.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/WeilUnitaryEntries.lean#L25)) and `famRowsSizes` ([FamRowsSizes.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/FamRowsSizes.lean#L13)).

Some details:

- The theorem has no hypothesis on $p$. So the defect row holds at all parameters. The caller `linkedAt_prmR_df_of_cuspRapidDecay` (line 85) takes four hypotheses named after published results and does not use them.
- The constant $C_0$ of `EvWC` is $0$. The definite side condition holds for every $C$ and $C_H$ once $c \ge c_0$.
- The constants $C_{YL}$ and $C_{Tu}$ are read from `cOut` by position, as entries 6 and 13 of the list.
- `PtE` in [WeilUnitaryEntries.lean](lean:Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/WeilUnitaryEntries.lean#L38) is a near copy of `PointEvaluationSide`, stated with `ColPins` in place of `ColumnCharactersCompatible`.
