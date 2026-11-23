---
id: local-component-vector-relation-alt
title: Lattices, base points and frames for a geometric datum, in statement form
kind: theorem
decl: GlobalTheory.T.local_component_vector_relation_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.LatticesFramesBasePointsExistStatement
covers: 423
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`lattices_frames_basePoints_exist_alt`](/entry/lattices-frames-base-points-exist-alt/). Its only user is [`core_data_of_point`](/entry/core-data-of-point/), which calls it in step 6 of its proof to get the lattices $N_j$ on the spaces $Y_j$, the base points $b_j$ and the local frames of the geometric family. The real content is in `lattices_frames_basePoints_exist_alt`.

## Statement

The statement is word for word the statement of [`lattices_frames_basePoints_exist_alt`](/entry/lattices-frames-base-points-exist-alt/). In short: let $a$ be a geometric datum with rational data $y$, measures $m$, level data $v$, type data $o$ and local data $l_{\mathfrak P}$ at the places of $P_g$ and $Q$, under the hypotheses that `core_data_of_point` has at that point. Then there are self-dual lattices $N_j$, finite adelic base points $b_j$ and a twist $d_T$ such that the shape condition holds, each $b_j$ moves the package lattice $\Lambda_Y^j$ to $N_j$ off the level places, and each place has normal frames (`LocY`).

## Proof

The proof applies `lattices_frames_basePoints_exist_alt`. Nothing else happens.

## In the Lean code

The theorem is at [LatticesFramesBasePointsExistStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LatticesFramesBasePointsExistStatement.lean#L16). The proof is the tactic `first | exact @GlobalTheory.Fam.lattices_frames_basePoints_exist_alt | ...`, so the theorem only passes its hypotheses along. The name speaks of a vector relation. The nearest clause is the field `tau` of `LocY`, which says that the local image of $\tau$ sends $\zeta_0$ to a multiple of the Bessel vector. The file name describes the statement better: lattices, frames and base points exist.
