---
id: etale-base-change-of-duality
title: Restriction to the generic fibre over an absolutely integrally closed local domain
kind: theorem
decl: UpperTheory.Et.etale_base_change_of_duality
module: Development.AutomorphicArithmetic.CommutativeAlgebra.EtaleCohomology.EtaleDualityTraceIsomorphism
covers: 725
status: drafted
drafted_by: writer@claude
---
This theorem proves the axiom E3 of the étale chapter. Its proof only collects 11 axiom theorems and passes them to [E3.main](/entry/e3-main/), where the content is. It has three users: [the finiteness theorem](/entry/etale-finiteness-of-duality/), `Gal.Mod.specGood` and `Gal.G3.jVBcS`. All three lie below [Steps holds](/entry/steps-holds/), the same users as [proper base change](/entry/proper-base-change/).

## Statement

A ring is *absolutely integrally closed* if each monic polynomial of positive degree over it has a root in it.

**Theorem.** Let $T$ be a local domain that is absolutely integrally closed, with fraction field $K$. Let $q \neq 0$ be a unit in $T$, and let $p \colon X \to \operatorname{Spec} T$ be smooth. Then for all $i$, restriction to the generic fibre
$$H^n(X, \mathbb{Z}/q(i)) \to H^n(X \times_T \operatorname{Spec} K, \mathbb{Z}/q(i))$$
is bijective in all degrees $n$.

## Proof

The proof is `E3.main` applied to the record `Hyp` of 11 axioms: A1 to A5, A9, B1, B2, B4, C3 and C4. Each is supplied by a theorem of the axiom layer, for example `etale_cohomology_ind_etale_base_change` for C3 and `homotopy_invariance_etale_alt` for C4. There is nothing else.

## In the Lean code

The theorem is at [EtaleDualityTraceIsomorphism.lean line 44](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/EtaleDualityTraceIsomorphism.lean#L44). E3 is stated in [DivisorSupportCondition.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/DivisorSupportCondition.lean#L141).

- The name is misleading. The statement has no duality, and the base change is the restriction to the generic fibre.
- The statement assumes $q \neq 0$ (`NeZero q`). It is forced: $q$ is a unit in a domain.
