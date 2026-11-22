---
id: theta-lift-adjoint-scalar-formula-injective
title: The scalar formula for the theta lift, and injectivity of its adjoint, the statement form
kind: theorem
decl: GlobalTheory.T.thetaLift_adjoint_scalarFormula_injective
module: Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.ThetaLiftAdjointScalarFormulaInjectiveStatement
covers: 1231
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It states the result of [`upInj`](/entry/up-inj/) and proves it by calling that theorem. The real content is in that entry. In the dominator tree it sits below [membership and bundles at the stronger parameters](/entry/member-bundles-large-unramified-exponents-alt/), in branch 1 of the [unitary hypotheses node](/proof/unitary-hypotheses/).

## Statement

The statement is the statement of [`upInj`](/entry/up-inj/), word for word. In short: let $R$ be a real datum with a face $F$, and let $\Theta_t$ be its theta map at the top of the chain. Assume ten named propositions from the literature, the conditions `Given R F`, that the ideal `D.host.ccK` is the unit ideal, that `R.Sb` equals $P_g$, and that the vacuum vectors are fixed at good places fixed by conjugation. Let $S$ be the set of places of $F$ below $P_g$. Then:

- there is $\kappa_0 > 0$ such that $\Theta_t \Theta_t^*$ acts on the $c$-part of $H_E$ away from $S$ as $\kappa_0 \prod_i z_i$, where $z_i$ are the $L$-values at $(i, t, c)$ (`BForm R S`);
- $\Theta_t^*$ is injective for every $t$ (`UpInj R`).

## Proof

The proof is `first | exact @GlobalTheory.Core.Rk.UpInjRow.upInj | ...`. It applies that theorem.

## In the Lean code

The theorem is in [ThetaLiftAdjointScalarFormulaInjectiveStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ThetaLiftAdjointScalarFormulaInjectiveStatement.lean#L26). It has three users in the same folder: `GlobalTheory.ScalAll.scal_matchUp_upInj` in [ThetaLiftScalarIdentityMatchingAdjointInjective.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ThetaLiftScalarIdentityMatchingAdjointInjective.lean#L38), `GlobalTheory.ThmAFinal.pThmA_short` in [ThetaLiftFirstHypotheses.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ThetaLiftFirstHypotheses.lean#L50) and `GlobalTheory.PosShort.pos_short` in [DefinitePositivityBothLevelsShortList.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/DefinitePositivityBothLevelsShortList.lean#L48). The last two keep only the injectivity half.

The name matches the conclusion: "scalar formula" is `BForm`, and "injective" is `UpInj`. Four hypotheses are not used in the proof below this theorem: `R.Sb = R.Pg`, `WeilSiegelFormulaUnitary`, `SiegelEisensteinContinuation` and `D.host.ccK = ⊤`. The [entry for `upInj`](/entry/up-inj/) says where each one is dropped.
