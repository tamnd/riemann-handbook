---
id: rows-body-col-face
title: The body of the column rows at one member
kind: theorem
decl: GlobalTheory.ColRowsTopS.rowsBody_colFace
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ColumnsMemberRowsOfLogLevelLe
covers: 1040
status: drafted
drafted_by: writer@claude
---
This theorem proves `RowsBody`, the main part of the row statement `RowsU` of the [definite side condition](/step/definite-side-condition-def/). Through [a relay](/entry/columns-member-rows-of-log-level-le/) and [a specialization](/entry/rows-body-of-ker-ties/), it goes to [the rows from the column pins](/entry/rows-u-of-col-pins-alt/).

## Statement

Let $K$ be the field `X.K` of a field record $X$ with `X.Ok`, with $K$ totally complex. Let $v$ run over the infinite places of $K$. Let $m$ be the rank `N.R.m` and $n = m - 2$.

- A definite side gives, for each tuple $t$ (with a base tuple $\mu_0$), a dimension $n_V(t)$ and a matrix $H_V(t)$ over $K$.
- The column face `colFace` gives, for each member $x$, a dimension $a(x)$, a frame matrix $X_c(x)_v$ for each $v$ (from the Hermitian lattice `MramH`), and for each $t$ a pairing $P(x,t) \colon K^{a(x)} \to (K^{n_V(t)})^\vee$ (the column period `colPer`).
- The kernel chain $Q$ (`memQ`, built by `KerChain.ofCol` at $\mu_0$ and $x$) has Hermitian families $F_0, \dots, F_n$ with step maps $F_j \to F_{j+1}$, a last Hermitian space $S_1$, and a map $\mathrm{col} \colon F_0 \to S_1$.
- $f_0 = $ `colsIn` is a linear map $K^{a(x)} \to F_0$.

`RowsBody` says that there exist:

1. a chain of dimensions $c_0 = a(x), \dots, c_{n+1}$, invertible frames $X_i$ at each $v$ with $X_0 = X_c(x)$, matrices $K_j$ from $K^{c_j}$ to $K^{c_{j+1}}$, and a last map $P_L$ with $P(x,\mu_0)(\varphi) = P_L(K_n \cdots K_0 \varphi)$;
2. a tie of this chain to $Q$: maps from $K^{c_i}$ to $F_i$ and to $S_1$ that are isometries for the frames $X_i$, that turn $K_j$ into the step map for $j < n$ and $K_n$ into the map to $S_1$, and whose first map is $f_0$;
3. frames $Y_v$ with $(Y_v^{-1})^* Y_v^{-1} = H_V(\mu_0)$;
4. height numbers $h$ for $R$ such that the squared operator norm of $P_L$ at $v$, from $X_{n+1}$ to the dual frame of $Y$, is at most $e^{h_P}$;
5. column bound data whose log sizes at step $j$ are at most $\sum_{l \mapsto j} h_{\mathrm{sz}}(l, v)$.

**Theorem.** For all reals $C_Y$ and $C_T \ge 0$ there is $C_0$ with this property. Take a member $x$ with word $u$ and level prime $T$, and assume: the four ties `HostTie`, `WeightTie`, `CharTie`, `AnalyticTie`; $\mu(\mu_0) = 1$, the constant at $\mu_0$ is sharp, and `FieldOfDefinition`; the size conditions `Sizes` and `SizeRowsS` $C_Y$; $\log T \le C_T\, m\, L$; `Reads` ($R$ records the numbers of $N$ and $\log T$); $C_0 \le R.C_h$; $H_V(\mu_0)$ is positive definite at each $v$; and for each frame $Y$ as in 3, $\operatorname{Re}\langle \mathrm{ev}\,F, \mathrm{ev}\,F\rangle_v \le \|F\|_{Y,v}^2$. Then `RowsBody` holds at $x$, and $\det X_c(x)_v$ is a unit for each $v$.

## Proof

Let $C \ge 0$ be the constant of `kernelHalf_chainNumbers_any_levelPrime` for $C_Y$. Put $C_0 = \max\bigl(2(16 + C_T),\, 6C + 1 + 2C^2,\, 4C(C_T + C)\bigr)$.

1. `kernelHalf_chainNumbers_any_levelPrime` bounds each step map of $Q$ (`FactorBounds`) by numbers of the shape `KerSide`.
2. $T$ is prime, so $T \ge 1$. With $\log T \le C_T m L$, `lastMapHalf_recNums_of_log_levelPrime_le` gives `LastSide` for the number `lastLog`.
3. `exists_htNums_of_kerSide_lastSide` packs the two into height numbers $h$ with $h_P = $ `lastLog`. It needs the three lower bounds on $R.C_h$ in $C_0$.
4. `exists_isFrames` gives $Y$. `colsIn_isometry` says that $f_0$ is an isometry and gives the second conclusion.
5. `kerChain_matrices_with_norm_bounds` gives `RowsBody` from frames of all families (`famFramed_chF`, `evGSD_datFramed`), the factorization $P = g \circ \mathrm{col} \circ f_0$ (`colPer_eq`, true by definition, with $g$ = `colPerL` the pairing on $S_1$) and a bound $|g(\psi)(F)|_v^2 \le e^{h_P} \operatorname{Re}\langle\psi,\psi\rangle_v \|F\|_{Y,v}^2$.
6. That bound is `period_le` with `lastMapNorm` (a norm statement for branching maps between interlacing weights, with the hypotheses `interlace` and `members_sameShift`), the last hypothesis, and $\langle\psi,\psi\rangle_v \ge 0$ (`ipAt_nonneg_of_datFramed`).

## In the Lean code

The theorem is in [ColumnsMemberRowsOfLogLevelLe.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ColumnsMemberRowsOfLogLevelLe.lean#L25). The lemmas in steps 1, 2 and 5 are relays to `kerSide_chainS`, `lastSide_of_logT_le` and `rowsBody_of_framed`, whose proofs we have not opened. `exists_htNums_of_kerSide_lastSide` only fills a record. Each hypothesis is used. We have not unfolded `HtNums`, the column bound data, `KerEquivC`, `Sizes` or the Hermitian families.

The namespace `GlobalTheory.ColRowsTop` has a theorem with the same short name, in [IpAtNonnegOfDatFramed.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IpAtNonnegOfDatFramed.lean#L109). It has four more hypotheses, uses `SizeRows` in place of `SizeRowsS` and the bound on $\log T$, and has the number 25 where this theorem has $C_T$. The index shows no use of it. The predicate `SizeRowsS` has a conjunct `True` ([ColHeightSharpWith.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/ColHeightSharpWith.lean#L16)).
