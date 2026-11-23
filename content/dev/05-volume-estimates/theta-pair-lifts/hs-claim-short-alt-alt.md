---
id: hs-claim-short-alt-alt
title: The Hilbert-Samuel claim on every component of a good cover
kind: theorem
decl: GlobalTheory.HSShortRun.hsClaim_short_alt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ExistsDegreeParametersBound
covers: 811
status: drafted
drafted_by: writer@claude
---
This theorem turns [the estimate at one level](/entry/hilbert-samuel-estimate-at-level/) into a cover statement. It collects, from eight cover statements, the inputs that the estimate needs on each component $Z$, and it bounds the six numbers of the estimate by the size parameter $P_P$. Its only user is its second name [exists_degree_parameters_bound_alt_alt](/entry/exists-degree-parameters-bound-alt-alt/). Below this theorem are 811 declarations.

## Statement

We use the notation of [hilbertSamuel_of_component_estimates_alt](/entry/hilbert-samuel-of-component-estimates-alt/). Let $P = (u_W, c_0, k - 2, T)$ be the weight parameter, with $T$ = `lenT`, $N$ = `dimFlag` and $\kappa$ = `kap p i`. Write $\delta(Z)$ and $h(Z)$ for the degree and the height at the weight $P.u_1$, and $\mathrm{rk}(Z)$, $\deg(Z)$ for the rank and the Arakelov degree at the weight $P_T$.

**Theorem.** Assume $\mathsf{HypothesesX}$, `PublishedHodgeBundleTheorems`, `GrothendieckDeformation`, `Quoted`, `SiegelToroidalIntegral`, `ToroidalForFanKS`, `SemiAbelianLieSeminegative`, `DeepGoodness`, `SizeCondition` and `FlatDegreeCondition`. Then, as a cover statement, each component $Z$ has real numbers $n, \Lambda, \beta, \Lambda_D, \Lambda_T, J$, all at least $1$ except $J$, with

- $\log n \le P_P$, $\log\beta \le P_P$ and $\log\delta(Z) \le P_P$;
- $\log\Lambda \le P_P(\kappa/T + 1)$, $\log\Lambda_D \le P_P\kappa$ and $\log\Lambda_T \le P_P\kappa$;
- $J \le 4\bigl(N P_P(\kappa/T + 1) + T P_P\bigr) + 2 P_P (\kappa/T) N$;
- `HSClaimS` with $C = 26$, $j_0 = 1$, and the data $T, N, \delta(Z), h(Z), \mathrm{rk}(Z), \deg(Z)$.

## Proof

1. **The inputs.** `hilbertSamuel_bergman_frame_bound_alt` gives two cusp frames $f_1, f_2$ and the numbers $\Lambda, \beta$ with their bounds, and $n$ = the size of $f_1$. `log_dg_u1_le_of_flatDeg` gives $\log\delta(Z) \le P_P$. `birOn_weightPair_both_components_alt`, `wtBig_run_alt`, `weight_parameter_strict_antitone_alt`, `size_bounds_for_family_alt`, `short_vectors_span_cusp_lattice_alt` and `short_path_weight_bound_alt` give the other hypotheses of the estimate. `covering_domain_lattice_regularity` gives goodness at each weight $P_i$, $i \le T$.
2. **The estimate.** [hilbertSamuel_estimate_at_level](/entry/hilbert-samuel-estimate-at-level/) gives $1 \le n$ and `HSClaimS` with $\Lambda_D = \Lambda_T = e^{P_P\kappa}$ and $J = N P_P(\kappa/T + 1)$. This is the step with content.
3. **The bound on $J$.** The three terms of the bound are at least $0$, so `linarith` gives it.

The rest is bookkeeping with `Closed.imp` and `Closed.and`.

## In the Lean code

The theorem is at [ExistsDegreeParametersBound.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsDegreeParametersBound.lean#L34).

- The proof is a copy of `hsClaim_short_alt` in [HodgeBundleWeights/ExistsDegreeParametersBound.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/ExistsDegreeParametersBound.lean#L78), which uses the versions of the input lemmas without `_alt` and `log_degree_bound_hilbertSamuel` in step 1.
- The bound on $J$ is weak: $J$ is the first of the three terms, and the bound is four times that term plus more.
- The estimate needs `NadelVanishingAndNonKltDivisor` and `Principalisation`. The proof takes them from `PublishedHodgeBundleTheorems` (`h2.q15`, `h2.q16`).
- We have not unfolded `kap`, `lenT`, `uW` or the input lemmas of step 1.
