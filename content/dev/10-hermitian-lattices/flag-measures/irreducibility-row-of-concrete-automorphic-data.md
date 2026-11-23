---
id: irreducibility-row-of-concrete-automorphic-data
title: The count rows from the ties (statement)
kind: theorem
decl: GlobalTheory.T.irreducibilityRow_of_concreteAutomorphicData
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.IrreducibilityRowOfConcreteAutomorphicDataStatement
covers: 531
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`IrrRowConcrete.irr_row_closed`](/entry/irr-row-closed/). It has the same statement, and its proof is that lemma. Its user is [`row_counts_of_ties_alt`](/entry/row-counts-of-ties-alt/), step 2 of the proof of the counting row: it gives the constant $c_{Ic} > 0$ and the map from the three ties to the second property of `CountsIrreducibilityConstants'`. The proof is in [`irr_row_closed`](/entry/irr-row-closed/).

## Statement

**Theorem.** Assume `SiegelWeilUnitaryConvergent` (stated in [the counting row](/entry/row-counts-of-ties-alt/)) and `RowsFinDim`. Then there is $c_{Ic} > 0$ with this property. Let $\mathcal{C}$ be a family class all of whose families satisfy `TuSize`. If it is [closed](/step/closed-def/) on $\mathcal{C}$ that, for large $x$ and each $i$, the datum $D(x,i)$ has a Hida setting $X$, a good operator $G$ and a linear isometry $\iota$ with the ties `AutTie`, `RowDictTie` and `LabTie`, then it is closed on $\mathcal{C}$ that, for large $x$ and each $i$, there are rows $A$ for $D(x,i)$ with `LabelCountGoodInjective`, `AllJoinA` and `CountAllRows A (epsC cIc r f)`.

The terms are explained in [`irr_row_closed`](/entry/irr-row-closed/).

## Proof

The proof is one line: it applies `GlobalTheory.IrrRowConcrete.irr_row_closed`.

## In the Lean code

The theorem is in [IrreducibilityRowOfConcreteAutomorphicDataStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/IrreducibilityRowOfConcreteAutomorphicDataStatement.lean#L13). The statement is copied word for word from `irr_row_closed`, and the proof is the usual `first | exact @... | ...` tactic. The name speaks of "concrete automorphic data". In the statement, these data are the Hida settings and ties in the hypothesis on $\mathcal{C}$.
