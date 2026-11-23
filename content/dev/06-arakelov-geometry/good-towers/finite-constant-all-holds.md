---
id: finite-constant-all-holds
title: The p-adic norm of a flat frame function is constant, restated
kind: theorem
decl: GlobalTheory.T.finite_constant_all_holds
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.FiniteConstantAllHoldsStatement
covers: 431
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It states `FinConstAll` and its proof applies [`FinAll.finConstAll`](/entry/fin-const-all/), which has the content. Its users are `finConst_of_all_hosts`, `FinGood.finGood` and `thmFlatA_of_parts`, below [`topCovolSlim2_use_alt_alt`](/proof/literature/).

## Statement

`FinConstAll` says that `FinConstFor H` holds for every CM field $E$ and every host datum $H$ of $E$. In words: let $O$ be a discrete valuation ring inside the coefficient field $F$ that is the unit ball of a $p$-adic embedding $\kappa \colon F \to \mathbb{C}_p$, and let $Y$ be a model over $O$ with `SplitFibres` and `N3`. If a frame function $\varphi$ is flat on a geometric compactification $Z$ over $Y$, then there is a real $t$ with $\log|\varphi(y, v, w)|_\kappa = t$ at every framed point with integral frames over a discrete valuation ring. The full hypotheses are in [the entry on `finConstAll`](/entry/fin-const-all/).

## Proof

The statement is the same as that of `FinAll.finConstAll`, and the proof applies it.

## In the Lean code

The theorem is in [FiniteConstantAllHoldsStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/FiniteConstantAllHoldsStatement.lean#L5). `FinConstAll` is in [FinConstFor.lean](lean:Development/AutomorphicSpectrum/Statements/GeometryStatements/FinConstFor.lean#L27). The same file has `FinConst`, which asks `FinConstFor H` only for hosts with `IsHostRange H`, and `FinConstAll.finConst` derives it at once. So the restriction to `IsHostRange` gives nothing that the case of all hosts does not give.
