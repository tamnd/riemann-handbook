---
id: isogeny-representable-finite-etale
title: Isogenies killed by k form a finite étale scheme, a renaming
kind: theorem
decl: GlobalTheory.T.isogeny_representable_finite_etale
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.IsogenyRepresentableFiniteEtaleStatement
covers: 399
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [isogeny_rep](/entry/isogeny-rep/), which has the real content. It says that the isogenies out of an abelian scheme $A/S$ that have a quasi-inverse for an integer $k$ invertible on $S$ are classified by a finite étale $S$-scheme. [exists_rep](/entry/isog-rep-exists-rep/) applies it with $k = c$, a power of the prime $p$, to the abelian scheme `o.A` of an object `o` of its moduli problem. Below this theorem are 399 declarations.

## Statement

The statement is word for word that of [isogeny_rep](/entry/isogeny-rep/): for $S$ locally noetherian, $A/S$ an abelian scheme and $k > 0$ invertible on $S$, there is a finite étale $Y \to S$ with a universal pair $\psi \colon A_Y \to B$, $\psi' \colon B \to A_Y$ with $\psi' \circ \psi = [k]$ and $\psi \circ \psi' = [k]$, such that each such pair over an $S$-scheme $T$ is the pullback of the universal one along a unique $S$-map $T \to Y$.

## Proof

The proof is `first | exact @GlobalTheory.UPel.HT.ES.IsogRep.isogeny_rep | ...`. The first alternative closes the goal, since the two statements are the same.

## In the Lean code

The theorem is in [IsogenyRepresentableFiniteEtaleStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsogenyRepresentableFiniteEtaleStatement.lean#L8). The `first` tactic lists four more alternatives, `ker_iff_of_pullbacks` and `exists_quot_quasiInv` with and without `@`. They have other statements and are never tried. The file imports `Mathlib` twice.
