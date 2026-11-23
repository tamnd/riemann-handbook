---
id: ordinary-selmer-vanishes-of-dual-vanishes
title: The ordinary Selmer group vanishes if the dual one does, by name
kind: theorem
decl: GlobalTheory.T.ordinarySelmer_vanishes_of_dual_vanishes
module: Development.AbelianVarietyTheory.Proofs.FoundationProofs.OrdinarySelmerVanishesOfDualVanishesStatement
covers: 350
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`grZero_of_grZero_dual1`](/entry/gr-zero-of-gr-zero-dual1/). It is the third of the four steps of [`es_vanish`](/entry/es-vanish/): after the dual ordinary Selmer group of $W$ is shown to vanish, this step gives the vanishing of the ordinary Selmer group of $W$ itself. The mathematics is in [the entry for `grZero_of_grZero_dual1`](/entry/gr-zero-of-gr-zero-dual1/).

## Statement

Assume the literature statements $\mathrm{LitCoh}$ on [[Galois cohomology|9MPCZ3EAJM]]. Let $\ell$ be a prime, $e \in \mathbb{N}$, $S$ a finite set of primes, $A$ a valuation ring of $\overline{\mathbb{Q}}$ and $W \colon G_\mathbb{Q} \to \mathrm{GL}_2(\overline{\mathbb{Q}}_\ell)$ a representation in the normal form $\mathrm{Nf}(e, S, A, W)$. Let $W^* = W \otimes \bar\chi\,(\det W)^{-1}$, with $\bar\chi$ the [[cyclotomic character|XSGB5K2KEG]].

**Theorem.** If the ordinary Selmer group of $W^*$ at $A$ is zero, then the ordinary Selmer group of $W$ at $A$ is zero.

The predicate $\mathrm{GrZero}$ and the twist $W^*$ are defined in [the entry for `grZero_of_grZero_dual1`](/entry/gr-zero-of-gr-zero-dual1/).

## Proof

The proof is the single term `GlobalTheory.Ord2.grZero_of_grZero_dual1`. Nothing else happens.

## In the Lean code

The theorem is at [line 6 of OrdinarySelmerVanishesOfDualVanishesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/OrdinarySelmerVanishesOfDualVanishesStatement.lean#L6). The two statements are the same word for word. The proof is a tactic `first | … | … | …` that tries three ways to give the same term. The size 350 is the subtree of `grZero_of_grZero_dual1` (349) plus this declaration.
