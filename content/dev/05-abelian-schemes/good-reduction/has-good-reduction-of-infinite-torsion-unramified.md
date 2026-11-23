---
id: has-good-reduction-of-infinite-torsion-unramified
title: Good reduction from infinitely many unramified torsion levels
kind: theorem
decl: UpperTheory.Lit.Nos.C6.hasGoodReduction_of_infinite_torsionUnramified
module: Development.AutomorphicArithmetic.ThetaCorrespondence.GoodReduction.HasGoodReductionOfInfiniteTorsionUnramified
covers: 339
status: drafted
drafted_by: writer@claude
---
This theorem is the hard direction of [the criterion of Néron, Ogg and Shafarevich](/entry/nos-neron-ogg-shafarevich/), the implication $3 \Rightarrow 1$ there. If inertia fixes the $m$-torsion of an [[abelian variety|R7W03TXRS9]] for infinitely many $m$ prime to the residue characteristic, then the abelian variety has good reduction. The proof goes up to the maximal unramified extension, where the torsion points become rational, and then comes back down.

## Statement

Let $R$ be a discrete valuation ring with perfect residue field $k$ and fraction field $K$. Let $\Omega$ be a separable closure of $K$, $V$ a valuation ring of $\Omega$ above $R$, and $I$ the inertia group of $V$ in $\mathrm{Gal}(\Omega/K)$. Let $A$ be an abelian variety over $K$.

**Theorem.** Suppose that the set of $m \in \mathbb{N}$ with $m \neq 0$ in $k$ and with $I$ fixing every point of $A[m](\Omega)$ is infinite. Then $A$ has good reduction over $R$.

The terms are defined in [the entry for the Serre-Tate theorems](/entry/serre-tate-good-reduction/).

## Proof

Let $K' = \Omega^I$ be the fixed field of inertia and $W = V \cap K'$. In standard terms, $K'$ is the maximal unramified extension of $K$ inside $\Omega$ for the place $V$.

1. **Reduction to $K'$.** By `C5.hasGoodReduction_of_inertiaFixed`, it is enough that $A_{K'}$ has good reduction over $W$. That lemma descends an abelian scheme model from $W$ to $R$ through `hasGoodReduction_of_unramified_abelianScheme_model`, whose proof we have not unfolded.
2. **The ring $W$.** By `inertiaFixedField_valuationRing_strictlyHenselian`, $W$ is a henselian discrete valuation ring with fraction field $K'$ and algebraically closed residue field (this is where $k$ perfect enters), and the inclusion $R \to W$ sends a uniformizer to a uniformizer.
3. **Rational torsion.** Let $g = \dim A$ (`exists_relativeDimension_abelianVariety_field`). Take $m$ in the given infinite set. Then $m$ is a unit in $R$, hence in $W$, so $m \neq 0$ in the residue field of $W$. Since $I$ fixes $A[m](\Omega)$, each of these points comes from a point over $K'$ (`exists_fixedField_point_of_fixed_by_subgroup`), so $A[m](K') = A[m](\Omega)$ (the auxiliary lemma `card_torsion_fixedField`). Since $m \neq 0$ in $K$ and $\Omega$ is separably closed, $|A[m](\Omega)| = m^{2g}$ (`card_abelianVariety_torsion_sepClosed`).
4. **Good reduction over $W$.** `hasGoodReduction_of_many_rational_torsion_points` says: over a henselian discrete valuation ring with algebraically closed residue field, an abelian variety of dimension $g$ with $|A[m](K')| = m^{2g}$ for infinitely many $m$ prime to the residue characteristic has good reduction. Step 3 gives its hypothesis.

Serre and Tate prove their Theorem 1 by the same route through the maximal unramified extension, with the Néron model for step 4 (Good reduction of abelian varieties, Ann. of Math. 88, 1968, §1). We have not checked whether the Lean proof of step 4 uses a Néron model.

## In the Lean code

The theorem is at [line 87 of HasGoodReductionOfInfiniteTorsionUnramified.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/GoodReduction/HasGoodReductionOfInfiniteTorsionUnramified.lean#L87). The same file defines `basePtEquiv`, `fixedPtHom` and `card_torsion_fixedField`, which identify $K'$-points of $A_{K'}$ with $K$-morphisms from $\operatorname{Spec} K'$ to $A$ and count them.

The lemmas that the proof calls:

- `UpperTheory.Lit.Nos.C5.hasGoodReduction_of_inertiaFixed`, in [HasGoodReductionOfInertiaFixed.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/GoodReduction/HasGoodReductionOfInertiaFixed.lean#L56).
- `GlobalTheory.T.inertiaFixedField_valuationRing_strictlyHenselian`, whose conclusion is the Prop `SS.SH` (discrete valuation ring, henselian, algebraically closed residue field, fraction field).
- `GlobalTheory.T.hasGoodReduction_of_many_rational_torsion_points`, proved by citing `GoodRedTorsion.hasGoodReduction_of_torsion` in HasGoodReductionOfManyRationalTorsionPoints.lean. We have not unfolded that proof.
- `GlobalTheory.T.card_abelianVariety_torsion_sepClosed` and `GlobalTheory.T.exists_relativeDimension_abelianVariety_field`.
