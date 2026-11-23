---
id: multiplier-vanishing-nef-twist
title: Vanishing on a log resolution for the rounded-down divisor, second name
kind: theorem
decl: GlobalTheory.T.multiplier_vanishing_nef_twist
module: Development.WeilBound.CoreStatements.PublishedTheorems.NadelVanishingPairs.NadelVanishingLemmas.MultiplierVanishingNefTwistStatement
covers: 608
status: drafted
drafted_by: writer@claude
---
This theorem is a second name of [`vanishing_logRes_floor`](/entry/vanishing-log-res-floor/). It has the same statement and its proof is that theorem. The real content is in that entry. Its only user is [`vanishing_logRes_pushforward_and_local`](/entry/vanishing-log-res-pushforward-and-local/), which pushes the vanishing down to $X$.

## Statement

The hypotheses are those of [`vanishing_logRes_pushforward_and_local`](/entry/vanishing-log-res-pushforward-and-local/): a log resolution $s \colon Y \to X$ over a field of characteristic $0$, the divisor $F = \lfloor s^*G/m \rfloor - K$ on $Y$, and line bundles $N$, $M$, $T$ on $X$ with $T = mr\,N - r\,G - m\,M$, $M$ and $T$ nef, and $a\,s^*M = A + F_d$ with $A$ ample.

**Theorem.** For each line bundle $Q$ on $Y$ with $Q = s^*N - F$ in $\operatorname{Pic} Y$, $H^i(Y, Q) = 0$ for all $i > 0$.

## Proof

The proof applies `GlobalTheory.Discrepancy.vanishing_logRes_floor`. The rest is bookkeeping.

## In the Lean code

The theorem is in [MultiplierVanishingNefTwistStatement.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/MultiplierVanishingNefTwistStatement.lean#L11). The proof is the tactic `first | exact @vanishing_logRes_floor | ...`, which tries three ways to close the goal with that theorem.

The name speaks of a multiplier ideal. The statement is about the cohomology of a line bundle on $Y$; no multiplier ideal appears.
