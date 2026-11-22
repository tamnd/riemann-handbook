---
id: packet-statements-hold
title: The eleven conclusions for an admitted formal group system
kind: theorem
decl: Formalism.MainNotions.FormalGroupSystem.Pf.packet_statements_hold
module: Formalism.SharpRestriction.GrowthBounds.MultisetValuation.PrvAndKernelCommutationUpToUnitsOfRests
covers: 821
status: drafted
drafted_by: writer@claude
---
This theorem proves `Conclusion₂ D X Y` for each admitted formal group system. It is a projection: it takes the first half of [the conclusions and kernel commutation from the rests](/entry/prv-and-kernel-commutation-up-to-units-of-rests/) and feeds it [the rests](/entry/rests/). Its users are `stmt_proved` and `stmtAt_proved` in the same file. Through `stmt_proved` it reaches [the service bounds](/entry/sum-over-primes-service/), which call `G.Joints.unit_bound_of_sum_over_primes` with it.

## Statement

Let $D$ be a datum of type `D7` and $p$ a prime. A system `X : Sys p` has a group datum `G` at $p$ with a ring $O$ and its fraction field $K_f$, a chain of levels $j = 0, \dots, m$ with $O$-lattices $\mathrm{Int}_j$ and $K_f$-linear maps $K_j$ from level $j$ to $j+1$, a uniformizer $\varpi$ and an integer $e_O$ with $p \sim \varpi^{e_O}$. `X.vGe j F g` says $F \in \varpi^{\lceil g e_O \rceil} \mathrm{Int}_j$. A datum `Y : Pend X` adds a valued field $K_c$ with valuation ring $O_c$, power series on pairs of lattice tuples at adjacent levels, and kernel maps. `admitted D X Y` is a conjunction of 13 conditions.

**Theorem.** If `admitted D X Y`, then `Conclusion₂ D X Y`.

`Conclusion₂` is a conjunction of 11 statements: `Conclusion0` and `Conclusion2` (lower bounds for $v(K_j G)$, $G \in \mathrm{Int}_j$), `Conclusion1`, `ExpansionsMultiply`, `projection_lemma_base_level`, `VolumeRatio₂` (lower bounds for the theta series), `MassRatio₂`, `PointsLemma`, `Conclusion4` (bounds after an operator `Zop` at one place), `Conclusion5` and `LowTermBound` (bounds at the top level $m$).

## Proof

The term is `(prv_and_kernel_commutation_up_to_units_of_rests D Y hA (rests D Y hA)).1`. [`rests`](/entry/rests/) proves four auxiliary statements from `admitted`. [`prv_and_kernel_commutation_up_to_units_of_rests`](/entry/prv-and-kernel-commutation-up-to-units-of-rests/) proves the 11 statements and `KernelCommutationUpToUnits`; this theorem keeps the first part. The real content is in those two entries.

## In the Lean code

The theorem is in [PrvAndKernelCommutationUpToUnitsOfRests.lean](lean:Formalism/SharpRestriction/GrowthBounds/MultisetValuation/PrvAndKernelCommutationUpToUnitsOfRests.lean#L104). `Sys` is in [FormalGroupSystem.lean](lean:Formalism/SharpRestriction/GrowthBounds/FormalGroupSystem.lean#L264), `Pend` at line 447, `admitted` at line 771 and `Conclusion₂` at line 775.

- Most of the conditions and conclusions take $D$ as an unused argument `_D`.
- The same file defines `Sys.Conclusion₂`, a real number (line 327), next to the proposition `Conclusion₂`. `Conclusion5` and `LowTermBound` use the real number.
- The name "packet statements" does not match a notion in the statement.
