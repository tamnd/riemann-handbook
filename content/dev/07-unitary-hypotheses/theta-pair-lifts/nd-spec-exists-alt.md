---
id: nd-spec-exists-alt
title: The Hecke localization of a datum exists
kind: theorem
decl: GlobalTheory.HeckeLocN.ndSpec_exists_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.NdSpecExists
covers: 324
status: drafted
drafted_by: writer@claude
---
This theorem builds the localization of the Hecke modules of a datum $D$ at their maximal ideals, over coefficient rings large enough to hold a given finite set of numbers. The result is a datum of type `NdSpec`. It is restated as [`side_rational_eigen_data_alt`](/entry/side-rational-eigen-data-alt/), which gives step 1 of [`locAll_exists_alt`](/entry/loc-all-exists-alt/).

## Statement

Let $D$, $A$, $M$, $C$ and `tp` be as in [`locAll_exists_alt`](/entry/loc-all-exists-alt/).

**Theorem.** Assume global Artin reciprocity, `HeckeStdPlain`, and the hypotheses 1 to 7 of [`locAll_exists_alt`](/entry/loc-all-exists-alt/). Then for each map `big` that gives a finite set of complex numbers at each place, there are a localization datum $X$, twist data $T$ over $X$, and a datum `NdSpec A.pl M C big X T`.

`HeckeStdPlain` says: for a CM field $L$, a weight, a level $J \subset \mathrm{GL}_n(\mathbb{A}_{L,f})$ and a character $\chi$ of $J$ trivial on a congruence subgroup, the Hecke operators $T_{s, \varpi, k}$ at good split places $s$ preserve the type space, are linear and commute, and for each eigenvalue $\mu$ and each prime $\ell$ that $s$ does not lie above, $d\mu$ is integral for some $d$ prime to $\ell$.

A datum `NdSpec` has these parts. Each index $i$ of $X$ carries a prime $\ell_i$, a ring $O_i$ and an embedding $\iota_i$ of its fraction field into $\overline{\mathbb{Q}}_{\ell_i}$; the image of $\iota_i$ reaches each number of `big`. A base $B$ carries a Hecke algebra $\mathbb{T}_{j,w}$ over a ring $O_{j,w}$. The indices at $(j, w)$ are in bijection with the maximal ideals $\mathfrak{m}$ of $\mathbb{T}_{j,w}$, and $O_i \cong O_{j,w}$. An injective map identifies the lattice of $i$ with the $\mathfrak{m}$-part of the module of $B$. The points of $i$ are the algebra maps $\mathbb{T}_{j,w} \to O_{j,w}$ with kernel class $\mathfrak{m}$ and a nonzero eigenspace.

## Proof

1. The conductor sets of $C$ satisfy `QOver` and `QConj` (`twistConductors_over_real_places_and_conj_stable`; we have not unfolded these two conditions). From them and `MtInput`, `heckeGeneratorPlacesOutsideLevel_of_stable` gives the condition `GenHyp` on the Hecke generator places.
2. With `HeckeStdPlain`, the double coset operators lift to coefficient-linear operators that commute (`exists_coefficientLinear_lift_doubleCosetOperators`, `liftedHeckeOperators_at_generators_commute`).
3. At each $w$ there are four finite extensions of $\mathbb{Q}_\ell$: one holds all Hecke eigenvalues, one holds the coefficient field and the numbers of `big`, one gives the local bridges, and one gives the ring maps for the twists. The coefficient datum is their compositum.
4. On the localized base, the Hecke ring is local, acts on the lattice (`ActEx`) and has nonzero eigenspaces at each point (`heckeRing_acts_faithfully_on_localisedLattice`, `localisation_heckeRing_isLocalRing`, `heckeEigenspace_ne_bot_every_localisation_point`).
5. From Artin reciprocity and `ChebSplit`, each twist character $\psi_w$, as a Galois character, is ramified at each place of its conductor set and is trivial on the decomposition groups above $\ell$ (`twistCharacter_ramified_at_conductor_trivial_above_l`).
6. `nonempty_spec` assembles the datum. The rest is bookkeeping on places.

## In the Lean code

The theorem is in [NdSpecExists.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/NdSpecExists.lean#L21). `NdSpec` is in [RingSpecNormalisedCharacterEq.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/RingSpecNormalisedCharacterEq.lean#L263), and `nonempty_spec` in [NonemptySpec.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/NonemptySpec.lean#L115).

- Two hypotheses are never used: the stability of $\mathrm{LL}_0$ under `star` and the integrality of `eExp`. The proof introduces them as `_ _` ([line 22](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/NdSpecExists.lean#L22)).
- The section `Psi` at lines 13 to 19 declares variables and no declaration.
- The older `ndSpec_exists` in [SideRationalEigenData.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/SideRationalEigenData.lean#L119) has the same shape, with `SideA` in place of `CharFrameHostEmbedding`.
- We have read the statements of the lemmas above, not their proofs.
