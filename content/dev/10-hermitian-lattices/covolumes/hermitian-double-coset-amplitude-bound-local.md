---
id: hermitian-double-coset-amplitude-bound-local
title: The local amplitude bound for Hermitian double cosets, statement form
kind: theorem
decl: GlobalTheory.T.hermitianDoubleCoset_amplitude_bound_local
module: Development.AbelianVarietyTheory.Proofs.FlagMeasures.HermitianDoubleCosetAmplitudeBoundLocalStatement
covers: 453
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming of [`ngAt`](/entry/ng-at/). Its only user is [`local_nongeneric_bound_record_family`](/entry/local-nongeneric-bound-record-family/), which restates it under the names of the global records. The content is in [`ngAt`](/entry/ng-at/).

## Statement

**Theorem.** Let $C \geq 39$. Let $M$ be a local model with `M.OK`: $F$ is a nonarchimedean local field of characteristic $0$, $E$ is a quadratic $F$-algebra with a conjugation, and $M$ carries a Haar measure on $E$. Let $H$ be a nondegenerate Hermitian space over $E$ of dimension $k + 2r + 1$, with $4r + 7 \leq k$. Let $P$ be a pair of frames in $H$ that satisfies `P.RelG (theta M)`. Then `NGAt k P C` holds.

`NGAt`, `RelG` and `theta` are stated in [the entry for `ngAt`](/entry/ng-at/). In short, `NGAt` bounds three weighted mean squares of oscillating sums over lattices by $H_P^{C(r+1)^2}$ times the total mass, with an extra factor $q^{-(k - 2r - 5)}$ for the part with a nonzero defect.

## Proof

The proof is the term `GlobalTheory.HL.AbstractBound.ngAt`. There is nothing else.

## In the Lean code

The theorem is at [HermitianDoubleCosetAmplitudeBoundLocalStatement.lean line 10](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/HermitianDoubleCosetAmplitudeBoundLocalStatement.lean#L10). The two statements have the same text, so the first branch of the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)` closes the goal. The file sets `maxHeartbeats` to 1,000,000 for this one line.

The name speaks of "double cosets", but no double coset occurs in the statement. The terms of the sums in `NGAt` are lattices up to the action of $N_A \cap N_B$, the intersection of the unipotent groups of the two frames.
