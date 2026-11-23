---
id: scalars-of-hecke-form-ns
title: Positive step scalars from the inner product formula for theta lifts and a parameter choice
kind: theorem
decl: GlobalTheory.Core.Rk.ScalarsRow.scalars_of_heckeFormNS
module: Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.ThetaChainStepPositiveScalarStandingHypotheses
covers: 1170
status: drafted
drafted_by: writer@claude
---
This theorem proves [`Scalars R`](/entry/scalars/) for a real datum $R$: each step of its theta chain multiplies inner products by a positive constant times an $L$-value. Its one piece of work is to get a gap between the nodes of the parameter of $D$ from the parameter choice in `Given R F`. Then it calls [the statement form](/entry/theta-chain-steps-positive-multiple-of-lvalue/) of [`scalars_of_given_all`](/entry/scalars-of-given-all/), which has the real content. Its only user is [`scalars`](/entry/scalars/).

## Statement

Assume the seven propositions `DiscreteSeriesCover`, `HarishChandraFinite`, `HarishChandraModules`, `CasselmanWallach`, `CuspRapidDecay`, `HoweUnram` and `UnramifiedDoublingGL`, and `HeckeFormNS D` for every datum $D$. Let $R$ be a real datum (`RealDat D A Ks`) with a face $F$. If `Given R F` holds, then `Scalars R`.

`HeckeFormNS D` is a hypothesis, not a theorem. For a pair of hermitian spaces $A, B$ with a Weil representation, two Fock vectors $\Phi_1, \Phi_2$ unramified away from $S$, and two forms $u_1, u_2$ on $A$ with a parameter family, it says, under conditions on $t$, on the Witt index of $B$ and on the integrand: the theta lifts of $u_1$ and $u_2$ to $B$ converge, an integral over the set `openOff` converges, and the Petersson product of the two lifts equals a volume times $L^S(t/2 + 1/2, \text{par}, \chi_B)$ divided by a normalizing factor `dSfun`, times that integral. This has the shape of a Rallis inner product formula. We have not checked it against a published form.

## Proof

1. From `Given R F`, take a size datum $L$ and a parameter choice $P$ (`ParameterChoice' D L`).
2. `P.nodeGap_ge_cubic_rank` gives `D.NodeGap h` with $h = 4N^3 + 2t_D + 6$, where $N$ is `D.R.N D.R.m`. This says: for every word $u$, every $\tau$ and $j + 1 < m$, the nodes $b$ of `D.hcW u τ` satisfy $b_{j+1} - b_j \ge h$.
3. `harishChandraNodesFarApart_of_cubic_node_gap` turns this into `ThetaSourceAction.NodeGap D`: there is $N \ge \operatorname{rank} X' + 1$ with $b_{i+1} - b_i \ge t_D + 2N^3 + 1$ for the nodes of `D.hc τ`. It takes $N$ as above, uses $N = \operatorname{rank} X' + 1$ (`factXm`), the word $u_0$ and `D.hcW_b`. The inequality follows from $t_D \ge 0$ and $N^3 \ge 0$.
4. [`thetaChain_steps_positive_multiple_of_LValue`](/entry/theta-chain-steps-positive-multiple-of-lvalue/) gives `Scalars R` from the seven propositions, `Given R F`, the node gap and `HeckeFormNS D`.

## In the Lean code

The theorem is in [ThetaChainStepPositiveScalarStandingHypotheses.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ThetaChainStepPositiveScalarStandingHypotheses.lean#L29). The lemmas it calls:

- `Formalism.BasicNotions.ParameterChoice'.nodeGap_ge_cubic_rank` in [HeightBoundGeFourthPowerRank.lean](lean:Formalism/LocalRingCardinality/HeightBoundGeFourthPowerRank.lean#L89);
- `GlobalTheory.Core.Rk.GapOfNodes.harishChandraNodesFarApart_of_cubic_node_gap` in [HarishChandraNodesFarApartOfCubicNodeGap.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/HarishChandraNodesFarApartOfCubicNodeGap.lean#L10);
- `GlobalTheory.T.thetaChain_steps_positive_multiple_of_LValue`.

`HeckeFormNS` is in [HeckeFormNSOfHeckeForm.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/HeckeFormNSOfHeckeForm.lean#L202). The hypothesis asks for `HeckeFormNS` at every datum, but the proof uses it only at $D$. The size datum $L$ of step 1 is not used.
