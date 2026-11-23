---
id: is-const-along-of-ks-zero
title: Constant degeneration data from a vanishing Kodaira-Spencer matrix, by heat operators
kind: theorem
decl: GlobalTheory.KSConst.isConstAlong_of_ks_zero
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.IsConstAlongOfKodairaSpencerZeroChart
covers: 306
status: drafted
drafted_by: writer@claude
---
This theorem proves [the statement form](/entry/is-const-along-of-kodaira-spencer-zero-chart/), which [`isConstAlong_of_ks_mem`](/entry/is-const-along-of-ks-mem/) applies on a boundary chart. The chain above ends in the injectivity of the log Kodaira-Spencer map at boundary points, [`logKS_inj_mod_boundary`](/entry/log-ks-inj-mod-boundary/). The proof goes through a heat operator that lifts the derivation $D$ to the Raynaud extension.

## Statement

The statement is that of [the statement form](/entry/is-const-along-of-kodaira-spencer-zero-chart/). On $R_k = k[[t, u]]$, with $\operatorname{char} k = 0$, a semi-abelian $G$ with degeneration data $P$ and monomial forms $\gamma_i$: if $D(t_i) = q_i t_i$ and the Kodaira-Spencer matrix $\Theta$ of $D$ is $0$ modulo the maximal ideal, then the degeneration data are constant along $\rho(r) = r(0) + \varepsilon \, (D r)(0)$ with rates $c \, q_i(0)$ for some rational $c \neq 0$.

**Heat operators.** Let $H \to A$ be a Raynaud extension of $P$ (the Lean structure `Ray`: a group scheme over $R_k$ whose points are given by `GtPt`, with an action of $\mathcal O_E$), with vector fields $\partial_1, \dots, \partial_{n'}$ on $H$. A heat operator for $D$ (`Heat`) is a symmetric matrix $\Theta^h$, a vector $u$, and an open cover $(W_i)$ of $H$ with derivations $d_i$ on $W_i$ that lift $D$ and functions $p_i, p'_i$, such that for each $k \geq 0$ the operators

$$2k\, d_i - \sum_{a,b} \Theta^h_{ab} \partial_a \partial_b + 2 \sum_a u_a \partial_a + 2k^2 p_i + 2k p'_i$$

glue to an operator on the $k$-th power of the pullback of the line bundle $L$ of $P$. `IsBasic` says that the cover comes from $A$ and that the $p_i$, $p'_i$ and the $d_i$ respect the weights of the torus action. `HasDefect Y h 0` says that the operator commutes with the shift of theta sections by periods, with zero defect. We call $\Theta^h$ the symbol.

## Proof

1. `MumfordChart.admissibleBase_chartRing`: $R_k$ is Noetherian and complete. A Raynaud extension $H$ exists (an instance of `Nonempty (Ray _)`).
2. `T.exists_basis_raynaudTangent_invariantFields`: the tangent module of $H$ has a basis $v'$ with invariant vector fields $\partial_a$.
3. [`T.exists_torusInvariant_heatOperator_commuting_periods`](/entry/exists-torus-invariant-heat-operator-commuting-periods/): since $D(t_i) \in (t_i)$ and $t_i \neq 0$, there is a heat operator $h$ for $D$ with `IsBasic` and zero defect.
4. `T.heat_symbol_mem_maximalIdeal_of_kodairaSpencer_zero`: if $\Theta \equiv 0$ modulo the maximal ideal, then the symbol $\Theta^h \equiv 0$ too. This step takes both the frame $v$ of $G$ and the frame $v'$ of $H$.
5. `T.degenerationData_constant_of_flat_heatOperators`: a basic heat operator with zero defect and symbol $0$ modulo the maximal ideal gives `IsConstAlong` for $\rho$ with rates $c \, q_i(0)$, $c \in \mathbb{Q}^\times$.

The rest is bookkeeping: the proof rebuilds $D$ as a derivation from its four laws, to match the form that step 3 takes.

Heat operators on theta functions appear in G. E. Welters, "Polarized abelian varieties and the heat equations", Compositio Math. 49 (1983). We have not compared his definitions with these.

## In the Lean code

The theorem is in [IsConstAlongOfKodairaSpencerZeroChart.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsConstAlongOfKodairaSpencerZeroChart.lean#L26). `Heat`, `IsBasic` and `HasDefect` are in [HasDefect.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/HasDefect.lean#L58); `Ray` is in [IsLinearHomPull.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/IsLinearHomPull.lean#L25). We read the statements of steps 2 to 5, not their proofs.

The instance `Nonempty (Ray oa)` is proved from `GlobalTheory.allSixLaws`, which we have not opened.
