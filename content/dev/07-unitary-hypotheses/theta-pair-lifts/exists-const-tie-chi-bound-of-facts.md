---
id: exists-const-tie-chi-bound-of-facts
title: The extra conditions from the norm choice facts, restated
kind: theorem
decl: GlobalTheory.T.exists_const_tieChi_bound_of_facts
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.ExtraBoundOfTwistingEigenFacts
covers: 3712
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It has the same statement as [the extra conditions from the facts](/entry/extra-from-facts-main-alt-alt/), and its proof only cites that theorem. Its user is [the link from good twists and the Galois preconditions](/entry/link-n-of-tw-good-galois-preconditions/). The content is there.

## Statement

**Theorem.** Assume the seven hypotheses $\mathrm{Hyp}_2$. Then there are a real $C \ge 0$ and an integer $C_T$ such that for each datum $D$ and norm choice $n$ the following holds. Suppose that the norm choice facts hold for $D$ and $n$, and that four further conditions hold: the tie condition on $\chi$, the existence of a datum $Q$ that is admissible and whose eigenvectors span, a polynomial tie inequality, and a local Selmer condition. Then $D$ satisfies the two extra conditions with $C$ and $C_T$:

1. at each twisted index $i$ with $\ell_i \notin \{g_0, g_1\}$, there is an endomorphism of $M_i$ that commutes with the Hecke algebra $T_i$ and acts by a fixed integer on Hecke eigenvectors at good points and by $0$ at the other points of $Z_i$;
2. the paired character condition with $C$ and $C_T$, a bound at the special primes $g_k$, stated in that entry.

We have not unfolded the four further conditions.

## Proof

The proof is the term `ExtraFromFacts.main_alt_alt`. There is nothing else.

## In the Lean code

The theorem is in [ExtraBoundOfTwistingEigenFacts.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExtraBoundOfTwistingEigenFacts.lean#L12). The proof is `first | exact @ExtraFromFacts.main_alt_alt | ...`, a tactic that tries three ways to apply the other theorem. The two statements are the same word for word.

The name says "tieChi bound", but the tie condition on $\chi$ is a hypothesis, not the conclusion. The conclusion is `NLink.ExtraAlt`.
