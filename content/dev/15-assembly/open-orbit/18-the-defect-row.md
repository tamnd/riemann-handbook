---
title: The defect row
decls:
  - GlobalTheory.Fc.RL.linkedAt_prmR_df_of_cuspRapidDecay
  - GlobalTheory.T.weil_unitary_entries'
  - GlobalTheory.Fc.RL.DefSide.linkedAt_df_of_parameters
  - GlobalTheory.Fc.RL.DefSide.definiteSideCondition_of_nprimeDef_of_nuFull
  - GlobalTheory.ColRows.rowsU_of_colPins_alt
  - GlobalTheory.T.kernel_columns_from_ties_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The defect row

This section proves [the Theorem on the defect row](/entry/weil-unitary-entries-prime/), step 10 of [the Theorem on the open parameter statements](/entry/open-orbit-of-unramified-exponents-alt/). The defect row is the row form of [the definite side condition](/step/definite-side-condition-def/). It asks that, eventually and for all large points, each bundle condition of a selection satisfies the definite side condition once its constant $c$ is large. We prove it in three steps. First, a condition on one bundle condition, the point evaluation side, holds at every linked bundle, because it is carried by the bundle witness. Second, the point evaluation side and a few numerical conditions give the definite side condition, through a result on kernel columns. Third, the numerical conditions hold eventually in the closed families, and the row follows.

We keep the notation of [the section on rows](/entry/fam-mi-star-row-alt-alt/) and of [the section on the open parameter statements](/entry/open-orbit-of-unramified-exponents-alt/). $p$ is a parameter set, $D$ a datum, $O$ an object over $D$ with scale $L$, $c$ a real and $b$ a bundle condition for $(D, O, c)$. The scale has the points $x$ and $X'$, the constant $a$ and the logarithm $L$; for a word $u$, $T_u$ is its twist number. The bundle condition carries the tied data with a kernel datum, a row side family $P$ and a column side with weights $W$.

**Definition 4.18.1 (Point evaluation side).** A bundle condition $b$ satisfies the *point evaluation side* if:

1. the real part of $D$ is tied, and there are symmetric tied column forms whose characters at step zero are finite;
2. the column characters of the column side are compatible, and there are weights $W$ of the kernel, equal to the weights of the column side, with the kernel ties for $W$;
3. for all $C_Y, C_T$: if the heights of the rows of $L$ are bounded by $C_Y$, $8 \leq X'$, $2 \leq x$, $4a < T_u$ for all $u$, and

   $$\log T_u \leq C_T \, m \, L \quad \text{for all } u,$$

   then the kernel datum has sizes for $(W, C_Y, C_T)$.

**Definition 4.18.2 (Kernel rows).** For a member $w$ of the column face, with lattice $N$ of $\nu$-vectors, the *kernel rows* at $w$ say: there are a column chain at $w$ with a chain tie and first columns; matrices $X_0(v)$ at the infinite places $v$ with unit determinant and

$$(X_0(v)^{-1})^* \, X_0(v)^{-1} = H_V(\mu_0)^v,$$

the hermitian matrix of the side at the base index; height numbers that bound the operator norm of the last column map in the dual frame of $X_0$; and square data whose logarithms are bounded by sums of the height sizes. In addition the column matrices at $w$ are invertible, the face has positive rank $a(w) > 0$, and $N$ is a lattice.

The definite side condition at $(C, C_H)$ asks: for the primitive link data, separated types, the covolume and pass-in conditions at $(C, C_H)$, the numerical facts at each word, and each three sided division datum $I$ that is tied and equal to the division datum of $b$, the kernel rows hold at each word $u$, at the member $I.w_U(u)$ with the $\nu$-lattice of $u$.

**Theorem 4.18.3 (Kernel columns from ties).** Let $C_Y$ and $C_T \geq 0$ be reals. There is $C_0$ such that for every datum $D$, tied data with a kernel datum, row side family $P$, square integrable columns with compatible column characters, weights $W$ with the kernel ties and the kernel sizes for $(W, C_Y, C_T)$, a $\nu$-datum that is full and of positive rank at each word, and every package, word $u$ and numerical data with constant $c \geq C_0$: the kernel rows hold at the member of $u$.

