---
id: nlink-e-main-alt-alt
title: The congruence bound along a family, for large parameters
kind: theorem
decl: GlobalTheory.NLinkE.main_alt_alt
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.AdmissibleParameterEventually
covers: 2068
status: drafted
drafted_by: writer@claude
---
This theorem proves the congruence bound for the data of a family, once the parameter is large. It is restated as [the congruence bound for large parameters](/entry/eventually-cong-bound-of-facts/), and [the closing of the family bound](/entry/nlink-close-main-alt-alt/) uses it to show that the local bound is zero at large primes. That chain goes up to the step [the hypotheses are not empty](/step/nonempty-hyps/).

## Statement

**Theorem.** Assume the seven hypotheses $\mathrm{Hyp}_2$. Let $F$ be a family with parameter $\varepsilon$. Then there is $x_0$ with the following property. Let $x \ge x_0$ with $x > x_1(F)$, let $i$ be an index at $x$, and suppose the norm choice facts hold for $D = D_{x,i}$. Let $k$ be an index of $D$ with prime $\ell = \ell_k$ such that $\ell > \ell^*(L)$, $\ell \ne g_j$ for all $j$, $\ell \notin \mathrm{Exc}(L)$, the weight tie holds and the condition HG holds. Let $r$ be a good family, $\pi \in Z_k$ and $\rho$ a rank $r$ part of $r(\pi)$. Then, in $[0, \infty]$,

$$v_{\mathrm{CC}}(\pi) \le s_\pi + \sum_{0 < e < t} \operatorname{len} Ш_e + v_\ell(h_E) + t \sum_{P \in Q_k} v(\zeta_P - 1).$$

Here $v_{\mathrm{CC}}(\pi)$ is the infimum over congruence elements $f$ of the normalized length of $O/(f(\pi))$, and $s_\pi$ is the normalized length of a Selmer group. $\mathrm{Exc}(L)$ is the set of primes above $\ell^*$ that divide an integer in a window around one of the base sizes.

## Proof

Take $x_0$ as the maximum of three thresholds: one from `exists_localPositionData_off_exceptional_primes` (it gives $\ell \ge 5$, $\ell > t+1$, $\ell \ne q, d$, $\ell$ not small, and position data), one from `eventually_prvJ_of_facts` (jump conditions), and one from the private lemma `admissible_parameter_eventually` (admissible parameters).

Then fix $k$, $r$, $\pi$, $\rho$. The host field is unramified at $\ell$. Lemmas for large good places give the admissibility conditions G1, G2 (with the Fontaine hypothesis) and G3, continuity and semisimplicity. `exists_globalStep_objects_of_cyclotomic_generator_inertia` gives a decomposition by orthogonal idempotents. The Bhatt-Scholze hypothesis gives a Wach functor and a comparison. The Bloch-Kato, Tate and Euler hypotheses give the top condition, and `UseLoc.main` gives local bounds above $\ell$. Then `globalCongruenceCount_of_rootDifference_unit`, with Artin reciprocity, gives a rational bound when the Selmer and Tate-Shafarevich groups are finite. `congruenceBound_extended_of_rationalBound` turns this into the bound in $[0, \infty]$.

## In the Lean code

The theorem is in [AdmissibleParameterEventually.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AdmissibleParameterEventually.lean#L30). The bound is `CongBound_at` in [BaseSizes.lean](lean:Development/AbelianVarietyTheory/BlockTheory/NonGaloisCusps/BaseSizes.lean#L87). We have not unfolded the conditions inside the lemmas for large places.

- The weight tie hypothesis is introduced as `_hW` and never used.
- The hypothesis `LocalFinitenessK` of $\mathrm{Hyp}_2$ is not used.
- The statement does not assume that the Selmer and Tate-Shafarevich groups are finite. The last lemma, in [CongruenceBoundExtendedOfRationalBoundStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CongruenceBoundExtendedOfRationalBoundStatement.lean#L19), takes the rational bound under these finiteness conditions and gives the bound with no condition. It restates `congBound_of_rational`, whose proof we have not read.
