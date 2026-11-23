---
id: square-integrable-columns-of-witnesses
title: A column record for each weighted point with a pinned kernel
kind: theorem
decl: GlobalTheory.Mem.R3.SelC.square_integrable_columns_of_witnesses
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ExistsRowsKCColPins
covers: 396
status: drafted
drafted_by: writer@claude
---
This theorem gives a read datum $C_0$ at each weighted point, and then a column record `SquareIntegrableColumns` for each set of arguments that agree with $C_0$. It sits below [bundles at good points](/entry/ex-bl-is-linked-prm-r-alt/): step 1 of that proof, `zeta_uniform_of_extension'`, calls it through `ze_u_prm_of_extension_with_law`. The work is bookkeeping of equalities between data. It is part of branch 1 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/).

## Statement

Let $q$ be a weighted point `WPt 𝒮 K`, and let $t$ be a tied kernel for the extra data of $q$. Assume `KPin q t`, and assume that the rows of $q$ have a witness (`Nonempty (RXs …)`). Then there are a face $D_c$, data $S_{p,0}$ and $Z_{sc,0}$, and a read datum $C_0$ of type `ReadC`, with this property. For each tied datum $T$ with kernel $t$, and each pair of arguments $a$, $x$ with $a.x = x$, $a.D_c = D_c$, $x.C.w_U = C_0.w_U$ and $x.C.e_\nu = C_0.e_\nu$, there is a record $C$ of type `SquareIntegrableColumns` $T$ over the row family of $x$, with:

- the face and the `SPer` data of $C$ equal to those of $x$;
- the weights of $C$ equal to the weights of $q$, and its $X_g$ equal to that of the rows of $q$;
- `ColumnCharactersCompatible C`: the group, the level and the point character of the family agree with those that $C$ builds.

The equalities are `HEq`.

## Proof

1. `exists_readC_wU_eq_id` builds $C_0$ with $w_U = \mathrm{id}$. It uses a dummy `SPer`, with space $\mathbb C$, zero maps and the zero submodule.
2. For given $T$, $a$, $x$, the proof substitutes $T.\mathrm{ker} = t$ and $a.x = x$, and calls `exists_square_integrable_columns_of_data`. That lemma reads the equalities of $a$ with `args_pinned_heq_zsOf_mem_eq`, and gets the record from `exists_rowsKC_colPins_alt`.

## In the Lean code

The theorem is at [ExistsRowsKCColPins.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsRowsKCColPins.lean#L213). The record is at [SquareIntegrableColumnsTied.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SquareIntegrableColumnsTied.lean#L28), and `ColumnCharactersCompatible` at [DIVColPins.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/DIVColPins.lean#L26). A second name with the same statement, `exists_square_integrable_columns_of_heq_data`, is at [ExistsRowsKCColPinsStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsRowsKCColPinsStatement.lean#L17).

Some points:

- The hypothesis $x.C.e_\nu = C_0.e_\nu$ is not used. The proof drops it with `_`.
- Of `KPin q t`, only the field `std` is used.
- The record has fields of data and of equalities only, such as `colTie`, `kerTie` and `famEq`. No field states that a function is square integrable.
- `ze_u_prm_of_extension_with_law` keeps only $C_0$ and drops the rest with `-`.