Lean: `GlobalTheory.ColRows.rowsU_of_colPins_alt` (also `GlobalTheory.T.kernel_columns_from_ties_alt`, a second name).

*Proof.* We feed a result on member rows with the facts it needs.

1. [The Theorem on member rows of kernel data](/entry/member-rows-of-kernel-datum-sizes/) gives $C_0$, depending only on $C_Y$ and $C_T$.
2. The base tuple of $P$ at $\mu_0$ is the base tuple of $D$.
3. The hermitian matrix $H_V(\mu_0)$ is positive definite at every infinite place, by the conjugation and irreducibility parts of the square integrable columns.
4. Since the $\nu$-datum is full at $u$, the $\nu$-lattice of $u$ is a lattice. Since its rank is positive, $a(w) > 0$ for the member $w$ of $u$.
5. A result of another chapter on the frames of $\tilde\Gamma$ gives the values of the frames from the compatibility of the column characters. The kernel ties give that the tuple at $\mu_0$ has $k$-value $1$, so the values apply.
6. The kernel ties unfold into the fields of a tied kernel datum. With steps 2, 3 and 5, the Theorem on member rows gives all clauses of the kernel rows except the last two. Step 4 gives the last two. $\square$

**Theorem 4.18.4 (Definite side from the point evaluation side).** Let $C_Y$ and $C_T \geq 0$ be reals. There is $C_0$ such that for all $D, O, c, b$ and $C, C_H$: if $b$ satisfies the point evaluation side, the heights of the rows of $L$ are bounded by $C_Y$, $8 \leq X'$, $2 \leq x$, $4a < T_u$ and $\log T_u \leq C_T m L$ for all $u$, the $N'$ definition holds, the $\nu$-datum of $D$ is full and of positive rank at each word, and $C_0 \leq c$, then $b$ satisfies the definite side condition at $(C, C_H)$.

Lean: `GlobalTheory.Fc.RL.DefSide.definiteSideCondition_of_nprimeDef_of_nuFull`.

*Proof.* Take $C_0$ from the Theorem on kernel columns from ties. Fix the data of the definite side condition: the primitive link data, the numerical facts, a tied division datum $I$ with $I = b.P.I$ and a word $u$.

1. The package built from the primitive links has the same scale data and the same two indefinite data as $b$, and the same column face.
2. A result of another chapter on three sided division data then gives that the member $I.w_U(u)$ is the member of $u$.
3. Part 2 of the point evaluation side gives the compatible column characters, the weights and the kernel ties. Part 3, at $(C_Y, C_T)$ and with the numerical hypotheses, gives the kernel sizes.
4. The Theorem on kernel columns from ties, with step 2, gives the kernel rows at $u$. $\square$

**Theorem 4.18.5 (Defect row at a parameter set).** Every parameter set $p$ is linked at the defect row.

Lean: `GlobalTheory.Fc.RL.DefSide.linkedAt_df_of_parameters`.

*Proof.* A row in the good bundles of $p$ gives a linked row. So we show the row of the definite side condition, with $E$ the point evaluation side.

1. At every linked bundle the point evaluation side holds. The linkage gives a witness point $q$, a bundle condition $b'$ at $q$ with a bundle witness, and an equality with $b$. At $q$, part 1 is the real tie of $q$ with the symmetric forms of the true columns; part 2 is the column pin of the witness, the weights of the witness and the standard kernel compatibilities of the true columns; part 3 is the size result for standard kernels. We transport along the equality.
2. Let $c_0(C_Y, C_T)$ be the constant of the previous theorem at $(C_Y, \max(C_T, 0))$. A result of another chapter on closed families says that, for a function of the constant list, eventually the size constant $C_{sz}$ of each closed family is at least that function. Apply it to $c_0(C_{YL}, C_{Tu})$.
3. Fix a family $F$ of the closed family with $C_{sz} \geq c_0(C_{YL}, C_{Tu})$. Its selections satisfy the real place second layer conditions from some point on. Two results of another chapter give, for all large $x$, that the $\nu$-datum is full and of positive rank at each word, and the bounds on heights, points, the constant $a$ and the twist numbers.
4. For $x$ beyond the three thresholds, the previous theorem applies to each selected bundle condition, with the $N'$ definition of $F$. This gives the definite side condition, with threshold $0$ on $c$. $\square$

