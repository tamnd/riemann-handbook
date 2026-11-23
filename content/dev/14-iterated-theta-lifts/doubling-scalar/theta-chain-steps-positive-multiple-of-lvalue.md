---
id: theta-chain-steps-positive-multiple-of-lvalue
title: Positive step scalars from the node gap, the statement form
kind: theorem
decl: GlobalTheory.T.thetaChain_steps_positive_multiple_of_LValue
module: Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.ScalarsOfGivenDataStatement
covers: 1169
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It states the result of [`scalars_of_given_all`](/entry/scalars-of-given-all/) and proves it by calling that theorem. The real content is in that entry. Its only user is [`scalars_of_heckeFormNS`](/entry/scalars-of-hecke-form-ns/), which supplies the node gap.

## Statement

Assume `HarishChandraFinite`, `CuspRapidDecay`, `DiscreteSeriesCover`, `HarishChandraModules`, `CasselmanWallach`, `HoweUnram` and `UnramifiedDoublingGL`. Let $R$ be a real datum (`RealDat D A Ks`) with a face $F$. Assume `Given R F`, the node gap `ThetaSourceAction.NodeGap D` (there is $N \ge \operatorname{rank} X' + 1$ with $b_{i+1} - b_i \ge t_D + 2N^3 + 1$ for the nodes $b$ of each parameter `D.hc τ`), and `HeckeFormNS D`. Then [`Scalars R`](/entry/scalars/): there are $\kappa_1, \dots, \kappa_m > 0$ such that step $j$ of the theta chain multiplies inner products by $\kappa_j$ times a positive value of a partial $L$-function at $(1 + t_D)/2$.

## Proof

The proof is `first | exact @GlobalTheory.ChainTw.scalars_of_given_all | ...`. It applies that theorem. The two statements are the same, word for word.

## In the Lean code

The theorem is in [ScalarsOfGivenDataStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ScalarsOfGivenDataStatement.lean#L20). The target `scalars_of_given_all` is in [ScalarsOfGivenData.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ScalarsOfGivenData.lean#L48). Its proof assembles about twenty-five lemmas and ends with `chainStep_scalars_of_realisation`. There `HeckeFormNS D` goes to `thetaLiftChainStep_exact_innerProduct`, and the node gap goes to `twistedChain_step_constants_tuple_indep` and `chainStep_scalars_of_realisation`.

The name matches the conclusion: `Scalars` says that each step scalar is a positive multiple of an $L$-value.
