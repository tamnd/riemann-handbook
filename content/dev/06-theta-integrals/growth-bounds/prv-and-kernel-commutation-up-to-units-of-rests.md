---
id: prv-and-kernel-commutation-up-to-units-of-rests
title: The eleven conclusions and kernel commutation from the rests
kind: theorem
decl: Formalism.MainNotions.FormalGroupSystem.Pf.prv_and_kernel_commutation_up_to_units_of_rests
module: Formalism.SharpRestriction.GrowthBounds.MultisetValuation.PrvAndKernelCommutationUpToUnitsOfRests
covers: 375
status: drafted
drafted_by: writer@claude
---
This theorem assembles the eleven conclusions `Conclusion₂ D X Y` and the statement `KernelCommutationUpToUnits D X` from `admitted D X Y` and the four [rest statements](/entry/rests/). Its only user is [the eleven conclusions](/entry/packet-statements-hold/), which keeps the first part. The proof is a chain of lemmas from other files, in a fixed order.

## Statement

The notation is as in [the eleven conclusions](/entry/packet-statements-hold/). For each place $v$ the system gives maps $K_j$ from level $j$ to $j+1$, operators `ecal v i j`, an operator `Zop v u m` and numbers `qh v x`.

**Theorem.** If `admitted D X Y` and `Rests D X Y`, then `Conclusion₂ D X Y` and `KernelCommutationUpToUnits D X`.

`KernelCommutationUpToUnits D X` says: for each place $v$ there are $u_l, m_l \in K_f$ with `vEqK (u l) 0` and `vEqK (m l) (vm v l)` for $1 \le l \le m$, such that for each $j < m$, $i \in \mathbb{N}$ and $F$ in `FQ j`,
$$\mathcal{E}_{v,i}^{(j+1)}(K_j F) = u_{j+1}^{\,i} \, K_j\Big(\sum_{l=0}^{i} e_l\big(m_{j+1} q_v(0), \dots, m_{j+1} q_v(t)\big) \, \mathcal{E}_{v,i-l}^{(j)} F\Big),$$
with $e_l$ the elementary symmetric polynomial of degree $l$. It also gives an identity for `Zop` on the chain, two bounds on the coefficients `cl`, and a lower bound for `Zop` applied to $K_j G$. In these last parts $m$ is replaced by $\hat m_l = m_l (u_1 \cdots u_{l-1})^{-1}$.

## Proof

First `formB` gives `FormB X Y` and `heckeCondition_of_adm` gives `RestHecke X`, both from `admitted`. Then:

1. `hecke_integral_of_forms` gives `MassRatio₂` from `Ent` and `U2`.
2. `latticeChain_succ_of_partial` gives `PointsLemma`.
3. `alternate_expansion_of_relations` gives `KernelCommutationUpToUnits` from `RestHecke`, `PointsLemma`, `MassRatio₂` and the condition `adm3b`.
4. `theorem_of_alternate_form` gives `Conclusion4`. This is the last four parts of `KernelCommutationUpToUnits`, with $m$ in place of $\hat m$.
5. `LowTermBound` splits on $e_O$. If $e_O = 0$, the system has no places and `vGe` holds for every threshold, so a short argument from `Conclusion0` works. If $e_O > 0$, `lift_bound_of_integrality` uses `Conclusion4`, `Ent` and the condition `adm8`.

The other conclusions come from the rests or from one lemma each: `form_valuation_of_bound` (`Conclusion0`, with `adm3`), `slopeEstimate_of_lemmaB_slopeLine` (`Conclusion2`), `theorem_A_entries_of_corollary` (`projection_lemma_base_level`) and `ramifiedLattice_of_chain_estimates` (`Conclusion5`, from `U2` and `LowTermBound`). `Conclusion1`, `ExpansionsMultiply` and `VolumeRatio₂` are the fields of the rests.

## In the Lean code

The theorem is in [PrvAndKernelCommutationUpToUnitsOfRests.lean](lean:Formalism/SharpRestriction/GrowthBounds/MultisetValuation/PrvAndKernelCommutationUpToUnitsOfRests.lean#L80). `KernelCommutationUpToUnits` is in [FormalGroupSystem.lean](lean:Formalism/SharpRestriction/GrowthBounds/FormalGroupSystem.lean#L683). The case $e_O = 0$ is in the same file at [line 45](lean:Formalism/SharpRestriction/GrowthBounds/MultisetValuation/PrvAndKernelCommutationUpToUnitsOfRests.lean#L45).

- The case $e_O = 0$ cannot happen when a place exists, because `eO_pos` ([TheoremOfAlternateForm.lean](lean:Formalism/SharpRestriction/GrowthBounds/MultisetValuation/TheoremOfAlternateForm.lean#L618)) proves $e_O > 0$ from one place.
- The second output is dropped by the only caller. It is still used inside the proof, for `Conclusion4`.
- We have not unfolded `ecal`, `Zop`, `cl`, `FQ` or the proofs of the lemmas.
