---
title: The covolume bound
decls:
  - SelfIntersectionVolumeEstimates.topCovolG_alt_alt
  - SelfIntersectionVolumeEstimates.topCovolSlim2_use_alt_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The covolume bound

This section proves the [covolume bound of $X$](/step/covolume-bound-of-x-def/): for every family of the class, at every point and level, the normalized log covolume of the lattice at the level is at most the main term $T_i$ plus a constant times the unit of error $E$. The proof assembles the results of this chapter. The height lower bound and the cover height sum give a uniform lower bound for a slope on each good cover. With the low defect bound at the last level, this gives a lower bound for the slope of the core lattice at every level. Eight level statements then turn the lower bound for the core slope into the upper bound for the covolume. The second theorem of the section derives all hypotheses except the published ones from a list of fifteen results of the literature, and so proves the covolume bound from that list. It is one of the steps of [the literature branch](/step/every-character-of-literature/) of the proof.

We use the language of [the first section](/entry/to-classical-theorems/): closed statements over the class of families, level statements and cover statements, the length $T$, the main term $T_i$ and the unit $E$.

The hypotheses fall into seven groups.

1. The *volume estimate hypotheses*: an upper bound for the self-intersection of a shifted hermitian line bundle on an integral model by the degree and the height of a lattice, and a bound for the number of small cusp sections of weight $8k$ by the number of small sections of the $8k$-th power of the line bundle.
2. The *hypotheses on the family*: toroidal compactifications for fans with the Kodaira-Spencer isomorphism, the seminegativity of the Lie algebra of semi-abelian schemes, a statement on Green functions of cuspidal type, the point separation statement for pairs and the Fubini-Study formula for Chow heights.
3. The published Hodge bundle theorems ([the published results](/step/published-results-arithmetic/)).
4. The *hypotheses on toroidal charts*: the Siegel toroidal integral, the toroidal charts for fans, the toroidal charts and the arithmetic degree.
5. Grothendieck's deformation theory.
6. The *quoted results*: vanishing and extension theorems, numerics of nef bundles, three statements on Chow forms and a length statement for proper intersections.
7. The *deep mean slope statement*, the mean slope hypothesis of [the height lower bound](/entry/height-of-mean-all-bound/) for all families and good covers.

**Theorem 2.9.1 (Covolume bound from the hypotheses).** Assume the seven groups of hypotheses. Then the covolume bound of $X$ holds.

Lean: `SelfIntersectionVolumeEstimates.topCovolG_alt_alt`.

*Proof.* The proof has five steps.

*Level data.* The published list gives, as level statements: the Gram condition; a comparison of Gram norms with Petersson norms (the measure condition); the existence of good covers at each level; a projector onto a good sublattice (the truncation); rationality of the lift; and a bound for the largest slope (the $\lambda$ bound). The size condition and the anchor condition hold without hypotheses.

*Covers.* Deep goodness follows from the published list, Grothendieck's deformation theory, the quoted results, the Siegel toroidal integral, the toroidal compactifications and the seminegativity of the Lie algebra. The flat degree condition follows from the published list. The cover degree condition and the share condition follow from these with the hypotheses on the family.

*Heights.* [The height lower bound](/entry/height-lower-bound-general-alt/) gives the height condition. It is the only step that uses the volume estimate hypotheses and the deep mean slope statement. [The cover height sum](/entry/hilbert-samuel-of-component-estimates-alt/) gives the Hilbert-Samuel lower bound for the degrees. From the height condition, the cover height sum, the cover degree, the share condition and a statement on sums over the components that follows from deep goodness, one obtains a uniform lower bound: on every good cover, the slope of the lattice of cusp forms of the weight of the level is at least $-C E$.

*Lower bound for the core slope.* At each level the slope of the core lattice satisfies
$$-T_i - C E \le \mu_i.$$
At the last level, $i + 1 = m$, this is [the low defect bound](/entry/covering-low-defect-alt/), which uses the Gram and anchor conditions. At the levels $i + 1 < m$, it follows from the uniform lower bound on a good cover, with the existence of good covers, deep goodness, a ring condition, the maps between the levels, the cover rank, the smallest Gram eigenvalue and a flatness statement; each of these is a level statement from the published list and the conditions above.

*Assembly.* Eight level statements combine: the Gram condition, the recursion of the lift, the truncation, the bad set of the lift, the $\lambda$ bound, the size condition, the comparison of the core lattice with the lift, and the lower bound for the core slope. At each point the normalized log covolume is at most minus the slope of the good sublattice. The slope of the good sublattice is at least the slope of the type lattice minus an error, and for large $x$ this error is at most $E$. With the lower bound for the core slope, the log covolume is at most $T_i + C E$. This is the covolume bound. $\square$

The results of the second section, on the separation of orbits by cusp forms, enter below the level statements of the first and fourth steps. The first section's translation of the published list into classical statements enters in the same way.

The second theorem reduces the seven groups to fifteen results of the literature. The list, in the order of the hypotheses, is the following.

