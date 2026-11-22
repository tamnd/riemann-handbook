---
id: global-theory-mi-star-row-alt-alt
title: The multiplicity row at the parameters of an extension
kind: theorem
decl: GlobalTheory.miStarRow_alt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.MainTheoremPublishedInputsThird
covers: 10940
status: drafted
drafted_by: writer@claude
---
This theorem gives two row statements about the period datum `MIstar2` at the parameters of a norm choice extension. Its only user is its renaming [`main_theorem_published_inputs_third_alt_alt`](/entry/main-theorem-published-inputs-third-alt-alt/), which supplies the multiplicity row and the divisor input of [branch 3](/entry/open-orbit-of-unramified-exponents-alt/). The work is below [`miStarRowClosing_alt_alt`](/entry/mi-star-row-closing-alt-alt/) and its renaming. This theorem fills in two of their hypotheses and changes the form of the conclusion.

## Statement

For a bundle $b$ write $X_b$ = `b.B.Q.Rl.toCx3 b.B.Q.F`. The predicate `MIstar2` for $b$ says: there is a datum $d = (V, a, U, \zeta)$, with $V$ a linear map of a complex space $E$, numbers $a(u) \in \mathbb C$, square matrices $U_u$ and numbers $\zeta(u, t) \in \mathbb C$, such that

- $V$ preserves a set `EEl true` and the norm on it, and each $U_u$ preserves a norm `fnorm`;
- $\zeta(u,t) \neq 0$, $\zeta(u, \mu_0) = 1$, and every element $k$ of the field with $\iota(k) = \zeta(u, \mu_w)$ has valuation $0$ at $w$;
- $a(u) \neq 0$ for all $u$;
- for all $u$, $t$, $\varphi$ and $F$: $\zeta(u,t)\, \iota\bigl(\mathrm{Pt}_{u,t}(\varphi, F)\bigr) = a(u)\, \bigl\langle s(V\, \Theta_t(j_t(e_t F))),\ P_u(U_u\, \iota\varphi) \bigr\rangle$.

Here $\iota$ is a complex embedding, $\Theta_t$ a theta map, $s$ the map `sEE` and $P_u$ a projection. We have not unfolded these objects.

**Theorem.** Assume fourteen named propositions: Harish-Chandra finiteness, rapid decay of cusp forms, `DiscreteSeriesCover`, Harish-Chandra modules, Casselman-Wallach, `HoweUnram`, the Weil representation of a unitary pair, the Weil-Siegel formula, `SiegelWeilUnitaryConvergent` (in `GlobalTheory.Published`), the doubling method, unramified doubling for $\mathrm{GL}$, the classification of discrete series, strong approximation for $\mathrm{SU}$, and a second `SiegelWeilUnitaryConvergent` (in `HeckeCharacterZeroLocus.SiegelWeilU`). Let $h_L$ prove `RecTExists`, $N$ be a norm choice extension, $S$ an S-extension and $\Gamma$ a geometry, and let $p$ be their parameters. Then

1. `LinkedAt p` of the row "`MIstar2` holds at every bundle of every admissible selection";
2. `LinkedAt p RowMultiplicityCondition`: the same, in the closed sense and eventually in $x$ (`Ind.EvW`).

## Proof

1. `diagonalRow_of_siegelWeil_unitary` turns the second Siegel-Weil hypothesis into the diagonal row `RowDiag` of scale and rank facts.
2. Each weighted point $q$ of $p$ carries a field `rx`, which gives the hypothesis `Nonempty (RXs …)`.
3. With these two inputs and the other thirteen hypotheses, [`main_theorem_published_inputs_variant_alt_alt`](/entry/main-theorem-published-inputs-variant-alt-alt/) gives `RowE` of `MIstar2`: for large parameters, at each point of the slot `IsGoodE` and each bundle that `BundleLinkage p` links to it, `MIstar2` holds.
4. `RowE.row` turns this into a `Row` with `AtAll`, and `LinkedAt.of_row` into part 1.
5. `evW_of_atAll` weakens "at all $x$" to "eventually in $x$", and `LinkedAt.of_row` gives part 2.

## In the Lean code

The theorem is in [MainTheoremPublishedInputsThird.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MainTheoremPublishedInputsThird.lean#L22). `MIstar2` is in [IsometricPeriodsOfUnitHypotheses.lean](lean:Formalism/LocalToGlobal/IndefiniteReal/IsometricPeriodsOfUnitHypotheses.lean#L27), and its parts `MIDat`, `MIid` and `AuNZ` in [IsometricPeriodsOfHypotheses.lean](lean:Formalism/LocalToGlobal/IndefiniteReal/IsometricPeriodsOfHypotheses.lean#L80). `RowMultiplicityCondition` and `LinkedAt.of_row` are in [RowGood.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/RowGood.lean#L33), `RowE.row` in [ValidForConstructedPointClassesEventuallyWorking.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/ValidForConstructedPointClassesEventuallyWorking.lean#L328), and `evW_of_atAll` in [RowOfCovolumeOntoGrid.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/RowOfCovolumeOntoGrid.lean#L51).

Part 2 follows from part 1, so the statement repeats itself in a weaker form. The two Siegel-Weil hypotheses have the same last name but different statements: the first is about Weil data and Fock vectors for a pair of Hermitian spaces, the second about nondegenerate Hermitian matrices over a CM extension. The name "multiplicity" is the Lean name of the row. The predicate is an identity between a period and an inner product with nonzero constants. We do not claim more than that.
