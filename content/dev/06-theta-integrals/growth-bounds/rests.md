---
id: rests
title: The four rest statements for an admitted system
kind: theorem
decl: Formalism.MainNotions.FormalGroupSystem.Pf.rests
module: Formalism.SharpRestriction.GrowthBounds.MultisetValuation.PrvAndKernelCommutationUpToUnitsOfRests
covers: 432
status: drafted
drafted_by: writer@claude
---
This theorem proves the four statements of the structure `Rests D X Y` for each admitted formal group system. [The eleven conclusions](/entry/packet-statements-hold/) give it to [the main assembly](/entry/prv-and-kernel-commutation-up-to-units-of-rests/), which uses the four fields as inputs. The theorem itself only collects four lemmas from other files.

## Statement

The objects `X : Sys p`, `Y : Pend X` and `admitted D X Y` are as in [the eleven conclusions](/entry/packet-statements-hold/). `Rests D X Y` is a structure with four fields:

- `S1 : Conclusion1 D X Y`,
- `allPlacesExpansion : ExpansionsMultiply D X Y`: for each field $K'$ over $K_c$ with an element $\varpi'$ such that $\varpi'^{p^2 - 1} = p$, there are integral elements $u$ such that `InProdA` holds for the series `ThA` at $\varpi'$ and for each family close to `hhA u` modulo $p$,
- `U2 : VolumeRatio₂ D X Y`: for each place $v$ and level $j < m$, the bound `LowAt j v` holds at the threshold `g0v v (j+1)`,
- `Ent : EntCondition X Y`: for $j < m$, if each place $v$ satisfies the place bound `PlaceB` with index $i_0(v)$ and threshold $g(v)$, then `EntB` holds with the threshold $\sum_v g(v)$.

`LowAt j v g` says: for each integral power series $U$, the coefficients of `applyD (PIv j I v)` applied to `ThZA` of $\exp(-\Phi_{j,v}) U$ satisfy `geC _ g`. Here `geC x g` means $x^b p^{-a} \in O_c$ whenever $a \le g b$. We have not unfolded `InProdA` or `EntB`.

**Theorem.** If `admitted D X Y`, then `Rests D X Y`.

## Proof

Each field has its own lemma.

- `S1` is `theta_kernel_expansion`, which is `baseChange_preserves_unitary_of` with `restBeta p` and `restGc p`.
- `allPlacesExpansion` is `expansions_multiply`, which is `expansion_all_places_of_computation` with `restBeta p` and `restGcA X`.
- `U2` is `first_theorem_place_bound`, applied to `hA` by `auxU_of_firstTheoremPlaceBound`. The place bound comes from `ea_A1U`.
- `Ent` is `restEnt_of`. It joins a placewise bound `LowAt j v (gv - alEven)` from `second_lemma_place_bound` and the bounds `LowAtI` for $1 \le i \le r$ from `hecke_place_bound`. It also uses `restPlaces`, which is built from `kernel_product_form`.

The shared input `restGc p` comes from `restTwoSums p`, which uses `sx_mu_alt`, `sx_dual`, `sx_frob_sum` and `frobenius_congruence_witt`. The jet input is `eb_brJet X`.

## In the Lean code

The theorem is in [PrvAndKernelCommutationUpToUnitsOfRests.lean](lean:Formalism/SharpRestriction/GrowthBounds/MultisetValuation/PrvAndKernelCommutationUpToUnitsOfRests.lean#L97) and the structure is at [line 70](lean:Formalism/SharpRestriction/GrowthBounds/MultisetValuation/PrvAndKernelCommutationUpToUnitsOfRests.lean#L70). The place bounds are in [FirstTheoremPlaceBound.lean](lean:Formalism/SharpRestriction/GrowthBounds/MultisetValuation/FirstTheoremPlaceBound.lean#L20).

- `auxU_of_firstTheoremPlaceBound` is `h hA`, because `EntryBoundOfHypotheses` is defined as `admitted D X Y → VolumeRatio₂ D X Y` ([line 56](lean:Formalism/SharpRestriction/GrowthBounds/MultisetValuation/AuxUOfFirstTheoremPlaceBound.lean#L56)).
- Two other theorems named `theta_kernel_expansion` exist, in LatticeSystems.lean and WittFrameLocaliserOrders.lean, with other statements.
