---
id: unfolding-genus-weights-sum-to-mass
title: The squared row weights over a genus sum to its mass, statement form
kind: theorem
decl: GlobalTheory.T.unfolding_genus_weights_sum_to_mass
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.UnfoldingGenusWeightsSumToMassStatement
covers: 742
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`weights_add_up_to_mass`](/entry/weights-add-up-to-mass/). Its user is [`rows_mass_genus`](/entry/rows-mass-genus/), in the last step of its proof. The content is in [`weights_add_up_to_mass_of`](/entry/weights-add-up-to-mass-of/).

## Statement

The statement is word for word that of [`weights_add_up_to_mass`](/entry/weights-add-up-to-mass/). In short: let $T_S$ be a set of terms that is closed under local moves of the term lattice, and $d$ a global datum whose genus contains the local data of one term of $T_S$. Let $K$ be the set of keys $(j(t), \nu(t))$ (row, double coset) of the terms $t \in T_S$ whose moved lattice has local data in the genus of $d$. Then
$$\sum_{\kappa \in K} w(t_\kappa)^2 = \mathrm{mass}(d),$$
where $t_\kappa$ is any term with key $\kappa$ and $\mathrm{mass}$ is defined in [the entry for `rows_mass_genus`](/entry/rows-mass-genus/). The hypotheses are stated in [the entry for `weights_add_up_to_mass_of`](/entry/weights-add-up-to-mass-of/).

## Proof

The proof is the term `GlobalTheory.Unfold.SumK.weights_add_up_to_mass`. There is nothing else.

## In the Lean code

The theorem is at [UnfoldingGenusWeightsSumToMassStatement.lean line 10](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/UnfoldingGenusWeightsSumToMassStatement.lean#L10). The proof is a tactic `first | exact @… | exact … | (intros; apply … <;> assumption)` with `maxHeartbeats` set to 1,000,000. The two statements are the same, so the first alternative fits.
