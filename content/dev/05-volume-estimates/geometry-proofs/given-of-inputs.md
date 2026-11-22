---
id: given-of-inputs
title: The inputs of the volume branch from twelve hypotheses
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Top.given_of_inputs
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.FinalTheoremOfInputsLeft
covers: 1191
status: drafted
drafted_by: writer@claude
---
This theorem assembles `Top.Given`, the list of fourteen inputs that the volume estimates use. It passes eleven of its twelve hypotheses through unchanged. It proves two parts outright and gets one part from a Siegel lemma. Its one user is the renaming [`T.final_theorem_of_inputs_left`](/entry/final-theorem-of-inputs-left/). Most of the real content of the subtree is in [the slope bound from the Siegel lemma](/entry/slope-bound-and-lemma-s-of-siegel/).

## Statement

`Top.Given` is the conjunction of these fourteen statements, in this order:

1. the model clause: `PartI`, `N1ab`, `N1c`, and for each CM field $E$, host and datum, the toroidal compatibilities of level and Hecke operators;
2. `KeyFormula`;
3. `SemiAbelianHomExtension`;
4. `NumericalSegre.Statement`;
5. `ResKStatement`;
6. `SAStatement`;
7. `HT.FarguesHodgeTate`;
8. `Flat.GagaSections`;
9. `SlopeBoundSt`, a bound for the maximal slope of a hermitian bundle with a semi-abelian model;
10. `PB.Inputs`;
11. `Prov.HS`, nine statements on successive minima, arithmetic intersection numbers, arithmetic volumes and Hilbert-Samuel bounds;
12. `Prov.An`;
13. `Prov.ZhangDimensionPushDownGrassmannianHeightBounds`;
14. `AntisymPerturbation.Statement`, on polynomials that vanish on diagonal hyperplanes. We have not unfolded it in full.

`SAStatement` says: let $E/F$ be a quadratic extension of number fields with conjugation $c$, and $J$ an $N \times N$ matrix over $E$ with $J^{\mathsf T} = c(J)$, $\det J$ a unit, and an isotropic vector. Then $\mathrm{SU}(J)$ over $E \otimes_F \mathbb{A}_{F,f}$ lies in the closure of $\mathrm{SU}(J)(E)$. This has the form of strong approximation (Platonov and Rapinchuk, Algebraic Groups and Number Theory, Chapter 7).

**Theorem.** Parts 1 to 5, 7, 8 and 10 to 13 of `Top.Given`, together with `LineOfLargeDegree.Statement`, imply `Top.Given`.

## Proof

Each part is one of three kinds.

- Parts 1 to 5, 7, 8 and 10 to 13 are hypotheses.
- Part 6 is `semi_abelian_statement_holds`, and part 14 is `antisymmetric_perturbation_holds`. Both are theorems with no hypothesis. We have not followed their proofs.
- Part 9 is the first half of [`slope_bound_of_line_large_degree`](/entry/slope-bound-of-line-large-degree/), applied to `LineOfLargeDegree.Statement`.

## In the Lean code

The theorem is in [FinalTheoremOfInputsLeft.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/FinalTheoremOfInputsLeft.lean#L22). `Top.Given` is in [GoodOrigin.lean](lean:Development/AutomorphicSpectrum/Definitions/DivisibilityTowers/GoodOrigin.lean#L67), and `SAStatement` in [SAOpenStatement.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/StrongApproximation/SAOpenStatement.lean#L49). The proof is an anonymous constructor with fourteen components.

Part 13 has a `True` conjunct: it is `ZhangLowerX.Statement ∧ DimX.Statement ∧ True ∧ PushDown.Statement ∧ GrassmannianHeightZTwo.Statement` ([ZhangDimensionPushDownGrassmannianHeightBounds.lean](lean:Development/AutomorphicSpectrum/Statements/GeometryStatements/ZhangDimensionPushDownGrassmannianHeightBounds.lean#L33)).