1. Resolution of singularities in characteristic zero: H. Hironaka, "Resolution of singularities of an algebraic variety over a field of characteristic zero. I, II", Ann. of Math. 79 (1964) ([resolution of singularities](/learn/geometry/#resolution-of-singularities)).
2. Principalisation of ideals in characteristic zero, from the same paper of Hironaka.
3. The inverse Poincaré-Lelong formula: P. Griffiths and J. Harris, *Principles of Algebraic Geometry* (1978).
4. The arithmetic Hilbert-Samuel upper bound with nonnegativity for nef bundles: H. Gillet and C. Soulé, "An arithmetic Riemann-Roch theorem", Invent. Math. 110 (1992).
5. Arithmetic bigness: A. Moriwaki, "Continuity of volumes on arithmetic varieties", J. Algebraic Geom. 18 (2009) ([arithmetic volume and bigness](/learn/arakelov/#arithmetic-volume-and-bigness)).
6. Exactness of the Hodge-Tate sequence: L. Fargues, in Progr. Math. 262 (2008).
7. Zarhin's trick: Yu. Zarhin, Math. USSR-Izv. 8 (1974) ([the Hodge bundle and Zarhin's trick](/learn/arakelov/#the-hodge-bundle-and-zarhins-trick)).
8. Asymptotic Riemann-Roch for nef divisors: R. Lazarsfeld, *Positivity in Algebraic Geometry I*.
9. The Siegel toroidal integral: G. Faltings and C.-L. Chai, *Degeneration of Abelian Varieties*, Ergeb. Math. (3) 22.
10. Toroidal compactifications for fans with the Kodaira-Spencer isomorphism: K.-W. Lan, *Arithmetic Compactifications of PEL-Type Shimura Varieties*, LMS Monographs 36 ([toroidal compactifications](/learn/geometry/#shimura-varieties-and-toroidal-compactifications)).
11. Seminegativity of the Lie algebra, that is, nefness of the Hodge bundle: L. Moret-Bailly, *Pinceaux de variétés abéliennes*, Astérisque 129.
12. Point separation for pairs: U. Angehrn and Y.-T. Siu, Invent. Math. 122 (1995) ([point separation](/learn/geometry/#point-separation)).
13. The arithmetic degree, with birational invariance and the Chern-Weil form of the degree: H. Gillet and C. Soulé, "Arithmetic intersection theory", Publ. Math. IHÉS 72 (1990).
14. The published Hodge bundle theorems.
15. Grothendieck's deformation theory: W. Messing, *The Crystals Associated to Barsotti-Tate Groups*, Lecture Notes in Math. 264.

**Theorem 2.9.2 (Covolume bound from the literature).** Assume the fifteen results above. Then the covolume bound of $X$ holds.

Lean: `SelfIntersectionVolumeEstimates.topCovolSlim2_use_alt_alt`.

*Proof.* We derive the seven groups of hypotheses of [Theorem 2.9.1](/entry/top-covol-g-alt-alt/) and apply it.

The hypotheses on the family: the toroidal compactifications for fans (10), the seminegativity of the Lie algebra (11) and point separation (12) are among the fifteen. The statement on Green functions holds by a proof from the regularity of the Green characters, and the Fubini-Study formula for Chow heights follows from the published list (14).

The hypotheses on toroidal charts: the toroidal charts for fans follow from (10). The toroidal charts follow from the Siegel toroidal integral (9) and the charts for fans. The arithmetic degree is (13).

The volume estimate hypotheses: the self-intersection bound is a comparison of Chow form heights, which is proved. The bound on small sections follows from the injectivity of multiplication on small sections, which needs a nonvanishing section on the toroidal compactification; that section exists by (9) and (10).

The quoted results: six of their eight parts are fields of the published list (14), and the other two are proved statements on Chow forms: the existence of the integral of a Chow form and its compatibility with hyperplane sections.

Grothendieck's deformation theory is (15), and the published list is (14).

The deep mean slope statement: it follows from the first eight results, (1) to (8), by the positivity argument of [the Weil bound chapter](/proof/weil-bound/). $\square$

So the first eight results of the literature are used only for the deep mean slope statement, and the other seven enter the covolume bound directly.

**Remark 2.9.3 (Formalization).** The first theorem is a tactic proof at [TopCovolG.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopCovolG.lean#L39). Its steps are named lemmas: `covering_gram_of_prints`, `cov_size_bound`, `covering_meas_of_prints`, `anchor_bound`, `covering_deepEx_of_prints`, `deepGood_of_toroidal_and_semiabelian`, `flatDeg_of_scholzeWeinstein_of_prints`, `coverDegree_of_grothendieck_deformation`, `share_of_deep_good_size_flat_deg_cover_degree`, `uniform_lower_bound_of_sums'` with `sum_c_of_deep_good`, `liftLowBound_of_cover_estimates` (line 57) and the assembly `covolX_of_truncation_badSet_lambda_lowBound`. Our description of their content follows their statements and names; we have not opened all of them. The second theorem is a term proof at [TopCovolSlim2Use.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopCovolSlim2Use.lean#L16). It builds the hypotheses on the family with `green_of_regular greenRegularCharacters_holds` and `fubiniStudy_chowHeight_formula`, the charts with `toroidalChartsForFan_of` and `toroidalCharts_of_siegel_of_forFan`, the volume estimate hypotheses with `chow_form_height_comparison` and `small_sections_injective (exists_nonvanishing_of_toroidal …)`, the quoted results as `⟨hP.q6, hP.q8, hP.q13, hP.q7, hP.q10, chowFormIntExists_holds, chow_form_hyperplane_section, hP.q12⟩`, and the deep mean slope statement as `deep_slim_use` applied to the first eight hypotheses. A different theorem `topCovolSlim2_use_alt`, with one fewer `alt`, is in `HodgeBundleWeights/TopCovolSlim2Use.lean` at line 16. The citations are those of the literature list of the handbook for the fifteen hypotheses; the published Hodge bundle theorems have no single citation there.
