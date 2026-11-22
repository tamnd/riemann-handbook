---
id: exists-is-weil-k
title: Existence of the Weil representation of a unitary dual pair
kind: theorem
decl: PositivityTheory.ThKW.S.exists_isWeil_k
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.ThetaParseval.ThetaKernels.WpSTop
covers: 394
status: drafted
drafted_by: writer@claude
---
This theorem is the proof behind [the existence statement for Weil representations](/entry/weil-ex-k/). It turns the hermitian space $X$ and the skew-hermitian space $W$ into the matrix data that two earlier lemmas need, and then it calls them. It is the `_k` copy of the proof in [the entry on `weilEx`](/entry/s-weil-ex/), with `GoodK` in place of `IsGood`.

## Statement

**Theorem.** The hypotheses are those of [the parent entry](/entry/weil-ex-k/): `GoodK` base data, a hermitian $X$ of signature $(r, s)$, a skew-hermitian $W$ of signature $(r', s')$, a good tensor model $M$, and Hecke characters $\chi_X, \chi_W$ with `ResEtaPow` for the exponents $n$ and $d$. Then there is $\omega$ with `M.IsWeil B.ψ χX χW ω`.

`IsWeil` is `IsUWeilPair` for the Gram matrices of $X$ and $W$, the Darboux basis `M.co` and the scalar $-1$. We have not unfolded `IsUWeilPair` past its first layer: $\omega$ is a map from the product of the two adelic unitary groups to operators on functions on $\mathbb{A}_F^{n \times d}$, and `IsUWeilPair` asks that each factor gives a unitary Weil representation.

## Proof

1. Get $\xi_0 \neq 0$ with $\sigma(\xi_0) = -\xi_0$ (`exists_trace_zero_element`).
2. The Gram matrices $J_X$ and $J_W$ have unit determinant (`isUnit_det_gram_of_hermitianSelfDualLatticeSpace`, `isUnit_det_gram_skewHermitian_signature`).
3. So $J_X^{T}$ is hermitian and nondegenerate, and so is $-\xi_0 J_W^{-1}$ (`isHermitianNondegenerate_neg_traceZero_smul_inv_skewHermitian`).
4. `latH_of` uses the field `cm` of `GoodK` to give `LatH`: a lattice with the properties `GoodLat` and `RatSD`. We have not unfolded these.
5. `restricted_eta_power_character` turns each `ResEtaPow` into the form that the next lemmas take.
6. `exists_isWeilDatumOF_k` gives a Weil datum $\omega_0$ for the pair $(-\xi_0 J_W^{-1}, J_X^{T})$.
7. A short matrix computation gives $(-1) J_W = \xi_0 (-\xi_0 J_W^{-1})^{-1}$. This matches the scalar $-1$ in `M.co` with the scalar $\xi_0$ of the datum.
8. `exists_isUWeilPair_cm_k` turns $\omega_0$ into the pair representation for the basis `M.co`. It needs the field `rat` of `M.IsGood`, which says that `M.co` sends rational matrices to rational points.

## In the Lean code

- The theorem is in [WpSTop.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/WpSTop.lean#L18). The two main lemmas are in [WpSDat.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/WpSDat.lean#L19) and [WpSPair.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/WpSPair.lean#L18).
- `Model` and `IsGood` are in [WeilTensorModels.lean](lean:Development/AbelianVarietyTheory/BlockTheory/DivisorBase/WeilTensorModels.lean#L235). Of the five fields of `IsGood`, only `rat` is used. The fields `vac`, `std`, `haar` and `dom` are not used.
- `exists_trace_zero_element` in [ExistsTraceZeroElement.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/ExistsTraceZeroElement.lean#L13) is a `first | exact` wrapper of `exists_ne_zero_conj_neg_k`. `restricted_eta_power_character` is a wrapper of the same kind.
- The proof is the same, line for line, as `exists_isWeil` in [WeilEx.lean](lean:Development/WeilBound/ThetaLifts/Reductions/WeilPairs/WeilPairExistence/WeilEx.lean#L21). Only the lemma names change.
