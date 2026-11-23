---
id: series-rat-s-and-ser-int-of-global-artin
title: Rationality and integrality of theta series, given global Artin reciprocity
kind: theorem
decl: GlobalTheory.seriesRatS_and_serInt_of_globalArtin
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.SeriesRationalIntegral
covers: 714
status: drafted
drafted_by: writer@claude
---
This theorem pairs two results on theta series: rationality, which needs global Artin reciprocity, and integrality, which needs nothing. It is below the step [nonempty hypotheses](/step/nonempty-hyps/). Its callers, such as `ontoX_of_hypotheses_alt_alt`, use the rationality half. The real content is in the two theorems that it calls.

## Statement

`GlobalArtinReciprocity` says: for each number field $K$ with an algebraic closure, there is a continuous map from the idèles of $K$ onto the abelianized Galois group that is an open quotient map, whose kernel is the closure of $K^\times$ times the connected component at infinity, and which matches inertia, Frobenius and decomposition groups at each finite place. This is the main theorem of global class field theory (Neukirch, *Algebraic Number Theory*, Chapter VI).

`SeriesRatS` says: for each datum of type `D7` with its laws, there is a constant $\varphi$ with $|\varphi| = 1$ such that on each good cover the theta series $\varphi\,\theta$ is rational, and so are its products with the twist functions. `SerInt` says that the twisted theta series are integral up to a power $\ell^c$, uniformly over the covers of a tower, and that integral forms descend.

**Theorem.** `GlobalArtinReciprocity` implies `SeriesRatS` and `SerInt`.

## Proof

1. `GlobalArtinReciprocity.rayClassFieldSt` turns the idèlic map into ray class fields: for each modulus $\mathfrak{m} \ne 0$ there is an abelian extension $L/K$ with an isomorphism from the ray class group mod $\mathfrak{m}$ to $\mathrm{Gal}(L/K)$, unramified outside $\mathfrak{m}$, sending the class of $\mathfrak{p}$ to its Frobenius.
2. `T.thetaSeriesRationalOnGoodCovers_of_untwisted` takes the ray class fields and the untwisted rationality `T.untwisted_theta_rational_on_good_covers`, and gives `SeriesRatS`.
3. `T.thetaSeries_integral_uniform_prime_power` gives `SerInt` with no hypothesis.

## In the Lean code

The theorem is in [SeriesRationalIntegral.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/SeriesRationalIntegral.lean#L12). `GlobalArtinReciprocity` is in [ExistsUniqueHcharOfFiniteOrder.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/ExistsUniqueHcharOfFiniteOrder.lean#L70). `SeriesRatS` is in [SeriesRatSOf.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/SeriesRatSOf.lean#L14). We have not unfolded the theta series, the good covers or the twist functions.

The hypothesis is used only for the first half. The callers [OntoXOfPrints.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OntoXOfPrints.lean#L34) and [PublishedInputsImplyGalois.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/PublishedInputsImplyGalois.lean#L44) take only the first half. In `ontoX_of_hypotheses_alt_alt` the hypothesis comes from the literature input `HeckeLAdicCharacter`, through `HeckeLAdicCharacter.globalArtin`. The file is in a folder named after the Iwasawa decomposition, but no Iwasawa decomposition appears in the statement.
