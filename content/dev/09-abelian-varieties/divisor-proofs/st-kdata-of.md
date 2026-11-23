---
id: st-kdata-of
title: Pseudo-coefficient data on K from the lowest K-type character
kind: theorem
decl: GlobalTheory.PsCo.PcEF.stKData_of
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.TraceEqOfMem
covers: 373
status: drafted
drafted_by: writer@claude
---
This theorem proves `StKData` from 24 named statements. It has the argument of [`maximalCompact_pseudoCoefficientData'`](/entry/maximal-compact-pseudo-coefficient-data-prime/), which supplies the 24 lemmas. The polynomial $P_M$ of [`localPC_holds`](/entry/local-pc-holds/) is, on $K$, a sign times $\overline{\chi_T} \cdot \det(1 - A(k))$. Here $\chi_T$ is the [[character|RMWMYBY8TC]] of one $K$-type $T$ of $D$.

## Statement

The conclusion is `StKData`, with clauses 1 to 4 as in [`maximalCompact_pseudoCoefficientData`](/entry/maximal-compact-pseudo-coefficient-data/). The hypotheses are 24 propositions (`BlockForm`, `OmDet`, `CoefPoly`, `TrPoly`, `ClassFn`, `GaInt`, `ToKType`, `PhysTor`, `TorusId`, `AvgMap`, `SchurOne`, `RangeFD`, `BuildY`, `StrKer`, `StrIdx`, `HWVec`, `CoordFD`, `CasCoord`, `AlgDatum`, `DatumEquiv`, `CptCase`, `GapNum`, `MatRep`, `CasScal`).

## Proof

Let $s$ be the number of pairs $(a, b)$ with $\varepsilon_a = 1$, $\varepsilon_b = -1$, $b < a$ (`sDeg`). Let $\Delta(k) = \det(1 - A(k))$, with $A(k)_{(a,b),(a',b')} = k_{aa'} \overline{k_{bb'}}$ over the pairs with $\varepsilon_a = 1$, $\varepsilon_b = -1$ (`physDet`).

1. `GapNum`: since $r$ is odd and the gaps are large, $\lambda$ is a Harish-Chandra parameter, and further gap conditions hold.
2. `exists_type` gives a $K$-irreducible $T$ of highest weight $\lambda - \rho_c + \rho_{hol}$ (`gaW`). For each polynomial $P$ with $P = \overline{\chi_T}$ on $K$, the operator $\int_K P(k) \Delta(k) D(k)\, dk$ has trace $(-1)^s$. If $p = 0$ or $q = 0$, `CptCase` says $\Delta = 1$, $s = 0$ and $D$ itself is $T$. Then the trace is $\int_K \lvert \chi_T \rvert^2 = 1$ by `SchurOne` ([[Schur orthogonality|ETNDTECY97]]). Otherwise the lemma `supTrace` gives the trace as $(-1)^s \int_K \lvert \chi_T \rvert^2$.
3. `CoefPoly` and `TrPoly` give such a $P$. `OmDet` gives $Q$ with $Q \det(\Omega) = \Delta$ on $K$. `BlockForm` applied to $(-1)^s P Q$ gives $M$ and $R$ in the block algebra with $P_M = \det(\bar{x})^M R \det(\Omega) = (-1)^s P \Delta$ on $K$.
4. Clause 1: `ClassFn` says $\Delta$ and $\chi_T$ are class functions on $K$.
5. Clause 2: `GaInt` writes the weight as integers $\Lambda$, $m$. `ToKType` and the lemma `weyl` give $\mathrm{den}(t_\theta)\, \chi_T(t_\theta) = \mathrm{num}(t_\theta)$, the Weyl character formula for $K$ (A. W. Knapp, *Lie Groups Beyond an Introduction*, Chapter V). `TorusId` turns this into $(-1)^s \chi_T(t_\theta) = \Theta_\lambda(t_\theta)\, \Delta(t_\theta)$. Take conjugates, multiply by $\Delta(t_\theta)$, and use $\lvert \Delta(t_\theta) \rvert^2 = d(\theta)$ (`PhysTor`).
6. Clause 3: $(-1)^s B$ is the operator of step 2, so $(-1)^s c = (-1)^s$ and $c = 1$.
7. Clause 4: suppose $c \neq 0$. `MatRep` extends $\pi$ to a function on matrices. `equiv_of_index` then gives a unitary equivalence of $\pi$ with $D$, which is false by hypothesis.

`equiv_of_index` uses the other eleven statements. A nonzero trace gives, through `StrIdx`, `StrKer` and `AvgMap`, a nonzero $K$-map from $T$ into a finite-dimensional space built from $\pi$. `HWVec` and `AlgDatum` give a $K$-irreducible subspace of highest weight $\lambda + \rho_n - \rho_c$ on which the Casimir acts by the scalar `casVal λ`. `DatumEquiv` says that this determines $D$. We have not unfolded `RangeFD`, `BuildY`, `StrKer`, `StrIdx`, `HWVec`, `CoordFD`, `CasCoord` or `AlgDatum`.

## In the Lean code

The theorem is in [TraceEqOfMem.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TraceEqOfMem.lean#L106). `exists_type` is at line 61 and `equiv_of_index` at line 27. The statements are in [VdmSplit.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/VdmSplit.lean#L23) and [DatumEquiv.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/DatumEquiv.lean#L36). `supTrace` and `weyl` are imported theorems, not hypotheses. `GapNum` repeats the body of `Gap4` instead of using the name.
