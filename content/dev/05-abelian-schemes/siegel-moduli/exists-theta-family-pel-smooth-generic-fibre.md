---
id: exists-theta-family-pel-smooth-generic-fibre
title: A PEL theta family with smooth generic fibre (statement form)
kind: theorem
decl: GlobalTheory.T.exists_thetaFamily_pel_smooth_generic_fibre
module: Development.AbelianVarietyTheory.Proofs.ModuliProofs.ExistsThetaFamilyPelSmoothGenericFibreStatement
covers: 558
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`ZM.exists_thetaFam_isPEL_smooth`](/entry/exists-theta-fam-is-pel-smooth/), with the same type. It gives the first group of lemmas in the proof of [`topAmpExists`](/entry/top-amp-exists/): a theta family over $o$ with a PEL structure and a smooth generic fibre. Its dominator in the written proof is the step [EveryCharacter from the literature and VWin](/step/every-character-of-literature/).

## Statement

Assume inputs 2, 3, 8, 9 and 10 of [`topAmpExists`](/entry/top-amp-exists/). Take a CM field $E$, a PEL datum $D$ of signature $(p, q)$, a symplectic basis of its lattice, and ring generators of $\mathcal{O}_E$. Then for each odd prime $n$ there is $j_0$ such that for $j \ge j_0$ and each base $o$ of level $n^{2j}$ of the type `ArBase`, there are a theta family $F$ for the PEL class and a PEL structure on its universal object, and the generic fibre of $F$ over $o$ is smooth of relative dimension $\tfrac{[E:\mathbb{Q}]}{2}\,pq$.

The entry [`exists_thetaFam_isPEL_smooth`](/entry/exists-theta-fam-is-pel-smooth/) states this in full and gives the proof.

## Proof

The proof is the tactic `first | exact @GlobalTheory.ZM.exists_thetaFam_isPEL_smooth | ...`. The first branch closes the goal, since the two types are the same.

## In the Lean code

The theorem is in [ExistsThetaFamilyPelSmoothGenericFibreStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/ExistsThetaFamilyPelSmoothGenericFibreStatement.lean#L13). It is a renaming. Its 558 declarations are those of `exists_thetaFam_isPEL_smooth` and one more, this theorem.
