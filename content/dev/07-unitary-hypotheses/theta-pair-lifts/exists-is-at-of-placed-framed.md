---
id: exists-is-at-of-placed-framed
title: A matching translation element for a placed framed Bessel datum, in statement form
kind: theorem
decl: GlobalTheory.T.exists_isAt_of_placed_framed
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ExistsIsAtStatement
covers: 449
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`exists_isAt_alt`](/entry/exists-is-at-alt/). Its only user is [one central pin for all placed framed Bessel data](/entry/exists-bot-dat-pin-of-placed-of-framed/), which calls it twice: in step 1 for a reference datum, and in step 5 for each placed framed datum. The real content is in `exists_isAt_alt`.

## Statement

The statement is word for word the statement of [`exists_isAt_alt`](/entry/exists-is-at-alt/). Let $W$ be a real package over $D$ with `PackageHypotheses W`, $u$ a word, $f$ a family character and $\mathcal B$ a Bessel datum on $X_0$ that is placed for $f$ (`PlacedAlt f B`) and framed. Then there are $a_0, a \in G(X_0)$ with `IsTranslate' f B a₀ a`:

1. $a_0$ is a transport adelic correction for the weight of `W.S.tr u`;
2. $a \in G_f(X_0)$, and $a$ is central in $G(X_0)$;
3. the translation element $x_u^{-1}\, \iota_{\mathcal B}(a_0 a)\, f.g.b_0$ matches the level set $J$ = `rJ_z W` and the character `realCharacter W` (`Matches`).

The notation is that of [one central pin](/entry/exists-bot-dat-pin-of-placed-of-framed/).

## Proof

The proof applies `exists_isAt_alt`. Nothing else happens.

## In the Lean code

The theorem is at [ExistsIsAtStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsIsAtStatement.lean#L22). The proof is the tactic `first | exact @GlobalTheory.MiTop.exists_isAt_alt | ...`, so the theorem only passes its hypotheses along. `PlacedAlt`, `translationElement` and `IsTranslate'` are in [Placed.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/Placed.lean#L29). The proof of `exists_isAt_alt`, in [ExistsIsAt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsIsAt.lean#L32), takes $a_0$ from `exists_transport_adelic_correction` and $a$ from `exists_central_stab_of_transport_correction`. We have not unfolded `Matches`.
