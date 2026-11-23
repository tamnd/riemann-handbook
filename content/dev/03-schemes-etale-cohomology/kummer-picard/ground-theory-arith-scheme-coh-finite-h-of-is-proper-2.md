---
id: ground-theory-arith-scheme-coh-finite-h-of-is-proper-2
title: Finiteness of coherent cohomology on a proper scheme, one degree at a time
kind: theorem
decl: GroundTheory.Arith.SchemeCoh.finite_H_of_isProper
module: GroundTheory.ArithmeticGeometry.SchemeCohomology.ProperFiniteness
covers: 672
status: drafted
drafted_by: writer@claude
---
This theorem says that each cohomology group of a coherent sheaf on a proper scheme over a noetherian ring $A$ is a finitely generated $A$-module. It is [`finiteH_of_isProper`](/entry/ground-theory-arith-scheme-coh-finite-h-of-is-proper/) evaluated at one degree $p$. Other parts of the code call it: for the Hodge groups of a smooth projective variety over $\mathbb{C}$ (`FiniteDimensionalHodgeCohomologyOfSmoothProj`), for proper pushforward (`ProperPushforwardCoherent`), for affine covers (`AffineCoverCohomologyFinite`) and for a Rees algebra (`ReesCech`). Through these it lies below [EveryCharacter](/step/every-character/).

## Statement

Let $A$ be a noetherian ring and $X$ a scheme with a proper morphism $X \to \operatorname{Spec} A$. Let $\mathcal{F}$ be a coherent $\mathcal{O}_X$-module.

**Theorem.** For each $p \geq 0$, $H^p(X, \mathcal{F})$ is a finitely generated $A$-module.

This is EGA III, Théorème 3.2.1.

## Proof

`FiniteH A F` is by definition the statement for all $p$, so the proof is `finiteH_of_isProper F hF p`.

## In the Lean code

The theorem is in [ProperFiniteness.lean](lean:GroundTheory/ArithmeticGeometry/SchemeCohomology/ProperFiniteness.lean#L23). It is a second name for [`finiteH_of_isProper`](/entry/ground-theory-arith-scheme-coh-finite-h-of-is-proper/), with $p$ as an argument. The content is in [`finiteH_of_supportedIn`](/entry/finite-h-of-supported-in/) and [`finiteH_step`](/entry/finite-h-step/).

The definitions behind the statement:

- $H^p$ is Mathlib's sheaf cohomology `Sheaf.H` of the underlying sheaf of abelian groups `modulesAb F`. The $A$-module structure is `H.instModule` in [Linear.lean](lean:GroundTheory/ArithmeticGeometry/SchemeCohomology/CechNaturality/Linear.lean#L146): $a \in A$ acts by the map on $H^p$ induced by multiplication by its image in $\Gamma(X, \mathcal{O}_X)$.
- `IsCoherent` in [TwistingSheaf.lean](lean:GroundTheory/ArithmeticGeometry/SchemeCohomology/ProjectiveCohomology/TwistingSheaf.lean#L18) means: quasi-coherent, and $\Gamma(U, \mathcal{F})$ is a finite $\Gamma(U, \mathcal{O}_X)$-module for each affine open $U$.
