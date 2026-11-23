---
id: etale-finiteness-of-duality
title: Finiteness of étale cohomology of proper varieties
kind: theorem
decl: UpperTheory.Et.etale_finiteness_of_duality
module: Development.AutomorphicArithmetic.CommutativeAlgebra.EtaleCohomology.EtaleDualityTraceIsomorphism
covers: 4117
status: drafted
drafted_by: writer@claude-opus-5-5
---
This theorem says that the étale cohomology groups of a proper variety over an algebraically closed field, with coefficients $\mathbb{Z}/q(i)$ and $q$ invertible, are finite. Its one user is [the finiteness of ℓ-adic cohomology](/entry/v-fin-holds/), which applies it with $q = \ell^a$ for each $a$ and gets that $H^n(X, \mathbb{Z}_\ell(i))$ is a finitely generated $\mathbb{Z}_\ell$-module. That result goes up through [the crystalline step](/entry/crys-step-holds/) to [the local steps](/entry/steps-holds/) of [the Galois row from geometry](/entry/geometric-realization-of-weight-one/). The theorem is the conclusion of [the conditional finiteness theorem](/entry/e4/) with its 27 hypotheses proved. Below it are 4,117 declarations.

## Statement

**Theorem.** Let $q \geq 1$ be an integer. Let $k$ be an algebraically closed field in which $q$ is invertible. Let $X$ be a scheme with a proper morphism $X \to \operatorname{Spec} k$. Then for all integers $n$ and $i$ the group $H^n(X, \mathbb{Z}/q(i))$ is finite.

This is the finiteness theorem for proper morphisms, in the case of the constant sheaves $\mathbb{Z}/q(i)$ over an algebraically closed field (SGA 4, tome 3, Exposé XIV, by M. Artin).

The cohomology and the sheaf $\mathbb{Z}/q(i)$ are the models of the Lean code. The [conditional theorem](/entry/e4/) describes them.

## Proof

The proof applies the [conditional finiteness theorem](/entry/e4/) to 27 theorems of the library, one for each of its hypotheses. In the order of the hypotheses:

- the formal properties A1 to A11: `quasiIso_hypercohomology_bijective`, `etC_a2`, `levelwiseEquivalence_isEquivalence`, `mayerVietoris_equivalence_of_cover`, `positiveDegreeClasses_die_on_etaleCover`, `etaleCohomology_coefficient_longExactSequence`, `etaleCohomology_coefficientRing_invariance`, `etaleCohomology_negative_vanishing_degree_zero`, `etaleCohomology_bijective_of_support_bijective` and `RedCoef.a11`;
- the local statements B1 to B7: `etaleCohomology_twisted_filtered_colimit_continuity`, `strictlyHenselianLocalRing_acyclic_every_sheaf`, `etC_b3`, `integralSurjection_cechDescent_tateTwist`, `absolutelyIntegrallyClosed_domain_tateTwistAcyclic` and `etaleCohomology_field_eq_galoisCohomology`;
- the statements on curves and polynomial rings C1 to C5: `etale_cohomology_vanishing_algebraic_over_ratFunc`, `smooth_affine_curve_etale_cohomologicalDimension_le_one`, `etale_cohomology_ind_etale_base_change`, `homotopy_invariance_etale_alt` and `etale_cohomology_locally_acyclic`;
- the classes D1 to D3: the [projective bundle formula](/entry/projective-bundle-formula-vector-bundle-any-space/), [`etale_duality_trace_isomorphism`](/entry/etale-duality-trace-isomorphism/) and `integerApproximationCount_holds`;
- the base change theorems E1 to E3: `affine_proper_base_change`, [`proper_base_change`](/entry/proper-base-change/) and `etale_base_change_of_duality`.

D2, D3 and E3 are proved in this file, and E1 and E2 in [AffineProperBaseChange.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/AffineProperBaseChange.lean#L26). The rest is bookkeeping. The real content is in [the conditional theorem](/entry/e4/) and in the 27 lemmas.

## In the Lean code

The theorem is in [EtaleDualityTraceIsomorphism.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/EtaleDualityTraceIsomorphism.lean#L46). Its statement is `GlobalTheory.EtC.E4`, defined in [DivisorSupportCondition.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/DivisorSupportCondition.lean#L145). The proof is one term: `e4` applied to the 27 lemmas above.

Odd points:

- The name says "of duality", but no duality statement enters. The definitions file has a Poincaré duality statement `E8`, and it is not among the 27 hypotheses. The word comes from the lemma `etale_duality_trace_isomorphism` ([line 40](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/EtaleDualityTraceIsomorphism.lean#L40)), which proves `D2`. `D2` is not a trace isomorphism: it gives, for each $k > 0$, classes $s(V) \in H^{2k}(E, \mathbb{Z}/q(k))$ of vector bundles that are natural, additive in direct sums and equal to $c_1(L)^k$ for a line bundle $L$.
- Three more names do not match their statements. `integerApproximationCount_holds` (line 42) proves `D3`, a statement on slant products with group homology. `etale_base_change_of_duality` (line 44) proves `E3`, a base change to the generic point for smooth schemes over a local domain. `etale_cohomology_locally_acyclic` proves `C5`, the cohomology of a Laurent polynomial ring.
- The statement holds for all integers $n$ and $i$. For $n < 0$ it is trivial, since the groups vanish by A9.
