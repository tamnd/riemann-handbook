---
id: smoothed-zeta-class-hodge-tate-law
title: The Hodge-Tate law for smoothed zeta classes, by name
kind: theorem
decl: UpperTheory.V.Z.Kato.K5.smoothedZetaClass_hodgeTateLaw
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.KatoQuadraticCharacters.SmoothedZetaClasses.SmoothedZetaClassHodgeTateLaw
covers: 1883
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It gives the Hodge-Tate law for smoothed zeta classes the name that the proof of [the unramified zeta theorem](/entry/zeta-ur/) uses. That proof feeds it, with the integrality of the Euler system and a nonvanishing result for Hecke projections, into [`kato_global_unit_law_of_smoothed_classes`](/entry/kato-global-unit-law-of-smoothed-classes/). The mathematics is in [the entry for `K5.top`](/entry/k5-top/), and the main proof step is in [the coefficient law](/entry/hco/).

## Statement

The statement is the proposition `SmoothedZetaClassHodgeTateLawStatement`. It is word for word the statement of [`K5.top`](/entry/k5-top/): for an odd prime $\ell$, a newform $g$ of weight $2e+1$ with its $\ell$-adic representation, a zeta system $Y$ of Galois cocycles, a character $\chi$ and a functional $\lambda$ with the stated properties, and an integer $d_0 \geq 2$ prime to $\ell$, the smoothed class $Y - d_0 \cdot Y(\,\cdot\, d_0)$ has a Hodge-Tate presentation whose twisted sums are congruent to an explicit Gauss sum times $\lambda$ of an Eisenstein-type projection. See that entry for the full list of hypotheses.

## Proof

The proof is the single term `UpperTheory.V.Z.Kato.K5.top`. Nothing else happens.

## In the Lean code

The theorem is in [SmoothedZetaClassHodgeTateLaw.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/SmoothedZetaClasses/SmoothedZetaClassHodgeTateLaw.lean#L4). The statement is defined in [SmoothedZetaClassHodgeTateLawStatement.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/FrobeniusHodgeTateLaws/SmoothedZetaClassHodgeTateLawStatement.lean#L31). The same file lists it as one of 22 inputs of the structure `Glue2` at line 92. The size 1,883 counts the subtree of `K5.top` plus this one declaration.
