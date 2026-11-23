---
id: hilbert-samuel-of-component-estimates-alt
title: A Hilbert-Samuel lower bound on the components of a good cover
kind: theorem
decl: GlobalTheory.CovTop.ShortRoad.hilbertSamuel_of_component_estimates_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.HilbertSamuelLowerBoundOfComponents
covers: 830
status: drafted
drafted_by: writer@claude
---
This theorem proves the cover statement `CoverHeightSum`: on each component of a good cover, the Arakelov degree of a lattice of cusp forms is at least a binomial coefficient times degree times height, minus an error of size $C\,\mathrm{unitE}$. Its only user is its second name [coverHeightSum_of_flatDeg_coverDegree_share](/entry/cover-height-sum-of-flat-deg-cover-degree-share/), which [the covolume bound](/entry/top-covol-g-alt-alt/) calls. Below this theorem are 830 declarations.

## Statement

We use the cover statements of [the covolume bound](/entry/top-covol-g-alt-alt/). Fix a point $p$, a level $i$ with $i + 1 < m$, a good cover $Y$ and a weight $u_1$ with the quotient condition `Quo`. Let $T$ be `lenT`, $N$ the flag dimension `dimFlag`, $R_T = \binom{T-1}{N}$ (`binT`), and $u^-$ the weight `uM`. For a component $Z$ of $Y$:

- $\delta(Z)$ is the degree of the image of $Z$ under the cusp forms of weight $u_1$ (`compDeg`, through a Chow form);
- $h(Z)$ is the height of that image for the norms and lattice of these cusp forms (`compHeight`);
- $\deg_\lambda(Z)$ and $\mathrm{rk}_\lambda(Z)$ are the Arakelov degree and the rank of the hermitian lattice of cusp forms of weight $\lambda$ on $Z$ (`degOn`, `rankOn`).

`HSAt` with constant $C$ says: there are $A > 0$ and $R \ge 0$ with $A \log\max(A, 1) + R \le C\,\mathrm{unitE}$ and, for each $Z$,

$$R_T\,\delta(Z)\Bigl(T\,h(Z) - 3(N+1)\,|h(Z)| - A\log\bigl(2 + |h(Z)|\bigr) - R\Bigr) \le \deg_{u^-}(Z).$$

**Theorem.** Assume $\mathsf{HypothesesX}$, `PublishedHodgeBundleTheorems`, `GrothendieckDeformation`, `Quoted`, `SiegelToroidalIntegral`, `ToroidalForFanKS`, `SemiAbelianLieSeminegative`, and the cover statements `DeepGoodness`, `SizeCondition`, `FlatDegreeCondition`, `CoverDegree` and `ShareCondition`. Then `CoverHeightSum` holds: `HSAt` holds for all such $p, i, Y, u_1$, with one constant $C$.

## Proof

1. **The claim at the top weight.** Let $P$ be the weight parameter $(u_W, c_0, k - 2, T)$ and $P_T$ its weight of index $T$. [exists_degree_parameters_bound_alt_alt](/entry/exists-degree-parameters-bound-alt-alt/) gives, for each $Z$, numbers $n, \Lambda, \beta, \Lambda_D, \Lambda_T, J$ with the inequality `HSClaimS` of [the estimate at one level](/entry/hilbert-samuel-estimate-at-level/) for $\deg_{P_T}(Z)$. This is the step with content.
2. **The twist.** The quotient condition gives $u_1 = P.u_1$ and $u^- = P_T + w$ for a flat twist $w$. `twisted_bundle_degree_lower_bound` gives $C_p \ge 0$ with $\deg_{P_T}(Z) - \mathrm{rk}_{P_T}(Z)\,C_p z^2 \le \deg_{u^-}(Z)$, where $z$ is `zBase`. `twisted_flat_bundle_ranks` says that the twist does not change the rank.
3. **The numbers.** `CoverDegree` gives $\delta(Z) \ge 1$. `ShareCondition` gives $(1 - \mathrm{zed})\,\mathrm{rk}_{u^-}(Z) \le R_T\,\delta(Z)$, and $\mathrm{rk}_{u^-} = \mathrm{rk}_{P_T}$. `SizeCondition`, `size_bounds_for_family_alt` and `weight_parameter_strict_antitone_alt` give the bounds on $T$, $N$ and the scale $b$.
4. **Assembly.** `deg_bound_of_claim_numbers`, an inequality between real numbers, combines steps 1 to 3. It gives the bound with $A = 26(26N^2 + 2\,\mathrm{zed}\,T)$ and $R = 4000\,b + 2C_p z^2$. `hilbertSamuel_ALogA_le` and $b \le \mathrm{unitE}$ give $A\log\max(A,1) + R \le (10000 + 2C_p)\,\mathrm{unitE}$.

The rest is bookkeeping with `Closed.imp` and `Closed.and`.

## In the Lean code

The theorem is at [HilbertSamuelLowerBoundOfComponents.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/HilbertSamuelLowerBoundOfComponents.lean#L25). It calls:

- `GlobalTheory.T.exists_degree_parameters_bound_alt_alt`;
- `GlobalTheory.T.twisted_bundle_degree_lower_bound`, `GlobalTheory.T.twisted_flat_bundle_ranks` and `GlobalTheory.T.covering_domain_lattice_regularity`, all from `PublishedHodgeBundleTheorems`;
- `GlobalTheory.T.size_bounds_for_family_alt`, `GlobalTheory.T.weight_parameter_strict_antitone_alt`;
- `GlobalTheory.CovHSNum.deg_bound_of_claim_numbers` and `GlobalTheory.hilbertSamuel_ALogA_le`.

Much of the proof checks numerical side conditions by `linarith` and `nlinarith`, such as $1 \le z$ and $z^2 \le b$. The constant $C = 10000 + 2C_p$ is explicit. We have not unfolded `compHeight`, `Quo` or the twist lemmas.
