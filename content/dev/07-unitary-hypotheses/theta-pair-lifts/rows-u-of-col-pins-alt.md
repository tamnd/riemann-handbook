---
id: rows-u-of-col-pins-alt
title: The column rows from the kernel ties
kind: theorem
decl: GlobalTheory.ColRows.rowsU_of_colPins_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.RowsUOfColPins
covers: 1102
status: drafted
drafted_by: writer@claude
---
This theorem proves the column row statement `RowsU` at one word, from the kernel ties and the kernel size bounds of the columns. `RowsU` is the conclusion of the [definite side condition](/step/definite-side-condition-def/). It is restated without change as [`kernel_columns_from_ties_alt`](/entry/kernel-columns-from-ties-alt/), and that copy is used by [`definiteSideCondition_of_nprimeDef_of_nuFull`](/entry/definite-side-condition-of-nprime-def-of-nu-full/). Most of the size is in [`memberRows_of_kernelDatum_sizes`](/entry/member-rows-of-kernel-datum-sizes/) (1,055 of 1,102 declarations).

## Statement

Let $D$ be a datum of type `D7` and $K_D$ = `D.what₂.LL`, a number field that we assume to be totally complex. Let $L$ be size data for $D$, `ex` an extra record, $T$ tied kernel data, $P$ a row side family and $K$ square integrable columns for $T$ and $P$. Let $W$ be column weights and $\Delta, h_0$ natural numbers. Write $N_u$ for the module `D.div.Nu u`.

**Theorem.** Let $C_Y$ and $C_T \ge 0$ be reals. There is $C_0$ with this property. Assume:

1. `ColumnCharactersCompatible K`, and the weight of $K$ is $W$;
2. `KerTies T.ker W Δ h0` and `KerSizes T.ker W Δ h0 CY CT`;
3. `NprimeDef D L`, `D.NuFull`, and each $N_u$ has positive rank.

Take an indefinite package $P_k$ over the face of $K$ with subspace $Z_s(P_k) = Z_s(P)$, a word $u$, reals $\lambda_0, c_0, c_e, C_h, S_w, C_1$ with the numerical facts $H$ at the letter of $u$, a member $w$ of the face with $w = u$ (as a heterogeneous equality), and a $K_D$-linear isomorphism $e \colon K_D^{a(w)} \to V_u$, where $V_u$ is the vector space of $N_u$. Here $a(w)$ is the size that the face gives to $w$. If $C_0 \le C_h$, then:

- there are a column chain at $w$ and a chain tie with `FirstCols`;
- there is, at each infinite place $v$ of $K_D$, an invertible matrix $X_0(v)$ with $(X_0(v)^{-1})^{*} X_0(v)^{-1} = H_V$ at $v$, where $H_V$ is the Hermitian matrix of the side of $P$ at $\mu_0$;
- there are height numbers `hn` for the record of numbers of $u$, with the operator norm bound $\lVert \cdot \rVert_v^2 \le \exp(h_{Pn})$ for the last matrix of the chain;
- there are column bound data whose logarithms are bounded by sums of the sizes of `hn`;
- the matrices $X_c(w, v)$ of the face are invertible, and $a(w) > 0$;
- the pull back `nuOf L u e` of the lattice `L.NuLat u` along $e$ is a lattice.

## Proof

1. `memberRows_of_kernelDatum_sizes` at $C_Y, C_T$ gives $C_0$.
2. `BlockDat.HV_pos` shows that $H_V$ is positive definite at each infinite place.
3. `nuLat_comap_isLattice`, with `NprimeDef` and `NuFull`, shows that `nuOf L u e` is a lattice.
4. $a(w) > 0$: the rank of $N_u$ is positive, and by `NuFull` it is $\dim V_u = a(w)$.
5. `frames_tilde_gamma_values_alt`, from `ColumnCharactersCompatible`, gives the bound of the inner product by the square of the norm for every frame $X_0$, once $\mu(\mu_0) = 1$.
6. The proof takes $K$, $T$, the kernel datum and the column record apart. The fourteen equalities of the kernel tie of $K$ identify the column record with the kernel datum. $\mu(\mu_0) = 1$ follows from `KerTies.mu0` and a tie of $P$.
7. Step 1, at the rebuilt kernel datum, gives the column rows and the invertibility of $X_c$. Steps 3 and 4 give the last two items.

The rest is bookkeeping.

## In the Lean code

The theorem is at [RowsUOfColPins.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowsUOfColPins.lean#L17). It calls:

- [`memberRows_of_kernelDatum_sizes`](/entry/member-rows-of-kernel-datum-sizes/) ([MemberRowsOfKernelDatumSizesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/MemberRowsOfKernelDatumSizesStatement.lean#L8)), whose proof calls [`rowsBody_of_kerTies`](/entry/rows-body-of-ker-ties/);
- `frames_tilde_gamma_values_alt` ([EvIpAtLeNormAtSqStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EvIpAtLeNormAtSqStatement.lean#L13));
- `nuLat_comap_isLattice` ([IsLatticeOfEqSpanFracSmul.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsLatticeOfEqSpanFracSmul.lean#L52));
- `BlockDat.HV_pos` ([RowLatLemmas.lean](lean:Formalism/LocalToGlobal/Divisibility/RowLatLemmas.lean#L38)).

Some details:

- The conclusion is the body of `RowsU` ([PtKOfReal.lean](lean:Formalism/LocalToGlobal/PtKOfReal.lean#L141)) with `Nu := nuOf L u e`, written out in full, not the name `RowsU`.
- The name says "col pins", but the hypothesis is `ColumnCharactersCompatible`. A separate structure `ColPins`, over `SquareIntegrableColumnsCompatible`, is in [ColPins.lean](lean:Formalism/LocalToGlobal/Divisibility/ColPins.lean#L41). The field `colPins` of the bundle witness also has the type `ColumnCharactersCompatible`.
- The scale, face and reals of the package are arbitrary. Only $Z_s(P_k) = Z_s(P)$ is used.
