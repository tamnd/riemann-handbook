---
id: exists-rep-principal-siegel-adjoint-order-action
title: Principal Siegel objects with an action of an order have a fine moduli scheme, statement form
kind: theorem
decl: GlobalTheory.T.exists_rep_principalSiegel_adjoint_orderAction
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsRepPrincipalSiegelAdjointOrderActionStatement
covers: 568
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the moduli of principal Siegel objects with an action of an order](/entry/act-sieg-exists-rep/). It is step 2 of [the representability of Siegel moduli with kernel killed by $d$](/entry/sd-rep-of-coprime/): there it gives the scheme $H$ that represents principal objects of genus $8h$ with an $O$-action.

## Statement

The statement is word for word the statement of `GlobalTheory.ActSieg.exists_rep`. In short: let $h \geq 1$, $M \geq 3$ odd, and let $O$ be a ring with an additive map $\bar{\ }$, a finite set of generators, and an integer matrix $W$ with $W + W^{\mathsf{T}}$ positive definite and $\sum W_{ij} e_j \bar e_i = d_0 > 0$. Then there is a scheme $H$, quasi-projective over $\mathbb{Z}[\zeta_M, 1/M]$ and locally noetherian, with a universal principal Siegel object of genus $h$ and level $M$ and a universal adjoint right $O$-action. Each such object with an action over a scheme $S$ is its pullback along a unique map $S \to H$.

## Proof

The proof is one tactic line: `exact @GlobalTheory.ActSieg.exists_rep`. All the content is in [the entry for `exists_rep`](/entry/act-sieg-exists-rep/).

## In the Lean code

The theorem is in [ExistsRepPrincipalSiegelAdjointOrderActionStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsRepPrincipalSiegelAdjointOrderActionStatement.lean#L7). The proof is `first | (exact @exists_rep) | ...`, with two fallback tactics. The parent `sdRep_of_coprime` calls this name, not `exists_rep`.
