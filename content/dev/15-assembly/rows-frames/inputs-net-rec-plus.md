---
id: inputs-net-rec-plus
title: The inputs of the index bound at all valued points, from the parameter conditions
kind: theorem
decl: GlobalTheory.InputsAtRecord.inputsNet_recPlus
module: Development.AbelianVarietyTheory.Proofs.HeightProofs.ExistsIndexBoundHypothesesWithNetAllValuedPoints
covers: 4548
status: drafted
drafted_by: writer@claude
---
This theorem collects, at one run, all the inputs that the index bound needs. It is the real content of [`runHolds_of_parOK`](/entry/run-holds-of-par-ok/), which uses it through its statement form [`exists_indexBoundHypothesesWithNet_allValuedPoints`](/entry/exists-index-bound-hypotheses-with-net-all-valued-points/). It is in branch 2 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/). The proof calls about ten large lemmas and joins their results.

## Statement

Use the record $T$, the algebra of forms $X_j$ and the conditions `ParOK` and `PageOK` from [the entry for `runHolds_of_parOK`](/entry/run-holds-of-par-ok/). Let $X_j^+$ be $X_j$ with the extra points `extAll` added. These are, over each prime $\lambda$, the valuations of `valSet` under the trivial class condition.

**Theorem.** There are $C_L \in \mathbb{R}$ and $C_q, Z_0 \colon \mathbb{R}^2 \to \mathbb{R}$ such that, for all data with `ParOK T EX p j`, `PageOK` for $X_j$ and $Z_0(H.C_A, H.C_K) \le$ `zBase L`, the property `InputsNet` holds for $X_j^+$ and `PageSupp` holds. The constants are `kR C_L` and $C_q(H.C_A, H.C_K)$, and the scalars are `scalOfP`.

`InputsNet` is a conjunction of four parts.

1. `BaseIn`: the run hypotheses `HypC`, the lattice condition `LatAt`, a lower bound `LAMwAt` with constant $C_L$, the bound `QAt` when $j < m$, and `DeepSubMul`.
2. `NetIn`: a net `NetData` with a complex embedding $\sigma_0$ of $K$, with four conditions and $\log \# N \le P_d$.
3. `FamIn`: a family `GlobalFamilyData` $G$ (forms $\theta'_i$ of weight $w_F$, forms of weight $w_L$, a number $\delta$ and more), with twelve conditions on it.
4. `PtIn`: the bound `CombBound`, and at each $\lambda$ a local point datum with the curve, tie and lift conditions and the `Heights` bound.

The constants of the family are $G_c =$ `gcR`, $P_H =$ `phR`, $P_{rw} =$ `prwR`, $P_{et} =$ `PPv 200000 2` and $P_d =$ `pdR`.

## Proof

1. `integralForms_logSupNorm_lower_bound_absolute` gives $C_L$ and `LAMwAt`. `recursive_page_lattice_bound` gives $C_q$ and `QAt`. `RunNum.polyDom_of_pageOK` gives $Z_0$ and the conditions `PageGq` and `PolyDom`.
2. `runHypotheses_formsScalars_of_parameterConditions` gives `HypC`, `LatAt`, `PageSupp` and a spanning set of forms of weight $w_F$.
3. `exists_gen_eta` gives a family $G_1$. It uses `exists_admissible_thetaLatticeGenerators` and, when $j < m$, `exists_scalarWeight_auxiliaryForm_of_runConditions`.
4. `sharesAt_all` gives the new $\delta$ and $\theta'$, and five share conditions. It uses `cuspFormBasisShares_indefinite_liftIndex` for $j < m$ and `cuspFormBasisShares_definite_liftIndex` for $j = m$. Put them into $G_1$ to get $G$.
5. `combinedBound_for_runScalars`, with `hodgeTate_inclusion_chart_characters`, gives `CombBound`. `RunJoin.net_at_run` gives the net and `DeepSubMul`.
6. [`exists_primeData_curve_lifting_heightBounds`](/entry/exists-prime-data-curve-lifting-height-bounds/) gives the local point data and `Heights`.
7. `combBound_xplus`, with `regularity_R2_extended_points`, moves `CombBound` to $X_j^+$.

The rest is bookkeeping.

## In the Lean code

The theorem is in [ExistsIndexBoundHypothesesWithNetAllValuedPoints.lean](lean:Development/AbelianVarietyTheory/Proofs/HeightProofs/ExistsIndexBoundHypothesesWithNetAllValuedPoints.lean#L79). `InputsNet` and its parts are in [ConclOfInputs4.lean](lean:Development/AbelianVarietyTheory/Definitions/HeightFunctions/ConclOfInputs4.lean#L51). We have not unfolded `HypC`, `CombBound`, `NetData` or the twelve conditions of `FamIn`.

- `baseIn_xplus` and `famIn_xplus` ([L29](lean:Development/AbelianVarietyTheory/Proofs/HeightProofs/ExistsIndexBoundHypothesesWithNetAllValuedPoints.lean#L29)) have the proof `h`. So `BaseIn` and `FamIn` do not see the extra points. Only `CombBound` and the local point data are about $X_j^+$.
- The proof drops one output of `runHypotheses_formsScalars_of_parameterConditions` and one of `net_at_run`.
