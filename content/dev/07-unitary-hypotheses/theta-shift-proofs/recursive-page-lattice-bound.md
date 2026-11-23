---
id: recursive-page-lattice-bound
title: The quotient index bound at a run (statement form)
kind: theorem
decl: GlobalTheory.T.recursive_page_lattice_bound
module: Development.AbelianVarietyTheory.Proofs.ThetaShiftProofs.RecursivePageLatticeBoundStatement
covers: 838
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`qAt_run`](/entry/q-at-run/), which has the real content. Its one user is [`inputsNet_recPlus`](/entry/inputs-net-rec-plus/), which takes from it the constant function $C_q$ and the bound `QAt` for the field `BaseIn` of the inputs of the index bound.

## Statement

Use the datum $D$, the record $T$ with `h : LawsP T`, the algebra of forms $X_j$ (`recPJ h j hj`) and the condition `PageOK` from [the entry for `runHolds_of_parOK`](/entry/run-holds-of-par-ok/). Let $K$, $S_\kappa$ and $M_\kappa$ be the number field, the space of cusp forms of weight $\kappa$ and its lattice in the provider `recB h.toLawsCore`.

**Theorem.** There is $C_q \colon \mathbb{R}^2 \to \mathbb{R}$ such that, for all data with $j \in [1, m)$: if `PageOK` holds for $X_j$ and $M_\kappa$ is a lattice in $S_\kappa$, then the quotient index bound `QAt` holds with the constants

$$C_R = 7,\quad C_k = H.C_K,\quad C_h = 1,\quad A_h = 4,\quad C_c = C_q(H.C_A, H.C_K),\quad A_c = 4,$$

and with $T = T_n$ and $c = $ `cc D L C2 A2 7 wL`.

[The entry for `qAt_run`](/entry/q-at-run/) says what `QAt` contains.

## Proof

The statement is the same as that of `GlobalTheory.RunJoin.qAt_run`, and the proof applies it.

## In the Lean code

The theorem is in [RecursivePageLatticeBoundStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/RecursivePageLatticeBoundStatement.lean#L22). The proof is `first | exact @GlobalTheory.RunJoin.qAt_run | ...`, a tactic that tries the alias in three forms. The name says "lattice bound", but the conclusion is the bound `QAt` on the index of a submodule in a quotient lattice, and the lattice property `LatAt` is a hypothesis.
