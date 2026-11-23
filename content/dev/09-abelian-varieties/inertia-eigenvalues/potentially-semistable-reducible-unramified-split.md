---
id: potentially-semistable-reducible-unramified-split
title: The reducible case of the monodromy induction (named form)
kind: theorem
decl: GlobalTheory.T.potentially_semistable_reducible_unramified_split
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.PotentiallySemistableReducibleUnramifiedSplitStatement
covers: 389
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It gives the theorem [`Red.redStep`](/entry/red-step/), which has the real content, a second name in the namespace `GlobalTheory.T`. Its parent in the spine is [`matThm_holds`](/entry/mat-thm-holds/), where it is step 4 of the induction on the size $n$.

## Statement

The statement is the proposition `RedStep`. Let $K$ be a finite extension of $\mathbb{Q}_\ell$, $r > 0$, and $\rho \colon G_K \to \mathrm{GL}_n(\mathbb{Q}_\ell^{\mathrm{ur}})$ with `IsRat r ρ` and `AdmDR P ρ`, as in [`matThm_holds`](/entry/mat-thm-holds/). Assume `Splits r ρ`: after conjugation by a matrix with entries fixed by $\mathrm{Fr}^r$, $\rho$ is block upper triangular with two nonempty diagonal blocks. Assume that `MatThm` holds for all sizes $a < n$, with the same $K$ and $r$. Then `AdmSt P ρ` holds: $\rho$ is semistable over a finite extension of $K$.

The entry [`redStep`](/entry/red-step/) gives the proof.

## Proof

The proof is the term `GlobalTheory.PMon.Red.redStep`. Nothing else happens.

## In the Lean code

The theorem is in [PotentiallySemistableReducibleUnramifiedSplitStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/PotentiallySemistableReducibleUnramifiedSplitStatement.lean#L7). The proof is the tactic `first | exact @GlobalTheory.PMon.Red.redStep | ...`, and the first branch closes the goal. The file sets `maxHeartbeats` to 1000000. `RedStep` is defined in [TwistStep.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/TwistStep.lean#L66). In the name, "unramified split" refers to the splitting by a matrix over $\mathbb{Q}_\ell^{\mathrm{ur}}$.
