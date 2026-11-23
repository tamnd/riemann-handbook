---
id: exists-weil-representation-big-cell-relation-fourier
title: The big cell relation for the Fourier transform (statement)
kind: theorem
decl: GlobalTheory.T.exists_weilRepresentation_bigCell_relation_fourier
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsWeilRepresentationBigCellRelationFourierStatement
covers: 857
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the Weyl cell relation](/entry/weyl-cell-relation/). Its proof applies that lemma and does nothing else. Its one user is [the construction of the Weil representation](/entry/exists-is-kw/), where it supplies the constant $\kappa$ and the relation for the big cell.

## Statement

The setting and the notation $P$, $w$, $\mathcal F$, $\rho$ are those of [the construction](/entry/exists-is-kw/). The theorem says: there is $\kappa \neq 0$ such that for each $p \in P$ with $wpw \in PwP$ there are $p_1, p_2 \in P$ with $wpw = p_1 w p_2$ and

$$\kappa\mathcal F\,\rho(p)\,\kappa\mathcal F\,\varphi = \rho(p_1)\,\kappa\mathcal F\,\rho(p_2)\,\varphi$$

for each locally constant $\varphi$ of compact support on $M_{m \times n}(E)$.

## Proof

The proof applies `GlobalTheory.KSp.weyl_cell_relation` to the same arguments. There is nothing else.

## In the Lean code

The theorem is at [ExistsWeilRepresentationBigCellRelationFourierStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsWeilRepresentationBigCellRelationFourierStatement.lean#L9). Its statement is the statement of `KSp.weyl_cell_relation`, and the proof is a `first` tactic that tries three ways to apply it. All 856 other declarations below it are below `weyl_cell_relation`.

The name is misleading. It begins with "exists Weil representation", but the statement has no representation in it. It is only the existence of $\kappa$ and of the relation above, which is one input to the construction of the representation.
