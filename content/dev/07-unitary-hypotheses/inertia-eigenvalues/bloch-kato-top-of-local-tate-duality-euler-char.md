---
id: bloch-kato-top-of-local-tate-duality-euler-char
title: The top local theorem from Tate duality and the Euler characteristic, a second name
kind: theorem
decl: GlobalTheory.T.blochKatoTop_of_localTateDuality_eulerChar
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.BlochKatoTopOfLocalTateDualityEulerCharStatement
covers: 1650
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the top local theorem](/entry/bloch-kato-top-of-local-tate-duality-euler-char-alt/). That entry has the content. Its user is [the congruence bound along a family](/entry/nlink-e-main-alt-alt/), which applies it with the three literature hypotheses of the [third place hypotheses](/step/unitary-group-third-place-hypotheses-def/).

## Statement

**Theorem.** Assume `BlochKatoLocal`, local Tate duality `LocalTateDualityK` and the local Euler characteristic formula `LocalEulerCharK`. Then for each datum $D$ and all local data $HW$, $F$, $Cm$ over it, the statement `aux₃ D HW F` holds.

`aux₃ D HW F` says: for each prime $\ell$, each unramified finite extension $K$ of $\mathbb{Q}_\ell$ with $\ell \neq 2$, each coefficient field $L$ that is good for $K$, and each irreducible $\lambda$ in the integers of $L$, three descriptions of admissible cocycles hold. It is stated in full in [the twisted lattice cohomology theorem](/entry/twisted-lattice-cohomology-theorem-top/).

## Proof

The proof applies `GlobalTheory.TopClosing.blochKatoTop_of_localTateDuality_eulerChar_alt`, which has the same statement. Nothing else happens.

## In the Lean code

The theorem is in [BlochKatoTopOfLocalTateDualityEulerCharStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/BlochKatoTopOfLocalTateDualityEulerCharStatement.lean#L8). The proof is a `first | exact ... | ...` combinator with three tries. Each try applies the same lemma. The file has `set_option maxHeartbeats 1000000` (line 7), which a one-line proof does not need. The file is named as a statement file, but it imports the proof module (line 2) and only renames it.

The name says "Bloch-Kato", but the hypothesis `BlochKatoLocal` is not used: the proof of the second name drops it at once. The conclusion does not depend on $Cm$.
