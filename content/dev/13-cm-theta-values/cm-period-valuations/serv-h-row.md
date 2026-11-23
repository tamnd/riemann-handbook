---
id: serv-h-row
title: The service row from six hypotheses
kind: theorem
decl: GlobalTheory.Svd.servH_row
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.BundleBothPartsOfStandardKernelAndSixHypotheses
covers: 5805
status: drafted
drafted_by: writer@claude
---
This theorem proves the service row `ServH` from six hypotheses about elliptic curves, formal groups and kernels at inert primes. Its user is the renaming [`bundle_bothParts_of_standardKernel_and_six_hypotheses`](/entry/bundle-both-parts-of-standard-kernel-and-six-hypotheses/), and through it [`servH_row_of_artin`](/entry/serv-h-row-of-artin/), which gets the six hypotheses from global Artin reciprocity.

## Statement

In each hypothesis, $D$ is a datum (`D7`), $\mathfrak c$ is an ideal of the ring of integers of the field $K$ of $D$ with `IsCurveIdeal`, $\delta \in \mathbb C$ satisfies `IsDiscriminantTwelfthRootOfIdealLattice`, and $\lambda \colon \overline{\mathbb Q} \to \mathbb C_p$ is an embedding. We give the shape of each hypothesis. We have not unfolded the predicates inside them.

1. `AlgTAll`: for each base $B$ over $(D, \mathfrak c, \delta)$ and each character $\chi$ with `IsChi`, the property `B.AlgT χ` holds.
2. `GenusOneModelExistsLattice`: for each prime $p \ge 5$ with `InertK D p` and each $\lambda$, there are $(\mathfrak c', \delta')$ with the same value of `lamOf` and a datum $g$ over $\lambda$ with `At D 𝔠' δ' g`, a model over the Witt vectors (`ModelOverW`) and an isomorphism `LTIso g`.
3. `CurveDict`: for such $g$ at a prime $\ell \ge 5$, there are $g_2, g_3, \varepsilon, s_2$ in the maximal unramified extension, with $g_2, g_3$ the Weierstrass invariants of $g$, a rescaling identity between two power series, a unit norm condition, `CurveAt`, and a dictionary `DictInt` for every datum.
4. `IntInert`: for each base $B$, character $\chi$, prime $p \ge 5$ with $\left(\frac{-d}{p}\right) = -1$, each $\lambda$ and each admitted pair of lattices $L, L'$, certain power series built from a curve model and an orthonormal local basis are integral (`IntFirst`).
5. `AdmAtEnt2`: for each tied kernel entry and each choice of chain data at a place $w$, if a list of conditions holds (`CurveIn`, `ThetaSeriesDataHypothesesBelowMaximalLevel`, `XiIn`, `LawInLt` and ties `TiesAt`), then the pending system at $w$ is `admitted`.
6. `CurveEx`: for each base $B$, character $\chi$, prime $p \ge 5$ prime to the norm of $\mathfrak c$ with `InertK D p`, and each $\lambda$, there is $g$ with `LTIso g` and `CurveIn D p 𝔠 δ g B χ λ`.

**Theorem.** Assume the six hypotheses. Let $Q$, $L_k$ and `ker` be as in [`servH_row_of_artin`](/entry/serv-h-row-of-artin/). Suppose that every point of $Q$ is in `positionOf HasPart`, and that `RowE` holds for "`ker b` has a standard tie" (`StdTie`). Then `Row Q Lk (ServH ker)`.

## Proof

1. **Local models.** For every point $\beta$ of $Q$, [`tuplesHaveLocalModels_at_constructedPoint_over_trueColumns`](/entry/tuples-have-local-models-at-constructed-point-over-true-columns/) (2,860 declarations) gives `ModelsAt β.D β.O` from `AdmAtEnt2`, `CurveEx` and the first side condition. `RowE.of_all` makes this a row condition for all parameters.
2. **First part.** `rowTwU` turns the row of local models into `Row Q Lk (Closed 𝒜 RowTwU)`.
3. **Second part.** [`rowAt_of_stdTie`](/entry/row-at-of-std-tie/) (2,327 declarations) uses `AlgTAll`, `GenusOneModelExistsLattice`, `CurveDict`, `IntInert` and the second side condition. It gives the row in which the kernel entry of each selected bundle satisfies `Pdv.At`.
4. `Row.and` joins the two rows. Their conjunction is `ServH ker` by definition.

## In the Lean code

The theorem is at [BundleBothPartsOfStandardKernelAndSixHypotheses.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/BundleBothPartsOfStandardKernelAndSixHypotheses.lean#L15). The lemmas it calls:

- `tuplesHaveLocalModels_at_constructedPoint_over_trueColumns`, a renaming of [`modelsAt_bpt`](/entry/models-at-bpt/);
- `rowTwU` in [RowTwUHolds.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/RowTwUHolds.lean#L15);
- `rowAt_of_stdTie` in [RowAtOfStdTie.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/RowAtOfStdTie.lean#L13);
- `RowE.of_all` and `Row.and`, general facts about rows.

Each hypothesis is used: two in the first part, four in the second. The proof of `rowTwU` proves `Closed` with $\varepsilon_1 = 1$ and a threshold record of zeros, so the first part needs no large constants. `AdmAtEnt2` is defined twice with the same body, in `GlobalTheory.TwV.Lt` ([ThetaSeriesDataHypothesesBelowMaximalLevel.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/ThetaSeriesDataHypothesesBelowMaximalLevel.lean#L106)) and in `Formalism.L2.KerInert.AdmLoc2`; this theorem uses the first.
