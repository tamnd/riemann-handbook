---
id: row-weights-local-orbits-sum-eq-genus-mass
title: The row weights over one local orbit sum to a genus mass, statement form
kind: theorem
decl: GlobalTheory.T.rowWeights_localOrbits_sum_eq_genusMass
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.RowWeightsLocalOrbitsSumEqGenusMassStatement
covers: 774
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`rows_mass_genus`](/entry/rows-mass-genus/). It has two users, `tied_mass_law` and `unfold_tied`, in the files MatchedFamilyMassLawBaseSituation.lean and UnfoldingIdentityMatchedFamilyClosedTerms.lean. Both are below the step [HypsAlt is nonempty](/step/nonempty-hyps/). The content is in [`rows_mass_genus`](/entry/rows-mass-genus/) and, for the counting, in [`weights_add_up_to_mass_of`](/entry/weights-add-up-to-mass-of/).

## Statement

The statement is word for word that of [`rows_mass_genus`](/entry/rows-mass-genus/). Let $F_m$ be a local family tied to a set $T_S$ of terms at one point, and let $d$ be one tuple of its local data. Then the sum of the weights $\mathrm{rw}(c)$ over the pairs (class, double coset) with local data $d$ is the mass of the genus of the global datum $\bar d$ that is $d$ on $P$ and the base datum off $P$:
$$\sum_{(c, n) :\ \mathrm{dat}(c, n) = d} \mathrm{rw}(c) = \sum_{[y] \subseteq \mathrm{genus}(\bar d)} \frac{1}{\lvert \mathrm{Stab}_{H_0}(y) \rvert}.$$
Also each $\bar d_p$ has a term over it. The hypotheses and the objects are in [that entry](/entry/rows-mass-genus/).

## Proof

The proof is the term `GlobalTheory.Unfold.GenusRows.rows_mass_genus`. There is nothing else.

## In the Lean code

The theorem is at [RowWeightsLocalOrbitsSumEqGenusMassStatement.lean line 10](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/RowWeightsLocalOrbitsSumEqGenusMassStatement.lean#L10). The proof is a tactic `first | exact @… | exact … | (intros; apply … <;> assumption)` with `maxHeartbeats` set to 1,000,000. The two statements are the same, so the first alternative fits.
