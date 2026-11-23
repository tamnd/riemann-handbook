---
id: expansion-pairing-invariant-inner-vertex-level
title: Invariance at an inner top vertex (named form)
kind: theorem
decl: GlobalTheory.T.expansionPairing_invariant_inner_vertex_level
module: Development.AbelianVarietyTheory.Proofs.TwistedOperators.ExpansionPairingInvariantInnerVertexLevelStatement
covers: 339
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It gives [`pairPts_update_top`](/entry/pair-pts-update-top/), which has the real content, a second name in the namespace `GlobalTheory.T`. Its one user is [`levels_invariant`](/entry/levels-invariant/), where it is the first of the four parts.

## Statement

Take the grid data, the expansion $\tau$ and the hypotheses of [`levels_invariant`](/entry/levels-invariant/), with the same notation. Let $P_\tau(x, y)$ be the pairing of points `pairPts S τ x y`. Let $0 < j < m$ and let $k$ be a point of the top vertex $j$ whose image lies in the level group $K^{\mathrm{top}}_j$ (`S.levTop t Φ β j`). Then

$$P_\tau(x_j \mapsto x_j k,\ y)\bigl(\Psi(x_0), F(y_0)\bigr) = P_\tau(x, y)\bigl(\Psi(x_0), F(y_0)\bigr).$$

In the Lean form, the left side has $\Psi$ at the point $0$ of the updated tuple. Since $j \ne 0$, this point is $x_0$.

## Proof

The proof is the term `GlobalTheory.ExpansionInvariance.pairPts_update_top`. Nothing else happens.

## In the Lean code

The theorem is in [ExpansionPairingInvariantInnerVertexLevelStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExpansionPairingInvariantInnerVertexLevelStatement.lean#L9). The proof is the tactic `first | exact @GlobalTheory.ExpansionInvariance.pairPts_update_top | ...`, and the first branch closes the goal. The statement is word for word that of `pairPts_update_top`.

A different theorem, `GlobalTheory.T.expansionPairing_invariant_innerVertex_level` in [ExpansionPairingInvariantInnerVertexLevelTer.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExpansionPairingInvariantInnerVertexLevelTer.lean#L9), has almost the same name. It is about the inner row vertices and comes from `GlobalTheory.RowVertexInv.pairPts_update_row`. The two names differ only in `inner_vertex` against `innerVertex`.
