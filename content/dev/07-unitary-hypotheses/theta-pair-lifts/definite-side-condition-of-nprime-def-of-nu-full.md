---
id: definite-side-condition-of-nprime-def-of-nu-full
title: The definite side condition at one bundle
kind: theorem
decl: GlobalTheory.Fc.RL.DefSide.definiteSideCondition_of_nprimeDef_of_nuFull
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.PointEvaluationSide
covers: 1104
status: drafted
drafted_by: writer@claude
---
This theorem proves the [definite side condition](/step/definite-side-condition-def/) at one bundle, from the property `PointEvaluationSide` of the bundle and from size bounds on the datum. Its only user is [`linkedAt_df_of_parameters`](/entry/linked-at-df-of-parameters/), which applies it at every selected bundle of a family to get the defect row. The work is in [`kernel_columns_from_ties_alt`](/entry/kernel-columns-from-ties-alt/), a restatement of [`rowsU_of_colPins_alt`](/entry/rows-u-of-col-pins-alt/).

## Statement

A bundle $b$ of type `BundleCondition D O c` has the fields described in the [step on the definite side condition](/step/definite-side-condition-def/). `PointEvaluationSide D O c b` is the conjunction of three facts.

1. `RealTied D` holds, and there are tied symmetric column forms $C$ with `ChiFin0` for each form $C_u$.
2. The columns of $b$ satisfy `ColumnCharactersCompatible`, a list of ten ties between the columns and the row side family of $b$.
3. There is a weight $W$ equal (as a heterogeneous equality) to the weight of the columns of $b$, with the kernel ties `KerTies` of the kernel datum of $b$. Also, for all reals $C_Y, C_T$, the five size bounds of the theorem below imply `KerSizes` with $C_Y, C_T$.

**Theorem.** Let $C_Y$ and $C_T \ge 0$ be reals. There is $C_0$ with this property. Let $D$ be a datum, $O$ an object over $D$ with size data $L$, $c$ a real, $b$ a bundle, and $C, C_H$ reals. Write $T_u$ for the number `(D.mem u).A.T`. Assume:

- `PointEvaluationSide D O c b`;
- `HtRowsS L CY`, and $X' \ge 8$, $x \ge 2$, $4a < T_u$ and $\log T_u \le C_T \, m \, L$ for all $u$, where $X', x, a, L$ are scale constants of $L$ and $m$ = `D.R.m`;
- `NprimeDef D L`, `D.NuFull`, and the module $N_u$ = `D.div.Nu u` has positive rank for all $u$;
- $C_0 \le c$.

Then `DefiniteSideCondition D O c b C CH`.

`NprimeDef` says that each lattice $N_u$ is the span over the ring of integers of `D.what₂.LL` of the products $a y$ with $a$ in an ideal $I_u$ and $y$ in the lattice `L.NuLat u`. `NuFull` says that each $N_u$ is finitely generated and spans its vector space.

## Proof

1. `kernel_columns_from_ties_alt` at $C_Y, C_T$ gives $C_0$.
2. Unfold `DefiniteSideCondition`. Take its side data, five reals, the numerical facts $H$, the submodules `NuC`, the division data $I$, and the hypothesis `HEq I b.P.I`. Let $P_k$ be the package `packageOfPrimitiveLinks` of the realisation of $b$.
3. The fields of `qRealOfBundle b` give: the subspace of $P_k$ is `b.P.Zs`, and the two indefinite data of $P_k$ are `b.P.S0` and `b.P.S1`. A tie of the columns of $b$ gives the face `b.P.Dc`. With `HEq I b.P.I`, the lemma `divTieDat3_heq` and the tie `b.C.wTie` show that the member $I.w_U(u)$ is $u$.
4. Apply step 1 at the kernel datum, the row side family and the columns of $b$. `KerSizes` comes from part 3 of `PointEvaluationSide` and the size bounds. The conclusion is `RowsU`, which is the claim.

## In the Lean code

The theorem is at [PointEvaluationSide.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PointEvaluationSide.lean#L49). It calls [`kernel_columns_from_ties_alt`](/entry/kernel-columns-from-ties-alt/) and `divTieDat3_heq` ([RecBridgeSel.lean](lean:Formalism/LocalToGlobal/Divisibility/RecBridgeSel.lean#L164)). The predicate `PointEvaluationSide` is defined in the same file, at line 27.

Some details:

- The hypothesis `DivTied3` of `DefiniteSideCondition` is introduced as `_` and never used. The submodules `NuC` are not used either. The lattice in the conclusion is `nuOf O.L u (I.eNu u)`, built from $L$, not `NuC`.
- Part 1 of `PointEvaluationSide` is dropped. It is used only by the caller.
- The reals $C$ and $C_H$ enter only through the package $P_k$. No bound on them is needed.
- The name names two of the ten hypotheses.
- The package term `packageOfPrimitiveLinks (qRealOfBundle b) hok1 hsep C CH hP hI` is written out five times in the proof.
