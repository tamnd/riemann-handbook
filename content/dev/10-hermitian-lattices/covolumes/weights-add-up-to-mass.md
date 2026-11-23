---
id: weights-add-up-to-mass
title: The squared row weights over a genus sum to its mass
kind: theorem
decl: GlobalTheory.Unfold.SumK.weights_add_up_to_mass
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.UnfoldingGenusWeightsSumToMass
covers: 741
status: drafted
drafted_by: writer@claude
---
This theorem removes the two hypotheses of [`weights_add_up_to_mass_of`](/entry/weights-add-up-to-mass-of/) by two proved theorems. Its statement form is [`unfolding_genus_weights_sum_to_mass`](/entry/unfolding-genus-weights-sum-to-mass/), which [`rows_mass_genus`](/entry/rows-mass-genus/) uses. The content is in [`weights_add_up_to_mass_of`](/entry/weights-add-up-to-mass-of/).

## Statement

The conclusion of [`weights_add_up_to_mass_of`](/entry/weights-add-up-to-mass-of/), with the same hypotheses on the data, and without its two hypotheses $h_{\mathrm{Rel}}$ and $h_{\mathrm{Inv}}$:
$$\sum_{\kappa \in K} w(t_\kappa)^2 = \mathrm{mass}(d).$$

## Proof

Apply `weights_add_up_to_mass_of` to:

- `equivalence_complementUnitaryOrbit_localInnerDatum_at_place` (proved as `OrbitRel.relEqv`): at each place, the local orbit relation `Datum.Rel` is an equivalence relation. This is $h_{\mathrm{Rel}}$.
- `genus_stable_under_rationalComplementGroup` (proved as `GenusStab.inGen_of_gRel`): if $y$ lies over a lattice, $y$ is in the genus of $d$, and $h \in H_0$ moves $y$ to $y'$, then $y'$ is in the genus of $d$. This is $h_{\mathrm{Inv}}$.

There is nothing else.

## In the Lean code

The theorem is in [UnfoldingGenusWeightsSumToMass.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/UnfoldingGenusWeightsSumToMass.lean#L102). It is a term proof of one line. We have not opened the proofs `relEqv` and `inGen_of_gRel`, only their statement forms.
