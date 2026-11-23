---
id: exists-theta-setup-ideal-over-clopen-component
title: A theta setup and a boundary ideal over one component (statement form)
kind: theorem
decl: GlobalTheory.T.exists_thetaSetup_ideal_over_clopen_component
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsThetaSetupIdealOverClopenComponentStatement
covers: 421
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It repeats [`exists_setup_ideal_over_component`](/entry/exists-setup-ideal-over-component/), which has the real content. Its one user is [`idealSt_holds`](/entry/ideal-st-holds/). That theorem applies it to each clopen irreducible piece of $Z$. The unitary analogue is [`exists_unitaryThetaSetup_ideal_over_component`](/entry/exists-unitary-theta-setup-ideal-over-component/).

## Statement

Use the theta compactification $i \colon X \to Z$, the traits and the polarization function $\varphi$ as in [`poinSt`](/entry/poin-st/), and theta setups as in [the entry with the proof](/entry/exists-setup-ideal-over-component/).

**Theorem.** Let $g \geq 1$, let $n \geq 3$ be odd, and let $W \subset Z$ be clopen and irreducible. Then there are an $8 \times 8$ integral matrix $W_8$, a theta setup for $(W_8, i)$ with finite map $\pi \colon M \to Z$, an integer $\iota \geq 1$ and an ideal $J_1$ on $M$ with $\pi(M) = W$, $\pi(\operatorname{supp} J_1) \cap i(X) = \emptyset$, and $\xi_1^* J_1 = (\varpi^{\iota\varphi(\beta)})$ for each trait and each $\xi_1 \colon \operatorname{Spec} V \to M$ with $\pi \circ \xi_1$ extending $i \circ y$.

## Proof

The statement is the same as that of `GlobalTheory.Poinc.exists_setup_ideal_over_component`, and the proof applies it.

## In the Lean code

The theorem is in [ExistsThetaSetupIdealOverClopenComponentStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsThetaSetupIdealOverClopenComponentStatement.lean#L11). The proof is `first | exact @GlobalTheory.Poinc.exists_setup_ideal_over_component | ...`, a tactic that tries the alias in three forms. The type is copied word for word from the theorem it calls.
