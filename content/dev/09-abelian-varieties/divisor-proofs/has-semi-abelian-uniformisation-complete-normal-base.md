---
id: has-semi-abelian-uniformisation-complete-normal-base
title: Mumford's construction over a complete normal local base (statement)
kind: theorem
decl: GlobalTheory.T.hasSemiAbelianUniformisation_complete_normal_base
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.HasSemiAbelianUniformisationCompleteNormalBaseStatement
covers: 3457
status: drafted
drafted_by: writer@claude
---
This theorem is a restatement of [`Mum.has_of_base`](/entry/has-of-base/), which has the real content. Its proof only calls that theorem. Three lemmas of this folder use it: `Mum.exists_canonOn_of_isMonomialTau`, `MumDesc.image_unif` and `UChart.exists_sab_pelUnif_of_norm`. Its place in the proof is under the literature layer, the step [EveryCharacter from the literature and VWin](/step/every-character-of-literature/).

## Statement

Let $R$ be a local domain with maximal ideal $\mathfrak{m}$. Suppose that $R$ is noetherian, integrally closed, $\mathfrak{m}$-adically complete and of characteristic zero (the predicate `Base R`). Let $D$ be degeneration data over $R$ for $\mathfrak{m}$. Then there are a semi-abelian scheme $G$ over $\operatorname{Spec} R$, a polarised abelian variety $A$ over $\operatorname{Frac}(R)$ and a uniformisation of $G$ by $D$ with generic fibre $A$ (the predicate `Has D`).

The [entry for `has_of_base`](/entry/has-of-base/) unfolds the degeneration data and the uniformisation. The statement has the shape of Mumford's construction (D. Mumford, An analytic construction of degenerating abelian varieties over complete rings, Compositio Math. 24 (1972); Faltings and Chai, *Degeneration of Abelian Varieties*, Springer 1990, Chapter III), for the ideal $\mathfrak{m}$ and with the extra hypothesis of characteristic zero.

## Proof

The proof is `Mum.has_of_base`.

## In the Lean code

The theorem is in [HasSemiAbelianUniformisationCompleteNormalBaseStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasSemiAbelianUniformisationCompleteNormalBaseStatement.lean#L13). The proof is the tactic `first | exact @GlobalTheory.Mum.has_of_base | ...`. The two statements are identical, so `exact` with that theorem closes the goal.

The name says "complete normal base". The hypothesis `Base R` also asks for a noetherian ring of characteristic zero.
