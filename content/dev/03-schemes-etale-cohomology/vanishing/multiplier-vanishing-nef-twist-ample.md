---
id: multiplier-vanishing-nef-twist-ample
title: Nadel vanishing and local vanishing on a log resolution, second name
kind: theorem
decl: GlobalTheory.T.multiplier_vanishing_nef_twist_ample
module: Development.WeilBound.CoreStatements.PublishedTheorems.NadelVanishingPairs.NadelVanishingLemmas.MultiplierVanishingNefTwistAmpleStatement
covers: 702
status: drafted
drafted_by: writer@claude
---
This theorem is a second name of [`vanishing_logRes_pushforward_and_local`](/entry/vanishing-log-res-pushforward-and-local/). It has the same statement and its proof is that theorem. The real content is in that entry. Through two users this name reaches [EveryCharacter from the literature and VWin](/step/every-character-of-literature/). Below it are 702 declarations.

## Statement

The hypotheses and the conclusion are those of [`vanishing_logRes_pushforward_and_local`](/entry/vanishing-log-res-pushforward-and-local/), word for word. In short: let $s \colon Y \to X$ be a log resolution over a field of characteristic $0$, let $F = \lfloor s^*G/m \rfloor - K$, and let the line bundle $N$ on $X$ satisfy $N = \tfrac1m G + \tfrac1r M + \tfrac1{mr} T$ with $M$, $T$ nef and $s^*M$ big. Then $H^i(X, s_*\mathcal{O}_Y(-F) \otimes N) = 0$ for $i > 0$, and $H^j(s^{-1}U, \mathcal{O}_Y(-F) \otimes s^*N) = 0$ for $j > 0$ and each affine open $U \subseteq X$.

## Proof

The proof applies `GlobalTheory.vanishing_logRes_pushforward_and_local`. The rest is bookkeeping.

## In the Lean code

The theorem is in [MultiplierVanishingNefTwistAmpleStatement.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/MultiplierVanishingNefTwistAmpleStatement.lean#L11). The proof is the tactic `first | exact @vanishing_logRes_pushforward_and_local | ...`, which tries three ways to close the goal with that theorem.

The theorem has two users:

- `nadel_of_logRes` in [MultiplierIdealBoundaryMonotone.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/MultiplierIdealBoundaryMonotone.lean#L18), which takes part 1;
- `exists_logRes_subsingleton_cohOn_one` in [ExistsLogResolutionLocalVanishing.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsLogResolutionLocalVanishing.lean#L18), which takes part 2 over $\mathbb{C}$.

The name speaks of a multiplier ideal, a nef twist and an ample bundle. The statement has no multiplier ideal: it has the sheaf $s_*\mathcal{O}_Y(-F)$, which is a multiplier ideal twisted by $K_X$ only when $X$ is smooth.
