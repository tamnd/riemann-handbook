---
id: lattices-frames-base-points-exist-alt
title: Lattices, base points and frames for a geometric datum
kind: theorem
decl: GlobalTheory.Fam.lattices_frames_basePoints_exist_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.LatticesFramesBasePointsExist
covers: 422
status: drafted
drafted_by: writer@claude
---
This theorem chooses, for a geometric datum, the lattices $N_j$ on the spaces $Y_j$, the base points $b_j$ and the local frames at the places of $P_g$ and $Q$. Through its second name [`local_component_vector_relation_alt`](/entry/local-component-vector-relation-alt/) it gives these to [`core_data_of_point`](/entry/core-data-of-point/), in step 6 of its proof. It joins two lemmas: one makes the lattices, the other the base points.

## Statement

We use the notation of [`core_data_of_point`](/entry/core-data-of-point/): $W$, $u$, $T_u$, the datum $a$, rational data $y$, measures $m$, level data $v$ with level places $P_G$ and twist places $P_T$, type data $o$, and local data $l_{\mathfrak P}$ (`LocX`) at each place $\mathfrak P$ of $P_g$ or $Q$, over a split local field $k_{\mathfrak P}$, with a family `bas` of bases. A lattice $N$ of a hermitian space $S$ is *self-dual* (`IsSelfDualC`) if $y \in N$ exactly when $\langle x, y \rangle \in \mathcal O_E$ for all $x \in N$. A frame $F$ at a split place $q$ is *integral* for $N$ (`IntIn`) if $y \in k^Y$ is integral exactly when $F y$ lies in the completion of $N$ at $q$.

Assume `PackageHypotheses W`, the conditions on the common datum, `y.Tau`, $\langle \zeta_0, \zeta_0 \rangle = T_u$, $v.\tau = y.\tau$, $v.N_T = L_T$, $o.\zeta_0 = \zeta_0$, $L_T$ self-dual, $P_G$ the places under $P_g$, $P_T$ the places dividing $T_u$, `PreT v o`, the orthogonality condition off $P_T$, and `bas` = 1 off $P_g$.

**Theorem.** There are lattices $N_j$ of $Y_j$, elements $b_j \in G_f(Y_j)$, a finitely supported $d_T$, and lattices $M$ and frames $\beta_0$ on the Bessel spaces of $y$, such that:

1. `ShapeOff` holds for $v$ with $N$, $d_T$ and the ramified sets of $o$, and for $o$ with $M$, $\beta_0$;
2. each matrix in the support of $d_T$ satisfies `MxAt` at $P_T$ (`CombAt`);
3. for $j < m$, $N_j$ is self-dual, and $b_j$ moves $\Lambda_Y^j$ to $N_j$ (`Moves`) at each set of places outside $P_G$;
4. at each $\mathfrak P$, `LocY` holds: normal frames $F_Y$ and units $s_j$ with the Bessel and Jacquet frame conditions and a relation for $\tau$, the frames $F_Y$ integral for $N_j$, and the condition `MovedTo` on $b_j$, $\beta_Y^j$ and the frame $F_Y \cdot$ `bas` after an ordering of its index set.

## Proof

1. `level_prime_not_mem_under_Pg_alt` (line 20) shows that $T_u$ lies in no place under $P_g$: $T_u$ and the primes $g_k$ that define $P_g$ are distinct primes, hence coprime. So $P_G$ and $P_T$ are disjoint.
2. `levelPrime_not_mem_places_alt` extends this to the places of $Q$.
3. At each $\mathfrak P$, `exists_normalFrames_rationalDecompositions_over_local` gives normal frames $F_Y$ and units $s$ (`IsNormalFr`). It needs `y.Tau`, the norm of $\zeta_0$ and step 2.
4. [`local_component_measure_identity_alt_bis`](/entry/local-component-measure-identity-alt-bis/) gives $N$, $d_T$, $M$, $\beta_0$ with clauses 1, 2, self-duality and the integrality of $F_Y$ for $N$.
5. `local_component_measure_identity_alt_alt` gives $b$ with $b_j \in G_f(Y_j)$, the moves of clause 3 and the frame condition of clause 4.
6. `IsNormalFr` is the first six fields of `LocY`; with steps 4 and 5 this fills the last two.

## In the Lean code

The theorem is at [LatticesFramesBasePointsExist.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LatticesFramesBasePointsExist.lean#L39). `LocY` is in [FrameTopAlt.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/FrameTopAlt.lean#L87), `IsNormalFr` in [IsNormalFr.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/IsNormalFr.lean#L20), `IntIn` in [HzUnit.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/HzUnit.lean#L26), `IsSelfDualC` in [LocalNewformFunction.lean](lean:Formalism/LocalToGlobal/IndefiniteReal/LocalNewformFunction.lean#L337), `Moves` in [IsSumFrame.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/IsSumFrame.lean#L50).

The names of the two lemmas of steps 4 and 5 speak of a "measure identity", but their conclusions are about lattices, frames and base points. We have not opened their proofs, nor unfolded `ShapeOff`, `PreT` or `MovedTo`. A parallel copy for `RealPack`, `lattices_frames_basePoints_exist`, is in [LocalComponentVectorRelation.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/LocalComponentVectorRelation.lean#L46).
