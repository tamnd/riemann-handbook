---
id: strict-vanishing-dual-of-literature
title: The strict dual Selmer group vanishes, by name
kind: theorem
decl: GlobalTheory.T.strict_vanishing_dual_of_literature
module: Development.AbelianVarietyTheory.Proofs.FoundationProofs.StrictVanishingDualOfLiteratureStatement
covers: 303
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`StrictKill.main`](/entry/strict-kill-main/). It is the first of the four steps of [`es_vanish`](/entry/es-vanish/): from an Euler system class for $W$, it makes the strict Selmer group of the Tate dual $W^*$ vanish. The next steps of `es_vanish` pass from this to the ordinary Selmer group of $W^*$ and then, through [`ordinarySelmer_vanishes_of_dual_vanishes`](/entry/ordinary-selmer-vanishes-of-dual-vanishes/), to that of $W$. The mathematics is in [the entry for `StrictKill.main`](/entry/strict-kill-main/).

## Statement

Assume $\mathrm{LitCoh}$, the literature statements on [[Galois cohomology|9MPCZ3EAJM]]. Let $W \colon G_\mathbb{Q} \to \mathrm{GL}_2(\overline{\mathbb{Q}}_\ell)$ satisfy the normal form $\mathrm{Nf}(e, S, A, W)$ of [the unramified zeta theorem](/entry/zeta-ur/), and let $W^* = W \otimes \bar\chi\,(\det W)^{-1}$.

**Theorem.** If $W$ has an Euler system class $\mathrm{ES}(W, A)$, then $\mathrm{StrZero}(W^*, A)$ holds: every continuous cocycle of $W^*$ that is unramified at all primes $w \neq \ell$ and a coboundary on the decomposition group at $A$ is a coboundary.

$\mathrm{ES}$ is stated in [the entry for the unramified zeta theorem](/entry/zeta-ur/), which proves it under a further hypothesis on a modular source.

## Proof

The proof is the single term `GlobalTheory.Ord2.StrictKill.main`. Nothing else happens.

## In the Lean code

The theorem is at [line 7 of StrictVanishingDualOfLiteratureStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/StrictVanishingDualOfLiteratureStatement.lean#L7). The two statements are the same word for word. The proof is a tactic `first | … | … | …` that tries three ways to give the same term. The name says "of literature", but the only literature input is the hypothesis $\mathrm{LitCoh}$, which `StrictKill.main` also takes.
