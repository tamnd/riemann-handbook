---
id: theta-chain-step-positive-scalar-standing-hypotheses
title: Positive step scalars of the theta chain, the statement form
kind: theorem
decl: GlobalTheory.T.thetaChainStep_positive_scalar_standingHypotheses
module: Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.ThetaChainStepPositiveScalarStandingHypothesesStatement
covers: 1172
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It states the result of [`scalars`](/entry/scalars/) and proves it by calling that theorem. The real content is further down, in [`scalars_of_given_all`](/entry/scalars-of-given-all/). Its only user is [`upInj`](/entry/up-inj/), where it gives the step scalars that `ChainScalar.bForm` composes into the scalar formula for the top theta map.

## Statement

The statement is the statement of [`scalars`](/entry/scalars/), word for word. Assume the ten named propositions `DiscreteSeriesCover`, `HarishChandraFinite`, `HarishChandraModules`, `CasselmanWallach`, `CuspRapidDecay`, `HoweUnram`, `WeilSiegelFormulaUnitary`, `HeckeFormNS D'` for all $D'$, `SiegelEisensteinContinuation` and `UnramifiedDoublingGL`. Let $R$ be a real datum with a face $F$. If `Given R F` holds and the ideal `D.host.ccK` is the unit ideal, then `Scalars R`: there are $\kappa_1, \dots, \kappa_m > 0$ such that step $j$ of the theta chain multiplies inner products by $\kappa_j$ times a positive value of a partial $L$-function at $(1 + t_D)/2$. The [entry for `scalars`](/entry/scalars/) states `Scalars` in full.

## Proof

The proof is `first | exact @GlobalTheory.Core.Rk.ScalarsRow.scalars | ...`. It applies that theorem.

## In the Lean code

The theorem is in [ThetaChainStepPositiveScalarStandingHypothesesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ThetaChainStepPositiveScalarStandingHypothesesStatement.lean#L26). It is used once, in [ThetaLiftAdjointScalarFormulaInjective.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ThetaLiftAdjointScalarFormulaInjective.lean#L34).

Three of its hypotheses are not used: `WeilSiegelFormulaUnitary`, `SiegelEisensteinContinuation` and `D.host.ccK = ⊤`. The proof of `scalars` discards them. "Standing hypotheses" in the name refers to no object of the statement.