**Theorem 4.18.6 (Defect row).** Assume the Weil representation of a unitary pair, the existence of discrete series, the finiteness theorem of Harish-Chandra and the rapid decay of cusp forms. Then for each recursion datum $h_L$, each extension choice $N$, each $S$-extension $S$ and each geometry $\Gamma$, the parameter set of $(N, S, \Gamma)$ is linked at the defect row.

Lean: `GlobalTheory.Fc.RL.linkedAt_prmR_df_of_cuspRapidDecay` (also `GlobalTheory.T.weil_unitary_entries'`, a second name).

*Proof.* This is the previous theorem at the parameter set of $(N, S, \Gamma)$. $\square$

The four published statements are not used in the proof. The defect row holds at every parameter set by the bundle witnesses and the eventual sizes of the closed families alone.

**Remark 4.18.7 (Formalization).** The four theorems are at [PointEvaluationSide.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PointEvaluationSide.lean#L85) (the defect row at line 85, the row at a parameter set at line 65, the definite side at line 49) and [RowsUOfColPins.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowsUOfColPins.lean#L17). The second names are relays at [PointEvaluationSideStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PointEvaluationSideStatement.lean#L14) and [RowsUOfColPinsStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowsUOfColPinsStatement.lean#L13). The point evaluation side is `PointEvaluationSide` at line 27 of PointEvaluationSide.lean, with `pointEvaluationSide_of_bWit` (line 34) and `pointEvaluationSide_of_isLinked` (line 45) for step 1 of the third proof. The definite side condition is `DefiniteSideCondition` in [DefiniteSideCondition.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/DefiniteSideCondition.lean#L25), the defect row is `RowDefectCondition` and linkage is `LinkedAt` in [RowGood.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowGood.lean#L36), and the kernel rows are `RowsU` in Formalism/LocalToGlobal/PtKOfReal.lean at line 141. Some details:

- The defect row theorem binds its four published inputs as `_` at line 88 and passes nothing to `linkedAt_df_of_parameters`. The name `weil_unitary_entries'` speaks of the Weil representation, which is not used.
- In the definite side proof, part 1 of the point evaluation side is dropped with `-` at line 55, and the tie hypothesis `DivTied3` is bound as `_` at line 56. The package term `packageOfPrimitiveLinks` is written out five times in that proof.
- At line 69 the constants are read off the constant list by position, `l.getD 6 0` and `l.getD 13 0`, standing for $C_{YL}$ and $C_{Tu}$.
- At line 77 the threshold on $c$ is $0$; the real threshold is carried by $C_{sz}$.
- The name `rowsU_of_colPins_alt` speaks of column pins, but the hypothesis it uses is the compatibility of column characters. In its proof, line 34 clears hypotheses, and lines 35 to 72 unfold the kernel datum and the kernel ties by about fourteen substitutions.
- `PtE` in WeilUnitaryEntries.lean at line 38 is a near copy of `PointEvaluationSide`. The results of step 3 of the third proof are `full_rank` (WeilUnitaryEntries.lean, line 25) and `famRowsSizes` (FamRowsSizes.lean, line 13); the closed family result is `closed_Csz_ge_fn` in Formalism/SharpRestriction/Divisibility/ClosedSizeLink/AdmissibleFamilyOfThreshold.lean at line 77, and step 2 of the second proof is `divTieDat3_heq` in Formalism/LocalToGlobal/Divisibility/RecBridgeSel.lean at line 164.
- We have not opened `memberRows_of_kernelDatum_sizes`, `frames_tilde_gamma_values_alt`, `kernelCompatibilities_standardKernelData_trueColumns` and `kerSizes_of_stdKer`, nor unfolded `KerTies`, `KerSizes`, `NumFacts` and the covolume conditions.
