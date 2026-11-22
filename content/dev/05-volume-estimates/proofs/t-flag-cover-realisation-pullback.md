---
id: t-flag-cover-realisation-pullback
title: Square systems on a flag cover, the statement form
kind: theorem
decl: GlobalTheory.T.flag_cover_realisation_pullback
module: Development.AutomorphicSpectrum.Proofs.MetricProofs.FlagCoverRealisationPullbackStatement
covers: 1109
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It states that square systems exist on a flag cover, and its proof calls [the relay](/entry/relay-flag-cover-realisation-pullback/), which calls [square systems on a flag cover](/entry/t-c-sqsys/). The real content is in that last entry. Two proofs use this theorem: the tie lemma `tie_of`, which feeds [the swap relation from seven statements](/entry/good-tower-antisymmetry-of/), and `flagVarieties_flagSys`. Both sit below [the volume theorem from its inputs](/entry/volume-theorem-x-of-inputs/).

## Statement

The statement is the same as in [square systems on a flag cover](/entry/t-c-sqsys/): assume `Inputs`, a flag model $M$ with a base metric and analytic flag data of dimension $d$, and a realization along a flag cover $M' \to M$. If the coordinate ideal of $M$ is an arithmetic variety of dimension $d + 2$, then each adjacent pair $(\tau, a)$, $b = a + 1$ with $b < j$ or $j \leq a$, has a square system with coefficients $\xi_{\tau,a}$.

## Proof

The proof is `first | exact @GlobalTheory.CompanionTheory.Relay.flag_cover_realisation_pullback | ...`. It applies the relay.

## In the Lean code

The theorem is in [FlagCoverRealisationPullbackStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/MetricProofs/FlagCoverRealisationPullbackStatement.lean#L8). Its users are in [ChooseTwoAdd.lean](lean:Development/WeilBound/CoreStatements/MultihomogeneousSquares/ChooseTwoAdd.lean#L88) and [FlagVarietyAnalyticSystemExists.lean](lean:Development/AutomorphicSpectrum/Proofs/MetricProofs/FlagVarietyAnalyticSystemExists.lean#L49).

The name is misleading. The conclusion is the existence of a square system. The realization of the cover is a hypothesis, and the pullbacks appear only inside the proof of [square systems on a flag cover](/entry/t-c-sqsys/).
