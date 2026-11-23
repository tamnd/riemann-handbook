---
id: ground-theory-arith-scheme-coh-finite-h-of-is-proper
title: Finiteness of coherent cohomology on a proper scheme
kind: theorem
decl: GroundTheory.Arith.SchemeCoh.finiteH_of_isProper
module: GroundTheory.ArithmeticGeometry.SchemeCohomology.ProperFiniteness
covers: 671
status: drafted
drafted_by: writer@claude
---
This theorem says that all cohomology groups of a coherent sheaf on a proper scheme over a noetherian ring $A$ are finitely generated $A$-modules. It is the case "support in all of $X$" of [`finiteH_of_supportedIn`](/entry/finite-h-of-supported-in/). Its only user is [the same statement one degree at a time](/entry/ground-theory-arith-scheme-coh-finite-h-of-is-proper-2/).

## Statement

Let $A$ be a noetherian ring, $X$ a scheme with a proper morphism $X \to \operatorname{Spec} A$, and $\mathcal{F}$ a coherent $\mathcal{O}_X$-module.

**Theorem.** `FiniteH A F` holds: for every $p \geq 0$, $H^p(X, \mathcal{F})$ is a finitely generated $A$-module.

This is EGA III, Théorème 3.2.1. The [next entry up](/entry/ground-theory-arith-scheme-coh-finite-h-of-is-proper-2/) states what $H^p$, the $A$-module structure and coherence mean in the code.

## Proof

Apply [`finiteH_of_supportedIn`](/entry/finite-h-of-supported-in/) with $T = X$. Every sheaf is supported in $X$ (`Scheme.Modules.SupportedIn.univ`). The rest is bookkeeping.

## In the Lean code

The theorem is in [ProperFiniteness.lean](lean:GroundTheory/ArithmeticGeometry/SchemeCohomology/ProperFiniteness.lean#L17). It is a pass-through. `FiniteH` is in [CohFinite.lean](lean:GroundTheory/ArithmeticGeometry/SchemeCohomology/ProperCohomology/CohFinite.lean#L16).

The names `finiteH_of_isProper` and `finite_H_of_isProper` differ in one character and state the same fact. The first gives `FiniteH`, a statement for all degrees; the second gives one degree.
