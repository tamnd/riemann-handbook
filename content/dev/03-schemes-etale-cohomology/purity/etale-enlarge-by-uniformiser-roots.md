---
id: etale-enlarge-by-uniformiser-roots
title: Roots of uniformisers make the closure of a torsor étale, statement form
kind: theorem
decl: GlobalTheory.T.etale_enlarge_by_uniformiser_roots
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.EtaleEnlargeByUniformiserRootsStatement
covers: 416
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the étale enlargement](/entry/etale-enlarge/). It is the third step of [the enlargement to a good model](/entry/enlarge-good/): after the first two steps give a model with a retraction and a point at zero, this step makes the integral closure of the $\mathbb{Z}/q$-torsor étale in codimension one over the base.

## Statement

The statement is word for word the statement of `GlobalTheory.KeyOriginEnlarge.etale_enlarge`. In short: given a noetherian model over $A$ (an étale neighbourhood $R$ of the origin of $A[X]$ with a map to a strict henselisation $O$ of $T[X]$, and a $\mathbb{Z}/q$-torsor $D$ over the generic fibre of $R$), with a retraction $\rho \colon R \to A$ and a point at zero, there is a good model over some $A'$: the integral closure of $R'$ in $D'$ is also étale over $R'$ at each prime above a prime of height at most one of $A'$. Ring maps of generic fibres and of torsor algebras link the two models. The definitions are in the entry for `etale_enlarge`.

## Proof

The proof is one tactic line: `exact @GlobalTheory.KeyOriginEnlarge.etale_enlarge`. All the content is in [the étale enlargement](/entry/etale-enlarge/).

## In the Lean code

The theorem is in [EtaleEnlargeByUniformiserRootsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/EtaleEnlargeByUniformiserRootsStatement.lean#L10). The proof is `first | (exact @etale_enlarge) | ...`, with two fallback tactics. The file imports `Mathlib` twice. The parent `enlarge_good` calls this name, not `etale_enlarge`.
