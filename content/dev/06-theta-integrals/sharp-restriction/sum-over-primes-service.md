---
id: sum-over-primes-service
title: The service bounds for a closed class of families
kind: theorem
decl: Formalism.MainNotions.Pk.sum_over_primes_service
module: Formalism.SharpRestriction.SmoothDesignExistence.SumOverPrimesHypotheses
covers: 1747
status: drafted
drafted_by: writer@claude
---
This theorem proves the family statement `ServF` for all large families of a class $\mathcal{C}$, from a size bound and the two fields of the structure `SumOverPrimesHypotheses`. Its only user is [`closed_servF_of_servT_of_dGamSize`](/entry/closed-serv-f-of-serv-t-of-d-gam-size/), which builds the structure from a twist selection. Its result fills the field `serv` in [`closed_family_admissible_twist_link_alt`](/entry/closed-family-admissible-twist-link-alt/), on the way to [the shape theorem from Green](/entry/shape-closed-link-n-of-green/) and the branch [ZeroFreeAll from Green, VWin and HypsAlt](/step/zero-free-all-of-green-v-win/).

## Statement

A family `FamP ε` gives, for each large $x$ and each index $i$, a datum $D_{x,i}$ of type `D7`, size data $L_{x,i}$ and further choices. A class $\mathcal{C}$ is a predicate on families. As in [the definition Closed](/step/closed-def/), `Closed 𝒞 P` means: there is $\varepsilon_1 > 0$ such that for each $\varepsilon \in (0, \varepsilon_1]$ there are thresholds $K$ with $P(F_m, C_H)$ for each family $F_m \in \mathcal{C}$ whose constants are above $K$.

- `DGamSize Fm`: there are $C$ and $x_0$ such that for $x \ge x_0$, each $i$ and each word $u$, $\log \Delta_\Gamma(u) \le C f N_m \log(f N_m)$, where $\Delta_\Gamma(u)$ is the number `DGam` of the member $u$ of $D_{x,i}$ and $f$, $N_m$ are ranks of $D_{x,i}$.
- `ServF Fm`: there are $C \ge 0$ and $x_0$ such that for $x \ge x_0$ and each $i$ the statement `Serv` holds. `Serv` is a conjunction of three parts: `TypePrimeSizeConds` (size bounds over sets of small primes), `Conclusion1` (valuation lower bounds on columns at good places), and `ColumnValuationAwayFromTypePrimes`.
- `SumOverPrimesHypotheses 𝒞` has two closed fields. `twU` gives, for large $x$, a choice `LC` of levels and chains with a comparison `CmpV` and the system statement `SysTw`: for each used $\mu$, word $u$ and place $w$, an admitted formal group system with low bounds `LowAt` whose sum controls `lowS`. `pdv` gives a kernel entry $E$ with four unit and rationality conditions and six orbit conditions (`EvenConditionsInert`, `JetIntegralityBis`, `Shape` and others).

**Theorem.** If `Closed 𝒞 DGamSize` and `SumOverPrimesHypotheses 𝒞`, then `Closed 𝒞 ServF`.

## Proof

Fix a family and large $x$, $i$.

1. `closed_large_pos` joins the closed inputs `hD`, `twU`, `pdv` and `num_closed` (the numerical comparison `NumCmpF`).
2. `admissible_size_family` gives `TypePrimeSizeConds` from `DGamSize`.
3. From `twU`, `G.Joints.unit_bound_of_sum_over_primes` gives the unit bound at twisted places. It also uses the proved `FormalGroupSystem.Pf.stmt_proved`.
4. From `pdv`, the proof builds `OrbitPlaces.admitted`. It needs $\mathrm{splitBound} \ge 3$, which `three_le_split` gives for $x \ge 3^{5/e_z}$, and then `orbit_admissible_of_split_bound`, `typeG_ne_d`, `theta_isometry_facts_hold`, `kform_of_ker` and `split_bound_eleven_one`. Then `four_orbit_conditions_of_proof` and `orbit_entry_bounds_hold` give four more conditions.
5. With `local_theorem_of_statement`, these make `WeilJacquetShalikaLaw.admitted`, six conditions. `serv_of` applies the proved statement `WeilJacquetShalikaLaw.Proof.stmt_proved` to it and gives `Serv` for the lattice instance with the new choice `LC`. `serv_re` moves `Serv` back to the original instance.

The rest is bookkeeping with maxima of thresholds.

## In the Lean code

The theorem is in [SumOverPrimesHypotheses.lean](lean:Formalism/SharpRestriction/SmoothDesignExistence/SumOverPrimesHypotheses.lean#L187), and the structure is at [line 132](lean:Formalism/SharpRestriction/SmoothDesignExistence/SumOverPrimesHypotheses.lean#L132). `ServF` and `Serv` are in [WeilJacquetShalikaLaw.lean](lean:Formalism/SharpRestriction/GrowthBounds/WeilJacquetShalikaLaw.lean#L241). `Closed` and `DGamSize` are in [ParamsHeightRankConstant.lean](lean:Formalism/SharpRestriction/ParamsHeightRankConstant.lean#L159).

Odd points:

- `closed_large_pos` is called with all thresholds $0$, and the proof never uses the largeness hypothesis `hL` that it gets. So the step acts as `Closed.imp`.
- `num_closed` ignores its hypothesis `_hN` ([PlaneCountTheoremWithConstants.lean](lean:Formalism/SharpRestriction/GrowthBounds/PlaneCountTheoremWithConstants.lean#L1833)). The term `stmtNumE` passed to it does no work.
- The namespace `WeilJacquetShalikaLaw` and the name "sum over primes" do not name a published result that we could identify. We have not unfolded `Conclusion1`, `SysTw` or the six orbit conditions past their first level.
