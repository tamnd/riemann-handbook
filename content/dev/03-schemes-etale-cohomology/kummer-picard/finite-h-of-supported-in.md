---
id: finite-h-of-supported-in
title: Finiteness of coherent cohomology by noetherian induction on the support
kind: theorem
decl: GroundTheory.Arith.SchemeCoh.finiteH_of_supportedIn
module: GroundTheory.ArithmeticGeometry.SchemeCohomology.ProperCohomology.FinitenessStep
covers: 669
status: drafted
drafted_by: writer@claude
---
This theorem proves the finiteness of coherent cohomology on a proper scheme for all sheaves supported in a closed set $T$, by noetherian induction on $T$. The induction step is [`finiteH_step`](/entry/finite-h-step/), which holds the geometry. With $T = X$ the theorem gives [finiteness of coherent cohomology on a proper scheme](/entry/ground-theory-arith-scheme-coh-finite-h-of-is-proper/).

## Statement

Let $A$ be a noetherian ring and $X$ a scheme with a proper morphism $X \to \operatorname{Spec} A$. Let $T \subseteq X$ be closed. Say that $\mathcal{F}$ is *supported in* $T$ if every section of $\mathcal{F}$ over an open set disjoint from $T$ is zero.

**Theorem.** For each coherent $\mathcal{O}_X$-module $\mathcal{F}$ supported in $T$ and each $p \geq 0$, $H^p(X, \mathcal{F})$ is a finitely generated $A$-module.

## Proof

Since $X \to \operatorname{Spec} A$ is of finite type and quasi-compact, $X$ is locally noetherian and quasi-compact, so its underlying space is noetherian. So the closed sets of $X$ satisfy the descending chain condition, and we may use well-founded induction on $T$ (`WellFoundedLT.induction`). Suppose that the theorem holds for each closed $T' \subsetneq T$. Then [`finiteH_step`](/entry/finite-h-step/) gives it for $T$.

In outline, `finiteH_step` does the following. It writes $\mathcal{F}$ as a pushforward from a closed subscheme $Z$ with support in $T$; if that support is smaller than $T$, the induction hypothesis applies. Otherwise it takes an irreducible closed subscheme $Z_1$ of $Z$ that equals $Z$ over a nonempty open set, and a Chow cover $Z' \to Z_1$: $Z'$ is closed in a projective space over $A$, and the map is an isomorphism over an open set that contains the generic point (`exists_chow`). It also takes a twist $n$ large enough for Serre's theorems on $Z'$. It builds a map $\alpha \colon \mathcal{F} \to \psi_* (\psi^* \mathcal{F}(n))$, with $\psi \colon Z' \to X$, that is an isomorphism over an open set $W$ that meets $T$. The target has finite cohomology by the projective case (`ProjScheme.finite_H`). The kernel and cokernel of $\alpha$ are supported in $T \setminus W \subsetneq T$, so the induction hypothesis applies to them. Two short exact sequences finish the step. This is the plan of the proof of EGA III, Théorème 3.2.1.

## In the Lean code

The theorem is in [FinitenessStep.lean](lean:GroundTheory/ArithmeticGeometry/SchemeCohomology/ProperCohomology/FinitenessStep.lean#L230), and `finiteH_step` in the same file at [line 40](lean:GroundTheory/ArithmeticGeometry/SchemeCohomology/ProperCohomology/FinitenessStep.lean#L40). `Scheme.Modules.SupportedIn` is in [Support.lean](lean:GroundTheory/ArithmeticGeometry/SchemeCohomology/ProperCohomology/Support.lean#L15).

The theorem itself only sets up the induction. Here $T$ is a term of `Closeds X`, and the induction is on the order of `Closeds X`. The hypothesis $T' \subsetneq T$ in `finiteH_step` is on sets, so the proof converts it back.
