---
id: top-covol-g-alt-alt
title: The covolume bound from heights and the positivity statement
kind: theorem
decl: SelfIntersectionVolumeEstimates.topCovolG_alt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.TopCovolG
covers: 12516
status: drafted
drafted_by: writer@claude
---
This theorem proves the [covolume bound](/step/covolume-bound-of-x-def/) $\mathsf{CovolumeBoundOfX}$ from seven groups of hypotheses. One of them is the positivity statement $\mathsf{DeepStR}$, which [deep_slim_use](/proof/weil-bound/) proves. Its only caller is [the volume branch](/proof/literature/), which builds the other inputs. Below this theorem are 12,516 declarations.

## Statement

**Theorem.** Suppose that the following hold:

1. $\mathsf{VolumeEstimateHypotheses}$: an upper bound $a \le [K:\mathbb{Q}](D+1)\,\deg \cdot (h + t)$ for the self-intersection $a$ of a shifted hermitian line bundle on an integral model, with a degree and a height of a lattice (`SelfIntersectionBound`), and a bound of the number of small cusp sections of weight $8i$ by the number of small sections of the $8i$-th power of that bundle (`SmallSectionsInject`);
2. $\mathsf{HypothesesX}$: the five statements `ToroidalForFanKS`, `SemiAbelianLieSeminegative`, `GreenCuspidal`, `PointSeparationPair`, `FubiniStudyChowHeight`;
3. the 28-field bundle [PublishedHodgeBundleTheorems](/step/published-results-arithmetic/);
4. $\mathsf{HypothesesH}$: `SiegelToroidalIntegral`, `ToroidalChartsForFan`, `ToroidalCharts`, `ArDegree`;
5. `GrothendieckDeformation`, a deformation statement for rings with an ideal that carries nilpotent divided powers;
6. `Quoted`: Kawamata-Viehweg, $L^2$ extension, Serre's holomorphic sections, nef numerics, three statements on Chow forms, and a length statement for proper intersections;
7. $\mathsf{DeepStR}$, the mean slope bound of the [Weil bound chapter](/proof/weil-bound/).

Then $\mathsf{CovolumeBoundOfX}$ holds.

We use two shapes of statement. A *level statement* $\mathrm{Lifts}(Q)$ says: [closed](/step/closed-def/) over the class `FamHyp`, there is $C \ge 0$ such that for all large $x$, each point $p$ that satisfies `RowsTAlt` and each level $i < m$, $Q(p, i, C)$ holds. A *cover statement* $\mathrm{Covers}(Q)$ is $\mathrm{Lifts}$ of: if $i + 1 < m$, then $Q$ holds for each good cover $Y$ of $p$ at level $i$ (a tower object `Deep` at level $i+1$ with `GoodCov`). The conclusion bounds a normalised log covolume: $\operatorname{lcv}(M_i)/D \le \mathrm{mainT}_i + C\,\mathrm{unitE}$.

## Proof

1. **Level data.** From the bundle (3), `covering_gram_of_prints`, `covering_meas_of_prints`, `covering_deepEx_of_prints`, `liftTruncation_of_prints`, `liftRational_of_prints` and `liftLambdaBound_of_gram_meas` give level statements: Gram norms, a comparison with Petersson norms, good covers, a projector onto a good sublattice, rationality, and a maximal slope bound. `cov_size_bound` and `anchor_bound` are unconditional.
2. **Covers.** `deepGood_of_toroidal_and_semiabelian` proves `DeepGoodness`. `flatDeg_of_scholzeWeinstein_of_prints`, `coverDegree_of_grothendieck_deformation` and `share_of_deep_good_size_flat_deg_cover_degree` give flat degrees, degrees and rank shares on the components of a cover.
3. **Heights.** [height_lower_bound_general_alt](/entry/height-lower-bound-general-alt/) proves `HeightCondition`. It is the only step that uses (1) and (7). With `coverHeightSum_of_flatDeg_coverDegree_share` and `sum_c_of_deep_good`, `uniform_lower_bound_of_sums'` gives a uniform lower bound $-C\,\mathrm{unitE} \le \mu(Y)$ for a slope on the cover.
4. **Lower bound.** `liftLowBound_of_cover_estimates` proves $-\mathrm{mainT}_i - C\,\mathrm{unitE} \le \mu_{\mathrm{core}}$. At the top level $i + 1 = m$ this is the low defect bound. Below it, `lowAt_of_cover` applies to the data and the uniform bound on a good cover $Y$.
5. **Assembly.** `covolX_of_truncation_badSet_lambda_lowBound` combines eight level statements. Three more come in here: `lift_recursion_of_gram_bound`, `liftBadSet_of_deep_size_flatDeg_share` and `coreLe_of_gram_meas_liftRational`. At each point, `lcv_le` chains $\operatorname{lcv}/D \le -\mu(\text{good sublattice})$, then $\mu(\text{good}) \ge \mu(\text{type lattice}) - \text{error}$ by `slope_good_ge`, then the core bound and step 4. For large $x$ the error is at most $\mathrm{unitE}$.

The rest is bookkeeping with `Closed.and` and `Closed.imp`.

## In the Lean code

The theorem is at [TopCovolG.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopCovolG.lean#L39). The proof is 16 `have` steps and one `exact`.

- `covolX_of_truncation_badSet_lambda_lowBound` and `liftLowBound_of_cover_estimates` only restate `covolX_of_lift_bounds_and_coreLe` and `low_of_cover_hypotheses`, by `first | exact ...`.
- `SelfIntersectionBound` and `SmallSectionsInject` each take `PublishedHodgeBundleTheorems` as a premise inside the definition. The caller proves both, by `chow_form_height_comparison` and `small_sections_injective`, so (1) is not open in the final proof.
- We have not unfolded the 28 statements of (3), the statements of (2), (4) and (6), or `lowAt_of_cover`.
- The theorem with real content in step 3 is `height_of_meanAll_bound`; in step 5 it is `lcv_le`.
