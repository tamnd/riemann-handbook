---
id: de-rham-extension-potentially-semistable
title: A de Rham extension of potentially semistable blocks (named form)
kind: theorem
decl: GlobalTheory.T.deRhamExtension_potentiallySemistable
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.DeRhamExtensionPotentiallySemistableStatement
covers: 360
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It gives the theorem [`extStep_holds`](/entry/ext-step-holds/), which has the real content, a second name in the namespace `GlobalTheory.T`. Its parent in the spine is [`Red.redStep`](/entry/red-step/), which uses it as the last step of the reducible case.

## Statement

The statement is the proposition `ExtStep`. Use the notation of [`matThm_holds`](/entry/mat-thm-holds/). Let $K$ be a finite extension of $\mathbb{Q}_\ell$, $r$ an integer, and

$$\rho(g) = \begin{pmatrix} \rho_1(g) & c(g) \\ 0 & \rho_2(g) \end{pmatrix}$$

for all $g \in G_K$, with $\rho \colon G_K \to \mathrm{GL}_{a+b}(\mathbb{Q}_\ell^{\mathrm{ur}})$, $\rho_1$ and $\rho_2$ homomorphisms to $\mathrm{GL}_a$ and $\mathrm{GL}_b$, and $c$ any map to $a \times b$ matrices. If `IsRat r ρ`, `AdmDR P ρ`, `AdmSt P ρ₁` and `AdmSt P ρ₂` hold, then `AdmSt P ρ` holds. In words: a de Rham extension of two potentially semistable representations is potentially semistable.

## Proof

The proof is the term `GlobalTheory.PMon.extStep_holds`. Nothing else happens.

## In the Lean code

The theorem is in [DeRhamExtensionPotentiallySemistableStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/DeRhamExtensionPotentiallySemistableStatement.lean#L7). The proof is the tactic `first | exact @GlobalTheory.PMon.extStep_holds | ...`, and the first branch closes the goal. The file sets `maxHeartbeats` to 1000000. `ExtStep` is defined in [TwistStep.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/TwistStep.lean#L50).
