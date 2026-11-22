---
id: relay-flag-cover-realisation-pullback
title: Square systems on a flag cover, the relay
kind: theorem
decl: GlobalTheory.CompanionTheory.Relay.flag_cover_realisation_pullback
module: Development.AutomorphicSpectrum.Proofs.MetricProofs.FlagCoverRealisationPullback
covers: 1108
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It has the same statement as [square systems on a flag cover](/entry/t-c-sqsys/) and proves it by calling that theorem. The real content is in that entry. Its only user is [the statement form](/entry/t-flag-cover-realisation-pullback/), which is also a relay.

## Statement

Assume `Inputs`. Let $M$ be a flag model with a base metric and analytic flag data of dimension $d$, and let $\mathrm{CR}$ be a realization of these data along a flag cover $M' \to M$. If the coordinate ideal of $M$ is an arithmetic variety of dimension $d + 2$, then for each $\tau$ and each $a$, $b = a + 1$ with $b < j$ or $j \leq a$, there is a square system for $\mathrm{CR}$ at $(\tau, a)$ with coefficients $\xi_{\tau,a} = (1, -2, 1)$ at the columns $a - 1$, $a$, $a + 1$ of row $\tau$. [Square systems on a flag cover](/entry/t-c-sqsys/) explains each object.

## Proof

The proof is `first | exact @PositivityTheory.Xgp.t_c_sqsys | exact PositivityTheory.Xgp.t_c_sqsys`.

## In the Lean code

The theorem is in [FlagCoverRealisationPullback.lean](lean:Development/AutomorphicSpectrum/Proofs/MetricProofs/FlagCoverRealisationPullback.lean#L9). The chain from the statement form to the proof is two relays long. The name speaks of a pullback of a realization, but the conclusion is a square system.
