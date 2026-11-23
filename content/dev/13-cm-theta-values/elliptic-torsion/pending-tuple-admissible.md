---
id: pending-tuple-admissible
title: The pending tuple of a formal group system is admissible
kind: theorem
decl: Formalism.L2.PairingIndexBounds.Ent.pending_tuple_admissible
module: Formalism.LocalToGlobal.PairingIndexBounds.RowActionCoefficients.LatticeShapeMiddleHolds
covers: 420
status: drafted
drafted_by: writer@claude
---
This theorem says that the pending tuple `pendT` of a formal group system is admissible (`adm7`). It is a pass-through: it gives eight facts, each proved with no hypothesis, to `pending_tuple_admissible_of_shape`. Its user is [`admissible_general_of_kernel_law`](/entry/admissible-general-of-kernel-law/). The real content is in the lemma `admissible_general_lattice_tuple`.

## Statement

Let $X$ be a formal group system at a prime $p$ (`Sys p`). Let $E$, `hfin`, `hst`, `hLT`, `pos` and $F$ be the other data of `pendT`. Let $D$ be a datum.

**Theorem.** `adm7 D X (pendT X E hfin hst hLT pos F)` holds.

`adm7` says this. Take lattice tuples $L_a$ at level $j$ and $L', L''$ at level $j+1$, and $i_0$ such that at each place either $i_0(v) = 0$ and $L''_v = L'_v$, or $(L''_v, L'_v)$ is an edge of type $i_0(v) \ge 1$. Then there is a frame $\varphi$ such that, for each power series $f$ whose differential coefficients have valuation at least $g$, the kernel `kerF` of $f$ after substitution by $\varphi$, scaled by powers of $p$, lies in the lattice `inLatC (j+1) g L'`. We have not unfolded `kerF` or `inLatC`.

## Proof

The proof applies `pending_tuple_admissible_of_shape` to the facts `XShape`, `XBrS`, `XBrT`, `XInj`, `XSpanN`, `XMid`, `XUnit` and `XEdge`. That lemma applies `admissible_general_lattice_tuple` with $K_c = \mathbb C_p$, where `XEdge` gives the frame and the other facts give the lattice bound.

## In the Lean code

The theorem is at [LatticeShapeMiddleHolds.lean](lean:Formalism/LocalToGlobal/PairingIndexBounds/RowActionCoefficients/LatticeShapeMiddleHolds.lean#L26). `pending_tuple_admissible_of_shape` is in [FinalOf.lean](lean:Formalism/LocalToGlobal/PairingIndexBounds/RowActionCoefficients/FinalOf.lean#L15), and `admissible_general_lattice_tuple` in [AdmissibleGeneralLatticeTuple.lean](lean:Formalism/LocalToGlobal/PairingIndexBounds/RowActionCoefficients/AdmissibleInterpolation/AdmissibleGeneralLatticeTuple.lean#L17).

`adm7` at [FormalGroupSystem.lean](lean:Formalism/SharpRestriction/GrowthBounds/FormalGroupSystem.lean#L613) takes the datum as `_D` and does not use it. The module is named after the helper `lattice_shape_middle_holds` at line 18, not after the theorem.
