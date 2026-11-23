---
id: exists-unitary-theta-setup-ideal-over-component
title: A theta setup and a boundary ideal over one component (statement form)
kind: theorem
decl: GlobalTheory.T.exists_unitaryThetaSetup_ideal_over_component
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsUnitaryThetaSetupIdealOverComponentStatement
covers: 440
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`exists_uSetup_ideal_over_component`](/entry/exists-u-setup-ideal-over-component/), which has the real content. Its one user is [`uIdealSt_holds`](/entry/u-ideal-st-holds/). That theorem applies it to each irreducible component of the compactification $Z$ that meets the interior, and then pushes the ideal down to $Z$.

## Statement

Use the compactification $C$ (a `UCompact`, see [the theta compactification](/entry/umin-theta-compactification-exists/)), the fan function $\varphi$ and the condition `UValThru` from [the entry with the proof](/entry/exists-u-setup-ideal-over-component/).

**Theorem.** Assume $p + q \geq 1$ and `IsPolFan` for $\varphi$ in rank $\min(p, q)$. Let $A \subset Z$ be clopen and irreducible, with $A \cap i(X^\circ_F) \neq \emptyset$. Then there are a theta setup $X_1$ over $C$ with finite map $\pi \colon M \to Z$, an integer $\iota \geq 1$ and an ideal sheaf $J_1$ on $M$ such that $\pi(M) = A$, $\pi$ maps the support of $J_1$ outside $i(X^\circ_F)$, and `UValThru` holds for $J_1$ through $\pi$ with exponent $\iota$.

## Proof

The statement is the same as that of `GlobalTheory.UPoinc.exists_uSetup_ideal_over_component`, and the proof applies it.

## In the Lean code

The theorem is in [ExistsUnitaryThetaSetupIdealOverComponentStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsUnitaryThetaSetupIdealOverComponentStatement.lean#L12). The proof is `first | exact @GlobalTheory.UPoinc.exists_uSetup_ideal_over_component | ...`, a tactic that tries the alias in three forms. The type is copied word for word from the theorem it calls.
