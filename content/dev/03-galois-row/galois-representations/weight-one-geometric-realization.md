---
id: weight-one-geometric-realization
title: The holomorphic Lefschetz formula, as the hypothesis of the Galois row from geometry
kind: theorem
decl: UpperTheory.Gal.Int.Geo.weight_one_geometric_realization
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.IntegralStructures.GeometricFlagBases.WeightOneGeometricRealization
covers: 1814
status: drafted
drafted_by: writer@claude
---
This theorem proves the holomorphic Lefschetz formula $\mathrm{HLF}$, the one hypothesis of [the Galois row from geometry](/entry/geometric-realization-of-weight-one/). The step [GeoOne holds](/step/geo-one-holds/) feeds it into that theorem. The proof only passes the result of another lemma along. The real content is in [the Lefschetz formula for finite étale correspondences](/entry/cb-lefschetz-fixed-point-finite-etale-correspondence/). Below this theorem are 1,814 declarations.

## Statement

**Theorem.** $\mathrm{HLF}$ holds: let $Z$ be smooth and projective over $\mathbb{C}$ of dimension $d$, and let $c_1, c_2 \colon Y \to Z$ be finite étale maps over $\mathbb{C}$. Let $F$ be the finite set of points $y$ with $c_1(y) = c_2(y)$. Suppose that at each $y \in F$ the matrix $A_y$ of $c_2$ relative to $c_1$ on tangent spaces has $\det(1 - A_y) \neq 0$. Then for each $a$ the groups $H^b(Z, \Omega^a)$ have finite dimension, and

$$\sum_{b=0}^{d} (-1)^b \operatorname{tr}\bigl(c_{1*} c_2^* \mid H^b(Z, \Omega^a)\bigr) = \sum_{y \in F} \frac{[t^a] \det(1 + t A_y)}{\det(1 - A_y)}.$$

This is the holomorphic Lefschetz formula of Atiyah and Bott (Ann. of Math. 88, 1968), in the form for correspondences.

## Proof

The proof unfolds the name `HolomorphicLefschetzFormula` and applies `GlobalTheory.T.lefschetz_fixedPoint_finite_etale_correspondence` ([its entry](/entry/t-lefschetz-fixed-point-finite-etale-correspondence/)). That lemma has the same statement, and its proof applies `UpperTheory.Cb.lefschetz_fixedPoint_finite_etale_correspondence`. So both are restatements of the `Cb` lemma.

## In the Lean code

The theorem is in [WeightOneGeometricRealization.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/WeightOneGeometricRealization.lean#L7). The definition of $\mathrm{HLF}$ is in [HodgeTraceFromLefschetzAndGroupSide.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/LefschetzSigmaSums/HodgeTraceFromLefschetzAndGroupSide.lean#L102). The `T` lemma is in [LefschetzFixedPointFiniteEtaleCorrespondence.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/LefschetzFixedPointFiniteEtaleCorrespondence.lean#L8), and the `Cb` lemma in [LefschetzFixedPointFiniteEtaleCorrespondence.lean](lean:Development/AutomorphicArithmetic/Foundations/EtaleClopenDescent/LefschetzFixedPointFiniteEtaleCorrespondence.lean#L255).

The group $H^b(Z, \Omega^a)$ is `hodgeH s a b`, and the operator is `hodgeTrace h1 a b ∘ₗ hodgePull h2 a b`, the trace along $c_1$ after the pullback along $c_2$. The tangent condition is `IsTan`.

Two points are odd. The name says "weight one geometric realization", but the theorem is the Lefschetz formula. The theorem that does the geometric realization is `geometric_realization_of_weight_one`. The two names are swapped. Also, $\mathrm{HLF}$ asks for $c_1$ finite and étale through instance arguments, and for $c_2$ through explicit hypotheses. This does not change the content.
