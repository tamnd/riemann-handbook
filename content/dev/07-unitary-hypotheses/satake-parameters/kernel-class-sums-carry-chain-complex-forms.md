---
id: kernel-class-sums-carry-chain-complex-forms
title: The kernel maps raise the filtration of member forms (restatement)
kind: theorem
decl: GlobalTheory.T.kernelClassSums_carry_chainComplexForms
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.KernelClassSumsCarryChainComplexFormsStatement
covers: 340
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`kFi_of_tie`](/entry/k-fi-of-tie/), with the same statement. [`at_of_true_columns`](/entry/at-of-true-columns/) calls it for the second entry $t'$ of the duties of a standard tie, and gets the conjunct `KFi` of `Pdv.At`. The content is in `kFi_of_tie`.

## Statement

Let $D$ be a datum (`D7`) with its data and extra data `ex`, and let $t$ be a tied kernel entry of `ex` (`KerEntTied ex`).

**Theorem.** If $t$ has the column side properties (`ColSide t`) and its member forms are pinned (`FormsPin t`), then `OrbitPlaces.KFi D ex.tw` holds.

`KFi D T` says that the kernel maps raise the filtration of member forms by one step. For each word $u$ and each level $i < m$, the kernel map $K_i$ of the chain of $u$ sends the space $F_i$ of member forms of $D$ into $F_{i+1}$. The same holds for the twisted forms `T.fm u μ` and the twisted chains `D.chTw u μ`, for each used tuple $\mu$. The [entry for `kFi_of_tie`](/entry/k-fi-of-tie/) says what `ColSide` and `FormsPin` ask.

## Proof

The proof is `exact kFi_of_tie`, through a `first | exact … | …` tactic block.

## In the Lean code

The theorem is at [KernelClassSumsCarryChainComplexFormsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/KernelClassSumsCarryChainComplexFormsStatement.lean#L7). `KFi` is at [OrbitPlaces.lean](lean:Formalism/SharpRestriction/Divisibility/OrbitPlaces.lean#L107).

The name speaks of "class sums" and "chain complex forms". Neither appears in the statement. The conclusion does not depend on $t$; the tie only supplies witnesses.
