---
id: exists-breuil-kisin-frame-semistable-bounded-jumps
title: A Breuil-Kisin frame for a semistable lattice, second name
kind: theorem
decl: GlobalTheory.T.exists_breuilKisinFrame_semistable_boundedJumps
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ExistsBreuilKisinFrameSemistableBoundedJumpsStatement
covers: 351
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [exists_frame_sst](/entry/exists-frame-sst/). It has the same statement, and its proof only calls that theorem. Its two users, `frEx_holds` and `closed_of_cover`, apply it to each layer of a tower of $\mathbb{Z}_\ell$-lattices. Both are below [coreAll_of](/entry/core-all-of/); `frEx_holds` leads to its input `ClosedPhi`. The content is in [exists_frame_sst](/entry/exists-frame-sst/). Below it are 351 declarations.

## Statement

Let $\ell$ be a prime, $K/\mathbb{Q}_\ell$ a finite extension, `bk` a Breuil-Kisin datum for $K$ and $\tau \in A_{\inf}$ a period for it. Let $P$, `AI`, `T` be the data of the period rings. Let $N, d \in \mathbb{N}$ and let $\rho \colon G_K \to \mathrm{GL}_d(\mathbb{Z}_\ell)$ be continuous, with $V = \rho \otimes \mathbb{Q}_\ell$ semistable and with Hodge-Tate jumps in $[-N, N]$.

**Theorem.** There is a Breuil-Kisin frame of height $N$ for $\rho$ that is de Rham, and crystalline if $V$ is crystalline.

Each object is unfolded in [the entry of exists_frame_sst](/entry/exists-frame-sst/).

## Proof

The proof is `GlobalTheory.BKLim.exists_frame_sst`, applied with `exact`.

## In the Lean code

The theorem is in [ExistsBreuilKisinFrameSemistableBoundedJumpsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsBreuilKisinFrameSemistableBoundedJumpsStatement.lean#L11). Its type is the type of `exists_frame_sst` word for word, and the proof is a `first` combinator that tries three ways to apply it. The users are [FrExHolds.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ClosedPhiFunctoriality/FrExHolds.lean#L31) and [ClosedOfCover.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ClosedOfCover.lean#L185). In `frEx_holds`, the bound $N$ is the largest absolute value of a Hodge-Tate jump in the given multisets, and the jump condition comes from `layer_DdR_bounds_alt`.
