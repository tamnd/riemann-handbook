---
id: log-canonical-pair-iff
title: Cusp forms as canonical forms on a smooth model
kind: theorem
decl: GlobalTheory.LogCanon.log_canonical_pair_iff
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.HodgeBundleWeights.LogCanonicalCriterionBoundary
covers: 358
status: drafted
drafted_by: writer@claude
---
This theorem says that cusp forms of weight $\kappa + b$ on a toroidal flag space are the global sections of $K_{X'} \otimes L(b)$ on any smooth projective model $X'$. Its only user is its second name [log_canonical_criterion_boundary](/entry/log-canonical-criterion-boundary/), which is below [the covolume bound](/entry/top-covol-g-alt-alt/). The proof reduces to the flag space itself, where [logCanonical_divisor_refl](/entry/log-canonical-divisor-refl/) does the work. Below this theorem are 358 declarations.

## Statement

Let $E$ be a CM field, and let $\bar X$ (the Lean `Y₀`) be the part of a toroidal flag space `TF` over the closure of a connected component $Z$. It is smooth of relative dimension $n$ (`dimFlag`) over the coefficient field $F$. Let $U \subseteq \bar X$ be the interior (`U₀`), which is dense, and $D$ its complement. For a weight $\lambda$, $L(\lambda)$ is the automorphic line bundle `L₀ TF.X Z λ`. Let $\kappa$ be the canonical weight `FlagTan.kap`.

A *modification* $M$ (`Modif`) is a scheme $X'$ with a map $\sigma \colon X' \to \bar X$ such that $X'$ is smooth of relative dimension $n$ and projective over $F$, $\sigma$ is an isomorphism over $U$, and $\sigma^{-1}(U)$ is dense. Its canonical bundle $K_{X'}$ is the bundle of top forms (`CanonLB.all`). A *canonical identification* (`CanId M`) is a nowhere zero section $\omega$ of $K_{X'} \otimes \sigma^* L(\kappa)^{-1}$ over $\sigma^{-1}(U)$ that matches the Kodaira-Spencer map at each framed point (`IsKS`).

**Theorem.** Assume `Hypotheses''` and `GrothendieckDeformation`, and that $F$ is algebraically closed in the function field of each component (`FnAlgClosed`). Let $M$ be a modification with a canonical identification $\omega$. Let $b, s$ be weights with $\kappa + b = s$, and let $m$ be a section of $L(s)$ over $U$. Then the following are equivalent:

1. $m$ is the restriction of a global section of $L(s)$ whose germs at each point of $D$ lie in the maximal ideal (`vanBd`);
2. $\omega \cdot \sigma^* m$ is the restriction of a global section of $K_{X'} \otimes \sigma^* L(b)$ on $X'$.

In standard terms, (1) says that $m$ is a cusp form. The equivalence rests on $L(\kappa) \cong \Omega^n(\log D)$, which for toroidal compactifications of locally symmetric varieties is due to Mumford (Invent. Math. 42, 1977). In the Lean code it comes from the simple pole of a canonical identification along $D$ (see [log_canonical_refl_of_boundary](/entry/log-canonical-refl-of-boundary/)). We have not checked whether a field of `Hypotheses''` carries Mumford's result.

## Proof

1. **Case $p + q \ge 1$.** `flag_tangent_kodaira_spencer_iso` gives the Kodaira-Spencer isomorphism at every framed point. `nonempty_kodairaSpencer_identification_offBoundary` gives a canonical identification $\omega_0$ for the trivial modification $\bar X$ itself. It uses the field `p5` (`AbelianDeRham`). Then [logCanonical_divisor_refl](/entry/log-canonical-divisor-refl/) proves the equivalence for $\bar X$ and $\omega_0$. `canonicalExtension_birational_invariance` proves that condition (2) for $\bar X$ is equivalent to (2) for $M$.
2. **Case $p + q = 0$.** Then $n = 0$ (`dimFlag_eq_zero`). A dense open subset of a smooth scheme of relative dimension $0$ is everything (`dense_open_eq_univ_of_smooth_relDim_zero`). So $D$ is empty, $\sigma^{-1}(U) = X'$, and both conditions hold by `restr_top_surj`.

## In the Lean code

The theorem is at [LogCanonicalCriterionBoundary.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/LogCanonicalCriterionBoundary.lean#L21). `Modif` is in [IsoOverOfIsOpenImmersion.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsoOverOfIsOpenImmersion.lean#L623), `CanId` in [NonemptyCuspFrame.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/NonemptyCuspFrame.lean#L63), and `vanBd` in [BarCompSubsetClosure.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/BarCompSubsetClosure.lean#L385).

- `canonicalExtension_birational_invariance` restates `CanonBirat.canonicalExtension_extends_iff_modification`, whose proof we have not opened. We have not opened the two Kodaira-Spencer lemmas of step 1.
- The product $\omega \cdot \sigma^* m$ is taken in the chart system `canChart`, which multiplies $K \otimes L(\kappa)^{-1}$ and $L(s)$ into $K \otimes L(b)$.
