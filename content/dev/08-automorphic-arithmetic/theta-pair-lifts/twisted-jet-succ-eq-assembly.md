---
id: twisted-jet-succ-eq-assembly
title: Periods of the row test are multiples of class sums
kind: theorem
decl: GlobalTheory.RowClaim.JetsAssembly.twistedJet_succ_eq_assembly
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.LocalTypeDictionary.TwistedJetSuccEqAssembly
covers: 1004
status: drafted
drafted_by: writer@claude
---
This theorem proves the jet step `StepJets` of the row test. A finite combination of periods, the terms that the [unfolding step](/entry/twisted-theta-integral-unfolding/) produces, is one fixed multiple of a finite sum over classes. Its one user is the renaming [`twisted_jets_assemble`](/entry/twisted-jets-assemble/), and through it the lift formula of [the five properties of the twisted theta lifts](/entry/theta-lift-row-properties-conj/). The proof is a short linearity argument. The content is in the lemma `twisted_pairing_identity`.

## Statement

Assume `ThetaLocalInputs`, the [record of named literature statements](/step/theta-local-inputs-def/), and `SumOKK`, which says that the finite sums of the row test are meaningful. Then for all large admissible choices $\mathrm{ch}$ (in the sense of `Big`), the statement `JetsAt ch` holds ([StepUnfold.lean](lean:Development/AbelianVarietyTheory/Statements/HeckeThetaIntegrals/StepUnfold.lean#L115)). It has two parts.

1. For all $t$, data $\Phi$ and cosets $\beta$, there is a volume $M$ that meets `IsTermVol`: on the column it is at the levels of the term at $\beta$, and on the row at fixed levels.
2. For each finite combination $\sigma$ of polynomial data on the column and the row, there is $\kappa \in \mathbb{C}$ such that for all $t$, $a$, $\beta \in \operatorname{supp}_t(\Phi_a)$, volumes $M$ with `IsTermVol`, expansions $\tau$ with `IsExpansion`, and all $y$:
$$P_M(\sigma, \tau; \varphi_a, F_y) = \kappa \sum_{c} \gamma(c)^{-1}\, \langle \tau, c\rangle\bigl(\tilde\Psi_a(p_c), F'_y(q_c)\bigr).$$

Here $P_M$ (`defTot`) is the finite combination of periods of the [unfolding step](/entry/twisted-theta-integral-unfolding/). The sum (`classSum`) runs over the finite set of classes $c$ at $\beta$, with weight $\gamma(c)^{-1}$ (`invGam`), the pairing `pairAt` of $\tau$ at $c$, and the values of two functions $\tilde\Psi_a$ (`psiC` of $\Psi_a$) and $F'_y$ (`formC`) at two points $p_c$, $q_c$ of the class. The constant $\kappa$ depends on $\sigma$ and the choice, not on $t$, $a$, $\beta$, $M$, $\tau$ or $y$.

## Proof

1. `twisted_jet_one_of_all` gives the statement $\mathrm{Big}(\texttt{JetsOne})$. This is part 2 for $\sigma$ a single basis element $P$, with a constant $\kappa_P$. It is a renaming of `twisted_pairing_identity`.
2. `jetsAt_of_one` gives `JetsAt` from `JetsOne` at each choice. It uses the level condition `s.core.lev` of the setting `HidaSetting`. Part 1 is `StepsModel.exists_isTermVol`. For part 2, `defTot` is linear in $\sigma$ (`defTot_eq_sum`). So $\kappa = \sum_P \sigma(P)\, \kappa_P$ works.

The rest is bookkeeping.

## In the Lean code

The theorem is in [TwistedJetSuccEqAssembly.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedJetSuccEqAssembly.lean#L17). `jetsAt_of_one` is in [JetsOfOrthogonalSum.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/JetsOfOrthogonalSum.lean#L37), and `twisted_pairing_identity` in [PairingOfPointsExpansion.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/PairingOfPointsExpansion.lean#L55).

- The name says "succ eq": a recursion in a successor. The statement and the proof have no successor and no induction.
- The theorem is a near copy of `GlobalTheory.RowClaim.JetsAssembly.stepJets` in [JetsOfOrthogonalSum.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/JetsOfOrthogonalSum.lean#L48). That theorem assumes `Hypotheses₂` instead of `ThetaLocalInputs` and calls `term_volume_class_sum` instead of `twisted_pairing_identity`. The proof text is otherwise the same.
- `ThetaLocalInputs` goes only to `twisted_pairing_identity`, and we have not checked which of its fields that proof uses.
