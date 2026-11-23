---
id: row-data-supplied-at-self-conjugate-places
title: Row data at self-conjugate places (statement form)
kind: theorem
decl: GlobalTheory.T.rowData_supplied_at_selfConjugate_places
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.RowDataSuppliedAtSelfConjugatePlacesStatement
covers: 304
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`supplyC_selfConj`](/entry/supply-c-self-conj/), which has the real content. Its one user is [`exists_rowFam`](/entry/exists-row-fam/), which applies it to the labelling of the embeddings by a place and a sign, at a prime where Frobenius acts as complex conjugation.

## Statement

**Theorem.** Assume `UpFSt p` for all primes $p$, and that the involution on $\mathcal{O}_E$ is the conjugation of the host. Let $y$ be an algebraic integral point of the moduli scheme $X$ with a chart, and let $Y$ be a chart over a valued field $C$ of characteristic $0$, tied to the chart at $y$ by `IsBC`. The structure `FBChart` of $Y$ asks that $C$ be algebraically closed and complete. Let a labelling $\tau \colon \mathrm{Orb} \times \mathbb{Z}/2 \to (E \to \mathbb{C})$ with ranks $n, j, j'$ satisfy `ArithS`, be onto, satisfy `RankOK`, and have $j' < n$. Let $a$ be a dominant weight, and let $\nu \le$ `nuLocC` at the chart. Then `SupplyC` holds: there are row data and flags with the sizes $n$ and $j + j'$, alternating, with ranks $\mathrm{mult}\,\tau(o,s)$, and with the block bound `ValBlocksC` on $\nu$.

[The entry for `supplyC_selfConj`](/entry/supply-c-self-conj/) gives each hypothesis in full.

## Proof

The proof is one line: `first | exact @GlobalTheory.RowAt.supplyC_selfConj | ...`. The statement is the same as that of `supplyC_selfConj`, word for word.

## In the Lean code

The theorem is in [RowDataSuppliedAtSelfConjugatePlacesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/RowDataSuppliedAtSelfConjugatePlacesStatement.lean#L9). It calls `GlobalTheory.RowAt.supplyC_selfConj` in [RowDataSuppliedAtSelfConjugatePlaces.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/RowDataSuppliedAtSelfConjugatePlaces.lean#L32). `SupplyC` is in [IsSelfOf.lean](lean:Development/AbelianVarietyTheory/Definitions/Jets/IsSelfOf.lean#L36).
