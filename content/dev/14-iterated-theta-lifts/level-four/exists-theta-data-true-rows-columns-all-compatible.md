---
id: exists-theta-data-true-rows-columns-all-compatible
title: Theta data for every level 4 object, under its published name
kind: theorem
decl: GlobalTheory.T.exists_thetaData_trueRowsColumns_allCompatible
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ExistsThetaDataTrueRowsColumnsAllCompatibleStatement
covers: 808
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`thEx_main`](/entry/th-ex-main/). The [membership theorem](/entry/member-e-closing-alt-alt/) calls it twice, once for the slot $s$ and once for the refined slot $s_g$, with the side condition from `io_zero`. The content is in [`thEx_main`](/entry/th-ex-main/).

## Statement

The statement is word for word the statement of [`thEx_main`](/entry/th-ex-main/). It has seven hypotheses: the Weil representation of a unitary pair, rapid decay of cusp forms, Casselman-Wallach, Harish-Chandra modules, and three statements on discrete series (existence, uniqueness up to unitary equivalence, and existence of a discrete series datum with a given parameter).

Let $\mathcal{S}$ be a slot. Assume that for each rows object $t$ at the position $\mathcal{S}.\mathrm{Rx}$, and for each tuple $\mu$ that is not used (neither $\mu_0$ nor $\mu_w$ for a place $w$), the maps $\mathrm{io}_{\mu,j}$ vanish for $j < m$. Then `ThEx 𝒮`: each level 4 object has a theta datum.

## Proof

The proof is one call of `thEx_main`, written as a `first` block that tries `exact` and `apply`.

## In the Lean code

The theorem is in [ExistsThetaDataTrueRowsColumnsAllCompatibleStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsThetaDataTrueRowsColumnsAllCompatibleStatement.lean#L16). The name says "true rows and columns, all compatible", but the conclusion asks for no column data: `ThEx` asks only for a theta datum with the certificate `ThT`. Two of the seven hypotheses, Casselman-Wallach and Harish-Chandra modules, are not used by `thEx_main`, so they are not used here either.
