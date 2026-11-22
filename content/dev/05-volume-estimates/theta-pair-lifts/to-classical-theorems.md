---
id: to-classical-theorems
title: The classical inputs from the published bundle, with Mumford proportionality
kind: theorem
decl: GlobalTheory.CovTop.PublishedHodgeBundleTheorems.toClassicalTheorems
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.HodgeBundleWeights.CoveringTopologyRefinement
covers: 1342
status: drafted
drafted_by: writer@claude
---
This theorem turns the 28-field bundle [PublishedHodgeBundleTheorems](/step/published-results-arithmetic/) into the smaller bundle `Hypotheses''` of 17 classical statements. Its only real step is to derive a proportionality statement for Shimura varieties of unitary type from a statement on good metrics. Its two callers are `covering_topology_refinement`, a restatement in the same file, and `hodgeLineBundle_isBig`, through `isNef_hodgeBundle_unitWeight`. Both are below [the covolume bound from heights](/entry/top-covol-g-alt-alt/). Below this theorem are 1,342 declarations, nearly all under the proportionality step.

## Statement

**Theorem.** If $\mathsf{PublishedHodgeBundleTheorems}$ holds, then $\mathsf{Hypotheses''}$ holds.

$\mathsf{Hypotheses''}$ is a structure of type `Prop`. Fifteen of its 17 fields have the same names and types as fields of the bundle (toroidal compactification, volumes, arithmetic intersection, class field theory, strong approximation for $\mathrm{SU}$, and others). The other two are:

- `p18`, `FinitenessOfHermitianClasses`: for a CM field $E$ and a nondegenerate hermitian matrix $G$ over $E$, each family of $\mathcal{O}_E$-lattices whose dual is a fixed fractional ideal times the lattice, with marked vectors, has a finite set of representatives: a unitary $\gamma$ maps each lattice onto a representative, with the marked vectors matched modulo $\mathfrak{m}$ times the lattice, for a fixed nonzero ideal $\mathfrak{m}$;
- `p16`, `MumfordProportionality`: for a CM field, a unitary datum of signature $(p, q)$, a level, an integral model with a toroidal model, an embedding into $\mathbb{C}$ and a good unfolding $U$, each flag component $k$ and each weight $\lambda$ satisfy
$$(L_\lambda^{\dim Y_k}) = \operatorname{covol}(U_k)\cdot \operatorname{flagDeg}(\Psi_H, p+q, \lambda).$$
So the self-intersection number of the automorphic line bundle $L_\lambda$ is the covolume times a degree on the flag variety. By its name and form, this is Hirzebruch proportionality in Mumford's non-compact form (D. Mumford, Hirzebruch's proportionality theorem in the non-compact case, Invent. Math. 42 (1977), 239 to 272).

In the bundle, field `p16` is instead `GoodChernWeil`, the conjunction of two statements. `GoodChernNumbers` says that for a frame with a good metric (in the sense of `IsGood`) on a variety, refined to a graded frame on a flag bundle, Chern integrals equal intersection numbers on the flag bundle. `FlagPushForward` says that two polynomials in the Chern roots with the same antisymmetrisation, up to the root discriminant, give the same intersection numbers.

## Proof

The theorem is `toClassicalTheoremsOf` applied to `toroidalFlagProportionality_of_goodChernWeil`, which is `mumfordProportionality_of_goodChernWeil`.

1. Fifteen fields are copied from the bundle.
2. `p18` comes from `finitenessOfHermitianClasses_holds`, a proof in the code that does not use the bundle.
3. `p16`: fix the data, $k$ and $\lambda$. `exists_goodBase` gives a base variety with a frame, a refinement to the graded frame of the flag component, and a good metric (`hodgeMetric_lieGram_isGood_mumford`) whose Chern integral is $\operatorname{covol}(U_k)\,\operatorname{flagDeg}$ (`hodgeMetric_chernIntegral_eq_covolume_mul_flagDegree`). `selfInter_Lw_interPoly` writes $(L_\lambda^{\dim})$ as the intersection number of a power of a linear form in the Chern roots. `antisymm_eq_chernRoots_mul_rootDiscr` writes its antisymmetrisation as a symmetric polynomial times the root discriminant. Then `GoodChernWeil.flag` says that this intersection number is also the same Chern integral. A Chern integral is unique (`hasChernIntegral_unique`), so the two values are equal.

## In the Lean code

The theorem is at [CoveringTopologyRefinement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/CoveringTopologyRefinement.lean#L10). It is a one-line term. The work is in [ToKnownTheoremsOf.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/ToKnownTheoremsOf.lean#L39) and [ToroidalFlagProportionalityOfGoodChernWeil.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ToroidalFlagProportionalityOfGoodChernWeil.lean#L19).

- For `p16`, `toClassicalTheoremsOf` tries `exact h.p16`, which fails on the type, then `exact hM'`.
- The 12 `q` fields of the bundle (`q1` Grothendieck-Messing to `q18` formal algebraisation) are not used. `p16` is used only through the proportionality step.
- We have not unfolded `IsGood`, `HasChernIntegral`, `flagDeg`, or the two `hodgeMetric_` lemmas, so we do not claim that the Lean metric is Mumford's good metric.
