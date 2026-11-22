---
id: proper-base-change
title: Proper base change over a strictly henselian local ring
kind: theorem
decl: UpperTheory.Et.proper_base_change
module: Development.AutomorphicArithmetic.CommutativeAlgebra.EtaleCohomology.AffineProperBaseChange
covers: 1247
status: drafted
drafted_by: writer@claude
---
This theorem proves the axiom E2 of the étale chapter: proper base change over a strictly henselian local ring. It has three users, one of them [the finiteness theorem](/entry/etale-finiteness-of-duality/). All three lie below [Steps holds](/entry/steps-holds/). Its proof only collects 15 axiom theorems and passes them to [E2.main](/entry/e2-main/), where the content is.

## Statement

**Theorem.** Let $A$ be a strictly henselian local ring with residue field $\kappa$, and let $q$ be an integer that is a unit in $A$. Let $p \colon X \to \operatorname{Spec} A$ be proper, and let $X_0 = X \times_A \operatorname{Spec} \kappa$ be the closed fibre. Then for all $i$, restriction $H^n(X, \mathbb{Z}/q(i)) \to H^n(X_0, \mathbb{Z}/q(i))$ is bijective in all degrees $n$.

Here a strictly henselian ring is a henselian local ring with separably closed residue field. This is the proper base change theorem of SGA 4, Exposé XII (Artin), in the special case of the coefficients $\mathbb{Z}/q(i)$ with $q$ invertible. SGA 4 does not need $q$ invertible.

## Proof

The proof is `E2.main` applied to a record `Hyp` of 15 axioms: A1 to A5, A7 to A10, B1 to B5 and E1. The axiom E1 is supplied by `affine_proper_base_change`, in the same file. E1 says this: for a henselian pair $(A, I)$ with $q$ a unit in $A$, restriction from $\operatorname{Spec} A$ to $\operatorname{Spec} A/I$ is bijective on $H^*(\,\cdot\,, \mathbb{Z}/q(i))$. This is the affine analogue of proper base change of Gabber (Israel J. Math. 87, 1994), for these coefficients. The other 14 are theorems of the axiom layer. There is nothing else.

## In the Lean code

The theorem is in [AffineProperBaseChange.lean](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/AffineProperBaseChange.lean#L29). E2 is stated in [DivisorSupportCondition.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/DivisorSupportCondition.lean#L137).

- The Lean statement has no hypothesis $q \neq 0$. It is forced: $q$ is a unit in a local ring, so $q \neq 0$.
- Its users are `UpperTheory.Gal.Mod.specGood`, `UpperTheory.Gal.G3.jVBcS` and `etale_finiteness_of_duality`.
- The file name refers to E1, `affine_proper_base_change`, which is proved at line 26 from `etaleCohomology_descent_of_cech_cover`. We have not unfolded that proof.
