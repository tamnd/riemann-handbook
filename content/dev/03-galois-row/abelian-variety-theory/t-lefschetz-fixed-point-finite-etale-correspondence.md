---
id: t-lefschetz-fixed-point-finite-etale-correspondence
title: The holomorphic Lefschetz formula for finite étale correspondences (statement form)
kind: theorem
decl: GlobalTheory.T.lefschetz_fixedPoint_finite_etale_correspondence
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.LefschetzFixedPointFiniteEtaleCorrespondence
covers: 1813
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [the holomorphic Lefschetz formula for finite étale correspondences](/entry/cb-lefschetz-fixed-point-finite-etale-correspondence/), which has the real content. Its one user is `weight_one_geometric_realization` ([its entry](/entry/weight-one-geometric-realization/)), which proves the formula $\mathrm{HLF}$ that [the Galois row from geometry](/entry/geometric-realization-of-weight-one/) assumes.

## Statement

**Theorem.** Let $Z$ be smooth of relative dimension $d$ and projective over $\mathbb{C}$. Let $c_1, c_2 \colon Y \to Z$ be finite étale maps over $\mathbb{C}$. Let $F$ be a finite set of $\mathbb{C}$-points of $Y$ that is exactly the set of $y$ with $c_1(y) = c_2(y)$. For each $y \in F$ let $A_y$ be a $d \times d$ matrix that gives the map on tangent spaces in local coordinates, with $\det(1 - A_y) \neq 0$. Then for each $a$ the spaces $H^b(Z, \Omega^a)$ have finite dimension, and

$$\sum_{b=0}^{d} (-1)^b \operatorname{tr}\bigl(c_{1*} c_2^* \mid H^b(Z, \Omega^a)\bigr) = \sum_{y \in F} \frac{[t^a] \det(1 + t A_y)}{\det(1 - A_y)}.$$

This is the holomorphic Lefschetz formula of Atiyah and Bott (Ann. of Math. 88, 1968), in the form for correspondences.

## Proof

The statement is the same as that of `UpperTheory.Cb.lefschetz_fixedPoint_finite_etale_correspondence`, and the proof applies it.

## In the Lean code

The theorem is in [LefschetzFixedPointFiniteEtaleCorrespondence.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/LefschetzFixedPointFiniteEtaleCorrespondence.lean#L8). The proof is `first | exact @UpperTheory.Cb.lefschetz_fixedPoint_finite_etale_correspondence | ...`. The cohomology is `hodgeH s a b`, the trace is that of `hodgeTrace h1 a b ∘ₗ hodgePull h2 a b`, and the tangent condition is `IsTan`, in [IsGaloisCover.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsGaloisCover.lean#L14).

The finiteness and étaleness of $c_1$ are instance arguments, but those of $c_2$ are explicit hypotheses. The fixed set is given as a `Finset` $F$ with a hypothesis that it equals the fixed locus, so finiteness of the fixed points is assumed, not proved.
