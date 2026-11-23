---
id: kodaira-spencer-of-commuting-heat-operators-raynaud
title: The symbol of a commuting heat operator is the Kodaira-Spencer matrix (statement form)
kind: theorem
decl: GlobalTheory.T.kodairaSpencer_of_commuting_heat_operators_raynaud
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.KodairaSpencerOfCommutingHeatOperatorsRaynaudStatement
covers: 515
status: drafted
drafted_by: writer@claude
---
This theorem is the statement form of [`isKS_of_heat`](/entry/is-ks-of-heat/), which has the real content. It sits under the [log Kodaira-Spencer isomorphism](/entry/has-log-ks/): the boundary-chart lemmas `exists_isKS_of_heat` and `exists_basis_isKS_symbol` call it.

## Statement

Let $G$ be a semi-abelian scheme over a complete Noetherian local domain $R \supseteq \mathbb{Q}$, with an $\mathcal{O}_E$-action and a Mumford uniformisation, whose periods are monomial in nonzero $t_1, \dots, t_m$ and whose abelian locus is $\{t_1 \cdots t_m \neq 0\}$. Let $h$ be a basic heat operator for a derivation $D$ on the Raynaud extension, with defect 0, and let $v'$ be the tangent frame of $G$ that matches the frame of the Raynaud extension. Then over $\operatorname{Spec} R[1/(t_1 \cdots t_m)]$ the symbol $\Theta$ of $h$ is the Kodaira-Spencer matrix of $D$ in the frame $v'$ (`IsKS`).

The full list of hypotheses is in [the entry of the proof](/entry/is-ks-of-heat/).

## Proof

The proof is one line: it applies `GlobalTheory.KBracket.isKS_of_heat`.

## In the Lean code

The theorem is in [KodairaSpencerOfCommutingHeatOperatorsRaynaudStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KodairaSpencerOfCommutingHeatOperatorsRaynaudStatement.lean#L17). Its statement is the same as that of `isKS_of_heat`, word for word, and the proof is the tactic `first | exact @GlobalTheory.KBracket.isKS_of_heat | ...`. It is a second name and adds nothing.
